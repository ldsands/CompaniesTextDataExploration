import plotly.express as px
import polars as pl
import streamlit as st

import scripts.company_functions as company_functs
import scripts.script_functions as functs


def get_posts_by_date(dta: pl.DataFrame) -> pl.DataFrame:
    return dta.group_by(pl.col("year_dt")).agg(pl.len().alias("count")).sort("year_dt")


def graph_post_by_date(fig_dta: pl.DataFrame):
    fig_title = "Posts by Date"
    fig = px.line(fig_dta, x="year_dt", y="count", title="Posts by Date")
    return fig, fig_title, fig_dta


def get_posts_by_date_by_company(dta: pl.DataFrame) -> pl.DataFrame:
    return (
        dta.group_by(pl.col("year_dt"), pl.col("company_name"))
        .agg(pl.len().alias("count"))
        .sort("year_dt")
        .sort("company_name")
    )


def graph_terms_by_date_raw_count(
    fig_dta: pl.DataFrame, term_col_names: list[str], term_col_colors
):
    fig_title = "Terms by Date Raw Count (All Companies)"
    col_names = term_col_names.copy()
    col_names.append("year_dt")
    fig_dta = fig_dta.select(pl.col(col_names))
    term_col_names.append("year_dt")
    fig_dta = fig_dta.group_by(pl.col("year_dt")).sum().sort("year_dt")
    fig = px.line(
        fig_dta,
        x="year_dt",
        y=term_col_names,
        title=fig_title,
        color_discrete_map=term_col_colors,
    )
    return fig, fig_title, fig_dta


def graph_terms_by_date_raw_count_companies(
    fig_dta: pl.DataFrame,
    term_col_names: list[str],
    term_col_colors,
    companies_selection: list[str],
):
    companies_selection_string = ", ".join(companies_selection)
    fig_title = f"Terms by Date Raw Count ({companies_selection_string})"
    col_names = term_col_names.copy()
    fig_dta = fig_dta.select(pl.col(col_names))
    term_col_names.append("year_dt")
    fig_dta = fig_dta.group_by(pl.col("year_dt")).sum().sort("year_dt")
    fig = px.line(
        fig_dta,
        x="year_dt",
        y=term_col_names,
        color_discrete_map=term_col_colors,
        title=fig_title,
    )
    return fig, fig_title, fig_dta


def graph_terms_by_date_prop(
    fig_dta: pl.DataFrame, term_col_names: list[str], term_col_colors: dict
):
    fig_title = "Terms by Date Proportion of Words (All Companies)"
    col_names = term_col_names.copy()
    col_names.append("year_dt")
    col_names.append("word_count")
    fig_dta = fig_dta.select(pl.col(col_names))
    fig_dta = fig_dta.group_by(pl.col("year_dt")).sum().sort("year_dt")
    # st.write(fig_dta)  # TEMPPRINT:
    for term in term_col_names:
        fig_dta = fig_dta.with_columns(
            (pl.col(term) / pl.col("word_count")).alias(f"{term.replace('_count', '_prop')}")
        )
    # st.write(fig_dta)  # TEMPPRINT:
    fig = px.line(
        fig_dta,
        x="year_dt",
        y=term_col_names,
        color_discrete_map=term_col_colors,
        title=fig_title,
    )
    return fig, fig_title, fig_dta


def graph_terms_by_date_prop_companies(
    fig_dta: pl.DataFrame,
    term_col_names: list[str],
    term_col_colors: dict,
    companies_selection: list[str],
):
    companies_selection_string = ", ".join(companies_selection)
    fig_title = f"Terms by Date Proportion of Words ({companies_selection_string})"
    col_names = term_col_names.copy()
    col_names.append("year_dt")
    col_names.append("word_count")
    col_names.append("company_name")
    fig_dta = fig_dta.filter(pl.col("company_name").is_in(companies_selection))
    fig_dta = fig_dta.select(pl.col(col_names))
    fig_dta = fig_dta.group_by(pl.col("year_dt")).sum().sort("year_dt")
    for term in term_col_names:
        fig_dta = fig_dta.with_columns(
            (pl.col(term) / pl.col("word_count")).alias(f"{term.replace('_count', '_prop')}")
        )
    fig = px.line(
        fig_dta,
        x="year_dt",
        y=term_col_names,
        color_discrete_map=term_col_colors,
        title=fig_title,
    )
    return fig, fig_title, fig_dta


