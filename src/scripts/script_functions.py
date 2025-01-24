from pathlib import Path

import plotly.express as px
import polars as pl
import streamlit as st


def set_page_configs(page_title) -> None:
    """
    Configures the Streamlit page settings.

    This function sets the layout to wide, the page title to "Basic Descriptive Graphs",
    and the initial sidebar state to expanded. Additionally, it hides the Streamlit
    main menu and footer for a cleaner interface.

    Returns:
        None
    """
    # can only set this once, first thing to set
    st.set_page_config(
        layout="wide",
        initial_sidebar_state="expanded",
    )
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def print_updated_time():
    """
    Returns the current time formatted as a string indicating the last update time.

    This function retrieves the current system time, formats it to a string in the
    format "HH:MM:SS", and returns a message indicating the last update time.

    Returns:
        str: A string message indicating the last update time in the format "App last updated at HH:MM:SS".
    """
    from datetime import datetime

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return f"App last updated at {current_time}"


def create_dictionary_dicts():
    """
    Creates a dictionary containing multiple dictionaries, each representing a specific category
    with associated terms and their corresponding color codes.

    Returns:
        dict: A dictionary where keys are category names and values are dictionaries with
              'label' and 'terms'. 'label' is a string describing the category, and 'terms'
              is a dictionary where keys are terms (or term patterns) and values are color codes.
    """
    dictionary_dicts = {
        "climate_change": {
            "Climate Change Dictionary": "climate_change",  # to get name easier
            "label": "Climate Change Dictionary",
            "terms": {
                "climate change": "#c97a55",
                # "net-zero": "#827cde",
                "net zero": "#a08e33",
                "greenhouse gas": "#9f479a",
                "GHG": "#9b341e",
                "scope 1": "#0178af",
                "scope 2": "#bb7aa3",
                "scope 3": "#903646",
                # "climate change": "#006d09", # old terms from former dictionary
                # "global warming": "#bc1055", # old terms from former dictionary
                # "greenhouse gas": "#0b913e", # old terms from former dictionary
                # "methane": "#c66509", # old terms from former dictionary
                # "emission": "#990099", # old terms from former dictionary
            },
        },
        "sustainability|exploitation": {
            "Sustainability|Exploitation Dictionary": "sustainability|exploitation",  # to get name easier
            "label": "Sustainability|Exploitation Dictionary",
            "terms": {
                # sustainability cool
                "sustain|sustainability": "#00FF00",
                "vegan": "#0000FF",
                "climate change": "#006d09",
                "environment": "#808000",
                "land use": "#008000",
                "water use": "#800080",
                "growing population": "#008080",
                "supply chain": "#000080",
                # exploitation warm
                "exploit|exploitation": "#FF0000",
                "process|processed": "#aa0000",
                "product|production|produce": "#999900",
                "kill": "#800000",
                "slaughter": "#4d0000",
                "butcher": "#aa0000",
            },
        },
        "prosocial": {
            "Prosocial Dictionary": "prosocial",  # to get name easier
            "label": "Prosocial Dictionary",
            "terms": {
                "donate|donation": "#00FF00",
                "share|sharing": "#0000FF",
                "volunteer|volunteering": "#00FFFF",
                "honor": "#808000",
                "award": "#008000",
                "support": "#800080",
                "pledge": "#008080",
                "generosity|generos": "#000080",
                "compassion": "#FF0000",
                "community|communities": "#FFFF00",
                "contribut": "#FF00FF",
            },
        },
        "health_general": {
            "General Health Dictionary": "health_general",  # to get name easier
            "label": "General Health Dictionary",
            "terms": {
                "health": "#00FF00",
                "public health": "#0000FF",
                "antibiotic|prebiotic": "#00FFFF",
                "nutrition|nutritious|nutrient": "#808000",
                "hygiene": "#008000",
                "safe|safety": "#800080",
                "wellness": "#008080",
                "health safety": "#000080",
                "health expert|health research": "#FF0000",
                "health outcome|health benefits|health care|health clinic|health support|health service": "#FFFF00",
                "health department|health official|health inspection": "#FF00FF",
                "diet": "#800000",
                "heath product": "#FF8C00",
                "animal health|herd health|healthy cattle": "#aa0000",
            },
        },
        "health_human": {
            "Human Health Dictionary": "health_human",  # to get name easier
            "label": "Human Health Dictionary",
            "terms": {
                "human health": "#00FF00",
                "public health": "#0000FF",
                "antibiotic|prebiotic": "#00FFFF",
                "nutrition|nutritious|nutrient": "#808000",
                "hygiene": "#008000",
                "safe|safety": "#800080",
                "wellness": "#008080",
                "health safety": "#000080",
                "health expert|health research": "#FF0000",
                "health outcome|health benefits|health care|health clinic|health support|health service": "#FFFF00",
                "health department|health official|health inspection": "#FF00FF",
                "diet": "#800000",
                "heath product": "#FF8C00",
            },
        },
    }
    return dictionary_dicts


