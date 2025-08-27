## Chatbot + Web Scraping com Playwright (Python)

Projeto acadêmico (uso interno do grupo): Chatbot que utiliza raspagem (web scraping) como uma das etapas do pipeline para coletar dados de um site. Este README explica o que o projeto faz, como rodar e documenta linha por linha o script de scraping.

# 🔎 Visão Geral

Objetivo: Demonstrar a coleta automatizada de dados (ex.: usuário, nome, links) a partir de um site.
Stack: Python + Playwright (API síncrona).
Saída: Um arquivo data.txt contendo os dados extraídos em JSON.
Uso no Chatbot: As informações coletadas podem alimentar a base de conhecimento/intent do chatbot ou compor respostas.

# 🧩 Arquitetura do Trabalho (Visão Macro)
Usuário → Chatbot → (Consulta) → Base local/Arquivo JSON ← (Atualiza) ← Scraper Playwright

1 - O scraper visita o site desenvolvido pelo grupo e extrai dados relevantes.

2 - Os dados são salvos como JSON em data.txt.

3 - O chatbot consulta esse JSON para responder perguntas.

# ✅ Pré‑requisitos

Python 3.9+ (Baixar pelo navegador)

pip (gerenciador de pacotes do Python)

Dependências Python:

 playwright

No primeiro uso do Playwright, é preciso instalar os browsers que ele controla.

# ⚙️ Instalação (passo a passo)

1) Instale as dependências

pip install playwright

2) Baixe os navegadores do Playwright
 
python -m playwright install

▶️ Como Executar a Raspagem

Coloque o arquivo do script (ex.: one.py) no diretório do projeto e rode:

python one.py

Saída esperada: criação/atualização de um arquivo data.json com JSON contendo os dados coletados do site.

🗂️ Estrutura Sugerida de Pastas

│  README.md

│  scraper.py         

└─ data.json
