from pathlib import Path

import polars as pl
import streamlit as st

import scripts.script_functions as functs


def get_dirs() -> Path:
    parent_dir = Path(__file__).parent.parent
    dataframe_dir = parent_dir / "Dataframes"
    return dataframe_dir


def load_dta(dataframe_dir) -> pl.DataFrame:
    return pl.read_parquet((dataframe_dir / "combined_non_oil_company_dta.parquet"))


def main() -> None:
    page_title = "Dictionary Terms"
    functs.set_page_configs(page_title)

    dictionary_dicts = functs.create_dictionary_dicts()
    for dictionary_name, dictionary_dict in dictionary_dicts.items():
        st.write(
            f"### {dictionary_dict['label']} ({dictionary_name}) dictionary:\ndictionary terms: {', '.join(dictionary_dict['terms'])}"
        )
    st.sidebar.write(functs.print_updated_time())  # PROGRESSTRACKING:
    print(functs.print_updated_time())  # PROGRESSTRACKING:


main()
