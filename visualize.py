import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd


def visualize(data_source):
    df = pd.read_excel(data_source)

    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_default_column(
        resizable=True, sortable=True, filterable=True, hideable=True, editable=True)
    gb.configure_grid_options(domLayout='1000px')
    gb.configure_side_bar(filters_panel=False)
    grid_options = gb.build()

    st.title("Scraped Data from Polovni Automobili")
    st.subheader(f"Showing data from: {data_source}")
    AgGrid(df, gridOptions=grid_options,
           enable_enterprise_modules=True, width=1400, height=600)


if __name__ == '__main__':
    visualize('results/testing.xlsx')
