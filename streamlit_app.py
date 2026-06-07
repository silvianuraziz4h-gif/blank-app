import streamlit as st
import math

# Set up halaman standar (tanpa aneh-aneh)
st.set_page_config(
    page_title="Kalkulator Kimia Analitik",
    page_icon="🧪",
    layout="centered"  # Diubah ke centered biar lebih umum digunakan
)

# Judul Utama menggunakan komponen standar Streamlit
st.title("Kalkulator Analisis Kuantitatif")
st.write("Aplikasi untuk membantu perhitungan laboratorium kimia analitik.")
st.markdown("---")

# Inisialisasi menu navigasi menggunakan sidebar standar
menu = st.sidebar.selectbox(
    "Pilih Modul Kalkulator:",
    ["Home", "Pengenceran Larutan", "Konsentrasi & Stoikiometri", "Kesetimbangan & pH", "Larutan Buffer", "Galat & Statistik"]
)

# ---------------------------------------------------------------
# HALAMAN HOME
# ---------------------------------------------------------------
if menu == "Home":
    st.subheader("Selamat Datang di Aplikasi Kalkulator Kimia")
    st.write("Aplikasi ini dibuat untuk mempermudah perhitungan analisis kuantitatif di laboratorium.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**🎯 Tujuan**\n\nMenyediakan alat hitung cepat untuk meminimalisir kesalahan desimal saat praktikum.")
    with col2:
        st.success("**✨ Manfaat**\n\nMembantu verifikasi data hasil pengenceran, titrasi, dan perhitungan statistik galat.")

# ---------------------------------------------------------------
# MODUL PENGENCERAN
# ---------------------------------------------------------------
elif menu == "Pengenceran Larutan":
    st.subheader("💧 Modul Pengenceran Larutan")
    
    pilihan_sub = st.radio("Metode Pengenceran:", ["Rumus C1.V1 = C2.V2", "Pengenceran Serial", "Faktor Pengenceran"])
    
    if pilihan_sub == "Rumus C1.V1 = C2.V2":
        st.write("**Rumus Dasarnya:** $C_1 \\times V_1 = C_2 \\times V_2$")
        
        cari = st.selectbox("Variabel yang ingin dicari:", ["C2 (Konsentrasi Akhir)", "V2 (Volume Akhir)", "C1 (Konsentrasi Awal)", "V1 (Volume Awal)"])
        satuan_kons = st.text_input("Masukkan Satuan Konsentrasi (misal: M, ppm, %):", value="M")
        
        col1, col2 = st.columns(2)
        
        if cari == "C2 (Konsentrasi Akhir)":
            with col1:
                c1 = col1.number_input("C1 (Konsentrasi awal):", value=1.0, format="%.4f")
                v1 = col1.number_input("V1 (Volume awal dalam mL):", value=10.0, format="%.2f")
            with col2:
                v2 = col2.number_input("V2 (Volume akhir dalam mL):", value=100.0, format="%.2f")
            
            if v2 > 0:
                hasil = (c1 * v1) / v2
                st.success(f"**Hasil Perhitungan C2:** {hasil:.6f} {satuan_kons}")
                st.code(f"Langkah Kerja:\nC2 = (C1 x V1) / V2\nC2 = ({c1} x {v1}) / {v2}\nC2 = {hasil:.6f}")
                
        elif cari == "V2 (Volume Akhir)":
            with col1:
                c1 = col1.number_input("C1 (Konsentrasi awal):", value=1.0, format="%.4f")
                v1 = col1.number_input("V1 (Volume awal dalam mL):", value=10.0, format="%.2f")
            with col2:
                c2 = col2.number_input("C2 (Konsentrasi akhir):", value=0.1, format="%.4f")
                
            if c2 > 0:
                hasil = (c1 * v1) / c2
                st.success(f"**Hasil Perhitungan V2:** {hasil:.2f} mL")
                st.code(f"Langkah Kerja:\nV2 = (C1 x V1) / C2\nV2 = ({c1} x {v1}) / {c2}\nV2 = {hasil:.2f} mL")

        elif cari == "C1 (Konsentrasi Awal)":
            with col1:
                v1 = col1.number_input("V1 (Volume awal dalam mL):", value=10.0, format="%.2f")
                c2 = col1.number_input("C2 (Konsentrasi akhir):", value=0.1, format="%.4f")
            with col2:
                v2 = col2.number_input("V2 (Volume akhir dalam mL):", value=100.0, format="%.2f")
                
            if v1 > 0:
                hasil = (c2 * v2) / v1
                st.success(f"**Hasil Perhitungan C1:** {hasil:.6f} {satuan_kons}")
                st.code(f"Langkah Kerja:\nC1 = (C2 x V2) / V1\nC1 = ({c2} x {v2}) / {v1}\nC1 = {hasil:.6f}")

        elif cari == "V1 (Volume Awal)":
            with col1:
                c1 = col1.number_input("C1 (Konsentrasi awal):", value=1.0, format="%.4f")
                c2 = col1.number_input("C2 (Konsentrasi akhir):", value=0.1, format="%.4f")
            with col2:
                v2 = col2.number_input("V2 (Volume akhir dalam mL):", value=100.0, format="%.2f")
                
            if c1 > 0:
                hasil = (c2 * v2) / c1
                st.success(f"**Hasil Perhitungan V1 (Volume yang harus dipipet):** {hasil:.2f} mL")
                st.code(f"Langkah Kerja:\nV1 = (C2 x V2) / C1\nV1 = ({c2} x {v2}) / {c1}\nV1 = {hasil:.2f} mL")

    elif pilihan_sub == "Pengenceran Serial":
        st.write("Perhitungan pengenceran bertingkat (serial dilution).")
        c0 = st.number_input("Konsentrasi Larutan Induk (Stok):", value=100.0)
        n_tabung = st.number_input("Jumlah Tabung Pengenceran:", min_value=1, max_value=10, value=5)
        v_aliquot = st.number_input("Volume sampel yang dipindahkan (mL):", value=1.0)
        v_total = st.number_input("Volume total campuran di tabung (mL):", value=10.0)
        
        if v_aliquot >= v_total:
            st.error("Error: Volume aliquot tidak boleh lebih besar atau sama dengan volume total!")
        else:
            faktor = v_aliquot / v_total
            data_tabel = []
            
            # Perulangan manual ala mahasiswa
            kons_sekarang = c0
            data_tabel.append({"Tabung": "Induk (Stok)", "Konsentrasi": kons_sekarang})
            
            for i in range(1, n_tabung + 1):
                kons_sekarang = kons_sekarang * faktor
                data_tabel.append({"Tabung": f"Tabung {i}", "Konsentrasi": float(f"{kons_sekarang:.4f}")})
                
            st.write("**Hasil Konsentrasi Tiap Tabung:**")
            st.table(data_tabel)  # Menggunakan tabel bawaan streamlit yang standar

    elif pilihan_sub == "Faktor Pengenceran":
        v_awal = st.number_input("Volume Awal Sampel (mL):", value=2.0)
        v_akhir = st.number_input("Volume Akhir Setelah Diencerkan (mL):", value=50.0)
        
        if v_awal > 0:
            fp = v_akhir / v_awal
            st.success(f"Faktor Pengenceran (FP) = **{fp:.2f} kali**")
            st.info(f"Artinya sampel diencerkan dengan perbandingan 1 : {fp:.2f}")

