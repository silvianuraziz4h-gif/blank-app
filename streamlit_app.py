import streamlit as st
import math

st.set_page_config(
    page_title="Kalkulator Kimia Analitik",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Kumpulan Gaya CSS Custom (Tetap dipertahankan agar visual tidak berubah)
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600&family=Space+Mono:wght@400;700&display=swap');

.stApp {
    background: #1a1a2e !important;
    background-image: radial-gradient(ellipse at top left, #16213e 0%, #1a1a2e 60%, #0f3460 100%) !important;
    background-attachment: fixed;
    color: #f0f0f0 !important;
}

html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
}

.stMarkdown, p, label, .stSlider, .stRadio, div[data-baseweb="checkbox"] {
    color: #f0f0f0 !important;
}

/* input field text color fix */
div[data-testid="stNumberInput"] input,
div[data-testid="stTextInput"] input,
div[data-testid="stTextArea"] textarea,
div[data-baseweb="select"] div {
    color: #1a1a2e !important;
    font-weight: 500 !important;
}
div[data-shaded="true"], ul[role="listbox"] li {
    color: #1a1a2e !important;
}

/* tab styling */
button[data-baseweb="tab"] p { color: #9e9e9e !important; }
button[data-baseweb="tab"][aria-selected="true"] p {
    color: #e8a045 !important;
    font-weight: 700 !important;
}

.badge-label {
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
    font-family: 'Space Grotesk', sans-serif;
    font-size: 38px;
    font-weight: 600;
    line-height: 1.2;
    color: #ffffff;
    margin: 0 0 .4rem;
}
.main-title em {
    font-style: normal;
    color: #e8a045;
}
.subtitle {
    font-size: 14px;
    color: #9e9e9e;
    line-height: 1.6;
    max-width: 560px;
    margin-bottom: 1.5rem;
}

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

/* halaman welcome */
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
.welcome-header h1 {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 36px;
    font-weight: 600;
    margin: 0;
    color: #fff;
}
.welcome-body {
    padding: 2rem 2rem;
    text-align: center;
    color: #cfcfcf;
}
.welcome-desc {
    font-size: 18px;
    font-weight: 400;
    line-height: 1.5;
    margin: 0 auto;
    max-width: 560px;
}

.info-card {
    background: rgba(255,255,255,0.04);
    border-radius: 12px;
    padding: 1.4rem;
    height: 100%;
    border: 1px solid rgba(255,255,255,0.07);
    border-top: 4px solid #e8a045;
}
.info-card h4 {
    margin-top: 0;
    font-size: 16px;
    margin-bottom: 0.6rem;
    color: #e8a045;
}
.info-card ul {
    margin: 0;
    padding-left: 1.2rem;
    font-size: 14px;
    color: #b0b0b0;
    line-height: 1.7;
}

/* menu cards */
.menu-card {
    background: rgba(255,255,255,0.04);
    border-radius: 10px;
    padding: 1.4rem;
    min-height: 180px;
    border: 1px solid rgba(255,255,255,0.06);
    transition: background 0.2s ease, transform 0.15s ease;
}
.menu-card:hover {
    background: rgba(255,255,255,0.07);
    transform: translateY(-2px);
}
.card-p1 { border-left: 4px solid #e8a045; }
.card-p2 { border-left: 4px solid #4fc3f7; }
.card-p3 { border-left: 4px solid #81c784; }
.card-p4 { border-left: 4px solid #ce93d8; }
.card-p5 { border-left: 4px solid #ef9a9a; }

.menu-icon  { font-size: 22px; margin-bottom: 0.4rem; }
.menu-title { font-size: 16px; font-weight: 600; margin-top: 0.2rem; margin-bottom: 0.4rem; color: #f0f0f0; }
.menu-desc  { font-size: 12px; color: #9e9e9e; line-height: 1.5; }

/* tombol */
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
div.stButton > button:hover {
    opacity: 0.88;
}

/* kotak hasil */
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

# Inisialisasi navigasi menu utama
if 'menu_aktif' not in st.session_state:
    st.session_state.menu_aktif = "Start"

# List pilihan satuan konv
SATUAN_KONSENTRASI = ["Molaritas (M)", "% massa/volume (% m/v)", "ppm (mg/L)", "ppb (µg/L)", "mg/mL", "Molalitas (m)"]

# ---------------------------------------------------------------
# HALAMAN START
# ---------------------------------------------------------------
if st.session_state.menu_aktif == "Start":
    st.markdown("""
    <div class="welcome-outer">
        <div class="welcome-header">
            <h1>Selamat Datang 👋</h1>
        </div>
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

    col_tujuan, col_manfaat = st.columns(2)
    with col_tujuan:
        st.markdown("""
        <div class="info-card">
            <h4>🎯 Tujuan Aplikasi</h4>
            <ul>
                <li>Menyediakan platform hitung laboratorium yang mudah dipahami.</li>
                <li>Mengecek kekeliruan pengerjaan angka desimal berkat otomasi kalkulasi analitis.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    with col_manfaat:
        st.markdown("""
        <div class="info-card">
            <h4>✨ Manfaat Aplikasi</h4>
            <ul>
                <li><b>Cepat & Efisien:</b> Memproses rumus C₁V₁=C₂V₂ dan stoikiometri dalam hitungan detik.</li>
                <li><b>Transparan:</b> Dilengkapi langkah penyelesaian lengkap dan hitung galat SD/RSD.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# ---------------------------------------------------------------
# DASHBOARD UTAMA
# ---------------------------------------------------------------
elif st.session_state.menu_aktif == "Dashboard":
    st.markdown('<div class="badge-label">🧪 Kimia Analitik</div>', unsafe_allow_html=True)
    st.markdown("""
    <h1 class="main-title">Kalkulator <em>Analisis</em> Kuantitatif</h1>
    <p class="subtitle">Pilih salah satu modul kalkulator di bawah ini untuk memulai:</p>
    """, unsafe_allow_html=True)
    st.divider()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="menu-card card-p1"><div class="menu-icon">💧</div><div class="menu-title">Pengenceran Larutan</div><div class="menu-desc">Kalkulator pengenceran tunggal, serial/bertingkat, dan penentuan faktor pengenceran sampel.</div></div>', unsafe_allow_html=True)
        if st.button("Buka Modul 01 →", key="btn_m1", use_container_width=True):
            st.session_state.menu_aktif = "Pengenceran"
            st.rerun()
    with col2:
        st.markdown('<div class="menu-card card-p2"><div class="menu-icon">🔄</div><div class="menu-title">Konsentrasi & Stoikiometri</div><div class="menu-desc">Konversi antar satuan kimia (M, %, ppm, ppb) dan hitung stoikiometri reaksi mol.</div></div>', unsafe_allow_html=True)
        if st.button("Buka Modul 02 →", key="btn_m2", use_container_width=True):
            st.session_state.menu_aktif = "Stoikiometri"
            st.rerun()
    with col3:
        st.markdown('<div class="menu-card card-p3"><div class="menu-icon">🌈</div><div class="menu-title">Kesetimbangan & pH</div><div class="menu-desc">Prediksi pH sistem asam-basa kuat/lemah dan perhitungan Ka/Kb tetapan larutan.</div></div>', unsafe_allow_html=True)
        if st.button("Buka Modul 03 →", key="btn_m3", use_container_width=True):
            st.session_state.menu_aktif = "pH"
            st.rerun()

    st.write("")
    col4, col5, _ = st.columns(3)
    with col4:
        st.markdown('<div class="menu-card card-p4"><div class="menu-icon">🧪</div><div class="menu-title">Larutan Buffer</div><div class="menu-desc">Desain sistem penyangga menggunakan persamaan Henderson-Hasselbalch.</div></div>', unsafe_allow_html=True)
        if st.button("Buka Modul 04 →", key="btn_m4", use_container_width=True):
            st.session_state.menu_aktif = "Buffer"
            st.rerun()
    with col5:
        st.markdown('<div class="menu-card card-p5"><div class="menu-icon">📊</div><div class="menu-title">Galat & Propagasi</div><div class="menu-desc">Hitung ketidakpastian, deviasi standar (SD), dan nilai RSD data pengukuran.</div></div>', unsafe_allow_html=True)
        if st.button("Buka Modul 05 →", key="btn_m5", use_container_width=True):
            st.session_state.menu_aktif = "Galat"
            st.rerun()

# ---------------------------------------------------------------
# KONTEN ISI MODUL-MODUL
# ---------------------------------------------------------------
else:
    if st.button("← Kembali ke Menu Utama", key="btn_kembali"):
        st.session_state.menu_aktif = "Dashboard"
        st.rerun()
    st.divider()

    # ==========================================
    # MODUL 1: PENGENCERAN
    # ==========================================
    if st.session_state.menu_aktif == "Pengenceran":
        st.markdown("### 💧 Pengenceran Larutan")
        tab_cv, tab_serial, tab_fp = st.tabs(["C₁V₁ = C₂V₂", "Serial / Bertingkat", "Faktor Pengenceran"])

        with tab_cv:
            st.markdown('<div class="formula-box">C₁ × V₁ = C₂ × V₂</div>', unsafe_allow_html=True)
            cari = st.selectbox("Variabel yang dicari:", [
                "C₂ — Konsentrasi akhir",
                "V₂ — Volume akhir",
                "C₁ — Konsentrasi awal",
                "V₁ — Volume awal"
            ], key="pilihan_cari_cv")
            satuan = st.selectbox("Satuan konsentrasi:", ["M", "mM", "µM", "mg/mL", "ppm", "ppb"], key="satuan_cv")
            col1, col2 = st.columns(2)

            if cari == "C₂ — Konsentrasi akhir":
                with col1:
                    c1 = st.number_input("C₁ — Konsentrasi awal", 0.0, value=1.0, format="%.5f", key="input_c1_hitung_c2")
                    v1 = st.number_input("V₁ — Volume awal (mL)", 0.0, value=10.0, format="%.3f", key="input_v1_hitung_c2")
                with col2:
                    v2 = st.number_input("V₂ — Volume akhir (mL)", 1e-9, value=100.0, format="%.3f", key="input_v2_hitung_c2")
                hasil = (c1 * v1) / v2
                
                st.markdown(f'<div class="result-card"><p class="result-label">C₂ — Konsentrasi akhir</p><p class="result-value">{hasil:.6g} <span style="font-size:16px; color:#e8a045;">{satuan}</span></p></div>', unsafe_allow_html=True)
                
                st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (C₂ = (C₁ × V₁) / V₂):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>C₂ = ({c1} × {v1}) / {v2}</p><p style='margin: 0 0 8px 0;'>C₂ = {c1 * v1} / {v2}</p><p style='margin: 0 0 8px 0;'>C₂ = <b>{hasil:.6g} {satuan}</b></p></div></div>""", unsafe_allow_html=True)

            elif cari == "V₂ — Volume akhir":
                with col1:
                    c1 = st.number_input("C₁ — Konsentrasi awal", 0.0, value=1.0, format="%.5f", key="input_c1_hitung_v2")
                    v1 = st.number_input("V₁ — Volume awal (mL)", 0.0, value=10.0, format="%.3f", key="input_v1_hitung_v2")
                with col2:
                    c2 = st.number_input("C₂ — Konsentrasi akhir", 1e-9, value=0.1, format="%.5f", key="input_c2_hitung_v2")
                hasil = (c1 * v1) / c2
                
                st.markdown(f'<div class="result-card"><p class="result-label">V₂ — Volume akhir</p><p class="result-value">{hasil:.5g} <span style="font-size:16px; color:#e8a045;">mL</span></p></div>', unsafe_allow_html=True)
                
                st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (V₂ = (C₁ × V₁) / C₂):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>V₂ = ({c1} × {v1}) / {c2}</p><p style='margin: 0 0 8px 0;'>V₂ = {c1 * v1} / {c2}</p><p style='margin: 0 0 8px 0;'>V₂ = <b>{hasil:.5g} mL</b></p></div></div>""", unsafe_allow_html=True)

            elif cari == "C₁ — Konsentrasi awal":
                with col1:
                    v1 = st.number_input("V₁ — Volume awal (mL)", 1e-9, value=10.0, format="%.3f", key="input_v1_hitung_c1")
                    c2 = st.number_input("C₂ — Konsentrasi akhir", 0.0, value=0.1, format="%.5f", key="input_c2_hitung_c1")
                with col2:
                    v2 = st.number_input("V₂ — Volume akhir (mL)", 1e-9, value=100.0, format="%.3f", key="input_v2_hitung_c1")
                hasil = (c2 * v2) / v1
                
                st.markdown(f'<div class="result-card"><p class="result-label">C₁ — Konsentrasi awal</p><p class="result-value">{hasil:.6g} <span style="font-size:16px; color:#e8a045;">{satuan}</span></p></div>', unsafe_allow_html=True)
                
                st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (C₁ = (C₂ × V₂) / V₁):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>C₁ = ({c2} × {v2}) / {v1}</p><p style='margin: 0 0 8px 0;'>C₁ = {c2 * v2} / {v1}</p><p style='margin: 0 0 8px 0;'>C₁ = <b>{hasil:.6g} {satuan}</b></p></div></div>""", unsafe_allow_html=True)

            else:
                with col1:
                    c1 = st.number_input("C₁ — Konsentrasi awal", 1e-9, value=1.0, format="%.5f", key="input_c1_hitung_v1")
                    c2 = st.number_input("C₂ — Konsentrasi akhir", 0.0, value=0.1, format="%.5f", key="input_c2_hitung_v1")
                with col2:
                    v2 = st.number_input("V₂ — Volume akhir (mL)", 1e-9, value=100.0, format="%.3f", key="input_v2_hitung_v1")
                hasil = (c2 * v2) / c1
                
                st.markdown(f'<div class="result-card"><p class="result-label">V₁ — Volume awal</p><p class="result-value">{hasil:.5g} <span style="font-size:16px; color:#e8a045;">mL</span></p></div>', unsafe_allow_html=True)
                
                st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (V₁ = (C₂ × V₂) / C₁):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>V₁ = ({c2} × {v2}) / {c1}</p><p style='margin: 0 0 8px 0;'>V₁ = {c2 * v2} / {c1}</p><p style='margin: 0 0 8px 0;'>V₁ = <b>{hasil:.5g} mL</b></p></div></div>""", unsafe_allow_html=True)

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
                
                # Proses pembuatan tabel HTML manual tanpa loop baris otomatis bawaan AI
                rows = ""
                for idx in range(int(nstep) + 1):
                    nama_tabung = "Stok" if idx == 0 else f"Langkah {idx}"
                    nilai_kons = c0 * (f ** idx)
                    rows += f"""<tr>
                        <td style='padding:6px 10px; border-bottom:1px solid rgba(255,255,255,0.07)'>{nama_tabung}</td>
                        <td style='padding:6px 10px; font-family:Space Mono,monospace; color:#e8a045; border-bottom:1px solid rgba(255,255,255,0.07)'>{nilai_kons:.4e}</td>
                        <td style='padding:6px 10px; color:#9e9e9e; border-bottom:1px solid rgba(255,255,255,0.07)'>{sat_s}</td>
                    </tr>"""
                    
                st.markdown(
                    f"""<table style="width:100%;border-collapse:collapse;border:1px solid rgba(232,160,69,0.2);
                        font-size:13px;margin-top:.5rem;background:rgba(255,255,255,0.03);border-radius:8px;overflow:hidden">
                        <thead><tr style="background:rgba(232,160,69,0.08)">
                            <th style="padding:8px 10px;text-align:left;color:#e8a045">Tabung</th>
                            <th style="padding:8px 10px;text-align:left;color:#e8a045">Konsentrasi</th>
                            <th style="padding:8px 10px;text-align:left;color:#e8a045">Satuan</th>
                        </tr></thead><tbody>{rows}</tbody></table>""",
                    unsafe_allow_html=True
                )
                
                st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (Faktor Pengenceran Serial):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>Faktor per tabung = {va_s} mL / {vt_s} mL = <b>{f:.4f}</b></p><p style='margin: 0 0 8px 0;'>Cₙ = {c0} × ({f:.4f})ⁿ</p></div></div>""", unsafe_allow_html=True)

        with tab_fp:
            col1, col2 = st.columns(2)
            with col1:
                va_fp = st.number_input("Volume awal (mL)", 0.001, value=1.0, format="%.3f", key="fp_va")
                vb_fp = st.number_input("Volume akhir (mL)", 0.001, value=100.0, format="%.3f", key="fp_vb")
            with col2:
                ca_fp = st.number_input("Konsentrasi awal (opsional)", 0.0, value=1.0, format="%.5f", key="fp_ca")
            fp = vb_fp / va_fp
            
            st.markdown(f'<div class="result-card"><p class="result-label">Faktor Pengenceran</p><p class="result-value">1 : {fp:.4f} <span style="font-size:16px; color:#e8a045;"></span></p></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="result-card"><p class="result-label">Konsentrasi Akhir</p><p class="result-value">{ca_fp / fp:.5g} <span style="font-size:16px; color:#e8a045;"></span></p></div>', unsafe_allow_html=True)
            
            st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (Faktor Pengenceran (FP)):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>FP = Volume Akhir / Volume Awal = {vb_fp} / {va_fp} = <b>{fp:.4f}</b></p><p style='margin: 0 0 8px 0;'>Konsentrasi Akhir = C_awal / FP = {ca_fp} / {fp:.4f} = <b>{ca_fp / fp:.5g}</b></p></div></div>""", unsafe_allow_html=True)

    # ==========================================
    # MODUL 2: STOIKIOMETRI & KONVERSI SATUAN
    # ==========================================
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
                # Membongkar fungsi otomatisasi ke_mgL dengan logika IF-ELIF manual mahasiswa
                mgL = nilai
                if satuan_dari == "Molaritas (M)":
                    mgL = nilai * mr_k * 1000
                elif satuan_dari == "% massa/volume (% m/v)":
                    mgL = nilai * 10000
                elif satuan_dari == "ppm (mg/L)":
                    mgL = nilai
                elif satuan_dari == "ppb (µg/L)":
                    mgL = nilai / 1000
                elif satuan_dari == "mg/mL":
                    mgL = nilai * 1000
                elif satuan_dari == "Molalitas (m)":
                    mgL = nilai * mr_k * rho * 1000

                # Membongkar fungsi otomatisasi dari_mgL dengan logika IF-ELIF manual mahasiswa
                hasil = mgL
                if satuan_ke == "Molaritas (M)":
                    hasil = mgL / (mr_k * 1000)
                elif satuan_ke == "% massa/volume (% m/v)":
                    hasil = mgL / 10000
                elif satuan_ke == "ppm (mg/L)":
                    hasil = mgL
                elif satuan_ke == "ppb (µg/L)":
                    hasil = mgL * 1000
                elif satuan_ke == "mg/mL":
                    hasil = mgL / 1000
                elif satuan_ke == "Molalitas (m)":
                    hasil = mgL / (mr_k * rho * 1000)

                st.markdown(f'<div class="result-card"><p class="result-label">Hasil Konversi</p><p class="result-value">{hasil:.6g} <span style="font-size:16px; color:#e8a045;">{satuan_ke}</span></p></div>', unsafe_allow_html=True)
                
                st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (Alur Jembatan Konversi):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>Tahap 1: '{satuan_dari}' → basis standar ppm (mg/L):</p><p style='margin: 0 0 8px 0;'>&nbsp;&nbsp;&nbsp;→ <b>{mgL:.4e} mg/L</b></p><p style='margin: 0 0 8px 0;'>Tahap 2: mg/L → target '{satuan_ke}':</p><p style='margin: 0 0 8px 0;'>&nbsp;&nbsp;&nbsp;→ <b>{hasil:.6g} {satuan_ke}</b></p></div><p style='margin: 10px 0 0 0; font-size: 11px; color: #9e9e9e; border-top: 1px solid rgba(255,255,255,0.08); padding-top: 8px;'>Tetapan: Mr = {mr_k} g/mol | Density = {rho} g/mL</p></div>""", unsafe_allow_html=True)

        with tab_mol:
            pilihan_mol = st.selectbox("Cari:", [
                "Mol (n) dari massa & Mr",
                "Mol (n) dari M & V",
                "Massa (g) dari n & Mr",
                "Molaritas (M) dari n & V",
                "Volume (mL) dari n & M"
            ], key="pilihan_cari_mol")
            col1, col2 = st.columns(2)

            if "massa & Mr" in pilihan_mol:
                with col1: massa = st.number_input("Massa (gram)", 0.0, value=5.85, format="%.4f", key="mol_massa_g")
                with col2: mr2   = st.number_input("Mr (g/mol)", 0.001, value=58.44, key="mol_mr_g")
                hasil = massa / mr2
                st.markdown(f'<div class="result-card"><p class="result-label">Mol (n)</p><p class="result-value">{hasil:.5g} <span style="font-size:16px; color:#e8a045;">mol</span></p></div>', unsafe_allow_html=True)
                st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (n = gram / Mr):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>n = {massa} / {mr2}</p><p style='margin: 0 0 8px 0;'>n = <b>{hasil:.5g} mol</b></p></div></div>""", unsafe_allow_html=True)

            elif "M & V" in pilihan_mol:
                with col1: Mm = st.number_input("Molaritas (M)", 0.0, value=1.0, key="mol_molar_M")
                with col2: Vm = st.number_input("Volume (mL)", 0.0, value=100.0, key="mol_vol_ml")
                hasil = Mm * (Vm / 1000)
                st.markdown(f'<div class="result-card"><p class="result-label">Mol (n)</p><p class="result-value">{hasil:.5g} <span style="font-size:16px; color:#e8a045;">mol</span></p></div>', unsafe_allow_html=True)
                st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (n = M × (V / 1000)):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>n = {Mm} × ({Vm} / 1000)</p><p style='margin: 0 0 8px 0;'>n = <b>{hasil:.5g} mol</b></p></div></div>""", unsafe_allow_html=True)

            elif "Massa (g)" in pilihan_mol:
                with col1: nm  = st.number_input("Mol (n)", 0.0, value=0.1, key="mol_n_input")
                with col2: mr3 = st.number_input("Mr (g/mol)", 0.001, value=58.44, key="mol_mr_input")
                hasil = nm * mr3
                st.markdown(f'<div class="result-card"><p class="result-label">Massa (m)</p><p class="result-value">{hasil:.5g} <span style="font-size:16px; color:#e8a045;">gram</span></p></div>', unsafe_allow_html=True)
                st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (gram = n × Mr):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>gram = {nm} × {mr3}</p><p style='margin: 0 0 8px 0;'>gram = <b>{hasil:.5g} gram</b></p></div></div>""", unsafe_allow_html=True)

            elif "Molaritas" in pilihan_mol:
                with col1: nm  = st.number_input("Mol (n)", 0.0, value=0.1, key="mol_n_input_molar")
                with col2: Vm2 = st.number_input("Volume (mL)", 0.001, value=100.0, key="mol_v_input_molar")
                hasil = nm / (Vm2 / 1000)
                st.markdown(f'<div class="result-card"><p class="result-label">Molaritas (M)</p><p class="result-value">{hasil:.5g} <span style="font-size:16px; color:#e8a045;">mol/L</span></p></div>', unsafe_allow_html=True)
                st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (M = n / (V / 1000)):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>M = {nm} / ({Vm2} / 1000)</p><p style='margin: 0 0 8px 0;'>M = <b>{hasil:.5g} M</b></p></div></div>""", unsafe_allow_html=True)

            else:
                with col1: nm2 = st.number_input("Mol (n)", 0.0, value=0.1, key="mol_n_input_vol")
                with col2: Mm3 = st.number_input("Molaritas (M)", 0.001, value=1.0, key="mol_m_input_vol")
                hasil = (nm2 / Mm3) * 1000
                st.markdown(f'<div class="result-card"><p class="result-label">Volume (V)</p><p class="result-value">{hasil:.5g} <span style="font-size:16px; color:#e8a045;">mL</span></p></div>', unsafe_allow_html=True)
                st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (V (mL) = (n / M) × 1000):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>V = ({nm2} / {Mm3}) × 1000</p><p style='margin: 0 0 8px 0;'>V = <b>{hasil:.5g} mL</b></p></div></div>""", unsafe_allow_html=True)

        with tab_reaksi:
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                kA = st.number_input("Koef A", 1, value=1, key="koef_a")
                nA = st.text_input("Nama A", "HCl", key="nama_a")
                mA = st.number_input("Mr A", 0.001, value=36.46, key="mr_a")
            with col2:
                kB = st.number_input("Koef B", 1, value=1, key="koef_b")
                nB = st.text_input("Nama B", "NaOH", key="nama_b")
                mB = st.number_input("Mr B", 0.001, value=40.00, key="mr_b")
            with col3:
                kC = st.number_input("Koef C", 1, value=1, key="koef_c")
                nC = st.text_input("Nama C", "NaCl", key="nama_c")
                mC = st.number_input("Mr C", 0.001, value=58.44, key="mr_c")
            with col4:
                kD = st.number_input("Koef D", 1, value=1, key="koef_d")
                nD = st.text_input("Nama D", "H₂O", key="nama_d")
                mD = st.number_input("Mr D", 0.001, value=18.02, key="mr_d")

            st.info(f"**Reaksi:** {kA} {nA} + {kB} {nB} → {kC} {nC} + {kD} {nD}")
            zat_r = st.selectbox("Reaktan pembatas:", [nA, nB], key="pilihan_reaktan_pembatass")
            n_ref = st.number_input("Mol Reaktan Pembatas", 0.0, value=0.1, key="mol_pembatas_reaksi")
            
            k_ref = kA if zat_r == nA else kB

            nC_mol = n_ref * (kC / k_ref)
            st.markdown(f'<div class="result-card"><p class="result-label">Hasil {nC}</p><p class="result-value">{nC_mol:.5g} mol ({nC_mol * mC:.5g} g) <span style="font-size:16px; color:#e8a045;"></span></p></div>', unsafe_allow_html=True)
            
            st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (Perbandingan Koefisien Reaksi):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>Mol {nC} = (Koef {nC} / Koef Pembatas) × Mol Pembatas</p><p style='margin: 0 0 8px 0;'>Mol {nC} = ({kC} / {k_ref}) × {n_ref} = <b>{nC_mol:.5g} mol</b></p><p style='margin: 0 0 8px 0;'>Massa {nC} = Mol × Mr = {nC_mol:.5g} × {mC} = <b>{nC_mol * mC:.5g} gram</b></p></div></div>""", unsafe_allow_html=True)

    # ==========================================
    # MODUL 3: PH LARUTAN
    # ==========================================
    elif st.session_state.menu_aktif == "pH":
        st.markdown("### 🌈 Kesetimbangan & Perubahan pH")
        tab_asam, tab_basa, tab_ka, tab_dilusi = st.tabs([
            "🔴 pH Asam", "🔵 pH Basa", "🔬 Hitung Ka/Kb", "📉 ΔpH Pengenceran"
        ])

        with tab_asam:
            jenis_a = st.radio("Jenis asam:", ["Asam Kuat", "Asam Lemah"], horizontal=True, key="pilihan_asam_kuat_lemah")
            Ca = st.number_input("Konsentrasi C (M)", 1e-14, value=0.1, key="as_C")
            if jenis_a == "Asam Kuat":
                pH = -math.log10(max(Ca, 1e-14))
                st.markdown(f'<div class="result-card"><p class="result-label">pH Larutan</p><p class="result-value">{pH:.4f} <span style="font-size:16px; color:#e8a045;"></span></p></div>', unsafe_allow_html=True)
                st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (pH = -log[H⁺]):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>[H⁺] = Molaritas Asam Kuat = {Ca} M</p><p style='margin: 0 0 8px 0;'>pH = -log({Ca}) = <b>{pH:.4f}</b></p></div></div>""", unsafe_allow_html=True)
            else:
                Ka_a   = st.number_input("Ka", 1e-20, value=1.8e-5, key="as_Ka")
                h_plus = math.sqrt(Ka_a * Ca)
                pH     = -math.log10(h_plus)
                st.markdown(f'<div class="result-card"><p class="result-label">pH Larutan</p><p class="result-value">{pH:.4f} <span style="font-size:16px; color:#e8a045;"></span></p></div>', unsafe_allow_html=True)
                st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (pH Asam Lemah):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>[H⁺] = √(Ka × Ca) = √({Ka_a} × {Ca}) = {h_plus:.4e} M</p><p style='margin: 0 0 8px 0;'>pH = -log({h_plus:.4e}) = <b>{pH:.4f}</b></p></div></div>""", unsafe_allow_html=True)

        with tab_basa:
            jenis_b = st.radio("Jenis basa:", ["Basa Kuat", "Basa Lemah"], horizontal=True, key="pilihan_basa_kuat_lemah")
            Cb = st.number_input("Konsentrasi C (M)", 1e-14, value=0.1, key="bs_C")
            if jenis_b == "Basa Kuat":
                pH = 14 + math.log10(Cb)
                st.markdown(f'<div class="result-card"><p class="result-label">pH Larutan</p><p class="result-value">{pH:.4f} <span style="font-size:16px; color:#e8a045;"></span></p></div>', unsafe_allow_html=True)
                st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (pH = 14 - pOH):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>[OH⁻] = {Cb} M</p><p style='margin: 0 0 8px 0;'>pOH = -log({Cb}) = {-math.log10(Cb):.4f}</p><p style='margin: 0 0 8px 0;'>pH = 14 - pOH = <b>{pH:.4f}</b></p></div></div>""", unsafe_allow_html=True)
            else:
                Kb_b   = st.number_input("Kb", 1e-20, value=1.8e-5, key="bs_Kb")
                oh_min = math.sqrt(Kb_b * Cb)
                pH     = 14 + math.log10(oh_min)
                st.markdown(f'<div class="result-card"><p class="result-label">pH Larutan</p><p class="result-value">{pH:.4f} <span style="font-size:16px; color:#e8a045;"></span></p></div>', unsafe_allow_html=True)
                st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (pH Basa Lemah):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>[OH⁻] = √(Kb × Cb) = √({Kb_b} × {Cb}) = {oh_min:.4e} M</p><p style='margin: 0 0 8px 0;'>pOH = -log({oh_min:.4e}) = {-math.log10(oh_min):.4f}</p><p style='margin: 0 0 8px 0;'>pH = 14 - pOH = <b>{pH:.4f}</b></p></div></div>""", unsafe_allow_html=True)

        with tab_ka:
            Ck  = st.number_input("Konsentrasi C (M)", 1e-10, value=0.1, key="kk_C")
            pHk = st.number_input("pH terukur", 0.0, 14.0, value=2.87, key="kk_pH")
            H   = 10 ** (-pHk)
            if Ck > H:
                ka_pred = H ** 2 / (Ck - H)
                st.markdown(f'<div class="result-card"><p class="result-label">Ka Prediksi</p><p class="result-value">{ka_pred:.4e} <span style="font-size:16px; color:#e8a045;"></span></p></div>', unsafe_allow_html=True)
                st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (Ka = [H⁺]² / (C - [H⁺])):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>[H⁺] = 10^(-pH) = 10^(-{pHk}) = {H:.4e} M</p><p style='margin: 0 0 8px 0;'>Ka = ({H:.4e})² / ({Ck} - {H:.4e})</p><p style='margin: 0 0 8px 0;'>Ka = <b>{ka_pred:.4e}</b></p></div></div>""", unsafe_allow_html=True)

        with tab_dilusi:
            jenis_d = st.radio("Jenis larutan:", ["Asam Kuat", "Asam Lemah", "Basa Kuat", "Basa Lemah"], horizontal=True, key="dp_j")

            C1d = st.number_input("C₁ (M)", 1e-14, value=0.1, key="dp_C1")
            V1d = st.number_input("V₁ (mL)", 0.001, value=10.0, key="dp_V1")
            V2d = st.number_input("V₂ (mL)", 0.001, value=100.0, key="dp_V2")
            Kd  = st.number_input("Ka / Kb", 1e-20, value=1.8e-5, key="dp_K") if "Lemah" in jenis_d else None

            # Menghitung pH awal (pH1) secara manual
            c1_safe = max(C1d, 1e-14)
            if jenis_d == "Asam Kuat":
                pH1 = -math.log10(c1_safe)
            elif jenis_d == "Asam Lemah":
                pH1 = -math.log10(math.sqrt(Kd * c1_safe))
            elif jenis_d == "Basa Kuat":
                pH1 = 14 + math.log10(c1_safe)
            elif jenis_d == "Basa Lemah":
                pH1 = 14 + math.log10(math.sqrt(Kd * c1_safe))

            # Hitung konsentrasi baru setelah pengenceran
            C2d = C1d * V1d / V2d
            c2_safe = max(C2d, 1e-14)

            # Menghitung pH akhir (pH2) secara manual
            if jenis_d == "Asam Kuat":
                pH2 = -math.log10(c2_safe)
            elif jenis_d == "Asam Lemah":
                pH2 = -math.log10(math.sqrt(Kd * c2_safe))
            elif jenis_d == "Basa Kuat":
                pH2 = 14 + math.log10(c2_safe)
            elif jenis_d == "Basa Lemah":
                pH2 = 14 + math.log10(math.sqrt(Kd * c2_safe))

            st.markdown(f'<div class="result-card"><p class="result-label">pH Akhir</p><p class="result-value">{pH2:.4f} (Awal: {pH1:.4f}) <span style="font-size:16px; color:#e8a045;"></span></p></div>', unsafe_allow_html=True)
            
            st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (Efek Dilusi Terhadap pH):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>1. C₂ baru = (C₁ × V₁) / V₂ = ({C1d} × {V1d}) / {V2d} = <b>{C2d:.4e} M</b></p><p style='margin: 0 0 8px 0;'>2. pH awal (C₁) → <b>pH₁ = {pH1:.4f}</b></p><p style='margin: 0 0 8px 0;'>3. pH akhir (C₂) → <b>pH₂ = {pH2:.4f}</b></p><p style='margin: 0 0 8px 0;'>4. ΔpH = <b>{abs(pH2 - pH1):.4f}</b></p></div></div>""", unsafe_allow_html=True)

    # ==========================================
    # MODUL 4: LARUTAN BUFFER
    # ==========================================
    elif st.session_state.menu_aktif == "Buffer":
        st.markdown("### 🧪 Pembuatan Larutan Buffer")
        tab_ph_buf, tab_rasio, tab_beta = st.tabs([
            "🧮 Hitung pH Buffer", "⚖️ Hitung Rasio [A⁻]/[HA]", "📊 Kapasitas Buffer (β)"
        ])

        with tab_ph_buf:
            pKa_b  = st.number_input("pKa asam", 0.0, 14.0, value=4.74, key="pka_buffer_langsung")
            ab     = st.number_input("[A⁻] Basa Konjugat (M)", 0.0001, value=0.1, key="base_konjugat_M")
            ha     = st.number_input("[HA] Asam (M)", 0.0001, value=0.1, key="acid_lemah_M")
            ph_buf = pKa_b + math.log10(ab / ha)
            
            st.markdown(f'<div class="result-card"><p class="result-label">pH Buffer</p><p class="result-value">{ph_buf:.4f} <span style="font-size:16px; color:#e8a045;"></span></p></div>', unsafe_allow_html=True)
            
            st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (Henderson-Hasselbalch):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>pH = pKa + log([A⁻] / [HA])</p><p style='margin: 0 0 8px 0;'>pH = {pKa_b} + log({ab} / {ha})</p><p style='margin: 0 0 8px 0;'>pH = {pKa_b} + {math.log10(ab / ha):.4f}</p><p style='margin: 0 0 8px 0;'>pH = <b>{ph_buf:.4f}</b></p></div></div>""", unsafe_allow_html=True)

        with tab_rasio:
            pHt    = st.number_input("pH target", 0.0, 14.0, value=5.0, key="ph_target_buffer")
            pKa_r  = st.number_input("pKa asam", 0.0, 14.0, value=4.74, key="br_pka")
            Ctot   = st.number_input("Konsentrasi total (M)", 0.001, value=0.2, key="kons_total_buffer")
            ratio  = 10 ** (pHt - pKa_r)
            a_min  = Ctot * ratio / (1 + ratio)
            ha_val = Ctot / (1 + ratio)
            
            st.markdown(f'<div class="result-card"><p class="result-label">Rasio [A⁻]/[HA]</p><p class="result-value">{ratio:.5f} <span style="font-size:16px; color:#e8a045;">([A⁻]={a_min:.4f}M)</span></p></div>', unsafe_allow_html=True)
            
            st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (Persamaan Komposisi Rasio):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>[A⁻]/[HA] = 10^(pH - pKa) = 10^({pHt} - {pKa_r}) = <b>{ratio:.5f}</b></p><p style='margin: 0 0 8px 0;'>Fraksi komponen:</p><p style='margin: 0 0 8px 0;'>&nbsp;&nbsp;• [A⁻] = ({ratio:.5f} / (1 + {ratio:.5f})) × {Ctot} M = <b>{a_min:.4f} M</b></p><p style='margin: 0 0 8px 0;'>&nbsp;&nbsp;• [HA] = {Ctot} - {a_min:.4f} = <b>{ha_val:.4f} M</b></p></div></div>""", unsafe_allow_html=True)

        with tab_beta:
            Cbc    = st.number_input("Konsentrasi total (M)", 0.0001, value=0.1, key="bc_C")
            Ka_bc  = st.number_input("Ka", 1e-20, value=1.8e-5, key="bc_Ka")
            pH_bc  = st.number_input("pH larutan", 0.0, 14.0, value=4.74, key="bc_pH")
            H_bc   = 10 ** (-pH_bc)
            beta   = 2.303 * Cbc * (Ka_bc * H_bc) / (Ka_bc + H_bc) ** 2
            
            st.markdown(f'<div class="result-card"><p class="result-label">Kapasitas Buffer (β)</p><p class="result-value">{beta:.4e} <span style="font-size:16px; color:#e8a045;"></span></p></div>', unsafe_allow_html=True)
            
            st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (Van Slyke Equation):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>β = 2.303 × C_tot × (Ka × [H⁺]) / (Ka + [H⁺])²</p><p style='margin: 0 0 8px 0;'>[H⁺] = 10^(-{pH_bc}) = {H_bc:.4e} M</p><p style='margin: 0 0 8px 0;'>β = 2.303 × {Cbc} × ({Ka_bc:.2e} × {H_bc:.2e}) / ({Ka_bc:.2e} + {H_bc:.2e})²</p><p style='margin: 0 0 8px 0;'>β = <b>{beta:.4e}</b></p></div></div>""", unsafe_allow_html=True)

    # ==========================================
    # MODUL 5: PROPAGASI GALAT & STATISTIK
    # ==========================================
    elif st.session_state.menu_aktif == "Galat":
        st.markdown("### 📊 Galat & Propagasi Error")
        tab_ga, tab_prop, tab_stat = st.tabs([
            "📏 Galat Absolut & Relatif", "⚡ Propagasi Error", "📊 Statistik (SD & RSD)"
        ])

        with tab_ga:
            xu    = st.number_input("Nilai terukur", value=9.87, key="nilai_eksperimen_terukur")
            xb    = st.number_input("Nilai benar", value=10.00, key="nilai_teoritis_sebenarnya")
            g_abs = abs(xu - xb)
            g_rel = (g_abs / xb) * 100
            
            st.markdown(f'<div class="result-card"><p class="result-label">Galat Absolut</p><p class="result-value">{g_abs:.5g} <span style="font-size:16px; color:#e8a045;"></span></p></div>', unsafe_allow_html=True)
            
            st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (Akurasi Pengukuran):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>Galat Absolut = |Nilai Terukur - Nilai Benar| = |{xu} - {xb}| = <b>{g_abs:.5g}</b></p><p style='margin: 0 0 8px 0;'>Galat Relatif = (Galat Absolut / Nilai Benar) × 100% = ({g_abs:.5g} / {xb}) × 100 = <b>{g_rel:.3f}%</b></p></div></div>""", unsafe_allow_html=True)

        with tab_prop:
            op     = st.selectbox("Operasi:", [
                "Penjumlahan / Pengurangan (x ± y)",
                "Perkalian / Pembagian (x × y atau x/y)"
            ], key="operasi_propagasi_error")
            x_val  = st.number_input("Nilai x", value=10.0, key="nilai_x_prop")
            dx_val = st.number_input("δx", value=0.05, key="ketidakpastian_x")
            y_val  = st.number_input("Nilai y", value=5.0, key="nilai_y_prop")
            dy_val = st.number_input("δy", value=0.03, key="ketidakpastian_y")

            if "Penjumlahan" in op:
                unc = math.sqrt(dx_val ** 2 + dy_val ** 2)
                st.markdown(f'<div class="result-card"><p class="result-label">Ketidakpastian Akhir</p><p class="result-value">± {unc:.5g} <span style="font-size:16px; color:#e8a045;"></span></p></div>', unsafe_allow_html=True)
                
                st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (δz = √(δx² + δy²)):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>δz = √({dx_val}² + {dy_val}²)</p><p style='margin: 0 0 8px 0;'>δz = √({dx_val**2:.5f} + {dy_val**2:.5f})</p><p style='margin: 0 0 8px 0;'>δz = <b>± {unc:.5g}</b></p></div></div>""", unsafe_allow_html=True)
            else:
                unc = (x_val * y_val) * math.sqrt((dx_val / x_val) ** 2 + (dy_val / y_val) ** 2)
                st.markdown(f'<div class="result-card"><p class="result-label">Ketidakpastian Akhir</p><p class="result-value">± {unc:.5g} <span style="font-size:16px; color:#e8a045;"></span></p></div>', unsafe_allow_html=True)
                
                st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (δz/z = √((δx/x)² + (δy/y)²)):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>z = x × y = {x_val * y_val}</p><p style='margin: 0 0 8px 0;'>δz = {x_val * y_val} × √(({dx_val}/{x_val})² + ({dy_val}/{y_val})²)</p><p style='margin: 0 0 8px 0;'>δz = <b>± {unc:.5g}</b></p></div></div>""", unsafe_allow_html=True)

        with tab_stat:
            raw = st.text_area("Data pengukuran (pisahkan dengan koma):", value="9.87, 9.92, 9.85, 9.90, 9.88", key="area_input_data_laboratorium")
            
            # Parsing data manual khas mahasiswa
            arr = []
            for t in raw.split(','):
                if t.strip() != "":
                    arr.append(float(t.strip()))
                    
            if len(arr) >= 2:
                mean_s = sum(arr) / len(arr)
                
                # Hitung Standar Deviasi manual tanpa fungsi otomatisasi rumit sekali baris
                jumlah_kuadrat = 0
                for xi in arr:
                    jumlah_kuadrat += (xi - mean_s) ** 2
                sd_s = math.sqrt(jumlah_kuadrat / (len(arr) - 1))
                
                rsd    = (sd_s / mean_s) * 100
                
                st.markdown(f'<div class="result-card"><p class="result-label">Rata-rata ± SD</p><p class="result-value">{mean_s:.4g} ± {sd_s:.4g} <span style="font-size:16px; color:#e8a045;">(RSD: {rsd:.3f}%)</span></p></div>', unsafe_allow_html=True)
                
                st.markdown(f"""<div style="background: rgba(255,255,255,0.04); padding: 20px; border-radius: 10px; border: 1px dashed rgba(232,160,69,0.4); font-family: 'Courier New', monospace; margin-top: 15px;"><p style="margin: 0 0 12px 0; color: #e8a045; font-weight: 600; font-size: 13px;">📋 Penyelesaian (Statistik Deskriptif):</p><div style="font-size: 13px; color: #cfcfcf; line-height: 1.7; padding-left: 5px;"><p style='margin: 0 0 8px 0;'>1. Rata-rata (μ) = Σx / n = <b>{mean_s:.4g}</b></p><p style='margin: 0 0 8px 0;'>2. Standar Deviasi (SD) = √(Σ(xᵢ - μ)² / (n - 1)) = <b>{sd_s:.4g}</b></p><p style='margin: 0 0 8px 0;'>3. RSD = (SD / μ) × 100% = ({sd_s:.4g} / {mean_s:.4g}) × 100 = <b>{rsd:.3f}%</b></p></div></div>""", unsafe_allow_html=True)

# Footer aplikasi bawaan awal
st.divider()
st.markdown(
    '<p style="text-align:center; font-size:12px; color:#9e9e9e;">⚗️ Kalkulator Analisis Kuantitatif · Kimia Analitik</p>',
    unsafe_allow_html=True
)
