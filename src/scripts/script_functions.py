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
        page_title=page_title,
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
        "GOVERNANCE": {
            "label": "Governance",
            "dict_color": "#808080",
            "terms": {
                "transparency": "#FF0000",
                "ethics": "#aa0000",
                "integrity": "#550000",
                "business conduct": "#00FF00",
                "anti-corruption": "#32CD32",
                "board leadership": "#006400",
                "ethical conduct": "#0000FF",
                "ethic": "#000099",
                "ethical standards": "#000033",
                "risk oversight": "#FFFF00",
                "governance": "#999900",
                "corruption": "#333300",
                "accountability": "#00FFFF",
                "accountable management": "#009999",
                "lobbying": "#003333",
                "political contribution": "#FF00FF",
                "political contributions": "#990099",
                "internal audit": "#330033",
                "internal audits": "#808080",
            },
        },
        "SOCIAL": {
            "label": "Social",
            "dict_color": "#0000FF",
            "terms": {
                "accommodate": "#FF0000",
                "accommodating": "#aa0000",
                "accommodation": "#550000",
                "adopted child": "#00FF00",
                "adopted children": "#32CD32",
                "affordable housing": "#006400",
                "affordable": "#0000FF",
                "alternative lifestyle": "#000099",
                "alternative lifestyles": "#000033",
                "beneficially": "#FFFF00",
                "beneficiary": "#999900",
                "benefit the masses": "#333300",
                "benefit": "#00FFFF",
                "benefits": "#009999",
                "blended families": "#003333",
                "bribe": "#FF00FF",
                "care": "#990099",
                "certification": "#330033",
                "certifications": "#808080",
                "certify": "#C0C0C0",
                "certifying": "#1a1a1a",
                "charitability": "#800000",
                "charitable foundation": "#4d0000",
                "charitable giving": "#1a0000",
                "charitable": "#808000",
                "charitably": "#4d4d00",
                "charities": "#1a1a00",
                "charity": "#008000",
                "child labor": "#003300",
                "child laborers": "#001100",
                "civic duties": "#800080",
                "civic duty": "#4d004d",
                "civic engagement": "#1a001a",
                "civic engagements": "#008080",
                "civic": "#004d4d",
                "civil": "#001a1a",
                "collective well being": "#000080",
                "collective well beings": "#00004d",
                "collectively": "#5b5bff",
                "communal": "#FF8C00",
                "communities": "#663800",
                "community development": "#331c00",
                "community developments": "#DAA520",
                "community group": "#836313",
                "community groups": "#eccc7d",
                "community impact": "#FF1493",
                "community investment": "#6e003b",
                "community investments": "#ff79c1",
                "community minded": "#FF0000",
                "community mission": "#aa0000",
                "community outreach": "#550000",
                "community policies": "#00FF00",
                "community policy": "#32CD32",
                "community project": "#006400",
                "community projects": "#0000FF",
                "community": "#000099",
                "conflict mineral": "#000033",
                "conflict minerals": "#FFFF00",
                "corporate foundation": "#999900",
                "cultural preservation": "#333300",
                "cultures": "#00FFFF",
                "customs": "#009999",
                "disabilities": "#003333",
                "disability": "#FF00FF",
                "disaster relief": "#990099",
                "discriminating": "#330033",
                "discrimination": "#808080",
                "discriminatory": "#C0C0C0",
                "diversity": "#1a1a1a",
                "donation": "#800000",
                "donations": "#4d0000",
                "educate": "#1a0000",
                "educating": "#808000",
                "education": "#4d4d00",
                "educational programs": "#1a1a00",
                "educational": "#008000",
                "employ": "#003300",
                "employed": "#001100",
                "employee equity": "#800080",
                "employee involvement": "#4d004d",
                "employee relations": "#1a001a",
                "employee safety": "#008080",
                "employee welfare": "#004d4d",
                "employee well being": "#001a1a",
                "employee": "#000080",
                "employee's well being": "#00004d",
                "employees well being": "#5b5bff",
                "employees": "#FF8C00",
                "employees'": "#663800",
                "employer": "#331c00",
                "employers": "#DAA520",
                "employing": "#836313",
                "employment": "#eccc7d",
                "employs": "#FF1493",
                "empower": "#6e003b",
                "empowered": "#ff79c1",
                "empowering": "#FF0000",
                "empowerment": "#aa0000",
                "empowers": "#550000",
                "engage": "#00FF00",
                "engaging": "#32CD32",
                "enjoyable": "#006400",
                "equal opportunity": "#0000FF",
                "equal": "#000099",
                "equity": "#000033",
                "ergonomic": "#FFFF00",
                "ergonomically": "#999900",
                "ethically": "#333300",
                "ethnic diversity": "#00FFFF",
                "ethnic": "#009999",
                "ethnicities": "#003333",
                "ethnicity": "#FF00FF",
                "exercise": "#990099",
                "extended families": "#330033",
                "extended family": "#808080",
                "fair": "#C0C0C0",
                "fairness": "#1a1a1a",
                "families": "#800000",
                "family": "#4d0000",
                "female": "#1a0000",
                "fiduciary": "#808000",
                "food pantries": "#4d4d00",
                "food pantry": "#1a1a00",
                "foodbank": "#008000",
                "foodbanks": "#003300",
                "freedom": "#001100",
                "future generation": "#800080",
                "future generations": "#4d004d",
                "gay": "#1a001a",
                "gays": "#008080",
                "gender diversity": "#004d4d",
                "giving": "#001a1a",
                "governance": "#000080",
                "groups of stakeholders": "#00004d",
                "health benefits": "#5b5bff",
                "health care benefits": "#FF8C00",
                "health insurance": "#663800",
                "health": "#331c00",
                "healthcare": "#DAA520",
                "healthcaring": "#836313",
                "healthy": "#eccc7d",
                "help": "#FF1493",
                "hire": "#6e003b",
                "hiring": "#ff79c1",
                "human rights": "#FF0000",
                "humanitarian": "#aa0000",
                "impact on community": "#550000",
                "impact on local communities": "#00FF00",
                "impact on local community": "#32CD32",
                "impact on society": "#006400",
                "inclusion": "#0000FF",
                "indigenous people": "#000099",
                "indigenous peoples": "#000033",
                "indigenous": "#FFFF00",
                "infectious": "#999900",
                "insurance": "#333300",
                "internal stakeholder": "#00FFFF",
                "internal stakeholders": "#009999",
                "job creation": "#003333",
                "jobs": "#FF00FF",
                "labor rights": "#990099",
                "labor": "#330033",
                "laborers": "#808080",
                "lawfulness": "#C0C0C0",
                "laws": "#1a1a1a",
                "lesbian": "#800000",
                "lesbians": "#4d0000",
                "less fortunate": "#1a0000",
                "life benefits": "#808000",
                "life partner": "#4d4d00",
                "lifestyles": "#1a1a00",
                "lives": "#008000",
                "local communities": "#003300",
                "local community": "#001100",
                "local development": "#800080",
                "local developments": "#4d004d",
                "local residents": "#1a001a",
                "malaria": "#008080",
                "minorities": "#004d4d",
                "minority": "#001a1a",
                "moral": "#000080",
                "mortality": "#00004d",
                "native people": "#5b5bff",
                "native peoples": "#FF8C00",
                "native": "#663800",
                "nature": "#331c00",
                "not for profit": "#DAA520",
                "occupational": "#836313",
                "oppressive regimes": "#eccc7d",
                "orphan": "#FF1493",
                "orphans": "#6e003b",
                "paid time off": "#ff79c1",
                "paid vacation time": "#FF0000",
                "partnerships": "#aa0000",
                "pension": "#550000",
                "people group": "#00FF00",
                "people groups": "#32CD32",
                "people": "#006400",
                "person": "#0000FF",
                "personal": "#000099",
                "personnel": "#000033",
                "persons": "#FFFF00",
                "philanthropic": "#999900",
                "philanthropies": "#333300",
                "philanthropy": "#00FFFF",
                "philosophies": "#009999",
                "poor individual": "#003333",
                "poor individuals": "#FF00FF",
                "poor people": "#990099",
                "prejudice": "#330033",
                "prejudiced": "#808080",
                "prejudices": "#C0C0C0",
                "preservation": "#1a1a1a",
                "preserve culture": "#800000",
                "principles": "#4d0000",
                "professional": "#1a0000",
                "professionals": "#808000",
                "profit sharing": "#4d4d00",
                "promotion": "#1a1a00",
                "rebuilding": "#008000",
                "religious diversity": "#003300",
                "religious": "#001100",
                "respects": "#800080",
                "responsibility": "#4d004d",
                "responsible": "#1a001a",
                "retirement": "#008080",
                "safe": "#004d4d",
                "safety": "#001a1a",
                "salaries": "#000080",
                "satisfaction": "#00004d",
                "scholarships": "#5b5bff",
                "social activities": "#FF8C00",
                "social inclination": "#663800",
                "social issue": "#331c00",
                "social issues": "#DAA520",
                "social policies": "#836313",
                "social policy": "#eccc7d",
                "social wellbeing": "#FF1493",
                "social": "#6e003b",
                "socially inclined": "#ff79c1",
                "socially minded": "#FF0000",
                "socially": "#aa0000",
                "societal development": "#550000",
                "societal developments": "#00FF00",
                "societal impact": "#32CD32",
                "societal": "#006400",
                "sponsors": "#0000FF",
                "sponsorship": "#000099",
                "spousal relationship": "#000033",
                "spousal relationships": "#FFFF00",
                "spouse": "#999900",
                "stakeholder engagement": "#333300",
                "stakeholders": "#00FFFF",
                "sweat shops": "#009999",
                "talented": "#003333",
                "team": "#FF00FF",
                "teams": "#990099",
                "teamwork": "#330033",
                "tenure": "#808080",
                "trained": "#C0C0C0",
                "transparency": "#1a1a1a",
                "transparent": "#800000",
                "trust": "#4d0000",
                "tuition reimbursement": "#1a0000",
                "unemployment": "#808000",
                "unethical": "#4d4d00",
                "unfair": "#1a1a00",
                "union": "#008000",
                "unionized": "#003300",
                "unions": "#001100",
                "unsafe": "#800080",
                "urban planning": "#4d004d",
                "urban": "#1a001a",
                "urbanization": "#008080",
                "vacation time": "#004d4d",
                "vision benefit": "#001a1a",
                "vision benefits": "#000080",
                "voluntarily": "#00004d",
                "voluntary": "#5b5bff",
                "volunteer": "#FF8C00",
                "volunteerism": "#663800",
                "volunteers": "#331c00",
                "vulnerability": "#DAA520",
                "vulnerable": "#836313",
                "wage": "#eccc7d",
                "welfare": "#FF1493",
                "wellness": "#6e003b",
                "wheelchair access": "#ff79c1",
                "wheelchair": "#FF0000",
                "wheelchairs": "#aa0000",
                "wife": "#550000",
                "women": "#00FF00",
                "work life balance": "#32CD32",
                "work": "#006400",
                "workday": "#0000FF",
                "worker": "#000099",
                "workers": "#000033",
                "workforce": "#FFFF00",
                "workforces": "#999900",
                "working men and women": "#333300",
                "workmen": "#00FFFF",
                "workplaces": "#009999",
                "works": "#003333",
                "workspaces": "#FF00FF",
            },
        },
        "ENVIRONMENT": {
            "label": "Environment",
            "dict_color": "#00FF00",
            "terms": {
                "acid rain": "#FF0000",
                "acid rains": "#aa0000",
                "air emissions": "#550000",
                "air filtration": "#00FF00",
                "air pollution": "#32CD32",
                "algae": "#006400",
                "alternative energy": "#0000FF",
                "amazon rain forest": "#000099",
                "battery": "#000033",
                "bio diversities": "#FFFF00",
                "biodiesel": "#999900",
                "biodiversity": "#333300",
                "biofuels": "#00FFFF",
                "biomass": "#009999",
                "caged animal": "#003333",
                "caged animals": "#FF00FF",
                "carbon": "#990099",
                "carbon capture": "#330033",
                "carbon capture and storage": "#808080",
                "carbon dioxide": "#C0C0C0",
                "carbon dioxide capture": "#1a1a1a",
                "carbon dioxide emission": "#800000",
                "carbon dioxide reduction": "#4d0000",
                "carbon dioxide sequestration": "#1a0000",
                "carbon dioxides": "#808000",
                "carbon disclosure": "#4d4d00",
                "carbon disclosures": "#1a1a00",
                "carbon emission": "#008000",
                "carbon emissions": "#003300",
                "carbon footprint": "#001100",
                "carbon reduction": "#800080",
                "carbon sequestration": "#4d004d",
                "carbon storage": "#1a001a",
                "carbonate": "#008080",
                "carbonated": "#004d4d",
                "carbonates": "#001a1a",
                "carrying capacities": "#000080",
                "carrying capacity": "#00004d",
                "carrying load": "#5b5bff",
                "carrying loads": "#FF8C00",
                "catastrophic": "#663800",
                "ccs": "#331c00",
                "charging station": "#DAA520",
                "chemicals": "#836313",
                "clean energies": "#eccc7d",
                "clean energy": "#FF1493",
                "clean power": "#6e003b",
                "climate": "#ff79c1",
                "climate change": "#FF0000",
                "climate changes": "#aa0000",
                "climate event": "#550000",
                "co2": "#00FF00",
                "co2 capture": "#32CD32",
                "co2 emission": "#006400",
                "co2 reduction": "#0000FF",
                "co2 sequestration": "#000099",
                "conservation": "#000033",
                "conservationist": "#FFFF00",
                "conservationists": "#999900",
                "conservations": "#333300",
                "conserve": "#00FFFF",
                "dioxide": "#009999",
                "dioxides": "#003333",
                "disclosing": "#FF00FF",
                "disclosure": "#990099",
                "disposal": "#330033",
                "double bottom line": "#808080",
                "dwindling": "#C0C0C0",
                "eco system": "#1a1a1a",
                "eco systems": "#800000",
                "ecological": "#4d0000",
                "efficiencies": "#1a0000",
                "efficiently": "#808000",
                "electric car": "#4d4d00",
                "emission": "#1a1a00",
                "emissions": "#008000",
                "energy efficiencies": "#003300",
                "energy efficiency": "#001100",
                "energy efficient": "#800080",
                "energy star": "#4d004d",
                "environment": "#1a001a",
                "environmental": "#008080",
                "environmental activism": "#004d4d",
                "environmental activist": "#001a1a",
                "environmental activists": "#000080",
                "environmental activities": "#00004d",
                "environmental activity": "#5b5bff",
                "environmental disclosure": "#FF8C00",
                "environmental disclosures": "#663800",
                "environmental impact": "#331c00",
                "environmental inclination": "#DAA520",
                "environmental management systems": "#836313",
                "environmental performance": "#eccc7d",
                "environmental policies": "#FF1493",
                "environmental policy": "#6e003b",
                "environmental position": "#ff79c1",
                "environmental positions": "#FF0000",
                "environmental protection agency": "#aa0000",
                "environmental reform": "#550000",
                "environmental reformation": "#00FF00",
                "environmental resource": "#32CD32",
                "environmental resources": "#006400",
                "environmental responsibilities": "#0000FF",
                "environmental responsibility": "#000099",
                "environmental safety": "#000033",
                "environmental stance": "#FFFF00",
                "environmental stewardship": "#999900",
                "environmentalist": "#333300",
                "environmentalists": "#00FFFF",
                "environmentally": "#009999",
                "environmentally friendly": "#003333",
                "environmentally inclined": "#FF00FF",
                "environmentally safe": "#990099",
                "food safety": "#330033",
                "fuel efficiency": "#808080",
                "genetically modified": "#C0C0C0",
                "ghg capture": "#1a1a1a",
                "ghg reduction": "#800000",
                "ghg sequestration": "#4d0000",
                "ghg emission": "#1a0000",
                "global warming": "#808000",
                "green building": "#4d4d00",
                "green buildings": "#1a1a00",
                "green engineering": "#008000",
                "greenhouse effect": "#003300",
                "greenhouse gas capture": "#001100",
                "greenhouse gas emission": "#800080",
                "greenhouse gas reduction": "#4d004d",
                "greenhouse gas sequestration": "#1a001a",
                "gri": "#008080",
                "gri frameworks": "#004d4d",
                "gri ratings": "#001a1a",
                "gri standards": "#000080",
                "groundwater": "#00004d",
                "harm": "#5b5bff",
                "harmony": "#FF8C00",
                "harness wind energy": "#663800",
                "harness wind power": "#331c00",
                "hazardous": "#DAA520",
                "hazardous waste": "#836313",
                "hcfc": "#eccc7d",
                "hybrid": "#FF1493",
                "hybrid car": "#6e003b",
                "hybrid energy": "#ff79c1",
                "hybrid vehicle": "#FF0000",
                "hybrid vehicles": "#aa0000",
                "hydro power": "#550000",
                "hydro powered": "#00FF00",
                "hydrogen power": "#32CD32",
                "hydrogen powered": "#006400",
                "kld": "#0000FF",
                "kld categories": "#000099",
                "kld standards": "#000033",
                "land conservation": "#FFFF00",
                "land conservationism": "#999900",
                "land conservationist": "#333300",
                "land conservationists": "#00FFFF",
                "lifestyle of health and sustainability": "#009999",
                "lower emission": "#003333",
                "lower emissions": "#FF00FF",
                "material stewardship": "#990099",
                "methane capture": "#330033",
                "methane emission": "#808080",
                "methane reduction": "#C0C0C0",
                "methane sequestration": "#1a1a1a",
                "msci": "#800000",
                "natural": "#4d0000",
                "natural resource": "#1a0000",
                "natural resources": "#808000",
                "nature": "#4d4d00",
                "organic": "#1a1a00",
                "overcapacity": "#008000",
                "ozone": "#003300",
                "ozone depleting": "#001100",
                "ozone depletion": "#800080",
                "ozone depletions": "#4d004d",
                "photovoltaic": "#1a001a",
                "plastic pollution": "#008080",
                "plastic waste": "#004d4d",
                "pollutant": "#001a1a",
                "pollutants": "#000080",
                "polluting": "#00004d",
                "pollution": "#5b5bff",
                "pollution prevention": "#FF8C00",
                "preservation": "#663800",
                "preserve": "#331c00",
                "preserve way of life": "#DAA520",
                "preserves": "#836313",
                "prevention": "#eccc7d",
                "pro environmental": "#FF1493",
                "purification": "#6e003b",
                "pv": "#ff79c1",
                "rainforest": "#FF0000",
                "recycle": "#aa0000",
                "renew": "#550000",
                "renewable": "#00FF00",
                "renewable energies": "#32CD32",
                "renewable energy": "#006400",
                "renewable power": "#0000FF",
                "resource conservation": "#000099",
                "resource conservationism": "#000033",
                "resource conservationist": "#FFFF00",
                "resource conservationists": "#999900",
                "reusable": "#333300",
                "reuse": "#00FFFF",
                "reuses": "#009999",
                "safe": "#003333",
                "safety": "#FF00FF",
                "smart growth": "#990099",
                "solar": "#330033",
                "solar cells": "#808080",
                "solar energy": "#C0C0C0",
                "solar panels": "#1a1a1a",
                "solar photovoltaic": "#800000",
                "solar power": "#4d0000",
                "solar pv": "#1a0000",
                "stewardship": "#808000",
                "sustainable": "#4d4d00",
                "sustainable consumption": "#1a1a00",
                "symbiotic": "#008000",
                "symbiotic relationship": "#003300",
                "symbiotic relationships": "#001100",
                "tree": "#800080",
                "trees": "#4d004d",
                "triple bottom line": "#1a001a",
                "unsafe": "#008080",
                "voluntary": "#004d4d",
                "voluntary disclosure": "#001a1a",
                "voluntary disclosures": "#000080",
                "vulnerability": "#00004d",
                "vulnerable": "#5b5bff",
                "waste": "#FF8C00",
                "waste reduction": "#663800",
                "wasteland": "#331c00",
                "water": "#DAA520",
                "water desalination": "#836313",
                "water purification": "#eccc7d",
                "water purifications": "#FF1493",
                "wetland": "#6e003b",
                "wetlands": "#ff79c1",
                "wilderness": "#FF0000",
                "wildlife conservation": "#aa0000",
                "wind": "#550000",
                "wind energies": "#00FF00",
                "wind energy": "#32CD32",
                "wind power": "#006400",
                "wind turbine": "#0000FF",
                "windmill": "#000099",
            },
        },
        "CSR": {
            "label": "CSR",
            "dict_color": "#800080",
            "terms": {
                "csr": "#FF0000",
                "corporate social responsibility": "#aa0000",
                "sustainability": "#550000",
                "sustainable development": "#00FF00",
                "sustainable development goals": "#32CD32",
                "triple bottom line": "#006400",
                "esg": "#0000FF",
                "environmental social and governance": "#000099",
                "circular economy": "#000033",
            },
        },
        "CLIMATE CHANGE": {
            "label": "Climate Change",
            "dict_color": "#00FFFF",
            "terms": {
                "climate change": "#FF0000",
                "global warming": "#aa0000",
                "greenhouse effect": "#550000",
                "greenhouse": "#00FF00",
                "greenhouse gas": "#32CD32",
                "greenhouse gas emission": "#006400",
                "greenhouse gas sequestration": "#0000FF",
                "greenhouse gas capture": "#000099",
                "greenhouse gas reduction": "#000033",
                "ghg emission": "#FFFF00",
                "ghg sequestration": "#999900",
                "ghg capture": "#333300",
                "ghg reduction": "#00FFFF",
                "co2 emission": "#009999",
                "co2 sequestration": "#003333",
                "co2 capture": "#FF00FF",
                "co2 reduction": "#990099",
                "carbon dioxide emission": "#330033",
                "carbon dioxide sequestration": "#808080",
                "carbon dioxide capture": "#C0C0C0",
                "carbon dioxide reduction": "#1a1a1a",
                "carbon disclosure": "#800000",
                "methane emission": "#4d0000",
                "methane sequestration": "#1a0000",
                "methane capture": "#808000",
                "methane reduction": "#4d4d00",
                "carbon emission": "#1a1a00",
                "carbon sequestration": "#008000",
                "carbon capture": "#003300",
                "carbon reduction": "#001100",
                "carbon footprint": "#800080",
                "net zero": "#4d004d",
                "net-zero": "#1a001a",
                "climate neutral": "#008080",
            },
        },
        "RENEWABLES": {
            "label": "Renewables",
            "dict_color": "#FF8C00",
            "terms": {
                "renewable energy": "#FF0000",
                "clean energy": "#aa0000",
                "renewable power": "#550000",
                "clean power": "#00FF00",
                "wind power": "#32CD32",
                "wind energy": "#006400",
                "wind turbine": "#0000FF",
                "offshore wind": "#000099",
                "solar power": "#000033",
                "solar energy": "#FFFF00",
                "solar pv": "#999900",
                "solar photovoltaic": "#333300",
                "electric car": "#00FFFF",
                "electric vehicle": "#009999",
                "energy storage": "#003333",
                "battery": "#FF00FF",
                "charging station": "#990099",
            },
        },
        "BIOMASS": {
            "label": "Biomass",
            "dict_color": "#DAA520",
            "terms": {
                "biomass": "#FF0000",
                "algae": "#aa0000",
                "biodiesel": "#550000",
                "ethanol": "#00FF00",
                "biofuel": "#32CD32",
                "biofuels": "#006400",
            },
        },
        "CARBON CAPTURE": {
            "label": "Carbon Capture",
            "dict_color": "#FFFF00",
            "terms": {
                "global warming": "#FF0000",
                "carbon sequestration": "#aa0000",
                "carbon capture": "#550000",
                "carbon dioxide sequestration": "#00FF00",
                "carbon dioxide capture": "#32CD32",
                "co2 sequestration": "#006400",
                "co2 capture": "#0000FF",
                "ghg sequestration": "#000099",
                "ghg capture": "#000033",
                "greenhouse gas sequestration": "#FFFF00",
                "greenhouse gas capture": "#333300",
            },
        },
        # "climate_change": {
        #     "Climate Change Dictionary": "climate_change",  # to get name easier
        #     "label": "Climate Change Dictionary",
        #     "terms": {
        #         "climate change": "#c97a55",
        #         # "net-zero": "#827cde",
        #         "net zero": "#a08e33",
        #         "greenhouse gas": "#9f479a",
        #         "GHG": "#9b341e",
        #         "scope 1": "#0178af",
        #         "scope 2": "#bb7aa3",
        #         "scope 3": "#903646",
        #         # "climate change": "#006d09", # old terms from former dictionary
        #         # "global warming": "#bc1055", # old terms from former dictionary
        #         # "greenhouse gas": "#0b913e", # old terms from former dictionary
        #         # "methane": "#c66509", # old terms from former dictionary
        #         # "emission": "#990099", # old terms from former dictionary
        #     },
        # },
        # "sustainability|exploitation": {
        #     "Sustainability|Exploitation Dictionary": "sustainability|exploitation",  # to get name easier
        #     "label": "Sustainability|Exploitation Dictionary",
        #     "terms": {
        #         # sustainability cool
        #         "sustain|sustainability": "#00FF00",
        #         "vegan": "#0000FF",
        #         "climate change": "#006d09",
        #         "environment": "#808000",
        #         "land use": "#008000",
        #         "water use": "#800080",
        #         "growing population": "#008080",
        #         "supply chain": "#000080",
        #         # exploitation warm
        #         "exploit|exploitation": "#FF0000",
        #         "process|processed": "#aa0000",
        #         "product|production|produce": "#999900",
        #         "kill": "#800000",
        #         "slaughter": "#4d0000",
        #         "butcher": "#aa0000",
        #     },
        # },
        # "prosocial": {
        #     "Prosocial Dictionary": "prosocial",  # to get name easier
        #     "label": "Prosocial Dictionary",
        #     "terms": {
        #         "donate|donation": "#00FF00",
        #         "share|sharing": "#0000FF",
        #         "volunteer|volunteering": "#00FFFF",
        #         "honor": "#808000",
        #         "award": "#008000",
        #         "support": "#800080",
        #         "pledge": "#008080",
        #         "generosity|generos": "#000080",
        #         "compassion": "#FF0000",
        #         "community|communities": "#FFFF00",
        #         "contribut": "#FF00FF",
        #     },
        # },
        # "health_general": {
        #     "General Health Dictionary": "health_general",  # to get name easier
        #     "label": "General Health Dictionary",
        #     "terms": {
        #         "health": "#00FF00",
        #         "public health": "#0000FF",
        #         "antibiotic|prebiotic": "#00FFFF",
        #         "nutrition|nutritious|nutrient": "#808000",
        #         "hygiene": "#008000",
        #         "safe|safety": "#800080",
        #         "wellness": "#008080",
        #         "health safety": "#000080",
        #         "health expert|health research": "#FF0000",
        #         "health outcome|health benefits|health care|health clinic|health support|health service": "#FFFF00",
        #         "health department|health official|health inspection": "#FF00FF",
        #         "diet": "#800000",
        #         "heath product": "#FF8C00",
        #         "animal health|herd health|healthy cattle": "#aa0000",
        #     },
        # },
        # "health_human": {
        #     "Human Health Dictionary": "health_human",  # to get name easier
        #     "label": "Human Health Dictionary",
        #     "terms": {
        #         "human health": "#00FF00",
        #         "public health": "#0000FF",
        #         "antibiotic|prebiotic": "#00FFFF",
        #         "nutrition|nutritious|nutrient": "#808000",
        #         "hygiene": "#008000",
        #         "safe|safety": "#800080",
        #         "wellness": "#008080",
        #         "health safety": "#000080",
        #         "health expert|health research": "#FF0000",
        #         "health outcome|health benefits|health care|health clinic|health support|health service": "#FFFF00",
        #         "health department|health official|health inspection": "#FF00FF",
        #         "diet": "#800000",
        #         "heath product": "#FF8C00",
        #     },
        # },
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


