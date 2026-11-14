-- Execute no SQL Editor do projeto TechTransfer-Patents-DB.
begin;
create table if not exists public.patentes (
  id bigint generated always as identity primary key,
  nasa_id text not null unique,
  codigo text not null,
  titulo text not null,
  descricao text,
  categoria text,
  centro text,
  inventor text,
  status_licenciamento text,
  termo_busca text not null,
  fonte text not null,
  atualizado_em timestamptz not null default now()
);
create table if not exists public.execucoes (
  id uuid primary key,
  iniciado_em timestamptz not null,
  finalizado_em timestamptz not null,
  registros_processados integer not null check (registros_processados >= 0),
  lotes integer not null check (lotes >= 0),
  erros integer not null check (erros >= 0),
  status text not null check (status in ('concluido', 'erro_parcial', 'erro_critico')),
  mensagem text,
  termo_busca text not null
);
create index if not exists execucoes_finalizado_idx on public.execucoes (finalizado_em desc);
alter table public.patentes enable row level security;
alter table public.execucoes enable row level security;
drop policy if exists leitura_publica on public.patentes;
create policy leitura_publica on public.patentes for select to anon, authenticated using (true);
drop policy if exists leitura_publica on public.execucoes;
create policy leitura_publica on public.execucoes for select to anon, authenticated using (true);
revoke all on public.patentes, public.execucoes from anon, authenticated;
grant usage on schema public to anon, authenticated, service_role;
grant select on public.patentes, public.execucoes to anon, authenticated;
grant all on public.patentes, public.execucoes to service_role;
grant usage, select on sequence public.patentes_id_seq to service_role;
commit;

