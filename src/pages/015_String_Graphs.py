import plotly.express as px
import polars as pl
import streamlit as st

import scripts.script_functions as functs


def get_posts_by_date(dta: pl.DataFrame) -> pl.DataFrame:
    return dta.group_by(pl.col("year_month_dt")).agg(pl.len().alias("count")).sort("year_month_dt")


def graph_post_by_date(fig_dta: pl.DataFrame):
    fig_title = "Posts by Date"
    # fig = alt.Chart(fig_dta).mark_line().encode(x="year_month_dt", y="count", color="company_name")
    fig = px.line(fig_dta, x="year_month_dt", y="count", title="Posts by Date")
    return fig, fig_title, fig_dta


def get_posts_by_date_by_company(dta: pl.DataFrame) -> pl.DataFrame:
    return (
        dta.group_by(pl.col("year_month_dt"), pl.col("company_name"))
        .agg(pl.len().alias("count"))
        .sort("year_month_dt")
        .sort("company_name")
    )


def graph_terms_by_date_raw_count(fig_dta: pl.DataFrame, term_col_names: list[str]):
    fig_title = "Terms by Date Raw Count"
    col_names = term_col_names.copy()
    col_names.append("year_month_dt")
    fig_dta = fig_dta.select(pl.col(col_names))
    term_col_names.append("year_month_dt")
    fig_dta = fig_dta.group_by(pl.col("year_month_dt")).sum().sort("year_month_dt")
    fig = px.line(fig_dta, x="year_month_dt", y=term_col_names, title=fig_title)
    return fig, fig_title, fig_dta


def graph_terms_by_date_prop(fig_dta: pl.DataFrame, term_col_names: list[str]):
    fig_title = "Terms by Date Proportion of Words"
    col_names = term_col_names.copy()
    col_names.append("year_month_dt")
    col_names.append("word_count")
    fig_dta = fig_dta.select(pl.col(col_names))
    fig_dta = fig_dta.group_by(pl.col("year_month_dt")).sum().sort("year_month_dt")
    # st.write(fig_dta)  # TEMPPRINT:
    for term in term_col_names:
        if "count" in term:
            fig_dta = fig_dta.with_columns(
                (pl.col(term) / pl.col("word_count")).alias(f"{term.replace('_count', '_prop')}")
            )
    term_prop_cols = [term.replace("_count", "_prop") for term in term_col_names]
    # st.write(fig_dta)  # TEMPPRINT:
    fig = px.line(fig_dta, x="year_month_dt", y=term_prop_cols, title=fig_title)
    return fig, fig_title, fig_dta


def graph_terms_by_date_prop_companies(
    fig_dta: pl.DataFrame, term_col_names: list[str], companies_selection: list[str]
):
    companies_selection_string = ", ".join(companies_selection)
    fig_title = f"Terms by Date Proportion of Words ({companies_selection_string})"
    col_names = term_col_names.copy()
    if "year_month_dt" in col_names:
        pass
    else:
        col_names.append("year_month_dt")
    col_names.append("word_count")
    col_names.append("company_name")
    # filter to selected companies
    fig_dta = fig_dta.filter(pl.col("company_name").is_in(companies_selection))
    fig_dta = fig_dta.select(pl.col(col_names))
    fig_dta = fig_dta.group_by(pl.col("year_month_dt")).sum().sort("year_month_dt")
    for term in term_col_names:
        if "count" in term:
            fig_dta = fig_dta.with_columns(
                (pl.col(term) / pl.col("word_count")).alias(f"{term.replace('_count', '_prop')}")
            )
    term_prop_cols = [term.replace("_count", "_prop") for term in term_col_names]
    # st.write(fig_dta)  # TEMPPRINT:
    fig = px.line(fig_dta, x="year_month_dt", y=term_prop_cols, title=fig_title)
    return fig, fig_title, fig_dta


def graph_post_by_date_by_company(fig_dta: pl.DataFrame):
    fig_title = "Posts by Company by Date"
    fig = px.line(
        fig_dta,
        x="year_month_dt",
        y="count",
        color="company_name",
        title="Posts by Company by Date",
    )
    return fig, fig_title, fig_dta


