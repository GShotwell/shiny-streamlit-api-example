import streamlit as st
from helpers import read_penguins, scatter_plot, density_plot

if "slider" not in st.session_state:
    st.session_state["slider"] = 6000


def reset_slider():
    st.session_state["slider"] = 6000


with st.sidebar:
    mass = st.slider("Max Body Mass", min_value=2000, max_value=8000, key="slider")
    smoother = st.checkbox("Add Smoother")
    reset = st.button("Reset slider", on_click=reset_slider)

df = read_penguins()
df = df.loc[df["body_mass_g"] < mass]

st.pyplot(scatter_plot(df, smoother).draw())
st.pyplot(density_plot(df).draw())