def graph_terms_by_date_prop_select_companies_dictionary(
    fig_dta: pl.DataFrame,
    term_col_names: list[str],
    term_col_colors: dict,
    companies_selection: list[str],
    dict_selection_label: str,
):
    companies_selection_string = ", ".join(companies_selection)
    fig_title = f"Terms by Date Proportion of Words in {dict_selection_label} Dictionary ({companies_selection_string})"
    col_names = term_col_names.copy()
    col_names.append("year_dt")
    col_names.append("word_count")
    col_names.append("company_name")
    fig_dta = fig_dta.filter(pl.col("company_name").is_in(companies_selection))
    fig_dta = fig_dta.select(pl.col(col_names))
    fig_dta = fig_dta.group_by(pl.col("year_dt"), pl.col("company_name")).sum().sort("year_dt")
    for term in term_col_names:
        fig_dta = fig_dta.with_columns(
            (pl.col(term) / pl.col("word_count")).alias(f"{term.replace('_count', '_prop')}")
        )
    fig = px.line(
        fig_dta,
        x="year_dt",
        y=fig_dta[dict_selection_label],
        color=fig_dta["company_name"],
        color_discrete_map=company_functs.company_colors_dict(),
        title=fig_title,
    )
    fig.update_yaxes(title_text="Proportion of Words in Dictionary")
    fig.update_xaxes(title_text="Date by Year")
    return fig, fig_title, fig_dta


def graph_post_by_date_by_company(fig_dta: pl.DataFrame):
    fig_title = "Posts by Company by Date"
    fig = px.line(
        fig_dta,
        x="year_dt",
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
    page_title = "Basic Dictionary Graphs"
    functs.set_page_configs(page_title)
    dictionary_dicts = functs.create_dictionary_dicts()
    dict_key, dict_label, dict_terms, dict_terms_colors = functs.select_dictionary(dictionary_dicts)

    dta = functs.load_dta()
    dta = functs.get_year_selection_filter_bar(dta)
    # st.write(f"dta.columns: {dta.columns}")  # TEMPPRINT:
    dta = functs.get_article_word_count(dta)
    # st.write(f"dta.columns: {dta.columns}")  # TEMPPRINT:
    dta = functs.get_word_count_by_year_by_company(dta)
    dta, term_col_names, term_col_colors = functs.get_dicts_combined_term_count(
        dta, dictionary_dicts
    )
    # dta, term_col_names = functs.get_dict_term_count(dta, dict_terms)
    raw_counts_selection = st.checkbox("Show Raw Counts?", value=False)
    if raw_counts_selection:
        fig, fig_title, fig_dta = graph_terms_by_date_raw_count(
            dta, term_col_names, term_col_colors
        )
        st.plotly_chart(fig, use_container_width=True)
        display_graph_dta(fig_dta, fig_title)
        companies_selection = st.segmented_control(
            label="Select Companies to Include in Line Graphs",
            options=dta["company_name"].unique().sort().to_list(),
            selection_mode="multi",
        )
        fig, fig_title, fig_dta = graph_terms_by_date_raw_count_companies(  # todo:
            dta, term_col_names, term_col_colors, companies_selection
        )
        st.plotly_chart(fig, use_container_width=True)
        display_graph_dta(fig_dta, fig_title)
    else:
        fig, fig_title, fig_dta = graph_terms_by_date_prop(
            dta, term_col_names, term_col_colors
        )  # todo:
        st.plotly_chart(fig, use_container_width=True)
        display_graph_dta(fig_dta, fig_title)
        companies_selection = st.segmented_control(
            label="Select Companies to Include in Line Graphs",
            options=dta["company_name"].unique().sort().to_list(),
            selection_mode="multi",
        )
        fig, fig_title, fig_dta = graph_terms_by_date_prop_companies(  # todo:
            dta, term_col_names, term_col_colors, companies_selection
        )
        st.plotly_chart(fig, use_container_width=True)
        display_graph_dta(fig_dta, fig_title)
        # for displaying companies at the same time for one dict
        st.write("### Companies by Dictionary Selection (Proportion of Words)")
        companies_selection = st.segmented_control(
            label="Select Companies to Include in Line Graphs",
            options=dta["company_name"].unique().sort().to_list(),
            selection_mode="multi",
            key="prop_companies_dict_selection",
            default=dta["company_name"].unique().sort().to_list()[0:2],
        )
        dict_selection = st.segmented_control(
            label="Select Dictionary to Include in Line Graph",
            options=dictionary_dicts.keys(),
            selection_mode="single",
            key="prop_dictionary_selection",
            default=["CLIMATE CHANGE"],
        )
        dict_selection_label = dictionary_dicts[dict_selection]["label"]
        fig, fig_title, fig_dta = graph_terms_by_date_prop_select_companies_dictionary(
            dta, term_col_names, term_col_colors, companies_selection, dict_selection_label
        )
        st.plotly_chart(fig, use_container_width=True)
        display_graph_dta(fig_dta, fig_title)

    st.sidebar.write(functs.print_updated_time())  # PROGRESSTRACKING:
    print(functs.print_updated_time())  # PROGRESSTRACKING:


main()
