"""
OutLog Distribox — preview de interface unificada.

Este arquivo é só uma casca simples: mostra em uma única tela o conceito de
juntar os dois sistemas (fluxo por setores do "Controle Logística" +
estrutura física de casulos do "Distribox"), com dados de exemplo (mock),
sem banco de dados ainda. Serve pra visualizar como a interface pode ficar
antes de entrar na parte pesada (API real, Postgres, autenticação etc).
"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="OutLog Distribox - Preview")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# ---------------------------------------------------------------------------
# Dados de exemplo (mock) — representam a fusão dos dois conceitos:
# "Card" migrando por setor (Controle Logística) + posição real de casulo
# (Distribox). Isso tudo vai virar consulta real ao banco depois.
# ---------------------------------------------------------------------------

SETORES = ["Recebimento", "Qualidade", "Processamento", "Estocagem"]

CARDS = [
    {
        "id": 1,
        "produto": "Regata Aurean - Grade",
        "referencia": "AUR-2201",
        "setor": "Recebimento",
        "status": "Aguardando recebimento",
        "quantidade": 240,
        "casulo": None,
    },
    {
        "id": 2,
        "produto": "Bermuda Saldo",
        "referencia": "BER-1187",
        "setor": "Qualidade",
        "status": "Em inspeção",
        "quantidade": 96,
        "casulo": None,
    },
    {
        "id": 3,
        "produto": "Camiseta Basic - Grade",
        "referencia": "CAM-0532",
        "setor": "Processamento",
        "status": "Em processamento",
        "quantidade": 180,
        "casulo": None,
    },
    {
        "id": 4,
        "produto": "Jaqueta Corta-Vento",
        "referencia": "JAQ-0410",
        "setor": "Estocagem",
        "status": "Estocado",
        "quantidade": 40,
        "casulo": "Rua 09 - Col. 114 (M)",
    },
    {
        "id": 5,
        "produto": "Vestido Longo",
        "referencia": "VES-0287",
        "setor": "Estocagem",
        "status": "Estocado",
        "quantidade": 18,
        "casulo": "Rua 04 - Col. 108 (G)",
    },
]

# Estrutura física simplificada só pra dar noção visual do Visualizador de
# Casulos (na versão real, vem do ESTRUTURA_CD + API ID Brasil)
CASULOS_RUA_09 = [
    {"coluna": 111, "tipo": "M", "ocupacao": 6, "capacidade": 12},
    {"coluna": 112, "tipo": "M", "ocupacao": 12, "capacidade": 12},
    {"coluna": 113, "tipo": "M", "ocupacao": 0, "capacidade": 12},
    {"coluna": 114, "tipo": "M", "ocupacao": 10, "capacidade": 12},
    {"coluna": 115, "tipo": "M", "ocupacao": 4, "capacidade": 12},
]


def cards_por_setor():
    return {setor: [c for c in CARDS if c["setor"] == setor] for setor in SETORES}


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "setores": SETORES,
            "cards_por_setor": cards_por_setor(),
            "casulos": CASULOS_RUA_09,
        },
    )


@app.get("/api/cards")
async def listar_cards():
    return CARDS
