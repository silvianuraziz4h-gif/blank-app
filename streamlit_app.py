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
    "Asam salisilat (C⇋H₆O₃)":           138.12,
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

# styling custom (Bekerja adaptif dan jelas di dark maupun light mode)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600&family=Space+Mono:wght@400;700&display=swap');

/* ===== BASE / DARK MODE ===== */
html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; }

.stApp {
    background: #1a1a2e !important;
    background-image: radial-gradient(ellipse at top left, #16213e 0%, #1a1a2e 60%, #0f3460 100%) !important;
    background-attachment: fixed;
}

/* Teks dan judul bertema dark */
.main-title { font-size: 38px; font-weight: 600; line-height: 1.2; color: #e8e8e8; margin: 0 0 .4rem; }
.main-title em { font-style: normal; color: #e8a045; }
.subtitle { font-size: 14px; color: #8aa0c0; line-height: 1.6; max-width: 560px; margin-bottom: 1.5rem; }

/* Input fields dark */
div[data-testid="stNumberInput"] input,
div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea {
    color: #1a1a2e !important;
    background: #d8e4f0 !important;
    font-weight: 600 !important;
}
div[data-baseweb="select"] div { color: #1a1a2e !important; font-weight: 600 !important; }
div[data-shaded="true"], ul[role="listbox"] li { color: #1a1a2e !important; }

/* Tabs dark */
button[data-baseweb="tab"] p { color: #aaa !important; }
button[data-baseweb="tab"][aria-selected="true"] p {
    color: #e8a045 !important;
    font-weight: 700 !important;
}

/* ===== LIGHT MODE ===== */
@media (prefers-color-scheme: light) {
    .stApp {
        background: #eef2f7 !important;
        background-image: radial-gradient(ellipse at top, #dce8f5 0%, #eef2f7 60%, #e0eaf5 100%) !important;
    }

    div[data-testid="stNumberInput"] input,
    div[data-testid="stTextInput"] input,
    div[data-testid="stTextArea"] textarea {
        color: #0d1a33 !important;
        background: #fff !important;
        font-weight: 600 !important;
    }
    div[data-baseweb="select"] div { color: #0d1a33 !important; }
    div[data-shaded="true"], ul[role="listbox"] li { color: #0d1a33 !important; }

    button[data-baseweb="tab"] p { color: #557 !important; }
    button[data-baseweb="tab"][aria-selected="true"] p { color: #b37010 !important; }

    .main-title { color: #0d1a33 !important; }
    .main-title em { color: #b37010 !important; }
    .subtitle { color: #3a4a6a !important; }
    .badge { color: #b37010 !important; border-color: #b37010 !important; background: rgba(180,120,20,0.10) !important; }
    .formula-box { color: #7a4e00 !important; background: rgba(180,120,20,0.09) !important; border-color: rgba(180,120,20,0.45) !important; }

    .identitas-box { background: linear-gradient(135deg, #2a4080, #1a2e6a) !important; border-color: rgba(232,160,69,0.6) !important; }
    .identitas-title { color: #f8d48a !important; }
    .identitas-name { color: #e8f0ff !important; }

    .welcome-outer { background: #f0f5ff !important; border-color: #c0cce0 !important; }
    .welcome-header { background: linear-gradient(135deg, #1a3a7a, #0f2460) !important; }
    .welcome-body { color: #2a3a5a !important; }
    .welcome-desc { color: #2a3a5a !important; }

    .info-card { background: #dce8f7 !important; border-color: #b0c8e0 !important; }
    .info-card h4 { color: #b37010 !important; }
    .info-card ul { color: #1a2744 !important; }

    .menu-card { background: #dce8f7 !important; border-color: #b0c8e0 !important; }
    .menu-card:hover { background: #ccdaee !important; }
    .menu-title { color: #0d1a33 !important; }
    .menu-desc { color: #3a4a6a !important; }

    .result-card { background: rgba(180,120,20,0.10) !important; border-color: rgba(180,120,20,0.4) !important; }
    .result-label { color: #3a4a6a !important; }
    .result-value { color: #7a4e00 !important; }

    .istilah-box { background: #d0e8fa !important; border-color: #2980b9 !important; border-left-color: #1a6fa0 !important; color: #0a2a4a !important; }
    .istilah-box b { color: #0a2a4a !important; }

    div[data-testid="stNumberInput"],
    div[data-testid="stSelectbox"],
    div[data-testid="stTextInput"],
    div[data-testid="stTextArea"] { background: rgba(0,30,80,0.05) !important; }
}

/* ===== SHARED COMPONENTS ===== */
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
    background: rgba(232,160,69,0.10);
}

.formula-box {
    background: rgba(232,160,69,0.08);
    border: 1px solid rgba(232,160,69,0.5);
    border-radius: 8px;
    padding: 10px 16px;
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    color: #f0c070;
    text-align: center;
    margin: 1rem 0;
}

/* ===== IDENTITAS TIM ===== */
.identitas-box {
    max-width: 420px;
    margin: 1.2rem auto 1.5rem;
    background: linear-gradient(135deg, #0f2a60, #1a1a3e);
    border: 1.5px solid rgba(232,160,69,0.5);
    border-radius: 14px;
    padding: 1.4rem 2rem 1.6rem;
    text-align: center;
    box-shadow: 0 4px 20px rgba(0,0,0,0.35);
}
.identitas-title {
    font-size: 11px;
    font-family: 'Space Mono', monospace;
    text-transform: uppercase;
    letter-spacing: .14em;
    color: #e8a045;
    margin-bottom: 1rem;
}
.identitas-divider {
    width: 40px;
    height: 2px;
    background: linear-gradient(90deg, transparent, #e8a045, transparent);
    margin: 0.5rem auto 1rem;
}
.identitas-name {
    font-size: 15px;
    font-weight: 500;
    color: #d8e8ff;
    line-height: 2;
    letter-spacing: 0.03em;
}

/* ===== KETERANGAN ISTILAH ===== */
.istilah-box {
    background: rgba(52,152,219,0.12);
    border: 1px solid rgba(52,152,219,0.40);
    border-left: 4px solid #3498db;
    border-radius: 6px;
    padding: 10px 14px;
    font-size: 12.5px;
    color: #a8d4f0;
    margin: 0.5rem 0 1rem;
    line-height: 1.7;
}

/* ===== WELCOME PAGE ===== */
.welcome-outer {
    max-width: 680px;
    margin: 2rem auto 2rem;
    background: rgba(255,255,255,0.03);
    border-radius: 18px;
    overflow: hidden;
    border: 1px solid rgba(232,160,69,0.25);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}
.welcome-header {
    background: linear-gradient(135deg, #0f3460, #16213e);
    padding: 2.5rem;
    text-align: center;
    border-bottom: 2px solid #e8a045;
}
.welcome-header h1 { font-size: 34px; font-weight: 600; margin: 0; color: #f0f0f0; }
.welcome-body { padding: 1.8rem 2rem; text-align: center; }
.welcome-desc { font-size: 16px; line-height: 1.6; color: #b0c8e0; margin: 0 auto; max-width: 500px; }

/* ===== INFO CARDS ===== */
.info-card {
    background: rgba(30,50,90,0.5);
    border-radius: 12px;
    padding: 1.4rem;
    height: 100%;
    border: 1px solid rgba(100,140,200,0.25);
    border-top: 4px solid #e8a045;
}
.info-card h4 { margin-top: 0; font-size: 15px; margin-bottom: 0.6rem; color: #e8a045; }
.info-card ul { margin: 0; padding-left: 1.2rem; font-size: 13.5px; color: #b0c8e0; line-height: 1.8; }

/* ===== MENU CARDS ===== */
.menu-card {
    background: rgba(30,50,90,0.45);
    border-radius: 10px;
    padding: 1.4rem;
    min-height: 180px;
    border: 1px solid rgba(100,140,200,0.20);
    transition: background 0.2s ease, transform 0.15s ease;
}
.menu-card:hover { background: rgba(40,70,120,0.65); transform: translateY(-2px); }
.card-p1 { border-left: 4px solid #e8a045; }
.card-p2 { border-left: 4px solid #4fc3f7; }
.card-p3 { border-left: 4px solid #81c784; }
.card-p4 { border-left: 4px solid #ce93d8; }
.card-p5 { border-left: 4px solid #ef9a9a; }
.menu-icon  { font-size: 22px; margin-bottom: 0.4rem; }
.menu-title { font-size: 15px; font-weight: 600; margin: 0.2rem 0 0.4rem; color: #d8e8ff; }
.menu-desc  { font-size: 12px; color: #8aa0c0; line-height: 1.5; }

/* ===== BUTTON ===== */
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
div.stButton > button:hover { opacity: 0.85; }

/* ===== RESULT CARD ===== */
.result-card {
    background: rgba(232,160,69,0.09);
    border-radius: 10px;
    padding: 1rem 1.4rem;
    margin-top: .75rem;
    border: 1px solid rgba(232,160,69,0.35);
}
.result-label {
    font-size: 10px;
    font-family: 'Space Mono', monospace;
    text-transform: uppercase;
    letter-spacing: .1em;
    margin: 0 0 4px;
    color: #8aa0c0;
}
.result-value {
    font-size: 24px;
    font-weight: 600;
    margin: 0;
    font-family: 'Space Mono', monospace;
    color: #f0c070;
}

/* ===== INPUT CONTAINERS ===== */
div[data-testid="stNumberInput"],
div[data-testid="stSelectbox"],
div[data-testid="stTextInput"],
div[data-testid="stTextArea"] {
    background-color: rgba(20,40,80,0.35) !important;
    border-radius: 6px !important;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# KOMPONEN IDENTITAS TIM
# ============================================================
def tampilkan_identitas():
    st.markdown("""
    <div class="identitas-box">
        <div class="identitas-title">👥 Tim Penyusun</div>
        <div class="identitas-divider"></div>
        <div class="identitas-name">1. &nbsp; Anisa</div>
        <div class="identitas-name">2. &nbsp; Rahma</div>
        <div class="identitas-name">3. &nbsp; Wewing</div>
        <div class="identitas-name">4. &nbsp; Abum</div>
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
# FUNGSI TAMPILAN UMUM (Menggunakan properti warna adaptif)
# ============================================================
def tampilkan_kotak(judul, konten_html):
    return f"""
    <div style="background: var(--background-color, rgba(30,55,100,0.15)); padding:20px; border-radius:10px;
                border:1px dashed #e8a045; font-family:'Courier New',monospace; margin-top:15px;">
        <p style="margin:0 0 12px 0; color:#e8a045; font-weight:600; font-size:13px;">📋 {judul}</p>
        <div style="font-size:13px; color: var(--text-color, inherit); line-height:1.7; padding-left:5px;">
            {konten_html}
        </div>
    </div>
    """

def buat_baris(teks):
    return f"<p style='margin:0 0 8px 0; color: inherit;'>{teks}</p>"

def tampilkan_hasil(nama_variabel, angka, satuan=""):
    sat_html = f'<span style="font-size:15px; color:#e8a045; opacity:0.85;">{satuan}</span>' if satuan else ""
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
        st.markdown("### 💧 Pengenceran Larutan")
        tab_cv, tab_serial, tab_fp = st.tabs(["C₁V₁ = C₂V₂", "Serial / Bertingkat", "Faktor Pengenceran"])

        with tab_cv:
            st.markdown('<div class="formula-box">C₁ × V₁ = C₂ × V₂</div>', unsafe_allow_html=True)
            keterangan("Molaritas")
            yang_dicari = st.selectbox("Variabel yang dicari:", [
                "C₂ — Konsentrasi akhir",
                "V₂ — Volume akhir",
                "C₁ — Konsentrasi awal",
                "V₁ — Volume awal"
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
                tampilkan_hasil("V₂ — Volume akhir", f"{jawaban:.4f}", "mL")
                st.markdown(tampilkan_kotak("Penyelesaian (V₂ = C₁V₁ / C₂)",
                    buat_baris(f"V₂ = ({c1} × {v1}) / {c2}") +
                    buat_baris(f"V₂ = <b>{jawaban:.4f} mL</b>") +
                    buat_baris(f"Volume air penambah = V₂ - V₁ = {jawaban - v1:.4f} mL")
                ), unsafe_allow_html=True)

            elif yang_dicari == "C₁ — Konsentrasi awal":
                with col1:
                    c2 = st.number_input("C₂", 0.0, value=0.1, format="%.5f", key="c2_c1")
                    v2 = st.number_input("V₂ (mL)", 0.0, value=100.0, format="%.3f", key="v2_c1")
                with col2:
                    v1 = st.number_input("V₁ (mL)", 1e-9, value=10.0, format="%.3f", key="v1_c1")
                jawaban = (c2 * v2) / v1
                tampilkan_hasil("C₁ — Konsentrasi awal", f"{jawaban:.6g}", satuan)
                st.markdown(tampilkan_kotak("Penyelesaian (C₁ = C₂V₂ / V₁)",
                    buat_baris(f"C₁ = ({c2} × {v2}) / {v1}") +
                    buat_baris(f"C₁ = <b>{jawaban:.6g} {satuan}</b>")
                ), unsafe_allow_html=True)

            elif yang_dicari == "V₁ — Volume awal":
                with col1:
                    c2 = st.number_input("C₂", 0.0, value=0.1, format="%.5f", key="c2_v1")
                    v2 = st.number_input("V₂ (mL)", 0.0, value=100.0, format="%.3f", key="v2_v1")
                with col2:
                    c1 = st.number_input("C₁", 1e-9, value=1.0, format="%.5f", key="c1_v1")
                jawaban = (c2 * v2) / c1
                tampilkan_hasil("V₁ — Volume awal (Pipet)", f"{jawaban:.4f}", "mL")
                st.markdown(tampilkan_kotak("Penyelesaian (V₁ = C₂V₂ / C₁)",
                    buat_baris(f"V₁ = ({c2} × {v2}) / {c1}") +
                    buat_baris(f"V₁ = <b>{jawaban:.4f} mL</b>") +
                    buat_baris(f"Ambil {jawaban:.4f} mL larutan pekat, encerkan sampai wadah {v2} mL.")
                ), unsafe_allow_html=True)

        with tab_serial:
            st.markdown('<div class="formula-box">Faktor Tiap Tahap = V_total / V_pindah</div>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                c_awal = st.number_input("Konsentrasi awal Induk:", 0.0, value=1000.0, key="ser_c")
                v_pindah = st.number_input("Volume yang dipindahkan (mL):", 0.001, value=1.0, key="ser_vp")
                v_labu = st.number_input("Volume Labu Takar tujuan (mL):", 0.001, value=10.0, key="ser_vl")
            with col2:
                jumlah_tahap = st.number_input("Jumlah tahap pengenceran seris:", 1, 10, value=3, key="ser_n")
                satuan_seris = st.selectbox("Satuan:", ["ppm", "ppb", "M", "mg/L"], key="ser_sat")

            faktor_tahap = v_labu / v_pindah
            st.write("##### Hasil Konsentrasi Tiap Tabung:")
            html_tahap = ""
            c_sekarang = c_awal
            for i in range(int(jumlah_tahap)):
                c_sekarang /= faktor_tahap
                st.write(f"Tabung {i+1} : **{c_sekarang:.5g} {satuan_seris}**")
                html_tahap += buat_baris(f"Tahap {i+1}: {c_sekarang*faktor_tahap:.4g} / {faktor_tahap:.3g} = <b>{c_sekarang:.5g}</b>")

            st.markdown(tampilkan_kotak("Langkah Pengenceran Bertingkat",
                buat_baris(f"Faktor pengenceran per tabung = {v_labu} mL / {v_pindah} mL = <b>{faktor_tahap:.4g}x</b>") +
                buat_baris(f"Total pengenceran akhir = {faktor_tahap**jumlah_tahap:.5g}x") + html_tahap
            ), unsafe_allow_html=True)

        with tab_fp:
            st.markdown('<div class="formula-box">FP = V_akhir / V_awal &nbsp;|&nbsp; Kadar Sampel = Kadar Terukur × FP</div>', unsafe_allow_html=True)
            keterangan("Faktor pengenceran")
            col1, col2 = st.columns(2)
            with col1:
                v_awal_fp = st.number_input("Volume sampel dipipet (mL):", 0.001, value=2.0, key="fp_v1")
                v_akhir_fp = st.number_input("Volume akhir pengenceran (mL):", 0.001, value=50.0, key="fp_v2")
            with col2:
                kadar_terukur = st.number_input("Konsentrasi terukur instrumen:", 0.0, value=5.4, format="%.4f", key="fp_c")
                sat_fp = st.selectbox("Satuan konsentrasi:", ["ppm", "ppb", "mg/L", "M"], key="fp_sat")

            fp = v_akhir_fp / v_awal_fp
            kadar_asli = kadar_terukur * fp
            tampilkan_hasil("Faktor Pengenceran (FP)", f"{fp:.4g}", "kali")
            tampilkan_hasil("Kadar Sampel Asli", f"{kadar_asli:.6g}", sat_fp)
            st.markdown(tampilkan_kotak("Perhitungan Faktor Pengenceran",
                buat_baris(f"FP = {v_akhir_fp} mL / {v_awal_fp} mL = <b>{fp:.4g}</b>") +
                buat_baris(f"Kadar asli = {kadar_terukur} × {fp} = <b>{kadar_asli:.6g} {sat_fp}</b>")
            ), unsafe_allow_html=True)

    # ----------------------------------------------------------
    # STOIKIOMETRI
    # ----------------------------------------------------------
    elif st.session_state.menu_aktif == "Stoikiometri":
        st.markdown("### 🔄 Konsentrasi & Stoikiometri")
        tab_konv, tab_reaksi = st.tabs(["Konversi Satuan Larutan", "Stoikiometri Mol Reaksi"])

        with tab_konv:
            st.write("##### Konversi Molaritas ke ppm / sebaliknya")
            mr_pilih, unsur_nama = pilih_mr("Zat Terlarut", "stoik")
            pilihan_arah = st.radio("Pilih jenis konversi:", [
                "Molaritas (M) ➔ ppm (mg/L)",
                "ppm (mg/L) ➔ Molaritas (M)"
            ], horizontal=True)

            if pilihan_arah == "Molaritas (M) ➔ ppm (mg/L)":
                m_in = st.number_input("Konsentrasi Molaritas (M):", 0.0, value=0.01, format="%.6f", key="m_in")
                ppm_out = m_in * mr_pilih * 1000
                tampilkan_hasil("Hasil Konsentrasi", f"{ppm_out:.5g}", "ppm (mg/L)")
                st.markdown(tampilkan_kotak("Rumus: ppm = M × Mr × 1000",
                    buat_baris(f"ppm = {m_in} M × {mr_pilih} g/mol × 1000") +
                    buat_baris(f"ppm = <b>{ppm_out:.5g} mg/L</b>")
                ), unsafe_allow_html=True)
            else:
                ppm_in = st.number_input("Konsentrasi ppm (mg/L):", 0.0, value=100.0, key="ppm_in")
                m_out = ppm_in / (mr_pilih * 1000)
                tampilkan_hasil("Hasil Molaritas", f"{m_out:.6g}", "M")
                st.markdown(tampilkan_kotak("Rumus: M = ppm / (Mr × 1000)",
                    buat_baris(f"M = {ppm_in} / ({mr_pilih} × 1000)") +
                    buat_baris(f"M = <b>{m_out:.6g} mol/L</b>")
                ), unsafe_allow_html=True)

        with tab_reaksi:
            st.markdown('<div class="formula-box">a A + b B ➔ c C + d D</div>', unsafe_allow_html=True)
            keterangan("Reaktan pembatas")
            st.write("Masukkan koefisien reaksi dan jumlah mol masing-masing reaktan:")
            col1, col2 = st.columns(2)
            with col1:
                st.write("**Reaktan A**")
                koef_a = st.number_input("Koefisien A:", 1, value=1, key="ka")
                mol_a = st.number_input("Mol A yang tersedia:", 0.0, value=0.5, format="%.4f", key="ma")
            with col2:
                st.write("**Reaktan B**")
                koef_b = st.number_input("Koefisien B:", 1, value=2, key="kb")
                mol_b = st.number_input("Mol B yang tersedia:", 0.0, value=0.8, format="%.4f", key="mb")

            if mol_a > 0 and mol_b > 0:
                uji_a = mol_a / koef_a
                uji_b = mol_b / koef_b
                if uji_a < uji_b:
                    pembatas = "A"
                    mol_bereaksi_a = mol_a
                    mol_bereaksi_b = mol_a * koef_b / koef_a
                elif uji_b < uji_a:
                    pembatas = "B"
                    mol_bereaksi_b = mol_b
                    mol_bereaksi_a = mol_b * koef_a / koef_b
                else:
                    pembatas = "Kedua reaktan habis bersamaan (Ekuivalen)"
                    mol_bereaksi_a = mol_a
                    mol_bereaksi_b = mol_b

                tampilkan_hasil("Pereaksi Pembatas", pembatas)
                st.markdown(tampilkan_kotak("Analisis Pembatas Reaksi",
                    buat_baris(f"Uji rasio mol/koefisien A = {mol_a}/{koef_a} = <b>{uji_a:.4g}</b>") +
                    buat_baris(f"Uji rasio mol/koefisien B = {mol_b}/{koef_b} = <b>{uji_b:.4g}</b>") +
                    buat_baris(f"Zat pembatas diambil dari rasio terkecil yaitu reaktan <b>{pembatas}</b>.") +
                    buat_baris(f"Mol B yang ikut bereaksi = <b>{mol_bereaksi_b:.4g} mol</b>") +
                    buat_baris(f"Sisa reaktan B berlebih = {mol_b - mol_bereaksi_b:.4g} mol")
                ), unsafe_allow_html=True)

    # ----------------------------------------------------------
    # pH KESETIMBANGAN
    # ----------------------------------------------------------
    elif st.session_state.menu_aktif == "pH":
        st.markdown("### 🌈 Kesetimbangan & pH")
        jenis_zat = st.radio("Sifat Larutan:", ["Asam Kuat", "Basa Kuat", "Asam Lemah", "Basa Lemah"], horizontal=True)

        if jenis_zat == "Asam Kuat":
            st.markdown('<div class="formula-box">[H⁺] = Valensi × M &nbsp;|&nbsp; pH = -log[H⁺]</div>', unsafe_allow_html=True)
            m = st.number_input("Molaritas Asam (M):", 1e-9, value=0.05, format="%.5f", key="ak_m")
            val = st.number_input("Valensi asam (jumlah H⁺):", 1, 4, value=1, key="ak_v")
            h_pos = val * m
            ph = -math.log10(h_pos) if h_pos > 0 else 7
            tampilkan_hasil("pH Larutan", f"{ph:.3f}")
            st.markdown(tampilkan_kotak("Penyelesaian Asam Kuat",
                buat_baris(f"[H⁺] = {val} × {m} M = <b>{h_pos:.5g} M</b>") +
                buat_baris(f"pH = -log({h_pos:.5g}) = <b>{ph:.3f}</b>")
            ), unsafe_allow_html=True)

        elif jenis_zat == "Basa Kuat":
            st.markdown('<div class="formula-box">[OH⁻] = Valensi × M &nbsp;|&nbsp; pOH = -log[OH⁻] &nbsp;|&nbsp; pH = 14 - pOH</div>', unsafe_allow_html=True)
            m = st.number_input("Molaritas Basa (M):", 1e-9, value=0.02, format="%.5f", key="bk_m")
            val = st.number_input("Valensi basa (jumlah OH⁻):", 1, 4, value=1, key="bk_v")
            oh_neg = val * m
            poh = -math.log10(oh_neg) if oh_neg > 0 else 7
            ph = 14 - poh
            tampilkan_hasil("pH Larutan", f"{ph:.3f}")
            st.markdown(tampilkan_kotak("Penyelesaian Basa Kuat",
                buat_baris(f"[OH⁻] = {val} × {m} M = <b>{oh_neg:.5g} M</b>") +
                buat_baris(f"pOH = -log({oh_neg:.5g}) = <b>{poh:.3f}</b>") +
                buat_baris(f"pH = 14 - {poh:.3f} = <b>{ph:.3f}</b>")
            ), unsafe_allow_html=True)

        elif jenis_zat == "Asam Lemah":
            st.markdown('<div class="formula-box">[H⁺] = √(Ka × M) &nbsp;|&nbsp; pH = -log[H⁺]</div>', unsafe_allow_html=True)
            keterangan("Ka")
            m = st.number_input("Molaritas Asam Lemah (M):", 1e-9, value=0.1, format="%.5f", key="al_m")
            ka = st.number_input("Tetapan asam (Ka):", 1e-15, value=1.8e-5, format="%.2e", key="al_ka")
            h_pos = math.sqrt(ka * m)
            ph = -math.log10(h_pos) if h_pos > 0 else 7
            tampilkan_hasil("pH Larutan", f"{ph:.3f}")
            st.markdown(tampilkan_kotak("Penyelesaian Asam Lemah",
                buat_baris(f"[H⁺] = √({ka} × {m}) = <b>{h_pos:.5e} M</b>") +
                buat_baris(f"pH = -log({h_pos:.5e}) = <b>{ph:.3f}</b>")
            ), unsafe_allow_html=True)

        elif jenis_zat == "Basa Lemah":
            st.markdown('<div class="formula-box">[OH⁻] = √(Kb × M) &nbsp;|&nbsp; pH = 14 - (-log[OH⁻])</div>', unsafe_allow_html=True)
            keterangan("Kb")
            m = st.number_input("Molaritas Basa Lemah (M):", 1e-9, value=0.1, format="%.5f", key="bl_m")
            kb = st.number_input("Tetapan basa (Kb):", 1e-15, value=1.8e-5, format="%.2e", key="bl_kb")
            oh_neg = math.sqrt(kb * m)
            poh = -math.log10(oh_neg) if oh_neg > 0 else 7
            ph = 14 - poh
            tampilkan_hasil("pH Larutan", f"{ph:.3f}")
            st.markdown(tampilkan_kotak("Penyelesaian Basa Lemah",
                buat_baris(f"[OH⁻] = √({kb} × {m}) = <b>{oh_neg:.5e} M</b>") +
                buat_baris(f"pOH = -log({oh_neg:.5e}) = <b>{poh:.3f}</b>") +
                buat_baris(f"pH = 14 - {poh:.3f} = <b>{ph:.3f}</b>")
            ), unsafe_allow_html=True)

    # ----------------------------------------------------------
    # LARUTAN BUFFER
    # ----------------------------------------------------------
    elif st.session_state.menu_aktif == "Buffer":
        st.markdown("### 🧪 Larutan Buffer")
        st.markdown('<div class="formula-box">pH = pKa + log(Mol Garam / Mol Asam Weak)</div>', unsafe_allow_html=True)
        keterangan("Henderson")
        col1, col2 = st.columns(2)
        with col1:
            ka = st.number_input("Tetapan Asam Lemah (Ka):", 1e-14, value=1.8e-5, format="%.2e", key="buf_ka")
            mol_asam = st.number_input("Jumlah Mol Asam Lemah:", 1e-9, value=0.05, format="%.4f", key="buf_ma")
        with col2:
            mol_garam = st.number_input("Jumlah Mol Garam / Basa Konjugasi:", 1e-9, value=0.05, format="%.4f", key="buf_mg")

        pka = -math.log10(ka)
        ph_buffer = pka + math.log10(mol_garam / mol_asam)
        tampilkan_hasil("pH Buffer Terbentuk", f"{ph_buffer:.3f}")
        st.markdown(tampilkan_kotak("Perhitungan Nilai Keseimbangan Penyangga",
            buat_baris(f"pKa = -log({ka}) = <b>{pka:.3f}</b>") +
            buat_baris(f"Rasio log(garam/asam) = log({mol_garam}/{mol_asam}) = <b>{math.log10(mol_garam/mol_asam):.4f}</b>") +
            buat_baris(f"pH = {pka:.3f} + ({math.log10(mol_garam/mol_asam):.4f}) = <b>{ph_buffer:.3f}</b>")
        ), unsafe_allow_html=True)

    # ----------------------------------------------------------
    # GALAT & PROPAGASI
    # ----------------------------------------------------------
    elif st.session_state.menu_aktif == "Galat":
        st.markdown("### 📊 Galat & Propagasi Ketidakpastian")
        tab_stat, tab_prop = st.tabs(["Statistik Deskriptif (SD & RSD)", "Propagasi Nilai"])

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
                st.markdown(st.markdown(tampilkan_kotak("Statistik Deskriptif",
                    buat_baris(f"n = {len(angka_data)} data") +
                    buat_baris(f"Rata-rata (μ) = Σx / n = <b>{rata2:.4g}</b>") +
                    buat_baris(f"SD = √(Σ(xᵢ-μ)² / (n-1)) = <b>{sd:.4g}</b>") +
                    buat_baris(f"RSD = (SD / μ) × 100% = <b>{rsd:.3f}%</b>")
                ), unsafe_allow_html=True))
            else:
                st.warning("Masukkan minimal 2 angka yang dipisahkan koma untuk memproses nilai presisi.")