# ---------------------------------------------------------------
# MODUL STOIKIOMETRI & KONVERSI
# ---------------------------------------------------------------
elif menu == "Konsentrasi & Stoikiometri":
    st.subheader("🔄 Modul Satuan Konsentrasi & Stoikiometri")
    
    tab1, tab2 = st.tabs(["Konversi Satuan", "Hitung Mol Dasar"])
    
    with tab1:
        st.write("Fitur konversi sederhana antara Molaritas dan ppm.")
        pilihan_konv = st.selectbox("Jenis Konversi:", ["Molaritas (M) ke ppm (mg/L)", "ppm (mg/L) ke Molaritas (M)"])
        nilai_input = st.number_input("Masukkan Nilai Konsentrasi:", value=0.1, format="%.4f")
        mr_zat = st.number_input("Berat Molekul / Mr Zat (g/mol):", value=58.44)
        
        if pilihan_konv == "Molaritas (M) ke ppm (mg/L)":
            # Rumus manual: M * Mr * 1000
            hasil_ppm = nilai_input * mr_zat * 1000
            st.success(f"Hasil Konversi: **{hasil_ppm:.2f} ppm (mg/L)**")
        else:
            # Rumus manual: ppm / (Mr * 1000)
            hasil_m = nilai_input / (mr_zat * 1000)
            st.success(f"Hasil Konversi: **{hasil_m:.6f} M**")
            
    with tab2:
        opsi_mol = st.selectbox("Pilih Parameter yang Diketahui:", ["Mencari Mol dari Massa", "Mencari Massa dari Mol"])
        if opsi_mol == "Mencari Mol dari Massa":
            massa = st.number_input("Massa Zat (gram):", value=5.85)
            mr = st.number_input("Mr Zat (g/mol):", value=58.44, key="mr_mol")
            if mr > 0:
                mol = massa / mr
                st.success(f"Jumlah Mol = **{mol:.4f} mol**")
        else:
            mol_input = st.number_input("Jumlah Mol:", value=0.1)
            mr = st.number_input("Mr Zat (g/mol):", value=58.44, key="mr_massa")
            massa_hasil = mol_input * mr
            st.success(f"Massa Zat = **{massa_hasil:.4f} gram**")

