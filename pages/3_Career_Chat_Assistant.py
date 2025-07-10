import streamlit as st
import requests
import json
from datetime import datetime
from typing import Dict, List, Optional
import time

# Page config
st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="🤖",
    layout="wide"
)

# Dark Purple Neon Sci-Fi Theme CSS (consistent with main theme)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Exo+2:wght@300;400;500;600;700&display=swap');
    
    /* Global Dark Theme */
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a0e2e 25%, #2d1b3d 50%, #1a0e2e 75%, #0a0a0a 100%);
        color: #e0e0ff;
    }
    
    /* Animated Background */
    .stApp::before {
        content: '';
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: 
            radial-gradient(circle at 20% 50%, rgba(139, 69, 255, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 80% 20%, rgba(255, 69, 255, 0.1) 0%, transparent 50%),
            radial-gradient(circle at 40% 80%, rgba(69, 139, 255, 0.1) 0%, transparent 50%);
        animation: nebula 10s ease-in-out infinite;
        pointer-events: none;
        z-index: -1;
    }
    
    @keyframes nebula {
        0%, 100% { opacity: 0.7; }
        50% { opacity: 1; }
    }
    
    .chat-header {
        text-align: center;
        padding: 3rem 2rem;
        background: linear-gradient(135deg, rgba(139, 69, 255, 0.2), rgba(255, 69, 255, 0.2));
        border: 2px solid #8b45ff;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 
            0 0 30px rgba(139, 69, 255, 0.5),
            inset 0 0 30px rgba(139, 69, 255, 0.1);
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(10px);
    }
    
    .chat-header::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: linear-gradient(45deg, transparent, rgba(139, 69, 255, 0.1), transparent);
        animation: scan 4s linear infinite;
    }
    
    @keyframes scan {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .chat-header h1 {
        font-family: 'Orbitron', monospace;
        font-weight: 900;
        text-shadow: 
            0 0 10px #8b45ff,
            0 0 20px #8b45ff,
            0 0 30px #8b45ff;
        animation: glow 2s ease-in-out infinite alternate;
        margin: 0;
        position: relative;
        z-index: 1;
    }
    
    @keyframes glow {
        from { text-shadow: 0 0 10px #8b45ff, 0 0 20px #8b45ff, 0 0 30px #8b45ff; }
        to { text-shadow: 0 0 20px #8b45ff, 0 0 30px #8b45ff, 0 0 40px #8b45ff; }
    }
    
    .chat-container {
        background: linear-gradient(145deg, rgba(13, 13, 13, 0.9), rgba(26, 14, 46, 0.9));
        border: 1px solid #8b45ff;
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 0 25px rgba(139, 69, 255, 0.3);
        margin: 2rem 0;
        min-height: 600px;
        display: flex;
        flex-direction: column;
        backdrop-filter: blur(10px);
    }
    
    .message-user {
        background: linear-gradient(135deg, #8b45ff, #ff45ff);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 20px 20px 5px 20px;
        margin: 0.5rem 0 0.5rem 4rem;
        box-shadow: 0 0 15px rgba(139, 69, 255, 0.4);
        animation: slideInRight 0.3s ease;
        font-family: 'Exo 2', sans-serif;
    }
    
    .message-assistant {
        background: linear-gradient(145deg, rgba(139, 69, 255, 0.1), rgba(255, 69, 255, 0.1));
        color: #e0e0ff;
        padding: 1rem 1.5rem;
        border-radius: 20px 20px 20px 5px;
        margin: 0.5rem 4rem 0.5rem 0;
        border-left: 4px solid #00ff88;
        box-shadow: 0 0 15px rgba(0, 255, 136, 0.2);
        animation: slideInLeft 0.3s ease;
        font-family: 'Exo 2', sans-serif;
        border: 1px solid rgba(139, 69, 255, 0.2);
    }
    
    @keyframes slideInRight {
        from { transform: translateX(30px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    @keyframes slideInLeft {
        from { transform: translateX(-30px); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
    }
    
    .chat-input-container {
        position: sticky;
        bottom: 0;
        background: linear-gradient(145deg, rgba(13, 13, 13, 0.95), rgba(26, 14, 46, 0.95));
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 -5px 20px rgba(139, 69, 255, 0.2);
        margin-top: auto;
        border: 1px solid rgba(139, 69, 255, 0.3);
    }
    
    .suggested-prompts {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin: 1rem 0;
    }
    
    .prompt-chip {
        background: rgba(139, 69, 255, 0.2);
        color: #8b45ff;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        border: 1px solid rgba(139, 69, 255, 0.3);
        cursor: pointer;
        transition: all 0.3s ease;
        font-size: 0.9em;
        font-family: 'Exo 2', sans-serif;
    }
    
    .prompt-chip:hover {
        background: rgba(139, 69, 255, 0.3);
        transform: translateY(-2px);
        box-shadow: 0 0 15px rgba(139, 69, 255, 0.4);
        color: #ff45ff;
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .feature-card {
        background: linear-gradient(145deg, rgba(13, 13, 13, 0.9), rgba(26, 14, 46, 0.9));
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 0 20px rgba(139, 69, 255, 0.3);
        border: 1px solid #8b45ff;
        transition: all 0.3s ease;
        text-align: center;
        position: relative;
        overflow: hidden;
        backdrop-filter: blur(10px);
    }
    
    .feature-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(139, 69, 255, 0.2), transparent);
        transition: left 0.5s;
    }
    
    .feature-card:hover::before {
        left: 100%;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        border-color: #ff45ff;
        box-shadow: 0 10px 30px rgba(255, 69, 255, 0.4);
    }
    
    .feature-card h4 {
        color: #ff45ff;
        font-family: 'Orbitron', monospace;
        margin-bottom: 1rem;
        position: relative;
        z-index: 1;
    }
    
    .typing-indicator {
        display: inline-flex;
        align-items: center;
        padding: 1rem 1.5rem;
        background: rgba(139, 69, 255, 0.1);
        border-radius: 20px 20px 20px 5px;
        margin: 0.5rem 4rem 0.5rem 0;
        border: 1px solid rgba(139, 69, 255, 0.3);
    }
    
    .typing-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #8b45ff;
        margin: 0 2px;
        animation: typing 1.4s infinite ease-in-out;
    }
    
    .typing-dot:nth-child(1) { animation-delay: -0.32s; }
    .typing-dot:nth-child(2) { animation-delay: -0.16s; }
    
    @keyframes typing {
        0%, 80%, 100% { transform: scale(0.8); opacity: 0.5; }
        40% { transform: scale(1); opacity: 1; }
    }
    
    .status-indicator {
        display: inline-block;
        width: 10px;
        height: 10px;
        background: #00ff88;
        border-radius: 50%;
        margin-right: 0.5rem;
        animation: pulse 2s infinite;
        box-shadow: 0 0 10px #00ff88;
    }
    
    @keyframes pulse {
        0% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.5; transform: scale(1.1); }
        100% { opacity: 1; transform: scale(1); }
    }
    
    .error-message {
        background: rgba(255, 69, 69, 0.2);
        color: #ff4545;
        border: 1px solid rgba(255, 69, 69, 0.3);
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .success-message {
        background: rgba(0, 255, 136, 0.2);
        color: #00ff88;
        border: 1px solid rgba(0, 255, 136, 0.3);
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    /* Text Elements */
    h1, h2, h3, h4 {
        font-family: 'Orbitron', monospace;
        color: #e0e0ff;
    }
    
    p, span, div {
        font-family: 'Exo 2', sans-serif;
        color: #c0c0ff;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #8b45ff, #ff45ff);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-family: 'Exo 2', sans-serif;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        box-shadow: 0 0 15px rgba(139, 69, 255, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(255, 69, 255, 0.5);
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: linear-gradient(180deg, rgba(13, 13, 13, 0.95), rgba(26, 14, 46, 0.95));
        border-right: 1px solid #8b45ff;
    }
    
    /* Form elements */
    .stTextArea > div > div > textarea {
        background: rgba(13, 13, 13, 0.8);
        color: #e0e0ff;
        border: 1px solid #8b45ff;
        border-radius: 10px;
        font-family: 'Exo 2', sans-serif;
    }
    
    .stTextArea > div > div > textarea:focus {
        border-color: #ff45ff;
        box-shadow: 0 0 10px rgba(255, 69, 255, 0.3);
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .message-user, .message-assistant {
            margin-left: 1rem;
            margin-right: 1rem;
        }
        
        .chat-header {
            padding: 2rem 1rem;
        }
        
        .feature-grid {
            grid-template-columns: 1fr;
        }
    }
</style>
""", unsafe_allow_html=True)

# Configuration for OpenRouter API (Llama 3.2)
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_API_KEY = st.secrets.get("OPENROUTER_API_KEY", "")

# Career-focused system prompt
SYSTEM_PROMPT = """You are an expert AI Career Advisor specializing in emerging technology fields including AI, Blockchain, Cybersecurity, Data Science, and Cloud Computing. Your role is to provide:

1. **Personalized Career Guidance**: Tailored advice based on user's background, goals, and interests
2. **Industry Insights**: Current market trends, salary ranges, growth projections, and skill demands
3. **Learning Roadmaps**: Step-by-step guidance for skill development and career transitions
4. **Job Market Analysis**: Information about job opportunities, company cultures, and career paths
5. **Interview Preparation**: Tips for technical interviews, portfolio building, and networking

**Guidelines:**
- Provide actionable, practical advice
- Use current industry data and trends (as of 2024-2025)
- Be encouraging but realistic about timelines and challenges
- Suggest specific resources, courses, and certifications
- Consider different experience levels (entry, mid, senior)
- Address both technical and soft skills development

**Tone**: Professional yet approachable, supportive, and knowledgeable. Use emojis sparingly for emphasis.

Remember: You're helping people transform their careers and achieve their professional goals in rapidly evolving technology fields."""

def get_ai_response(user_message: str, conversation_history: List[Dict]) -> str:
    """Get response from OpenRouter API using Llama 3.2"""
    
    if not OPENROUTER_API_KEY:
        return "⚠️ **API Configuration Error**: OpenRouter API key not found. Please set up your API key in Streamlit secrets to enable the AI assistant."
    
    try:
        # Prepare messages for API
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        
        # Add conversation history (last 10 messages to stay within context limits)
        for msg in conversation_history[-10:]:
            messages.append(msg)
        
        # Add current user message
        messages.append({"role": "user", "content": user_message})
        
        # API request payload
        payload = {
            "model": "meta-llama/llama-3.2-90b-vision-instruct:free",
            "messages": messages,
            "max_tokens": 1000,
            "temperature": 0.7,
            "top_p": 0.9,
            "stream": False
        }
        
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://career-shift-analyzer.streamlit.app",
            "X-Title": "Career Shift Analyzer Pro"
        }
        
        # Make API request
        response = requests.post(
            OPENROUTER_API_URL,
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            response_data = response.json()
            return response_data["choices"][0]["message"]["content"]
        else:
            error_msg = f"API Error {response.status_code}: {response.text}"
            return f"⚠️ **Service Temporarily Unavailable**: {error_msg[:100]}... Please try again in a moment."
            
    except requests.RequestException as e:
        return f"🔗 **Connection Error**: Unable to reach AI service. Please check your internet connection and try again."
    except Exception as e:
        return f"🤖 **AI Service Error**: {str(e)[:100]}... Please try again or contact support."

def initialize_chat_session():
    """Initialize chat session state"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    if "conversation_started" not in st.session_state:
        st.session_state.conversation_started = False

def display_message(role: str, content: str, timestamp: Optional[str] = None):
    """Display a chat message with proper styling"""
    if timestamp is None:
        timestamp = datetime.now().strftime("%H:%M")
    
    if role == "user":
        st.markdown(f"""
        <div class="message-user">
            <strong>You</strong> <small style="opacity: 0.8;">({timestamp})</small><br>
            {content}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="message-assistant">
            <strong>🤖 AI Career Advisor</strong> <small style="opacity: 0.8;">({timestamp})</small><br>
            {content}
        </div>
        """, unsafe_allow_html=True)

def show_suggested_prompts():
    """Display suggested conversation starters"""
    prompts = [
        "How do I transition into AI/ML from my current role?",
        "What skills are most in-demand for cybersecurity jobs?",
        "Should I learn blockchain development in 2025?",
        "How much can I earn as a data scientist?",
        "What's the best path to become a cloud architect?",
        "How do I prepare for technical interviews?",
        "Which programming language should I learn first?",
        "What are the pros and cons of remote work in tech?"
    ]
    
    st.markdown("### 💡 **Suggested Questions**")
    st.markdown('<div class="suggested-prompts">', unsafe_allow_html=True)
    
    cols = st.columns(2)
    for i, prompt in enumerate(prompts):
        with cols[i % 2]:
            if st.button(prompt, key=f"prompt_{i}", use_container_width=True):
                return prompt
    
    st.markdown('</div>', unsafe_allow_html=True)
    return None

def main():
    """Main function for Career Chat Assistant"""
    
    # Initialize session
    initialize_chat_session()
    
    # Header
    st.markdown("""
    <div class="chat-header">
        <h1 style="font-size: 2.8em; font-weight: 900;">🤖 AI CAREER ASSISTANT</h1>
        <p style="font-size: 1.3em; margin: 1rem 0; opacity: 0.9; position: relative; z-index: 1;">
            Your Personal AI Career Advisor
        </p>
        <p style="font-size: 1em; margin: 0.5rem 0; opacity: 0.8; position: relative; z-index: 1;">
            <span class="status-indicator"></span>
            Powered by Meta Llama 3.2 • Available 24/7 • Expert Career Guidance
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Main content area
    if not st.session_state.conversation_started:
        # Welcome screen
        st.header("👋 Welcome to Your AI Career Journey!")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            ### 🎯 **How I Can Help You:**
            
            **🚀 Career Transitions**
            - Personalized roadmaps for entering AI, Blockchain, Cybersecurity, Data Science
            - Skill gap analysis and learning recommendations
            - Timeline planning and milestone setting
            
            **💼 Job Market Insights**
            - Current salary ranges and growth projections
            - In-demand skills and emerging technologies
            - Company culture insights and job search strategies
            
            **📚 Learning Guidance**
            - Recommended courses, certifications, and resources
            - Project ideas to build your portfolio
            - Interview preparation and technical assessment tips
            
            **🤝 Career Development**
            - Networking strategies and professional branding
            - Leadership skills and soft skills development
            - Long-term career planning and advancement
            """)
        
        with col2:
            st.markdown("""
            ### 📊 **Specializing In:**
            
            🤖 **Artificial Intelligence**
            - Machine Learning
            - Deep Learning
            - Data Science
            - Computer Vision
            - Natural Language Processing
            
            🔗 **Blockchain & Web3**
            - Smart Contracts
            - DeFi Development
            - Cryptocurrency
            - NFT Platforms
            
            🔒 **Cybersecurity**
            - Penetration Testing
            - Security Analysis
            - Compliance
            - Incident Response
            
            ☁️ **Cloud Computing**
            - AWS, Azure, GCP
            - DevOps & SRE
            - Kubernetes
            - Infrastructure as Code
            """)
        
        # Features grid
        st.markdown("### ✨ **AI Assistant Features**")
        st.markdown("""
        <div class="feature-grid">
            <div class="feature-card">
                <h4>🎯 Personalized Advice</h4>
                <p>Tailored recommendations based on your background, goals, and current market trends.</p>
            </div>
            <div class="feature-card">
                <h4>📊 Real-time Data</h4>
                <p>Up-to-date salary information, job market trends, and skill demand analysis.</p>
            </div>
            <div class="feature-card">
                <h4>🛣️ Learning Roadmaps</h4>
                <p>Step-by-step learning paths with specific resources and timeline recommendations.</p>
            </div>
            <div class="feature-card">
                <h4>💡 Interview Prep</h4>
                <p>Technical interview questions, coding challenges, and behavioral interview guidance.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Suggested prompts
        selected_prompt = show_suggested_prompts()
        
        if selected_prompt:
            st.session_state.conversation_started = True
            st.session_state.messages.append({
                "role": "user", 
                "content": selected_prompt,
                "timestamp": datetime.now().strftime("%H:%M")
            })
            st.rerun()
    
    else:
        # Chat interface
        st.markdown('<div class="chat-container">', unsafe_allow_html=True)
        
        # Display conversation history
        if st.session_state.messages:
            for message in st.session_state.messages:
                display_message(
                    message["role"], 
                    message["content"], 
                    message.get("timestamp")
                )
        
        # Chat input area
        st.markdown('<div class="chat-input-container">', unsafe_allow_html=True)
        
        # Input form
        with st.form(key="chat_form", clear_on_submit=True):
            col1, col2 = st.columns([4, 1])
            
            with col1:
                user_input = st.text_area(
                    "Ask me anything about your career...",
                    placeholder="e.g., How do I transition from marketing to data science?",
                    height=80,
                    label_visibility="collapsed"
                )
            
            with col2:
                send_button = st.form_submit_button("Send 🚀", use_container_width=True, type="primary")
        
        # Action buttons
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🔄 New Conversation", use_container_width=True):
                st.session_state.messages = []
                st.session_state.conversation_started = False
                st.rerun()
        
        with col2:
            if st.button("💾 Save Chat", use_container_width=True):
                if st.session_state.messages:
                    chat_export = {
                        "timestamp": datetime.now().isoformat(),
                        "messages": st.session_state.messages
                    }
                    st.download_button(
                        label="📥 Download Chat History",
                        data=json.dumps(chat_export, indent=2),
                        file_name=f"career_chat_{datetime.now().strftime('%Y%m%d_%H%M')}.json",
                        mime="application/json"
                    )
                else:
                    st.info("No conversation to save yet!")
        
        with col3:
            if st.button("❓ Help & Tips", use_container_width=True):
                st.info("""
                **💡 Tips for better conversations:**
                - Be specific about your current role and goals
                - Ask follow-up questions for detailed guidance
                - Mention your experience level and timeline
                - Ask about specific companies or technologies
                """)
        
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Process user input
        if send_button and user_input.strip():
            # Add user message
            st.session_state.messages.append({
                "role": "user",
                "content": user_input.strip(),
                "timestamp": datetime.now().strftime("%H:%M")
            })
            
            # Show typing indicator
            with st.spinner("AI is analyzing your question..."):
                # Get AI response
                conversation_history = [
                    {"role": msg["role"], "content": msg["content"]} 
                    for msg in st.session_state.messages[:-1]
                ]
                
                ai_response = get_ai_response(user_input.strip(), conversation_history)
            
            # Add AI response
            st.session_state.messages.append({
                "role": "assistant",
                "content": ai_response,
                "timestamp": datetime.now().strftime("%H:%M")
            })
            
            # Rerun to show new messages
            st.rerun()
    
    # Sidebar with quick actions and info
    with st.sidebar:
        st.header("🚀 Quick Actions")
        
        if st.button("📊 Skill Gap Analysis", use_container_width=True):
            st.switch_page("pages/2_Skill_Gap_Analysis.py")
        
        if st.button("🎯 Career Simulation", use_container_width=True):
            st.switch_page("pages/1_Career_Simulation.py")
        
        if st.button("🏠 Back to Home", use_container_width=True):
            st.switch_page("main.py")
        
        st.markdown("---")
        
        st.header("💡 Pro Tips")
        st.info("""
        **For Best Results:**
        - Ask specific questions about your situation
        - Mention your experience level
        - Include your timeline/goals
        - Ask for actionable next steps
        """)
        
        st.success("""
        **Popular Topics:**
        - Career transition strategies
        - Salary negotiation tips
        - Learning roadmaps
        - Interview preparation
        - Skill prioritization
        """)
        
        st.markdown("---")
        
        # Chat statistics
        if st.session_state.messages:
            total_messages = len(st.session_state.messages)
            user_messages = len([m for m in st.session_state.messages if m["role"] == "user"])
            
            st.header("📈 Chat Stats")
            st.metric("Total Messages", total_messages)
            st.metric("Your Questions", user_messages)
            st.metric("AI Responses", total_messages - user_messages)

if __name__ == "__main__":
    main()
