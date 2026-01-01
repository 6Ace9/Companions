import streamlit as st

st.set_page_config(page_title="Landscape", layout="wide")

background_url = "https://raw.githubusercontent.com/6Ace9/Companions/main/Landscape.jpg"

css = f"""
<style>
    /* Full widescreen background - stretches to fill the entire screen */
    .stApp {{
        background: url('{background_url}') no-repeat center center fixed;
        background-size: cover;        /* Now fills the screen completely (widescreen style) */
    }}
    
    /* Remove all default Streamlit padding/margins and hide UI elements */
    .stApp {{ margin: 0; padding: 0; }}
    header, footer, .stDecoratedContent, .stApp > div {{ visibility: hidden !important; }}
    section.main {{ padding: 0 !important; margin: 0 !important; }}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# Absolutely nothing else - pure image
st.markdown("")
