# app.py
import streamlit as st
import streamlit.components.v1 as components
import random
import time
import os
import base64
from datetime import datetime

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="A Little World Made for Ruhii 💗",
    page_icon="🎂",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- IMAGE LOADER (FOR LOCAL & GITHUB / STREAMLIT CLOUD DEPLOYMENTS) ---
def load_image_base64(path_candidates):
    """Finds and encodes image to base64 from a list of candidate paths"""
    for p in path_candidates:
        if os.path.exists(p):
            try:
                with open(p, "rb") as f:
                    encoded = base64.b64encode(f.read()).decode()
                    return f"data:image/jpeg;base64,{encoded}"
            except Exception:
                pass
    return ""

RUHII_PORTRAIT_B64 = load_image_base64([
    "ruhii.jpg",
    "public/ruhii.jpg",
    "public/assets/aistudio/IMG-20260614-WA0010_9d360bed.jpg",
    "assets/aistudio/IMG-20260614-WA0010_9d360bed.jpg"
])

GALLERY_1_B64 = load_image_base64([
    "gallery_1.jpg",
    "public/gallery_1.jpg",
    "public/assets/aistudio/IMG-20260614-WA0008_2481bf8f.jpg",
    "assets/aistudio/IMG-20260614-WA0008_2481bf8f.jpg"
])

GALLERY_2_B64 = load_image_base64([
    "gallery_2.jpg",
    "public/gallery_2.jpg",
    "public/assets/aistudio/WhatsApp_Image_2026-08-22_at_6.52.11_PM__1__e0871e45.jpeg",
    "assets/aistudio/WhatsApp_Image_2026-08-22_at_6.52.11_PM__1__e0871e45.jpeg"
])

GALLERY_3_B64 = load_image_base64([
    "gallery_3.jpg",
    "public/gallery_3.jpg",
    "public/assets/aistudio/WhatsApp_Image_2026-08-22_at_6.52.11_PM_1dcb8110.jpeg",
    "assets/aistudio/WhatsApp_Image_2026-08-22_at_6.52.11_PM_1dcb8110.jpeg"
])

GALLERY_4_B64 = load_image_base64([
    "gallery_4.jpg",
    "public/gallery_4.jpg",
    "public/assets/aistudio/WhatsApp_Image_2026-08-22_at_6.52.02_PM_52075a0d.jpeg",
    "assets/aistudio/WhatsApp_Image_2026-08-22_at_6.52.02_PM_52075a0d.jpeg"
])

GALLERY_ITEMS = [
    {
        "img": GALLERY_1_B64,
        "title": "Royal Traditional Charm 👑",
        "tagline": "Velvet elegance & royal grace • MashAllah pure queen vibes!"
    },
    {
        "img": GALLERY_2_B64,
        "title": "Radiant in Red ❤️",
        "tagline": "That sweet, innocent smile that lights up the whole room! ✨"
    },
    {
        "img": GALLERY_3_B64,
        "title": "Peaceful in White 🕊️",
        "tagline": "Sukoon aur Saadgi ki misaal • An angel in human form 🤍"
    },
    {
        "img": GALLERY_4_B64,
        "title": "The Sweet Dark Angel 🖤",
        "tagline": "Masoomiyat + thori si nautanki = 100% certified Ruhii! 🌸"
    }
]

# --- SESSION STATE INITIALIZATION & TIME TRACKING ---
if "countdown_done" not in st.session_state:
    st.session_state.countdown_done = False
if "entered_world" not in st.session_state:
    st.session_state.entered_world = False
if "current_page" not in st.session_state:
    st.session_state.current_page = 1
if "compliment" not in st.session_state:
    st.session_state.compliment = ""
if "show_hug" not in st.session_state:
    st.session_state.show_hug = False

# Secret page & activity tracker state
if "show_secret_page" not in st.session_state:
    st.session_state.show_secret_page = False
if "secret_unlocked" not in st.session_state:
    st.session_state.secret_unlocked = False
if "activity_log" not in st.session_state:
    st.session_state.activity_log = [
        {"time": datetime.now().strftime("%I:%M:%S %p"), "event": "Website opened by Ruhii 🌸"}
    ]
if "page_enter_time" not in st.session_state:
    st.session_state.page_enter_time = time.time()

def log_activity(event_description):
    """Log an activity event with formatted timestamp"""
    st.session_state.activity_log.append({
        "time": datetime.now().strftime("%I:%M:%S %p"),
        "event": event_description
    })

def switch_page(new_page):
    """Switch page and calculate time spent on previous page"""
    time_spent = int(time.time() - st.session_state.page_enter_time)
    page_names = {
        1: "Letter (Birthday Wishes)",
        2: "Duas & Prayers",
        3: "Royal Gallery (Ruhii's Photos)",
        4: "Masti & Pagalpanti",
        5: "Special Message & Hug"
    }
    old_name = page_names.get(st.session_state.current_page, f"Page {st.session_state.current_page}")
    new_name = page_names.get(new_page, f"Page {new_page}")

    log_activity(f"Stayed on {old_name} for {time_spent} seconds")
    log_activity(f"Opened {new_name} ➔")

    st.session_state.current_page = new_page
    st.session_state.page_enter_time = time.time()
    st.session_state.show_hug = False

# --- COMPLIMENTS REPERTOIRE ---
COMPLIMENTS = [
    "Tumhari smile literally kisi ka bhi kharab mood 2 second mein fresh kar sakti hai! ✨",
    "Tum cute bhi ho, sweet bhi ho, aur certified 24/7 troublemaker bhi! 😇😈",
    "Tumhari friendship Netflix ke premium 4K subscription jaisi hai — priceless & irreplaceable! 💎",
    "Tumhare jaisi pagal aur loving dost milna sirf kismat walon ka naseeb hota hai! 🍀",
    "Duniya ek taraf, aur Ruhii ki drama queen vibes ek taraf! Full cinematic experience! 🎬👑",
    "Allah ne tumhe banate waqt thori zyada sweetness aur bohat saari masti daal di thi! 🍬",
    "Tumhare saath 5 minute baat karne se saara stress gayab ho jata hai. Free therapy! 🌸",
    "Tumhare jokes chahe kitne bhi lame hon, tumhari hansi dekh kar sabko hansi aa hi jati hai! 🤣",
    "Ek hoti hain achi dost, aur ek hoti hai Ruhii — purest soul with a heart of pure gold! 💖",
    "Jitna bhi nakhre dikha lo madam, tumhari kindness humesha dil jeet leti hai! 🕊️"
]

