import streamlit as st
import requests
import json

st.set_page_config(page_title="Career Chat Assistant", layout="wide")

st.title("🤖 Career Chat Assistant")
st.markdown("""
Tanyakan apa saja seputar pergeseran karier ke industri masa depan seperti AI, Blockchain, BioTech, dsb. 
Jawaban dihasilkan oleh model AI melalui OpenRouter. 🧠
""")

# Suggested questions
st.subheader("💡 Pertanyaan Populer:")
col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 Gimana prediksi mu karir komite audit 5 tahun mendatang?"):
        st.session_state.suggested_question = "Gimana prediksi mu karir komite audit 5 tahun mendatang?"
    if st.button("💼 Skill apa yang dibutuhkan untuk AI Engineer?"):
        st.session_state.suggested_question = "Skill apa yang dibutuhkan untuk AI Engineer?"

with col2:
    if st.button("🔗 Bagaimana prospek karir di blockchain?"):
        st.session_state.suggested_question = "Bagaimana prospek karir di blockchain?"
    if st.button("🎯 Tips transisi karir ke tech industry?"):
        st.session_state.suggested_question = "Tips transisi karir ke tech industry?"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to get AI response
def get_ai_response(question):
    try:
        # Check if API key exists
        if "openrouter" not in st.secrets or not st.secrets.openrouter.get("api_key"):
            return "⚠️ API key OpenRouter belum di-setup. Silakan tambahkan di Streamlit Cloud Settings → Secrets."
        
        api_key = st.secrets.openrouter["api_key"]
        
        # OpenRouter API call with free model
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "X-Title": "Career Shift Analyzer"
        }
        
        data = {
            "model": "meta-llama/llama-3.2-3b-instruct:free",  # Free model
            "messages": [
                {
                    "role": "system", 
                    "content": "Kamu adalah konsultan karir yang ahli dalam industri masa depan seperti AI, blockchain, biotech, renewable energy, dan space tech. Berikan saran yang praktis dan actionable dalam bahasa Indonesia."
                },
                {"role": "user", "content": question}
            ],
            "max_tokens": 500,
            "temperature": 0.7
        }
        
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=30
        )
        
        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"]
        elif response.status_code == 401:
            return "🔑 API key tidak valid. Silakan periksa kembali API key OpenRouter Anda."
        elif response.status_code == 402:
            return "💳 Credit OpenRouter habis. Silakan top-up di openrouter.ai/credits"
        else:
            return f"❌ Error {response.status_code}: {response.text}"
            
    except requests.exceptions.Timeout:
        return "⏱️ Request timeout. Silakan coba lagi."
    except requests.exceptions.RequestException as e:
        return f"🌐 Network error: {str(e)}"
    except Exception as e:
        return f"🚫 Unexpected error: {str(e)}"

# Handle suggested questions
if "suggested_question" in st.session_state:
    question = st.session_state.suggested_question
    del st.session_state.suggested_question
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": question})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(question)
    
    # Get and display AI response
    with st.chat_message("assistant"):
        with st.spinner("🤔 Sedang berpikir..."):
            response = get_ai_response(question)
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Chat input
if prompt := st.chat_input("Tanyakan sesuatu tentang karier masa depan..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get and display AI response
    with st.chat_message("assistant"):
        with st.spinner("🤔 Sedang berpikir..."):
            response = get_ai_response(prompt)
            st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Clear chat button
if st.button("🗑️ Clear Chat"):
    st.session_state.messages = []
    st.rerun()

st.markdown("---")
st.caption("© 2025 Career Shift Analyzer | Powered by Llama 3.2 via OpenRouter")