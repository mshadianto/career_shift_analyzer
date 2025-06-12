import streamlit as st
import pandas as pd
from utils.recommender import simple_recommender
from utils.future_readiness import calculate_readiness_score

# Konfigurasi awal
st.set_page_config(page_title="🔮 Career Shift Analyzer", layout="wide")
st.title("🔮 Career Shift Analyzer")
st.markdown("**Aplikasi ini membantu Anda menganalisis potensi pergeseran karier ke industri masa depan:**\
\nAI, Blockchain, Renewable Energy, Biotechnology, dan Space Exploration.")

# --- Step 1: Profil Karier Pengguna ---
st.header("📌 Profil Karier Anda Saat Ini")
col1, col2 = st.columns(2)
with col1:
    nama = st.text_input("Nama Lengkap", placeholder="Masukkan nama Anda")
    profesi = st.text_input("Profesi Sekarang", placeholder="Contoh: Akuntan, Guru, Admin, IT Support")
with col2:
    pengalaman = st.slider("Total Pengalaman Kerja (tahun)", 0, 40, 5)
    waktu_belajar = st.selectbox("Waktu Belajar Tersedia per Minggu", [2, 5, 10, 15, 20])

skill = st.text_area("🌟 Skill yang Dimiliki (pisahkan dengan koma)", placeholder="Python, Excel, Komunikasi, SQL")

# --- Step 2: Minat Industri Masa Depan ---
st.header("🚀 Minat Industri Masa Depan")
industries = st.multiselect(
    "Pilih bidang industri masa depan yang menarik bagi Anda:",
    ["Artificial Intelligence", "Blockchain", "Renewable Energy", "Biotechnology", "Space Exploration"]
)

# --- Step 3: Proses Analisis ---
if st.button("🔍 Analisa Karier Masa Depan"):
    with st.spinner("Menganalisis profil dan preferensi Anda..."):
        user_skill_list = [s.strip().lower() for s in skill.split(",")]
        hasil = simple_recommender(user_skill_list, industries)

        st.subheader("🌟 Rekomendasi Potensi Karier Baru:")
        for bidang, jobs in hasil.items():
            st.markdown(f"**🚗 {bidang}:**")
            for job in jobs:
                st.write(f"- {job}")

        # Hitung skor readiness
        skor = calculate_readiness_score(user_skill_list, industries, waktu_belajar)
        st.subheader("📈 Future Industry Readiness Score")
        st.progress(skor / 100)
        st.metric(label="Tingkat Kesiapan Anda", value=f"{skor}/100")

        if skor >= 75:
            st.success("🚀 Anda siap untuk mulai transisi ke industri masa depan!")
        elif skor >= 50:
            st.warning("💡 Kesiapan Anda cukup, tapi masih perlu belajar tambahan.")
        else:
            st.error("🔧 Skill dan waktu belajar masih kurang, perlu pengembangan lebih lanjut.")

# --- Footer ---
st.markdown("---")
st.caption("© 2025 Sopian & Faby – Career Shift to Future Industry App (Beta)")
