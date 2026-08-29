# Correção V3.1 — interface antiga aparecendo

Foram identificadas duas situações capazes de fazer a V3 parecer igual à versão anterior:

1. o navegador reutilizava `app.js` e `style.css` da porta 8000;
2. uma V2 ainda aberta podia continuar ocupando a porta 8000, impedindo a V3 de iniciar.

## Correções

- arquivos visuais agora possuem versão explícita `3.1.0` na URL;
- respostas da interface recebem instrução para não usar cache antigo;
- a V3.1 abre exclusivamente em `http://127.0.0.1:8010`;
- o servidor antigo na porta 8000 não precisa ser encerrado para testar esta versão.

Ao abrir a V3.1, confirme que o endereço exibido no navegador termina em `:8010`.

