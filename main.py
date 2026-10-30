
import streamlit as st
import streamlit.components.v1 as components
import time

# ==========================================
# RUHII - BIRTHDAY SURPRISE WEBSITE
# ==========================================

st.set_page_config(
    page_title="Happy Birthday My Dear Bestiee 🎀",
    page_icon="💗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# PERSONAL DETAILS
# ==========================================

FRIEND = "Ruhii"
YOUR_NAME = "Your Best Friend"

# Change YOUR_NAME to your actual name.

# ==========================================
# SESSION STATE
# ==========================================

if "step" not in st.session_state:
    st.session_state.step = 0

if "gift_open" not in st.session_state:
    st.session_state.gift_open = False

if "letter_open" not in st.session_state:
    st.session_state.letter_open = False

# ==========================================
# DESIGN
# ==========================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@500;600;700&family=Playfair+Display:wght@500;600;700&family=Poppins:wght@300;400;500;600;700&display=swap');

.stApp {
    font-family: 'Poppins', sans-serif;
}

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    font-weight: 700;
    letter-spacing: 0.5px;
}

.hero h1 {
    font-family: 'Playfair Display', serif !important;
    font-size: clamp(38px, 7vw, 68px);
    font-weight: 700;
    letter-spacing: 1px;
}

.special-text {
    font-family: 'Dancing Script', cursive !important;
    font-size: clamp(38px, 6vw, 58px);
    color: #d34f91;
    font-weight: 700;
    text-align: center;
}

.subtitle {
    font-family: 'Poppins', sans-serif;
    font-size: 16px;
    font-weight: 400;
    line-height: 2.1;
    letter-spacing: 0.2px;
}

.quote {
    font-family: 'Dancing Script', cursive;
    font-size: 27px;
    color: #b64279;
}


@keyframes appear {
    from {opacity:0; transform:translateY(25px);}
    to {opacity:1; transform:translateY(0);}
}

@keyframes beat {
    0%,100% {transform:scale(1);}
    50% {transform:scale(1.2);}
}

@keyframes bounce {
    0%,100% {transform:translateY(0);}
    50% {transform:translateY(-15px);}
}

