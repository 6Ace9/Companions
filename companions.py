import streamlit as st

st.set_page_config(page_title="Companions", layout="wide")

background_url = "https://raw.githubusercontent.com/6Ace9/Companions/main/Companions.jpg"

css = f"""
<style>
    /* Full-screen background */
    .stApp {{
        background: url('{background_url}') no-repeat center center fixed;
        background-size: 100% 100%;
        background-color: black;
        height: 100vh;
        margin: 0;
        padding: 0;
        overflow: hidden;
    }}
    
    /* Hide Streamlit UI */
    header, footer, .stApp > div:first-child {{ visibility: hidden; }}
    [data-testid="stSidebar"] {{ display: none; }}

    /* Base ring style */
    .ring-button {{
        width: 260px;
        height: 260px;
        border-radius: 50%;
        background: transparent;
        border: 10px solid;
        cursor: pointer;
        position: absolute;
        transform: translate(-50%, -50%);
        box-sizing: border-box;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: transform 0.4s ease;
    }}

    .ring-button:hover {{
        transform: translate(-50%, -50%) scale(1.2);
    }}

    /* Icon inside the ring */
    .ring-icon {{
        font-size: 100px;          /* Big emoji icons */
        pointer-events: none;      /* So clicks pass through to button */
        text-shadow: 0 0 30px black;
    }}

    /* Owl Ring */
    #owl-ring {{
        border-color: #c084fc;
        box-shadow: 0 0 50px 15px #a855f7, 0 0 100px 35px #7e22ce, inset 0 0 80px 10px rgba(139,92,246,0.5);
        animation: owlPulse 4s ease-in-out infinite;
    }}

    /* Koi Ring */
    #koi-ring {{
        border-color: #7dd3fc;
        box-shadow: 0 0 50px 12px #38bdf8, 0 0 100px 30px #0ea5e9, inset 0 0 80px 8px rgba(56,189,248,0.4);
        animation: koiPulse 5s ease-in-out infinite;
    }}

    /* Fox Ring */
    #fox-ring {{
        border-color: #fb923c;
        box-shadow: 0 0 50px 15px #f97316, 0 0 100px 35px #ea580c, inset 0 0 80px 10px rgba(251,146,60,0.5);
        animation: foxPulse 3s ease-in-out infinite;
    }}

    @keyframes owlPulse {{
        0%, 100% {{ box-shadow: 0 0 50px 15px #a855f7, 0 0 100px 35px #7e22ce, inset 0 0 80px 10px rgba(139,92,246,0.5); }}
        50% {{ box-shadow: 0 0 80px 30px #c084fc, 0 0 150px 60px #a855f7, inset 0 0 120px 20px rgba(168,85,247,0.7); }}
    }}

    @keyframes koiPulse {{
        0%, 100% {{ box-shadow: 0 0 50px 12px #38bdf8, 0 0 100px 30px #0ea5e9, inset 0 0 80px 8px rgba(56,189,248,0.4); }}
        50% {{ box-shadow: 0 0 80px 25px #7dd3fc, 0 0 150px 55px #38bdf8, inset 0 0 120px 15px rgba(125,211,252,0.6); }}
    }}

    @keyframes foxPulse {{
        0%, 100% {{ box-shadow: 0 0 50px 15px #f97316, 0 0 100px 35px #ea580c, inset 0 0 80px 10px rgba(251,146,60,0.5); }}
        50% {{ box-shadow: 0 0 85px 30px #fb923c, 0 0 160px 65px #f97316, inset 0 0 130px 20px rgba(251,146,60,0.8); }}
    }}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# Rings with icons only (no text labels)
st.markdown("""
<div style="position: relative; height: 100vh; width: 100vw; margin: 0; padding: 0;">
    <!-- Owl Ring -->
    <button class="ring-button" id="owl-ring" 
            style="top: 22%; left: 55%;"
            onclick="alert('You chose the wise Owl companion ✨🦉')">
        <div class="ring-icon">🦉</div>
    </button>

    <!-- Koi Ring -->
    <button class="ring-button" id="koi-ring" 
            style="top: 58%; left: 50%;"
            onclick="alert('You chose the graceful Koi companion 🪷🐟')">
        <div class="ring-icon">🪷</div>
    </button>

    <!-- Fox Ring -->
    <button class="ring-button" id="fox-ring" 
            style="top: 78%; left: 68%;"
            onclick="alert('You chose the clever Fox companion 🔥🦊')">
        <div class="ring-icon">🦊</div>
    </button>
</div>
""", unsafe_allow_html=True)
