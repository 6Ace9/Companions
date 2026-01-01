import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Companions", layout="wide")

background_url = "https://raw.githubusercontent.com/6Ace9/Companions/main/Companions.jpg"

full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        html, body {{
            height: 100%;
            margin: 0;
            overflow: hidden;
            background: url('{background_url}') no-repeat center center fixed;
            background-size: 100% 100%;
        }}
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
            position: absolute;
            transition: transform 0.4s ease;
            box-sizing: border-box;
            user-select: none;
            z-index: 10;
        }}
        .ring-button:hover {{
            transform: scale(1.2);
        }}
        #owl-ring {{ border-color: #c084fc; box-shadow: 0 0 50px 15px #a855f7, 0 0 100px 35px #7e22ce, inset 0 0 80px 10px rgba(139,92,246,0.5); animation: pulse 4s ease-in-out infinite; }}
        #koi-ring {{ border-color: #7dd3fc; box-shadow: 0 0 50px 12px #38bdf8, 0 0 100px 30px #0ea5e9, inset 0 0 80px 8px rgba(56,189,248,0.4); animation: pulse 5s ease-in-out infinite; }}
        #fox-ring {{ border-color: #fb923c; box-shadow: 0 0 50px 15px #f97316, 0 0 100px 35px #ea580c, inset 0 0 80px 10px rgba(251,146,60,0.5); animation: pulse 3s ease-in-out infinite; }}
        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.8; transform: scale(1.05); }}
        }}
        #lock-btn {{
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 1000;
            padding: 12px 24px;
            font-size: 18px;
            border-radius: 30px;
            background: red;
            color: white;
            border: none;
            cursor: pointer;
            box-shadow: 0 0 20px red;
        }}
        #lock-btn.locked {{ background: green; box-shadow: 0 0 20px green; }}
    </style>
</head>
<body>
    <button id="owl-ring" class="ring-button">Owl</button>
    <button id="koi-ring" class="ring-button">Koi</button>
    <button id="fox-ring" class="ring-button">Fox</button>
    <button id="lock-btn">Unlock Dragging</button>

    <script>
        const defaultPos = {{ 'owl-ring': {{x:20, y:35}}, 'koi-ring': {{x:50, y:55}}, 'fox-ring': {{x:80, y:40}} }};
        let pos = {{ ...defaultPos }};
        Object.keys(pos).forEach(id => {{
            let saved = localStorage.getItem(id);
            if (saved) pos[id] = JSON.parse(saved);
            let el = document.getElementById(id);
            el.style.left = pos[id].x + 'vw';
            el.style.top = pos[id].y + 'vh';
        }});

        let dragging = null;
        let offset = {{x:0, y:0}};
        let locked = false;

        document.getElementById('lock-btn').addEventListener('click', () => {{
            locked = !locked;
            document.getElementById('lock-btn').textContent = locked ? 'Lock Positions' : 'Unlock Dragging';
            document.getElementById('lock-btn').classList.toggle('locked', locked);
            document.querySelectorAll('.ring-button').forEach(b => b.style.cursor = locked ? 'default' : 'move');
        }});

        document.querySelectorAll('.ring-button').forEach(btn => {{
            btn.addEventListener('mousedown', e => {{
                if (locked) return;
                dragging = btn;
                let rect = btn.getBoundingClientRect();
                offset.x = e.clientX - rect.left;
                offset.y = e.clientY - rect.top;
                e.preventDefault();
            }});

            btn.addEventListener('click', e => {{
                if (dragging) {{ e.preventDefault(); return; }}
                alert(`You chose the ${{btn.textContent.toLowerCase()}} companion!`);
            }});
        }});

        document.addEventListener('mousemove', e => {{
            if (!dragging || locked) return;
            let x = (e.clientX - offset.x) / window.innerWidth * 100;
            let y = (e.clientY - offset.y) / window.innerHeight * 100;
            dragging.style.left = x + 'vw';
            dragging.style.top = y + 'vh';
            pos[dragging.id] = {{x, y}};
        }});

        document.addEventListener('mouseup', () => {{
            if (dragging) {{
                localStorage.setItem(dragging.id, JSON.stringify(pos[dragging.id]));
                dragging = null;
            }}
        }});
    </script>
</body>
</html>
"""

# Important: import from streamlit.components.v1 as components, then use html(...)
html(full_html, height=800, scrolling=False)