@keyframes gift {
    0%,100% {transform:rotate(-5deg) scale(1);}
    50% {transform:rotate(5deg) scale(1.1);}
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# LIVE FLOATING HEARTS
# ==========================================

components.html("""
<div id="sky"></div>
<style>
#sky {
    position: fixed;
    inset: 0;
    pointer-events: none;
    overflow: hidden;
}
.floating {
    position: absolute;
    bottom: -50px;
    animation: floatUp linear infinite;
    opacity: 0;
}
@keyframes floatUp {
    0% {transform:translateY(0) rotate(0deg);opacity:0;}
    15% {opacity:.8;}
    100% {transform:translateY(-110vh) rotate(360deg);opacity:0;}
}
</style>
<script>
const sky=document.getElementById("sky");
const symbols=["💗","💕","✨","🌸","🎀","🦋","💖"];
for(let i=0;i<24;i++){
    let x=document.createElement("span");
    x.className="floating";
    x.innerText=symbols[Math.floor(Math.random()*symbols.length)];
    x.style.left=Math.random()*100+"%";
    x.style.animationDuration=(8+Math.random()*10)+"s";
    x.style.animationDelay=(-Math.random()*15)+"s";
    x.style.fontSize=(16+Math.random()*18)+"px";
    sky.appendChild(x);
}
</script>
""", height=0)

# ==========================================
# BALLOON ENTRANCE ANIMATION
# ==========================================

def balloon_animation():

    components.html("""
    <div class="scene">
      <div class="balloon b1">🎈</div>
      <div class="balloon b2">🎈</div>
      <div class="balloon b3">🎈</div>
      <div class="balloon b4">🎈</div>
      <div class="balloon b5">🎈</div>
      <div class="balloon b6">🎈</div>
      <div class="balloon b7">🎈</div>
      <div class="balloon b8">🎈</div>
    </div>
    <style>
      body {margin:0;background:transparent;overflow:hidden;}
      .scene {height:180px;position:relative;overflow:hidden;}
      .balloon {
        position:absolute;
        bottom:-100px;
        font-size:65px;
        animation: enter 3s ease-out forwards;
      }
      .b1 {left:-10%;animation-delay:0s;}
      .b2 {left:12%;animation-delay:.3s;}
      .b3 {left:30%;animation-delay:.6s;}
      .b4 {left:48%;animation-delay:.9s;}
      .b5 {right:30%;animation-delay:1.2s;}
      .b6 {right:12%;animation-delay:.4s;}
      .b7 {right:-10%;animation-delay:.7s;}
      .b8 {left:68%;animation-delay:1s;}
      @keyframes enter {
        0% {transform:translateY(180px) scale(.3);opacity:0;}
        60% {opacity:1;}
        100% {transform:translateY(-180px) scale(1);opacity:1;}
      }
    </style>
    """, height=190)

# ==========================================
# NAVIGATION FUNCTION
# ==========================================

def next_page():
    st.session_state.step += 1
    st.rerun()

def previous_page():
    st.session_state.step -= 1
    st.rerun()

def next_button(label="NEXT PAGE 💗"):
    st.write("")
    a,b,c = st.columns([1,2,1])
    with b:
        if st.button(label, key=f"next_{st.session_state.step}"):
            next_page()

def back_button():
    a,b,c = st.columns([1,2,1])
    with b:
        if st.button("← PREVIOUS PAGE", key=f"back_{st.session_state.step}"):
            previous_page()

# ==========================================
# WELCOME SCREEN
# ==========================================

if st.session_state.step == 0:

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">A LITTLE SURPRISE IS WAITING FOR YOU</div>
        <div class="heart">💗</div>
        <h1>Hey Ruhii! 🎀</h1>
        <h2>Your Special Day Is Here!</h2>
        <p class="subtitle">
        Someone has created a little magical world
        just for you.
        <br><br>
        Are you ready to enter?
        </p>
        <div style="font-size:42px;">🌸 🦋 🎀 💕</div>
    </div>
    """, unsafe_allow_html=True)

    st.write("")
    a,b,c=st.columns([1,2,1])

    with b:
        if st.button("💗 CLICK HERE, RUHII 💗"):
            st.session_state.step=1
            st.rerun()

# ==========================================
# PAGE 1: BIRTHDAY CELEBRATION
# ==========================================

elif st.session_state.step == 1:

    balloon_animation()

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">TODAY IS ALL ABOUT YOU</div>
        <div class="heart">💖</div>
        <h1>Happy Birthday</h1>
        <h1>My Dear Bestiee!</h1>
        <div class="cake">🎂</div>
        <h2>Happiest Birthday Ruhii! 🎀</h2>
        <p class="subtitle">
        Finally, tumhara special day aa gaya!
        <br>
        Aaj sirf smile karna hai, enjoy karna hai
        aur bohat saari khushiyan collect karni hain.
        <br><br>
        You deserve all the beautiful things in life!
        </p>
        <div style="font-size:35px;">🎈 🌸 🦋 ✨ 🎉</div>
    </div>
    """, unsafe_allow_html=True)

    st.balloons()

    next_button("LET'S SEE YOUR WISHES 💌")
    back_button()

# ==========================================
# PAGE 2: BIRTHDAY WISHES
# ==========================================

