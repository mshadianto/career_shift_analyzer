import streamlit as st
import requests

st.set_page_config(page_title="Career Chat Assistant", layout="wide")
st.title("🤖 Career Chat Assistant")

st.markdown("""
Tanyakan apa saja seputar pergeseran karier ke industri masa depan seperti AI, Blockchain, BioTech, dsb.
Jawaban dihasilkan oleh model Qwen3 melalui OpenRouter. 💬
""")

# Sidebar untuk API Key (gunakan secrets)
API_KEY = st.secrets.get("openrouter", {}).get("api_key", "")
if not API_KEY:
    st.error("API key OpenRouter belum tersedia. Tambahkan di .streamlit/secrets.toml")
    st.stop()

# Fungsi panggil API
@st.cache_data(show_spinner=False)
def chat_with_qwen3(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "qwen3",
        "messages": [
            {"role": "system", "content": "Kamu adalah asisten karier profesional yang membantu user mengevaluasi potensi karier masa depan."},
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"[Error {response.status_code}] Tidak dapat menjawab saat ini."

# Chat input
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Tanyakan sesuatu tentang karier masa depan...")
if user_input:
    st.session_state.chat_history.append(("Anda", user_input))
    with st.spinner("Menjawab..."):
        response = chat_with_qwen3(user_input)
        st.session_state.chat_history.append(("Asisten Karier", response))

# Tampilkan riwayat obrolan
for sender, msg in st.session_state.chat_history:
    if sender == "Anda":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)

st.markdown("---")
st.caption("© 2025 Career Shift Analyzer | Qwen3 Chat via OpenRouter")

