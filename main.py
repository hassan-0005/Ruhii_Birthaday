
import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# RUHI'S SPECIAL BIRTHDAY WEBSITE
# Created with love and duas
# ==========================================

st.set_page_config(
    page_title="Happy Birthday Ruhi 🎀",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# PERSONAL SETTINGS
# ==========================================

FRIEND_NAME = "Ruhi"
YOUR_NAME = "Your Special Friend"

# Change YOUR_NAME to your own name.
# You can also personalize the messages below.

# ==========================================
# SESSION STATE
# ==========================================

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "surprise_open" not in st.session_state:
    st.session_state.surprise_open = False

if "letter_open" not in st.session_state:
    st.session_state.letter_open = False

if "celebrated" not in st.session_state:
    st.session_state.celebrated = False

# ==========================================
# CSS DESIGN AND ANIMATIONS
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

.stApp {
    background:
        radial-gradient(circle at 10% 10%, #ffe0ed 0%, transparent 35%),
        radial-gradient(circle at 90% 20%, #eadfff 0%, transparent 35%),
        linear-gradient(135deg, #fff7fa, #fff0f5, #f8f0ff);
    font-family: 'DM Sans', sans-serif;
}

header, footer, #MainMenu {
    visibility: hidden;
}

.block-container {
    max-width: 1050px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: #b64279 !important;
}

p {
    color: #77556a;
    line-height: 1.9;
}

.hero {
    background: rgba(255,255,255,0.78);
    border: 1px solid white;
    border-radius: 30px;
    padding: 48px 22px;
    text-align: center;
    box-shadow: 0 12px 40px rgba(190, 85, 140, 0.12);
    animation: fadeUp 1s ease;
}

.hero h1 {
    font-size: clamp(36px, 7vw, 68px);
    margin: 10px 0;
    background: linear-gradient(90deg, #d34f91, #9b6cce);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    font-size: 17px;
}

.eyebrow {
    color: #c35b91;
    letter-spacing: 3px;
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
}

.card {
    background: rgba(255,255,255,0.83);
    border: 1px solid #f8d6e7;
    border-radius: 24px;
    padding: 25px;
    margin: 17px 0;
    box-shadow: 0 8px 25px rgba(190, 85, 140, 0.08);
    transition: 0.3s;
    animation: fadeUp 0.8s ease;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 30px rgba(190, 85, 140, 0.15);
}

.center {
    text-align: center;
}

.subtitle {
    font-size: 16px;
    line-height: 2;
}

.big-heart {
    font-size: 45px;
    display: inline-block;
    animation: heartbeat 1.8s infinite;
}

.small-title {
    color: #b64279;
    font-family: 'Playfair Display', serif;
    font-size: 25px;
    font-weight: 600;
}

.quote {
    font-style: italic;
    font-size: 18px;
    color: #9c5480;
    text-align: center;
}

.gift {
    font-size: 100px;
    text-align: center;
    animation: giftBounce 2s infinite;
}

.footer {
    text-align: center;
    color: #ad6b8e;
    padding: 30px 10px;
    font-size: 13px;
}

.stButton > button {
    border-radius: 30px;
    background: linear-gradient(90deg, #e77eac, #b98cdb);
    color: white;
    border: none;
    padding: 12px 18px;
    font-weight: 600;
    transition: 0.3s;
    width: 100%;
}

.stButton > button:hover {
    transform: scale(1.025);
    color: white;
    border: 1px solid white;
    box-shadow: 0 6px 20px #e9bad3;
}

div[role="radiogroup"] {
    justify-content: center;
    gap: 8px;
}

div[role="radiogroup"] label {
    background: rgba(255,255,255,0.85);
    padding: 10px 16px;
    border-radius: 22px;
    border: 1px solid #f4c8dc;
}

div[role="radiogroup"] label p {
    color: #a34476;
    font-weight: 600;
}

div[data-testid="stTextArea"] textarea {
    border-radius: 15px;
}

@keyframes heartbeat {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.2); }
}

@keyframes giftBounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-13px); }
}

@keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes floatHeart {
    0% { transform: translateY(105vh) rotate(0deg); opacity: 0; }
    15% { opacity: 0.8; }
    100% { transform: translateY(-15vh) rotate(360deg); opacity: 0; }
}

