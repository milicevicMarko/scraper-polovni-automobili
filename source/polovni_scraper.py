from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

import pandas as pd
from datetime import datetime

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


def extract_basic_info_section(section):
    grid_items = section.find_all('div', class_='divider')

    def _key(item): return str(
        item.find('div', class_='uk-width-1-2').get_text(strip=True)).lower()
    def _value(item): return str(
        item.find('div', class_='uk-width-1-2 uk-text-bold').get_text(strip=True)).lower()

    return {_key(item): _value(item) for item in grid_items}


def extract_grid_listing(section):
    grid_items = section.find_all(
        'div', class_='uk-width-medium-1-4 uk-width-1-2 uk-margin-small-bottom')
    return {str(item.get_text(strip=True)).lower(): True for item in grid_items}


def extract_description(section):
    description = section.find(
        'div', class_='uk-width-1-1 description-wrapper')
    return {'opis': description.get_text(separator='\n', strip=True) if description else ''}


SECTION_EXTRACTION_RULES = {
    'Opšte informacije': extract_basic_info_section,
    'Dodatne informacije': extract_grid_listing,
    'Sigurnost': extract_grid_listing,
    'Oprema': extract_grid_listing,
    'Stanje': extract_grid_listing,
    'Opis': extract_description,
}


def extract_basic_info(soup: BeautifulSoup):
    section_info = soup.find('section', class_='js_fixedContetLoad')

    section_name = section_info.find('h2').get_text(strip=True)
    if section_name in SECTION_EXTRACTION_RULES:
        return SECTION_EXTRACTION_RULES[section_name](section_info)
    else:
        print('Basic info (Opste informacije) section not found')
        return {}


def extract_other_info(soup: BeautifulSoup):
    main_section = soup.find(
        'div', class_='js-tab-classified-content classified-content')

    result = {}

    if main_section is None:
        print("Failed to find main section")
    else:
        sections = main_section.find_all('section', recursive=False)
        for section in sections:
            section_name = section.find('h2').get_text(strip=True)
            if section_name in SECTION_EXTRACTION_RULES:
                section_result = SECTION_EXTRACTION_RULES[section_name](
                    section)
                result.update(section_result)
            else:
                print('Unknown section: ', section_name)
    return result


def extract_information(soup: BeautifulSoup):
    bi_result = extract_basic_info(soup)
    oi_result = extract_other_info(soup)
    return {**bi_result, **oi_result}


def quit_selenium(driver):
    driver.quit()


def scrape_site(url):
    driver = init_selenium()
    page_source = load_url(driver, url)
    source = cook_soup(page_source)
    result_json = extract_information(source)
    quit_selenium(driver)
    return result_json


def run_scrape(url):
    result_json = scrape_site(url)
    result = pd.DataFrame([result_json])
    return result


if __name__ == '__main__':
    timestamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    url = 'https://www.polovniautomobili.com/auto-oglasi/25181599/volkswagen-golf-8-20dstyleled?attp=p1_pv0_pc1_pl1_plv0'
    run_scrape(url).to_json(
        f'results/result-{timestamp}.json', orient='records', force_ascii=False)
    print('Scraping done')
