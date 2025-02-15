from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

WAIT_FOR_ELEMENT_TIMEOUT = 10


def init_selenium():
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    return webdriver.Chrome(options=options)


def load_url(driver, url):
    driver.get(url)

    WebDriverWait(driver, WAIT_FOR_ELEMENT_TIMEOUT).until(
        lambda d: d.execute_script('return document.readyState') == 'complete'
    )
    return driver.page_source


def cook_soup(page_source) -> BeautifulSoup:
    return BeautifulSoup(page_source, 'html.parser')


def extract_description(section):
    print(section.get_text(strip=True))


def unkown_handler(section):
    print("Unknown section")


SECTION_EXTRACTION_RULES = {
    'Dodatne informacije': extract_description,
    'Sigurnost': extract_description,
    'Oprema': extract_description,
    'Stanje': extract_description,
    'Opis': extract_description,
}


def extract_information(soup: BeautifulSoup):
    main_section = soup.find(
        'div', class_='js-tab-classified-content classified-content')
    if main_section is None:
        print("Failed to find main section")
    else:
        print("Found main section")
        sections = main_section.find_all('section', recursive=False)
        # sections_names = [section.find('h2').get_text(strip=True)
        #                   for section in sections]

        for section in sections:
            section_name = section.find('h2').get_text(strip=True)
            if section_name in SECTION_EXTRACTION_RULES:
                SECTION_EXTRACTION_RULES[section_name](section)
            else:
                print('Unknown section: ', section_name)


def quit_selenium(driver):
    driver.quit()


def scrape_site(url):
    driver = init_selenium()

    extract_information(cook_soup(load_url(driver, url)))

    quit_selenium(driver)


def run():
    scrape_site(
        'https://www.polovniautomobili.com/auto-oglasi/25181599/volkswagen-golf-8-20dstyleled?attp=p1_pv0_pc1_pl1_plv0')


if __name__ == '__main__':
    run()

# /html/body/div[5]/div[1]/div[2]/div/div[3]
# document.querySelector("#classified-content > div.uk-width-1-1 > div")
