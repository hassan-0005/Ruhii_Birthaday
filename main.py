import streamlit as st
import streamlit.components.v1 as components
import random
import time

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="A Little World Made for Ruhii 💗",
    page_icon="🎂",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- SESSION STATE INITIALIZATION ---
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

# --- COMPLIMENTS LIST ---
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

# --- UNIVERSAL STYLING & FONTS ---
UNIVERSAL_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600;700&family=Quicksand:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,600;1,600&display=swap');

/* Hide Streamlit default chrome */
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
    font-family: 'Quicksand', sans-serif;
    color: #4A3E4E;
    overflow-x: hidden;
}

/* Main Container Padding */
.block-container {
    padding-top: 1.8rem !important;
    padding-bottom: 3.5rem !important;
    max-width: 820px !important;
}

/* Glassmorphism Cards */
.glass-card {
    background: rgba(255, 255, 255, 0.72);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-radius: 28px;
    border: 1.5px solid rgba(255, 215, 230, 0.7);
    padding: 30px 28px;
    box-shadow: 0 15px 35px rgba(220, 160, 195, 0.22), 0 5px 15px rgba(255, 255, 255, 0.7) inset;
    margin-bottom: 24px;
    transition: all 0.4s ease;
}

.glass-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 20px 45px rgba(220, 140, 185, 0.28), 0 5px 20px rgba(255, 255, 255, 0.8) inset;
}

/* Page Titles */
.title-script {
    font-family: 'Dancing Script', cursive;
    font-size: 3.2rem;
    font-weight: 700;
    color: #C2417C;
    text-shadow: 0 4px 18px rgba(219, 39, 119, 0.25);
    line-height: 1.25;
    text-align: center;
    margin-bottom: 6px;
}

.subtitle-sweet {
    font-size: 1.15rem;
    font-weight: 600;
    color: #7A537A;
    text-align: center;
    margin-bottom: 22px;
}