# --- DUAS WITH SWEET EMOJIS (NO NUMBERING) ---
DUAS_DATA = [
    {"start": "🤲 🌸", "text": "Allah tumhari har jaiz dua qabool farmaye.", "end": "🤍"},
    {"start": "🌿 💖", "text": "Allah tumhari zindagi ko sehat, sukoon, khushiyon aur barkaton se bhar de.", "end": "✨"},
    {"start": "🕊️ 🌷", "text": "Tumhare har mushkil raste ko asaan farmaye.", "end": "💫"},
    {"start": "👑 🌟", "text": "Tumhein duniya aur akhirat dono mein kamyabi ata farmaye.", "end": "🌙"},
    {"start": "🥺 🌺", "text": "Tumhari aankhon mein hamesha khushi ke aansu hon, gham ke nahi.", "end": "💗"},
    {"start": "🛡️ 🕊️", "text": "Allah tumhein buri nazar, pareshani aur har takleef se mehfooz rakhe.", "end": "🤲"}
]

# --- UNIVERSAL STYLING & FONTS ---
UNIVERSAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Caveat:wght@500;600;700&family=Comfortaa:wght@500;600;700&family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Dancing+Script:wght@600;700&family=Great+Vibes&family=Outfit:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,600;0,700;1,600&family=Quicksand:wght@400;500;600;700&display=swap');

/* Hide Streamlit default UI chrome */
#MainMenu, header, footer, .stDeployButton {
    display: none !important;
    visibility: hidden !important;
}
div[data-testid="stToolbar"] {
    display: none !important;
}

/* Background & Body */
.stApp {
    background: linear-gradient(135deg, #FFF0F5 0%, #F5E6FA 40%, #FFE4E1 70%, #FFF5EE 100%);
    font-family: 'Outfit', sans-serif;
    color: #4A3E4E;
    overflow-x: hidden;
}

/* Main Container Padding */
.block-container {
    padding-top: 1.2rem !important;
    padding-bottom: 3.5rem !important;
    max-width: 820px !important;
}

/* Glassmorphism Cards */
.glass-card {
    background: rgba(255, 255, 255, 0.78);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-radius: 28px;
    border: 1.5px solid rgba(255, 215, 230, 0.75);
    padding: 30px 28px;
    box-shadow: 0 15px 35px rgba(220, 160, 195, 0.22), 0 5px 15px rgba(255, 255, 255, 0.7) inset;
    margin-bottom: 24px;
    transition: all 0.4s ease;
}

.glass-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 20px 45px rgba(220, 140, 185, 0.28), 0 5px 20px rgba(255, 255, 255, 0.8) inset;
}

/* Typography styles */
.title-greatvibes {
    font-family: 'Great Vibes', cursive;
    font-size: 3.8rem;
    font-weight: 700;
    color: #C2417C;
    text-shadow: 0 4px 18px rgba(219, 39, 119, 0.25);
    line-height: 1.2;
    text-align: center;
    margin-bottom: 6px;
}

.subtitle-caveat {
    font-family: 'Caveat', cursive;
    font-size: 1.85rem;
    font-weight: 700;
    color: #6A1B9A;
    text-align: center;
    margin-bottom: 22px;
    line-height: 1.3;
}

.letter-caveat {
    font-family: 'Caveat', cursive;
    font-size: 1.85rem;
    line-height: 1.7;
    color: #4A2840;
}

/* Ultra Stylish Bulletin Card */
.stylish-bulletin {
    background: linear-gradient(135deg, rgba(255, 240, 246, 0.95) 0%, rgba(255, 245, 250, 0.95) 100%);
    border: 2px solid rgba(240, 98, 146, 0.6);
    border-radius: 24px;
    padding: 22px 26px;
    margin-bottom: 20px;
    box-shadow: 0 10px 25px rgba(240, 98, 146, 0.2), inset 0 1px 0 rgba(255, 255, 255, 0.8);
    position: relative;
    overflow: hidden;
}

.bulletin-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 14px;
    background: linear-gradient(135deg, #FF4081, #E91E63);
    color: white;
    border-radius: 50px;
    font-family: 'Comfortaa', cursive;
    font-weight: 700;
    font-size: 0.8rem;
    letter-spacing: 1px;
    text-transform: uppercase;
    box-shadow: 0 4px 12px rgba(233, 30, 99, 0.35);
    margin-bottom: 12px;
}

.bulletin-text {
    font-family: 'Outfit', sans-serif;
    font-size: 1.15rem;
    color: #4A152E;
    line-height: 1.6;
    font-weight: 600;
}

