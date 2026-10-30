
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Happy Birthday Ruhii ❤️",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- SESSION STATE ----------------
if "page" not in st.session_state:
    st.session_state.page = 0

# ---------------- STYLING ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:wght@500;700;800&family=Poppins:wght@300;400;500;600;700&display=swap');

* {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg,#160d2b,#422052,#8b477e,#e6a4c6);
    background-attachment: fixed;
    color: white;
}

header, footer, #MainMenu {
    visibility: hidden;
}

.block-container {
    padding-top: 1.5rem;
    max-width: 900px;
}

.hero {
    text-align: center;
    padding: 35px 15px;
    animation: appear 1.5s ease;
}

.main-title {
    font-family: 'Great Vibes', cursive;
    font-size: clamp(55px, 10vw, 105px);
    color: #fff0f7;
    text-shadow: 0 0 15px #ff9ed0, 0 0 35px #ff5cab;
    animation: glow 2s infinite alternate;
}

.heading {
    font-family: 'Playfair Display', serif;
    font-size: clamp(32px, 6vw, 55px);
    font-weight: 800;
    text-align: center;
    color: #ffe2f2;
    text-shadow: 0 0 15px #ff8fcb;
}

.subheading {
    text-align: center;
    font-size: 17px;
    color: #ffd9ed;
    letter-spacing: 1px;
}

.card {
    background: rgba(255,255,255,0.12);
    border: 1px solid rgba(255,255,255,0.3);
    border-radius: 25px;
    padding: 30px;
    margin: 20px auto;
    text-align: center;
    box-shadow: 0 10px 40px rgba(0,0,0,0.2);
    backdrop-filter: blur(12px);
    animation: appear 1.2s ease;
}

.message {
    font-size: 17px;
    line-height: 2;
    color: #fff4fa;
}

