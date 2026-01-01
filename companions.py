import streamlit as st

st.set_page_config(page_title="My Website Homepage", layout="wide")

# Use the reliable raw URL (now that your repo is public, this should work perfectly)
background_url = "https://raw.githubusercontent.com/6Ace9/Companions/main/Landscape.jpg"
# Fallback if needed: "https://github.com/6Ace9/Companions/blob/main/Landscape.jpg?raw=true"

css = f"""
<style>
    /* Main app background - show the WHOLE image */
    .stApp {{
        background: url('{background_url}') no-repeat center center fixed;
        background-size: contain;  /* Shows the full image, no cropping */
        background-color: black;   /* Optional: black backdrop if image doesn't fill screen */
    }}
    
    /* Dark overlay for better text readability */
    .stApp::before {{
        content: '';
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(0, 0, 0, 0.5);  /* Increased opacity a bit for contrast */
        z-index: -1;
    }}
    
    .content {{
        text-align: center;
        color: white;
        padding: 40px;
        min-height: 100vh;  /* Full viewport height */
        display: flex;
        flex-direction: column;
        justify-content: center;  /* Vertically center content */
    }}
    
    h1 {{ font-size: 4rem; margin-bottom: 20px; text-shadow: 2px 2px 4px black; }}
    p {{ font-size: 1.8rem; max-width: 900px; margin: 0 auto 40px; text-shadow: 1px 1px 3px black; }}
    a.btn {{
        display: inline-block;
        padding: 18px 36px;
        background: #007bff;
        color: white;
        text-decoration: none;
        border-radius: 8px;
        font-size: 1.4rem;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }}
    a.btn:hover {{ background: #0056b3; }}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# Content container
st.markdown("<div class='content'>", unsafe_allow_html=True)
st.markdown("<h1>Welcome to My Website</h1>", unsafe_allow_html=True)
st.markdown("<p>This homepage shows your full fantasy landscape – no cropping!</p>", unsafe_allow_html=True)
st.markdown('<a href="#" class="btn">Get Started</a>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
