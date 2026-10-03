"""
Generates clean, professional SVG illustrations for all crops and vegetables in KisanSetu.
"""

import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "frontend", "static", "images", "crops")
os.makedirs(OUTPUT_DIR, exist_ok=True)

CROPS_SVG = {
    "tomato.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="tGrad" cx="38%" cy="32%" r="65%">
      <stop offset="0%" stop-color="#ff6b6b"/>
      <stop offset="60%" stop-color="#e53935"/>
      <stop offset="100%" stop-color="#b71c1c"/>
    </radialGradient>
    <linearGradient id="tStem" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#81c784"/>
      <stop offset="100%" stop-color="#2e7d32"/>
    </linearGradient>
  </defs>
  <ellipse cx="60" cy="68" rx="46" ry="42" fill="url(#tGrad)"/>
  <ellipse cx="46" cy="52" rx="14" ry="7" fill="#ffffff" opacity="0.3" transform="rotate(-25 46 52)"/>
  <!-- Sepals & Stem -->
  <path d="M60,32 C60,18 64,12 68,10 C69,15 65,22 62,32 Z" fill="url(#tStem)"/>
  <path d="M60,32 L46,24 C52,28 56,32 60,32 Z" fill="url(#tStem)"/>
  <path d="M60,32 L74,24 C68,28 64,32 60,32 Z" fill="url(#tStem)"/>
  <path d="M60,32 L40,36 C48,36 55,34 60,32 Z" fill="url(#tStem)"/>
  <path d="M60,32 L80,36 C72,36 65,34 60,32 Z" fill="url(#tStem)"/>
  <circle cx="60" cy="32" r="4.5" fill="#2e7d32"/>
</svg>''',

    "onion.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="oGrad" cx="42%" cy="45%" r="60%">
      <stop offset="0%" stop-color="#d87093"/>
      <stop offset="60%" stop-color="#9c27b0"/>
      <stop offset="100%" stop-color="#581845"/>
    </radialGradient>
  </defs>
  <!-- Roots -->
  <path d="M54,102 Q50,114 46,116 M60,102 Q60,116 60,118 M66,102 Q70,114 74,116" stroke="#c49a7a" stroke-width="2.5" stroke-linecap="round" fill="none"/>
  <!-- Bulb -->
  <path d="M60,20 C82,38 98,62 98,78 C98,94 81,104 60,104 C39,104 22,94 22,78 C22,62 38,38 60,20 Z" fill="url(#oGrad)"/>
  <!-- Onion lines -->
  <path d="M60,20 C74,42 84,65 84,80 C84,95 72,102 60,103" stroke="#e090b8" stroke-width="1.8" fill="none" opacity="0.6"/>
  <path d="M60,20 C46,42 36,65 36,80 C36,95 48,102 60,103" stroke="#e090b8" stroke-width="1.8" fill="none" opacity="0.6"/>
  <path d="M60,20 C66,42 70,68 70,82 C70,96 66,102 60,103" stroke="#e090b8" stroke-width="1.5" fill="none" opacity="0.6"/>
  <path d="M60,20 C54,42 50,68 50,82 C50,96 54,102 60,103" stroke="#e090b8" stroke-width="1.5" fill="none" opacity="0.6"/>
  <!-- Sprout stem -->
  <path d="M58,22 Q54,12 48,8 Q58,14 60,22 Z" fill="#66bb6a"/>
  <path d="M60,22 Q64,10 70,6 Q64,12 62,22 Z" fill="#4caf50"/>
</svg>''',

    "potato.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="pGrad" cx="38%" cy="38%" r="62%">
      <stop offset="0%" stop-color="#dfb887"/>
      <stop offset="65%" stop-color="#b8864b"/>
      <stop offset="100%" stop-color="#805626"/>
    </radialGradient>
  </defs>
  <!-- Irregular organic potato shape -->
  <path d="M30,45 C24,62 26,82 42,95 C58,108 88,104 100,86 C112,68 106,44 90,32 C74,20 42,24 30,45 Z" fill="url(#pGrad)"/>
  <!-- Potato eyes -->
  <ellipse cx="44" cy="48" rx="4" ry="2" fill="#6d461b" transform="rotate(-15 44 48)"/>
  <ellipse cx="68" cy="40" rx="5" ry="2" fill="#6d461b" transform="rotate(10 68 40)"/>
  <ellipse cx="86" cy="62" rx="4" ry="2" fill="#6d461b" transform="rotate(-20 86 62)"/>
  <ellipse cx="50" cy="78" rx="5" ry="2.5" fill="#6d461b" transform="rotate(15 50 78)"/>
  <ellipse cx="78" cy="84" rx="4" ry="2" fill="#6d461b" transform="rotate(-10 78 84)"/>
  <!-- Soft highlight -->
  <ellipse cx="56" cy="46" rx="16" ry="9" fill="#ffffff" opacity="0.25" transform="rotate(-12 56 46)"/>
</svg>''',

    "paddy.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <linearGradient id="pStem" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#81c784"/>
      <stop offset="100%" stop-color="#388e3c"/>
    </linearGradient>
    <linearGradient id="pGrain" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fff59d"/>
      <stop offset="60%" stop-color="#fbc02d"/>
      <stop offset="100%" stop-color="#f57f17"/>
    </linearGradient>
  </defs>
  <!-- Stalk -->
  <path d="M40,110 Q50,70 60,35 Q66,15 78,12" stroke="url(#pStem)" stroke-width="4" stroke-linecap="round" fill="none"/>
  <!-- Grains on stalk -->
  <ellipse cx="74" cy="18" rx="7" ry="3.5" fill="url(#pGrain)" transform="rotate(-30 74 18)"/>
  <ellipse cx="82" cy="24" rx="7" ry="3.5" fill="url(#pGrain)" transform="rotate(-20 82 24)"/>
  <ellipse cx="68" cy="28" rx="7" ry="3.5" fill="url(#pGrain)" transform="rotate(35 68 28)"/>
  <ellipse cx="76" cy="36" rx="7" ry="3.5" fill="url(#pGrain)" transform="rotate(-15 76 36)"/>
  <ellipse cx="62" cy="40" rx="7" ry="3.5" fill="url(#pGrain)" transform="rotate(40 62 40)"/>
  <ellipse cx="70" cy="48" rx="7" ry="3.5" fill="url(#pGrain)" transform="rotate(-20 70 48)"/>
  <ellipse cx="55" cy="54" rx="7" ry="3.5" fill="url(#pGrain)" transform="rotate(45 55 54)"/>
  <ellipse cx="63" cy="62" rx="7" ry="3.5" fill="url(#pGrain)" transform="rotate(-15 63 62)"/>
  <ellipse cx="48" cy="68" rx="7" ry="3.5" fill="url(#pGrain)" transform="rotate(50 48 68)"/>
  <ellipse cx="56" cy="76" rx="7" ry="3.5" fill="url(#pGrain)" transform="rotate(-20 56 76)"/>
  <!-- Leaves -->
  <path d="M48,85 Q25,75 14,88 Q30,82 45,95 Z" fill="#66bb6a"/>
  <path d="M42,98 Q70,95 86,108 Q65,102 40,105 Z" fill="#4caf50"/>
</svg>''',

    "maize.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="mKernels" cx="30%" cy="30%" r="70%">
      <stop offset="0%" stop-color="#fff59d"/>
      <stop offset="50%" stop-color="#fbc02d"/>
      <stop offset="100%" stop-color="#f57f17"/>
    </radialGradient>
    <linearGradient id="mHusk" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#a5d6a7"/>
      <stop offset="100%" stop-color="#388e3c"/>
    </linearGradient>
  </defs>
  <!-- Ear cob -->
  <ellipse cx="60" cy="52" rx="20" ry="42" fill="url(#mKernels)"/>
  <!-- Kernel grid lines -->
  <path d="M48,22 Q60,24 72,22 M44,32 Q60,35 76,32 M42,44 Q60,47 78,44 M41,56 Q60,59 79,56 M43,68 Q60,71 77,68 M47,80 Q60,82 73,80" stroke="#f57f17" stroke-width="1.5" fill="none" opacity="0.6"/>
  <path d="M52,18 Q50,55 52,90 M60,14 Q60,55 60,94 M68,18 Q70,55 68,90" stroke="#f57f17" stroke-width="1.5" fill="none" opacity="0.6"/>
  <!-- Husk Leaves -->
  <path d="M38,98 C30,75 32,45 44,28 C34,48 36,80 48,102 Z" fill="url(#mHusk)"/>
  <path d="M82,98 C90,75 88,45 76,28 C86,48 84,80 72,102 Z" fill="url(#mHusk)"/>
  <path d="M60,94 C56,104 54,114 52,118 C58,118 64,116 66,114 C64,108 62,100 60,94 Z" fill="#2e7d32"/>
</svg>''',

    "chilli.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <linearGradient id="chilliGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff5252"/>
      <stop offset="60%" stop-color="#d32f2f"/>
      <stop offset="100%" stop-color="#b71c1c"/>
    </linearGradient>
  </defs>
  <!-- Curving Chilli body -->
  <path d="M48,25 C62,28 76,42 78,64 C80,82 70,98 50,108 C40,112 34,110 38,106 C52,94 62,80 60,64 C58,48 48,36 36,32 Z" fill="url(#chilliGrad)"/>
  <!-- Stem & Cap -->
  <path d="M34,28 C42,32 50,30 52,24 C50,22 44,20 38,22 Z" fill="#388e3c"/>
  <path d="M44,22 C42,14 44,8 50,4 C46,8 44,14 44,22 Z" stroke="#2e7d32" stroke-width="3" stroke-linecap="round" fill="none"/>
  <!-- Highlight -->
  <path d="M52,40 C60,50 64,64 62,78" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" fill="none" opacity="0.4"/>
</svg>''',

    "banana.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <linearGradient id="bGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffee58"/>
      <stop offset="60%" stop-color="#fdd835"/>
      <stop offset="100%" stop-color="#f57f17"/>
    </linearGradient>
  </defs>
  <!-- Crescent shape -->
  <path d="M22,30 C38,18 78,20 98,54 C106,70 102,92 84,102 C82,103 80,101 82,98 C94,82 92,62 78,44 C62,26 32,26 22,30 Z" fill="url(#bGrad)"/>
  <!-- Inner ridge -->
  <path d="M26,30 C44,26 72,34 84,54 C92,68 88,86 82,98" stroke="#fbc02d" stroke-width="2" fill="none"/>
  <!-- Crown stem -->
  <path d="M22,30 C16,28 14,24 16,18 C19,22 22,26 25,28 Z" fill="#558b2f"/>
  <!-- Tip -->
  <circle cx="82" cy="100" r="3" fill="#6d4c41"/>
</svg>''',

    "brinjal.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="brinGrad" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#7b1fa2"/>
      <stop offset="60%" stop-color="#4a148c"/>
      <stop offset="100%" stop-color="#1f093d"/>
    </radialGradient>
  </defs>
  <!-- Pear body -->
  <path d="M60,34 C74,34 82,45 88,65 C94,85 86,104 60,104 C34,104 26,85 32,65 C38,45 46,34 60,34 Z" fill="url(#brinGrad)"/>
  <!-- Calyx -->
  <path d="M60,36 L50,48 L56,42 L42,42 L52,38 L48,26 L60,34 L72,26 L68,38 L78,42 L64,42 L70,48 Z" fill="#388e3c"/>
  <!-- Stem -->
  <path d="M60,32 C58,18 64,12 70,8 C68,14 64,22 62,32 Z" fill="#2e7d32"/>
  <!-- Specular shine -->
  <ellipse cx="48" cy="62" rx="8" ry="16" fill="#ffffff" opacity="0.25" transform="rotate(-15 48 62)"/>
</svg>''',

    "carrot.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <linearGradient id="cGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ff9800"/>
      <stop offset="60%" stop-color="#f57c00"/>
      <stop offset="100%" stop-color="#e65100"/>
    </linearGradient>
  </defs>
  <!-- Carrot root -->
  <path d="M46,34 C58,32 72,34 76,38 C74,58 64,88 56,112 C54,112 50,88 44,58 C42,46 42,36 46,34 Z" fill="url(#cGrad)"/>
  <!-- Texture ridges -->
  <path d="M48,46 Q58,48 68,47 M46,60 Q56,62 64,61 M50,74 Q56,76 62,75 M52,88 Q55,90 58,89" stroke="#bf360c" stroke-width="1.5" stroke-linecap="round" fill="none" opacity="0.5"/>
  <!-- Foliage -->
  <path d="M60,34 Q55,18 42,10 Q54,16 58,32 Z" fill="#4caf50"/>
  <path d="M60,34 Q62,14 62,6 Q66,16 63,32 Z" fill="#66bb6a"/>
  <path d="M60,34 Q70,18 80,10 Q72,18 64,32 Z" fill="#4caf50"/>
</svg>''',

    "cabbage.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="cabGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#c8e6c9"/>
      <stop offset="60%" stop-color="#81c784"/>
      <stop offset="100%" stop-color="#388e3c"/>
    </radialGradient>
  </defs>
  <!-- Outer leaves -->
  <circle cx="60" cy="62" r="42" fill="url(#cabGrad)"/>
  <path d="M22,55 C20,35 45,26 60,36 C42,32 26,42 22,55 Z" fill="#2e7d32" opacity="0.6"/>
  <path d="M98,55 C100,35 75,26 60,36 C78,32 94,42 98,55 Z" fill="#2e7d32" opacity="0.6"/>
  <path d="M30,85 C22,70 38,55 52,65 C38,62 26,72 30,85 Z" fill="#2e7d32" opacity="0.5"/>
  <path d="M90,85 C98,70 82,55 68,65 C82,62 94,72 90,85 Z" fill="#2e7d32" opacity="0.5"/>
  <!-- Leaf veins -->
  <path d="M60,62 Q45,50 35,46 M60,62 Q75,50 85,46 M60,62 Q52,78 46,88 M60,62 Q68,78 74,88" stroke="#e8f5e9" stroke-width="2.5" stroke-linecap="round" fill="none"/>
</svg>''',

    "groundnut.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="gnGrad" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#d7ccc8"/>
      <stop offset="50%" stop-color="#bcaaa4"/>
      <stop offset="100%" stop-color="#8d6e63"/>
    </radialGradient>
  </defs>
  <!-- Peanut shell shape -->
  <path d="M32,48 C24,62 30,78 44,82 C52,84 56,76 62,76 C68,76 72,84 82,82 C94,78 100,60 92,48 C84,36 74,40 68,44 C62,46 58,40 50,38 C38,36 34,42 32,48 Z" fill="url(#gnGrad)"/>
  <!-- Reticulated pattern lines -->
  <path d="M38,48 Q60,42 86,48 M36,62 Q60,56 88,62 M42,75 Q62,70 82,75" stroke="#6d4c41" stroke-width="1.2" stroke-dasharray="3,3" fill="none"/>
</svg>''',

    "cotton.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="cotGrad" cx="40%" cy="40%" r="60%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="70%" stop-color="#f5f5f5"/>
      <stop offset="100%" stop-color="#e0e0e0"/>
    </radialGradient>
  </defs>
  <!-- Fluffy cotton boll -->
  <circle cx="48" cy="50" r="20" fill="url(#cotGrad)"/>
  <circle cx="72" cy="50" r="20" fill="url(#cotGrad)"/>
  <circle cx="60" cy="38" r="18" fill="url(#cotGrad)"/>
  <circle cx="60" cy="62" r="20" fill="url(#cotGrad)"/>
  <!-- Calyx sepals -->
  <path d="M60,68 L48,82 L56,74 L42,92 L58,80 L60,98 L64,80 L78,92 L66,74 L74,82 Z" fill="#5d4037"/>
  <!-- Stem -->
  <path d="M60,82 Q58,102 52,112" stroke="#4e342e" stroke-width="4" stroke-linecap="round" fill="none"/>
</svg>''',

    "wheat.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <linearGradient id="wGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#fff9c4"/>
      <stop offset="60%" stop-color="#fbc02d"/>
      <stop offset="100%" stop-color="#d99b00"/>
    </linearGradient>
  </defs>
  <path d="M50,112 Q56,70 60,25" stroke="#c49a45" stroke-width="3.5" stroke-linecap="round" fill="none"/>
  <!-- Wheat Spikelets with Awns -->
  <ellipse cx="54" cy="32" rx="7" ry="4" fill="url(#wGrad)" transform="rotate(-30 54 32)"/>
  <line x1="50" y1="30" x2="34" y2="14" stroke="#c49a45" stroke-width="1.5"/>
  <ellipse cx="66" cy="32" rx="7" ry="4" fill="url(#wGrad)" transform="rotate(30 66 32)"/>
  <line x1="70" y1="30" x2="86" y2="14" stroke="#c49a45" stroke-width="1.5"/>
  <ellipse cx="54" cy="46" rx="7" ry="4" fill="url(#wGrad)" transform="rotate(-30 54 46)"/>
  <line x1="50" y1="44" x2="32" y2="28" stroke="#c49a45" stroke-width="1.5"/>
  <ellipse cx="66" cy="46" rx="7" ry="4" fill="url(#wGrad)" transform="rotate(30 66 46)"/>
  <line x1="70" y1="44" x2="88" y2="28" stroke="#c49a45" stroke-width="1.5"/>
  <ellipse cx="55" cy="60" rx="7" ry="4" fill="url(#wGrad)" transform="rotate(-30 55 60)"/>
  <line x1="51" y1="58" x2="34" y2="42" stroke="#c49a45" stroke-width="1.5"/>
  <ellipse cx="67" cy="60" rx="7" ry="4" fill="url(#wGrad)" transform="rotate(30 67 60)"/>
  <line x1="71" y1="58" x2="88" y2="42" stroke="#c49a45" stroke-width="1.5"/>
  <ellipse cx="56" cy="74" rx="7" ry="4" fill="url(#wGrad)" transform="rotate(-30 56 74)"/>
  <ellipse cx="68" cy="74" rx="7" ry="4" fill="url(#wGrad)" transform="rotate(30 68 74)"/>
</svg>''',

    "garlic.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="garGrad" cx="45%" cy="45%" r="55%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="70%" stop-color="#f0ece6"/>
      <stop offset="100%" stop-color="#d7ccc8"/>
    </radialGradient>
  </defs>
  <!-- Bulb -->
  <path d="M60,25 C75,38 92,60 92,78 C92,94 78,102 60,102 C42,102 28,94 28,78 C28,60 45,38 60,25 Z" fill="url(#garGrad)"/>
  <!-- Cloves segments -->
  <path d="M60,25 C70,45 78,68 78,82 C78,96 70,101 60,102" stroke="#c7b9b1" stroke-width="2" fill="none"/>
  <path d="M60,25 C50,45 42,68 42,82 C42,96 50,101 60,102" stroke="#c7b9b1" stroke-width="2" fill="none"/>
  <!-- Neck Stem -->
  <path d="M57,26 L55,14 L65,14 L63,26 Z" fill="#bcaaa4"/>
  <!-- Roots -->
  <path d="M54,102 Q50,112 46,114 M60,102 Q60,114 60,116 M66,102 Q70,112 74,114" stroke="#a1887f" stroke-width="2" fill="none"/>
</svg>''',

    "ginger.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="gingGrad" cx="35%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#e8cf9c"/>
      <stop offset="65%" stop-color="#cba465"/>
      <stop offset="100%" stop-color="#936d2e"/>
    </radialGradient>
  </defs>
  <!-- Rhizome knobby shape -->
  <path d="M34,70 C24,58 26,42 42,42 C50,42 54,48 60,46 C64,36 68,26 80,28 C90,30 90,44 84,52 C88,58 98,64 96,76 C94,88 80,94 68,90 C58,94 44,90 38,82 C34,80 34,74 34,70 Z" fill="url(#gingGrad)"/>
  <!-- Growth rings -->
  <path d="M38,50 Q46,54 44,62 M68,36 Q74,40 72,48 M78,64 Q84,70 82,78 M50,80 Q56,84 62,82" stroke="#79551c" stroke-width="1.8" fill="none" opacity="0.6"/>
</svg>''',

    "cauliflower.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 120" width="120" height="120">
  <defs>
    <radialGradient id="curdGrad" cx="45%" cy="45%" r="55%">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="70%" stop-color="#fdfbf7"/>
      <stop offset="100%" stop-color="#ede6d6"/>
    </radialGradient>
  </defs>
  <!-- Surrounding Leaves -->
  <path d="M25,85 C14,60 22,34 38,26 C36,46 32,70 48,88 Z" fill="#388e3c"/>
  <path d="M95,85 C106,60 98,34 82,26 C84,46 88,70 72,88 Z" fill="#388e3c"/>
  <path d="M60,94 C46,104 35,92 25,85 C42,88 54,92 60,94 Z" fill="#2e7d32"/>
  <path d="M60,94 C74,104 85,92 95,85 C78,88 66,92 60,94 Z" fill="#2e7d32"/>
  <!-- Curd clusters -->
  <circle cx="60" cy="56" r="16" fill="url(#curdGrad)"/>
  <circle cx="46" cy="48" r="14" fill="url(#curdGrad)"/>
  <circle cx="74" cy="48" r="14" fill="url(#curdGrad)"/>
  <circle cx="44" cy="66" r="14" fill="url(#curdGrad)"/>
  <circle cx="76" cy="66" r="14" fill="url(#curdGrad)"/>
  <circle cx="60" cy="74" r="13" fill="url(#curdGrad)"/>
  <circle cx="60" cy="42" r="12" fill="url(#curdGrad)"/>
</svg>'''
}

for filename, content in CROPS_SVG.items():
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content.strip())

print(f"Generated {len(CROPS_SVG)} crop SVG illustrations in {OUTPUT_DIR}")
