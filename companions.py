import streamlit as st

st.set_page_config(page_title="Companions", layout="wide")

background_url = "https://raw.githubusercontent.com/6Ace9/Companions/main/Landscape.jpg"

css = f"""
<style>
    /* Full-screen background */
    .stApp {{
        background: url('{background_url}') no-repeat center center fixed;
        background-size: 100% 100%;    /* Stretches to fill width and height fully */
        background-color: black;       /* Fallback color */
        height: 100vh;
        margin: 0;
        padding: 0;
    }}
    
    /* Alternative if you prefer no distortion (shows full image, fills width, may crop height slightly on tall screens):
    .stApp {{
        background: url('{background_url}') no-repeat center top fixed;
        background-size: cover;        /* Or try '100% auto' to fill width exactly */
        background-color: black;
    }}
    */
    
    /* Hide all default Streamlit elements */
    header, footer, .stApp > div:first-child {{ visibility: hidden; }}
    [data-testid="stSidebar"] {{ display: none; }}
    .stApp {{ margin: 0; padding: 0; }}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# Empty content for pure background view
st.markdown("")
