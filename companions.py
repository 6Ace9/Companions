import streamlit as st

st.set_page_config(page_title="Companions", layout="wide")

background_url = "https://raw.githubusercontent.com/6Ace9/Companions/main/Companions.jpg"

css = f"""
<style>
    .stApp {{
        background: url('{background_url}') no-repeat center center fixed;
        background-size: cover;
        background-color: black;
        height: 100vh;
        margin: 0;
        padding: 0;
        overflow: hidden;
    }}
    header, footer, #MainMenu, .stAlert {{ visibility: hidden; }}
    [data-testid="stSidebar"], [data-testid="stDecoration"] {{ display: none; }}

    .ring {{
        width: 260px;
        height: 260px;
        border-radius: 50%;
        background: transparent;
        border: 10px solid;
        display: block;
        position: absolute;
        transform: translate(-50%, -50%);
        transition: transform 0.4s ease;
        z-index: 10;
        pointer-events: auto;
    }}
    .ring:hover {{ transform: translate(-50%, -50%) scale(1.2); }}

    #owl-ring {{
        border-color: #c084fc;
        box-shadow: 0 0 50px 15px #a855f7, 0 0 100px 35px #7e22ce, inset 0 0 80px 10px rgba(139,92,246,0.5);
        animation: owlPulse 4s ease-in-out infinite;
    }}
    @keyframes owlPulse {{
        0%, 100% {{ box-shadow: 0 0 50px 15px #a855f7, 0 0 100px 35px #7e22ce, inset 0 0 80px 10px rgba(139,92,246,0.5); }}
        50% {{ box-shadow: 0 0 80px 30px #c084fc, 0 0 150px 60px #a855f7, inset 0 0 120px 20px rgba(168,85,247,0.7); }}
    }}

    #koi-ring {{
        border-color: #7dd3fc;
        box-shadow: 0 0 50px 12px #38bdf8, 0 0 100px 30px #0ea5e9, inset 0 0 80px 8px rgba(56,189,248,0.4);
        animation: koiPulse 5s ease-in-out infinite;
    }}
    @keyframes koiPulse {{
        0%, 100% {{ box-shadow: 0 0 50px 12px #38bdf8, 0 0 100px 30px #0ea5e9, inset 0 0 80px 8px rgba(56,189,248,0.4); }}
        50% {{ box-shadow: 0 0 80px 25px #7dd3fc, 0 0 150px 55px #38bdf8, inset 0 0 120px 15px rgba(125,211,252,0.6); }}
    }}

    #fox-ring {{
        border-color: #fb923c;
        box-shadow: 0 0 50px 15px #f97316, 0 0 100px 35px #ea580c, inset 0 0 80px 10px rgba(251,146,60,0.5);
        animation: foxPulse 3s ease-in-out infinite;
    }}
    @keyframes foxPulse {{
        0%, 100% {{ box-shadow: 0 0 50px 15px #f97316, 0 0 100px 35px #ea580c, inset 0 0 80px 10px rgba(251,146,60,0.5); }}
        50% {{ box-shadow: 0 0 85px 30px #fb923c, 0 0 160px 65px #f97316, inset 0 0 130px 20px rgba(251,146,60,0.8); }}
    }}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# ONE SINGLE clean line - no multiline indents, no comments inside
st.markdown(
    '<div style="position: relative; height: 100vh; width: 100vw; margin: 0; padding: 0;">'
    '<a href="https://readingcompanion.streamlit.app/" target="_blank" class="ring" id="owl-ring" style="top: 20%; left: 65%;"></a>'
    '<a href="https://healingpond.streamlit.app/" target="_blank" class="ring" id="koi-ring" style="top: 55%; left: 50%;"></a>'
    '<a href="https://culinaryfox.streamlit.app/" target="_blank" class="ring" id="fox-ring" style="top: 85%; left: 55%;"></a>'
    '</div>',
    unsafe_allow_html=True
)