/* Portrait Glowing Ring */
.portrait-glow-ring {
    position: relative;
    display: inline-block;
    padding: 6px;
    border-radius: 50%;
    background: linear-gradient(135deg, #FF4081, #AB47BC, #FF69B4, #FFA07A);
    box-shadow: 0 0 35px rgba(255, 64, 129, 0.5), 0 0 15px rgba(171, 71, 188, 0.4);
    animation: portraitPulse 3s ease-in-out infinite;
}

@keyframes portraitPulse {
    0%, 100% { transform: scale(1); box-shadow: 0 0 25px rgba(255, 64, 129, 0.5); }
    50% { transform: scale(1.03); box-shadow: 0 0 40px rgba(233, 30, 99, 0.7); }
}

.portrait-img {
    width: 210px;
    height: 210px;
    border-radius: 50%;
    object-fit: cover;
    display: block;
    border: 4px solid #FFFFFF;
}

/* Gallery Photo Cards */
.gallery-card {
    background: rgba(255, 255, 255, 0.85);
    border-radius: 24px;
    padding: 16px;
    border: 2px solid rgba(255, 182, 193, 0.7);
    box-shadow: 0 10px 25px rgba(220, 160, 195, 0.2);
    margin-bottom: 20px;
    transition: all 0.35s ease;
    text-align: center;
}
.gallery-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 16px 35px rgba(219, 39, 119, 0.25);
    border-color: #F06292;
}
.gallery-img-wrapper {
    width: 100%;
    border-radius: 18px;
    overflow: hidden;
    margin-bottom: 12px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
}
.gallery-img-wrapper img {
    width: 100%;
    height: 380px;
    object-fit: cover;
    display: block;
    transition: transform 0.4s ease;
}
.gallery-card:hover .gallery-img-wrapper img {
    transform: scale(1.03);
}