def get_dicts_combined_term_count(dta: pl.DataFrame, dictionary_dicts):
    """
    Combines terms from multiple dictionaries and counts their occurrences in a DataFrame column.
    Args:
        dta (pl.DataFrame): A Polars DataFrame containing a column named 'clean_text' where term occurrences will be counted.
        dictionary_dicts (dict): A dictionary of dictionaries, where each key is a dictionary name and each value is a dictionary
                                 containing 'terms' (a dictionary of terms to count) and 'label' (a label for the term count column).
                                 Each dictionary should also contain 'dict_color' for the color associated with the term count.
    Returns:
        tuple: A tuple containing:
            - dta (pl.DataFrame): The updated DataFrame with new columns for each dictionary's term count.
            - term_col_names (list): A list of the new column names added to the DataFrame.
            - term_col_colors (dict): A dictionary mapping each new column name to its associated color.
    """
    dict_keys = [dictionary_dict for dictionary_dict in dictionary_dicts.keys()]
    for dict_key in dict_keys:
        dict_terms = dictionary_dicts[dict_key]["terms"].keys()
        dict_terms = "|".join(dict_terms)
        dictionary_dicts[dict_key]["combined_terms"] = dict_terms
    dictionary_dicts
    term_col_names = []
    term_col_colors = {}
    for dict_key in dict_keys:
        combined_terms = dictionary_dicts[dict_key]["combined_terms"]
        dict_label = dictionary_dicts[dict_key]["label"]
        term_col_colors.update({f"{dict_label}": dictionary_dicts[dict_key]["dict_color"]})
        term_col_names.append(f"{dict_label}")
        combined_terms = combined_terms.lower()
        dta = dta.with_columns(
            pl.col("clean_text")
            .str.count_matches(combined_terms)
            .cast(pl.Int32)
            .alias(f"{dict_label}")
        )
    # st.write(dta)  # TEMPPRINT:
    # st.write(term_col_names)  # TEMPPRINT:
    # st.write(term_col_colors)  # TEMPPRINT:
    return dta, term_col_names, term_col_colors


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
            .alias(f"{term}")
            # pl.col("clean_text").str.contains(target_term).cast(pl.Int32).alias(f"{term}")
        )
    # st.write(dta)  # TEMPPRINT:
    term_col_names = [f"{term}" for term in dict_terms]
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
            .alias(f"{term}")
            # pl.col("clean_text").str.contains(target_term).cast(pl.Int32).alias(f"{term}")
        )
    # st.write(dta)  # TEMPPRINT:
    term_col_names = [f"{term}" for term in target_terms]
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


