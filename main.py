from source import *


def main():
    input_df, output_name, type, urls = command_line()
    scraped_df = run_scrape(urls)
    result = append_data(input_df, scraped_df)
    export_file(result, output_name, type)


if __name__ == '__main__':
    main()
