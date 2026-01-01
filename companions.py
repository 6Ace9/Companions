import streamlit as st

st.set_page_config(page_title="Companions", layout="wide")

background_url = "https://raw.githubusercontent.com/6Ace9/Companions/main/Companions.jpg"

css = f"""
<style>
    /* Original full-screen stretched background */
    .stApp {{
        background: url('{background_url}') no-repeat center center fixed;
        background-size: 100% 100%;
        background-color: black;
        height: 100vh;
        margin: 0;
        padding: 0;
        overflow: hidden;
    }}
    
    /* Hide all default Streamlit elements */
    header, footer, .stApp > div:first-child {{ visibility: hidden; }}
    [data-testid="stSidebar"] {{ display: none; }}

    /* Draggable glowing ring button */
    .ring-button {{
        width: 260px;
        height: 260px;
        border-radius: 50%;
        background: transparent;
        border: 10px solid;
        cursor: move;
        font-size: 36px;
        font-weight: bold;
        color: white;
        text-shadow: 0 0 25px white;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: transform 0.4s ease;
        box-sizing: border-box;
        position: absolute;
        user-select: none;
        touch-action: none;
    }}

    .ring-button:hover {{
        transform: scale(1.2);
    }}

    /* Owl - Purple Nebula */
    #owl-ring {{
        border-color: #c084fc;
        box-shadow: 
            0 0 50px 15px #a855f7,
            0 0 100px 35px #7e22ce,
            inset 0 0 80px 10px rgba(139, 92, 246, 0.5);
        animation: owlPulse 4s ease-in-out infinite;
    }}

    @keyframes owlPulse {{
        0%, 100% {{ box-shadow: 0 0 50px 15px #a855f7, 0 0 100px 35px #7e22ce, inset 0 0 80px 10px rgba(139,92,246,0.5); }}
        50% {{ box-shadow: 0 0 80px 30px #c084fc, 0 0 150px 60px #a855f7, inset 0 0 120px 20px rgba(168,85,247,0.7); }}
    }}

    /* Koi - Light Blue */
    #koi-ring {{
        border-color: #7dd3fc;
        box-shadow: 
            0 0 50px 12px #38bdf8,
            0 0 100px 30px #0ea5e9,
            inset 0 0 80px 8px rgba(56,189,248,0.4);
        animation: koiPulse 5s ease-in-out infinite;
    }}

    @keyframes koiPulse {{
        0%, 100% {{ box-shadow: 0 0 50px 12px #38bdf8, 0 0 100px 30px #0ea5e9, inset 0 0 80px 8px rgba(56,189,248,0.4); }}
        50% {{ box-shadow: 0 0 80px 25px #7dd3fc, 0 0 150px 55px #38bdf8, inset 0 0 120px 15px rgba(125,211,252,0.6); }}
    }}

    /* Fox - Red/Orange */
    #fox-ring {{
        border-color: #fb923c;
        box-shadow: 
            0 0 50px 15px #f97316,
            0 0 100px 35px #ea580c,
            inset 0 0 80px 10px rgba(251,146,60,0.5);
        animation: foxPulse 3s ease-in-out infinite;
    }}

    @keyframes foxPulse {{
        0%, 100% {{ box-shadow: 0 0 50px 15px #f97316, 0 0 100px 35px #ea580c, inset 0 0 80px 10px rgba(251,146,60,0.5); }}
        50% {{ box-shadow: 0 0 85px 30px #fb923c, 0 0 160px 65px #f97316, inset 0 0 130px 20px rgba(251,146,60,0.8); }}
    }}

    /* Lock button in top-right */
    #lock-btn {{
        position: fixed;
        top: 20px;
        right: 20px;
        z-index: 1000;
        padding: 10px 20px;
        font-size: 18px;
        border-radius: 30px;
        cursor: pointer;
        background: red;
        color: white;
        border: none;
        box-shadow: 0 0 15px rgba(255,0,0,0.8);
    }}

    #lock-btn.locked {{
        background: green;
        box-shadow: 0 0 15px rgba(0,255,0,0.8);
    }}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# Main container for draggable elements
st.markdown("""
<div id="scene" style="position: relative; width: 100vw; height: 100vh;">
    <button id="owl-ring" class="ring-button">Owl</button>
    <button id="koi-ring" class="ring-button">Koi</button>
    <button id="fox-ring" class="ring-button">Fox</button>
    
    <button id="lock-btn">Unlock Dragging</button>
