import json         # Importa o módulo padrão para trabalhar com JSON (serialização/deserialização)
from playwright.sync_api import sync_playwright     # Importa a API síncrona do Playwright para controlar o navegador

BASE_URL = 'https://github.com/topics/playwright'   # URL base do site 

def run(playwright):                                         # Define a função principal que receberá o objeto Playwright já inicializado
    browser = playwright.chromium.launch(headless=False)     # Abre o Chromium. headless=False = janela visível (útil para depuração)

    context = browser.new_context(                  # Cria um novo contexto (perfil isolado: cookies, cache, etc.)
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        viewport={"width": 800, "height": 600},     # Ajusta o tamanho da janela/viewport
        bypass_csp=True,                            # Ignora CSP (Content Security Policy) se houver
    )

    page = context.new_page()           # Abre uma nova aba/página dentro do contexto
    page.goto(BASE_URL)                 # Navega até a URL alvo (substitua pelo site do grupo)
    page.wait_for_selector("article")   # Aguarda a existência de ao menos um <article> (ajuste para o seletor do seu site)

    repo_cards = page.query_selector_all("article")     # Seleciona todos os elementos (ajuste para a estrutura do site)
    print("Cards encontrados:", len(repo_cards))        # Loga a quantidade encontrada
    repositories = []                                   # Lista que irá acumular os dicionários com dados extraídos
    for card in repo_cards:                             # Itera por cada card
        user, repo = card.query_selector_all("h3 a")    # Ajustar de acordo com os elementos presentes no site
        format_text = lambda element: element.inner_text().strip() if element else None     # Função compacta para pegar texto limpo
        

        repository = {
         "user": format_text(user),         # Campo 1: texto do elemento alvo
         "repo": format_text(repo),         # Campo 2: outro texto alvo
         "url": repo.get_attribute("href"), # Campo 3: link (relativo ou absoluto)
}
        repositories.append(repository)     # Adiciona o dicionário à lista principal

    print(repositories)                                                     # Exibe a lista final no console
    json_data = json.dumps(repositories, indent=4, ensure_ascii=False)      # Converte para JSON formatado

    with open("data.json", "w") as file:                    # Abre (ou cria) o arquivo de saída
     file.write(json_data)                                  # Escreve o JSON dentro de data.json

    browser.close()                     # Fecha o navegador
    
with sync_playwright() as playwright:   # Inicia o Playwright
     run(playwright)                    # Chama a função principal