# ---------------------------------------------------------------
# MODUL PH
# ---------------------------------------------------------------
elif menu == "Kesetimbangan & pH":
    st.subheader("🌈 Modul Perhitungan pH Larutan")
    
    Kategori = st.selectbox("Sifat Larutan:", ["Asam Kuat", "Asam Lemah", "Basa Kuat", "Basa Lemah"])
    konsetrasi_zat = st.number_input("Konsentrasi Larutan (M):", value=0.01, format="%.5f")
    
    if Kategori == "Asam Kuat":
        if konsetrasi_zat > 0:
            ph = -math.log10(konsetrasi_zat)
            st.success(f"pH Larutan Asam Kuat = **{ph:.2f}**")
            
    elif Kategori == "Asam Lemah":
        ka = st.number_input("Nilai Tetapan Asam (Ka):", value=1.8e-5, format="%.2e")
        if konsetrasi_zat > 0 and ka > 0:
            h_plus = math.sqrt(ka * konsetrasi_zat)
            ph = -math.log10(h_plus)
            st.success(f"pH Larutan Asam Lemah = **{ph:.2f}**")
            st.write(f"Konsentrasi [H+] = {h_plus:.2e} M")
            
    elif Kategori == "Basa Kuat":
        if konsetrasi_zat > 0:
            poh = -math.log10(konsetrasi_zat)
            ph = 14 - poh
            st.success(f"pH Larutan Basa Kuat = **{ph:.2f}**")
            
    elif Kategori == "Basa Lemah":
        kb = st.number_input("Nilai Tetapan Basa (Kb):", value=1.8e-5, format="%.2e")
        if konsetrasi_zat > 0 and kb > 0:
            oh_min = math.sqrt(kb * konsetrasi_zat)
            poh = -math.log10(oh_min)
            ph = 14 - poh
            st.success(f"pH Larutan Basa Lemah = **{ph:.2f}**")

# ---------------------------------------------------------------
# MODUL BUFFER
# ---------------------------------------------------------------
elif menu == "Larutan Buffer":
    st.subheader("🧪 Perhitungan pH Buffer (Henderson-Hasselbalch)")
    
    pka = st.number_input("Masukkan pKa Asam Lemah:", value=4.74)
    mol_basa_konj = st.number_input("Konsentrasi / Mol Basa Konjugasi [A-]:", value=0.1)
    mol_asam_lemah = st.number_input("Konsentrasi / Mol Asam Lemah [HA]:", value=0.1)
    
    if mol_basa_konj > 0 and mol_asam_lemah > 0:
        log_bagian = math.log10(mol_basa_konj / mol_asam_lemah)
        ph_buffer = pka + log_bagian
        st.success(f"pH Larutan Penyangga (Buffer) = **{ph_buffer:.2f}**")
        st.code(f"Rumus: pH = pKa + log([Basa Konjugat] / [Asam])\npH = {pka} + log({mol_basa_konj} / {mol_asam_lemah})\npH = {ph_buffer:.2f}")

# ---------------------------------------------------------------
# MODUL GALAT
# ---------------------------------------------------------------
elif menu == "Galat & Statistik":
    st.subheader("📊 Modul Perhitungan Statistik Laboratorium")
    
    st.write("Masukkan data hasil pengamatan Anda untuk mencari rata-rata, SD, dan RSD.")
    input_data = st.text_area("Masukkan data angka (pisahkan dengan koma saja, contoh: 10.1, 10.2, 9.9, 10.0):", value="9.87, 9.92, 9.85, 9.90, 9.88")
    
    # Proses pemisahan string data manual ala mahasiswa
    try:
        list_angka = [float(x.strip()) for x in input_data.split(",") if x.strip() != ""]
        
        if len(list_angka) >= 2:
            n = len(list_angka)
            rata_rata = sum(list_angka) / n
            
            # Hitung Standar Deviasi (SD) manual sampel (n-1)
            jumlah_kuadrat_selisih = sum((bi - rata_rata) ** 2 for bi in list_angka)
            sd = math.sqrt(jumlah_kuadrat_selisih / (n - 1))
            
            # Hitung RSD
            rsd = (sd / rata_rata) * 100
            
            st.write("---")
            st.info(f"Jumlah Data (n) = {n}")
            st.success(f"Rata-rata Pengukuran = **{rata_rata:.4f}**")
            st.success(f"Standar Deviasi (SD) = **{sd:.4f}**")
            st.success(f"Relative Standard Deviation (RSD) = **{rsd:.3f} %**")
        else:
            st.warning("Mohon masukkan minimal 2 data data agar bisa dihitung standar deviasinya.")
    except ValueError:
        st.error("Format data salah! Pastikan hanya memasukkan angka yang dipisahkan oleh tanda koma.")

# ---------------------------------------------------------------
# FOOTER STANDAR
# ---------------------------------------------------------------
st.markdown("---")
st.caption("Tugas Kuliah - Aplikasi Kalkulator Kimia Analitik Kuantitatif")