</div>
""", unsafe_allow_html=True)

# JavaScript for dragging, saving positions, and lock toggle
st.markdown("""
<script>
    const rings = {
        'owl-ring': {x: 20, y: 50},
        'koi-ring': {x: 50, y: 50},
        'fox-ring': {x: 80, y: 50}
    };

    // Load saved positions
    Object.keys(rings).forEach(id => {
        const saved = localStorage.getItem(id);
        if (saved) {
            const pos = JSON.parse(saved);
            rings[id] = pos;
        }
    });

    // Apply positions
    function applyPositions() {
        Object.keys(rings).forEach(id => {
            const el = document.getElementById(id);
            if (el) {
                el.style.left = `${rings[id].x}vw`;
                el.style.top = `${rings[id].y}vh`;
            }
        });
    }
    applyPositions();

    let isDragging = null;
    let offset = {x: 0, y: 0};
    let isLocked = false;

    const lockBtn = document.getElementById('lock-btn');
    lockBtn.addEventListener('click', () => {
        isLocked = !isLocked;
        lockBtn.textContent = isLocked ? 'Lock Positions' : 'Unlock Dragging';
        lockBtn.classList.toggle('locked', isLocked);
        Object.keys(rings).forEach(id => {
            document.getElementById(id).style.cursor = isLocked ? 'default' : 'move';
        });
    });

    document.querySelectorAll('.ring-button').forEach(btn => {
        btn.addEventListener('mousedown', (e) => {
            if (isLocked) return;
            isDragging = btn.id;
            const rect = btn.getBoundingClientRect();
            offset.x = e.clientX - rect.left - rect.width / 2;
            offset.y = e.clientY - rect.top - rect.height / 2;
        });

        btn.addEventListener('touchstart', (e) => {
            if (isLocked) return;
            isDragging = btn.id;
            const touch = e.touches[0];
            const rect = btn.getBoundingClientRect();
            offset.x = touch.clientX - rect.left - rect.width / 2;
            offset.y = touch.clientY - rect.top - rect.height / 2;
        });
    });

    document.addEventListener('mousemove', (e) => {
        if (!isDragging || isLocked) return;
        const x = (e.clientX - offset.x) / window.innerWidth * 100;
        const y = (e.clientY - offset.y) / window.innerHeight * 100;
        rings[isDragging] = {x, y};
        document.getElementById(isDragging).style.left = `${x}vw`;
        document.getElementById(isDragging).style.top = `${y}vh`;
    });

    document.addEventListener('touchmove', (e) => {
        if (!isDragging || isLocked) return;
        const touch = e.touches[0];
        const x = (touch.clientX - offset.x) / window.innerWidth * 100;
        const y = (touch.clientY - offset.y) / window.innerHeight * 100;
        rings[isDragging] = {x, y};
        document.getElementById(isDragging).style.left = `${x}vw`;
        document.getElementById(isDragging).style.top = `${y}vh`;
        e.preventDefault();
    });

    document.addEventListener('mouseup', () => {
        if (isDragging) {
            localStorage.setItem(isDragging, JSON.stringify(rings[isDragging]));
            isDragging = null;
        }
    });

    document.addEventListener('touchend', () => {
        if (isDragging) {
            localStorage.setItem(isDragging, JSON.stringify(rings[isDragging]));
            isDragging = null;
        }
    });

    // Button click actions (alert for now)
    document.getElementById('owl-ring').addEventListener('click', () => alert('You chose the wise Owl companion ✨'));
    document.getElementById('koi-ring').addEventListener('click', () => alert('You chose the graceful Koi companion 🪷'));
    document.getElementById('fox-ring').addEventListener('click', () => alert('You chose the clever Fox companion 🔥'));
</script>
""", unsafe_allow_html=True)