def select_dictionary(dictionary_dicts):
    dict_keys = [dictionary_dict for dictionary_dict in dictionary_dicts.keys()]
    dict_labels = [dictionary_dict["label"] for dictionary_dict in dictionary_dicts.values()]
    dict_select = st.sidebar.selectbox(label="Select a dictionary:", options=dict_labels)
    dict_label = dict_select
    for dict_key_loop in dict_keys:
        if dictionary_dicts[dict_key_loop]["label"] == dict_select:
            dict_key = dict_key_loop
            dict_terms_colors = dictionary_dicts[dict_key]["terms"]
            dict_terms = dictionary_dicts[dict_key]["terms"].keys()
    # st.write(f"dict_key:\n{dict_key}\n\n")  # TEMPPRINT:
    # st.write(f"dict_label:\n{dict_label}\n\n")  # TEMPPRINT:
    # st.write(f"dict_terms:\n{dict_terms}\n\n")  # TEMPPRINT:
    # st.write(f"dict_terms_colors:\n{dict_terms_colors}\n\n")  # TEMPPRINT:
    return dict_key, dict_label, dict_terms, dict_terms_colors


def get_dict_term_count(dta: pl.DataFrame, dict_terms: list[str]) -> tuple[pl.DataFrame, list[str]]:
    """
    Calculate the count of dictionary terms in the 'text' column of the given DataFrame.

    This function performs the following steps:
    1. Converts the text in the 'text' column to lowercase.
    2. Counts the occurrences of each dictionary term in the 'text' column.
    3. Renames the count column to 'term_count'.
    4. Drops the intermediate 'term_count' column.

    Args:
        dta (pl.DataFrame): A Polars DataFrame containing a 'text' column with text data.
        dict_terms (list[str]): A list of dictionary terms to count in the text data.

    Returns:
        pl.DataFrame: A Polars DataFrame with an additional 'term_count' column representing the count of
                     dictionary terms in each row.
    """
    for term in dict_terms:
        target_term = term.lower()
        dta = dta.with_columns(
            pl.col("clean_text")
            .str.count_matches(target_term)
            .cast(pl.Int32)
            .alias(f"{term}_count")
            # pl.col("clean_text").str.contains(target_term).cast(pl.Int32).alias(f"{term}_count")
        )
    # st.write(dta)  # TEMPPRINT:
    term_col_names = [f"{term}_count" for term in dict_terms]
    # st.write(term_col_names)  # TEMPPRINT:
    return dta, term_col_names


def get_term_count(dta: pl.DataFrame, term: str) -> tuple[pl.DataFrame, list[str]]:
    """
    Calculate the count of dictionary terms in the 'text' column of the given DataFrame.

    This function performs the following steps:
    1. Converts the text in the 'text' column to lowercase.
    2. Counts the occurrences of each dictionary term in the 'text' column.
    3. Renames the count column to 'term_count'.
    4. Drops the intermediate 'term_count' column.

    Args:
        dta (pl.DataFrame): A Polars DataFrame containing a 'text' column with text data.
        dict_terms (list[str]): A list of dictionary terms to count in the text data.

    Returns:
        pl.DataFrame: A Polars DataFrame with an additional 'term_count' column representing the count of
                     dictionary terms in each row.
    """
    if "," in term:
        target_terms = term.split(",")
    else:
        target_terms = [term]
    for term in target_terms:
        target_term = term.lower()
        dta = dta.with_columns(
            pl.col("clean_text")
            .str.count_matches(target_term)
            .cast(pl.Int32)
            .alias(f"{term}_count")
            # pl.col("clean_text").str.contains(target_term).cast(pl.Int32).alias(f"{term}_count")
        )
    # st.write(dta)  # TEMPPRINT:
    term_col_names = [f"{term}_count" for term in target_terms]
    # st.write(term_col_names)  # TEMPPRINT:
    return dta, term_col_names


