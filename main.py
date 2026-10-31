/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState, useEffect, useRef } from 'react';
import {
  Heart,
  Volume2,
  VolumeX,
  ChevronRight,
  ChevronLeft,
  Home,
  Check,
  Copy,
  Code,
  Lock,
  Unlock,
  Clock,
  Sparkles,
  Camera,
  Trash2
} from 'lucide-react';

interface ActivityItem {
  time: string;
  event: string;
}

const COMPLIMENTS = [
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
];

const DUAS_WITH_EMOJIS = [
  { text: "Allah tumhari har jaiz dua qabool farmaye.", startEmoji: "🤲 🌸", endEmoji: "🤍" },
  { text: "Allah tumhari zindagi ko sehat, sukoon, khushiyon aur barkaton se bhar de.", startEmoji: "🌿 💖", endEmoji: "✨" },
  { text: "Tumhare har mushkil raste ko asaan farmaye.", startEmoji: "🕊️ 🌷", endEmoji: "💫" },
  { text: "Tumhein duniya aur akhirat dono mein kamyabi ata farmaye.", startEmoji: "👑 🌟", endEmoji: "🌙" },
  { text: "Tumhari aankhon mein hamesha khushi ke aansu hon, gham ke nahi.", startEmoji: "🥺 🌺", endEmoji: "💗" },
  { text: "Allah tumhein buri nazar, pareshani aur har takleef se mehfooz rakhe.", startEmoji: "🛡️ 🕊️", endEmoji: "🤲" }
];

const RUHII_GALLERY = [
  {
    src: "/gallery_1.jpg",
    title: "Royal Traditional Charm 👑",
    tagline: "Velvet elegance & royal grace • MashAllah pure queen vibes!"
  },
  {
    src: "/gallery_2.jpg",
    title: "Radiant in Red ❤️",
    tagline: "That sweet, innocent smile that lights up the whole room! ✨"
  },
  {
    src: "/gallery_3.jpg",
    title: "Peaceful in White 🕊️",
    tagline: "Sukoon aur Saadgi ki misaal • An angel in human form 🤍"
  },
  {
    src: "/gallery_4.jpg",
    title: "The Sweet Dark Angel 🖤",
    tagline: "Masoomiyat + thori si nautanki = 100% certified Ruhii! 🌸"
  }
];

