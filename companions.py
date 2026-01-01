import streamlit as st

st.set_page_config(page_title="Landscape", layout="wide")

background_url = "https://raw.githubusercontent.com/6Ace9/Companions/main/Landscape.jpg"

css = f"""
<style>
    /* Full-screen background showing the entire image */
    .stApp {{
        background: url('{background_url}') no-repeat center center fixed;
        background-size: contain;      /* Shows the whole image, no cropping */
        background-color: black;       /* Black background for any empty space */
    }}
    
    /* Hide everything Streamlit adds by default */
    header, footer, .stApp > div:first-child {{ visibility: hidden; }}
    .stApp {{ margin: 0; padding: 0; }}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# No content at all – completely empty
st.markdown("")