def load_dta():
    def get_dirs() -> Path:
        parent_dir = Path(__file__).parent.parent
        dataframe_dir = parent_dir / "Dataframes"
        return dataframe_dir

    def load_dta_path(dataframe_dir) -> pl.DataFrame:
        return pl.read_parquet((dataframe_dir / "combined_non_oil_company_dta.parquet"))

    def remove_missing_values(dta: pl.DataFrame) -> pl.DataFrame:
        return dta.drop_nulls()

    def get_year_month_column(dta: pl.DataFrame) -> pl.DataFrame:
        dta = dta.with_columns(pl.col("date").dt.strftime("%Y-%m").alias("year_month"))
        dta = dta.with_columns(
            pl.col("date").dt.strftime("%Y-%m").str.to_date(format="%Y-%m").alias("year_month_dt")
        )
        dta = dta.with_columns(pl.col("date").dt.year().cast(pl.Utf8).alias("year"))
        dta = dta.with_columns(pl.col("date").dt.month().cast(pl.Utf8).alias("month"))
        return dta
        # return dta.with_columns(pl.col("date").dt.strftime("%Y-%m").alias("year_month").sort())

    dataframe_dir = get_dirs()
    dta = load_dta_path(dataframe_dir)
    dta = remove_missing_values(dta)
    dta = get_year_month_column(dta)
    return dta


def get_year_selection_filter_bar(dta: pl.DataFrame):
    """
    Filters the given DataFrame based on a year range selected by the user through Streamlit sliders.

    Args:
        dta (pl.DataFrame): The input DataFrame containing a 'year' column.

    Returns:
        pl.DataFrame: The filtered DataFrame with rows where the 'year' column is within the selected range.

    Notes:
        - The 'year' column in the input DataFrame is cast to an integer type for filtering.
        - Two Streamlit sliders are used to select the start and end years for the filter.
        - If the start year is greater than the end year, an error message is displayed.
    """
    dta = dta.with_columns(pl.col("year").cast(pl.Int32).alias("year_int"))
    min_value = dta.select(pl.min("year_int")).item()
    max_value = dta.select(pl.max("year_int")).item()
    start_year = st.sidebar.slider(
        "Select Start Year for Included Data:",
        min_value=min_value,
        max_value=max_value,
        value=min_value,
    )
    end_year = st.sidebar.slider(
        "Select End Year for Included Data:",
        min_value=start_year,
        max_value=max_value,
        value=max_value,
    )
    if start_year > end_year:
        st.error("Start year must be less than end year.")
    else:
        dta = dta.filter(pl.col("year_int").is_between(start_year, end_year))
    return dta


def get_article_word_count(dta: pl.DataFrame) -> pl.DataFrame:
    """
    Calculate the word count for each row in the 'text' column of the given DataFrame.
    This function performs the following steps:
    1. Converts the text in the 'text' column to lowercase.
    2. Removes all non-alphanumeric characters except spaces.
    3. Replaces all non-word characters with spaces.
    4. Replaces newline characters with spaces.
    5. Replaces multiple spaces with a single space.
    6. Strips leading and trailing spaces.
    7. Splits the cleaned text into a list of words.
    8. Calculates the length of the word list (i.e., the word count).
    9. Drops the intermediate 'word_list' column.
    Args:
        dta (pl.DataFrame): A Polars DataFrame containing a 'text' column with text data.
    Returns:
        pl.DataFrame: A Polars DataFrame with an additional 'word_count' column representing the word count for each row.
    """
    regex_pattern = r"[^A-Za-z0-9 ]+"
    dta = dta.with_columns(pl.col("text").str.to_lowercase().alias("clean_text"))
    dta = dta.with_columns(pl.col("clean_text").str.replace_all(regex_pattern, " "))
    dta = dta.with_columns(pl.col("clean_text").str.replace_all(r"\W", " "))
    dta = dta.with_columns(pl.col("clean_text").str.replace_all(r"\n", " "))
    dta = dta.with_columns(pl.col("clean_text").str.replace_all(r" +", " "))
    dta = dta.with_columns(pl.col("clean_text").str.strip_chars())
    dta = dta.with_columns((pl.col("clean_text").str.split(" ")).alias("word_list"))
    dta = dta.with_columns((pl.col("word_list").list.len()).alias("word_count"))
    dta = dta.drop("word_list")
    return dta


