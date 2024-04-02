from playwright.sync_api import sync_playwright, BrowserContext

def get_datalayer(ctx: BrowserContext, url: str):
    page = ctx.new_page()
    page.goto(url)
    page.wait_for_load_state("networkidle")
    return page.evaluate("window.dataLayer")


with sync_playwright() as p:
    browser = p.chromium.launch()
    with browser.new_context() as bcon:
        data_layer = get_datalayer(bcon, "https://www.tayara.tn/item/65ff301a7403ad20d850bdab/Autres%20V%C3%A9hicules/Zaghouan/El_Fahs/iphone_12_pro_/")
        print(data_layer)