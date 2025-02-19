from pathlib import Path
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd
import argparse

from source.read_existing import import_file


def visualize(data_source):
    df = import_file(Path(data_source))

    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_default_column(
        resizable=True, sortable=True, filterable=True, hideable=True, editable=True)
    gb.configure_grid_options(domLayout='1000px')
    gb.configure_side_bar(filters_panel=False)
    grid_options = gb.build()

    st.title("Scraped Data from Polovni Automobili")
    st.subheader(f"Showing data from: {data_source}")
    AgGrid(df, gridOptions=grid_options,
           enable_enterprise_modules=True, width=1000, height=1000)


def main():
    parser = argparse.ArgumentParser(description='Visualize scraped data.')
    parser.add_argument('data_source', type=str,
                        help='Path to the data source file')
    args = parser.parse_args()

    visualize(args.data_source)


if __name__ == '__main__':
    main()
