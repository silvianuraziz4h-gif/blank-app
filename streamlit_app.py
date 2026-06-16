import streamlit as st
import math

# setup halaman
st.set_page_config(
    page_title="Kalkulator Kimia Analitik",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# DATA: SELURUH UNSUR TABEL PERIODIK (Mr standar)
# ============================================================
TABEL_PERIODIK = {
    "H – Hidrogen":      1.008,
    "He – Helium":       4.003,
    "Li – Litium":       6.941,
    "Be – Berilium":     9.012,
    "B – Boron":        10.811,
    "C – Karbon":       12.011,
    "N – Nitrogen":     14.007,
    "O – Oksigen":      15.999,
    "F – Fluor":        18.998,
    "Ne – Neon":        20.180,
    "Na – Natrium":     22.990,
    "Mg – Magnesium":   24.305,
    "Al – Aluminium":   26.982,
    "Si – Silikon":     28.086,
    "P – Fosfor":       30.974,
    "S – Sulfur":       32.065,
    "Cl – Klor":        35.453,
    "Ar – Argon":       39.948,
    "K – Kalium":       39.098,
    "Ca – Kalsium":     40.078,
    "Sc – Skandium":    44.956,
    "Ti – Titanium":    47.867,
    "V – Vanadium":     50.942,
    "Cr – Krom":        51.996,
    "Mn – Mangan":      54.938,
    "Fe – Besi":        55.845,
    "Co – Kobalt":      58.933,
    "Ni – Nikel":       58.693,
    "Cu – Tembaga":     63.546,
    "Zn – Seng":        65.38,
    "Ga – Galium":      69.723,
    "Ge – Germanium":   72.630,
    "As – Arsen":       74.922,
    "Se – Selenium":    78.971,
    "Br – Brom":        79.904,
    "Kr – Kripton":     83.798,
    "Rb – Rubidium":    85.468,
    "Sr – Stronsium":   87.620,
    "Y – Itrium":       88.906,
    "Zr – Zirkonium":   91.224,
    "Nb – Niobium":     92.906,
    "Mo – Molibdenum":  95.960,
    "Tc – Teknesium":   98.000,
    "Ru – Rutenium":   101.070,
    "Rh – Rodium":     102.906,
    "Pd – Paladium":   106.420,
    "Ag – Perak":      107.868,
    "Cd – Kadmium":    112.411,
    "In – Indium":     114.818,
    "Sn – Timah":      118.710,
    "Sb – Antimon":    121.760,
    "Te – Telurium":   127.600,
    "I – Iodin":       126.904,
    "Xe – Xenon":      131.293,
    "Cs – Sesium":     132.905,
    "Ba – Barium":     137.327,
    "La – Lantanum":   138.905,
    "Ce – Serium":     140.116,
    "Pr – Praseodimium": 140.908,
    "Nd – Neodimium":  144.242,
    "Pm – Prometium":  145.000,
    "Sm – Samarium":   150.360,
    "Eu – Europium":   151.964,
    "Gd – Gadolinium": 157.250,
    "Tb – Terbium":    158.925,
    "Dy – Disprosium": 162.500,
    "Ho – Holmium":    164.930,
    "Er – Erbium":     167.259,
    "Tm – Tulium":     168.934,
    "Yb – Iterbium":   173.054,
    "Lu – Lutesium":   174.967,
    "Hf – Hafnium":    178.490,
    "Ta – Tantalum":   180.948,
    "W – Wolfram":     183.840,
    "Re – Renium":     186.207,
    "Os – Osmium":     190.230,
    "Ir – Iridium":    192.217,
    "Pt – Platina":    195.084,
    "Au – Emas":       196.967,
    "Hg – Raksa":      200.592,
    "Tl – Talium":     204.383,
    "Pb – Timbal":     207.200,
    "Bi – Bismut":     208.980,
    "Po – Polonium":   209.000,
    "At – Astatin":    210.000,
    "Rn – Radon":      222.000,
    "Fr – Fransium":   223.000,
    "Ra – Radium":     226.000,
    "Ac – Aktinium":   227.000,
    "Th – Torium":     232.038,
    "Pa – Protaktinium": 231.036,
    "U – Uranium":     238.029,
    "Np – Neptunium":  237.000,
    "Pu – Plutonium":  244.000,
    "Am – Amerisium":  243.000,
    "Cm – Kurium":     247.000,
    "Bk – Berkelium":  247.000,
    "Cf – Kalifornium": 251.000,
    "Es – Einsteinium": 252.000,
    "Fm – Fermium":    257.000,
    "Md – Mendelevium": 258.000,
    "No – Nobelium":   259.000,
    "Lr – Lawrensium": 266.000,
    "Rf – Rutherfordium": 267.000,
    "Db – Dubnium":    268.000,
    "Sg – Siborgium":  269.000,
    "Bh – Bohrium":    270.000,
    "Hs – Hassium":    277.000,
    "Mt – Meitnerium": 278.000,
    "Ds – Darmstadtium": 281.000,
    "Rg – Roentgenium": 282.000,
    "Cn – Kopernisium": 285.000,
    "Nh – Nihonium":   286.000,
    "Fl – Flerovium":  289.000,
    "Mc – Moskobium":  290.000,
    "Lv – Livermorium": 293.000,
    "Ts – Tennesin":   294.000,
    "Og – Oganesson":  294.000,
}

# Mr senyawa umum + unsur (dropdown otomatis)
MR_SENYAWA = {
    # === Senyawa Asam ===
    "HCl – Asam klorida":              36.46,
    "HNO₃ – Asam nitrat":              63.01,
    "H₂SO₄ – Asam sulfat":             98.08,
    "H₃PO₄ – Asam fosfat":             97.99,
    "CH₃COOH – Asam asetat":           60.05,
    "HF – Asam fluorida":               20.01,
    "HBr – Asam bromida":               80.91,
    "HI – Asam iodida":                127.91,
    "HClO₄ – Asam perklorat":          100.46,
    "HClO₃ – Asam klorat":              84.46,
    "HNO₂ – Asam nitrit":               47.01,
    "H₂S – Asam sulfida":               34.08,
    "H₂CO₃ – Asam karbonat":            62.02,
    "H₂C₂O₄ – Asam oksalat":            90.03,
    "HCOOH – Asam format":               46.03,
    "C₆H₅COOH – Asam benzoat":         122.12,
    # === Basa ===
    "NaOH – Natrium hidroksida":         40.00,
    "KOH – Kalium hidroksida":           56.11,
    "Ca(OH)₂ – Kalsium hidroksida":      74.09,
    "Mg(OH)₂ – Magnesium hidroksida":    58.32,
    "Al(OH)₃ – Aluminium hidroksida":    78.00,
    "NH₃ – Amonia":                      17.03,
    "NH₄OH – Amonium hidroksida":        35.05,
    "Ba(OH)₂ – Barium hidroksida":      171.34,
    # === Garam ===
    "NaCl – Natrium klorida":            58.44,
    "KCl – Kalium klorida":              74.55,
    "NaHCO₃ – Natrium bikarbonat":       84.01,
    "Na₂CO₃ – Natrium karbonat":        105.99,
    "CaCO₃ – Kalsium karbonat":         100.09,
    "MgSO₄ – Magnesium sulfat":         120.37,
    "CuSO₄ – Tembaga(II) sulfat":       159.61,
    "FeSO₄ – Besi(II) sulfat":          151.91,
    "Fe₂(SO₄)₃ – Besi(III) sulfat":    399.88,
    "AgNO₃ – Perak nitrat":             169.87,
    "BaCl₂ – Barium klorida":           208.23,
    "CaCl₂ – Kalsium klorida":          110.98,
    "KMnO₄ – Kalium permanganat":       158.03,
    "K₂Cr₂O₇ – Kalium dikromat":        294.18,
    "Na₂SO₄ – Natrium sulfat":          142.04,
    "Na₂S₂O₃ – Natrium tiosulfat":      158.11,
    "NH₄Cl – Amonium klorida":           53.49,
    "NH₄NO₃ – Amonium nitrat":           80.04,
    "(NH₄)₂SO₄ – Amonium sulfat":       132.14,
    "ZnSO₄ – Seng sulfat":             161.47,
    "Pb(NO₃)₂ – Timbal(II) nitrat":     331.21,
    "AlCl₃ – Aluminium klorida":        133.34,
    "Al₂(SO₄)₃ – Aluminium sulfat":     342.15,
    "FeCl₃ – Besi(III) klorida":        162.20,
    "FeCl₂ – Besi(II) klorida":        126.75,
    "MnSO₄ – Mangan(II) sulfat":       151.00,
    "KNO₃ – Kalium nitrat":             101.10,
    "NaNO₃ – Natrium nitrat":            84.99,
    "Ca(NO₃)₂ – Kalsium nitrat":       164.09,
    "K₂SO₄ – Kalium sulfat":            174.26,
    "KHSO₄ – Kalium hidrogen sulfat":   136.17,
    "Na₂HPO₄ – Natrium hidrogen fosfat": 141.96,
    "KH₂PO₄ – Kalium dihidrogen fosfat": 136.09,
    "CH₃COONa – Natrium asetat":         82.03,
    "CH₃COONH₄ – Amonium asetat":        77.08,
    # === Oksida ===
    "H₂O – Air":                         18.02,
    "CO₂ – Karbon dioksida":             44.01,
    "CO – Karbon monoksida":              28.01,
    "SO₂ – Sulfur dioksida":              64.06,
    "SO₃ – Sulfur trioksida":              80.06,
    "NO₂ – Nitrogen dioksida":             46.01,
    "NO – Nitrogen monoksida":             30.01,
    "N₂O – Dinitrogen monoksida":          44.01,
    "P₂O₅ – Difosfor pentaoksida":        141.94,
    "SiO₂ – Silikon dioksida":             60.08,
    "Fe₂O₃ – Besi(III) oksida":          159.69,
    "Fe₃O₄ – Besi(II,III) oksida":       231.53,
    "CuO – Tembaga(II) oksida":            79.55,
    "ZnO – Seng oksida":                   81.38,
    "Al₂O₃ – Aluminium oksida":          101.96,
    "MgO – Magnesium oksida":              40.30,
    "CaO – Kalsium oksida":                56.08,
    "Na₂O – Natrium oksida":               61.98,
    "K₂O – Kalium oksida":                 94.20,
    # === Organik ===
    "C₆H₁₂O₆ – Glukosa":               180.16,
    "C₁₂H₂₂O₁₁ – Sukrosa":             342.30,
    "C₂H₅OH – Etanol":                    46.07,
    "CH₃OH – Metanol":                     32.04,
    "C₃H₇OH – Propanol":                  60.10,
    "C₆H₆ – Benzena":                      78.11,
    "C₇H₈ – Toluena":                      92.14,
    "CHCl₃ – Kloroform":                  119.38,
    "CCl₄ – Karbon tetraklorida":         153.82,
    "CH₂Cl₂ – Diklorometana":              84.93,
    "EDTA (C₁₀H₁₆N₂O₈)":               292.24,
    "Asam salisilat (C₇H₆O₃)":           138.12,
    "Asam askorbat (C₆H₈O₆)":            176.12,
    "Urea (CO(NH₂)₂)":                    60.06,
    "Anilin (C₆H₅NH₂)":                   93.13,
}

# Gabungkan untuk dropdown Mr
MR_DROPDOWN = {**MR_SENYAWA, **{k: v for k, v in TABEL_PERIODIK.items() if k not in MR_SENYAWA}}

# Keterangan istilah kimia
KETERANGAN_ISTILAH = {
    "Mr": "**Mr (Massa Relatif / Berat Molekul)** — Massa rata-rata satu molekul zat dibandingkan 1/12 massa atom karbon-12. Satuan: g/mol.",
    "Molaritas": "**Molaritas (M)** — Jumlah mol zat terlarut per liter larutan. Rumus: M = n/V(L). Satuan: mol/L.",
    "Molalitas": "**Molalitas (m)** — Jumlah mol zat terlarut per kilogram pelarut. Satuan: mol/kg.",
    "ppm": "**ppm (parts per million)** — Konsentrasi 1 mg zat dalam 1 liter larutan (setara mg/L). Umum digunakan untuk larutan sangat encer.",
    "ppb": "**ppb (parts per billion)** — Konsentrasi 1 µg zat dalam 1 liter larutan (setara µg/L). Digunakan untuk analisis jejak/trace.",
    "Ka": "**Ka (Tetapan Ionisasi Asam)** — Ukuran kekuatan asam lemah. Semakin besar Ka, semakin kuat asamnya. Ka = [H⁺][A⁻]/[HA].",
    "Kb": "**Kb (Tetapan Ionisasi Basa)** — Ukuran kekuatan basa lemah. Semakin besar Kb, semakin kuat basanya. Kb = [BH⁺][OH⁻]/[B].",
    "pKa": "**pKa** — Logaritma negatif dari Ka: pKa = -log(Ka). Makin kecil pKa, makin kuat asamnya.",
    "Buffer": "**Larutan Buffer (Penyangga)** — Larutan yang mampu mempertahankan pH meskipun ditambahkan sedikit asam/basa. Umumnya berisi asam lemah dan basa konjugatnya.",
    "Henderson": "**Persamaan Henderson-Hasselbalch** — pH = pKa + log([A⁻]/[HA]). Digunakan menghitung pH larutan buffer.",
    "Galat": "**Galat (Error)** — Perbedaan antara nilai terukur dan nilai sebenarnya. Galat Absolut = |x_ukur - x_benar|. Galat Relatif = (Galat Absolut / x_benar) × 100%.",
    "SD": "**SD (Standar Deviasi)** — Ukuran sebaran data dari nilai rata-rata. Semakin kecil SD, data semakin presisi.",
    "RSD": "**RSD (Relative Standard Deviation) / CV** — RSD = (SD/rata-rata) × 100%. Menyatakan presisi data secara relatif.",
    "Stoikiometri": "**Stoikiometri** — Cabang kimia yang mempelajari hubungan kuantitatif antara reaktan dan produk dalam reaksi kimia berdasarkan hukum perbandingan tetap.",
    "Reaktan pembatas": "**Reaktan Pembatas (Limiting Reagent)** — Zat yang habis lebih dulu dalam reaksi, menentukan jumlah maksimum produk yang dapat dihasilkan.",
    "Faktor pengenceran": "**Faktor Pengenceran (FP)** — Perbandingan volume akhir terhadap volume sampel awal. FP = V_akhir / V_sampel.",
    "Beta": "**Kapasitas Buffer (β)** — Ukuran kemampuan larutan buffer menahan perubahan pH. Dihitung dengan persamaan Van Slyke: β = 2.303 × C × Ka[H⁺]/(Ka+[H⁺])².",
}

# styling custom (light & dark mode compatible)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600&family=Space+Mono:wght@400;700&display=swap');

/* ============ DARK MODE (default) ============ */
.stApp {
    background: #1a1a2e !important;
    background-image: radial-gradient(ellipse at top left, #16213e 0%, #1a1a2e 60%, #0f3460 100%) !important;
    background-attachment: fixed;
    color: #f0f0f0 !important;
}
html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; }

.stMarkdown, p, label, .stSlider, .stRadio,
div[data-baseweb="checkbox"] { color: #f0f0f0 !important; }

div[data-testid="stNumberInput"] input,
div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea,
div[data-baseweb="select"] div { color: #1a1a2e !important; font-weight: 500 !important; }

div[data-shaded="true"], ul[role="listbox"] li { color: #1a1a2e !important; }

button[data-baseweb="tab"] p { color: #9e9e9e !important; }
button[data-baseweb="tab"][aria-selected="true"] p {
    color: #e8a045 !important;
    font-weight: 700 !important;
}

/* ============ LIGHT MODE OVERRIDES ============ */
@media (prefers-color-scheme: light) {
    .stApp {
        background: #f5f7fa !important;
        background-image: none !important;
        color: #1a1a2e !important;
    }
    .stMarkdown, p, label, .stSlider, .stRadio,
    div[data-baseweb="checkbox"] { color: #1a1a2e !important; }
    .menu-title { color: #1a1a2e !important; }
    .menu-desc  { color: #444 !important; }
    .welcome-outer { background: #fff !important; border: 1px solid #ddd !important; }
    .welcome-body { color: #333 !important; }
    .welcome-desc { color: #444 !important; }
    .result-value { color: #b37010 !important; }
    .result-label { color: #555 !important; }
    .result-card { background: rgba(232,160,69,0.12) !important; border-color: rgba(232,160,69,0.5) !important; }
    .info-card { background: #fff !important; border: 1px solid #ddd !important; }
    .info-card ul { color: #444 !important; }
    .menu-card { background: #fff !important; border: 1px solid #e0e0e0 !important; }
    .menu-card:hover { background: #f0f4ff !important; }
    .badge { color: #b37010 !important; border-color: #b37010 !important; background: rgba(180,120,20,0.08) !important; }
    .main-title { color: #1a1a2e !important; }
    .main-title em { color: #b37010 !important; }
    .subtitle { color: #555 !important; }
    .formula-box { color: #b37010 !important; background: rgba(180,120,20,0.07) !important; border-color: rgba(180,120,20,0.4) !important; }
    .istilah-box { background: #eaf2fb !important; border-color: #3498db !important; color: #1a3a5c !important; }
    .istilah-box b { color: #1a3a5c !important; }
    div[data-testid="stNumberInput"] input,
    div[data-testid="stTextInput"] input,
    div[data-testid="stTextArea"] textarea { color: #1a1a2e !important; }
}

/* ============ SHARED COMPONENTS ============ */
.badge {
    display: inline-block;
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: .1em;
    text-transform: uppercase;
    color: #e8a045;
    border: 1.5px solid #e8a045;
    border-radius: 4px;
    padding: 3px 12px;
    margin-bottom: 1rem;
    background: rgba(232,160,69,0.08);
}
.main-title {
    font-size: 38px;
    font-weight: 600;
    line-height: 1.2;
    color: #fff;
    margin: 0 0 .4rem;
}
.main-title em { font-style: normal; color: #e8a045; }
.subtitle { font-size: 14px; color: #9e9e9e; line-height: 1.6; max-width: 560px; margin-bottom: 1.5rem; }

.formula-box {
    background: rgba(232,160,69,0.07);
    border: 1px solid rgba(232,160,69,0.5);
    border-radius: 8px;
    padding: 10px 16px;
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    color: #e8a045;
    text-align: center;
    margin: 1rem 0;
}

/* identitas tim */
.identitas-box {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(232,160,69,0.35);
    border-radius: 10px;
    padding: 1rem 1.4rem;
    margin-bottom: 1.2rem;
}
.identitas-title {
    font-size: 12px;
    font-family: 'Space Mono', monospace;
    text-transform: uppercase;
    letter-spacing: .1em;
    color: #e8a045;
    margin-bottom: 0.4rem;
}
.identitas-list {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem 1.5rem;
    margin: 0;
    padding: 0;
    list-style: none;
}
.identitas-list li {
    font-size: 14px;
    color: #cfcfcf;
}

/* keterangan istilah */
.istilah-box {
    background: rgba(52,152,219,0.10);
    border: 1px solid rgba(52,152,219,0.45);
    border-left: 4px solid #3498db;
    border-radius: 6px;
    padding: 10px 14px;
    font-size: 12.5px;
    color: #c0dff5;
    margin: 0.5rem 0 1rem;
    line-height: 1.6;
}

.welcome-outer {
    max-width: 700px;
    margin: 2.5rem auto 2rem;
    background: rgba(255,255,255,0.03);
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.08);
}
.welcome-header {
    background: linear-gradient(135deg, #0f3460, #16213e);
    padding: 2.5rem;
    text-align: center;
    border-bottom: 2px solid #e8a045;
}
.welcome-header h1 { font-size: 36px; font-weight: 600; margin: 0; color: #fff; }
.welcome-body { padding: 2rem; text-align: center; color: #cfcfcf; }
.welcome-desc { font-size: 18px; line-height: 1.5; margin: 0 auto; max-width: 560px; }

.info-card {
    background: rgba(255,255,255,0.04);
    border-radius: 12px;
    padding: 1.4rem;
    height: 100%;
    border: 1px solid rgba(255,255,255,0.07);
    border-top: 4px solid #e8a045;
}
.info-card h4 { margin-top: 0; font-size: 16px; margin-bottom: 0.6rem; color: #e8a045; }
.info-card ul { margin: 0; padding-left: 1.2rem; font-size: 14px; color: #b0b0b0; line-height: 1.7; }

.menu-card {
    background: rgba(255,255,255,0.04);
    border-radius: 10px;
    padding: 1.4rem;
    min-height: 180px;
    border: 1px solid rgba(255,255,255,0.06);
    transition: background 0.2s ease, transform 0.15s ease;
}
.menu-card:hover { background: rgba(255,255,255,0.07); transform: translateY(-2px); }
.card-p1 { border-left: 4px solid #e8a045; }
.card-p2 { border-left: 4px solid #4fc3f7; }
.card-p3 { border-left: 4px solid #81c784; }
.card-p4 { border-left: 4px solid #ce93d8; }
.card-p5 { border-left: 4px solid #ef9a9a; }
.menu-icon  { font-size: 22px; margin-bottom: 0.4rem; }
.menu-title { font-size: 16px; font-weight: 600; margin: 0.2rem 0 0.4rem; color: #f0f0f0; }
.menu-desc  { font-size: 12px; color: #9e9e9e; line-height: 1.5; }

div.stButton > button {
    background: #e8a045 !important;
    color: #1a1a2e !important;
    border: none !important;
    border-radius: 6px !important;
    padding: 0.55rem 1.4rem !important;
    font-weight: 700 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    letter-spacing: 0.02em !important;
    transition: opacity 0.15s;
}
div.stButton > button:hover { opacity: 0.88; }

.result-card {
    background: rgba(232,160,69,0.07);
    border-radius: 10px;
    padding: 1rem 1.4rem;
    margin-top: .75rem;
    border: 1px solid rgba(232,160,69,0.3);
}
.result-label {
    font-size: 10px;
    font-family: 'Space Mono', monospace;
    text-transform: uppercase;
    letter-spacing: .1em;
    margin: 0 0 4px;
    color: #9e9e9e;
}
.result-value {
    font-size: 24px;
    font-weight: 600;
    margin: 0;
    font-family: 'Space Mono', monospace;
    color: #e8a045;
}

div[data-testid="stNumberInput"],
div[data-testid="stSelectbox"],
div[data-testid="stTextInput"],
div[data-testid="stTextArea"] {
    background-color: rgba(255,255,255,0.04) !important;
    border-radius: 6px !important;
}
input, select, textarea { color: white !important; }
</style>
""", unsafe_allow_html=True)


# ============================================================
# KOMPONEN IDENTITAS TIM
# ============================================================
def tampilkan_identitas():
    st.markdown("""
    <div class="identitas-box">
        <div class="identitas-title">👥 Tim Penyusun</div>
        <ul class="identitas-list">
            <li>1. Anisa</li>
            <li>2. Rahma</li>
            <li>3. Wewing</li>
            <li>4. Abum</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# KOMPONEN KETERANGAN ISTILAH
# ============================================================
def keterangan(kunci):
    teks = KETERANGAN_ISTILAH.get(kunci, "")
    if teks:
        st.markdown(f'<div class="istilah-box">ℹ️ {teks}</div>', unsafe_allow_html=True)


# ============================================================
# FUNGSI TAMPILAN UMUM
# ============================================================
def tampilkan_kotak(judul, konten_html):
    return f"""
    <div style="background:rgba(255,255,255,0.04); padding:20px; border-radius:10px;
                border:1px dashed rgba(232,160,69,0.4); font-family:'Courier New',monospace; margin-top:15px;">
        <p style="margin:0 0 12px 0; color:#e8a045; font-weight:600; font-size:13px;">📋 {judul}</p>
        <div style="font-size:13px; color:#cfcfcf; line-height:1.7; padding-left:5px;">
            {konten_html}
        </div>
    </div>
    """

def buat_baris(teks):
    return f"<p style='margin:0 0 8px 0;'>{teks}</p>"

def tampilkan_hasil(nama_variabel, angka, satuan=""):
    sat_html = f'<span style="font-size:16px; color:#e8a045;">{satuan}</span>' if satuan else ""
    st.markdown(
        f'<div class="result-card">'
        f'<p class="result-label">{nama_variabel}</p>'
        f'<p class="result-value">{angka} {sat_html}</p>'
        f'</div>',
        unsafe_allow_html=True
    )

def pilih_mr(label, default_key, default_nama="NaCl – Natrium klorida", default_val=58.44):
    """Widget pilih Mr dari dropdown tabel periodik/senyawa atau input manual."""
    mode = st.radio(f"Input Mr untuk {label}:", ["Pilih dari daftar", "Input manual"], horizontal=True, key=f"mode_mr_{default_key}")
    if mode == "Pilih dari daftar":
        nama_list = list(MR_DROPDOWN.keys())
        idx_default = nama_list.index(default_nama) if default_nama in nama_list else 0
        pilihan = st.selectbox(f"Senyawa/Unsur ({label}):", nama_list, index=idx_default, key=f"sel_mr_{default_key}")
        return MR_DROPDOWN[pilihan], pilihan.split("–")[0].strip()
    else:
        val = st.number_input(f"Mr {label} (g/mol)", 0.001, value=default_val, key=f"num_mr_{default_key}")
        return val, label


# ============================================================
# SESSION STATE
# ============================================================
if 'menu_aktif' not in st.session_state:
    st.session_state.menu_aktif = "Start"

SATUAN_KONSENTRASI = ["Molaritas (M)", "% massa/volume (% m/v)", "ppm (mg/L)", "ppb (µg/L)", "mg/mL", "Molalitas (m)"]


# =============================================================
# HALAMAN START
# =============================================================
if st.session_state.menu_aktif == "Start":
    st.markdown("""
    <div class="welcome-outer">
        <div class="welcome-header">
             <h1>Selamat Datang 👋</h1>
        </div>
        <div class="welcome-body">
            <p class="welcome-desc" style="margin-bottom: 25px;">Aplikasi Kalkulator Kimia Analitik Kuantitatif</p>
            <img src="https://github.com/user-attachments/assets/33c8c3d4-cac9-482f-883d-0bf8a00563e3"
                 width="180"
                 style="display: block; margin:0 auto; border-radius: 50%; box-shadow: 0 4px 10px rgba(0,0,0,0.3);">
        </div>
    </div>
    """, unsafe_allow_html=True)

    tampilkan_identitas()

    _, col_tengah, _ = st.columns([1.2, 1, 1.2])
    with col_tengah:
        if st.button("Masuk ke Aplikasi →", key="btn_start", use_container_width=True):
            st.session_state.menu_aktif = "Dashboard"
            st.rerun()

    st.write("<br><br>", unsafe_allow_html=True)
    kol_kiri, kol_kanan = st.columns(2)
    with kol_kiri:
        st.markdown("""
        <div class="info-card">
            <h4>🎯 Tujuan Aplikasi</h4>
            <ul>
                <li>Menyediakan platform hitung laboratorium yang mudah dipahami.</li>
                <li>Mengecek kekeliruan pengerjaan angka desimal berkat otomasi kalkulasi analitis.</li>
            </ul>
        </div>""", unsafe_allow_html=True)
    with kol_kanan:
        st.markdown("""
        <div class="info-card">
            <h4>✨ Manfaat Aplikasi</h4>
            <ul>
                <li><b>Cepat & Efisien:</b> Memproses rumus C₁V₁=C₂V₂ dan stoikiometri dalam hitungan detik.</li>
                <li><b>Transparan:</b> Dilengkapi langkah penyelesaian lengkap dan hitung galat SD/RSD.</li>
            </ul>
        </div>""", unsafe_allow_html=True)


# =============================================================
# DASHBOARD
# =============================================================
elif st.session_state.menu_aktif == "Dashboard":
    tampilkan_identitas()
    st.markdown('<div class="badge">🧪 Kimia Analitik</div>', unsafe_allow_html=True)
    st.markdown("""
    <h1 class="main-title">Kalkulator <em>Analisis</em> Kuantitatif</h1>
    <p class="subtitle">Pilih salah satu modul kalkulator di bawah ini untuk memulai:</p>
    """, unsafe_allow_html=True)
    st.divider()

    col1, col2, col3 = st.columns(3)
    daftar_modul = [
        ("col1", "card-p1", "💧", "Pengenceran Larutan",
         "Kalkulator pengenceran tunggal, serial/bertingkat, dan penentuan faktor pengenceran sampel.",
         "Pengenceran", "btn_m1"),
        ("col2", "card-p2", "🔄", "Konsentrasi & Stoikiometri",
         "Konversi antar satuan kimia (M, %, ppm, ppb) dan hitung stoikiometri reaksi mol.",
         "Stoikiometri", "btn_m2"),
        ("col3", "card-p3", "🌈", "Kesetimbangan & pH",
         "Prediksi pH sistem asam-basa kuat/lemah dan perhitungan Ka/Kb tetapan larutan.",
         "pH", "btn_m3"),
    ]
    for nama_col, css_card, ikon, judul, deskripsi, halaman, kunci_btn in daftar_modul:
        with eval(nama_col):
            st.markdown(
                f'<div class="menu-card {css_card}">'
                f'<div class="menu-icon">{ikon}</div>'
                f'<div class="menu-title">{judul}</div>'
                f'<div class="menu-desc">{deskripsi}</div>'
                f'</div>',
                unsafe_allow_html=True
            )
            if st.button(f"Buka Modul →", key=kunci_btn, use_container_width=True):
                st.session_state.menu_aktif = halaman
                st.rerun()

    st.write("")
    col4, col5, _ = st.columns(3)
    modul_baris2 = [
        (col4, "card-p4", "🧪", "Larutan Buffer",
         "Desain sistem penyangga menggunakan persamaan Henderson-Hasselbalch.",
         "Buffer", "btn_m4"),
        (col5, "card-p5", "📊", "Galat & Propagasi",
         "Hitung ketidakpastian, deviasi standar (SD), dan nilai RSD data pengukuran.",
         "Galat", "btn_m5"),
    ]
    for kolom, css_card, ikon, judul, deskripsi, halaman, kunci_btn in modul_baris2:
        with kolom:
            st.markdown(
                f'<div class="menu-card {css_card}">'
                f'<div class="menu-icon">{ikon}</div>'
                f'<div class="menu-title">{judul}</div>'
                f'<div class="menu-desc">{deskripsi}</div>'
                f'</div>',
                unsafe_allow_html=True
            )
            if st.button("Buka Modul →", key=kunci_btn, use_container_width=True):
                st.session_state.menu_aktif = halaman
                st.rerun()


# =============================================================
# MODUL-MODUL
# =============================================================
else:
    if st.button("← Kembali ke Menu Utama", key="btn_back"):
        st.session_state.menu_aktif = "Dashboard"
        st.rerun()
    st.divider()

    # ----------------------------------------------------------
    # PENGENCERAN
    # ----------------------------------------------------------
    if st.session_state.menu_aktif == "Pengenceran":
        tampilkan_identitas()
        st.markdown("### 💧 Pengenceran Larutan")
        tab_cv, tab_serial, tab_fp = st.tabs(["C₁V₁ = C₂V₂", "Serial / Bertingkat", "Faktor Pengenceran"])

        with tab_cv:
            st.markdown('<div class="formula-box">C₁ × V₁ = C₂ × V₂</div>', unsafe_allow_html=True)
            keterangan("Molaritas")
            yang_dicari = st.selectbox("Variabel yang dicari:", [
                "C₂ — Konsentrasi akhir", "V₂ — Volume akhir",
                "C₁ — Konsentrasi awal",  "V₁ — Volume awal"
            ], key="cari_cv")
            satuan = st.selectbox("Satuan konsentrasi:", ["M", "mM", "µM", "mg/mL", "ppm", "ppb"], key="satuan_cv")
            col1, col2 = st.columns(2)

            if yang_dicari == "C₂ — Konsentrasi akhir":
                with col1:
                    c1 = st.number_input("C₁", 0.0, value=1.0, format="%.5f", key="c1_c2")
                    v1 = st.number_input("V₁ (mL)", 0.0, value=10.0, format="%.3f", key="v1_c2")
                with col2:
                    v2 = st.number_input("V₂ (mL)", 1e-9, value=100.0, format="%.3f", key="v2_c2")
                jawaban = (c1 * v1) / v2
                tampilkan_hasil("C₂ — Konsentrasi akhir", f"{jawaban:.6g}", satuan)
                st.markdown(tampilkan_kotak("Penyelesaian (C₂ = C₁V₁ / V₂)",
                    buat_baris(f"C₂ = ({c1} × {v1}) / {v2}") +
                    buat_baris(f"C₂ = <b>{jawaban:.6g} {satuan}</b>")
                ), unsafe_allow_html=True)

            elif yang_dicari == "V₂ — Volume akhir":
                with col1:
                    c1 = st.number_input("C₁", 0.0, value=1.0, format="%.5f", key="c1_v2")
                    v1 = st.number_input("V₁ (mL)", 0.0, value=10.0, format="%.3f", key="v1_v2")
                with col2:
                    c2 = st.number_input("C₂", 1e-9, value=0.1, format="%.5f", key="c2_v2")
                jawaban = (c1 * v1) / c2
                tampilkan_hasil("V₂ — Volume akhir", f"{jawaban:.5g}", "mL")
                st.markdown(tampilkan_kotak("Penyelesaian (V₂ = C₁V₁ / C₂)",
                    buat_baris(f"V₂ = ({c1} × {v1}) / {c2}") +
                    buat_baris(f"V₂ = <b>{jawaban:.5g} mL</b>")
                ), unsafe_allow_html=True)

            elif yang_dicari == "C₁ — Konsentrasi awal":
                with col1:
                    v1 = st.number_input("V₁ (mL)", 1e-9, value=10.0, format="%.3f", key="v1_c1")
                    c2 = st.number_input("C₂", 0.0, value=0.1, format="%.5f", key="c2_c1")
                with col2:
                    v2 = st.number_input("V₂ (mL)", 1e-9, value=100.0, format="%.3f", key="v2_c1")
                jawaban = (c2 * v2) / v1
                tampilkan_hasil("C₁ — Konsentrasi awal", f"{jawaban:.6g}", satuan)
                st.markdown(tampilkan_kotak("Penyelesaian (C₁ = C₂V₂ / V₁)",
                    buat_baris(f"C₁ = ({c2} × {v2}) / {v1}") +
                    buat_baris(f"C₁ = <b>{jawaban:.6g} {satuan}</b>")
                ), unsafe_allow_html=True)

            else:
                with col1:
                    c1 = st.number_input("C₁", 1e-9, value=1.0, format="%.5f", key="c1_v1")
                    c2 = st.number_input("C₂", 0.0, value=0.1, format="%.5f", key="c2_v1")
                with col2:
                    v2 = st.number_input("V₂ (mL)", 1e-9, value=100.0, format="%.3f", key="v2_v1")
                jawaban = (c2 * v2) / c1
                tampilkan_hasil("V₁ — Volume awal", f"{jawaban:.5g}", "mL")
                st.markdown(tampilkan_kotak("Penyelesaian (V₁ = C₂V₂ / C₁)",
                    buat_baris(f"V₁ = ({c2} × {v2}) / {c1}") +
                    buat_baris(f"V₁ = <b>{jawaban:.5g} mL</b>")
                ), unsafe_allow_html=True)

        with tab_serial:
            keterangan("Faktor pengenceran")
            n_tahap = st.slider("Jumlah tahap pengenceran:", 2, 6, 3, key="n_serial")
            c_awal = st.number_input("Konsentrasi awal C₀ (M)", 0.0, value=1.0, format="%.5f", key="c0_ser")

            c_skrg = c_awal
            langkah_html = buat_baris(f"C₀ = {c_awal} M")

            for i in range(n_tahap):
                kol_a, kol_b = st.columns(2)
                with kol_a:
                    v_ambil = st.number_input(f"V ambil tahap {i+1} (mL)", 0.001, value=1.0, key=f"va_{i}")
                with kol_b:
                    v_total = st.number_input(f"V total tahap {i+1} (mL)", 0.001, value=10.0, key=f"vt_{i}")
                fp_tahap = v_ambil / v_total
                c_skrg = c_skrg * fp_tahap
                langkah_html += buat_baris(
                    f"Tahap {i+1}: {v_ambil} mL → {v_total} mL, FP = {fp_tahap:.4f}, C = <b>{c_skrg:.4e} M</b>"
                )

            tampilkan_hasil("Konsentrasi Akhir (serial)", f"{c_skrg:.4e}", "M")
            st.markdown(tampilkan_kotak("Penyelesaian (Pengenceran Serial)", langkah_html), unsafe_allow_html=True)

        with tab_fp:
            keterangan("Faktor pengenceran")
            kol_a, kol_b = st.columns(2)
            with kol_a:
                va_fp = st.number_input("Volume sampel (mL)", 0.001, value=1.0, key="fp_va")
                ca_fp = st.number_input("Konsentrasi awal (opsional)", 0.0, value=1.0, format="%.5f", key="fp_ca")
            with kol_b:
                vb_fp = st.number_input("Volume akhir (mL)", 0.001, value=100.0, key="fp_vb")
            fp = vb_fp / va_fp
            tampilkan_hasil("Faktor Pengenceran", f"1 : {fp:.4f}")
            tampilkan_hasil("Konsentrasi Akhir", f"{ca_fp / fp:.5g}")
            st.markdown(tampilkan_kotak("Penyelesaian (Faktor Pengenceran)",
                buat_baris(f"FP = {vb_fp} / {va_fp} = <b>{fp:.4f}</b>") +
                buat_baris(f"C akhir = {ca_fp} / {fp:.4f} = <b>{ca_fp / fp:.5g}</b>")
            ), unsafe_allow_html=True)

    # ----------------------------------------------------------
    # STOIKIOMETRI
    # ----------------------------------------------------------
    elif st.session_state.menu_aktif == "Stoikiometri":
        tampilkan_identitas()
        st.markdown("### 🔄 Satuan Konsentrasi & Stoikiometri")
        tab_konv, tab_mol, tab_reaksi = st.tabs(["🔄 Konversi Satuan", "⚖️ Mol & Massa", "🧮 Stoikiometri Reaksi"])

        with tab_konv:
            keterangan("Molaritas")
            keterangan("ppm")
            col1, col2 = st.columns(2)
            with col1:
                satuan_dari = st.selectbox("Dari satuan:", SATUAN_KONSENTRASI, index=0, key="k_dari")
                nilai_input  = st.number_input("Nilai", 0.0, value=1.0, format="%.6f", key="k_val")
                mr_zat_val, mr_label = pilih_mr("zat", "konv", "NaCl – Natrium klorida", 58.44)
            with col2:
                satuan_ke = st.selectbox("Ke satuan:", SATUAN_KONSENTRASI, index=2, key="k_ke")
                densitas  = st.number_input("Densitas ρ (g/mL)", 0.001, value=1.0, key="k_rho")

            if satuan_dari == satuan_ke:
                st.warning("Pilih satuan yang berbeda.")
            else:
                ke_mgL = {
                    "Molaritas (M)":            lambda v: v * mr_zat_val * 1000,
                    "% massa/volume (% m/v)":   lambda v: v * 10000,
                    "ppm (mg/L)":               lambda v: v,
                    "ppb (µg/L)":               lambda v: v / 1000,
                    "mg/mL":                    lambda v: v * 1000,
                    "Molalitas (m)":            lambda v: v * mr_zat_val * densitas * 1000,
                }
                dari_mgL = {
                    "Molaritas (M)":            lambda v: v / (mr_zat_val * 1000),
                    "% massa/volume (% m/v)":   lambda v: v / 10000,
                    "ppm (mg/L)":               lambda v: v,
                    "ppb (µg/L)":               lambda v: v * 1000,
                    "mg/mL":                    lambda v: v / 1000,
                    "Molalitas (m)":            lambda v: v / (mr_zat_val * densitas * 1000),
                }
                nilai_mgL = ke_mgL[satuan_dari](nilai_input)
                nilai_target = dari_mgL[satuan_ke](nilai_mgL)
                tampilkan_hasil("Hasil Konversi", f"{nilai_target:.6g}", satuan_ke)
                st.markdown(tampilkan_kotak("Penyelesaian (via basis mg/L)",
                    buat_baris(f"'{satuan_dari}' → mg/L: <b>{nilai_mgL:.4e} mg/L</b>") +
                    buat_baris(f"mg/L → '{satuan_ke}': <b>{nilai_target:.6g} {satuan_ke}</b>") +
                    buat_baris(f"<span style='color:#9e9e9e;font-size:11px'>Mr ({mr_label}) = {mr_zat_val} g/mol | ρ = {densitas} g/mL</span>")
                ), unsafe_allow_html=True)

        with tab_mol:
            keterangan("Mr")
            keterangan("Molaritas")
            pilihan = st.selectbox("Cari:", [
                "Mol (n) dari massa & Mr", "Mol (n) dari M & V",
                "Massa (g) dari n & Mr",   "Molaritas (M) dari n & V",
                "Volume (mL) dari n & M"
            ], key="pilihan_mol")
            col1, col2 = st.columns(2)

            if "massa & Mr" in pilihan:
                with col1: massa = st.number_input("Massa (gram)", 0.0, value=5.85, format="%.4f", key="mol_m")
                with col2: mr, mr_lbl = pilih_mr("zat", "mol1", "NaCl – Natrium klorida", 58.44)
                n = massa / mr
                tampilkan_hasil("Mol (n)", f"{n:.5g}", "mol")
                st.markdown(tampilkan_kotak(f"n = gram / Mr({mr_lbl})",
                    buat_baris(f"n = {massa} / {mr} = <b>{n:.5g} mol</b>")
                ), unsafe_allow_html=True)

            elif "M & V" in pilihan:
                with col1: M_val = st.number_input("Molaritas (M)", 0.0, value=1.0, key="mol_M")
                with col2: V_val = st.number_input("Volume (mL)", 0.0, value=100.0, key="mol_V")
                n = M_val * (V_val / 1000)
                tampilkan_hasil("Mol (n)", f"{n:.5g}", "mol")
                st.markdown(tampilkan_kotak("n = M × (V/1000)",
                    buat_baris(f"n = {M_val} × ({V_val}/1000) = <b>{n:.5g} mol</b>")
                ), unsafe_allow_html=True)

            elif "Massa" in pilihan:
                with col1: n_input = st.number_input("Mol (n)", 0.0, value=0.1, key="mol_n_m")
                with col2: mr, mr_lbl = pilih_mr("zat", "mol3", "NaCl – Natrium klorida", 58.44)
                gram = n_input * mr
                tampilkan_hasil("Massa (m)", f"{gram:.5g}", "gram")
                st.markdown(tampilkan_kotak(f"gram = n × Mr({mr_lbl})",
                    buat_baris(f"gram = {n_input} × {mr} = <b>{gram:.5g} gram</b>")
                ), unsafe_allow_html=True)

            elif "Molaritas" in pilihan:
                with col1: n_input = st.number_input("Mol (n)", 0.0, value=0.1, key="mol_n_M")
                with col2: V_val = st.number_input("Volume (mL)", 0.001, value=100.0, key="mol_V2")
                M_hsl = n_input / (V_val / 1000)
                tampilkan_hasil("Molaritas (M)", f"{M_hsl:.5g}", "mol/L")
                st.markdown(tampilkan_kotak("M = n / (V/1000)",
                    buat_baris(f"M = {n_input} / ({V_val}/1000) = <b>{M_hsl:.5g} M</b>")
                ), unsafe_allow_html=True)

            else:
                with col1: n_input = st.number_input("Mol (n)", 0.0, value=0.1, key="mol_n_V")
                with col2: M_val = st.number_input("Molaritas (M)", 0.001, value=1.0, key="mol_M2")
                V_hsl = (n_input / M_val) * 1000
                tampilkan_hasil("Volume (V)", f"{V_hsl:.5g}", "mL")
                st.markdown(tampilkan_kotak("V (mL) = (n/M) × 1000",
                    buat_baris(f"V = ({n_input}/{M_val}) × 1000 = <b>{V_hsl:.5g} mL</b>")
                ), unsafe_allow_html=True)

        with tab_reaksi:
            keterangan("Stoikiometri")
            keterangan("Reaktan pembatas")

            # === Pilihan reaksi preset ===
            PRESET_REAKSI = {
                "HCl + NaOH → NaCl + H₂O (Netralisasi asam-basa)": {
                    "kA": 1, "nA": "HCl",  "mA": 36.46,
                    "kB": 1, "nB": "NaOH", "mB": 40.00,
                    "kC": 1, "nC": "NaCl", "mC": 58.44,
                    "kD": 1, "nD": "H₂O",  "mD": 18.02,
                },
                "H₂SO₄ + 2NaOH → Na₂SO₄ + 2H₂O": {
                    "kA": 1, "nA": "H₂SO₄",  "mA": 98.08,
                    "kB": 2, "nB": "NaOH",    "mB": 40.00,
                    "kC": 1, "nC": "Na₂SO₄",  "mC": 142.04,
                    "kD": 2, "nD": "H₂O",     "mD": 18.02,
                },
                "2HCl + CaCO₃ → CaCl₂ + H₂O + CO₂": {
                    "kA": 2, "nA": "HCl",    "mA": 36.46,
                    "kB": 1, "nB": "CaCO₃",  "mB": 100.09,
                    "kC": 1, "nC": "CaCl₂",  "mC": 110.98,
                    "kD": 1, "nD": "H₂O",    "mD": 18.02,
                },
                "Fe₂O₃ + 3CO → 2Fe + 3CO₂ (Reduksi besi)": {
                    "kA": 1, "nA": "Fe₂O₃", "mA": 159.69,
                    "kB": 3, "nB": "CO",     "mB": 28.01,
                    "kC": 2, "nC": "Fe",     "mC": 55.85,
                    "kD": 3, "nD": "CO₂",    "mD": 44.01,
                },
                "2H₂ + O₂ → 2H₂O (Pembakaran hidrogen)": {
                    "kA": 2, "nA": "H₂",  "mA": 2.016,
                    "kB": 1, "nB": "O₂",  "mB": 32.00,
                    "kC": 2, "nC": "H₂O", "mC": 18.02,
                    "kD": 0, "nD": "-",    "mD": 1.0,
                },
                "CH₄ + 2O₂ → CO₂ + 2H₂O (Pembakaran metana)": {
                    "kA": 1, "nA": "CH₄", "mA": 16.04,
                    "kB": 2, "nB": "O₂",  "mB": 32.00,
                    "kC": 1, "nC": "CO₂", "mC": 44.01,
                    "kD": 2, "nD": "H₂O", "mD": 18.02,
                },
                "AgNO₃ + NaCl → AgCl + NaNO₃ (Pengendapan)": {
                    "kA": 1, "nA": "AgNO₃", "mA": 169.87,
                    "kB": 1, "nB": "NaCl",  "mB": 58.44,
                    "kC": 1, "nC": "AgCl",  "mC": 143.32,
                    "kD": 1, "nD": "NaNO₃", "mD": 84.99,
                },
                "KMnO₄ + HCl → MnCl₂ + Cl₂ + KCl + H₂O (Redoks)": {
                    "kA": 2, "nA": "KMnO₄", "mA": 158.03,
                    "kB": 16,"nB": "HCl",   "mB": 36.46,
                    "kC": 2, "nC": "MnCl₂", "mC": 125.84,
                    "kD": 5, "nD": "Cl₂",   "mD": 70.90,
                },
                "Zn + H₂SO₄ → ZnSO₄ + H₂ (Logam + asam)": {
                    "kA": 1, "nA": "Zn",    "mA": 65.38,
                    "kB": 1, "nB": "H₂SO₄","mB": 98.08,
                    "kC": 1, "nC": "ZnSO₄", "mC": 161.47,
                    "kD": 1, "nD": "H₂",    "mD": 2.016,
                },
                "Na₂CO₃ + 2HCl → 2NaCl + H₂O + CO₂": {
                    "kA": 1, "nA": "Na₂CO₃","mA": 105.99,
                    "kB": 2, "nB": "HCl",   "mB": 36.46,
                    "kC": 2, "nC": "NaCl",  "mC": 58.44,
                    "kD": 1, "nD": "CO₂",   "mD": 44.01,
                },
                "Input Reaksi Manual": None,
            }

            preset_pilih = st.selectbox("Pilih reaksi preset atau input manual:", list(PRESET_REAKSI.keys()), key="preset_reaksi")
            p = PRESET_REAKSI[preset_pilih]

            if p is not None:
                kA_def, nA_def, mA_def = p["kA"], p["nA"], p["mA"]
                kB_def, nB_def, mB_def = p["kB"], p["nB"], p["mB"]
                kC_def, nC_def, mC_def = p["kC"], p["nC"], p["mC"]
                kD_def, nD_def, mD_def = p["kD"], p["nD"], p["mD"]
            else:
                kA_def, nA_def, mA_def = 1, "A", 36.46
                kB_def, nB_def, mB_def = 1, "B", 40.00
                kC_def, nC_def, mC_def = 1, "C", 58.44
                kD_def, nD_def, mD_def = 1, "D", 18.02

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.markdown("**Reaktan A**")
                kA = st.number_input("Koef A", 1, value=kA_def, key="kA")
                nA = st.text_input("Nama A", nA_def, key="nA")
                mA = st.number_input("Mr A (g/mol)", 0.001, value=float(mA_def), key="mA")
            with col2:
                st.markdown("**Reaktan B**")
                kB = st.number_input("Koef B", 1, value=kB_def, key="kB")
                nB = st.text_input("Nama B", nB_def, key="nB")
                mB = st.number_input("Mr B (g/mol)", 0.001, value=float(mB_def), key="mB")
            with col3:
                st.markdown("**Produk C**")
                kC = st.number_input("Koef C", 1, value=kC_def, key="kC")
                nC = st.text_input("Nama C", nC_def, key="nC")
                mC = st.number_input("Mr C (g/mol)", 0.001, value=float(mC_def), key="mC")
            with col4:
                st.markdown("**Produk D**")
                kD = st.number_input("Koef D", 0, value=kD_def, key="kD")
                nD = st.text_input("Nama D", nD_def, key="nD")
                mD = st.number_input("Mr D (g/mol)", 0.001, value=float(mD_def), key="mD")

            if kD > 0:
                persamaan = f"{kA} {nA} + {kB} {nB} → {kC} {nC} + {kD} {nD}"
            else:
                persamaan = f"{kA} {nA} + {kB} {nB} → {kC} {nC}"
            st.info(f"**Reaksi:** {persamaan}")

            reaktan_pembatas = st.selectbox("Reaktan pembatas:", [nA, nB], key="reaktan")
            mol_pembatas = st.number_input("Mol Reaktan Pembatas", 0.0, value=0.1, key="n_pem")

            k_ref = kA if reaktan_pembatas == nA else kB
            mol_C = mol_pembatas * (kC / k_ref)
            mol_D = mol_pembatas * (kD / k_ref) if kD > 0 else 0

            tampilkan_hasil(f"Hasil {nC}", f"{mol_C:.5g} mol ({mol_C * mC:.5g} g)")
            if kD > 0:
                tampilkan_hasil(f"Hasil {nD}", f"{mol_D:.5g} mol ({mol_D * mD:.5g} g)")

            langkah = (
                buat_baris(f"Reaksi: {persamaan}") +
                buat_baris(f"Reaktan pembatas: <b>{reaktan_pembatas}</b> = {mol_pembatas} mol") +
                buat_baris(f"Mol {nC} = ({kC}/{k_ref}) × {mol_pembatas} = <b>{mol_C:.5g} mol</b>") +
                buat_baris(f"Massa {nC} = {mol_C:.5g} × {mC} = <b>{mol_C * mC:.5g} gram</b>")
            )
            if kD > 0:
                langkah += (
                    buat_baris(f"Mol {nD} = ({kD}/{k_ref}) × {mol_pembatas} = <b>{mol_D:.5g} mol</b>") +
                    buat_baris(f"Massa {nD} = {mol_D:.5g} × {mD} = <b>{mol_D * mD:.5g} gram</b>")
                )
            st.markdown(tampilkan_kotak("Penyelesaian (perbandingan koefisien)", langkah), unsafe_allow_html=True)

    # ----------------------------------------------------------
    # pH & KESETIMBANGAN
    # ----------------------------------------------------------
    elif st.session_state.menu_aktif == "pH":
        tampilkan_identitas()
        st.markdown("### 🌈 Kesetimbangan & Perubahan pH")
        tab_asam, tab_basa, tab_ka, tab_dilusi = st.tabs([
            "🔴 pH Asam", "🔵 pH Basa", "🔬 Hitung Ka/Kb", "📉 ΔpH Pengenceran"
        ])

        with tab_asam:
            keterangan("Ka")
            tipe_asam = st.radio("Jenis asam:", ["Asam Kuat", "Asam Lemah"], horizontal=True, key="jenis_asam")
            C = st.number_input("Konsentrasi C (M)", 1e-14, value=0.1, key="C_asam")
            if tipe_asam == "Asam Kuat":
                pH = -math.log10(max(C, 1e-14))
                tampilkan_hasil("pH Larutan", f"{pH:.4f}")
                st.markdown(tampilkan_kotak("pH = -log[H⁺]",
                    buat_baris(f"[H⁺] = {C} M") +
                    buat_baris(f"pH = -log({C}) = <b>{pH:.4f}</b>")
                ), unsafe_allow_html=True)
            else:
                Ka = st.number_input("Ka", 1e-20, value=1.8e-5, key="Ka_asam")
                h  = math.sqrt(Ka * C)
                pH = -math.log10(h)
                tampilkan_hasil("pH Larutan", f"{pH:.4f}")
                st.markdown(tampilkan_kotak("pH Asam Lemah: [H⁺] = √(Ka × C)",
                    buat_baris(f"[H⁺] = √({Ka} × {C}) = {h:.4e} M") +
                    buat_baris(f"pH = -log({h:.4e}) = <b>{pH:.4f}</b>")
                ), unsafe_allow_html=True)

        with tab_basa:
            keterangan("Kb")
            tipe_basa = st.radio("Jenis basa:", ["Basa Kuat", "Basa Lemah"], horizontal=True, key="jenis_basa")
            C = st.number_input("Konsentrasi C (M)", 1e-14, value=0.1, key="C_basa")
            if tipe_basa == "Basa Kuat":
                pH = 14 + math.log10(C)
                tampilkan_hasil("pH Larutan", f"{pH:.4f}")
                st.markdown(tampilkan_kotak("pH = 14 - pOH",
                    buat_baris(f"pOH = -log({C}) = {-math.log10(C):.4f}") +
                    buat_baris(f"pH = 14 - pOH = <b>{pH:.4f}</b>")
                ), unsafe_allow_html=True)
            else:
                Kb = st.number_input("Kb", 1e-20, value=1.8e-5, key="Kb_basa")
                oh = math.sqrt(Kb * C)
                pH = 14 + math.log10(oh)
                tampilkan_hasil("pH Larutan", f"{pH:.4f}")
                st.markdown(tampilkan_kotak("pH Basa Lemah: [OH⁻] = √(Kb × C)",
                    buat_baris(f"[OH⁻] = √({Kb} × {C}) = {oh:.4e} M") +
                    buat_baris(f"pOH = -log({oh:.4e}) = {-math.log10(oh):.4f}") +
                    buat_baris(f"pH = 14 - pOH = <b>{pH:.4f}</b>")
                ), unsafe_allow_html=True)

        with tab_ka:
            keterangan("Ka")
            C  = st.number_input("Konsentrasi C (M)", 1e-10, value=0.1, key="C_ka")
            pH = st.number_input("pH terukur", 0.0, 14.0, value=2.87, key="pH_ka")
            H  = 10 ** (-pH)
            if C > H:
                Ka = H**2 / (C - H)
                tampilkan_hasil("Ka Prediksi", f"{Ka:.4e}")
                st.markdown(tampilkan_kotak("Ka = [H⁺]² / (C - [H⁺])",
                    buat_baris(f"[H⁺] = 10^(-{pH}) = {H:.4e} M") +
                    buat_baris(f"Ka = ({H:.4e})² / ({C} - {H:.4e}) = <b>{Ka:.4e}</b>")
                ), unsafe_allow_html=True)

        with tab_dilusi:
            keterangan("Molaritas")
            tipe_dil = st.radio("Jenis larutan:", ["Asam Kuat", "Asam Lemah", "Basa Kuat", "Basa Lemah"],
                             horizontal=True, key="jenis_dilusi")
            C1 = st.number_input("C₁ (M)", 1e-14, value=0.1, key="C1_dil")
            V1 = st.number_input("V₁ (mL)", 0.001, value=10.0, key="V1_dil")
            V2 = st.number_input("V₂ (mL)", 0.001, value=100.0, key="V2_dil")
            K_val = st.number_input("Ka / Kb", 1e-20, value=1.8e-5, key="K_dil") if "Lemah" in tipe_dil else None

            def hitung_pH_larutan(konsentrasi, tipe, K):
                c = max(konsentrasi, 1e-14)
                if tipe == "Asam Kuat":   return -math.log10(c)
                if tipe == "Asam Lemah":  return -math.log10(math.sqrt(K * c))
                if tipe == "Basa Kuat":   return 14 + math.log10(c)
                if tipe == "Basa Lemah":  return 14 + math.log10(math.sqrt(K * c))

            C2  = C1 * V1 / V2
            pH1 = hitung_pH_larutan(C1, tipe_dil, K_val)
            pH2 = hitung_pH_larutan(C2, tipe_dil, K_val)
            delta_pH = abs(pH2 - pH1)
            tampilkan_hasil("pH Akhir", f"{pH2:.4f}", f"(Awal: {pH1:.4f})")
            st.markdown(tampilkan_kotak("Penyelesaian (Efek Dilusi terhadap pH)",
                buat_baris(f"C₂ = ({C1} × {V1}) / {V2} = <b>{C2:.4e} M</b>") +
                buat_baris(f"pH₁ (C₁) = <b>{pH1:.4f}</b>") +
                buat_baris(f"pH₂ (C₂) = <b>{pH2:.4f}</b>") +
                buat_baris(f"ΔpH = <b>{delta_pH:.4f}</b>")
            ), unsafe_allow_html=True)

    # ----------------------------------------------------------
    # BUFFER
    # ----------------------------------------------------------
    elif st.session_state.menu_aktif == "Buffer":
        tampilkan_identitas()
        st.markdown("### 🧪 Pembuatan Larutan Buffer")
        tab_ph, tab_rasio, tab_beta = st.tabs([
            "🧮 Hitung pH Buffer", "⚖️ Hitung Rasio [A⁻]/[HA]", "📊 Kapasitas Buffer (β)"
        ])

        with tab_ph:
            keterangan("Buffer")
            keterangan("Henderson")
            pKa = st.number_input("pKa asam", 0.0, 14.0, value=4.74, key="pka_buf")
            ab  = st.number_input("[A⁻] Basa Konjugat (M)", 0.0001, value=0.1, key="ab_buf")
            ha  = st.number_input("[HA] Asam (M)", 0.0001, value=0.1, key="ha_buf")
            pH_buf = pKa + math.log10(ab / ha)
            tampilkan_hasil("pH Buffer", f"{pH_buf:.4f}")
            st.markdown(tampilkan_kotak("Henderson-Hasselbalch: pH = pKa + log([A⁻]/[HA])",
                buat_baris(f"pH = {pKa} + log({ab}/{ha})") +
                buat_baris(f"pH = {pKa} + {math.log10(ab/ha):.4f} = <b>{pH_buf:.4f}</b>")
            ), unsafe_allow_html=True)

        with tab_rasio:
            keterangan("pKa")
            pH_target = st.number_input("pH target", 0.0, 14.0, value=5.0, key="pH_rasio")
            pKa_r     = st.number_input("pKa asam", 0.0, 14.0, value=4.74, key="pka_rasio")
            C_total   = st.number_input("Konsentrasi total (M)", 0.001, value=0.2, key="Ctot_rasio")
            rasio = 10 ** (pH_target - pKa_r)
            konj  = C_total * rasio / (1 + rasio)
            asam  = C_total / (1 + rasio)
            tampilkan_hasil("Rasio [A⁻]/[HA]", f"{rasio:.5f}", f"([A⁻]={konj:.4f}M)")
            st.markdown(tampilkan_kotak("Rasio = 10^(pH - pKa)",
                buat_baris(f"[A⁻]/[HA] = 10^({pH_target} - {pKa_r}) = <b>{rasio:.5f}</b>") +
                buat_baris(f"[A⁻] = ({rasio:.5f} / (1+{rasio:.5f})) × {C_total} = <b>{konj:.4f} M</b>") +
                buat_baris(f"[HA] = {C_total} - {konj:.4f} = <b>{asam:.4f} M</b>")
            ), unsafe_allow_html=True)

        with tab_beta:
            keterangan("Beta")
            C_tot = st.number_input("Konsentrasi total (M)", 0.0001, value=0.1, key="Ctot_beta")
            Ka_b  = st.number_input("Ka", 1e-20, value=1.8e-5, key="Ka_beta")
            pH_b  = st.number_input("pH larutan", 0.0, 14.0, value=4.74, key="pH_beta")
            H_b   = 10 ** (-pH_b)
            beta  = 2.303 * C_tot * (Ka_b * H_b) / (Ka_b + H_b)**2
            tampilkan_hasil("Kapasitas Buffer (β)", f"{beta:.4e}")
            st.markdown(tampilkan_kotak("Van Slyke: β = 2.303 × C × Ka[H⁺] / (Ka+[H⁺])²",
                buat_baris(f"[H⁺] = 10^(-{pH_b}) = {H_b:.4e} M") +
                buat_baris(f"β = 2.303 × {C_tot} × ({Ka_b:.2e} × {H_b:.2e}) / ({Ka_b:.2e} + {H_b:.2e})²") +
                buat_baris(f"β = <b>{beta:.4e}</b>")
            ), unsafe_allow_html=True)

    # ----------------------------------------------------------
    # GALAT & PROPAGASI ERROR
    # ----------------------------------------------------------
    elif st.session_state.menu_aktif == "Galat":
        tampilkan_identitas()
        st.markdown("### 📊 Galat & Propagasi Error")
        tab_ga, tab_prop, tab_stat = st.tabs([
            "📏 Galat Absolut & Relatif", "⚡ Propagasi Error", "📊 Statistik (SD & RSD)"
        ])

        with tab_ga:
            keterangan("Galat")
            x_ukur  = st.number_input("Nilai terukur", value=9.87, key="x_ukur")
            x_benar = st.number_input("Nilai benar / referensi", value=10.00, key="x_benar")
            g_abs = abs(x_ukur - x_benar)
            g_rel = (g_abs / x_benar) * 100
            tampilkan_hasil("Galat Absolut", f"{g_abs:.5g}")
            st.markdown(tampilkan_kotak("Galat Absolut & Relatif",
                buat_baris(f"Galat Absolut = |{x_ukur} - {x_benar}| = <b>{g_abs:.5g}</b>") +
                buat_baris(f"Galat Relatif = ({g_abs:.5g} / {x_benar}) × 100 = <b>{g_rel:.3f}%</b>")
            ), unsafe_allow_html=True)

        with tab_prop:
            jenis_op = st.selectbox("Operasi:", [
                "Penjumlahan / Pengurangan (x ± y)",
                "Perkalian / Pembagian (x × y atau x/y)"
            ], key="op_prop")
            x_val  = st.number_input("Nilai x", value=10.0, key="xv")
            dx_val = st.number_input("δx", value=0.05, key="dxv")
            y_val  = st.number_input("Nilai y", value=5.0, key="yv")
            dy_val = st.number_input("δy", value=0.03, key="dyv")

            if "Penjumlahan" in jenis_op:
                unc = math.sqrt(dx_val**2 + dy_val**2)
                tampilkan_hasil("Ketidakpastian Akhir", f"± {unc:.5g}")
                st.markdown(tampilkan_kotak("δz = √(δx² + δy²)",
                    buat_baris(f"δz = √({dx_val}² + {dy_val}²) = √({dx_val**2:.5f} + {dy_val**2:.5f})") +
                    buat_baris(f"δz = <b>± {unc:.5g}</b>")
                ), unsafe_allow_html=True)
            else:
                z_val = x_val * y_val
                unc   = z_val * math.sqrt((dx_val/x_val)**2 + (dy_val/y_val)**2)
                tampilkan_hasil("Ketidakpastian Akhir", f"± {unc:.5g}")
                st.markdown(tampilkan_kotak("δz/z = √((δx/x)² + (δy/y)²)",
                    buat_baris(f"z = {x_val} × {y_val} = {z_val}") +
                    buat_baris(f"δz = {z_val} × √(({dx_val}/{x_val})² + ({dy_val}/{y_val})²)") +
                    buat_baris(f"δz = <b>± {unc:.5g}</b>")
                ), unsafe_allow_html=True)

        with tab_stat:
            keterangan("SD")
            keterangan("RSD")
            teks_data = st.text_area("Data pengukuran (pisahkan dengan koma):",
                               value="9.87, 9.92, 9.85, 9.90, 9.88", key="data_stat")
            angka_data = []
            for tok in teks_data.split(','):
                tok = tok.strip()
                if tok:
                    try:
                        angka_data.append(float(tok))
                    except ValueError:
                        pass

            if len(angka_data) >= 2:
                rata2 = sum(angka_data) / len(angka_data)
                sd    = math.sqrt(sum((x - rata2)**2 for x in angka_data) / (len(angka_data) - 1))
                rsd   = (sd / rata2) * 100
                tampilkan_hasil("Rata-rata ± SD", f"{rata2:.4g} ± {sd:.4g}", f"(RSD: {rsd:.3f}%)")
                st.markdown(tampilkan_kotak("Statistik Deskriptif",
                    buat_baris(f"n = {len(angka_data)} data") +
                    buat_baris(f"Rata-rata (μ) = Σx / n = <b>{rata2:.4g}</b>") +
                    buat_baris(f"SD = √(Σ(xᵢ-μ)² / (n-1)) = <b>{sd:.4g}</b>") +
                    buat_baris(f"RSD = (SD/μ) × 100% = <b>{rsd:.3f}%</b>")
                ), unsafe_allow_html=True)


st.divider()
st.markdown(
    '<p style="text-align:center; font-size:12px; color:#9e9e9e;">⚗️ Kalkulator Analisis Kuantitatif · Kimia Analitik · Anisa · Rahma · Wewing · Abum</p>',
    unsafe_allow_html=True
)