elif st.session_state.step == 2:

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">A MESSAGE FROM THE HEART</div>
        <h1>Birthday Wishes 💌</h1>
        <p>Every little wish is specially for you!</p>
    </div>
    """, unsafe_allow_html=True)

    wishes=[
        ("🌸 Endless Happiness",
         "May your life hamesha khushiyon se bhari rahe. "
         "Tumhari smile kabhi fade na ho aur har din "
         "tumhare liye ek beautiful reason lekar aaye."),

        ("🦋 Dream Big",
         "May all your dreams come true. Allah tumhein "
         "har us manzil tak pohanchaye jahan tum pohanchna chahti ho."),

        ("💗 Beautiful Memories",
         "I hope this year gives you unforgettable memories, "
         "unexpected surprises and lots of reasons to smile."),

        ("🎀 Keep Shining",
         "Never underestimate yourself. Tum bohat kuch "
         "achieve kar sakti ho. Always believe in yourself."),

        ("✨ A Beautiful Future",
         "May your future be brighter than your past "
         "and your coming days be full of love, success and peace.")
    ]

    for title,message in wishes:
        st.markdown(f"""
        <div class="card">
            <h2>{title}</h2>
            <p class="subtitle">{message}</p>
        </div>
        """,unsafe_allow_html=True)

    st.markdown("""
    <div class="card center">
        <div class="quote">
        "You deserve happiness, not just today,
        but every single day." 💗
        </div>
    </div>
    """,unsafe_allow_html=True)

    next_button("NOW SOME SPECIAL DUAS 🤲")
    back_button()

# ==========================================
# PAGE 3: DUAS
# ==========================================

elif st.session_state.step == 3:

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">PRAYERS FROM THE HEART</div>
        <h1>Special Duas For You 🤲</h1>
        <p>Words may finish, but good duas never do.</p>
    </div>
    """,unsafe_allow_html=True)

    duas=[
        ("🤲 Happiness",
         "May Allah tumhare dil ko sukoon de, "
         "har pareshani door kare aur hamesha khush rakhe."),

        ("🌷 Success",
         "May Allah tumhari mehnat mein barkat de, "
         "tumhare dreams poore kare aur har achay maqsad "
         "mein kamyabi ata farmaye."),

        ("💗 Health",
         "May Allah tumhein sehat, afiyat aur lambi "
         "khushhaal zindagi ata farmaye."),

        ("🕊️ Protection",
         "May Allah tumhein har buri nazar, har mushkil "
         "aur har nuqsan se mehfooz rakhe."),

        ("✨ Blessings",
         "May Allah tumhari zindagi ko rehmat, barkat, "
         "mohabbat aur kamyabi se bhar de.")
    ]

    for title,message in duas:
        st.markdown(f"""
        <div class="card">
            <h2>{title}</h2>
            <p class="subtitle">{message}</p>
        </div>
        """,unsafe_allow_html=True)

    st.markdown("""
    <div class="hero center">
        <h1>آمین یا رب العالمین 🤍</h1>
        <p>May every good dua become a reality.</p>
    </div>
    """,unsafe_allow_html=True)

    next_button("ONE MORE SPECIAL PAGE 🦋")
    back_button()

# ==========================================
# PAGE 4: MEMORIES AND PHOTOS
# ==========================================

elif st.session_state.step == 4:

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">SOME WORDS FOR MY BESTIE</div>
        <h1>Our Beautiful Bond 🦋</h1>
        <p>Some people make life a little more special.</p>
    </div>
    """,unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <h2>Dear Ruhii 💗</h2>
        <p class="subtitle">
        Life mein bohat se log milte hain,
        lekin kuch log apni jagah alag bana lete hain.
        <br><br>
        I hope tumhari life mein hamesha beautiful moments,
        genuine people aur endless happiness rahe.
        <br><br>
        Apne dreams kabhi mat chorna,
        apni worth kabhi mat bhoolna
        aur apni smile ko kabhi lose mat karna.
        <br><br>
        You are special and you deserve to be happy.
        </p>
    </div>
    """,unsafe_allow_html=True)

    st.markdown("""
    <div class="card center">
        <h2>Our Little Memory Gallery 📸</h2>
        <p>
        Add your favourite pictures together here!
        </p>
    </div>
    """,unsafe_allow_html=True)

    photos=st.file_uploader(
        "Upload 2-3 favourite pictures",
        type=["jpg","jpeg","png","webp"],
        accept_multiple_files=True,
        key="ruhi_photos"
    )

    if photos:
        for i in range(0,len(photos),2):
            cols=st.columns(2)
            for j in range(2):
                if i+j < len(photos):
                    with cols[j]:
                        st.image(
                            photos[i+j],
                            use_container_width=True,
                            caption="A beautiful memory 💗"
                        )

    st.markdown("""
    <div class="card center">
        <h2>Friendship Quotes 🌸</h2>
        <p class="quote">
        "Some bonds are special because they are genuine."
        </p>
        <p class="quote">
        "Good memories stay forever."
        </p>
        <p class="quote">
        "A little kindness can make someone's whole day."
        </p>
    </div>
    """,unsafe_allow_html=True)

    next_button("OPEN YOUR FINAL SURPRISE 🎁")
    back_button()

