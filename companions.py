import streamlit as st

st.set_page_config(page_title="Companions", layout="wide")

background_url = "https://raw.githubusercontent.com/6Ace9/Companions/main/Companions.jpg"

css = f"""
<style>
    /* Full-screen background - switched to cover to avoid distortion */
    .stApp {{
        background: url('{background_url}') no-repeat center center fixed;
        background-size: cover;
        background-color: black;
        height: 100vh;
        margin: 0;
        padding: 0;
    }}
    
    /* Hide Streamlit UI elements */
    header, footer {{ visibility: hidden; }}
    [data-testid="stSidebar"] {{ display: none; }}
    
    /* Container for centering buttons */
    .button-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 80px;
        height: 100vh;
        flex-wrap: wrap;
    }}
    
    /* Base ring button style */
    .glow-button {{
        width: 220px;
        height: 220px;
        border-radius: 50%;
        border: none;
        cursor: pointer;
        font-size: 28px;
        font-weight: bold;
        color: white;
        text-shadow: 0 0 15px white;
        position: relative;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: transform 0.3s ease;
    }}
    
    .glow-button:hover {{
        transform: scale(1.1);
    }}
    
    /* Owl - Purple Nebula */
    #owl-btn {{
        background: radial-gradient(circle, rgba(80,20,150,0.3) 0%, transparent 70%);
        box-shadow: 
            0 0 30px 10px #a855f7,
            0 0 60px 20px #7e22ce,
            inset 0 0 40px rgba(139,92,246,0.4);
        animation: owlPulse 4s ease-in-out infinite;
    }}
    
    @keyframes owlPulse {{
        0%, 100% {{ box-shadow: 0 0 30px 10px #a855f7, 0 0 60px 20px #7e22ce, inset 0 0 40px rgba(139,92,246,0.4); }}
        50% {{ box-shadow: 0 0 50px 20px #c084fc, 0 0 90px 35px #a855f7, inset 0 0 60px rgba(168,85,247,0.6); }}
    }}
    
    /* Koi - Light Blue */
    #koi-btn {{
        background: radial-gradient(circle, rgba(100,200,255,0.25) 0%, transparent 70%);
        box-shadow: 
            0 0 30px 8px #38bdf8,
            0 0 70px 15px #0ea5e9,
            inset 0 0 40px rgba(56,189,248,0.3);
        animation: koiPulse 5s ease-in-out infinite;
    }}
    
    @keyframes koiPulse {{
        0%, 100% {{ box-shadow: 0 0 30px 8px #38bdf8, 0 0 70px 15px #0ea5e9, inset 0 0 40px rgba(56,189,248,0.3); }}
        50% {{ box-shadow: 0 0 45px 15px #7dd3fc, 0 0 100px 30px #38bdf8, inset 0 0 60px rgba(125,211,252,0.5); }}
    }}
    
    /* Fox - Red/Orange */
    #fox-btn {{
        background: radial-gradient(circle, rgba(255,100,50,0.3) 0%, transparent 70%);
        box-shadow: 
            0 0 30px 10px #f97316,
            0 0 70px 20px #ea580c,
            inset 0 0 40px rgba(251,146,60,0.4);
        animation: foxPulse 3s ease-in-out infinite;
    }}
    
    @keyframes foxPulse {{
        0%, 100% {{ box-shadow: 0 0 30px 10px #f97316, 0 0 70px 20px #ea580c, inset 0 0 40px rgba(251,146,60,0.4); }}
        50% {{ box-shadow: 0 0 55px 20px #fb923c, 0 0 100px 40px #f97316, inset 0 0 70px rgba(251,146,60,0.6); }}
    }}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# Centered button container
st.markdown('<div class="button-container">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Owl", key="owl"):
        st.success("You chose the wise Owl companion ✨")

with col2:
    if st.button("Koi", key="koi"):
        st.success("You chose the graceful Koi companion 🪷")

with col3:
    if st.button("Fox", key="fox"):
        st.success("You chose the clever Fox companion 🔥")

st.markdown('</div>', unsafe_allow_html=True)

# Custom HTML/JS to apply the glowing styles (Streamlit buttons don't support direct id/class easily)
st.markdown("""
<script>
    const owl = document.querySelector('[data-testid="stButton"]').querySelector('button[kind="primary"]:nth-of-type(1)');
    const koi = document.querySelectorAll('[data-testid="stButton"]')[1].querySelector('button');
    const fox = document.querySelectorAll('[data-testid="stButton"]')[2].querySelector('button');
    
    if (owl) {{
        owl.classList.add('glow-button');
        owl.id = 'owl-btn';
    }}
    if (koi) {{
        koi.classList.add('glow-button');
        koi.id = 'koi-btn';
    }}
    if (fox) {{
        fox.classList.add('glow-button');
        fox.id = 'fox-btn';
    }}
</script>
""", unsafe_allow_html=True)
