# OutLog Distribox — Preview de interface

Esqueleto simples pra visualizar como pode ficar a tela unificada, juntando:

- o quadro por setor (Recebimento → Qualidade → Processamento → Estocagem) do app do Jonas (Controle Logística)
- o conceito de posição real de casulo do app do colega (Distribox)

Ainda **sem banco de dados** — os cards e casulos aqui são dados de exemplo
(mock), só pra dar noção visual. A ideia é usar isso como ponto de partida
pra depois plugar a API de verdade.

## Rodar localmente

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate   # Linux/Mac

pip install -r requirements.txt
uvicorn main:app --reload
```

Depois acesse `http://127.0.0.1:8000`.

## Estrutura

```
main.py              FastAPI + dados de exemplo
templates/index.html  Tela única com quadro por setor + visualizador de casulos
static/style.css      Estilo (tema escuro)
requirements.txt
```

## Próximos passos (não feitos ainda de propósito, pra ficar simples)

- Trocar os dados de exemplo por consulta real ao banco (Postgres)
- Trazer os módulos reais do Controle Logística (`quality_module.py`,
  `processing_module.py`, `downstream_module.py`)
- Trazer a estrutura física real de casulos (`ESTRUTURA_CD`) no lugar do
  mock da Rua 09
- Autenticação de usuários
