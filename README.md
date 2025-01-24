# Companies Text Data Exploration

## UV Environment

- Using uv you can manage all the dependencies and environment

```sh
# run the app
uv run streamlit run src/app.py
# if using on a computer for the first time install uv then use the command below
uv sync
```

- initial setup

```sh
uv init CompaniesTextDataExploration
uv add streamlit polars pyarrow plotly
```

- You MUST create a requirements.txt to run in streamlit
    - As if 2024-08-30 if you have a `pyproject.toml` streamlit cloud assumes it is a poetry project

```sh
# create a requirements.txt file for streamlit cloud to use
uv pip compile pyproject.toml -o requirements.txt
```

```sh
# to update packages to newer versions
uv lock --upgrade
```
