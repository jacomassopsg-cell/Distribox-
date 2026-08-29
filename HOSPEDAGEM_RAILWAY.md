# Hospedagem rápida no Railway

O repositório já contém `Dockerfile` e `railway.toml`.

1. Entre em https://railway.com e escolha **New Project**.
2. Selecione **Deploy from GitHub repo**.
3. Escolha `jonasloro/Distribox-`.
4. Aguarde a primeira implantação.
5. No serviço, abra **Settings → Networking → Generate Domain**.
6. Em **Volumes**, crie um volume com o caminho `/app/data`.

O volume preserva o banco SQLite e os uploads entre novas implantações.

## Configuração já aplicada

- servidor: `uvicorn app:app`;
- endereço: `0.0.0.0`;
- porta: variável automática `$PORT` do Railway;
- dados persistentes: `OUTLOG_DATA_DIR=/app/data`;
- verificação de saúde: `/`.

Após gerar o domínio, o Railway exibirá uma URL pública terminada em `.up.railway.app`.