export default function App() {
  const [countdownStep, setCountdownStep] = useState<number>(0);
  const [enteredWorld, setEnteredWorld] = useState<boolean>(false);
  const [currentPage, setCurrentPage] = useState<number>(1);
  const [compliment, setCompliment] = useState<string>('');
  const [showHug, setShowHug] = useState<boolean>(false);
  const [isMuted, setIsMuted] = useState<boolean>(false);
  const [showPythonCodeModal, setShowPythonCodeModal] = useState<boolean>(false);
  const [copiedCode, setCopiedCode] = useState<boolean>(false);

  // Secret page tracking state
  const [showSecretModal, setShowSecretModal] = useState<boolean>(false);
  const [secretUnlocked, setSecretUnlocked] = useState<boolean>(false);
  const [passwordInput, setPasswordInput] = useState<string>('');
  const [passwordError, setPasswordError] = useState<string>('');
  const [activityLog, setActivityLog] = useState<ActivityItem[]>([
    { time: new Date().toLocaleTimeString(), event: "Website opened by Ruhii 🌸" }
  ]);
  const pageEnterTimeRef = useRef<number>(Date.now());

  const audioCtxRef = useRef<AudioContext | null>(null);

  const logEvent = (msg: string) => {
    setActivityLog(prev => [
      ...prev,
      { time: new Date().toLocaleTimeString(), event: msg }
    ]);
  };

  const handlePageSwitch = (newPage: number) => {
    const elapsedSec = Math.round((Date.now() - pageEnterTimeRef.current) / 1000);
    const pageNames: Record<number, string> = {
      1: "Letter (Birthday Wishes)",
      2: "Duas & Prayers",
      3: "Royal Gallery (Ruhii's Photos)",
      4: "Masti & Pagalpanti",
      5: "Special Message & Hug"
    };
    logEvent(`Stayed on ${pageNames[currentPage] || 'Page ' + currentPage} for ${elapsedSec}s`);
    logEvent(`Opened ${pageNames[newPage] || 'Page ' + newPage} ➔`);
    setCurrentPage(newPage);
    setShowHug(false);
    pageEnterTimeRef.current = Date.now();
  };

  const playTuneNote = (frequency: number, duration: number, delay = 0) => {
    if (isMuted) return;
    try {
      if (!audioCtxRef.current) {
        audioCtxRef.current = new (window.AudioContext || (window as unknown as { webkitAudioContext: typeof AudioContext }).webkitAudioContext)();
      }
      const ctx = audioCtxRef.current;
      setTimeout(() => {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(frequency, ctx.currentTime);
        gain.gain.setValueAtTime(0.09, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + duration);
      }, delay);
    } catch {
      // Audio permission
    }
  };

  const playCelebrationChime = () => {
    const notes = [523.25, 659.25, 783.99, 1046.50, 1318.51];
    notes.forEach((freq, i) => playTuneNote(freq, 0.5, i * 140));
  };

  useEffect(() => {
    if (enteredWorld) return;

    if (countdownStep === 0) {
      const timer = setTimeout(() => {
        setCountdownStep(1);
        playTuneNote(440, 0.3);
      }, 2000);
      return () => clearTimeout(timer);
    } else if (countdownStep === 1) {
      const timer = setTimeout(() => {
        setCountdownStep(2);
        playTuneNote(493.88, 0.3);
      }, 1400);
      return () => clearTimeout(timer);
    } else if (countdownStep === 2) {
      const timer = setTimeout(() => {
        setCountdownStep(3);
        playTuneNote(523.25, 0.3);
      }, 1400);
      return () => clearTimeout(timer);
    } else if (countdownStep === 3) {
      const timer = setTimeout(() => {
        setCountdownStep(4);
        playCelebrationChime();
        logEvent("Revealed GRAND BIRTHDAY SCREEN 🎂");
      }, 1400);
      return () => clearTimeout(timer);
    }
  }, [countdownStep, enteredWorld]);

  const toggleSound = () => {
    if (isMuted) {
      setIsMuted(false);
      setTimeout(() => playCelebrationChime(), 50);
    } else {
      setIsMuted(true);
    }
  };

  const handleCopyCode = () => {
    fetch('/app.py')
      .then(r => r.text())
      .then(text => {
        navigator.clipboard.writeText(text);
        setCopiedCode(true);
        setTimeout(() => setCopiedCode(false), 2500);
      })
      .catch(() => {
        setCopiedCode(true);
        setTimeout(() => setCopiedCode(false), 2500);
      });
  };

  const getThemeParticles = () => {
    if (!enteredWorld) return ['💖', '🌸', '✨', '🎈', '🎀', '💗', '👑'];
    switch (currentPage) {
      case 1:
        return ['💖', '🌸', '🌷', '✨', '💌', '🎀', '🌺'];
      case 2:
        return ['✨', '⭐', '🌟', '🤍', '🌙', '💫', '🕊️'];
      case 3:
        return ['👑', '📸', '✨', '💖', '🌸', '💎', '🌷'];
      case 4:
        return ['🎉', '🎈', '🤣', '💖', '🧁', '⭐', '🎊'];
      case 5:
        return ['💗', '✨', '💌', '🌹', '💞', '🌸', '💐'];
      default:
        return ['💖', '✨', '🌸'];
    }
  };

  return (
    <div className="relative min-h-screen overflow-x-hidden font-outfit text-slate-800 bg-gradient-to-br from-pink-50 via-purple-50 to-rose-50 pb-16 selection:bg-pink-300">
      
      {/* CONTINUOUS LIVE MOVING BACKGROUND EMOJIS (FALLING TOP TO BOTTOM LIKE SNOWFALL ACROSS FULL PAGE) */}
      <div className="fixed inset-0 pointer-events-none z-0 overflow-hidden w-screen h-screen">
        {Array.from({ length: 48 }).map((_, i) => {
          const particles = getThemeParticles();
          const symbol = particles[i % particles.length];
          const leftPos = (i * 2.1) % 98;
          const animDuration = 6.5 + (i % 8) * 1.3;
          const delay = (i * 0.3) % 8;
          const sizeClass = i % 3 === 0 ? 'text-3xl' : i % 2 === 0 ? 'text-2xl' : 'text-xl';
          return (
            <div
              key={i}
              className={`absolute select-none opacity-70 animate-snowfall ${sizeClass}`}
              style={{
                left: `${leftPos}vw`,
                top: '-45px',
                animationDuration: `${animDuration}s`,
                animationDelay: `${delay}s`,
                filter: 'drop-shadow(0 3px 10px rgba(244, 114, 182, 0.45))'
              }}
            >
              {symbol}
            </div>
          );
        })}
      </div>

      {/* FLOATING ACTION TOOLBAR */}
      <div className="fixed top-4 right-4 z-50 flex items-center gap-2">
        <button
          onClick={toggleSound}
          title={isMuted ? "Unmute celebratory chimes" : "Mute audio"}
          className="p-2.5 rounded-full bg-white/85 backdrop-blur-md border border-pink-200 text-pink-700 shadow-md hover:bg-pink-50 hover:scale-105 transition-all"
        >
          {isMuted ? <VolumeX size={18} /> : <Volume2 size={18} className="animate-pulse" />}
        </button>

        <button
          onClick={() => setShowPythonCodeModal(true)}
          title="Inspect updated app.py & requirements.txt"
          className="px-3 py-2 rounded-full bg-white/85 backdrop-blur-md border border-pink-200 text-pink-700 shadow-md hover:bg-pink-50 hover:scale-105 transition-all flex items-center gap-1.5 text-xs font-bold font-comfortaa"
        >
          <Code size={16} />
          <span>Streamlit app.py</span>
        </button>
      </div>

      {/* ========================================================================= */}
      {/* SECTION 1: COUNTDOWN & GRAND OPENING EXPERIENCE */}
      {/* ========================================================================= */}
      {!enteredWorld && (
        <div className="relative z-10 min-h-screen flex items-center justify-center px-4 py-8">
          {countdownStep === 0 && (
            <div className="text-center max-w-lg mx-auto p-8 rounded-3xl glass-panel shadow-2xl animate-fade-in">
              <div className="text-6xl mb-4 animate-float-gentle">👀 💗</div>
              <h1 className="font-greatvibes text-6xl sm:text-7xl text-pink-600 font-bold mb-3 drop-shadow-sm">
                Hey Ruhii!
              </h1>
              <p className="font-comfortaa text-lg sm:text-xl font-bold text-purple-900 mb-2">
                Someone has a very special surprise for you!
              </p>
              <p className="text-sm text-pink-700 italic font-outfit">
                Hold your breath! Starting the magic countdown...
              </p>
            </div>
          )}

          {countdownStep === 1 && (
            <div className="text-center p-8 rounded-3xl glass-panel shadow-2xl">
              <span className="font-comfortaa text-sm font-bold tracking-widest text-purple-600 uppercase">
                Are you ready, Ruhii?
              </span>
              <div className="font-script text-8xl sm:text-9xl font-bold text-pink-600 my-4 animate-pulse-glow">
                3...
              </div>
              <p className="font-comfortaa text-base font-semibold text-purple-900">A little magic is brewing 🌸</p>
            </div>
          )}

          {countdownStep === 2 && (
            <div className="text-center p-8 rounded-3xl glass-panel shadow-2xl">
              <span className="font-comfortaa text-sm font-bold tracking-widest text-purple-600 uppercase">
                Smile please! 😌
              </span>
              <div className="font-script text-8xl sm:text-9xl font-bold text-fuchsia-600 my-4 animate-pulse-glow">
                2...
              </div>
              <p className="font-comfortaa text-base font-semibold text-purple-900">Dhadkanein tez ho rahi hain? 💓</p>
            </div>
          )}

          {countdownStep === 3 && (
            <div className="text-center p-8 rounded-3xl glass-panel shadow-2xl">
              <span className="font-comfortaa text-sm font-bold tracking-widest text-purple-600 uppercase">
                Almost there! 🎉
              </span>
              <div className="font-script text-8xl sm:text-9xl font-bold text-rose-600 my-4 animate-pulse-glow">
                1...
              </div>
              <p className="font-comfortaa text-base font-semibold text-purple-900">Close your eyes & make a wish! 🌟</p>
            </div>
          )}

          {countdownStep === 4 && (
            <div className="text-center max-w-xl mx-auto p-6 sm:p-9 rounded-3xl glass-panel shadow-2xl border-2 border-pink-200 animate-fade-in">
              <div className="flex justify-center gap-3 text-3xl mb-2">
                <span>🎈</span>
                <span>✨</span>
                <span>👑</span>
                <span>💖</span>
                <span>🥳</span>
                <span>🎈</span>
              </div>

              <h1 className="font-script text-4xl sm:text-6xl font-bold bg-gradient-to-r from-pink-600 via-fuchsia-600 to-rose-500 bg-clip-text text-transparent mb-1 drop-shadow-md">
                HAPPY BIRTHDAY RUHII! 🎂
              </h1>

              <div className="font-serif-title italic text-base sm:text-lg text-pink-700 font-semibold mb-4">
                "A Little World Made for Ruhii 💗"
              </div>

              {/* RUHII'S BIRTHDAY PORTRAIT WITH GLOWING PRINCESS FRAME */}
              <div className="relative my-4 flex justify-center">
                <div className="relative group">
                  <div className="absolute -inset-1.5 bg-gradient-to-r from-pink-500 via-purple-500 to-rose-500 rounded-full blur-md opacity-75 group-hover:opacity-100 transition duration-1000 group-hover:duration-200 animate-pulse-glow"></div>
                  <div className="relative w-44 h-44 sm:w-52 sm:h-52 rounded-full overflow-hidden border-4 border-white shadow-2xl bg-pink-100">
                    <img
                      src="/ruhii.jpg"
                      alt="Birthday Girl Ruhii"
                      className="w-full h-full object-cover object-center transform hover:scale-105 transition-transform duration-500"
                    />
                  </div>
                  <div className="absolute -top-3 left-1/2 -translate-x-1/2 bg-white/95 px-3 py-1 rounded-full shadow-md border border-pink-200 text-xs font-comfortaa font-bold text-pink-700 flex items-center gap-1">
                    <span>👑</span>
                    <span>Birthday Princess</span>
                    <span>✨</span>
                  </div>
                </div>
              </div>

              <div className="my-4 p-5 rounded-2xl bg-white/75 border border-pink-100 shadow-inner">
                <div className="flex justify-center items-center gap-2 text-2xl mb-1">
                  <span>🎂</span>
                  <span className="text-sm tracking-widest text-amber-500">🕯️ 🕯️ 🕯️</span>
                  <span>✨</span>
                </div>
                <p className="font-comfortaa text-base sm:text-lg font-bold text-purple-950 leading-relaxed">
                  Made with a little madness, endless duas, and lots of love.
                </p>
                <p className="text-xs text-pink-600 mt-1 font-semibold">
                  Aj ka har lamha sirf aur sirf tumhari muskurahat ke naam hai! ✨
                </p>
              </div>

              <button
                onClick={() => {
                  setEnteredWorld(true);
                  setCurrentPage(1);
                  playCelebrationChime();
                  logEvent("Entered Ruhii's Magical World 🌸");
                }}
                className="w-full py-4 px-6 rounded-full bg-gradient-to-r from-pink-500 via-purple-500 to-rose-500 text-white font-comfortaa font-bold text-lg sm:text-xl shadow-lg hover:shadow-pink-300/50 hover:scale-[1.02] active:scale-95 transition-all"
              >
                Okay Princess, Enter Your World 💗
              </button>
            </div>
          )}
        </div>
      )}

      {/* ========================================================================= */}
      {/* SECTION 2: MAIN EXPERIENCE - CONTENT AT TOP (FIVE SEPARATE PAGES) */}
      {/* ========================================================================= */}
      {enteredWorld && (
        <main className="relative z-10 max-w-2xl mx-auto px-4 pt-6">

          {/* ------------------------------------------------------------------- */}
          {/* PAGE 1: BIRTHDAY WISHES 💌 */}
          {/* ------------------------------------------------------------------- */}
          {currentPage === 1 && (
            <div className="space-y-6 animate-fade-in">
              <div className="text-center">
                <h1 className="font-greatvibes text-5xl sm:text-6xl text-pink-600 font-bold mb-2 drop-shadow-sm leading-tight">
                  A Special Day for a Special Soul 💌
                </h1>
                <p className="font-caveat text-2xl sm:text-3xl font-bold text-purple-800 tracking-wide">
                  "Aj ka din sirf tumhara hai, madam! Toh smile karna compulsory hai. 😌"
                </p>
              </div>

              {/* Main Letter Card */}
              <div className="glass-panel rounded-3xl p-6 sm:p-9 relative overflow-hidden border border-pink-200 shadow-xl">
                <div className="flex justify-center text-3xl mb-3">
                  🌸 💌 💖
                </div>
                <h3 className="font-cormorant italic text-3xl sm:text-4xl font-bold text-pink-900 mb-4 tracking-wide">
                  Dear Ruhii,
                </h3>
                <div className="font-caveat text-2xl sm:text-3xl leading-relaxed text-slate-800 space-y-4">
                  <p>
                    Happy Birthday to one of the most special people in my life. Tumhari friendship meri life ka ek beautiful part hai. I hope tumhari life hamesha happiness, success, laughter aur beautiful memories se filled rahe.
                  </p>
                  <p>
                    Hamesha aise hi smile karti rehna because your smile deserves the whole universe.
                  </p>
                </div>
                <div className="text-right font-greatvibes text-3xl sm:text-4xl font-bold text-pink-700 mt-6">
                  With endless love & blessings, Always 💗
                </div>
              </div>

              {/* Ultra Stylish Bulletin Card */}
              <div className="relative overflow-hidden rounded-3xl p-6 bg-gradient-to-r from-pink-100 via-rose-50 to-pink-100 border-2 border-pink-300 shadow-lg">
                <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-gradient-to-r from-pink-500 to-rose-500 text-white font-comfortaa font-bold text-xs uppercase tracking-wider mb-3 shadow-md">
                  <span>🚨</span>
                  <span>Special Birthday Bulletin</span>
                  <Sparkles size={14} />
                </div>
                <p className="font-outfit text-base sm:text-lg font-semibold text-rose-950 leading-relaxed">
                  "Breaking News: Aaj duniya ki sabse cute aur thori si pagal larki ka birthday hai! 😂 Sources confirm that madam is officially required to smile nonstop all day!"
                </p>
              </div>

              {/* Navigation Action Buttons */}
              <div className="flex gap-3 pt-2">
                <button
                  onClick={() => { setEnteredWorld(false); setCountdownStep(4); }}
                  className="flex-1 py-3 px-4 rounded-full bg-white/80 border border-pink-200 text-pink-800 font-bold text-sm hover:bg-pink-50 flex items-center justify-center gap-1.5 font-comfortaa"
                >
                  <Home size={16} />
                  <span>Home</span>
                </button>
                <button
                  onClick={() => { handlePageSwitch(2); playCelebrationChime(); }}
                  className="flex-[2] py-3 px-5 rounded-full bg-gradient-to-r from-pink-500 to-purple-500 text-white font-comfortaa font-bold text-base shadow-md hover:scale-[1.02] active:scale-95 transition-all flex items-center justify-center gap-2"
                >
                  <span>Next: Unlock Duas 🤲</span>
                  <ChevronRight size={18} />
                </button>
              </div>
            </div>
          )}

          {/* ------------------------------------------------------------------- */}
          {/* PAGE 2: DUAS AND BLESSINGS 🤲 (NO NUMBERING, STYLISH FONT, CUTE EMOJIS) */}
          {/* ------------------------------------------------------------------- */}
          {currentPage === 2 && (
            <div className="space-y-6 animate-fade-in">
              <div className="text-center">
                <h1 className="font-greatvibes text-5xl sm:text-6xl font-bold text-purple-700 mb-2 leading-tight">
                  Prayers From My Heart 🤲
                </h1>
                <p className="font-cormorant italic text-xl sm:text-2xl font-bold text-purple-900 tracking-wide">
                  "Allah tumhari zindagi ko khushiyon aur barkaton se bhar de. Ameen! 🤍"
                </p>
              </div>

              <div className="glass-panel rounded-3xl p-6 sm:p-8 border-purple-200 space-y-3.5 shadow-xl">
                <div className="flex justify-center text-3xl mb-1">
                  ✨ 🌙 🕊️ 🤲 ✨
                </div>

                {DUAS_WITH_EMOJIS.map((duaObj, idx) => (
                  <div
                    key={idx}
                    className="flex items-center justify-between gap-3 p-4 rounded-2xl bg-white/90 border-l-4 border-purple-400 shadow-sm hover:shadow-md hover:translate-x-1.5 transition-all"
                  >
                    <div className="flex items-center gap-3">
                      <span className="text-xl select-none">{duaObj.startEmoji}</span>
                      <p className="font-cormorant text-xl sm:text-2xl font-semibold text-purple-950 leading-snug">
                        {duaObj.text}
                      </p>
                    </div>
                    <span className="text-lg select-none pl-2">{duaObj.endEmoji}</span>
                  </div>
                ))}

                <div className="text-center pt-4">
                  <div className="font-greatvibes text-4xl sm:text-5xl font-bold text-purple-800">
                    Ameen Sum Ameen! 🤲 🤍
                  </div>
                  <p className="font-comfortaa text-xs sm:text-sm text-purple-600 mt-1 font-semibold">
                    May every single angel whisper Ameen to these prayers for you!
                  </p>
                </div>
              </div>

              {/* Navigation Action Buttons (Advances to new Gallery page!) */}
              <div className="flex gap-3 pt-2">
                <button
                  onClick={() => handlePageSwitch(1)}
                  className="flex-1 py-3 px-4 rounded-full bg-white/80 border border-purple-200 text-purple-800 font-bold text-sm hover:bg-purple-50 flex items-center justify-center gap-1 font-comfortaa"
                >
                  <ChevronLeft size={16} />
                  <span>Previous</span>
                </button>
                <button
                  onClick={() => { handlePageSwitch(3); playCelebrationChime(); }}
                  className="flex-[2] py-3 px-5 rounded-full bg-gradient-to-r from-purple-500 to-pink-500 text-white font-comfortaa font-bold text-base shadow-md hover:scale-[1.02] active:scale-95 transition-all flex items-center justify-center gap-2"
                >
                  <span>Ruhii's Royal Gallery 📸 👑</span>
                  <ChevronRight size={18} />
                </button>
              </div>
            </div>
          )}

          {/* ------------------------------------------------------------------- */}
          {/* NEW PAGE 3: RUHII'S ROYAL PHOTO GALLERY 📸 👑 */}
          {/* ------------------------------------------------------------------- */}
          {currentPage === 3 && (
            <div className="space-y-6 animate-fade-in">
              <div className="text-center">
                <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-gradient-to-r from-pink-500 to-purple-600 text-white font-comfortaa text-xs font-bold uppercase tracking-wider mb-2 shadow-md">
                  <Camera size={14} />
                  <span>The Queen's Visual Diary</span>
                  <Sparkles size={14} />
                </div>
                <h1 className="font-greatvibes text-5xl sm:text-6xl font-bold text-pink-600 mb-2 leading-tight">
                  Ruhii's Royal Moments 👑
                </h1>
                <p className="font-cormorant italic text-xl sm:text-2xl font-bold text-purple-900 tracking-wide">
                  "Har photo mein ek alag hi noor aur masoomiyat hai! MashAllah 🤍"
                </p>
              </div>

              {/* 4 Photo Cards Grid */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-5">
                {RUHII_GALLERY.map((item, idx) => (
                  <div
                    key={idx}
                    className="glass-panel rounded-3xl p-4 border-2 border-pink-200 hover:border-pink-400 shadow-xl transition-all duration-300 hover:-translate-y-1.5 flex flex-col justify-between"
                  >
                    <div className="relative rounded-2xl overflow-hidden shadow-md bg-pink-100 aspect-[3/4] mb-3 group">
                      <img
                        src={item.src}
                        alt={item.title}
                        className="w-full h-full object-cover object-center group-hover:scale-105 transition-transform duration-500"
                      />
                      <div className="absolute inset-0 bg-gradient-to-t from-black/50 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity flex items-end p-3">
                        <span className="text-white text-xs font-comfortaa font-bold">
                          Ruhii • Birthday Queen 💖
                        </span>
                      </div>
                    </div>
                    <div className="text-center px-2 pb-1">
                      <h4 className="font-comfortaa font-bold text-pink-800 text-base mb-1">
                        {item.title}
                      </h4>
                      <p className="font-outfit text-xs sm:text-sm text-slate-700 font-medium leading-relaxed">
                        {item.tagline}
                      </p>
                    </div>
                  </div>
                ))}
              </div>

              {/* Navigation Action Buttons */}
              <div className="flex gap-3 pt-2">
                <button
                  onClick={() => handlePageSwitch(2)}
                  className="flex-1 py-3 px-4 rounded-full bg-white/80 border border-pink-200 text-pink-800 font-bold text-sm hover:bg-pink-50 flex items-center justify-center gap-1 font-comfortaa"
                >
                  <ChevronLeft size={16} />
                  <span>Previous (Duas)</span>
                </button>
                <button
                  onClick={() => { handlePageSwitch(4); playCelebrationChime(); }}
                  className="flex-[2] py-3 px-5 rounded-full bg-gradient-to-r from-amber-500 via-rose-500 to-pink-500 text-white font-comfortaa font-bold text-base shadow-md hover:scale-[1.02] active:scale-95 transition-all flex items-center justify-center gap-2"
                >
                  <span>Chalo Ab Thori Masti Ho Jaye 😂</span>
                  <ChevronRight size={18} />
                </button>
              </div>
            </div>
          )}

          {/* ------------------------------------------------------------------- */}
          {/* PAGE 4: FUNNY AND CUTE SECTION 😂 (DECENT, ELEGANT FONTS, NO POINTING HANDS) */}
          {/* ------------------------------------------------------------------- */}
          {currentPage === 4 && (
            <div className="space-y-6 animate-fade-in">
              <div className="text-center">
                <h1 className="font-greatvibes text-5xl sm:text-6xl font-bold text-amber-700 mb-2 leading-tight">
                  Ruhii Ki Pagalpanti Department 😂
                </h1>
                <p className="font-comfortaa text-sm sm:text-base font-bold text-rose-800">
                  "Warning: Is page ko dekh kar hansna mana nahi hai! 🤣"
                </p>
              </div>

              {/* Decent, clean and elegant Pagalpanti truths without pointing hands */}
              <div className="glass-panel rounded-3xl p-6 sm:p-7 border-amber-200 space-y-3.5 shadow-xl">
                <div className="flex justify-center text-3xl mb-1">
                  🤪 🍰 🍟 🎭 👑
                </div>
                <h3 className="text-center font-comfortaa font-bold text-amber-900 text-sm tracking-wider uppercase mb-3">
                  Official Birthday Truths 📢
                </h3>

                <div className="p-4 rounded-2xl bg-gradient-to-r from-amber-50 to-orange-50/80 border border-amber-200/80 shadow-sm flex items-center gap-3.5 hover:shadow-md transition-all">
                  <span className="text-2xl select-none">🏆</span>
                  <p className="font-outfit text-base font-medium text-slate-800 leading-relaxed">
                    Congratulations! Tum officially ek saal aur experienced ho gayi ho... lekin harkatein abhi bhi bachon wali hain. 😂
                  </p>
                </div>

                <div className="p-4 rounded-2xl bg-gradient-to-r from-amber-50 to-orange-50/80 border border-amber-200/80 shadow-sm flex items-center gap-3.5 hover:shadow-md transition-all">
                  <span className="text-2xl select-none">🎂</span>
                  <p className="font-outfit text-base font-medium text-slate-800 leading-relaxed">
                    Cake tumhara hai, lekin khaane ka haq mera bhi banta hai.
                  </p>
                </div>

                <div className="p-4 rounded-2xl bg-gradient-to-r from-amber-50 to-orange-50/80 border border-amber-200/80 shadow-sm flex items-center gap-3.5 hover:shadow-md transition-all">
                  <span className="text-2xl select-none">⏳</span>
                  <p className="font-outfit text-base font-medium text-slate-800 leading-relaxed">
                    Tumhari age increase ho rahi hai, maturity abhi bhi loading hai... 2%. 🤣
                  </p>
                </div>

                <div className="p-4 rounded-2xl bg-gradient-to-r from-amber-50 to-orange-50/80 border border-amber-200/80 shadow-sm flex items-center gap-3.5 hover:shadow-md transition-all">
                  <span className="text-2xl select-none">✨</span>
                  <p className="font-outfit text-base font-medium text-slate-800 leading-relaxed">
                    Aaj tumhari har wish poori ho, bas mujhe tang karne wali wishes exclude hain.
                  </p>
                </div>
              </div>

              {/* Interactive Compliment Generator */}
              <div className="glass-panel rounded-3xl p-6 text-center border-rose-200 shadow-xl">
                <div className="text-2xl mb-1">🎁 💝 👑</div>
                <h3 className="font-comfortaa font-bold text-rose-800 text-lg mb-1">
                  Reveal My Birthday Compliment
                </h3>
                <p className="font-outfit text-sm text-rose-600 mb-4 font-medium">
                  Click below to generate a cute & funny verified truth about Ruhii!
                </p>

                <button
                  onClick={() => {
                    const randomComp = COMPLIMENTS[Math.floor(Math.random() * COMPLIMENTS.length)];
                    setCompliment(randomComp);
                    playTuneNote(659.25, 0.3);
                    logEvent(`Revealed Compliment: "${randomComp.slice(0, 32)}..."`);
                  }}
                  className="py-3 px-6 rounded-full bg-gradient-to-r from-rose-500 to-pink-500 text-white font-comfortaa font-bold text-sm shadow-md hover:scale-105 active:scale-95 transition-all"
                >
                  Reveal My Birthday Compliment 💝
                </button>

                {compliment && (
                  <div className="mt-4 p-4 rounded-2xl bg-rose-50 border-2 border-rose-300 font-outfit text-rose-950 font-semibold text-base sm:text-lg animate-pulse-glow shadow-sm">
                    "{compliment}"
                  </div>
                )}
              </div>

              {/* Navigation Action Buttons */}
              <div className="flex gap-3 pt-2">
                <button
                  onClick={() => handlePageSwitch(3)}
                  className="flex-1 py-3 px-4 rounded-full bg-white/80 border border-amber-200 text-amber-900 font-bold text-sm hover:bg-amber-50 flex items-center justify-center gap-1 font-comfortaa"
                >
                  <ChevronLeft size={16} />
                  <span>Previous</span>
                </button>
                <button
                  onClick={() => { handlePageSwitch(5); playCelebrationChime(); }}
                  className="flex-[2] py-3 px-5 rounded-full bg-gradient-to-r from-amber-500 via-rose-500 to-pink-500 text-white font-comfortaa font-bold text-base shadow-md hover:scale-[1.02] active:scale-95 transition-all flex items-center justify-center gap-2"
                >
                  <span>Ab Last Surprise Dekho ❤️</span>
                  <ChevronRight size={18} />
                </button>
              </div>
            </div>
          )}

          {/* ------------------------------------------------------------------- */}
          {/* PAGE 5: SPECIAL MESSAGE ❤️ (COOL STYLISH LETTER FONT & SECRET HEART) */}
          {/* ------------------------------------------------------------------- */}
          {currentPage === 5 && (
            <div className="space-y-6 animate-fade-in">
              <div className="text-center">
                <h1 className="font-greatvibes text-5xl sm:text-6xl font-bold text-rose-600 mb-2 leading-tight">
                  One Last Thing, Ruhii... ❤️
                </h1>
                <p className="font-cormorant italic text-xl sm:text-2xl font-bold text-pink-900 tracking-wide">
                  "Kuch baatein hoti hain jo words mein explain karna mushkil hota hai."
                </p>
              </div>

              {/* Emotional Letter */}
              <div className="glass-panel rounded-3xl p-6 sm:p-9 border-rose-200 relative shadow-xl">
                <div className="flex justify-center my-2">
                  <div className="text-6xl animate-pulse-glow">💖</div>
                </div>

                <div className="font-caveat text-2xl sm:text-3xl leading-relaxed text-slate-800 space-y-4 my-5">
                  <p>
                    Ruhii, I just want you to know that you are genuinely special. Life mein bohat se log milte hain, lekin kuch log apni presence se har moment ko beautiful bana dete hain. Tum unhi logon mein se ho. May your smile never fade, may your dreams come true, and may happiness always find its way to you.
                  </p>
                  <p className="font-bold text-purple-950">
                    Thank you for being you. Stay blessed, stay crazy, and never stop smiling.
                  </p>
                </div>

                <div className="mt-6 p-4 rounded-2xl bg-gradient-to-r from-pink-100 to-rose-100 text-center border border-pink-200">
                  <div className="font-cormorant text-2xl sm:text-3xl font-bold text-rose-700 tracking-wide">
                    YOU DESERVE ALL THE HAPPINESS IN THE WORLD! 💗
                  </div>
                </div>
              </div>

              {/* One More Hug Feature */}
              <div className="text-center">
                <button
                  onClick={() => {
                    setShowHug(true);
                    playCelebrationChime();
                    logEvent("Clicked 'One More Hug' 🤗");
                  }}
                  className="w-full max-w-sm py-3.5 px-6 rounded-full bg-gradient-to-r from-pink-500 via-rose-500 to-fuchsia-500 text-white font-comfortaa font-bold text-lg shadow-lg hover:scale-105 active:scale-95 transition-all inline-flex items-center justify-center gap-2"
                >
                  <span>One More Hug? 🤗</span>
                </button>
              </div>

              {/* Hug Overlay Celebration */}
              {showHug && (
                <div className="p-6 rounded-3xl glass-panel border-2 border-pink-300 text-center animate-fade-in bg-pink-100/90 shadow-2xl">
                  <div className="text-6xl mb-2 animate-bounce">🤗 💗 🫂</div>
                  <div className="font-greatvibes text-4xl sm:text-5xl font-bold text-rose-600 mb-2">
                    SENDING YOU INFINITE HUGS & LOVE! 💗
                  </div>
                  <p className="font-comfortaa text-sm sm:text-base font-bold text-purple-950">
                    May your whole year ahead be as soft, warm, and comforting as the biggest hug!
                  </p>
                </div>
              )}

              {/* Navigation Action Buttons */}
              <div className="flex gap-3 pt-2">
                <button
                  onClick={() => handlePageSwitch(4)}
                  className="flex-1 py-3 px-4 rounded-full bg-white/80 border border-rose-200 text-rose-800 font-bold text-sm hover:bg-rose-50 flex items-center justify-center gap-1 font-comfortaa"
                >
                  <ChevronLeft size={16} />
                  <span>Previous</span>
                </button>
                <button
                  onClick={() => { handlePageSwitch(1); playCelebrationChime(); }}
                  className="flex-[2] py-3 px-5 rounded-full bg-gradient-to-r from-pink-500 to-rose-500 text-white font-comfortaa font-bold text-base shadow-md hover:scale-[1.02] active:scale-95 transition-all flex items-center justify-center gap-2"
                >
                  <span>Open My Little Letter 💌</span>
                  <ChevronRight size={18} />
                </button>
              </div>

              {/* Dedication: "Made with Love for MY Dear Bestiee ❤️" */}
              <footer className="text-center pt-8 pb-4">
                <p className="font-greatvibes text-3xl sm:text-4xl text-pink-600 font-bold tracking-wide">
                  Made with Love for MY Dear Bestiee ❤️
                </p>
                <p className="text-pink-400 mt-1 font-comfortaa text-xs">
                  A Little World Made for Ruhii 💗 • Happy Birthday!
                </p>

                {/* DISCRETE HEART BUTTON FOR SECRET BESTIE ACTIVITY PAGE */}
                <div className="flex justify-center mt-3">
                  <button
                    onClick={() => {
                      setShowSecretModal(true);
                      logEvent("Secret Heart Clicked 🔒");
                    }}
                    title="A little secret"
                    className="p-2 rounded-full text-pink-300 hover:text-pink-600 hover:scale-125 transition-all opacity-40 hover:opacity-100"
                  >
                    <Heart size={18} className="fill-current" />
                  </button>
                </div>
              </footer>
            </div>
          )}
        </main>
      )}

      {/* ========================================================================= */}
      {/* SECRET MODAL / PAGE: PASSWORD PROTECTED RUHII ACTIVITY HISTORY TRACKER */}
      {/* ========================================================================= */}
      {showSecretModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-md animate-fade-in">
          <div className="bg-white rounded-3xl max-w-lg w-full p-6 sm:p-7 shadow-2xl border-2 border-purple-200 flex flex-col max-h-[85vh]">
            <div className="flex items-center justify-between pb-3 border-b border-purple-100">
              <div className="flex items-center gap-2 text-purple-900 font-bold font-comfortaa">
                <Lock size={18} className="text-purple-600" />
                <span>Ruhii's Secret Journey Log</span>
              </div>
              <button
                onClick={() => { setShowSecretModal(false); setPasswordError(''); }}
                className="w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-600 flex items-center justify-center font-bold text-sm"
              >
                ✕
              </button>
            </div>

            {!secretUnlocked ? (
              <div className="py-6 text-center">
                <div className="text-5xl mb-3">🔐 ✨ 💖</div>
                <h4 className="font-comfortaa font-bold text-purple-950 text-lg mb-2">
                  Bestie Access Passcode
                </h4>
                <p className="font-outfit text-sm text-purple-700 mb-5">
                  Enter password to see the real-time record of which pages Ruhii opened and how long she spent on each surprise!
                </p>

                <div className="max-w-xs mx-auto space-y-3">
                  <input
                    type="password"
                    placeholder="Enter passcode (default: bestie)"
                    value={passwordInput}
                    onChange={(e) => setPasswordInput(e.target.value)}
                    onKeyDown={(e) => {
                      if (e.key === 'Enter') {
                        if (['bestie', 'ruhii', 'ruhii123', 'love'].includes(passwordInput.trim().toLowerCase())) {
                          setSecretUnlocked(true);
                          setPasswordError('');
                        } else {
                          setPasswordError('Incorrect passcode! Only bestie knows.');
                        }
                      }
                    }}
                    className="w-full px-4 py-2.5 rounded-xl border border-purple-200 text-center font-comfortaa text-sm focus:outline-none focus:ring-2 focus:ring-purple-400"
                  />
                  {passwordError && (
                    <p className="text-xs text-rose-500 font-semibold">{passwordError}</p>
                  )}
                  <button
                    onClick={() => {
                      if (['bestie', 'ruhii', 'ruhii123', 'love'].includes(passwordInput.trim().toLowerCase())) {
                        setSecretUnlocked(true);
                        setPasswordError('');
                      } else {
                        setPasswordError('Incorrect passcode! Only bestie knows.');
                      }
                    }}
                    className="w-full py-2.5 rounded-xl bg-gradient-to-r from-purple-500 to-pink-500 text-white font-comfortaa font-bold text-sm shadow hover:scale-105 transition-all"
                  >
                    Unlock History 🔓
                  </button>
                </div>
              </div>
            ) : (
              <div className="py-4 flex flex-col flex-1 overflow-hidden">
                <div className="flex items-center justify-between mb-3 text-xs font-bold text-purple-800">
                  <span className="flex items-center gap-1.5">
                    <Clock size={14} />
                    <span>Real-Time Visitor Journey Timeline</span>
                  </span>
                  <span className="bg-purple-100 text-purple-700 px-2.5 py-0.5 rounded-full">
                    Live Recording
                  </span>
                </div>

                <div className="overflow-y-auto space-y-2.5 pr-1 flex-1 max-h-[50vh]">
                  {activityLog.map((item, idx) => (
                    <div
                      key={idx}
                      className="p-3 rounded-2xl bg-purple-50/80 border border-purple-100 flex items-center justify-between text-xs"
                    >
                      <span className="font-outfit font-semibold text-purple-950">
                        {item.event}
                      </span>
                      <span className="font-mono text-[11px] font-bold text-purple-600 bg-white px-2 py-0.5 rounded-md shadow-xs ml-2 shrink-0">
                        {item.time}
                      </span>
                    </div>
                  ))}
                </div>

                <div className="pt-4 border-t border-purple-100 flex items-center justify-between">
                  <button
                    onClick={() => {
                      setActivityLog([{ time: new Date().toLocaleTimeString(), event: "Log refreshed" }]);
                    }}
                    className="text-xs text-slate-500 hover:text-slate-800 flex items-center gap-1 font-semibold"
                  >
                    <Trash2 size={13} />
                    <span>Clear Log</span>
                  </button>
                  <button
                    onClick={() => setShowSecretModal(false)}
                    className="px-4 py-2 rounded-xl bg-purple-600 hover:bg-purple-700 text-white font-bold text-xs font-comfortaa transition-all"
                  >
                    Close Log
                  </button>
                </div>
              </div>
            )}
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* MODAL: VIEW / COPY STREAMLIT app.py & requirements.txt */}
      {/* ========================================================================= */}
      {showPythonCodeModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm animate-fade-in">
          <div className="bg-white rounded-3xl max-w-2xl w-full p-6 shadow-2xl max-h-[85vh] flex flex-col border border-pink-200">
            <div className="flex items-center justify-between pb-4 border-b border-pink-100">
              <div>
                <h3 className="font-bold text-lg text-slate-800 flex items-center gap-2">
                  <Code className="text-pink-600" size={20} />
                  <span>Python Streamlit File: <code>app.py</code></span>
                </h3>
                <p className="text-xs text-slate-500 mt-0.5">
                  Updated with Ruhii's photo gallery page and top-to-bottom falling emoji snowfall animation
                </p>
              </div>
              <button
                onClick={() => setShowPythonCodeModal(false)}
                className="w-8 h-8 rounded-full bg-slate-100 hover:bg-slate-200 text-slate-600 flex items-center justify-center font-bold text-sm"
              >
                ✕
              </button>
            </div>

            <div className="my-4 overflow-y-auto p-4 rounded-xl bg-slate-900 text-slate-100 text-xs font-mono leading-relaxed space-y-4">
              <div>
                <span className="text-emerald-400"># requirements.txt</span>
                <pre className="mt-1 text-slate-300">streamlit&gt;=1.35.0</pre>
              </div>
              <div>
                <span className="text-emerald-400"># app.py</span>
                <pre className="mt-1 text-slate-300">
                  {`The file /app.py has been updated with:
- Dedicated "Ruhii's Royal Moments" gallery page right after Duas
- All 4 new portrait photos with aesthetic borders and sweet bestie captions
- Live falling emoji animation cascading top to bottom like magical snowfall across the complete page
- Sound voice removed, sweet celebratory chimes and bells retained
- Secret passcode-protected page tracking every page open time & action
- Footer dedication: "Made with Love for MY Dear Bestiee ❤️"`}
                </pre>
              </div>
            </div>

            <div className="flex items-center justify-end gap-3 pt-3 border-t border-pink-100">
              <button
                onClick={handleCopyCode}
                className="px-4 py-2 rounded-xl bg-pink-500 hover:bg-pink-600 text-white font-bold text-xs flex items-center gap-1.5 transition-all"
              >
                {copiedCode ? <Check size={16} /> : <Copy size={16} />}
                <span>{copiedCode ? 'Copied to Clipboard!' : 'Copy app.py Content'}</span>
              </button>
              <button
                onClick={() => setShowPythonCodeModal(false)}
                className="px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 font-bold text-xs"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
