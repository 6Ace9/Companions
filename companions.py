import streamlit as st

st.set_page_config(page_title="Landscape", layout="wide")

background_url = "https://raw.githubusercontent.com/6Ace9/Companions/main/Landscape.jpg"

css = f"""
<style>
    /* Full-screen background that FILLS the entire screen */
    .stApp {{
        background: url('{background_url}') no-repeat center center fixed;
        background-size: cover;        /* Fills screen completely, no gaps, no distortion */
        background-color: black;       /* Fallback color */
    }}
    
    /* Hide all Streamlit UI elements */
    header, footer, .stApp > div:first-child {{ visibility: hidden; }}
    .stApp {{ margin: 0; padding: 0; height: 100vh; }}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# Completely empty content
st.markdown("")