/* Custom Streamlit Buttons */
div.stButton > button {
    background: linear-gradient(135deg, #FF69B4 0%, #DA70D6 50%, #FF8DA1 100%) !important;
    color: #FFFFFF !important;
    font-family: 'Quicksand', sans-serif !important;
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

/* Secondary Button Styling */
div[data-testid="stHorizontalBlock"] div.stButton > button {
    font-size: 0.95rem !important;
    padding: 0.55rem 1.1rem !important;
}

/* Dua Cards */
.dua-card {
    background: rgba(255, 255, 255, 0.85);
    border-left: 5px solid #DA70D6;
    border-radius: 18px;
    padding: 16px 20px;
    margin-bottom: 14px;
    box-shadow: 0 6px 18px rgba(200, 160, 220, 0.18);
    transition: all 0.3s ease;
    display: flex;
    align-items: center;
    gap: 14px;
}
.dua-card:hover {
    transform: translateX(6px);
    background: #FFFFFF;
    box-shadow: 0 10px 24px rgba(186, 104, 200, 0.28);
}
.dua-num {
    background: linear-gradient(135deg, #DA70D6, #FF69B4);
    color: white;
    width: 34px;
    height: 34px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 0.95rem;
    flex-shrink: 0;
}
.dua-text {
    font-size: 1.05rem;
    font-weight: 600;
    color: #3E2945;
    line-height: 1.45;
}

/* Funny Quote Cards */
.funny-box {
    background: linear-gradient(135deg, rgba(255, 240, 245, 0.9) 0%, rgba(255, 245, 238, 0.9) 100%);
    border: 2px dashed #FF94B8;
    border-radius: 20px;
    padding: 18px 22px;
    margin-bottom: 16px;
    font-size: 1.05rem;
    font-weight: 600;
    color: #5C324E;
    box-shadow: 0 8px 20px rgba(255, 148, 184, 0.15);
}

/* Progress Bar */
.progress-container {
    background: rgba(255, 255, 255, 0.6);
    border-radius: 50px;
    padding: 4px;
    margin-bottom: 25px;
    border: 1px solid rgba(255, 182, 193, 0.6);
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.progress-pill {
    padding: 6px 14px;
    border-radius: 50px;
    font-size: 0.85rem;
    font-weight: 700;
    color: #8C5D85;
}
.progress-active {
    background: linear-gradient(135deg, #FF69B4, #BA68C8);
    color: white !important;
    box-shadow: 0 4px 12px rgba(219, 39, 119, 0.3);
}

/* Pulse Heart */
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

/* Floating animation */
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

# --- CONTINUOUS BACKGROUND PARTICLES ---
def render_background_animation(theme="hearts"):
    """Render interactive background animations using canvas & CSS"""
    if theme == "hearts":
        particle_symbol = "['💖', '🌸', '✨', '💕', '🌷', '🎀']"
        theme_glow = "rgba(255, 182, 193, 0.25)"
    elif theme == "stars":
        particle_symbol = "['✨', '⭐', '🌟', '🤍', '🌙', '💫']"
        theme_glow = "rgba(218, 112, 214, 0.22)"
    elif theme == "confetti":
        particle_symbol = "['🎉', '🎈', '🤣', '💖', '🧁', '⭐']"
        theme_glow = "rgba(255, 160, 122, 0.25)"
    else:
        particle_symbol = "['💗', '✨', '💌', '🌹', '💞', '🌸']"
        theme_glow = "rgba(255, 105, 180, 0.25)"

    html_code = f"""
    <div id="particle-canvas" style="position:fixed; top:0; left:0; width:100vw; height:100vh; pointer-events:none; z-index:-1; overflow:hidden;"></div>
    <script>
    (function() {{
        const container = document.getElementById('particle-canvas');
        if (!container) return;
        const symbols = {particle_symbol};
        const maxParticles = 28;

        function createParticle() {{
            const p = document.createElement('div');
            const sym = symbols[Math.floor(Math.random() * symbols.length)];
            p.innerText = sym;
            p.style.position = 'absolute';
            p.style.bottom = '-40px';
            p.style.left = (Math.random() * 98) + 'vw';
            p.style.fontSize = (Math.random() * 18 + 14) + 'px';
            p.style.opacity = Math.random() * 0.7 + 0.3;
            p.style.filter = 'drop-shadow(0 2px 8px {theme_glow})';
            p.style.userSelect = 'none';
            p.style.pointerEvents = 'none';

            const duration = Math.random() * 7 + 6; // 6-13s
            const horizontalDrift = (Math.random() - 0.5) * 160;

            p.animate([
                {{ transform: 'translateY(0) translateX(0) rotate(0deg)', opacity: p.style.opacity }},
                {{ transform: `translateY(-115vh) translateX(${{horizontalDrift}}px) rotate(${{Math.random() * 360}}deg)`, opacity: 0 }}
            ], {{
                duration: duration * 1000,
                easing: 'cubic-bezier(0.25, 0.46, 0.45, 0.94)',
                fill: 'forwards'
            }});

            container.appendChild(p);

            setTimeout(() => {{
                p.remove();
            }}, duration * 1000);
        }}

        // Initial burst
        for (let i = 0; i < 14; i++) {{
            setTimeout(createParticle, i * 220);
        }}

        // Ongoing continuous spawn
        setInterval(createParticle, 550);
    }})();
    </script>
    """
    components.html(html_code, height=0, width=0)

# ==============================================================================
# 1. OPENING EXPERIENCE - AUTOMATIC COUNTDOWN & GRAND REVEAL
# ==============================================================================
if not st.session_state.entered_world:
    render_background_animation("hearts")

    if not st.session_state.countdown_done:
        # Welcome Screen & Automatic Countdown Container
        countdown_placeholder = st.empty()

        # Step 0: Initial Welcome Greeting
        countdown_placeholder.markdown("""
        <div style="text-align: center; padding: 60px 20px;">
            <div style="font-size: 3.5rem; margin-bottom: 12px;" class="soft-float">👀 💗</div>
            <h1 class="title-script" style="font-size: 3.8rem;">Hey Ruhii!</h1>
            <p style="font-size: 1.35rem; font-weight: 600; color: #7B3F61; margin-top: 15px;">
                Someone has a very special surprise for you... ✨
            </p>
            <p style="font-size: 1.05rem; color: #9E6B89; font-style: italic;">
                Hold your breath! Starting the countdown...
            </p>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(2.0)

        # Step 1: Countdown Number 3
        countdown_placeholder.markdown("""
        <div style="text-align: center; padding: 70px 20px;">
            <div style="font-size: 1.3rem; font-weight: 700; color: #BA68C8; letter-spacing: 2px; text-transform: uppercase;">
                Are you ready, Ruhii?
            </div>
            <div style="font-family: 'Dancing Script', cursive; font-size: 7.5rem; font-weight: 700; color: #FF4081; text-shadow: 0 0 40px rgba(255, 64, 129, 0.6); margin: 15px 0;">
                3...
            </div>
            <p style="font-size: 1.2rem; color: #7B3F61; font-weight: 600;">A little magic is brewing 🌸</p>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(1.3)

        # Step 2: Countdown Number 2
        countdown_placeholder.markdown("""
        <div style="text-align: center; padding: 70px 20px;">
            <div style="font-size: 1.3rem; font-weight: 700; color: #BA68C8; letter-spacing: 2px; text-transform: uppercase;">
                Smile please! 😌
            </div>
            <div style="font-family: 'Dancing Script', cursive; font-size: 8rem; font-weight: 700; color: #E040FB; text-shadow: 0 0 45px rgba(224, 64, 251, 0.65); margin: 15px 0;">
                2...
            </div>
            <p style="font-size: 1.2rem; color: #7B3F61; font-weight: 600;">Dhadkanein tez ho rahi hain? 💓</p>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(1.3)

        # Step 3: Countdown Number 1
        countdown_placeholder.markdown("""
        <div style="text-align: center; padding: 70px 20px;">
            <div style="font-size: 1.3rem; font-weight: 700; color: #BA68C8; letter-spacing: 2px; text-transform: uppercase;">
                Here it comes! 🎉
            </div>
            <div style="font-family: 'Dancing Script', cursive; font-size: 8.5rem; font-weight: 700; color: #FF1744; text-shadow: 0 0 50px rgba(255, 23, 68, 0.7); margin: 15px 0;">
                1...
            </div>
            <p style="font-size: 1.2rem; color: #7B3F61; font-weight: 600;">Close your eyes & make a wish! 🌟</p>
        </div>
        """, unsafe_allow_html=True)
        time.sleep(1.3)

        st.session_state.countdown_done = True
        st.rerun()

    else:
        # GRAND BIRTHDAY REVEAL SCREEN!
        st.balloons()

        reveal_html = """
        <div style="text-align: center; padding: 25px 15px 35px;">
            <!-- Floating Balloons & Emojis Header -->
            <div style="font-size: 2.8rem; margin-bottom: 8px;">
                🎈 ✨ 🎂 💖 🥳 🎈
            </div>

            <!-- Grand Birthday Heading -->
            <h1 style="font-family: 'Dancing Script', cursive; font-size: 3.8rem; font-weight: 700;
                       background: linear-gradient(135deg, #FF1493, #9C27B0, #FF69B4);
                       -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                       text-shadow: 0 6px 25px rgba(255, 20, 147, 0.35); margin: 5px 0 10px;">
                HAPPY BIRTHDAY RUHII! 🎂
            </h1>

            <div style="font-family: 'Playfair Display', serif; font-style: italic; font-size: 1.25rem; color: #C2417C; font-weight: 600; margin-bottom: 25px;">
                "A Little World Made for Ruhii 💗"
            </div>

            <!-- Glass Card with Cake & Tagline -->
            <div class="glass-card" style="max-width: 620px; margin: 0 auto 30px; border: 2px solid rgba(255, 182, 193, 0.8);">
                <!-- Animated Birthday Cake Illustration -->
                <div style="font-size: 4.8rem; margin-bottom: 10px;" class="pulsing-heart">
                    🎂
                </div>
                <div style="font-size: 1.5rem; margin-bottom: 14px;">
                    🕯️ 🕯️ 🕯️
                </div>

                <p style="font-size: 1.25rem; font-weight: 600; color: #532C4A; line-height: 1.6; margin-bottom: 12px;">
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
                st.rerun()

    st.stop()


# ==============================================================================
# 2. MAIN EXPERIENCE - FOUR SEPARATE PAGES
# ==============================================================================

# Background theme per page
bg_themes = {1: "hearts", 2: "stars", 3: "confetti", 4: "hearts"}
render_background_animation(bg_themes.get(st.session_state.current_page, "hearts"))

# Header Banner
st.markdown("""
<div style="text-align: center; margin-bottom: 15px;">
    <span style="font-family: 'Dancing Script', cursive; font-size: 2.2rem; font-weight: 700; color: #C2417C;">
        A Little World Made for Ruhii 💗
    </span>
</div>
""", unsafe_allow_html=True)

# Navigation Bar Tabs
nav1, nav2, nav3, nav4 = st.columns(4)

with nav1:
    btn_label_1 = "💌 Letter" if st.session_state.current_page != 1 else "💌 Letter ✨"
    if st.button(btn_label_1, key="nav_tab_1"):
        st.session_state.current_page = 1
        st.session_state.show_hug = False
        st.rerun()

with nav2:
    btn_label_2 = "🤲 Duas" if st.session_state.current_page != 2 else "🤲 Duas ✨"
    if st.button(btn_label_2, key="nav_tab_2"):
        st.session_state.current_page = 2
        st.session_state.show_hug = False
        st.rerun()

with nav3:
    btn_label_3 = "😂 Masti" if st.session_state.current_page != 3 else "😂 Masti ✨"
    if st.button(btn_label_3, key="nav_tab_3"):
        st.session_state.current_page = 3
        st.session_state.show_hug = False
        st.rerun()

with nav4:
    btn_label_4 = "❤️ Surprise" if st.session_state.current_page != 4 else "❤️ Surprise ✨"
    if st.button(btn_label_4, key="nav_tab_4"):
        st.session_state.current_page = 4
        st.session_state.show_hug = False
        st.rerun()

# Progress Indicator
current = st.session_state.current_page
p1_cls = "progress-active" if current == 1 else ""
p2_cls = "progress-active" if current == 2 else ""
p3_cls = "progress-active" if current == 3 else ""
p4_cls = "progress-active" if current == 4 else ""

st.markdown(f"""
<div class="progress-container">
    <div class="progress-pill {p1_cls}">Surprise 1 of 4</div>
    <div class="progress-pill {p2_cls}">Surprise 2 of 4</div>
    <div class="progress-pill {p3_cls}">Surprise 3 of 4</div>
    <div class="progress-pill {p4_cls}">Surprise 4 of 4</div>
</div>
""", unsafe_allow_html=True)


# ------------------------------------------------------------------------------
# PAGE 1: BIRTHDAY WISHES 💌
# ------------------------------------------------------------------------------
if st.session_state.current_page == 1:
    st.markdown("""
    <div style="text-align: center;">
        <h1 class="title-script">A Special Day for a Special Soul 💌</h1>
        <p class="subtitle-sweet">
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
        <div style="font-family: 'Playfair Display', serif; font-size: 1.45rem; font-weight: 600; color: #880E4F; margin-bottom: 14px;">
            Dear Ruhii,
        </div>
        <p style="font-size: 1.15rem; line-height: 1.8; color: #4A2840; margin-bottom: 16px;">
            Happy Birthday to one of the most special people in my life! 💕 Tumhari friendship meri life ka ek beautiful part hai.
            I hope tumhari life hamesha happiness, success, laughter aur beautiful memories se filled rahe.
        </p>
        <p style="font-size: 1.15rem; line-height: 1.8; color: #4A2840; margin-bottom: 16px;">
            Hamesha aise hi smile karti rehna because your smile deserves the whole universe. ✨ Tumhari maujoodgi har din ko bright aur positive bana deti hai.
        </p>
        <div style="text-align: right; font-family: 'Dancing Script', cursive; font-size: 1.6rem; color: #C2185B; font-weight: 700;">
            With endless love & blessings, Always 💗
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Funny Breaking News Card
    st.markdown("""
    <div class="funny-box" style="border-color: #F06292; background: rgba(255, 240, 246, 0.95);">
        <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 6px;">
            <span style="font-size: 1.5rem;">🚨</span>
            <span style="font-weight: 700; color: #D81B60; text-transform: uppercase; letter-spacing: 1px;">Breaking News Bulletin!</span>
        </div>
        <div style="font-size: 1.1rem; color: #4A2338; line-height: 1.5;">
            "Aaj duniya ki sabse cute aur thori si pagal larki ka birthday hai! 😂 Sources say birthday girl ko aaj treat dene se koi nahi bacha sakta!"
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Action / Navigation Buttons
    col_p1, col_p2 = st.columns([1, 1])
    with col_p1:
        if st.button("🏠 Home", key="btn_home_p1"):
            st.session_state.entered_world = False
            st.session_state.countdown_done = True
            st.rerun()
    with col_p2:
        if st.button("Next Surprise, Madam Ji! ➜", key="btn_next_p1"):
            st.session_state.current_page = 2
            st.rerun()


# ------------------------------------------------------------------------------
# PAGE 2: DUAS AND BLESSINGS 🤲
# ------------------------------------------------------------------------------
elif st.session_state.current_page == 2:
    st.markdown("""
    <div style="text-align: center;">
        <h1 class="title-script" style="color: #8E24AA;">Prayers From My Heart 🤲</h1>
        <p class="subtitle-sweet" style="color: #6A1B9A;">
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

    duas = [
        "Allah tumhari har jaiz dua qabool farmaye.",
        "Allah tumhari zindagi ko sehat, sukoon, khushiyon aur barkaton se bhar de.",
        "Tumhare har mushkil raste ko asaan farmaye.",
        "Tumhein duniya aur akhirat dono mein kamyabi ata farmaye.",
        "Tumhari aankhon mein hamesha khushi ke aansu hon, gham ke nahi.",
        "Allah tumhein buri nazar, pareshani aur har takleef se mehfooz rakhe."
    ]

    for idx, dua in enumerate(duas, 1):
        st.markdown(f"""
        <div class="dua-card">
            <div class="dua-num">{idx}</div>
            <div class="dua-text">{dua}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div style="text-align: center; margin-top: 25px; padding: 14px; background: linear-gradient(135deg, rgba(234, 187, 240, 0.35), rgba(255, 214, 230, 0.45)); border-radius: 20px;">
            <div style="font-family: 'Dancing Script', cursive; font-size: 2.2rem; font-weight: 700; color: #7B1FA2;">
                Ameen Sum Ameen! 🤲 🤍
            </div>
            <div style="font-size: 0.95rem; color: #6A1B9A; font-weight: 600; margin-top: 4px;">
                May every single angel whisper Ameen to these prayers for you!
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Navigation Buttons
    c_prev2, c_next2 = st.columns([1, 1])
    with c_prev2:
        if st.button("⬅️ Previous", key="btn_prev_p2"):
            st.session_state.current_page = 1
            st.rerun()
    with c_next2:
        if st.button("Chalo Ab Thori Masti Ho Jaye 😂", key="btn_next_p2"):
            st.session_state.current_page = 3
            st.rerun()


# ------------------------------------------------------------------------------
# PAGE 3: FUNNY AND CUTE SECTION 😂
# ------------------------------------------------------------------------------
elif st.session_state.current_page == 3:
    st.markdown("""
    <div style="text-align: center;">
        <h1 class="title-script" style="color: #E64A19;">Ruhii Ki Pagalpanti Department 😂</h1>
        <p class="subtitle-sweet" style="color: #D84315;">
            "Warning: Is page ko dekh kar hansna mana nahi hai! 🤣"
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="glass-card" style="border: 2px dashed #FFAB91;">
        <div style="text-align: center; font-size: 2.4rem; margin-bottom: 12px;">
            🤪 🍰 🍟 🎭 👑
        </div>
        <h3 style="text-align: center; color: #D84315; font-weight: 700; margin-bottom: 16px;">
            Official Birthday Truths 📢
        </h3>
    """, unsafe_allow_html=True)

    roasts = [
        "Congratulations! Tum officially ek saal aur experienced ho gayi ho... lekin harkatein abhi bhi bachon wali hain! 😂",
        "Cake tumhara hai, lekin khaane ka poora haq mera bhi banta hai (50% partner share)! 🎂🍴",
        "Tumhari age increase ho rahi hai, lekin maturity abhi bhi loading pe hai... 2% completed! 🤣",
        "Aaj tumhari har wish poori ho, bas mujhe tang karne wali wishes STRICTLY excluded hain! 🙅‍♂️"
    ]

    for item in roasts:
        st.markdown(f"""
        <div class="funny-box">
            👉 {item}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Interactive Compliment Generator
    st.markdown("""
    <div class="glass-card" style="text-align: center; background: rgba(255, 255, 255, 0.88); border: 2px solid #FF80AB;">
        <div style="font-size: 2rem; margin-bottom: 8px;">🎁 💝 👑</div>
        <h3 style="color: #C2185B; font-weight: 700; margin-bottom: 10px;">Special Mystery Compliment Generator</h3>
        <p style="font-size: 1rem; color: #733454; margin-bottom: 18px;">
            Press the magic button below to unlock a sweet & funny truth about you!
        </p>
    """, unsafe_allow_html=True)

    if st.button("Reveal My Birthday Compliment 💝", key="btn_compliment"):
        st.session_state.compliment = random.choice(COMPLIMENTS)

    if st.session_state.compliment:
        st.markdown(f"""
        <div style="margin-top: 18px; padding: 18px 24px; background: linear-gradient(135deg, #FFF0F5, #FCE4EC);
                    border: 2px solid #F06292; border-radius: 20px; box-shadow: 0 8px 25px rgba(240, 98, 146, 0.25);">
            <div style="font-size: 1.8rem; margin-bottom: 6px;">✨ 💖 ✨</div>
            <div style="font-size: 1.25rem; font-weight: 700; color: #880E4F; line-height: 1.5;">
                "{st.session_state.compliment}"
            </div>
            <div style="font-size: 0.9rem; color: #AD1457; margin-top: 8px; font-weight: 600;">
                (100% Certified Sach! 😌)
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Navigation Buttons
    c_prev3, c_next3 = st.columns([1, 1])
    with c_prev3:
        if st.button("⬅️ Previous", key="btn_prev_p3"):
            st.session_state.current_page = 2
            st.rerun()
    with c_next3:
        if st.button("Ab Last Surprise Dekho ❤️", key="btn_next_p3"):
            st.session_state.current_page = 4
            st.session_state.show_hug = False
            st.rerun()


# ------------------------------------------------------------------------------
# PAGE 4: SPECIAL MESSAGE ❤️
# ------------------------------------------------------------------------------
elif st.session_state.current_page == 4:
    st.markdown("""
    <div style="text-align: center;">
        <h1 class="title-script" style="color: #D81B60;">One Last Thing, Ruhii... ❤️</h1>
        <p class="subtitle-sweet" style="color: #AD1457;">
            "Kuch baatein hoti hain jo words mein explain karna mushkil hota hai."
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Emotional Heartfelt Card
    st.markdown("""
    <div class="glass-card" style="border: 2px solid rgba(244, 143, 177, 0.8);">
        <!-- Animated Beating Heart Centerpiece -->
        <div style="text-align: center; margin: 10px 0 20px;">
            <div class="pulsing-heart" style="font-size: 5rem; filter: drop-shadow(0 6px 20px rgba(233, 30, 99, 0.4));">
                💖
            </div>
        </div>

        <div style="font-size: 1.18rem; line-height: 1.85; color: #4A2840; margin-bottom: 18px;">
            Ruhii, I just want you to know that you are genuinely special. Life mein bohat se log milte hain, lekin kuch log apni presence se har moment ko beautiful bana dete hain. Tum unhi logon mein se ho.
        </div>

        <div style="font-size: 1.18rem; line-height: 1.85; color: #4A2840; margin-bottom: 22px;">
            May your smile never fade, may your dreams come true, and may happiness always find its way to you.
            <br><br>
            <strong>Thank you for being you. Stay blessed, stay crazy, and never stop smiling.</strong>
        </div>

        <div style="text-align: center; padding: 18px; background: linear-gradient(135deg, rgba(255, 192, 203, 0.4), rgba(225, 190, 231, 0.4)); border-radius: 20px; margin-top: 15px;">
            <div style="font-family: 'Dancing Script', cursive; font-size: 2.2rem; font-weight: 700; color: #C2185B; letter-spacing: 0.5px;">
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

    if st.session_state.show_hug:
        st.balloons()
        st.markdown("""
        <div class="glass-card" style="text-align: center; background: linear-gradient(135deg, #FFE4E1, #FFF0F5); border: 2.5px solid #FF4081; margin-top: 20px;">
            <div style="font-size: 4rem;" class="pulsing-heart">🤗 💗 🫂</div>
            <div style="font-family: 'Dancing Script', cursive; font-size: 2.8rem; font-weight: 700; color: #E91E63; margin: 10px 0;">
                SENDING YOU INFINITE HUGS & LOVE! 💗
            </div>
            <p style="font-size: 1.15rem; color: #7B2456; font-weight: 600;">
                May your whole year ahead be as soft, warm, and comforting as the biggest hug!
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Navigation Buttons
    col_p4_1, col_p4_2 = st.columns([1, 1])
    with col_p4_1:
        if st.button("⬅️ Previous", key="btn_prev_p4"):
            st.session_state.current_page = 3
            st.session_state.show_hug = False
            st.rerun()
    with col_p4_2:
        if st.button("Open My Little Letter 💌", key="btn_restart_to_1"):
            st.session_state.current_page = 1
            st.session_state.show_hug = False
            st.rerun()

    # Footer
    st.markdown("""
    <div style="text-align: center; margin-top: 40px; padding: 20px 0; border-top: 1px dashed rgba(200, 140, 180, 0.4);">
        <p style="font-family: 'Dancing Script', cursive; font-size: 1.5rem; color: #8E4A72; font-weight: 700;">
            Made with ❤️ especially for Ruhii.
        </p>
        <p style="font-size: 0.85rem; color: #A87093;">
            A Little World Made for Ruhii 💗 • Happy Birthday!
        </p>
    </div>
    """, unsafe_allow_html=True)
