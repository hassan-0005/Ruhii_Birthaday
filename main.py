
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Happy Birthday Ruhii ❤️",
    page_icon="🎀",
    layout="centered"
)

if "page" not in st.session_state:
    st.session_state.page = 0

# ---------------- CSS ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:wght@600;700;800&family=Cormorant+Garamond:wght@600;700&family=Poppins:wght@400;500;600;700&display=swap');

.stApp {
    background: linear-gradient(135deg,#160d2b,#51234f,#9b537e,#e9a9ca);
    background-attachment: fixed;
    color: white;
}

header, footer, #MainMenu {
    visibility: hidden;
}

.block-container {
    max-width: 900px;
    padding-top: 2rem;
}

.hero {
    text-align: center;
    padding: 25px 10px;
    animation: fadeIn 1.5s ease;
}

.main-title {
    font-family: 'Great Vibes', cursive;
    font-size: clamp(60px, 11vw, 110px);
    color: #fff2fa;
    text-shadow: 0 0 15px #ff8bc7, 0 0 35px #ff3d9e;
    animation: glow 2s infinite alternate;
}

.heading {
    font-family: 'Playfair Display', serif;
    font-size: clamp(34px, 7vw, 60px);
    font-weight: 800;
    text-align: center;
    color: #ffe1f1;
    text-shadow: 0 0 20px #ff79bd;
    letter-spacing: 1px;
}

.subheading {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(23px, 4vw, 32px);
    font-weight: 700;
    text-align: center;
    color: #ffd1e8;
    letter-spacing: 2px;
    text-shadow: 0 0 12px #ff9bcd;
    font-style: italic;
    margin-top: 12px;
}

.card {
    background: rgba(255,255,255,0.13);
    border: 1px solid rgba(255,220,240,0.4);
    border-radius: 28px;
    padding: 30px 22px;
    margin: 22px auto;
    text-align: center;
    box-shadow: 0 10px 40px rgba(0,0,0,.2);
    backdrop-filter: blur(15px);
    animation: fadeIn 1.3s ease;
}

.message {
    font-family: 'Poppins', sans-serif;
    font-size: 16px;
    line-height: 2;
    color: #fff4fa;
}

.decor {
    font-size: 42px;
    text-align: center;
    letter-spacing: 10px;
    margin: 15px;
}

