import streamlit as st

st.set_page_config(page_title="Companions", layout="wide")

background_url = "https://raw.githubusercontent.com/6Ace9/Companions/main/Companions.jpg"

css = f"""
<style>
    /* Original full-screen background - back to stretch as you had it */
    .stApp {{
        background: url('{background_url}') no-repeat center center fixed;
        background-size: 100% 100%;
        background-color: black;
        height: 100vh;
        margin: 0;
        padding: 0;
    }}
    
    /* Hide all default Streamlit elements */
    header, footer, .stApp > div:first-child {{ visibility: hidden; }}
    [data-testid="stSidebar"] {{ display: none; }}
    .stApp {{ margin: 0; padding: 0; }}

    /* Center the three rings horizontally */
    .ring-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 100px;
        height: 100vh;
        flex-wrap: wrap;
    }}

    /* Base glowing ring button */
    .ring-button {{
        width: 240px;
        height: 240px;
        border-radius: 50%;
        background: transparent;
        border: none;
        cursor: pointer;
        font-size: 32px;
        font-weight: bold;
        color: white;
        text-shadow: 0 0 20px white;
        display: flex;
        align-items: center;
        justify-content: center;
        position: relative;
        transition: transform 0.3s ease;
    }}

    .ring-button:hover {{
        transform: scale(1.15);
    }}

    /* Owl - Purple Nebula */
    #owl-ring {{
        box-shadow: 
            0 0 40px 15px #a855f7,
            0 0 80px 30px #7e22ce,
            inset 0 0 60px 10px rgba(139, 92, 246, 0.4);
        border: 8px solid #c084fc;
        animation: owlPulse 4s ease-in-out infinite;
    }}

    @keyframes owlPulse {{
        0%, 100% {{ 
            box-shadow: 0 0 40px 15px #a855f7, 0 0 80px 30px #7e22ce, inset 0 0 60px 10px rgba(139, 92, 246, 0.4);
        }}
        50% {{ 
            box-shadow: 0 0 60px 25px #c084fc, 0 0 120px 50px #a855f7, inset 0 0 90px 15px rgba(168, 85, 247, 0.6);
        }}
    }}

    /* Koi - Light Blue */
    #koi-ring {{
        box-shadow: 
            0 0 40px 12px #38bdf8,
            0 0 80px 25px #0ea5e9,
            inset 0 0 60px 8px rgba(56, 189, 248, 0.3);
        border: 8px solid #7dd3fc;
        animation: koiPulse 5s ease-in-out infinite;
    }}

    @keyframes koiPulse {{
        0%, 100% {{ 
            box-shadow: 0 0 40px 12px #38bdf8, 0 0 80px 25px #0ea5e9, inset 0 0 60px 8px rgba(56, 189, 248, 0.3);
        }}
        50% {{ 
            box-shadow: 0 0 60px 20px #7dd3fc, 0 0 120px 45px #38bdf8, inset 0 0 90px 12px rgba(125, 211, 252, 0.5);
        }}
    }}

    /* Fox - Red/Orange */
    #fox-ring {{
        box-shadow: 
            0 0 40px 15px #f97316,
            0 0 80px 30px #ea580c,
            inset 0 0 60px 10px rgba(251, 146, 60, 0.4);
        border: 8px solid #fb923c;
        animation: foxPulse 3s ease-in-out infinite;
    }}

    @keyframes foxPulse {{
        0%, 100% {{ 
            box-shadow: 0 0 40px 15px #f97316, 0 0 80px 30px #ea580c, inset 0 0 60px 10px rgba(251, 146, 60, 0.4);
        }}
        50% {{ 
            box-shadow: 0 0 65px 25px #fb923c, 0 0 130px 55px #f97316, inset 0 0 90px 15px rgba(251, 146, 60, 0.7);
        }}
    }}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# Container for rings
st.markdown('<div class="ring-container">', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,1,1])

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

# Apply custom ring styles via JavaScript
st.markdown("""
<script>
    const buttons = document.querySelectorAll('[data-testid="stButton"] button');
    if (buttons.length >= 3) {
        buttons[0].classList.add('ring-button');
        buttons[0].id = 'owl-ring';
        
        buttons[1].classList.add('ring-button');
        buttons[1].id = 'koi-ring';
        
        buttons[2].classList.add('ring-button');
        buttons[2].id = 'fox-ring';
    }
</script>
""", unsafe_allow_html=True)
