import streamlit as st


def set_page_configs():
    st.set_page_config(
        layout="wide",
        page_title="Companies Text Data Exploration Streamlit Page Descriptions",
        page_icon="👋",
        initial_sidebar_state="expanded",
    )
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def write_markdown():
    st.write("# Companies Text Data Exploration Streamlit Home Page")

    st.sidebar.success("Select page from above to access the different graph categories.")
    st.markdown(
        """
    ## Dictionary Terms

    This page displays each dictionary and the terms included.

    """
    )

    # ## Descriptive Graphs

    # This page allows for displaying and filtering the data in several ways.

    # ## Term Filter Graphs

    # This page is very similar to the "Descriptive Graphs" page however it includes several ways to filter and display the data while filtering for terms from the topic dictionaries.

    # ## Proportional Term Filter Graphs

    # This page is very similar to the "Term Filter Graphs" page however it displays the term filtered graphs while normalizing the graphs based upon selectable factors.

    # ## Topic Model Outputs

    # This page contains several outputs from topic models run on each organization included in the data. Note that the Factiva based data were merged based on regional, national or business organization categorizations.

    # ## Dictionary Term Context Viewer

    # This page allows for selecting a term(s) from the topic dictionaries and then displaying the context of the term(s) in the data. The context is displayed in a table format with the organization, date, document ID and word location index. The context is also displayed in a text format with the target term highlighted in yellow. It also allows for selecting the number of words to display before and after the target term(s).

    # ## String Search Display

    # This page allows for entering any term(s) to then displaying the context of the term in the data. The context is displayed in a table format with the organization, date, document ID and word location index. The context is also displayed in a text format with the target term highlighted in yellow. It also allows for selecting the number of words to display before and after the target term(s).

    # ## NGram Viewer

    # This page shows n-grams for data selected based on the filtering options included.

    # ## Fixed Graphs for Exploration

    # This page contains several graphs that are fixed and not as interactive. They are included for exploration purposes.

    # ## Fixed Graphs for Pub

    # This page contains several graphs that are fixed supposed to be a "final" version of each. They are intended to be used for publication purposes.


def main():
    set_page_configs()
    write_markdown()


main()
