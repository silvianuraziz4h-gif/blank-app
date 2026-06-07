import streamlit as st
import math

st.set_page_config(
    page_title="Kalkulator Kimia Analitik",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600&family=Space+Mono:wght@400;700&display=swap');

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


# ---------- state ----------
if 'menu_aktif' not in st.session_state:
    st.session_state.menu_aktif = "Start"

SATUAN_KONSENTRASI = ["Molaritas (M)", "% massa/volume (% m/v)", "ppm (mg/L)", "ppb (µg/L)", "mg/mL", "Molalitas (m)"]


# ---------- helper: kotak penyelesaian ----------
def kotak(judul, isi_html):
    return f"""
    <div style="background:rgba(255,255,255,0.04); padding:20px; border-radius:10px;
                border:1px dashed rgba(232,160,69,0.4); font-family:'Courier New',monospace; margin-top:15px;">
        <p style="margin:0 0 12px 0; color:#e8a045; font-weight:600; font-size:13px;">📋 {judul}</p>
        <div style="font-size:13px; color:#cfcfcf; line-height:1.7; padding-left:5px;">
            {isi_html}
        </div>
    </div>
    """

def baris(teks):
    return f"<p style='margin:0 0 8px 0;'>{teks}</p>"

def hasil_card(label, nilai, satuan=""):
    satuan_html = f'<span style="font-size:16px; color:#e8a045;">{satuan}</span>' if satuan else ""
    st.markdown(
        f'<div class="result-card">'
        f'<p class="result-label">{label}</p>'
        f'<p class="result-value">{nilai} {satuan_html}</p>'
        f'</div>',
        unsafe_allow_html=True
    )


# =============================================================
# HALAMAN START
# =============================================================
if st.session_state.menu_aktif == "Start":
    st.markdown("""
    <div class="welcome-outer">
        <div class="welcome-header"><h1>Selamat Datang 👋</h1></div>
        <div class="welcome-body">
            <p class="welcome-desc">Aplikasi Kalkulator Kimia Analitik Kuantitatif</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    _, col_btn, _ = st.columns([1.2, 1, 1.2])
    with col_btn:
        if st.button("Masuk ke Aplikasi →", key="btn_start", use_container_width=True):
            st.session_state.menu_aktif = "Dashboard"
            st.rerun()

    st.write("<br><br>", unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class="info-card">
            <h4>🎯 Tujuan Aplikasi</h4>
            <ul>
                <li>Menyediakan platform hitung laboratorium yang mudah dipahami.</li>
                <li>Mengecek kekeliruan pengerjaan angka desimal berkat otomasi kalkulasi analitis.</li>
            </ul>
        </div>""", unsafe_allow_html=True)
    with col_b:
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
    modul_info = [
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
    for col_var, card_cls, ikon, judul, desk, menu, btn_key in modul_info:
        with eval(col_var):
            st.markdown(
                f'<div class="menu-card {card_cls}">'
                f'<div class="menu-icon">{ikon}</div>'
                f'<div class="menu-title">{judul}</div>'
                f'<div class="menu-desc">{desk}</div>'
                f'</div>',
                unsafe_allow_html=True
            )
            if st.button(f"Buka Modul →", key=btn_key, use_container_width=True):
                st.session_state.menu_aktif = menu
                st.rerun()

    st.write("")
    col4, col5, _ = st.columns(3)
    modul_bawah = [
        (col4, "card-p4", "🧪", "Larutan Buffer",
         "Desain sistem penyangga menggunakan persamaan Henderson-Hasselbalch.",
         "Buffer", "btn_m4"),
        (col5, "card-p5", "📊", "Galat & Propagasi",
         "Hitung ketidakpastian, deviasi standar (SD), dan nilai RSD data pengukuran.",
         "Galat", "btn_m5"),
    ]
    for col_var, card_cls, ikon, judul, desk, menu, btn_key in modul_bawah:
        with col_var:
            st.markdown(
                f'<div class="menu-card {card_cls}">'
                f'<div class="menu-icon">{ikon}</div>'
                f'<div class="menu-title">{judul}</div>'
                f'<div class="menu-desc">{desk}</div>'
                f'</div>',
                unsafe_allow_html=True
            )
            if st.button("Buka Modul →", key=btn_key, use_container_width=True):
                st.session_state.menu_aktif = menu
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
    # MODUL 1: PENGENCERAN
    # ----------------------------------------------------------
    if st.session_state.menu_aktif == "Pengenceran":
        st.markdown("### 💧 Pengenceran Larutan")
        tab_cv, tab_serial, tab_fp = st.tabs(["C₁V₁ = C₂V₂", "Serial / Bertingkat", "Faktor Pengenceran"])

        with tab_cv:
            st.markdown('<div class="formula-box">C₁ × V₁ = C₂ × V₂</div>', unsafe_allow_html=True)
            cari   = st.selectbox("Variabel yang dicari:", [
                "C₂ — Konsentrasi akhir", "V₂ — Volume akhir",
                "C₁ — Konsentrasi awal",  "V₁ — Volume awal"
            ], key="cari_cv")
            satuan = st.selectbox("Satuan konsentrasi:", ["M", "mM", "µM", "mg/mL", "ppm", "ppb"], key="satuan_cv")
            col1, col2 = st.columns(2)

            if cari == "C₂ — Konsentrasi akhir":
                with col1:
                    c1 = st.number_input("C₁", 0.0, value=1.0, format="%.5f", key="c1_c2")
                    v1 = st.number_input("V₁ (mL)", 0.0, value=10.0, format="%.3f", key="v1_c2")
                with col2:
                    v2 = st.number_input("V₂ (mL)", 1e-9, value=100.0, format="%.3f", key="v2_c2")
                hasil = (c1 * v1) / v2
                hasil_card("C₂ — Konsentrasi akhir", f"{hasil:.6g}", satuan)
                st.markdown(kotak("Penyelesaian (C₂ = C₁V₁ / V₂)",
                    baris(f"C₂ = ({c1} × {v1}) / {v2}") +
                    baris(f"C₂ = <b>{hasil:.6g} {satuan}</b>")
                ), unsafe_allow_html=True)

            elif cari == "V₂ — Volume akhir":
                with col1:
                    c1 = st.number_input("C₁", 0.0, value=1.0, format="%.5f", key="c1_v2")
                    v1 = st.number_input("V₁ (mL)", 0.0, value=10.0, format="%.3f", key="v1_v2")
                with col2:
                    c2 = st.number_input("C₂", 1e-9, value=0.1, format="%.5f", key="c2_v2")
                hasil = (c1 * v1) / c2
                hasil_card("V₂ — Volume akhir", f"{hasil:.5g}", "mL")
                st.markdown(kotak("Penyelesaian (V₂ = C₁V₁ / C₂)",
                    baris(f"V₂ = ({c1} × {v1}) / {c2}") +
                    baris(f"V₂ = <b>{hasil:.5g} mL</b>")
                ), unsafe_allow_html=True)

            elif cari == "C₁ — Konsentrasi awal":
                with col1:
                    v1 = st.number_input("V₁ (mL)", 1e-9, value=10.0, format="%.3f", key="v1_c1")
                    c2 = st.number_input("C₂", 0.0, value=0.1, format="%.5f", key="c2_c1")
                with col2:
                    v2 = st.number_input("V₂ (mL)", 1e-9, value=100.0, format="%.3f", key="v2_c1")
                hasil = (c2 * v2) / v1
                hasil_card("C₁ — Konsentrasi awal", f"{hasil:.6g}", satuan)
                st.markdown(kotak("Penyelesaian (C₁ = C₂V₂ / V₁)",
                    baris(f"C₁ = ({c2} × {v2}) / {v1}") +
                    baris(f"C₁ = <b>{hasil:.6g} {satuan}</b>")
                ), unsafe_allow_html=True)

            else:
                with col1:
                    c1 = st.number_input("C₁", 1e-9, value=1.0, format="%.5f", key="c1_v1")
                    c2 = st.number_input("C₂", 0.0, value=0.1, format="%.5f", key="c2_v1")
                with col2:
                    v2 = st.number_input("V₂ (mL)", 1e-9, value=100.0, format="%.3f", key="v2_v1")
                hasil = (c2 * v2) / c1
                hasil_card("V₁ — Volume awal", f"{hasil:.5g}", "mL")
                st.markdown(kotak("Penyelesaian (V₁ = C₂V₂ / C₁)",
                    baris(f"V₁ = ({c2} × {v2}) / {c1}") +
                    baris(f"V₁ = <b>{hasil:.5g} mL</b>")
                ), unsafe_allow_html=True)

        with tab_serial:
            st.markdown('<div class="formula-box">Cₙ = C₀ × (V_aliquot / V_total)ⁿ</div>', unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                c0    = st.number_input("C₀ — Konsentrasi stok", 0.0, value=1.0, format="%.5f", key="s_c0")
                nstep = st.number_input("Jumlah langkah", 1, 15, value=5, key="s_n")
            with col2:
                va_s  = st.number_input("Volume aliquot (mL)", 0.001, value=1.0, format="%.3f", key="s_va")
                vt_s  = st.number_input("Volume total tiap tabung (mL)", 0.001, value=10.0, format="%.3f", key="s_vt")
                sat_s = st.selectbox("Satuan", ["M", "mM", "µM", "mg/mL", "ppm"], key="s_sat")

            if va_s >= vt_s:
                st.warning("Volume aliquot harus lebih kecil dari volume total.")
            else:
                f = va_s / vt_s
                rows = ""
                for i in range(int(nstep) + 1):
                    nama = "Stok" if i == 0 else f"Langkah {i}"
                    kons = c0 * (f ** i)
                    rows += f"""<tr>
                        <td style='padding:6px 10px; border-bottom:1px solid rgba(255,255,255,0.07)'>{nama}</td>
                        <td style='padding:6px 10px; font-family:Space Mono,monospace; color:#e8a045; border-bottom:1px solid rgba(255,255,255,0.07)'>{kons:.4e}</td>
                        <td style='padding:6px 10px; color:#9e9e9e; border-bottom:1px solid rgba(255,255,255,0.07)'>{sat_s}</td>
                    </tr>"""
                st.markdown(f"""
                <table style="width:100%;border-collapse:collapse;border:1px solid rgba(232,160,69,0.2);
                    font-size:13px;margin-top:.5rem;background:rgba(255,255,255,0.03);border-radius:8px;overflow:hidden">
                    <thead><tr style="background:rgba(232,160,69,0.08)">
                        <th style="padding:8px 10px;text-align:left;color:#e8a045">Tabung</th>
                        <th style="padding:8px 10px;text-align:left;color:#e8a045">Konsentrasi</th>
                        <th style="padding:8px 10px;text-align:left;color:#e8a045">Satuan</th>
                    </tr></thead><tbody>{rows}</tbody>
                </table>""", unsafe_allow_html=True)
                st.markdown(kotak("Penyelesaian (Serial)",
                    baris(f"Faktor per tabung = {va_s} / {vt_s} = <b>{f:.4f}</b>") +
                    baris(f"Cₙ = {c0} × ({f:.4f})ⁿ")
                ), unsafe_allow_html=True)

        with tab_fp:
            col1, col2 = st.columns(2)
            with col1:
                va_fp = st.number_input("Volume awal (mL)", 0.001, value=1.0, format="%.3f", key="fp_va")
                vb_fp = st.number_input("Volume akhir (mL)", 0.001, value=100.0, format="%.3f", key="fp_vb")
            with col2:
                ca_fp = st.number_input("Konsentrasi awal (opsional)", 0.0, value=1.0, format="%.5f", key="fp_ca")
            fp = vb_fp / va_fp
            hasil_card("Faktor Pengenceran", f"1 : {fp:.4f}")
            hasil_card("Konsentrasi Akhir", f"{ca_fp / fp:.5g}")
            st.markdown(kotak("Penyelesaian (Faktor Pengenceran)",
                baris(f"FP = {vb_fp} / {va_fp} = <b>{fp:.4f}</b>") +
                baris(f"C akhir = {ca_fp} / {fp:.4f} = <b>{ca_fp / fp:.5g}</b>")
            ), unsafe_allow_html=True)

    # ----------------------------------------------------------
    # MODUL 2: STOIKIOMETRI
    # ----------------------------------------------------------
    elif st.session_state.menu_aktif == "Stoikiometri":
        st.markdown("### 🔄 Satuan Konsentrasi & Stoikiometri")
        tab_konv, tab_mol, tab_reaksi = st.tabs(["🔄 Konversi Satuan", "⚖️ Mol & Massa", "🧮 Stoikiometri Reaksi"])

        with tab_konv:
            col1, col2 = st.columns(2)
            with col1:
                satuan_dari = st.selectbox("Dari satuan:", SATUAN_KONSENTRASI, index=0, key="k_dari")
                nilai       = st.number_input("Nilai", 0.0, value=1.0, format="%.6f", key="k_val")
                mr_k        = st.number_input("Mr zat (g/mol)", 0.001, value=58.44, key="k_mr")
            with col2:
                satuan_ke = st.selectbox("Ke satuan:", SATUAN_KONSENTRASI, index=2, key="k_ke")
                rho       = st.number_input("Densitas ρ (g/mL)", 0.001, value=1.0, key="k_rho")

            if satuan_dari == satuan_ke:
                st.warning("Pilih satuan yang berbeda.")
            else:
                # konversi ke basis mg/L dulu, baru ke target
                konversi_ke_mgL = {
                    "Molaritas (M)":            lambda v: v * mr_k * 1000,
                    "% massa/volume (% m/v)":   lambda v: v * 10000,
                    "ppm (mg/L)":               lambda v: v,
                    "ppb (µg/L)":               lambda v: v / 1000,
                    "mg/mL":                    lambda v: v * 1000,
                    "Molalitas (m)":            lambda v: v * mr_k * rho * 1000,
                }
                konversi_dari_mgL = {
                    "Molaritas (M)":            lambda v: v / (mr_k * 1000),
                    "% massa/volume (% m/v)":   lambda v: v / 10000,
                    "ppm (mg/L)":               lambda v: v,
                    "ppb (µg/L)":               lambda v: v * 1000,
                    "mg/mL":                    lambda v: v / 1000,
                    "Molalitas (m)":            lambda v: v / (mr_k * rho * 1000),
                }
                mgL   = konversi_ke_mgL[satuan_dari](nilai)
                hasil = konversi_dari_mgL[satuan_ke](mgL)
                hasil_card("Hasil Konversi", f"{hasil:.6g}", satuan_ke)
                st.markdown(kotak("Penyelesaian (via basis mg/L)",
                    baris(f"'{satuan_dari}' → mg/L: <b>{mgL:.4e} mg/L</b>") +
                    baris(f"mg/L → '{satuan_ke}': <b>{hasil:.6g} {satuan_ke}</b>") +
                    baris(f"<span style='color:#9e9e9e;font-size:11px'>Mr = {mr_k} g/mol | ρ = {rho} g/mL</span>")
                ), unsafe_allow_html=True)

        with tab_mol:
            pilihan = st.selectbox("Cari:", [
                "Mol (n) dari massa & Mr", "Mol (n) dari M & V",
                "Massa (g) dari n & Mr",   "Molaritas (M) dari n & V",
                "Volume (mL) dari n & M"
            ], key="pilihan_mol")
            col1, col2 = st.columns(2)

            if "massa & Mr" in pilihan:
                with col1: massa = st.number_input("Massa (gram)", 0.0, value=5.85, format="%.4f", key="mol_m")
                with col2: mr    = st.number_input("Mr (g/mol)", 0.001, value=58.44, key="mol_mr")
                hasil = massa / mr
                hasil_card("Mol (n)", f"{hasil:.5g}", "mol")
                st.markdown(kotak("n = gram / Mr",
                    baris(f"n = {massa} / {mr} = <b>{hasil:.5g} mol</b>")
                ), unsafe_allow_html=True)

            elif "M & V" in pilihan:
                with col1: M = st.number_input("Molaritas (M)", 0.0, value=1.0, key="mol_M")
                with col2: V = st.number_input("Volume (mL)", 0.0, value=100.0, key="mol_V")
                hasil = M * (V / 1000)
                hasil_card("Mol (n)", f"{hasil:.5g}", "mol")
                st.markdown(kotak("n = M × (V/1000)",
                    baris(f"n = {M} × ({V}/1000) = <b>{hasil:.5g} mol</b>")
                ), unsafe_allow_html=True)

            elif "Massa" in pilihan:
                with col1: n  = st.number_input("Mol (n)", 0.0, value=0.1, key="mol_n_m")
                with col2: mr = st.number_input("Mr (g/mol)", 0.001, value=58.44, key="mol_mr2")
                hasil = n * mr
                hasil_card("Massa (m)", f"{hasil:.5g}", "gram")
                st.markdown(kotak("gram = n × Mr",
                    baris(f"gram = {n} × {mr} = <b>{hasil:.5g} gram</b>")
                ), unsafe_allow_html=True)

            elif "Molaritas" in pilihan:
                with col1: n = st.number_input("Mol (n)", 0.0, value=0.1, key="mol_n_M")
                with col2: V = st.number_input("Volume (mL)", 0.001, value=100.0, key="mol_V2")
                hasil = n / (V / 1000)
                hasil_card("Molaritas (M)", f"{hasil:.5g}", "mol/L")
                st.markdown(kotak("M = n / (V/1000)",
                    baris(f"M = {n} / ({V}/1000) = <b>{hasil:.5g} M</b>")
                ), unsafe_allow_html=True)

            else:
                with col1: n = st.number_input("Mol (n)", 0.0, value=0.1, key="mol_n_V")
                with col2: M = st.number_input("Molaritas (M)", 0.001, value=1.0, key="mol_M2")
                hasil = (n / M) * 1000
                hasil_card("Volume (V)", f"{hasil:.5g}", "mL")
                st.markdown(kotak("V (mL) = (n/M) × 1000",
                    baris(f"V = ({n}/{M}) × 1000 = <b>{hasil:.5g} mL</b>")
                ), unsafe_allow_html=True)

        with tab_reaksi:
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                kA = st.number_input("Koef A", 1, value=1, key="kA")
                nA = st.text_input("Nama A", "HCl", key="nA")
                mA = st.number_input("Mr A", 0.001, value=36.46, key="mA")
            with col2:
                kB = st.number_input("Koef B", 1, value=1, key="kB")
                nB = st.text_input("Nama B", "NaOH", key="nB")
                mB = st.number_input("Mr B", 0.001, value=40.00, key="mB")
            with col3:
                kC = st.number_input("Koef C", 1, value=1, key="kC")
                nC = st.text_input("Nama C", "NaCl", key="nC")
                mC = st.number_input("Mr C", 0.001, value=58.44, key="mC")
            with col4:
                kD = st.number_input("Koef D", 1, value=1, key="kD")
                nD = st.text_input("Nama D", "H₂O", key="nD")
                mD = st.number_input("Mr D", 0.001, value=18.02, key="mD")

            st.info(f"**Reaksi:** {kA} {nA} + {kB} {nB} → {kC} {nC} + {kD} {nD}")
            reaktan = st.selectbox("Reaktan pembatas:", [nA, nB], key="reaktan")
            n_pem   = st.number_input("Mol Reaktan Pembatas", 0.0, value=0.1, key="n_pem")
            k_ref   = kA if reaktan == nA else kB
            nC_mol  = n_pem * (kC / k_ref)

            hasil_card(f"Hasil {nC}", f"{nC_mol:.5g} mol ({nC_mol * mC:.5g} g)")
            st.markdown(kotak("Penyelesaian (perbandingan koefisien)",
                baris(f"Mol {nC} = ({kC}/{k_ref}) × {n_pem} = <b>{nC_mol:.5g} mol</b>") +
                baris(f"Massa {nC} = {nC_mol:.5g} × {mC} = <b>{nC_mol * mC:.5g} gram</b>")
            ), unsafe_allow_html=True)

    # ----------------------------------------------------------
    # MODUL 3: pH
    # ----------------------------------------------------------
    elif st.session_state.menu_aktif == "pH":
        st.markdown("### 🌈 Kesetimbangan & Perubahan pH")
        tab_asam, tab_basa, tab_ka, tab_dilusi = st.tabs([
            "🔴 pH Asam", "🔵 pH Basa", "🔬 Hitung Ka/Kb", "📉 ΔpH Pengenceran"
        ])

        with tab_asam:
            jenis = st.radio("Jenis asam:", ["Asam Kuat", "Asam Lemah"], horizontal=True, key="jenis_asam")
            C = st.number_input("Konsentrasi C (M)", 1e-14, value=0.1, key="C_asam")
            if jenis == "Asam Kuat":
                pH = -math.log10(max(C, 1e-14))
                hasil_card("pH Larutan", f"{pH:.4f}")
                st.markdown(kotak("pH = -log[H⁺]",
                    baris(f"[H⁺] = {C} M") +
                    baris(f"pH = -log({C}) = <b>{pH:.4f}</b>")
                ), unsafe_allow_html=True)
            else:
                Ka = st.number_input("Ka", 1e-20, value=1.8e-5, key="Ka_asam")
                h  = math.sqrt(Ka * C)
                pH = -math.log10(h)
                hasil_card("pH Larutan", f"{pH:.4f}")
                st.markdown(kotak("pH Asam Lemah: [H⁺] = √(Ka × C)",
                    baris(f"[H⁺] = √({Ka} × {C}) = {h:.4e} M") +
                    baris(f"pH = -log({h:.4e}) = <b>{pH:.4f}</b>")
                ), unsafe_allow_html=True)

        with tab_basa:
            jenis = st.radio("Jenis basa:", ["Basa Kuat", "Basa Lemah"], horizontal=True, key="jenis_basa")
            C = st.number_input("Konsentrasi C (M)", 1e-14, value=0.1, key="C_basa")
            if jenis == "Basa Kuat":
                pH = 14 + math.log10(C)
                hasil_card("pH Larutan", f"{pH:.4f}")
                st.markdown(kotak("pH = 14 - pOH",
                    baris(f"pOH = -log({C}) = {-math.log10(C):.4f}") +
                    baris(f"pH = 14 - pOH = <b>{pH:.4f}</b>")
                ), unsafe_allow_html=True)
            else:
                Kb = st.number_input("Kb", 1e-20, value=1.8e-5, key="Kb_basa")
                oh = math.sqrt(Kb * C)
                pH = 14 + math.log10(oh)
                hasil_card("pH Larutan", f"{pH:.4f}")
                st.markdown(kotak("pH Basa Lemah: [OH⁻] = √(Kb × C)",
                    baris(f"[OH⁻] = √({Kb} × {C}) = {oh:.4e} M") +
                    baris(f"pOH = -log({oh:.4e}) = {-math.log10(oh):.4f}") +
                    baris(f"pH = 14 - pOH = <b>{pH:.4f}</b>")
                ), unsafe_allow_html=True)

        with tab_ka:
            C   = st.number_input("Konsentrasi C (M)", 1e-10, value=0.1, key="C_ka")
            pH  = st.number_input("pH terukur", 0.0, 14.0, value=2.87, key="pH_ka")
            H   = 10 ** (-pH)
            if C > H:
                Ka = H**2 / (C - H)
                hasil_card("Ka Prediksi", f"{Ka:.4e}")
                st.markdown(kotak("Ka = [H⁺]² / (C - [H⁺])",
                    baris(f"[H⁺] = 10^(-{pH}) = {H:.4e} M") +
                    baris(f"Ka = ({H:.4e})² / ({C} - {H:.4e}) = <b>{Ka:.4e}</b>")
                ), unsafe_allow_html=True)

        with tab_dilusi:
            jenis = st.radio("Jenis larutan:", ["Asam Kuat", "Asam Lemah", "Basa Kuat", "Basa Lemah"],
                             horizontal=True, key="jenis_dilusi")
            C1 = st.number_input("C₁ (M)", 1e-14, value=0.1, key="C1_dil")
            V1 = st.number_input("V₁ (mL)", 0.001, value=10.0, key="V1_dil")
            V2 = st.number_input("V₂ (mL)", 0.001, value=100.0, key="V2_dil")
            K  = st.number_input("Ka / Kb", 1e-20, value=1.8e-5, key="K_dil") if "Lemah" in jenis else None

            def hitung_pH(konsentrasi, jenis_lar, K_val):
                c = max(konsentrasi, 1e-14)
                if jenis_lar == "Asam Kuat":   return -math.log10(c)
                if jenis_lar == "Asam Lemah":  return -math.log10(math.sqrt(K_val * c))
                if jenis_lar == "Basa Kuat":   return 14 + math.log10(c)
                if jenis_lar == "Basa Lemah":  return 14 + math.log10(math.sqrt(K_val * c))

            C2   = C1 * V1 / V2
            pH1  = hitung_pH(C1, jenis, K)
            pH2  = hitung_pH(C2, jenis, K)
            dpH  = abs(pH2 - pH1)
            hasil_card("pH Akhir", f"{pH2:.4f}", f"(Awal: {pH1:.4f})")
            st.markdown(kotak("Penyelesaian (Efek Dilusi terhadap pH)",
                baris(f"C₂ = ({C1} × {V1}) / {V2} = <b>{C2:.4e} M</b>") +
                baris(f"pH₁ (C₁) = <b>{pH1:.4f}</b>") +
                baris(f"pH₂ (C₂) = <b>{pH2:.4f}</b>") +
                baris(f"ΔpH = <b>{dpH:.4f}</b>")
            ), unsafe_allow_html=True)

    # ----------------------------------------------------------
    # MODUL 4: BUFFER
    # ----------------------------------------------------------
    elif st.session_state.menu_aktif == "Buffer":
        st.markdown("### 🧪 Pembuatan Larutan Buffer")
        tab_ph, tab_rasio, tab_beta = st.tabs([
            "🧮 Hitung pH Buffer", "⚖️ Hitung Rasio [A⁻]/[HA]", "📊 Kapasitas Buffer (β)"
        ])

        with tab_ph:
            pKa = st.number_input("pKa asam", 0.0, 14.0, value=4.74, key="pka_buf")
            ab  = st.number_input("[A⁻] Basa Konjugat (M)", 0.0001, value=0.1, key="ab_buf")
            ha  = st.number_input("[HA] Asam (M)", 0.0001, value=0.1, key="ha_buf")
            pH  = pKa + math.log10(ab / ha)
            hasil_card("pH Buffer", f"{pH:.4f}")
            st.markdown(kotak("Henderson-Hasselbalch: pH = pKa + log([A⁻]/[HA])",
                baris(f"pH = {pKa} + log({ab}/{ha})") +
                baris(f"pH = {pKa} + {math.log10(ab/ha):.4f} = <b>{pH:.4f}</b>")
            ), unsafe_allow_html=True)

        with tab_rasio:
            pH_t  = st.number_input("pH target", 0.0, 14.0, value=5.0, key="pH_rasio")
            pKa_r = st.number_input("pKa asam", 0.0, 14.0, value=4.74, key="pka_rasio")
            Ctot  = st.number_input("Konsentrasi total (M)", 0.001, value=0.2, key="Ctot_rasio")
            ratio = 10 ** (pH_t - pKa_r)
            a_min = Ctot * ratio / (1 + ratio)
            ha_v  = Ctot / (1 + ratio)
            hasil_card("Rasio [A⁻]/[HA]", f"{ratio:.5f}", f"([A⁻]={a_min:.4f}M)")
            st.markdown(kotak("Rasio = 10^(pH - pKa)",
                baris(f"[A⁻]/[HA] = 10^({pH_t} - {pKa_r}) = <b>{ratio:.5f}</b>") +
                baris(f"[A⁻] = ({ratio:.5f} / (1+{ratio:.5f})) × {Ctot} = <b>{a_min:.4f} M</b>") +
                baris(f"[HA] = {Ctot} - {a_min:.4f} = <b>{ha_v:.4f} M</b>")
            ), unsafe_allow_html=True)

        with tab_beta:
            Ctot = st.number_input("Konsentrasi total (M)", 0.0001, value=0.1, key="Ctot_beta")
            Ka   = st.number_input("Ka", 1e-20, value=1.8e-5, key="Ka_beta")
            pH_b = st.number_input("pH larutan", 0.0, 14.0, value=4.74, key="pH_beta")
            H    = 10 ** (-pH_b)
            beta = 2.303 * Ctot * (Ka * H) / (Ka + H)**2
            hasil_card("Kapasitas Buffer (β)", f"{beta:.4e}")
            st.markdown(kotak("Van Slyke: β = 2.303 × C × Ka[H⁺] / (Ka+[H⁺])²",
                baris(f"[H⁺] = 10^(-{pH_b}) = {H:.4e} M") +
                baris(f"β = 2.303 × {Ctot} × ({Ka:.2e} × {H:.2e}) / ({Ka:.2e} + {H:.2e})²") +
                baris(f"β = <b>{beta:.4e}</b>")
            ), unsafe_allow_html=True)

    # ----------------------------------------------------------
    # MODUL 5: GALAT
    # ----------------------------------------------------------
    elif st.session_state.menu_aktif == "Galat":
        st.markdown("### 📊 Galat & Propagasi Error")
        tab_ga, tab_prop, tab_stat = st.tabs([
            "📏 Galat Absolut & Relatif", "⚡ Propagasi Error", "📊 Statistik (SD & RSD)"
        ])

        with tab_ga:
            x_ukur = st.number_input("Nilai terukur", value=9.87, key="x_ukur")
            x_benar = st.number_input("Nilai benar", value=10.00, key="x_benar")
            g_abs = abs(x_ukur - x_benar)
            g_rel = (g_abs / x_benar) * 100
            hasil_card("Galat Absolut", f"{g_abs:.5g}")
            st.markdown(kotak("Galat Absolut & Relatif",
                baris(f"Galat Absolut = |{x_ukur} - {x_benar}| = <b>{g_abs:.5g}</b>") +
                baris(f"Galat Relatif = ({g_abs:.5g} / {x_benar}) × 100 = <b>{g_rel:.3f}%</b>")
            ), unsafe_allow_html=True)

        with tab_prop:
            op   = st.selectbox("Operasi:", [
                "Penjumlahan / Pengurangan (x ± y)",
                "Perkalian / Pembagian (x × y atau x/y)"
            ], key="op_prop")
            xv   = st.number_input("Nilai x", value=10.0, key="xv")
            dxv  = st.number_input("δx", value=0.05, key="dxv")
            yv   = st.number_input("Nilai y", value=5.0, key="yv")
            dyv  = st.number_input("δy", value=0.03, key="dyv")

            if "Penjumlahan" in op:
                unc = math.sqrt(dxv**2 + dyv**2)
                hasil_card("Ketidakpastian Akhir", f"± {unc:.5g}")
                st.markdown(kotak("δz = √(δx² + δy²)",
                    baris(f"δz = √({dxv}² + {dyv}²) = √({dxv**2:.5f} + {dyv**2:.5f})") +
                    baris(f"δz = <b>± {unc:.5g}</b>")
                ), unsafe_allow_html=True)
            else:
                z   = xv * yv
                unc = z * math.sqrt((dxv/xv)**2 + (dyv/yv)**2)
                hasil_card("Ketidakpastian Akhir", f"± {unc:.5g}")
                st.markdown(kotak("δz/z = √((δx/x)² + (δy/y)²)",
                    baris(f"z = {xv} × {yv} = {z}") +
                    baris(f"δz = {z} × √(({dxv}/{xv})² + ({dyv}/{yv})²)") +
                    baris(f"δz = <b>± {unc:.5g}</b>")
                ), unsafe_allow_html=True)

        with tab_stat:
            raw = st.text_area("Data pengukuran (pisahkan dengan koma):",
                               value="9.87, 9.92, 9.85, 9.90, 9.88", key="data_stat")
            data = []
            for token in raw.split(','):
                token = token.strip()
                if token:
                    try:
                        data.append(float(token))
                    except ValueError:
                        pass

            if len(data) >= 2:
                mean = sum(data) / len(data)
                sd   = math.sqrt(sum((x - mean)**2 for x in data) / (len(data) - 1))
                rsd  = (sd / mean) * 100
                hasil_card("Rata-rata ± SD", f"{mean:.4g} ± {sd:.4g}", f"(RSD: {rsd:.3f}%)")
                st.markdown(kotak("Statistik Deskriptif",
                    baris(f"n = {len(data)} data") +
                    baris(f"Rata-rata (μ) = Σx / n = <b>{mean:.4g}</b>") +
                    baris(f"SD = √(Σ(xᵢ-μ)² / (n-1)) = <b>{sd:.4g}</b>") +
                    baris(f"RSD = (SD/μ) × 100% = <b>{rsd:.3f}%</b>")
                ), unsafe_allow_html=True)


st.divider()
st.markdown(
    '<p style="text-align:center; font-size:12px; color:#9e9e9e;">⚗️ Kalkulator Analisis Kuantitatif · Kimia Analitik</p>',
    unsafe_allow_html=True
)
