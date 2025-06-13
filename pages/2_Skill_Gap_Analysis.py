import streamlit as st
import pandas as pd

st.set_page_config(page_title="Skill Gap Analysis", layout="wide")
st.title("📊 Skill Gap Analysis")
st.markdown("""
Bandingkan skill yang Anda miliki dengan skill yang dibutuhkan di industri masa depan.
Aplikasi ini akan menampilkan visualisasi sederhana dan saran jalur pembelajaran.
""")

# Dummy skill mapping (bisa diganti dengan data asli)
skill_targets = {
    "Artificial Intelligence": ["python", "sql", "machine learning"],
    "Blockchain": ["crypto", "solidity", "smart contract"],
    "Renewable Energy": ["solar", "sustainability", "electrical"],
    "Biotechnology": ["bioinformatics", "genetics", "lab"],
    "Space Exploration": ["physics", "engineering", "navigation"]
}

selected_field = st.selectbox("Pilih bidang industri masa depan:", list(skill_targets.keys()))
skills_user = st.text_input("Masukkan skill Anda (pisahkan dengan koma)", placeholder="python, teamwork, excel")

if st.button("🔎 Lihat Analisis Skill Gap"):
    user_skills = [s.strip().lower() for s in skills_user.split(",")]
    target_skills = skill_targets[selected_field]
    match = [s for s in user_skills if s in target_skills]
    gap = [s for s in target_skills if s not in user_skills]
    
    st.subheader("✅ Skill yang Dimiliki vs Dibutuhkan")
    
    # Menggunakan Streamlit native chart
    chart_data = pd.DataFrame({
        "Skill": target_skills,
        "Dimiliki": [1 if s in match else 0 for s in target_skills],
        "Kurang": [1 if s not in match else 0 for s in target_skills]
    })
    
    # Bar chart dengan Streamlit
    st.bar_chart(chart_data.set_index("Skill"))
    
    # Alternative: Menggunakan color coding dengan columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.success("**✅ Skill yang Sudah Dimiliki:**")
        if match:
            for skill in match:
                st.write(f"• {skill.title()}")
        else:
            st.write("Belum ada skill yang cocok")
    
    with col2:
        st.error("**❌ Skill yang Perlu Ditingkatkan:**")
        if gap:
            for skill in gap:
                st.write(f"• {skill.title()}")
        else:
            st.write("Semua skill sudah tercukupi!")
    
    # Progress bar untuk visualisasi persentase
    skill_percentage = len(match) / len(target_skills) * 100 if target_skills else 0
    st.subheader(f"📈 Skill Match: {skill_percentage:.1f}%")
    st.progress(skill_percentage / 100)
    
    st.subheader("🎓 Rekomendasi Learning Path")
    if gap:
        for s in gap:
            st.markdown(f"**{s.title()}** → [Cari Kursus di Coursera](https://www.coursera.org/search?query={s})")
    else:
        st.success("🎉 Selamat! Anda sudah memiliki semua skill yang dibutuhkan!")

st.markdown("---")
st.caption("© 2025 Career Shift Analyzer")