def get_word_count_by_month_by_company(dta: pl.DataFrame) -> pl.DataFrame:
    dta_count_month = dta.group_by(pl.col("year_month")).agg([pl.sum("word_count")])
    dta_count_month = dta_count_month.sort("year_month")
    dta_count_month = dta_count_month.rename({"word_count": "word_count_month"})
    dta_count_month_company = dta.group_by(pl.col("year_month"), pl.col("company_name")).agg(
        [pl.sum("word_count")]
    )
    dta_count_month_company = dta_count_month_company.sort("company_name", "year_month")
    dta_count_month_company = dta_count_month_company.rename(
        {"word_count": "word_count_month_company"}
    )
    dta = dta.join(dta_count_month, on=["year_month"], how="left")
    dta = dta.join(dta_count_month_company, on=["year_month", "company_name"], how="left")
    dta = dta.sort("company_name", "year_month")
    # st.write(dta)  # TEMPPRINT:
    return dta


def get_term_counts_by_month_by_company(dta: pl.DataFrame, target_term: str) -> pl.DataFrame:
    dta = dta.filter(pl.col("clean_text").str.contains(target_term))
    dta_count_month = dta.group_by(pl.col("year_month")).agg([pl.sum("word_count")])
    dta_count_month = dta_count_month.sort("year_month")
    dta_count_month = dta_count_month.rename({"word_count": "word_count_month"})
    dta_count_month_company = dta.group_by(pl.col("year_month"), pl.col("company_name")).agg(
        [pl.sum("word_count")]
    )
    dta_count_month_company = dta_count_month_company.sort("company_name", "year_month")
    dta_count_month_company = dta_count_month_company.rename(
        {"word_count": "word_count_month_company"}
    )
    dta = dta.join(dta_count_month, on=["year_month"], how="left")
    dta = dta.join(dta_count_month_company, on=["year_month", "company_name"], how="left")
    dta = dta.sort("company_name", "year_month")
    return dta


def display_graph_dta(fig_dta: pl.DataFrame, fig_title):
    """
    Display a dataframe in a Streamlit app with an optional checkbox.

    Parameters:
    fig_dta (pl.DataFrame): The dataframe to be displayed.
    fig_title (str): The title of the figure or dataframe.

    Returns:
    None
    """
    chart_display = st.checkbox(f"Display Dataframe for {fig_title}?")
    if chart_display:
        st.write(f"#### {fig_title} Dataframe")
        st.dataframe(fig_dta)
        st.write(f"Dataframe shape: {fig_dta.shape}")


# def display_graph(fig_title, fig, fig_dta):
#     st.write(f"## {fig_title}")
#     # st.altair_chart(fig, use_container_width=True)
#     st.plotly_chart(fig, use_container_width=True)
#     chart_display = st.checkbox(f"Display Dataframe for {fig_title}?")
#     if chart_display:
#         st.write(f"#### {fig_title} Dataframe")
#         st.dataframe(fig_dta)
#         st.write(f"Dataframe shape: {fig_dta.shape}")


# TESTCODE:
def line_graph(fig_dta: pl.DataFrame, x_col: str, y_col: str, color_col: str, title: str):
    fig = px.line(fig_dta, x=x_col, y=y_col, color=color_col, title=title)
    return fig
