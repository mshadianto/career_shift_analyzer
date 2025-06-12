import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
    chart_data = pd.DataFrame({
        "Skill": target_skills,
        "Status": ["Dimiliki" if s in match else "Kurang" for s in target_skills]
    })

    fig, ax = plt.subplots()
    colors = ["green" if status == "Dimiliki" else "red" for status in chart_data["Status"]]
    ax.bar(chart_data["Skill"], [1]*len(chart_data), color=colors)
    ax.set_title(f"Skill Mapping untuk {selected_field}")
    ax.set_yticks([])
    st.pyplot(fig)

    st.info(f"Skill yang sudah Anda kuasai: {', '.join(match) if match else '-'}")
    st.warning(f"Skill yang perlu ditingkatkan: {', '.join(gap) if gap else '-'}")

    st.subheader("🎓 Rekomendasi Learning Path")
    for s in gap:
        st.markdown(f"**{s.title()}** → [Cari Kursus di Coursera](https://www.coursera.org/search?query={s})")

st.markdown("---")
st.caption("© 2025 Career Shift Analyzer")

