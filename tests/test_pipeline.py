import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("pipeline", Path(__file__).parents[1] / "scripts/fetch_nasa.py")
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)


class PipelineTests(unittest.TestCase):
    def row(self):
        return ["id-1", "CODE", '<span class="highlight">Engine</span> &amp; power', "Descrição", "CODE", "Sensors", "", "", "", "GRC"]

    def test_dedup_html_and_missing_fields(self):
        rows, errors = p.normalize([self.row(), self.row(), []], "engine")
        self.assertEqual(len(rows), 1)
        self.assertEqual(errors, 1)
        self.assertEqual(rows[0]["titulo"], "Engine & power")
        self.assertIsNone(rows[0]["inventor"])
        self.assertIsNone(rows[0]["status_licenciamento"])

    def test_truncated_response_fails(self):
        with patch.object(p, "request_json", return_value={"results": [self.row()], "total": 2}):
            with self.assertRaises(ValueError):
                p.collect("engine")

    def test_partial_failure_logs_and_exits_nonzero(self):
        saved = []
        def request(url, headers, body):
            if "execucoes" in url:
                saved.append(dict(body))
            elif len(body) == 1:
                raise RuntimeError("simulated failure")
        rows = [{"nasa_id": str(i)} for i in range(101)]
        with patch.dict(p.os.environ, {"SUPABASE_URL": "https://example.supabase.co", "SUPABASE_SERVICE_KEY": "test", "NASA_SEARCH_TERM": "engine"}), patch.object(p, "collect", return_value=(rows, 0)), patch.object(p, "request_json", side_effect=request):
            self.assertEqual(p.main([]), 1)
        self.assertEqual(saved[0]["status"], "erro_parcial")
        self.assertEqual(saved[0]["registros_processados"], 100)
        self.assertEqual(saved[0]["lotes"], 1)

    def test_log_failure_never_reports_success(self):
        def request(url, headers, body):
            if "execucoes" in url:
                raise RuntimeError("unavailable")
        with patch.dict(p.os.environ, {"SUPABASE_URL": "https://example.supabase.co", "SUPABASE_SERVICE_KEY": "test", "NASA_SEARCH_TERM": "engine"}), patch.object(p, "collect", return_value=([{"nasa_id": "1"}], 0)), patch.object(p, "request_json", side_effect=request):
            self.assertEqual(p.main([]), 1)


if __name__ == "__main__":
    unittest.main()

