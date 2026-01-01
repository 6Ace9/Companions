import streamlit as st

# Set page config for full width and initial sidebar state if needed
st.set_page_config(page_title="My Website Homepage", layout="wide")

# Custom CSS for full-screen background
background_url = "https://github.com/6Ace9/Companions/blob/main/Landscape.jpg?raw=true"  # Temporary workaround
# Or use a public direct link once fixed, e.g., from Imgur or Pexels

css = f"""
<style>
    .stApp {{
        background: url('{background_url}') no-repeat center center fixed;
        background-size: cover;
    }}
    /* Dark overlay for text readability */
    .stApp::before {{
        content: '';
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(0, 0, 0, 0.4);
        z-index: -1;
    }}
    .content {{
        text-align: center;
        color: white;
        padding: 20px;
    }}
    h1 {{ font-size: 4rem; margin-bottom: 20px; }}
    p {{ font-size: 1.5rem; max-width: 800px; margin: 0 auto 40px; }}
    a.btn {{
        display: inline-block;
        padding: 15px 30px;
        background: #007bff;
        color: white;
        text-decoration: none;
        border-radius: 5px;
        font-size: 1.2rem;
    }}
    a.btn:hover {{ background: #0056b3; }}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

# Center content vertically
st.markdown("<div class='content' style='position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 100%;'>", unsafe_allow_html=True)
st.markdown("<h1>Welcome to My Website</h1>", unsafe_allow_html=True)
st.markdown("<p>This homepage uses your landscape as a full-screen background!</p>", unsafe_allow_html=True)
st.markdown('<a href="#" class="btn">Get Started</a>', unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
