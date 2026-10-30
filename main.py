import random
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="A Little World Made for Ruhii 💗",
    page_icon="💗",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------- SESSION STATE ----------------------------
defaults = {
    "entered": False,
    "current_page": 1,
    "compliment": None,
    "hug_sent": False,
}
for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ---------------------------- GLOBAL STYLING ----------------------------
st.markdown(
    r"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700;800&family=Great+Vibes&display=swap');

    :root {
      --ink: #563b58;
      --muted: #866b87;
      --pink: #f7a9c8;
      --rose: #d982a9;
      --lavender: #c7b5f4;
      --cream: #fff8fb;
    }
    html, body, [data-testid="stAppViewContainer"] {
      background: #fff8fc !important;
      color: var(--ink);
      font-family: 'DM Sans', sans-serif;
    }
    [data-testid="stHeader"], [data-testid="stToolbar"],
    [data-testid="stDecoration"], footer, #MainMenu,
    [data-testid="stSidebar"] { display: none !important; }
    .block-container {
      max-width: 1050px !important;
      padding: 2rem 1.15rem 3rem !important;
    }
    [data-testid="stAppViewContainer"] {
      background:
        radial-gradient(circle at 12% 12%, rgba(255,190,218,.42), transparent 28%),
        radial-gradient(circle at 88% 20%, rgba(203,185,255,.35), transparent 30%),
        radial-gradient(circle at 55% 90%, rgba(255,218,196,.35), transparent 32%),
        linear-gradient(135deg,#fff8fc 0%,#fbf6ff 52%,#fff9f5 100%) !important;
      min-height: 100vh;
    }
    .eyebrow {
      text-transform: uppercase; letter-spacing: .22em; font-size: .72rem;
      color: #b2779a; font-weight: 700; text-align: center;
    }
    .hero-title {
      font-family: 'Playfair Display', serif; font-weight: 800;
      text-align: center; line-height: 1.08; letter-spacing: -.035em;
      font-size: clamp(2.55rem, 7vw, 5.7rem);
      background: linear-gradient(100deg,#c66f9e,#8e76c7,#d98b9f);
      -webkit-background-clip: text; background-clip: text; color: transparent;
      filter: drop-shadow(0 8px 18px rgba(207,125,171,.18));
      margin: .35rem 0 .65rem;
    }
    .script-title {
      font-family: 'Great Vibes', cursive; color: #bd79a0;
      font-size: clamp(2.3rem,5vw,3.5rem); text-align:center;
      line-height:1.1; margin:.2rem 0 .5rem;
    }
    .subtitle {
      text-align:center; color:#896f8d; font-size:1.03rem;
      line-height:1.75; max-width:760px; margin:0 auto 1.5rem;
    }
    .glass {
      background: rgba(255,255,255,.69);
      border: 1px solid rgba(255,255,255,.92);
      border-radius: 28px; padding: clamp(1.2rem,3vw,2.1rem);
      box-shadow: 0 18px 55px rgba(164,112,158,.12), inset 0 1px 0 #fff;
      backdrop-filter: blur(16px);
      margin: 1rem auto;
    }
    .letter {
      color:#654e68; font-size:1.02rem; line-height:2;
      white-space:normal;
    }
    .quote-card {
      background: linear-gradient(135deg,rgba(255,226,239,.88),rgba(247,238,255,.9));
      border:1px solid rgba(255,255,255,.95); border-radius:22px;
      padding:1.1rem 1.25rem; margin:.8rem 0;
      color:#755777; box-shadow:0 10px 28px rgba(190,135,177,.10);
      line-height:1.75;
    }
    .dua-card {
      background:linear-gradient(135deg,rgba(255,255,255,.92),rgba(241,235,255,.9));
      border:1px solid #fff; border-radius:20px; padding:1rem 1.2rem;
      margin:.72rem 0; color:#65567c; line-height:1.7;
      box-shadow:0 9px 24px rgba(141,117,183,.09);
    }
    .news {
      text-align:center; padding:1.25rem; border-radius:22px;
      background:linear-gradient(110deg,#fff0f5,#fff8ed);
      border:1px solid #fff; color:#a65d81; font-weight:700;
      line-height:1.7; box-shadow:0 10px 25px rgba(208,134,164,.1);
    }
    .progress-wrap { max-width:520px; margin:1rem auto 1.7rem; }
    .progress-label { text-align:center; color:#9a7b9d; font-size:.82rem; margin-bottom:.55rem; }
    .progress-track { height:7px; border-radius:20px; background:#f0e5f0; overflow:hidden; }
    .progress-fill { height:100%; border-radius:20px; background:linear-gradient(90deg,#f3a6c7,#b9a2ed); }
    .heart-orbit { font-size:5rem; text-align:center; animation: heartbeat 1.5s ease-in-out infinite; filter:drop-shadow(0 8px 14px #e9a3c4); }
    .footer-note { text-align:center; color:#a184a1; font-size:.85rem; padding:2rem 0 .5rem; }
    .tiny-note { text-align:center; color:#b18ba7; font-size:.78rem; letter-spacing:.06em; }
    .stButton > button {
      border:0 !important; border-radius:999px !important;
      padding:.78rem 1.3rem !important; min-height:3rem;
      color:#fff !important; font-weight:700 !important; letter-spacing:.01em;
      background:linear-gradient(100deg,#df8fb5,#aa91dc) !important;
      box-shadow:0 9px 23px rgba(190,123,173,.25) !important;
      transition:transform .22s ease, box-shadow .22s ease !important;
      width:100%;
    }
    .stButton > button:hover {
      transform:translateY(-3px) scale(1.015);
      box-shadow:0 13px 27px rgba(190,123,173,.34) !important;
    }
    .stButton > button:focus { outline:2px solid #d99abd !important; outline-offset:3px; }
    div[data-testid="column"] { min-width:0; }
    @keyframes heartbeat { 0%,100%{transform:scale(1)} 15%{transform:scale(1.12)} 30%{transform:scale(1)} 45%{transform:scale(1.08)} }
    @media(max-width:640px) {
      .block-container{padding:1.2rem .85rem 2rem !important}
      .glass{border-radius:22px}
      .subtitle{font-size:.94rem}
    }
    @media(prefers-reduced-motion:reduce) {
      *,*::before,*::after{animation-duration:.01ms !important;animation-iteration-count:1 !important;scroll-behavior:auto !important}
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------- ANIMATED BACKDROP ----------------------------
def render_ambient(theme: str = "pink", height: int = 1):
    palettes = {
        "pink": ("#f6a9c8", "#d8b5f4", "💗", "🌸"),
        "lavender": ("#c9b8f4", "#f2d49a", "✦", "✨"),
        "party": ("#f5a1c6", "#a9d9ef", "🎉", "😂"),
        "romance": ("#ef9fbd", "#c2a9ed", "♡", "💞"),
    }
    a, b, symbol1, symbol2 = palettes.get(theme, palettes["pink"])
    components.html(
        f"""
        <div class="ambient">
          <div class="orb orb-a"></div><div class="orb orb-b"></div>
          <div class="float f1">{symbol1}</div><div class="float f2">{symbol2}</div>
          <div class="float f3">✧</div><div class="float f4">♡</div>
          <div class="float f5">❀</div><div class="float f6">✦</div>
          <div class="dust d1">·</div><div class="dust d2">✧</div><div class="dust d3">·</div>
        </div>
        <style>
          html,body{{margin:0;background:transparent;overflow:hidden}}
          .ambient{{height:1px;position:relative;overflow:visible;pointer-events:none}}
          .orb{{position:fixed;width:240px;height:240px;border-radius:50%;filter:blur(65px);opacity:.15;z-index:0}}
          .orb-a{{background:{a};top:15%;left:-100px;animation:driftA 17s ease-in-out infinite alternate}}
          .orb-b{{background:{b};right:-100px;bottom:5%;animation:driftB 20s ease-in-out infinite alternate}}
          .float{{position:fixed;bottom:-60px;z-index:0;opacity:0;color:{a};font-size:24px;
            text-shadow:0 0 16px {b};animation:rise 17s linear infinite}}
          .f1{{left:8%;animation-delay:-3s}}.f2{{left:28%;animation-delay:-11s;font-size:18px}}
          .f3{{left:57%;animation-delay:-7s;font-size:22px}}.f4{{left:78%;animation-delay:-14s}}
          .f5{{left:91%;animation-delay:-5s;font-size:19px}}.f6{{left:43%;animation-delay:-16s}}
          .dust{{position:fixed;color:{b};font-size:25px;opacity:.55;animation:twinkle 4s ease-in-out infinite}}
          .d1{{left:18%;top:25%}}.d2{{left:82%;top:40%;animation-delay:1.4s}}.d3{{left:65%;top:15%;animation-delay:2s}}
          @keyframes rise{{0%{{transform:translateY(0) rotate(0);opacity:0}}12%{{opacity:.5}}85%{{opacity:.45}}100%{{transform:translateY(-115vh) rotate(250deg);opacity:0}}}}
          @keyframes twinkle{{0%,100%{{opacity:.2;transform:scale(.7)}}50%{{opacity:.85;transform:scale(1.25)}}}}
          @keyframes driftA{{to{{transform:translate(90px,50px)}}}}@keyframes driftB{{to{{transform:translate(-80px,-60px)}}}}
        </style>
        """,
        height=height,
        scrolling=False,
    )

# ---------------------------- HELPERS ----------------------------
def go_to(page: int):
    st.session_state.current_page = max(1, min(4, page))
    st.rerun()

def page_header(title: str, subtitle: str, page: int):
    st.markdown(f'<div class="eyebrow">A LITTLE WORLD MADE FOR RUHII · {page:02d}/04</div>', unsafe_allow_html=True)
    st.markdown(f'<h1 class="script-title">{title}</h1>', unsafe_allow_html=True)
    st.markdown(f'<div class="subtitle">{subtitle}</div>', unsafe_allow_html=True)
    pct = page * 25
    st.markdown(
        f'<div class="progress-wrap"><div class="progress-label">Surprise {page} of 4 · {pct}% of the magic</div>'
        f'<div class="progress-track"><div class="progress-fill" style="width:{pct}%"></div></div></div>',
        unsafe_allow_html=True,
    )

def nav_row(previous: bool = True, next_label: str = "Next Surprise ➜", next_page: int = 2):
    left, right = st.columns(2) if previous else (None, st.container())
    if previous:
        with left:
            if st.button("← Previous Little Surprise", key=f"prev_{st.session_state.current_page}"):
                go_to(st.session_state.current_page - 1)
    with right:
        if st.button(next_label, key=f"next_{st.session_state.current_page}"):
            go_to(next_page)

# ---------------------------- OPENING EXPERIENCE ----------------------------
if not st.session_state.entered:
    render_ambient("pink")
    st.markdown('<div style="height:2.3rem"></div>', unsafe_allow_html=True)
    st.markdown('<div class="eyebrow">A SECRET LITTLE SURPRISE IS WAITING</div>', unsafe_allow_html=True)
    st.markdown('<h1 class="hero-title" style="font-size:clamp(2.8rem,8vw,5.4rem)">Hey Ruhii! 👀</h1>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Someone has a very special surprise for you!<br>So take a deep breath, princess… your little world is ready. 💗</div>', unsafe_allow_html=True)

    components.html(
        r"""
        <div class="count-wrap">
          <div class="count-label">THE MAGIC BEGINS IN</div>
          <div id="count" class="count">3</div>
          <div class="count-caption">Make a wish ✨</div>
        </div>
        <style>
          body{margin:0;background:transparent;font-family:Arial,sans-serif}
          .count-wrap{text-align:center;padding:8px 0 15px}
          .count-label{font-size:11px;letter-spacing:4px;color:#b27e9e;font-weight:bold}
          .count{font-size:90px;font-weight:800;line-height:1.25;
            background:linear-gradient(130deg,#e78eb7,#a58bdb);-webkit-background-clip:text;color:transparent;
            filter:drop-shadow(0 8px 18px #e9b4d0);animation:pop .85s ease-in-out infinite}
          .count-caption{color:#a786a7;font-size:14px;letter-spacing:2px}
          @keyframes pop{0%,100%{transform:scale(.88);opacity:.7}50%{transform:scale(1.12);opacity:1}}
          .reveal{font-size:clamp(25px,5vw,46px);font-weight:900;letter-spacing:1px;
            background:linear-gradient(90deg,#d97ca8,#9278ca,#e4a17e);-webkit-background-clip:text;color:transparent;
            animation:reveal .8s ease both;text-shadow:0 8px 25px #f2c6dc}
          @keyframes reveal{from{opacity:0;transform:scale(.55) rotate(-5deg)}to{opacity:1;transform:scale(1) rotate(0)}}
          .cake{font-size:64px;animation:bounce 1.5s ease-in-out infinite}
          @keyframes bounce{0%,100%{transform:translateY(0)}50%{transform:translateY(-12px)}}
          .spark{font-size:22px;display:inline-block;animation:spin 4s linear infinite;margin:0 9px}
          @keyframes spin{to{transform:rotate(360deg)}}
          .confetti{position:fixed;top:-15px;width:8px;height:13px;animation:fall 3.2s linear infinite;opacity:.85}
          @keyframes fall{to{transform:translateY(110vh) rotate(760deg);opacity:.1}}
        </style>
        <div id="birthday" style="display:none;text-align:center">
          <div><span class="spark">✦</span><span class="spark">✧</span><span class="spark">✦</span></div>
          <div class="reveal">HAPPY BIRTHDAY RUHII! 🎂</div>
          <div class="cake">🎂</div>
          <div style="color:#98799b;line-height:1.8">Made with a little madness, endless duas,<br>and lots of love. 💗</div>
          <div style="font-size:25px;margin-top:10px">🎈 💖 🎈</div>
        </div>
        <script>
          const el=document.getElementById('count'), birthday=document.getElementById('birthday');
          let n=3;
          const timer=setInterval(()=>{
            n--;
            if(n>0){el.textContent=n;}
            else{
              clearInterval(timer);
              document.querySelector('.count-label').style.display='none';
              el.style.display='none';
              document.querySelector('.count-caption').style.display='none';
              birthday.style.display='block';
              for(let i=0;i<48;i++){
                const c=document.createElement('i');c.className='confetti';
                c.style.left=Math.random()*100+'vw';
                c.style.background=['#f3a4c5','#c4a8ee','#f5c58f','#a8d8d1'][i%4];
                c.style.animationDelay=Math.random()*2+'s';
                c.style.animationDuration=(2.5+Math.random()*2)+'s';
                document.body.appendChild(c);
              }
            }
          },1000);
        </script>
        """,
        height=280,
        scrolling=False,
    )
    st.markdown(
        '<div class="glass" style="text-align:center;max-width:650px">'
        '<div style="font-size:1.15rem;color:#956e91;font-family:Playfair Display,serif">A tiny universe, made just for you.</div>'
        '<div style="font-size:2rem;margin:.5rem">🌷 💌 🦋</div>'
        '<div class="tiny-note">YOUR SMILE IS THE MAIN EVENT</div></div>',
        unsafe_allow_html=True,
    )
    if st.button("Okay Princess, Enter Your World 💗", key="enter_world"):
        st.session_state.entered = True
        st.session_state.current_page = 1
        st.rerun()
    st.markdown('<div class="footer-note">P.S. The countdown runs all by itself… no patience test, promise. 😉</div>', unsafe_allow_html=True)

# ---------------------------- MAIN FOUR-PAGE EXPERIENCE ----------------------------
else:
    page = st.session_state.current_page
    theme = {1: "pink", 2: "lavender", 3: "party", 4: "romance"}[page]
    render_ambient(theme)

    # Compact top navigation / home control
    top_left, top_right = st.columns([3, 1])
    with top_left:
        st.markdown('<div style="color:#ad83a5;font-size:.78rem;letter-spacing:.15em;padding:.5rem 0">♡ THE RUHII EDITION · MADE WITH LOVE</div>', unsafe_allow_html=True)
    with top_right:
        if st.button("⌂ Home", key=f"home_{page}"):
            st.session_state.current_page = 1
            st.rerun()

    if page == 1:
        page_header("A Special Day for a Special Soul", "Aj ka din sirf tumhara hai, madam! Toh smile karna compulsory hai. 😌", 1)
        st.markdown(
            """
            <div class="glass">
              <div class="eyebrow">A LETTER, STRAIGHT FROM THE HEART</div>
              <div class="script-title" style="font-size:2.6rem">Dear Ruhii, 💌</div>
              <div class="letter">
                Happy Birthday to one of the most special people in my life. Tumhari friendship meri life ka ek beautiful part hai.
                I hope tumhari life hamesha happiness, success, laughter aur beautiful memories se filled rahe.
                Hamesha aise hi smile karti rehna because your smile deserves the whole universe.
                <br><br><b>May this new chapter bring you beautiful surprises, peaceful days, big wins, and countless reasons to smile.</b>
              </div>
              <div style="text-align:center;font-size:2rem;margin-top:1rem;letter-spacing:.4rem">💗 💞 💗</div>
            </div>
            <div class="quote-card" style="text-align:center">
              <div style="font-size:1.6rem">♡  ♡  ♡</div>
              Some people make life brighter just by being in it. You are one of those people, Ruhii. 🌷
            </div>
            <div class="news">🚨 BREAKING NEWS 🚨<br>Aaj duniya ki sabse cute aur thori si pagal larki ka birthday hai! 😂</div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('<div style="height:.6rem"></div>', unsafe_allow_html=True)
        if st.button("Next Surprise, Madam Ji! ➜", key="page1_next"):
            go_to(2)

    elif page == 2:
        page_header("Prayers From My Heart", "Allah tumhari zindagi ko khushiyon aur barkaton se bhar de. Ameen! 🤍", 2)
        duas = [
            "Allah tumhari har jaiz dua qabool farmaye. 🤲",
            "Allah tumhari zindagi ko sehat, sukoon, khushiyon aur barkaton se bhar de. ✨",
            "Tumhare har mushkil raste ko asaan farmaye. 🌙",
            "Tumhein duniya aur akhirat dono mein kamyabi ata farmaye. 🤍",
            "Tumhari aankhon mein hamesha khushi ke aansu hon, gham ke nahi. 🌸",
            "Allah tumhein buri nazar, pareshani aur har takleef se mehfooz rakhe. 🧿",
        ]
        st.markdown('<div class="glass"><div class="eyebrow">SIX LITTLE PRAYERS, ONE BIG WISH</div>', unsafe_allow_html=True)
        for i, dua in enumerate(duas, 1):
            st.markdown(f'<div class="dua-card"><span style="color:#b392d6;font-weight:800;margin-right:10px">{i:02d}</span>{dua}</div>', unsafe_allow_html=True)
        st.markdown('<div class="script-title" style="font-size:2.8rem;margin-top:1rem">Ameen Sum Ameen! 🤲</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="tiny-note">MAY EVERY GOOD THING FIND ITS WAY TO YOU ✦</div>', unsafe_allow_html=True)
        nav_row(True, "Chalo Ab Thori Masti Ho Jaye 😂", 3)

    elif page == 3:
        page_header("Ruhii Ki Pagalpanti Department", "Warning: Is page ko dekh kar hansna mana nahi hai! 🤣", 3)
        funny = [
            "Congratulations! Tum officially ek saal aur experienced ho gayi ho... lekin harkatein abhi bhi bachon wali hain. 😂",
            "Cake tumhara hai, lekin khaane ka haq mera bhi banta hai. 🎂",
            "Tumhari age increase ho rahi hai, maturity abhi bhi loading hai... 2%. 🤣",
            "Aaj tumhari har wish poori ho, bas mujhe tang karne wali wishes exclude hain. 😌",
        ]
        st.markdown('<div class="glass"><div class="eyebrow">OFFICIAL DEPARTMENT MEMO</div>', unsafe_allow_html=True)
        for item in funny:
            st.markdown(f'<div class="quote-card">😂 &nbsp; {item}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        compliments = [
            "Tumhari smile literally mood fresh kar deti hai. 🌷",
            "Tum cute bhi ho aur certified troublemaker bhi. 😂",
            "Tumhari friendship ek premium subscription jaisi hai — totally worth it! 💗",
            "Tumhare jaisi dost milna lucky logon ka kaam hai. 🍀",
            "Tumhari energy boring din ko bhi mini celebration bana deti hai. 🎉",
            "Tumhari aankhon mein shararat aur dil mein bohat sweetness hai. ✨",
            "Tum ek walking sunshine ho… bas kabhi kabhi thunderstorm bhi. ⛈️",
            "Tumhari presence hi kisi bhi memory ko special bana sakti hai. 🦋",
            "Tumhari hasi ka volume high ho sakta hai, lekin value us se bhi high hai. 😭💞",
        ]
        if st.button("Reveal My Birthday Compliment 💝", key="compliment_button"):
            choices = [c for c in compliments if c != st.session_state.compliment]
            st.session_state.compliment = random.choice(choices or compliments)
        if st.session_state.compliment:
            st.markdown(
                f'<div class="glass" style="text-align:center;border:1px solid #f5d2e3">'
                f'<div class="script-title" style="font-size:2.4rem">Ahem… listen up! 💝</div>'
                f'<div style="font-size:1.12rem;line-height:1.8;color:#765979">{st.session_state.compliment}</div>'
                f'<div style="font-size:1.8rem;margin-top:.6rem">💗 ✨ 💗</div></div>',
                unsafe_allow_html=True,
            )
        nav_row(True, "Ab Last Surprise Dekho ❤️", 4)

    elif page == 4:
        page_header("One Last Thing, Ruhii...", "Kuch baatein hoti hain jo words mein explain karna mushkil hota hai.", 4)
        st.markdown(
            """
            <div class="glass" style="text-align:center">
              <div class="eyebrow">A LITTLE SOMETHING TO KEEP</div>
              <div class="heart-orbit">💗</div>
              <div class="letter" style="text-align:left;margin-top:1rem">
                Ruhii, I just want you to know that you are genuinely special. Life mein bohat se log milte hain,
                lekin kuch log apni presence se har moment ko beautiful bana dete hain. Tum unhi logon mein se ho.
                May your smile never fade, may your dreams come true, and may happiness always find its way to you.
                <br><br>
                Thank you for being you. Stay blessed, stay crazy, and never stop smiling.
              </div>
              <div class="script-title" style="font-size:clamp(1.8rem,4vw,2.8rem);margin-top:1.5rem">
                YOU DESERVE ALL THE HAPPINESS IN THE WORLD! 💗
              </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("One More Hug? 🤗", key="hug_button"):
            st.session_state.hug_sent = True
        if st.session_state.hug_sent:
            components.html(
                r"""
                <div class="hug-screen">
                  <div class="hug-heart">💗</div>
                  <div class="hug-title">SENDING YOU INFINITE<br>HUGS &amp; LOVE! 💗</div>
                  <div class="hug-sub">A giant virtual hug, wrapped in a million good wishes. 🤗</div>
                  <div class="hug-float">♡　💞　♡　💗　♡</div>
                </div>
                <style>
                  body{margin:0;background:transparent;font-family:Arial,sans-serif}
                  .hug-screen{text-align:center;padding:25px 8px 30px;border-radius:28px;
                    background:radial-gradient(circle,#fff 0%,#fff0f7 48%,#f1eaff 100%);overflow:hidden}
                  .hug-heart{font-size:85px;animation:heart .9s ease-in-out infinite;filter:drop-shadow(0 10px 20px #e9a3c4)}
                  .hug-title{font-size:clamp(23px,5vw,38px);font-weight:900;line-height:1.3;
                    background:linear-gradient(90deg,#d77da8,#9279c6);-webkit-background-clip:text;color:transparent}
                  .hug-sub{color:#947b9b;margin-top:12px;line-height:1.6}
                  .hug-float{font-size:25px;margin-top:17px;animation:float 2.5s ease-in-out infinite}
                  @keyframes heart{0%,100%{transform:scale(1)}50%{transform:scale(1.18)}}
                  @keyframes float{50%{transform:translateY(-9px)}}
                </style>
                """,
                height=270,
                scrolling=False,
            )
        st.markdown('<div class="footer-note">Made with ❤️ especially for Ruhii.</div>', unsafe_allow_html=True)
        left, right = st.columns(2)
        with left:
            if st.button("← Read the Duas Again", key="back_duas"):
                go_to(2)
        with right:
            if st.button("Start Our Little World Again ↺", key="restart"):
                st.session_state.current_page = 1
                st.session_state.compliment = None
                st.session_state.hug_sent = False
                st.rerun()

    st.markdown('<div class="footer-note">A Little World Made for Ruhii 💗 · Stay magical, princess.</div>', unsafe_allow_html=True)