# ==========================================
# PAGE 5: FINAL SURPRISE
# ==========================================

elif st.session_state.step == 5:

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">THE LAST SURPRISE IS HERE</div>
        <h1>Something Special For You!</h1>
        <p>A little gift with lots of love. 💗</p>
    </div>
    """,unsafe_allow_html=True)

    st.markdown('<div class="gift">🎁</div>',
                unsafe_allow_html=True)

    a,b,c=st.columns([1,2,1])

    with b:
        if st.button("🎀 OPEN YOUR GIFT 🎀"):
            st.session_state.gift_open=True
            st.balloons()
            st.snow()

    if st.session_state.gift_open:

        st.markdown("""
        <div class="hero">
            <div class="cake">🎂</div>
            <h1>Happy Birthday My Dear Bestiee!</h1>
            <h2>Ruhii! 💗</h2>
            <p class="subtitle">
            I hope tumhari life ka har naya chapter
            pehle se zyada beautiful ho.
            <br><br>
            May Allah tumhari har achi wish poori kare,
            tumhein bohat saari khushiyan de
            aur hamesha apni hifazat mein rakhe.
            <br><br>
            Keep smiling, keep shining
            and never stop believing in yourself.
            <br><br>
            You deserve the world and all its beautiful things!
            </p>
            <h2>Stay Blessed Always! 🤲</h2>
        </div>
        """,unsafe_allow_html=True)

    st.write("")

    if st.button("💌 READ YOUR PERSONAL LETTER"):

        st.session_state.letter_open = not st.session_state.letter_open

    if st.session_state.letter_open:

        st.markdown(f"""
        <div class="card center">
            <h1>Dear Ruhii, 💗</h1>
            <p class="subtitle">
            Aaj tumhara birthday hai aur main chahta hoon
            ke tumhara din bohat beautiful guzray.
            <br><br>
            I genuinely wish that you achieve everything
            you dream about.
            <br><br>
            Life mein ups and downs aate rehte hain,
            but I hope tum hamesha strong raho
            aur apni happiness ko priority do.
            <br><br>
            May Allah bless you with everything
            that is good for your duniya and akhirah.
            <br><br>
            Once again, Happy Birthday My Dear Bestiee!
            <br><br>
            With lots of love and duas,
            <br>
            <b>{YOUR_NAME}</b> 🎀
            </p>
        </div>
        """,unsafe_allow_html=True)

    st.markdown("""
    <div class="card center">
        <h2>One Last Reminder 💕</h2>
        <p class="subtitle">
        This website has an ending,
        but my good wishes for you don't.
        <br><br>
        Keep smiling, Ruhii!
        </p>
        <div style="font-size:40px;">💗 🌸 🎀 🦋</div>
    </div>
    """,unsafe_allow_html=True)

    if st.button("RESTART YOUR BIRTHDAY JOURNEY 🔄"):
        st.session_state.step=0
        st.session_state.gift_open=False
        st.session_state.letter_open=False
        st.rerun()

    back_button()

# ==========================================
# PROGRESS AND FOOTER
# ==========================================

if st.session_state.step > 0:

    st.markdown("---")

    if st.session_state.step <= 5:
        st.markdown(
            f'<div class="progress-text">Birthday Journey: '
            f'{st.session_state.step}/5 💗</div>',
            unsafe_allow_html=True
        )

        st.progress(st.session_state.step/5)

st.markdown("""
<div class="footer">
    🎀 Made with love, prayers and happiness 🎀
    <br><br>
    A little magical world for Ruhii 💗
    <br>
    Keep Smiling. Keep Shining. ✨
</div>
""",unsafe_allow_html=True)
