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
