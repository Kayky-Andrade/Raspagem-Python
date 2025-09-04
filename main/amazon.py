import json
from playwright.sync_api import sync_playwright

BASE_URL = "https://www.amazon.com.br/s?k=Belmicro"

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        viewport={"width": 1280, "height": 800},
    )
    page = context.new_page()
    print("[INFO] Acessando página...")
    page.goto(BASE_URL, timeout=60000)

    page.wait_for_selector('div.s-main-slot', timeout=15000)
    print("[INFO] Página carregada, buscando produtos...")

    product_cards = page.query_selector_all('div.s-main-slot div[data-asin]:not([data-asin=""])')
    print(f"[INFO] Total de blocos com data-asin: {len(product_cards)}")

    products = []
    for i, card in enumerate(product_cards, 1):
        asin = card.get_attribute('data-asin')
        if not asin:
            print(f"[SKIP] Produto {i} ignorado (ASIN vazio).")
            continue

        # Busca título do produto
        name_el = card.query_selector('div[data-cy="title-recipe"] a')
        if not name_el:
            name_el = card.query_selector('h2 a')
        name = name_el.inner_text().strip() if name_el else None

        if not name:
            print(f"[SKIP] Produto {i} ignorado (sem nome).")
            continue

        # Busca preço
        price_el = card.query_selector('span.a-price > span.a-offscreen')
        price = price_el.inner_text().strip() if price_el else None

        # URL do produto
        link = "https://www.amazon.com.br" + name_el.get_attribute('href') if name_el else None

        print(f"[OK] Produto {i}: {name} - Preço: {price}")

        products.append({
            "asin": asin,
            "name": name,
            "price": price,
            "url": link,
        })

    print(f"[INFO] Total de produtos válidos encontrados: {len(products)}")

    with open("amazon_data.json", "w", encoding="utf-8") as f:
        json.dump(products, f, indent=4, ensure_ascii=False)

    browser.close()

with sync_playwright() as playwright:
    run(playwright)

