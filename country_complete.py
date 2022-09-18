import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

hide = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        body {overflow: hidden;}
        div.block-container {padding-top:1rem;}
        div.block-container {padding-bottom:1rem;}
        </style>
        """

st.markdown(hide, unsafe_allow_html=True)

country = pd.read_csv("country_complete.csv")

# st.header("Visualizing the tips dataset")

col1, col2 = st.columns([1,3])

with col1:
    plot = st.selectbox(
        "Plot",
        [
            "Box plot",
            "Density plot",
            "Histogram"
        ]
    )

    numerical = st.selectbox(
        "Numerical feature",
        [
            "Years",
            "Fertility",
            "Emissions",
            "Internet"
        ]
    )

    continent = st.selectbox(
        "Continent",
        [
            "Africa",
            "Americas",
            "Asia",
            "Europe"
        ]
    )

    check = st.checkbox("Display summary")
    if check: 
        five_num = country[country["Continent"]==continent].describe()
        summary = five_num[numerical]
        st.dataframe(summary)


with col2:
    df = country[country["Continent"]==continent][numerical]
    fig, ax = plt.subplots()

    if plot == "Box plot":
        sns.boxplot(x=df, width=0.5)

    elif plot == "Histogram":
        sns.histplot(x=df)

    elif plot == "Density plot":
        sns.histplot(x=df, kde=True)

    ax.set_xlabel(numerical, fontsize=14)
    ax.ticklabel_format(style='plain', axis='x')

    if plot=="Histogram": ax.set_ylabel("Count", fontsize=14)
    if plot=="Density plot":
        ax.set_ylabel("Count", fontsize=14)
        ax.ticklabel_format(style='plain', axis='y')

    st.pyplot(fig)