.stButton button {
    width: 100%;
    border-radius: 40px;
    border: 2px solid #ffd1e9;
    background: linear-gradient(90deg,#ff65a8,#b64de0);
    color: white;
    font-size: 15px;
    font-weight: 700;
    padding: 15px;
    transition: .3s;
    box-shadow: 0 5px 20px #e85baf55;
}

.stButton button:hover {
    transform: scale(1.04);
    box-shadow: 0 0 25px #ff9aca;
    color: white;
    border-color: white;
}

@keyframes glow {
    from {text-shadow:0 0 10px #ff9ed0;}
    to {text-shadow:0 0 35px #ff42a1,0 0 55px #ffb6da;}
}

@keyframes fadeIn {
    from {opacity:0;transform:translateY(30px);}
    to {opacity:1;transform:translateY(0);}
}
</style>
""", unsafe_allow_html=True)

# ---------------- CONTINUOUS ANIMATIONS ----------------
components.html("""
<div id="effects"></div>
<style>
#effects {
position:fixed;
inset:0;
pointer-events:none;
z-index:999999;
overflow:hidden;
}
.particle {
position:absolute;
top:-40px;
animation:fall linear forwards;
}
.heart {
position:absolute;
bottom:-40px;
animation:floatup linear forwards;
}
@keyframes fall {
to {transform:translateY(110vh) rotate(720deg);opacity:0;}
}
@keyframes floatup {
to {transform:translateY(-110vh) scale(1.5);opacity:0;}
}
</style>
<script>
const root=document.getElementById("effects");
const symbols=["❤️","💕","✨","❄️","🌸","💗","🎀","⭐","🌷","🦋"];

function particle(){
let p=document.createElement("div");
p.className="particle";
p.innerHTML=symbols[Math.floor(Math.random()*symbols.length)];
p.style.left=Math.random()*100+"vw";
p.style.fontSize=(15+Math.random()*25)+"px";
p.style.animationDuration=(5+Math.random()*8)+"s";
root.appendChild(p);
setTimeout(()=>p.remove(),14000);
}

function heart(){
let h=document.createElement("div");
h.className="heart";
h.innerHTML=["💗","❤️","💕","💖"][Math.floor(Math.random()*4)];
h.style.left=Math.random()*100+"vw";
h.style.fontSize=(15+Math.random()*25)+"px";
h.style.animationDuration=(7+Math.random()*7)+"s";
root.appendChild(h);
setTimeout(()=>h.remove(),15000);
}
setInterval(particle,300);
setInterval(heart,650);
</script>
""", height=0)

# ---------------- COUNTDOWN ----------------
if st.session_state.page == 0:

    components.html("""
    <div style="text-align:center;padding:35px;color:white">
    <p style="font-family:serif;letter-spacing:5px;color:#ffd1e8">
    ✨ A MAGICAL SURPRISE AWAITS ✨
    </p>
    <div id="num" style="
    font-family:cursive;
    font-size:140px;
    color:#ffb6dc;
    text-shadow:0 0 30px #ff42a1;">
    3
    </div>
    <p style="font-family:serif;font-size:24px;color:#ffe0f1">
    Ruhii, get ready for something special! 💗
    </p>
    </div>
    <script>
    let n=3;
    let x=setInterval(()=>{
    n--;
    if(n>0) document.getElementById("num").innerText=n;
    else {
    clearInterval(x);
    document.getElementById("num").innerText="🎉";
    }
    },1000);
    </script>
    """, height=280)

    st.markdown("""
    <div class="hero">
    <div class="main-title">The Magic Begins</div>
    <div class="subheading">Aaj kuch bohat special hone wala hai... 🎀</div>
    <div class="card">
    <div class="decor">🎁 💗 🎂</div>
    <p class="message">
    Madam Ruhii! Apni excitement control karo. 😂<br>
    Tumhare liye ek chota sa surprise ready hai!
    </p>
    </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("💖 UNLOCK YOUR SURPRISE 💖"):
        st.session_state.page = 1
        st.rerun()

# ---------------- PAGE 1: BIRTHDAY REVEAL ----------------
elif st.session_state.page == 1:

    st.markdown("""
    <div class="hero">
    <div class="decor">👑 🎂 👑</div>
    <div class="main-title">Happy Birthday</div>
    <div class="main-title">Ruhii</div>
    <div class="subheading">Aaj ka din sirf tumhare naam! 💗</div>
    </div>

    <div class="card">
    <div class="decor">🌷 🦋 ✨</div>
    <h2 class="heading">It's Your Special Day!</h2>
    <p class="message">
    Finallyyyyy! Tumhara birthday aa hi gaya! 🥳<br><br>
    Aaj duniya ki sab se special madam ka din hai.<br>
    May your smile always shine brighter than the stars.<br><br>
    Tumhari zindagi khushiyon, success aur beautiful memories
    se bhar jaye.<br><br>
    Aur haan cake mein mera hissa lazmi rakhna! 😂🎂
    </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🎀 NEXT → Chalo Ab Duayein Le Lo"):
        st.session_state.page = 2
        st.rerun()

# ---------------- PAGE 2: DUAS ----------------
elif st.session_state.page == 2:

    st.markdown("""
    <div class="hero">
    <div class="decor">🤲 🌙 ✨</div>
    <h1 class="heading">Beautiful Prayers</h1>
    <div class="subheading">Meri pyari si duayein tumhare liye... 🤍</div>
    </div>

    <div class="card">
    <p class="message">
    🤍 Allah tumhari zindagi ko khushiyon se bhar de.<br><br>
    🤍 Tumhari har jaiz dua qubool ho.<br><br>
    🤍 Allah tumhein sehat, sukoon aur kamyabi ata farmaye.<br><br>
    🤍 Tumhare har mushkil raste ko asaan kare.<br><br>
    🤍 Tumhari aankhon mein aansu aayein bhi to sirf khushi ke.<br><br>
    🤍 Allah tumhein duniya aur akhirat dono mein kamyabi de.<br><br>
    <b>Ameen Sum Ameen! 🤲❤️</b>
    </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("💗 NEXT → Ab Tareef Suno Madam"):
        st.session_state.page = 3
        st.rerun()

# ---------------- PAGE 3: CONGRATULATIONS ----------------
elif st.session_state.page == 3:

    st.markdown("""
    <div class="hero">
    <div class="decor">😂 👑 💅</div>
    <h1 class="heading">Officially Amazing!</h1>
    <div class="subheading">Aaj tumhari hi party hai madam! 🤣</div>
    </div>

    <div class="card">
    <p class="message">
    🏆 Congratulations! Ek aur saal survive kar liya! 😂<br><br>
    👑 Beauty level: Unlimited<br><br>
    💅 Attitude level: Premium subscription<br><br>
    🤣 Drama level: Out of syllabus<br><br>
    💖 Smile level: Absolutely priceless<br><br>
    Aur sab se bari achievement...<br>
    Meri jaisi personality ko tolerate karna! 🤣❤️
    </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🌸 NEXT → Ab Thori Dil Ki Baat"):
        st.session_state.page = 4
        st.rerun()

# ---------------- PAGE 4: SPECIAL MESSAGE ----------------
elif st.session_state.page == 4:

    st.markdown("""
    <div class="hero">
    <div class="decor">💌 🌹 ❤️</div>
    <h1 class="heading">A Special Message</h1>
    <div class="subheading">Kuch baatein jo dil se kehni hain... 🥹</div>
    </div>

    <div class="card">
    <div class="main-title" style="font-size:60px">Dear Ruhii</div>
    <p class="message">
    Life mein kuch log aise hote hain jo apni presence se
    har moment ko special bana dete hain.<br><br>

    Tum bhi unhi special logon mein se ho.<br><br>

    I hope tumhari life ka har naya chapter pehle se zyada
    beautiful ho. Tum hamesha grow karo, smile karo aur
    apne dreams achieve karo.<br><br>

    Chahe kitni bhi nok jhok ho, meri dua hai ke tum hamesha
    khush raho aur tumhein woh sab mile jo tumhare dil ke liye
    behtareen ho. ❤️
    </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("💌 NEXT → Last Surprise Baqi Hai"):
        st.session_state.page = 5
        st.rerun()

# ---------------- PAGE 5: FINAL SURPRISE ----------------
elif st.session_state.page == 5:

    st.markdown("""
    <div class="hero">
    <div class="decor">🎀 💖 🌸</div>
    <div class="main-title">Forever Blessed</div>
    <div class="subheading">Hamesha muskurati rehna Ruhii! 🦋</div>
    </div>

    <div class="card">
    <h2 class="heading">One Last Wish</h2>
    <p class="message">
    May every sunrise bring you hope,<br>
    every sunset bring you peace,<br>
    and every new day bring you countless reasons to smile.<br><br>

    Keep shining, keep smiling and keep being YOU! ❤️<br><br>

    Once Again...<br>
    <b>HAPPY BIRTHDAY RUHII! 🎂🎉</b>
    </p>
    <div class="decor">❤️ 🥹 🌷 🎂</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🎉 ONE LAST CLICK - LET'S CELEBRATE!"):
        st.balloons()
        st.snow()

    if st.button("🔁 REPLAY MY SURPRISE"):
        st.session_state.page = 0
        st.rerun()

# ---------------- FOOTER ----------------
st.markdown("""
<div style="text-align:center;padding:30px;color:#ffe0f0;
font-family:'Cormorant Garamond',serif;font-size:23px;">
Made with love, a little madness & lots of duas 💗<br>
✧ A Birthday Surprise for Ruhii ✧
</div>
""", unsafe_allow_html=True)
