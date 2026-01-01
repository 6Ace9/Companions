import streamlit as st

st.set_page_config(page_title="Companions", layout="wide")

background_url = "https://raw.githubusercontent.com/6Ace9/Companions/main/Companions.jpg"

css = f"""
<style>
    /* Full-screen stretched background */
    .stApp {{
        background: url('{background_url}') no-repeat center center fixed;
        background-size: 100% 100%;
        background-color: black;
        height: 100vh;
        margin: 0;
        padding: 0;
        overflow: hidden;
        position: relative;
    }}
    
    /* Hide default Streamlit elements */
    header, footer, .stApp > div:first-child {{ visibility: hidden; }}
    [data-testid="stSidebar"] {{ display: none; }}

    /* Container for absolute-positioned rings */
    .ring-container {{
        position: relative;
        width: 100%;
        height: 100vh;
    }}

    /* Glowing ring button */
    .ring-button {{
        position: absolute;
        width: 260px;
        height: 260px;
        border-radius: 50%;
        background: transparent;
        border: 10px solid;
        cursor: pointer;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: transform 0.4s ease, box-shadow 0.4s ease;
        box-sizing: border-box;
        text-decoration: none;
    }}

    .ring-button:hover {{
        transform: scale(1.2);
    }}

    /* Owl ring - Purple */
    #owl-ring {{
        top: 17.5%;
        left: 72%;
        transform: translate(-50%, -50%);
        border-color: #c084fc;
        box-shadow: 
            0 0 50px 15px #a855f7,
            0 0 100px 35px #7e22ce,
            inset 0 0 80px 10px rgba(139, 92, 246, 0.5);
        animation: owlPulse 4s ease-in-out infinite;
    }}

    #owl-ring:hover {{
        box-shadow: 
            0 0 85px 30px #c084fc,
            0 0 160px 65px #a855f7,
            inset 0 0 130px 20px rgba(168, 85, 247, 0.8);
    }}

    @keyframes owlPulse {{
        0%, 100% {{ box-shadow: 0 0 50px 15px #a855f7, 0 0 100px 35px #7e22ce, inset 0 0 80px 10px rgba(139,92,246,0.5); }}
        50% {{ box-shadow: 0 0 80px 30px #c084fc, 0 0 150px 60px #a855f7, inset 0 0 120px 20px rgba(168,85,247,0.7); }}
    }}

    /* Koi ring - Light Blue */
    #koi-ring {{
        top: 45%;
        left: 50.5%;
        transform: translate(-50%, -50%);
        border-color: #7dd3fc;
        box-shadow: 
            0 0 50px 12px #38bdf8,
            0 0 100px 30px #0ea5e9,
            inset 0 0 80px 8px rgba(56,189,248,0.4);
        animation: koiPulse 5s ease-in-out infinite;
    }}

    #koi-ring:hover {{
        box-shadow: 
            0 0 85px 30px #7dd3fc,
            0 0 160px 65px #38bdf8,
            inset 0 0 130px 20px rgba(125,211,252,0.8);
    }}

    @keyframes koiPulse {{
        0%, 100% {{ box-shadow: 0 0 50px 12px #38bdf8, 0 0 100px 30px #0ea5e9, inset 0 0 80px 8px rgba(56,189,248,0.4); }}
        50% {{ box-shadow: 0 0 80px 25px #7dd3fc, 0 0 150px 55px #38bdf8, inset 0 0 120px 15px rgba(125,211,252,0.6); }}
    }}

    /* Fox ring - Orange (already had strong hover) */
    #fox-ring {{
        top: 65%;
        left: 65%;
        transform: translate(-50%, -50%);
        border-color: #fb923c;
        box-shadow: 
            0 0 50px 15px #f97316,
            0 0 100px 35px #ea580c,
            inset 0 0 80px 10px rgba(251,146,60,0.5);
        animation: foxPulse 3s ease-in-out infinite;
    }}

    #fox-ring:hover {{
        box-shadow: 
            0 0 85px 30px #fb923c,
            0 0 160px 65px #f97316,
            inset 0 0 130px 20px rgba(251,146,60,0.8);
    }}

    @keyframes foxPulse {{
        0%, 100% {{ box-shadow: 0 0 50px 15px #f97316, 0 0 100px 35px #ea580c, inset 0 0 80px 10px rgba(251,146,60,0.5); }}
        50% {{ box-shadow: 0 0 85px 30px #fb923c, 0 0 160px 65px #f97316, inset 0 0 130px 20px rgba(251,146,60,0.8); }}
    }}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

st.markdown(
    '<div class="ring-container">'
    '  <a href="https://readingcompanion.streamlit.app/" target="_blank" class="ring-button" id="owl-ring"></a>'
    '  <a href="https://healingpond.streamlit.app/" target="_blank" class="ring-button" id="koi-ring"></a>'
    '  <a href="https://culinaryfox.streamlit.app/" target="_blank" class="ring-button" id="fox-ring"></a>'
    '</div>',
    unsafe_allow_html=True
)
