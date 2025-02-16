from source import *


def main():
    input_df, output_name, type, url = command_line()
    scraped_df = run_scrape(url)
    result = append_data(input_df, scraped_df)
    export_file(result, output_name, type)


if __name__ == '__main__':
    main()


# python main.py --o testing --t excel --url 'https://www.polovniautomobili.com/auto-oglasi/25181599/volkswagen-golf-8-20dstyleled?attp=p1_pv0_pc1_pl1_plv0'
# python main.py --a results/testing.xlsx --url 'https://www.polovniautomobili.com/auto-oglasi/25829255/volkswagen-golf-8-styleiqmasazamt6?attp=p1_pv0_pc1_pl1_plv0'