.float-heart {
    position: fixed;
    bottom: -40px;
    z-index: 0;
    pointer-events: none;
    animation: floatHeart linear infinite;
    opacity: 0.7;
    font-size: 22px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# FLOATING HEARTS AND SPRINKLES
# ==========================================

components.html("""
<div id="birthday-effects"></div>
<style>
.float {
    position: fixed;
    bottom: -40px;
    animation: rise linear infinite;
    pointer-events: none;
    z-index: 9999;
    opacity: 0.8;
}
@keyframes rise {
    0% { transform: translateY(0) rotate(0deg); opacity: 0; }
    15% { opacity: 0.8; }
    100% { transform: translateY(-110vh) rotate(360deg); opacity: 0; }
}
</style>
<script>
const container = document.getElementById("birthday-effects");
const icons = ["💗","💕","✨","🌸","🎀","🦋","💖","🌷"];
for (let i = 0; i < 22; i++) {
    let item = document.createElement("span");
    item.className = "float";
    item.innerText = icons[Math.floor(Math.random()*icons.length)];
    item.style.left = Math.random()*100 + "vw";
    item.style.animationDuration = (7 + Math.random()*10) + "s";
    item.style.animationDelay = (-Math.random()*12) + "s";
    item.style.fontSize = (15 + Math.random()*16) + "px";
    container.appendChild(item);
}
</script>
""", height=0)

# ==========================================
# HEADER
# ==========================================

st.markdown("""
<div class="center">
    <div class="eyebrow">A LITTLE WORLD MADE FOR SOMEONE SPECIAL</div>
    <div style="font-size:25px; margin-top:5px;">
        🎀 💗 🌸 💗 🎀
    </div>
</div>
""", unsafe_allow_html=True)

# ==========================================
# NAVIGATION
# ==========================================

pages = [
    "🏠 Home",
    "💌 Wishes",
    "🤲 Duas",
    "🦋 Memories",
    "🎁 Surprise"
]

current_page = st.session_state.page

page_labels = {
    "🏠 Home": "Home",
    "💌 Wishes": "Wishes",
    "🤲 Duas": "Duas",
    "🦋 Memories": "Memories",
    "🎁 Surprise": "Surprise"
}

default_label = next(
    (label for label, value in page_labels.items()
     if value == current_page),
    "🏠 Home"
)

selected = st.radio(
    "Navigate",
    pages,
    index=pages.index(default_label),
    horizontal=True,
    label_visibility="collapsed",
    key="navigation"
)

new_page = page_labels[selected]

if new_page != st.session_state.page:
    st.session_state.page = new_page
    st.rerun()

st.markdown("---")

# ==========================================
# PAGE 1: HOME
# ==========================================

if st.session_state.page == "Home":

    st.markdown(f"""
    <div class="hero">
        <div class="eyebrow">TODAY IS ALL ABOUT YOU</div>
        <div class="big-heart">💗</div>
        <h1>Happy Birthday {FRIEND_NAME}!</h1>
        <h2>🎂 Your Special Day Is Here 🎂</h2>
        <p>
        Aaj ka din bohat special hai,
        kyun ke aaj ek bohat pyari person ka birthday hai!
        </p>
        <div style="font-size:38px;">🌸 🦋 🎀 💕 ✨</div>
        <p>
        Welcome to your little birthday world.
        This small surprise is made just to bring a smile
        to your face.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown(f"""
    <div class="card center">
        <div class="small-title">Dear {FRIEND_NAME} 💌</div>
        <p class="subtitle">
        Pata hai? Kuch log apni presence se ordinary
        moments ko bhi beautiful bana dete hain.
        <br><br>
        And today, I just want to celebrate you!
        <br><br>
        May your smile never fade, your dreams never stop
        and your heart always find reasons to be happy.
        <br><br>
        Aaj bas enjoy karo, khush raho aur bohat saari
        smiles do!
        </p>
        <div class="quote">
        "You deserve all the happiness in this world." 💗
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        if st.button("Let's Start Your Surprise Journey 💕"):
            st.session_state.page = "Wishes"
            st.rerun()

    st.markdown("""
    <div class="card center">
        <h2>Today's Special Reminder 🌷</h2>
        <p class="subtitle">
        You are precious. Your dreams are important.
        Your happiness matters.
        <br>
        Never forget your worth.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# PAGE 2: WISHES
# ==========================================

elif st.session_state.page == "Wishes":

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">A FEW WORDS FROM THE HEART</div>
        <h1>Birthday Wishes 💌</h1>
        <p>Har wish mein tumhare liye ek pyara sa message hai.</p>
    </div>
    """, unsafe_allow_html=True)

    wishes = [
        (
            "🌸 Happiness",
            "May your life always be full of happiness. "
            "Tumhari smile hamesha aisi hi beautiful rahe "
            "aur tumhein kabhi khush rehne ke liye kisi reason "
            "ki zaroorat na ho."
        ),
        (
            "🦋 Dreams & Success",
            "May every dream you have slowly become reality. "
            "Allah tumhein har us manzil tak pohanchaye "
            "jahan tum jana chahti ho. Keep believing in yourself!"
        ),
        (
            "💗 Beautiful Moments",
            "May this year give you unforgettable memories, "
            "beautiful surprises and people who genuinely care "
            "about you."
        ),
        (
            "🎀 Endless Smiles",
            "I hope tumhari life mein sadness se zyada smiles, "
            "worries se zyada peace aur disappointments se "
            "zyada beautiful surprises hon."
        ),
        (
            "✨ A New Chapter",
            "A new year of your life means new opportunities, "
            "new experiences and new reasons to shine. "
            "Make this chapter your most beautiful one!"
        )
    ]

    for title, message in wishes:
        st.markdown(f"""
        <div class="card">
            <div class="small-title">{title}</div>
            <p class="subtitle">{message}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="hero">
        <h2>Once Again, Happy Birthday! 🎂</h2>
        <p>
        Stay happy, stay blessed and keep shining.
        The best is yet to come! 💗
        </p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# PAGE 3: DUAS
# ==========================================

elif st.session_state.page == "Duas":

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">PRAYERS FROM THE HEART</div>
        <h1>Special Duas For You 🤲</h1>
        <p>
        Kuch wishes words mein hoti hain,
        aur kuch dil se nikli hui duaein.
        </p>
    </div>
    """, unsafe_allow_html=True)

    duas = [
        (
            "🤲 Happiness & Peace",
            "May Allah tumhare dil ko hamesha sukoon de, "
            "tumhari zindagi se pareshaniyan door kare "
            "aur tumhein har haal mein khush rakhe."
        ),
        (
            "🌷 Success & Dreams",
            "May Allah tumhari mehnat mein barkat de, "
            "tumhare liye kamyabi ke raaste kholay "
            "aur tumhare achay khwabon ko haqeeqat banaye."
        ),
        (
            "💗 Health & Protection",
            "May Allah tumhein sehat, afiyat aur apni hifazat "
            "mein rakhe. Har buri nazar, mushkil aur pareshani "
            "se mehfooz farmaye."
        ),
        (
            "✨ Blessings",
            "May Allah tumhari zindagi mein itni barkat de "
            "ke tum har din apni blessings ko appreciate kar sako."
        ),
        (
            "🕊️ A Beautiful Future",
            "May Allah tumhara mustaqbil roshan kare, "
            "tumhein achay logon ka saath de "
            "aur har faislay mein behtari ata farmaye."
        )
    ]

    for title, message in duas:
        st.markdown(f"""
        <div class="card">
            <div class="small-title">{title}</div>
            <p class="subtitle">{message}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card center">
        <h1 style="font-size:36px;">آمین یا رب العالمین 🤍</h1>
        <p class="subtitle">
        May Allah accept every sincere dua made for you.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# PAGE 4: MEMORIES
# ==========================================

elif st.session_state.page == "Memories":

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">A LITTLE APPRECIATION</div>
        <h1>Our Special Bond 🦋</h1>
        <p>
        Some people are not just part of life,
        they become part of our favourite memories.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="card">
        <h2>Dear {FRIEND_NAME} 💗</h2>
        <p class="subtitle">
        Life mein bohat se log milte hain,
        lekin har koi special nahi hota.
        <br><br>
        Some people leave beautiful memories,
        some teach us important lessons,
        and some make us smile without even trying.
        <br><br>
        I hope tumhari life mein hamesha aise moments
        aate rahein jo tumhein genuinely happy karein.
        <br><br>
        Chahe life kitni bhi busy ho jaye,
        apni happiness, apni self-respect
        aur apne dreams ko kabhi ignore mat karna.
        <br><br>
        You deserve genuine happiness and beautiful things.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card center">
        <h2>Little Friendship Quotes 🌸</h2>
        <p class="quote">
        "Some people make life a little more beautiful."
        </p>
        <p class="quote">
        "Real connections are remembered, not measured."
        </p>
        <p class="quote">
        "A beautiful friendship is a blessing."
        </p>
        <p class="quote">
        "Distance and time cannot erase genuine memories."
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card center">
        <h2>My Wish For You ✨</h2>
        <p class="subtitle">
        I hope you become the person you dream of being.
        <br><br>
        I hope you achieve things that make you proud.
        <br><br>
        And most importantly, I hope you never stop
        loving the person you are becoming.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card center">
        <div style="font-size:35px;">💌 🌷 💗</div>
        <h2>A Little Reminder</h2>
        <p class="subtitle">
        You matter. You are valuable.
        Never let anyone make you feel otherwise.
        </p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# PAGE 5: SURPRISE
# ==========================================

elif st.session_state.page == "Surprise":

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">THE LAST PAGE HAS SOMETHING SPECIAL</div>
        <h1>Your Birthday Surprise 🎁</h1>
        <p>
        A little gift, a little love
        and a message just for you.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="gift">🎁</div>',
                unsafe_allow_html=True)

    st.markdown("""
    <div class="center">
        <h2>Ready to open your gift?</h2>
        <p>Tap below and see what is waiting for you. 💗</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        if st.button("🎀 OPEN YOUR SPECIAL GIFT 🎀"):
            st.session_state.surprise_open = True
            st.balloons()
            st.snow()

    if st.session_state.surprise_open:

        st.markdown(f"""
        <div class="card center">
            <div style="font-size:60px;">🎂💗🌸</div>
            <h1>Happy Birthday {FRIEND_NAME}!</h1>
            <h2>You Are Truly Special!</h2>
            <p class="subtitle">
            I hope this new chapter of your life brings
            you more happiness than you can imagine.
            <br><br>
            May every morning bring you hope,
            every challenge make you stronger
            and every night give you peace.
            <br><br>
            Tumhari har achi wish poori ho,
            tumhare har din mein khushi ho
            aur tumhara future bohat bright ho.
            <br><br>
            Never stop smiling, never stop dreaming
            and never forget your worth.
            <br><br>
            Sending you lots of love,
            duas and best wishes! 💕
            </p>
            <h2>Stay Blessed Always! 🤲</h2>
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <div class="card center">
        <h2>💌 One Last Thing...</h2>
        <p class="subtitle">
        This website may have five pages,
        but my good wishes for you are endless.
        <br><br>
        I hope jab bhi tum is website ko dekho,
        tumhare face par ek pyari si smile aa jaye.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("💗 Read Your Personal Birthday Letter"):

        st.session_state.letter_open = not st.session_state.letter_open

    if st.session_state.letter_open:

        st.markdown(f"""
        <div class="card center">
            <h1>Dear {FRIEND_NAME},</h1>
            <p class="subtitle">
            Aaj tumhara special day hai, and I just want
            to say that I genuinely wish the best for you.
            <br><br>
            Life hamesha perfect nahi hoti,
            but I hope tumhein har difficult moment ke baad
            ek beautiful reason mile to smile again.
            <br><br>
            Apne dreams ke liye mehnat karna,
            apni value kabhi kam mat samajhna
            aur hamesha apne liye bhi time nikalna.
            <br><br>
            May Allah always guide you,
            protect you and bless you with everything
            that is truly good for you.
            <br><br>
            Once again, Happy Birthday!
            <br><br>
            With best wishes and duas,
            <br>
            <b>{YOUR_NAME}</b> 🎀
            </p>
        </div>
        """, unsafe_allow_html=True)

# ==========================================
# FOOTER
# ==========================================

st.markdown("""
<div class="footer">
    🎀 Made with love, duas and lots of pink sprinkles 🎀
    <br><br>
    A special birthday world for Ruhi 💗
    <br>
    Stay Happy. Stay Blessed. Keep Shining. ✨
</div>
""", unsafe_allow_html=True)