@keyframes glow {
    from { text-shadow: 0 0 10px #ff9ed0; }
    to { text-shadow: 0 0 30px #ff42a1, 0 0 55px #ffb6da; }
}

@keyframes appear {
    from { opacity: 0; transform: translateY(35px); }
    to { opacity: 1; transform: translateY(0); }
}

.stButton button {
    width: 100%;
    border-radius: 35px;
    border: 2px solid #ffd1e9;
    background: linear-gradient(90deg,#ff65a8,#c44de0);
    color: white;
    font-size: 16px;
    font-weight: 700;
    padding: 14px;
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.04);
    box-shadow: 0 0 25px #ff9aca;
    color: white;
    border-color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LIVE ANIMATIONS ----------------
components.html("""
<div id="birthday-effects"></div>

<style>
#birthday-effects {
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 999999;
    overflow: hidden;
}

.particle {
    position: absolute;
    top: -40px;
    animation: fall linear infinite;
    opacity: 0.8;
}

@keyframes fall {
    0% { transform: translateY(-40px) rotate(0deg); opacity: 1; }
    100% { transform: translateY(110vh) rotate(720deg); opacity: 0; }
}

.heart {
    position: absolute;
    bottom: -40px;
    animation: floatup linear infinite;
    opacity: 0.8;
}

@keyframes floatup {
    0% { transform: translateY(0) scale(.7); opacity: 0; }
    20% { opacity: 1; }
    100% { transform: translateY(-110vh) scale(1.4); opacity: 0; }
}
</style>

<script>
const root = document.getElementById("birthday-effects");

const symbols = ["❤️","💕","✨","❄️","🌸","💗","🎀","⭐","🌷"];

function makeParticle() {
    let p = document.createElement("div");
    p.className = "particle";
    p.innerHTML = symbols[Math.floor(Math.random()*symbols.length)];
    p.style.left = Math.random()*100 + "vw";
    p.style.fontSize = (12+Math.random()*22)+"px";
    p.style.animationDuration = (5+Math.random()*8)+"s";
    root.appendChild(p);
    setTimeout(()=>p.remove(),13000);
}

function makeHeart() {
    let h = document.createElement("div");
    h.className = "heart";
    h.innerHTML = ["💗","❤️","💕","💖"][Math.floor(Math.random()*4)];
    h.style.left = Math.random()*100+"vw";
    h.style.fontSize = (15+Math.random()*25)+"px";
    h.style.animationDuration = (7+Math.random()*7)+"s";
    root.appendChild(h);
    setTimeout(()=>h.remove(),15000);
}

setInterval(makeParticle,300);
setInterval(makeHeart,650);
</script>
""", height=0, scrolling=False)

# ---------------- COUNTDOWN ----------------
if st.session_state.page == 0:

    components.html("""
    <div class="countdown">
        <div class="count-label">A LITTLE MAGIC IS WAITING...</div>
        <div id="number">3</div>
        <div class="count-sub">Ruhii, your surprise is almost here! 💗</div>
    </div>

    <style>
    .countdown {
        text-align:center;
        padding:60px 10px;
        color:white;
    }
    .count-label {
        font-family:'Playfair Display',serif;
        letter-spacing:4px;
        color:#ffd6eb;
        font-size:18px;
    }
    #number {
        font-family:'Great Vibes',cursive;
        font-size:140px;
        color:#ffb6dc;
        text-shadow:0 0 35px #ff42a1;
        animation:pulse 1s infinite;
    }
    .count-sub {font-size:16px;color:#ffe5f4;}
    @keyframes pulse {
        50% {transform:scale(1.2);opacity:.7;}
    }
    </style>

    <script>
    let n=3;
    const number=document.getElementById("number");
    const timer=setInterval(()=>{
        n--;
        if(n>0) number.innerText=n;
        else {
            clearInterval(timer);
            number.innerText="🎉";
            document.getElementById("number").style.fontSize="110px";
        }
    },1000);
    </script>
    """, height=300)

    st.markdown("""
    <div class="hero">
        <div class="main-title">Ready Ruhii?</div>
        <p class="subheading">Aaj tumhara special din hai, madam! 😂💕</p>
        <div class="card">
            <div style="font-size:55px;">🎁 💗 🎂</div>
            <p class="message">
            Tumhare liye kuch special prepare kiya hai.<br>
            Lekin itni jaldi nahi... pehle surprise unlock karo! 😌
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("💗 OPEN MY SURPRISE 💗"):
        st.session_state.page = 1
        st.rerun()

# ---------------- PAGE 1 ----------------
elif st.session_state.page == 1:

    st.markdown("""
    <div class="hero">
        <div style="font-size:65px;">🎂🎀✨</div>
        <div class="main-title">Happy Birthday Ruhii</div>
        <p class="subheading">Aaj ki queen sirf tum ho! 👑</p>
    </div>

    <div class="card">
        <div style="font-size:55px;">🥳💖🌷</div>
        <h2 class="heading">Your Special Day</h2>
        <p class="message">
        Finally, tumhara birthday aa hi gaya! 😂<br>
        May your smile always shine brighter than the stars.<br>
        Tumhari life khushiyon, laughter aur beautiful memories se bhari rahe.<br><br>
        Aur haan, cake mein mera hissa mat bhoolna! 🎂🤣
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("NEXT → Madam, Agla Surprise Dekho 😂"):
        st.session_state.page = 2
        st.rerun()

# ---------------- PAGE 2 ----------------
elif st.session_state.page == 2:

    st.markdown("""
    <div class="hero">
        <div style="font-size:60px;">🤲🌙✨</div>
        <h1 class="heading">My Heartfelt Prayers</h1>
        <p class="subheading">Ab thori serious baat, dil se... 💗</p>
    </div>

    <div class="card">
        <p class="message">
        🤍 Allah tumhari zindagi ko khushiyon se bhar de.<br><br>
        🤍 Tumhari har jaiz dua qubool ho.<br><br>
        🤍 Allah tumhein sehat, sukoon aur kamyabi ata farmaye.<br><br>
        🤍 Tumhare har mushkil raste ko asaan kare.<br><br>
        🤍 Tumhari aankhon mein kabhi aansu aayein bhi to sirf khushi ke.<br><br>
        🤍 Allah tumhein duniya aur akhirat dono mein kamyabi de.<br><br>
        Ameen Sum Ameen! 🤲❤️
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("NEXT → Ab Compliments Ki Baarish Hogi 😂"):
        st.session_state.page = 3
        st.rerun()

# ---------------- PAGE 3 ----------------
elif st.session_state.page == 3:

    st.markdown("""
    <div class="hero">
        <div style="font-size:60px;">😂💅👑</div>
        <h1 class="heading">Officially Amazing!</h1>
        <p class="subheading">Ruhii ki tareef karna farz hai! 🤣</p>
    </div>

    <div class="card">
        <p class="message">
        🏆 Congratulations! Tumne ek aur saal survive kar liya! 😂<br><br>
        👑 Beauty level: Unlimited<br><br>
        🤣 Drama level: Out of syllabus<br><br>
        💖 Attitude level: Premium subscription<br><br>
        🌸 Smile level: Absolutely priceless<br><br>
        Aur sab se bari achievement...<br>
        Meri jaisi personality ko tolerate karna! 🤣❤️
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("NEXT → Last Wala Dil Se Hai ❤️"):
        st.session_state.page = 4
        st.rerun()

# ---------------- PAGE 4 ----------------
elif st.session_state.page == 4:

    st.markdown("""
    <div class="hero">
        <div style="font-size:65px;">💌🌹❤️</div>
        <h1 class="heading">A Little Message For You</h1>
        <p class="subheading">Ab thora emotional hone ki permission hai... 🥹</p>
    </div>

    <div class="card">
        <div class="main-title" style="font-size:55px;">
            Dear Ruhii
        </div>

        <p class="message">
        Life mein kuch log aise hote hain jo apni presence se
        har moment ko special bana dete hain.<br><br>

        Tum bhi unhi special logon mein se ho.<br><br>

        I hope tumhari life ka har naya chapter pehle se zyada
        beautiful ho. Tum hamesha grow karo, smile karo aur
        apne dreams achieve karo.<br><br>

        Chahe kitni bhi nok jhok ho, meri dua hai ke tum hamesha
        khush raho aur tumhein woh sab mile jo tumhare dil ke liye
        behtareen ho.<br><br>

        **Once again, Happy Birthday Ruhii!** 🎂💗<br><br>

        Stay blessed, stay happy and never stop smiling! 🌸
        </p>

        <div style="font-size:55px;">❤️ 🥹 🌷</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔁 EK BAAR PHIR SE SURPRISE DEKHO"):
        st.session_state.page = 0
        st.rerun()

    if st.button("💗 THE END - LOVE & BEST WISHES"):
        st.balloons()
        st.snow()

# ---------------- FOOTER ----------------
st.markdown("""
<div style="text-align:center;padding:25px;color:#ffe0f0;">
    Made with lots of love, smiles and a little madness! 💗<br>
    A special birthday surprise for Ruhii 🎀
</div>
""", unsafe_allow_html=True)