/* Custom Streamlit Buttons */
div.stButton > button {
    background: linear-gradient(135deg, #FF69B4 0%, #DA70D6 50%, #FF8DA1 100%) !important;
    color: #FFFFFF !important;
    font-family: 'Comfortaa', cursive !important;
    font-weight: 700 !important;
    font-size: 1.05rem !important;
    padding: 0.65rem 1.6rem !important;
    border-radius: 50px !important;
    border: none !important;
    box-shadow: 0 8px 22px rgba(219, 39, 119, 0.35) !important;
    transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    width: 100% !important;
    letter-spacing: 0.5px !important;
}

div.stButton > button:hover {
    transform: scale(1.03) translateY(-2px) !important;
    box-shadow: 0 12px 28px rgba(219, 39, 119, 0.48) !important;
    color: #FFFFFF !important;
}

div.stButton > button:active {
    transform: scale(0.98) !important;
}

/* Dua Cards */
.dua-card-new {
    background: rgba(255, 255, 255, 0.9);
    border-left: 5px solid #BA68C8;
    border-radius: 20px;
    padding: 16px 20px;
    margin-bottom: 14px;
    box-shadow: 0 6px 18px rgba(200, 160, 220, 0.18);
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.dua-card-new:hover {
    transform: translateX(6px);
    background: #FFFFFF;
    box-shadow: 0 10px 24px rgba(186, 104, 200, 0.28);
}
.dua-text-stylish {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.45rem;
    font-weight: 600;
    color: #3E1E45;
    line-height: 1.4;
    flex-grow: 1;
}

/* Decent, Clean & Elegant Pagalpanti Quotes Cards */
.masti-card-decent {
    background: linear-gradient(135deg, rgba(255, 255, 255, 0.92) 0%, rgba(255, 245, 240, 0.92) 100%);
    border: 1.5px solid rgba(255, 183, 161, 0.6);
    border-radius: 20px;
    padding: 18px 22px;
    margin-bottom: 15px;
    font-family: 'Outfit', sans-serif;
    font-size: 1.08rem;
    font-weight: 500;
    color: #3D2232;
    line-height: 1.6;
    box-shadow: 0 6px 18px rgba(255, 171, 145, 0.15);
    display: flex;
    align-items: center;
    gap: 16px;
    transition: all 0.3s ease;
}
.masti-card-decent:hover {
    transform: translateY(-2px);
    border-color: #FF8A65;
    box-shadow: 0 10px 24px rgba(255, 138, 101, 0.22);
}

/* Animations */
@keyframes heartPulse {
    0% { transform: scale(1); }
    15% { transform: scale(1.15); }
    30% { transform: scale(1); }
    45% { transform: scale(1.22); }
    60% { transform: scale(1); }
}
.pulsing-heart {
    display: inline-block;
    animation: heartPulse 1.8s infinite ease-in-out;
}

@keyframes softFloat {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-10px) rotate(2deg); }
}
.soft-float {
    animation: softFloat 4s ease-in-out infinite;
}
</style>
"""
st.markdown(UNIVERSAL_CSS, unsafe_allow_html=True)

# --- COMPLETE FULL-PAGE CONTINUOUS LIVE MOVING EMOJI SNOWFALL (TOP TO BOTTOM) ---
def render_complete_page_live_snowfall(theme="hearts"):
    """Spans the entire screen with continuous live emoji snowfall falling top-to-bottom"""
    if theme == "hearts":
        particle_symbol = "['💖', '🌸', '✨', '💕', '🌷', '🎀', '💗', '🌺', '👑']"
        theme_glow = "rgba(255, 182, 193, 0.45)"
    elif theme == "stars":
        particle_symbol = "['✨', '⭐', '🌟', '🤍', '🌙', '💫', '🕊️', '🌸', '💎']"
        theme_glow = "rgba(218, 112, 214, 0.4)"
    elif theme == "gallery":
        particle_symbol = "['👑', '📸', '✨', '💖', '🌸', '💎', '🌷', '💐']"
        theme_glow = "rgba(255, 192, 203, 0.45)"
    elif theme == "confetti":
        particle_symbol = "['🎉', '🎈', '🤣', '💖', '🧁', '⭐', '🎊', '🍰', '🎁']"
        theme_glow = "rgba(255, 160, 122, 0.42)"
    else:
        particle_symbol = "['💗', '✨', '💌', '🌹', '💞', '🌸', '💐', '💖', '👑']"
        theme_glow = "rgba(255, 105, 180, 0.45)"

    html_code = f"""
    <div id="fullpage-snowfall-canvas" style="position:fixed; top:0; left:0; width:100vw; height:100vh; pointer-events:none; z-index:0; overflow:hidden;"></div>
    <script>
    (function() {{
        const container = document.getElementById('fullpage-snowfall-canvas');
        if (!container) return;
        const symbols = {particle_symbol};

        function spawnFallingSnowEmoji() {{
            const p = document.createElement('div');
            const sym = symbols[Math.floor(Math.random() * symbols.length)];
            p.innerText = sym;
            p.style.position = 'absolute';
            p.style.top = '-55px';
            p.style.left = (Math.random() * 97) + 'vw';
            p.style.fontSize = (Math.random() * 22 + 16) + 'px';
            p.style.opacity = Math.random() * 0.65 + 0.35;
            p.style.filter = 'drop-shadow(0 4px 12px {theme_glow})';
            p.style.userSelect = 'none';
            p.style.pointerEvents = 'none';

            const duration = Math.random() * 5.5 + 5.5; // 5.5s to 11s smooth descent
            const drift = (Math.random() - 0.5) * 190;
            const rotation = (Math.random() - 0.5) * 540;

            // Falling from top to bottom like snowfall!
            p.animate([
                {{ transform: 'translateY(0) translateX(0) rotate(0deg) scale(0.8)', opacity: p.style.opacity }},
                {{ transform: `translateY(118vh) translateX(${{drift}}px) rotate(${{rotation}}deg) scale(1.15)`, opacity: 0 }}
            ], {{
                duration: duration * 1000,
                easing: 'cubic-bezier(0.25, 0.46, 0.45, 0.94)',
                fill: 'forwards'
            }});

            container.appendChild(p);
            setTimeout(() => {{ p.remove(); }}, duration * 1000);
        }}

        // Initial burst covering complete page height
        for (let i = 0; i < 26; i++) {{
            setTimeout(spawnFallingSnowEmoji, i * 140);
        }}
        // Continuous downward snowfall stream
        setInterval(spawnFallingSnowEmoji, 320);
    }})();
    </script>
    """
    components.html(html_code, height=0, width=0)

# --- CELEBRATORY CHIMES & BELLS ONLY (VOICE REMOVED AS REQUESTED) ---
def play_celebration_bells():
    """Play melodic celebratory chimes and bells via Web Audio API"""
    chimes_js = """
    <script>
    (function() {
        try {
            const AudioContext = window.AudioContext || window.webkitAudioContext;
            if (AudioContext) {
                const ctx = new AudioContext();
                const notes = [523.25, 659.25, 783.99, 1046.50, 1318.51];
                notes.forEach((freq, i) => {
                    setTimeout(() => {
                        const osc = ctx.createOscillator();
                        const gain = ctx.createGain();
                        osc.type = 'triangle';
                        osc.frequency.setValueAtTime(freq, ctx.currentTime);
                        gain.gain.setValueAtTime(0.12, ctx.currentTime);
                        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.65);
                        osc.connect(gain);
                        gain.connect(ctx.destination);
                        osc.start();
                        osc.stop(ctx.currentTime + 0.65);
                    }, i * 140);
                });
            }
        } catch(e) {
            console.log(e);
        }
    })();
    </script>
    """
    components.html(chimes_js, height=0, width=0)

# ==============================================================================
# 1. OPENING EXPERIENCE - AUTOMATIC COUNTDOWN & GRAND REVEAL WITH PHOTO
# ==============================================================================
if not st.session_state.entered_world:
    render_complete_page_live_snowfall("hearts")

    if not st.session_state.countdown_done:
        countdown_placeholder = st.empty()

        # Step 0: Welcome greeting
        countdown_placeholder.markdown("""
        <div style="text-align: center; padding: 60px 20px;">
            <div style="font-size: 3.5rem; margin-bottom: 12px;" class="soft-float">👀 💗</div>
            <h1 class="title-greatvibes" style="font-size: 4.5rem;">Hey Ruhii!</h1>
            <p style="font-family: 'Comfortaa', cursive; font-size: 1.35rem; font-weight: 700; color: #7B3F61; margin-top: 15px;">
                Someone has a very special surprise for you... ✨
            </p>
            <p style="font-size: 1.05rem; color: #9E6B89; font-style: italic;">
                Hold your breath! Starting the countdown...
            </p>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(2.0)

        # Step 1: Countdown 3
        countdown_placeholder.markdown("""
        <div style="text-align: center; padding: 70px 20px;">
            <div style="font-family: 'Comfortaa', cursive; font-size: 1.3rem; font-weight: 700; color: #BA68C8; letter-spacing: 2px; text-transform: uppercase;">
                Are you ready, Ruhii?
            </div>
            <div style="font-family: 'Dancing Script', cursive; font-size: 7.5rem; font-weight: 700; color: #FF4081; text-shadow: 0 0 40px rgba(255, 64, 129, 0.6); margin: 15px 0;">
                3...
            </div>
            <p style="font-family: 'Comfortaa', cursive; font-size: 1.2rem; color: #7B3F61; font-weight: 600;">A little magic is brewing 🌸</p>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(1.3)

        # Step 2: Countdown 2
        countdown_placeholder.markdown("""
        <div style="text-align: center; padding: 70px 20px;">
            <div style="font-family: 'Comfortaa', cursive; font-size: 1.3rem; font-weight: 700; color: #BA68C8; letter-spacing: 2px; text-transform: uppercase;">
                Smile please! 😌
            </div>
            <div style="font-family: 'Dancing Script', cursive; font-size: 8rem; font-weight: 700; color: #E040FB; text-shadow: 0 0 45px rgba(224, 64, 251, 0.65); margin: 15px 0;">
                2...
            </div>
            <p style="font-family: 'Comfortaa', cursive; font-size: 1.2rem; color: #7B3F61; font-weight: 600;">Dhadkanein tez ho rahi hain? 💓</p>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(1.3)

        # Step 3: Countdown 1
        countdown_placeholder.markdown("""
        <div style="text-align: center; padding: 70px 20px;">
            <div style="font-family: 'Comfortaa', cursive; font-size: 1.3rem; font-weight: 700; color: #BA68C8; letter-spacing: 2px; text-transform: uppercase;">
                Here it comes! 🎉
            </div>
            <div style="font-family: 'Dancing Script', cursive; font-size: 8.5rem; font-weight: 700; color: #FF1744; text-shadow: 0 0 50px rgba(255, 23, 68, 0.7); margin: 15px 0;">
                1...
            </div>
            <p style="font-family: 'Comfortaa', cursive; font-size: 1.2rem; color: #7B3F61; font-weight: 600;">Close your eyes & make a wish! 🌟</p>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(1.3)

        st.session_state.countdown_done = True
        st.rerun()

    else:
        # GRAND BIRTHDAY REVEAL SCREEN WITH PHOTO & CELEBRATORY BELLS
        st.balloons()
        play_celebration_bells()

        photo_markup = ""
        if RUHII_PORTRAIT_B64:
            photo_markup = f"""
            <div style="text-align: center; margin: 15px 0 20px;">
                <div class="portrait-glow-ring">
                    <img src="{RUHII_PORTRAIT_B64}" alt="Ruhii" class="portrait-img" />
                </div>
                <div style="margin-top: 10px;">
                    <span style="background: rgba(255, 255, 255, 0.95); padding: 5px 16px; border-radius: 50px; font-family: 'Comfortaa', cursive; font-weight: 700; font-size: 0.85rem; color: #C2185B; box-shadow: 0 4px 15px rgba(219, 39, 119, 0.2); border: 1px solid rgba(255, 182, 193, 0.8);">
                        👑 Birthday Princess Ruhii ✨
                    </span>
                </div>
            </div>
            """

        reveal_html = f"""
        <div style="text-align: center; padding: 20px 15px 30px;">
            <div style="font-size: 2.8rem; margin-bottom: 6px;">
                🎈 ✨ 👑 💖 🥳 🎈
            </div>

            <h1 style="font-family: 'Dancing Script', cursive; font-size: 3.8rem; font-weight: 700;
                       background: linear-gradient(135deg, #FF1493, #9C27B0, #FF69B4);
                       -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                       text-shadow: 0 6px 25px rgba(255, 20, 147, 0.35); margin: 5px 0 8px;">
                HAPPY BIRTHDAY RUHII! 🎂
            </h1>

            <div style="font-family: 'Playfair Display', serif; font-style: italic; font-size: 1.25rem; color: #C2417C; font-weight: 600; margin-bottom: 18px;">
                "A Little World Made for Ruhii 💗"
            </div>

            {photo_markup}

            <div class="glass-card" style="max-width: 620px; margin: 0 auto 25px; border: 2px solid rgba(255, 182, 193, 0.8);">
                <div style="font-size: 1.5rem; margin-bottom: 10px;">
                    🎂 🕯️ 🕯️ 🕯️ ✨
                </div>

                <p style="font-family: 'Comfortaa', cursive; font-size: 1.2rem; font-weight: 700; color: #532C4A; line-height: 1.6; margin-bottom: 10px;">
                    Made with a little madness, endless duas, and lots of love.
                </p>

                <p style="font-size: 0.98rem; color: #8F557C; margin-bottom: 0;">
                    Aaj ka har pal sirf tumhari muskurahat ke naam hai! ✨
                </p>
            </div>
        </div>
        """
        st.markdown(reveal_html, unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 4, 1])
        with col2:
            if st.button("Okay Princess, Enter Your World 💗", key="btn_enter_world"):
                st.session_state.entered_world = True
                st.session_state.current_page = 1
                st.session_state.page_enter_time = time.time()
                log_activity("Entered Main Birthday World 🌸")
                st.rerun()

    st.stop()


# ==============================================================================
# SECRET PAGE (PASSWORD-PROTECTED RUHII ACTIVITY & HISTORY TRACKER)
# ==============================================================================
if st.session_state.show_secret_page:
    render_complete_page_live_snowfall("stars")

    st.markdown("""
    <div style="text-align: center; margin-top: 10px; margin-bottom: 15px;">
        <h1 class="title-greatvibes" style="color: #8E24AA; font-size: 3.5rem;">Ruhii's Secret Journey Log 🔒</h1>
        <p style="font-family: 'Comfortaa', cursive; font-size: 1.05rem; font-weight: 600; color: #6A1B9A;">
            Confidential Diary & Real-Time Bestie Activity Tracker
        </p>
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.secret_unlocked:
        st.markdown("""
        <div class="glass-card" style="text-align: center; max-width: 500px; margin: 0 auto; border: 2px solid #BA68C8;">
            <div style="font-size: 3.5rem; margin-bottom: 12px;">🔐 ✨ 💖</div>
            <h3 style="font-family: 'Comfortaa', cursive; color: #6A1B9A; font-weight: 700; margin-bottom: 10px;">
                Enter Bestie Passcode
            </h3>
            <p style="font-family: 'Outfit', sans-serif; font-size: 0.95rem; color: #5B2C4E; margin-bottom: 18px;">
                This secret portal records every timestamp, page open duration, and action Ruhii takes on this website.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col_pw1, col_pw2, col_pw3 = st.columns([1, 2, 1])
        with col_pw2:
            pwd = st.text_input("Password", type="password", placeholder="Enter secret password (default: bestie)", key="pwd_input")
            if st.button("Unlock History 🔓", key="btn_unlock"):
                if pwd.strip().lower() in ["bestie", "ruhii", "ruhii123", "love"]:
                    st.session_state.secret_unlocked = True
                    st.rerun()
                else:
                    st.error("Incorrect passcode! Only Ruhii's bestie knows the secret word.")

            if st.button("Back to Website ↩️", key="btn_back_from_secret_locked"):
                st.session_state.show_secret_page = False
                st.rerun()

    else:
        st.markdown("""
        <div class="glass-card" style="border: 2px solid #BA68C8;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 18px;">
                <h3 style="font-family: 'Comfortaa', cursive; color: #6A1B9A; font-weight: 700; margin: 0;">
                    📊 Ruhii's Real-Time Session Story
                </h3>
                <span style="background: #E1BEE7; color: #4A148C; font-size: 0.8rem; font-weight: 700; padding: 4px 12px; border-radius: 50px;">
                    LIVE TRACKING
                </span>
            </div>
            <p style="font-family: 'Outfit', sans-serif; font-size: 0.95rem; color: #5C324E; margin-bottom: 16px;">
                Here is the exact record of which surprises Ruhii explored, when she visited them, and how long she spent admiring each page:
            </p>
        """, unsafe_allow_html=True)

        for idx, item in enumerate(st.session_state.activity_log, 1):
            st.markdown(f"""
            <div style="display: flex; align-items: center; justify-content: space-between; padding: 10px 16px; margin-bottom: 8px; background: rgba(255, 255, 255, 0.9); border-radius: 14px; border-left: 4px solid #AB47BC; font-family: 'Outfit', sans-serif;">
                <span style="font-weight: 600; color: #3E1E45;">{item['event']}</span>
                <span style="font-size: 0.85rem; font-weight: 700; color: #8E24AA; background: #F3E5F5; padding: 3px 10px; border-radius: 12px;">{item['time']}</span>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)

        col_b1, col_b2 = st.columns([1, 1])
        with col_b1:
            if st.button("Lock & Return to Surprises 🔒", key="btn_close_secret"):
                st.session_state.show_secret_page = False
                st.session_state.secret_unlocked = False
                st.rerun()
        with col_b2:
            if st.button("Clear Log 🧹", key="btn_clear_log"):
                st.session_state.activity_log = [
                    {"time": datetime.now().strftime("%I:%M:%S %p"), "event": "Log refreshed"}
                ]
                st.rerun()

    st.stop()


# ==============================================================================
# 2. MAIN EXPERIENCE - CONTENT AT TOP (FIVE SEPARATE PAGES)
# ==============================================================================

# Background theme per page with complete full-page downward live snowfall
bg_themes = {1: "hearts", 2: "stars", 3: "gallery", 4: "confetti", 5: "hearts"}
render_complete_page_live_snowfall(bg_themes.get(st.session_state.current_page, "hearts"))


# ------------------------------------------------------------------------------
# PAGE 1: BIRTHDAY WISHES 💌
# ------------------------------------------------------------------------------
if st.session_state.current_page == 1:
    st.markdown("""
    <div style="text-align: center; margin-top: 5px; margin-bottom: 18px;">
        <h1 class="title-greatvibes">A Special Day for a Special Soul 💌</h1>
        <p class="subtitle-caveat">
            "Aj ka din sirf tumhara hai, madam! Toh smile karna compulsory hai. 😌"
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Main Letter Card
    st.markdown("""
    <div class="glass-card">
        <div style="text-align: center; font-size: 2.2rem; margin-bottom: 12px;">
            🌸 💌 💖
        </div>
        <div style="font-family: 'Cormorant Garamond', serif; font-style: italic; font-size: 2.2rem; font-weight: 700; color: #880E4F; margin-bottom: 14px;">
            Dear Ruhii,
        </div>
        <div class="letter-caveat" style="margin-bottom: 18px;">
            Happy Birthday to one of the most special people in my life. Tumhari friendship meri life ka ek beautiful part hai. I hope tumhari life hamesha happiness, success, laughter aur beautiful memories se filled rahe.
        </div>
        <div class="letter-caveat" style="margin-bottom: 22px;">
            Hamesha aise hi smile karti rehna because your smile deserves the whole universe.
        </div>
        <div style="text-align: right; font-family: 'Great Vibes', cursive; font-size: 2.5rem; color: #C2185B; font-weight: 700;">
            With endless love & blessings, Always 💗
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Ultra Stylish Bulletin Card
    st.markdown("""
    <div class="stylish-bulletin">
        <div class="bulletin-badge">
            <span>🚨</span>
            <span>Special Birthday Bulletin</span>
            <span>✨</span>
        </div>
        <div class="bulletin-text">
            "Breaking News: Aaj duniya ki sabse cute aur thori si pagal larki ka birthday hai! 😂 Sources confirm that madam is officially required to smile nonstop all day!"
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Navigation Buttons
    col_p1, col_p2 = st.columns([1, 1])
    with col_p1:
        if st.button("🏠 Home", key="btn_home_p1"):
            st.session_state.entered_world = False
            st.session_state.countdown_done = True
            log_activity("Returned to Home Reveal Screen 🏠")
            st.rerun()
    with col_p2:
        if st.button("Next: Unlock Duas 🤲", key="btn_next_p1"):
            switch_page(2)
            st.rerun()


# ------------------------------------------------------------------------------
# PAGE 2: DUAS AND BLESSINGS 🤲 (NO NUMBERING, STYLISH FONT, CUTE EMOJIS)
# ------------------------------------------------------------------------------
elif st.session_state.current_page == 2:
    st.markdown("""
    <div style="text-align: center; margin-top: 5px; margin-bottom: 18px;">
        <h1 class="title-greatvibes" style="color: #8E24AA;">Prayers From My Heart 🤲</h1>
        <p class="subtitle-caveat" style="color: #6A1B9A;">
            "Allah tumhari zindagi ko khushiyon aur barkaton se bhar de. Ameen! 🤍"
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card" style="background: rgba(255, 255, 255, 0.82); border-color: rgba(206, 147, 216, 0.6);">
        <div style="text-align: center; font-size: 2.2rem; margin-bottom: 18px;">
            ✨ 🌙 🕊️ 🤲 ✨
        </div>
    """, unsafe_allow_html=True)

    for item in DUAS_DATA:
        st.markdown(f"""
        <div class="dua-card-new">
            <span style="font-size: 1.5rem; margin-right: 12px; select: none;">{item['start']}</span>
            <div class="dua-text-stylish">{item['text']}</div>
            <span style="font-size: 1.3rem; margin-left: 10px; select: none;">{item['end']}</span>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div style="text-align: center; margin-top: 25px; padding: 14px; background: linear-gradient(135deg, rgba(234, 187, 240, 0.35), rgba(255, 214, 230, 0.45)); border-radius: 20px;">
            <div style="font-family: 'Great Vibes', cursive; font-size: 2.8rem; font-weight: 700; color: #7B1FA2;">
                Ameen Sum Ameen! 🤲 🤍
            </div>
            <div style="font-family: 'Comfortaa', cursive; font-size: 0.95rem; color: #6A1B9A; font-weight: 600; margin-top: 4px;">
                May every single angel whisper Ameen to these prayers for you!
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Navigation Buttons (Advances to new Gallery page!)
    c_prev2, c_next2 = st.columns([1, 1])
    with c_prev2:
        if st.button("⬅️ Previous", key="btn_prev_p2"):
            switch_page(1)
            st.rerun()
    with c_next2:
        if st.button("Ruhii's Royal Gallery 📸 👑", key="btn_next_p2"):
            switch_page(3)
            st.rerun()


# ------------------------------------------------------------------------------
# NEW PAGE 3: RUHII'S ROYAL PHOTO GALLERY 📸 👑 (RIGHT AFTER DUAS!)
# ------------------------------------------------------------------------------
elif st.session_state.current_page == 3:
    st.markdown("""
    <div style="text-align: center; margin-top: 5px; margin-bottom: 18px;">
        <div style="display: inline-block; padding: 5px 18px; border-radius: 50px; background: linear-gradient(135deg, #FF4081, #AB47BC); color: white; font-family: 'Comfortaa', cursive; font-size: 0.85rem; font-weight: 700; margin-bottom: 8px;">
            📸 The Queen's Visual Diary ✨
        </div>
        <h1 class="title-greatvibes" style="color: #C2185B;">Ruhii's Royal Moments 👑</h1>
        <p class="subtitle-caveat" style="color: #7B1FA2;">
            "Har photo mein ek alag hi noor aur masoomiyat hai! MashAllah 🤍"
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 4 Photo Cards Grid
    col_g1, col_g2 = st.columns(2)

    for idx, item in enumerate(GALLERY_ITEMS):
        target_col = col_g1 if idx % 2 == 0 else col_g2
        with target_col:
            img_html = ""
            if item["img"]:
                img_html = f"""
                <div class="gallery-img-wrapper">
                    <img src="{item['img']}" alt="{item['title']}" />
                </div>
                """
            st.markdown(f"""
            <div class="gallery-card">
                {img_html}
                <h4 style="font-family: 'Comfortaa', cursive; font-weight: 700; color: #880E4F; font-size: 1.05rem; margin-bottom: 6px;">
                    {item['title']}
                </h4>
                <p style="font-family: 'Outfit', sans-serif; font-size: 0.88rem; color: #5C324E; font-weight: 500; line-height: 1.5; margin: 0;">
                    {item['tagline']}
                </p>
            </div>
            """, unsafe_allow_html=True)

    # Navigation Buttons
    c_prev3, c_next3 = st.columns([1, 1])
    with c_prev3:
        if st.button("⬅️ Previous (Duas)", key="btn_prev_p3"):
            switch_page(2)
            st.rerun()
    with c_next3:
        if st.button("Chalo Ab Thori Masti Ho Jaye 😂", key="btn_next_p3"):
            switch_page(4)
            st.rerun()


# ------------------------------------------------------------------------------
# PAGE 4: FUNNY AND CUTE SECTION 😂 (DECENT, ELEGANT FONTS, NO POINTING HANDS)
# ------------------------------------------------------------------------------
elif st.session_state.current_page == 4:
    st.markdown("""
    <div style="text-align: center; margin-top: 5px; margin-bottom: 18px;">
        <h1 class="title-greatvibes" style="color: #E64A19;">Ruhii Ki Pagalpanti Department 😂</h1>
        <p class="subtitle-caveat" style="color: #D84315;">
            "Warning: Is page ko dekh kar hansna mana nahi hai! 🤣"
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card" style="border: 2px dashed #FFAB91;">
        <div style="text-align: center; font-size: 2.4rem; margin-bottom: 12px;">
            🤪 🍰 🍟 🎭 👑
        </div>
        <h3 style="text-align: center; font-family: 'Comfortaa', cursive; color: #D84315; font-weight: 700; margin-bottom: 18px;">
            Official Birthday Truths 📢
        </h3>
    """, unsafe_allow_html=True)

    roasts_clean = [
        {"icon": "🏆", "text": "Congratulations! Tum officially ek saal aur experienced ho gayi ho... lekin harkatein abhi bhi bachon wali hain. 😂"},
        {"icon": "🎂", "text": "Cake tumhara hai, lekin khaane ka haq mera bhi banta hai."},
        {"icon": "⏳", "text": "Tumhari age increase ho rahi hai, maturity abhi bhi loading hai... 2%. 🤣"},
        {"icon": "✨", "text": "Aaj tumhari har wish poori ho, bas mujhe tang karne wali wishes exclude hain."}
    ]

    for item in roasts_clean:
        st.markdown(f"""
        <div class="masti-card-decent">
            <span style="font-size: 1.7rem; select: none;">{item['icon']}</span>
            <div>{item['text']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Interactive Compliment Generator with decent font
    st.markdown("""
    <div class="glass-card" style="text-align: center; background: rgba(255, 255, 255, 0.88); border: 2px solid #FF80AB;">
        <div style="font-size: 2rem; margin-bottom: 8px;">🎁 💝 👑</div>
        <h3 style="font-family: 'Comfortaa', cursive; color: #C2185B; font-weight: 700; margin-bottom: 10px;">Special Mystery Compliment Generator</h3>
        <p style="font-family: 'Outfit', sans-serif; font-size: 0.98rem; color: #733454; margin-bottom: 18px; font-weight: 500;">
            Press the magic button below to unlock a sweet & funny truth about you!
        </p>
    """, unsafe_allow_html=True)

    if st.button("Reveal My Birthday Compliment 💝", key="btn_compliment"):
        selected_comp = random.choice(COMPLIMENTS)
        st.session_state.compliment = selected_comp
        log_activity(f"Revealed Compliment: '{selected_comp[:35]}...'")

    if st.session_state.compliment:
        st.markdown(f"""
        <div style="margin-top: 18px; padding: 18px 24px; background: linear-gradient(135deg, #FFF0F5, #FCE4EC);
                    border: 2px solid #F06292; border-radius: 20px; box-shadow: 0 8px 25px rgba(240, 98, 146, 0.25);">
            <div style="font-size: 1.8rem; margin-bottom: 6px;">✨ 💖 ✨</div>
            <div style="font-family: 'Outfit', sans-serif; font-size: 1.18rem; font-weight: 600; color: #880E4F; line-height: 1.6;">
                "{st.session_state.compliment}"
            </div>
            <div style="font-family: 'Comfortaa', cursive; font-size: 0.88rem; color: #AD1457; margin-top: 8px; font-weight: 700;">
                (100% Certified Sach! 😌)
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Navigation Buttons
    c_prev4, c_next4 = st.columns([1, 1])
    with c_prev4:
        if st.button("⬅️ Previous (Gallery)", key="btn_prev_p4"):
            switch_page(3)
            st.rerun()
    with c_next4:
        if st.button("Ab Last Surprise Dekho ❤️", key="btn_next_p4"):
            switch_page(5)
            st.rerun()


# ------------------------------------------------------------------------------
# PAGE 5: SPECIAL MESSAGE ❤️ (COOL STYLISH LETTER FONT & SECRET HEART)
# ------------------------------------------------------------------------------
elif st.session_state.current_page == 5:
    st.markdown("""
    <div style="text-align: center; margin-top: 5px; margin-bottom: 18px;">
        <h1 class="title-greatvibes" style="color: #D81B60;">One Last Thing, Ruhii... ❤️</h1>
        <p class="subtitle-caveat" style="color: #AD1457;">
            "Kuch baatein hoti hain jo words mein explain karna mushkil hota hai."
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Emotional Heartfelt Card with cool stylish font
    st.markdown("""
    <div class="glass-card" style="border: 2px solid rgba(244, 143, 177, 0.8);">
        <div style="text-align: center; margin: 10px 0 20px;">
            <div class="pulsing-heart" style="font-size: 5rem; filter: drop-shadow(0 6px 20px rgba(233, 30, 99, 0.4));">
                💖
            </div>
        </div>

        <div class="letter-caveat" style="margin-bottom: 18px;">
            Ruhii, I just want you to know that you are genuinely special. Life mein bohat se log milte hain, lekin kuch log apni presence se har moment ko beautiful bana dete hain. Tum unhi logon mein se ho. May your smile never fade, may your dreams come true, and may happiness always find its way to you.
        </div>

        <div class="letter-caveat" style="margin-bottom: 22px; font-weight: 700; color: #5B2C4E;">
            Thank you for being you. Stay blessed, stay crazy, and never stop smiling.
        </div>

        <div style="text-align: center; padding: 18px; background: linear-gradient(135deg, rgba(255, 192, 203, 0.4), rgba(225, 190, 231, 0.4)); border-radius: 20px; margin-top: 15px;">
            <div style="font-family: 'Cormorant Garamond', serif; font-size: 2.2rem; font-weight: 700; color: #C2185B; letter-spacing: 0.5px;">
                YOU DESERVE ALL THE HAPPINESS IN THE WORLD! 💗
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Hug Feature
    hug_col1, hug_col2, hug_col3 = st.columns([1, 3, 1])
    with hug_col2:
        if st.button("One More Hug? 🤗", key="btn_hug"):
            st.session_state.show_hug = True
            log_activity("Clicked 'One More Hug' 🤗")

    if st.session_state.show_hug:
        st.balloons()
        st.markdown("""
        <div class="glass-card" style="text-align: center; background: linear-gradient(135deg, #FFE4E1, #FFF0F5); border: 2.5px solid #FF4081; margin-top: 20px;">
            <div style="font-size: 4rem;" class="pulsing-heart">🤗 💗 🫂</div>
            <div style="font-family: 'Great Vibes', cursive; font-size: 3.2rem; font-weight: 700; color: #E91E63; margin: 10px 0;">
                SENDING YOU INFINITE HUGS & LOVE! 💗
            </div>
            <p style="font-family: 'Comfortaa', cursive; font-size: 1.05rem; color: #7B2456; font-weight: 700;">
                May your whole year ahead be as soft, warm, and comforting as the biggest hug!
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Navigation Buttons
    col_p5_1, col_p5_2 = st.columns([1, 1])
    with col_p5_1:
        if st.button("⬅️ Previous", key="btn_prev_p5"):
            switch_page(4)
            st.rerun()
    with col_p5_2:
        if st.button("Open My Little Letter 💌", key="btn_restart_to_1"):
            switch_page(1)
            st.rerun()

    # Footer with user-requested dedication: "Made with Love for MY Dear Bestiee ❤️"
    st.markdown("""
    <div style="text-align: center; margin-top: 40px; padding: 20px 0; border-top: 1px dashed rgba(200, 140, 180, 0.4);">
        <p style="font-family: 'Great Vibes', cursive; font-size: 2.4rem; color: #8E4A72; font-weight: 700; margin-bottom: 4px;">
            Made with Love for MY Dear Bestiee ❤️
        </p>
        <p style="font-family: 'Comfortaa', cursive; font-size: 0.85rem; color: #A87093;">
            A Little World Made for Ruhii 💗 • Happy Birthday!
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Discreet Heart Secret Button
    c_sec1, c_sec2, c_sec3 = st.columns([5, 1, 5])
    with c_sec2:
        if st.button("💗", key="btn_secret_heart", help="Special memory portal"):
            st.session_state.show_secret_page = True
            log_activity("Clicked secret heart button 🔒")
            st.rerun()
