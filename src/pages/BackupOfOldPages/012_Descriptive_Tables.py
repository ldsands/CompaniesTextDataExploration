import plotly.express as px
import polars as pl
import streamlit as st

import scripts.script_functions as functs


def get_word_count_by_year(dta: pl.DataFrame) -> pl.DataFrame:  # TODO: test
    return dta.group_by(pl.col("year")).agg(pl.len().alias("count")).sort("year")


def get_word_count_by_year_by_company(dta: pl.DataFrame) -> pl.DataFrame:  # TODO: test
    return (
        dta.group_by(pl.col("year"), pl.col("company_name"))
        .agg(pl.len().alias("count"))
        .sort("year")
        .sort("company_name")
    )


def get_posts_by_date(dta: pl.DataFrame) -> pl.DataFrame:
    return dta.group_by(pl.col("year_month_dt")).agg(pl.len().alias("count")).sort("year_month_dt")


def graph_post_by_date(fig_dta: pl.DataFrame):
    fig_title = "Posts by Date"
    # fig = alt.Chart(fig_dta).mark_line().encode(x="year_month_dt", y="count", color="company_name")
    fig = px.line(fig_dta, x="year_month_dt", y="count", title=fig_title)
    return fig, fig_title, fig_dta


def get_posts_by_date_by_company(dta: pl.DataFrame) -> pl.DataFrame:
    return (
        # dta.group_by("year_month", "company_name").agg(pl.len().alias("count")).sort("year_month")
        # dta.group_by("year_month", "company_name").agg(pl.len().alias("count"))
        dta.group_by(pl.col("year_month_dt"), pl.col("company_name"))
        .agg(pl.len().alias("count"))
        .sort("year_month_dt")
        .sort("company_name")
    )


def graph_post_by_date_by_company(fig_dta: pl.DataFrame):
    fig_title = "Posts by Company by Date"
    # fig = alt.Chart(fig_dta).mark_line().encode(x="year_month_dt", y="count", color="company_name")
    fig = px.line(fig_dta, x="year_month_dt", y="count", color="company_name", title=fig_title)
    return fig, fig_title, fig_dta


def display_graph(fig_title, fig, fig_dta):
    st.write(f"## {fig_title}")
    st.plotly_chart(fig, use_container_width=True)
    chart_display = st.checkbox(f"Display Dataframe for {fig_title}?")
    if chart_display:
        st.write(f"#### {fig_title} Dataframe")
        st.dataframe(fig_dta)
        st.write(f"Dataframe shape: {fig_dta.shape}")


def main() -> None:
    page_title = "Descriptive Graphs"
    functs.set_page_configs(page_title)
    dta = functs.load_dta()
    dta = functs.get_year_selection_filter_bar(dta)
    dta = functs.get_article_word_count(dta)
    dta = dta.drop(["source_url", "text", "year", "month"])
    # get start year by company
    dta_start_year = dta[["company_name", "year_int"]]
    dta_start_year = dta_start_year.group_by(pl.col("company_name")).agg(pl.min("year_int"))
    dta_start_year = dta_start_year.rename({"year_int": "start_year"})
    dta_start_year = dta_start_year.unique()
    dta_start_year = dta_start_year.sort("company_name", "start_year")
    st.write("## Start Year by Company")
    st.write(dta_start_year)
    # get total articles by company
    dta_total_articles = dta[["company_name", "date"]]
    dta_total_articles = (
        dta.group_by(pl.col("company_name")).agg(pl.len().alias("count")).sort("company_name")
    )
    st.write("## Total Articles by Company")
    st.write(dta_total_articles)
    # get total word count by company
    dta_total_word_count = dta[["company_name", "word_count"]]
    dta_total_word_count = dta.group_by(pl.col("company_name")).agg(pl.sum("word_count"))
    dta_total_word_count = dta_total_word_count.sort("company_name")
    st.write("## Total Word Count by Company")
    st.write(dta_total_word_count)
    st.sidebar.write(functs.print_updated_time())  # PROGRESSTRACKING:
    print(functs.print_updated_time())  # PROGRESSTRACKING:


main()