def display_graph_dta(fig_dta, fig_title):
    chart_display = st.checkbox(f"Display Dataframe for {fig_title}?")
    if chart_display:
        st.write(f"#### {fig_title} Dataframe")
        st.dataframe(fig_dta)
        st.write(f"Dataframe shape: {fig_dta.shape}")


def display_graph(fig_title, fig, fig_dta):
    st.write(f"## {fig_title}")
    st.plotly_chart(fig, use_container_width=True)
    chart_display = st.checkbox(f"Display Dataframe for {fig_title}?")
    if chart_display:
        st.write(f"#### {fig_title} Dataframe")
        st.dataframe(fig_dta)
        st.write(f"Dataframe shape: {fig_dta.shape}")


def main() -> None:
    page_title = "Basic Descriptive Graphs"
    functs.set_page_configs(page_title)
    dictionary_dicts = functs.create_dictionary_dicts()
    # dict_key, dict_label, dict_terms, dict_terms_colors = functs.select_dictionary(dictionary_dicts)

    dta = functs.load_dta()
    dta = functs.get_year_selection_filter_bar(dta)
    # st.write(f"dta.columns: {dta.columns}")  # TEMPPRINT:
    dta = functs.get_article_word_count(dta)
    # st.write(f"dta.columns: {dta.columns}")  # TEMPPRINT:
    dta = functs.get_word_count_by_month_by_company(dta)
    # dta, term_col_names = functs.get_dict_term_count(dta, dict_terms)
    user_term = st.text_input(
        "Enter a Term to Graph\n\nIf you want to use more than 1 term separate them by using the character ',' do not include spaces\n\n\nYou can also use the pipe character to combine terms using regex (and thus combine them into one line)\n\nExample: scope 1|scope 2|scope 3",
        "scope 1,scope 2,scope 3",
    )  # TODO: add term selection
    dta, term_col_names = functs.get_term_count(dta, user_term)
    raw_counts_selection = st.checkbox("Show Raw Counts?", value=False)
    if raw_counts_selection:
        fig, fig_title, fig_dta = graph_terms_by_date_raw_count(dta, term_col_names)
        st.plotly_chart(fig, use_container_width=True)
        display_graph_dta(fig_dta, fig_title)
    else:
        fig, fig_title, fig_dta = graph_terms_by_date_prop(dta, term_col_names)
        st.plotly_chart(fig, use_container_width=True)
        display_graph_dta(fig_dta, fig_title)

    # companies_selection = st.multiselect( # TODO: issue with constantly reloading company list
    #     label="Select Companies to Include in Line Graphs",
    #     options=dta["company_name"].unique().to_list(),
    # )
    # companies_selection = st.selectbox(
    #     label="Select Companies to Include in Line Graphs",
    #     options=dta["company_name"].unique().to_list(),
    # )
    companies_selection = (
        st.segmented_control(  # TODO: issue with constantly reloading company list
            label="Select Companies to Include in Line Graphs Below",
            options=dta["company_name"].unique().sort().to_list(),
            selection_mode="multi",
        )
    )
    fig, fig_title, fig_dta = graph_terms_by_date_prop_companies(
        dta, term_col_names, companies_selection
    )

    # dta_by_date = get_posts_by_date(dta)
    # fig, fig_title, fig_dta = graph_post_by_date(dta_by_date)
    st.plotly_chart(fig, use_container_width=True)
    display_graph_dta(fig_dta, fig_title)
    # dta_by_date = get_posts_by_date_by_company(dta)
    # fig, fig_title, fig_dta = graph_post_by_date_by_company(dta_by_date)
    # st.plotly_chart(fig, use_container_width=True)
    # display_graph_dta(fig_dta, fig_title)

    st.sidebar.write(functs.print_updated_time())  # PROGRESSTRACKING:
    print(functs.print_updated_time())  # PROGRESSTRACKING:


main()