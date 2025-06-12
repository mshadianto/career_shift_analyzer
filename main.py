# Career Shift Analyzer - Landing Page
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Career Shift Analyzer", layout="wide")

st.title("🔮 Career Shift Analyzer")

# Optional logo if available in assets
try:
    logo = Image.open("assets/logo.png")
    st.image(logo, width=120)
except:
    pass

st.markdown("""
Selamat datang di aplikasi **Career Shift Analyzer**! 👋

Aplikasi ini membantu Anda mengevaluasi kesiapan beralih karier ke industri masa depan:
- 🧠 Artificial Intelligence (AI)
- 🔗 Blockchain
- ☀️ Renewable Energy
- 🧬 Biotechnology
- 🚀 Space Exploration

### 🧭 Navigasi Menu:
- **Career Simulation**: Masukkan profil Anda dan dapatkan rekomendasi karier masa depan
- **Skill Gap Analysis**: Lihat perbandingan skill Anda dengan kebutuhan bidang masa depan
- **Career Chat Assistant**: Konsultasikan pertanyaan karier Anda ke AI assistant

> Dibangun oleh Sopian & Faby – untuk masa depan karier yang lebih cerah. 🌟
""")

st.markdown("---")
st.caption("© 2025 Career Shift Analyzer | Powered by Qwen3 via OpenRouter")