"""
#FF0000
#aa0000
#550000
#00FF00
#32CD32
#006400
#0000FF
#000099
#000033
#FFFF00
#999900
#333300
#00FFFF
#009999
#003333
#FF00FF
#990099
#330033
#808080
#C0C0C0
#1a1a1a
#800000
#4d0000
#1a0000
#808000
#4d4d00
#1a1a00
#008000
#003300
#001100
#800080
#4d004d
#1a001a
#008080
#004d4d
#001a1a
#000080
#00004d
#5b5bff
#FF8C00
#663800
#331c00
#DAA520
#836313
#eccc7d
#FF1493
#6e003b
#ff79c1

Red         #FF0000     #aa0000     #550000
Lime        #00FF00     #32CD32     #006400
Blue        #0000FF     #000099     #000033
Yellow      #FFFF00     #999900     #333300
Cyan        #00FFFF     #009999     #003333
Magenta     #FF00FF     #990099     #330033
Gray        #808080     #C0C0C0     #1a1a1a
Maroon      #800000     #4d0000     #1a0000
Olive       #808000     #4d4d00     #1a1a00
Green       #008000     #003300     #001100
Purple      #800080     #4d004d     #1a001a
Teal        #008080     #004d4d     #001a1a
Navy        #000080     #00004d     #5b5bff
darkorange  #FF8C00     #663800     #331c00
black       #000000     #000000     #000000

Cool colors
Lime        #00FF00     #32CD32     #006400
Blue        #0000FF     #000099     #000033
Cyan        #00FFFF     #009999     #003333
Olive       #808000     #4d4d00     #1a1a00
Green       #008000     #003300     #001100
Purple      #800080     #4d004d     #1a001a
Teal        #008080     #004d4d     #001a1a
Navy        #000080     #00004d     #5b5bff

Warm colors
Red         #FF0000     #aa0000     #550000
Yellow      #FFFF00     #999900     #333300
Magenta     #FF00FF     #990099     #330033
Maroon      #800000     #4d0000     #1a0000
darkorange  #FF8C00     #663800     #331c00

Other color groups
Gray        #808080     #C0C0C0     #1a1a1a
"""
