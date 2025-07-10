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

# Enhanced Custom CSS for Chat Interface
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .chat-header {
        text-align: center;
        padding: 3rem 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        color: white;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .chat-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
        animation: shine 3s infinite;
    }
    
    @keyframes shine {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    
    .chat-container {
        background: white;
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        margin: 2rem 0;
        border: 2px solid rgba(102, 126, 234, 0.1);
        min-height: 600px;
        display: flex;
        flex-direction: column;
    }
    
    .message-user {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 1rem 1.5rem;
        border-radius: 20px 20px 5px 20px;
        margin: 0.5rem 0 0.5rem 4rem;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
        animation: slideInRight 0.3s ease;
    }
    
    .message-assistant {
        background: linear-gradient(145deg, #f8f9ff, #e8f0fe);
        color: #333;
        padding: 1rem 1.5rem;
        border-radius: 20px 20px 20px 5px;
        margin: 0.5rem 4rem 0.5rem 0;
        border-left: 4px solid #667eea;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        animation: slideInLeft 0.3s ease;
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
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 -5px 20px rgba(0,0,0,0.1);
        margin-top: auto;
    }
    
    .suggested-prompts {
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        margin: 1rem 0;
    }
    
    .prompt-chip {
        background: rgba(102, 126, 234, 0.1);
        color: #667eea;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        border: 1px solid rgba(102, 126, 234, 0.2);
        cursor: pointer;
        transition: all 0.3s ease;
        font-size: 0.9em;
    }
    
    .prompt-chip:hover {
        background: rgba(102, 126, 234, 0.2);
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.2);
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .feature-card {
        background: linear-gradient(145deg, #ffffff, #f8f9ff);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        border-left: 5px solid #667eea;
        transition: all 0.3s ease;
        text-align: center;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.2);
    }
    
    .typing-indicator {
        display: inline-flex;
        align-items: center;
        padding: 1rem 1.5rem;
        background: #f0f2f6;
        border-radius: 20px 20px 20px 5px;
        margin: 0.5rem 4rem 0.5rem 0;
    }
    
    .typing-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #667eea;
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
        background: #28a745;
        border-radius: 50%;
        margin-right: 0.5rem;
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.5; transform: scale(1.1); }
        100% { opacity: 1; transform: scale(1); }
    }
    
    .error-message {
        background: #f8d7da;
        color: #721c24;
        border: 1px solid #f5c6cb;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .success-message {
        background: #d4edda;
        color: #155724;
        border: 1px solid #c3e6cb;
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    /* Responsive design */
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
OPENROUTER_API_KEY = st.secrets.get("OPENROUTER_API_KEY", "")  # Set this in your Streamlit secrets

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
            "model": "meta-llama/llama-3.2-90b-vision-instruct:free",  # Free Llama 3.2 model
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

def show_typing_indicator():
    """Show typing indicator while AI is responding"""
    st.markdown("""
    <div class="typing-indicator">
        <span style="margin-right: 0.5rem;">AI is thinking</span>
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
    </div>
    """, unsafe_allow_html=True)

def main():
    """Main function for Career Chat Assistant"""
    
    # Initialize session
    initialize_chat_session()
    
    # Header
    st.markdown("""
    <div class="chat-header">
        <h1 style="margin: 0; font-size: 2.8em; font-weight: 700;">🤖 AI Career Assistant</h1>
        <p style="font-size: 1.3em; margin: 1rem 0; opacity: 0.9;">
            Your Personal AI Career Advisor
        </p>
        <p style="font-size: 1em; margin: 0.5rem 0; opacity: 0.8;">
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
                <h4 style="color: #667eea; margin-bottom: 1rem;">🎯 Personalized Advice</h4>
                <p>Tailored recommendations based on your background, goals, and current market trends.</p>
            </div>
            <div class="feature-card">
                <h4 style="color: #667eea; margin-bottom: 1rem;">📊 Real-time Data</h4>
                <p>Up-to-date salary information, job market trends, and skill demand analysis.</p>
            </div>
            <div class="feature-card">
                <h4 style="color: #667eea; margin-bottom: 1rem;">🛣️ Learning Roadmaps</h4>
                <p>Step-by-step learning paths with specific resources and timeline recommendations.</p>
            </div>
            <div class="feature-card">
                <h4 style="color: #667eea; margin-bottom: 1rem;">💡 Interview Prep</h4>
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
                    for msg in st.session_state.messages[:-1]  # Exclude the current message
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
    
    st.markdown("---")
    
    # Method 1: Direct simple footer (temporary fix)
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, #667eea, #764ba2); color: white; border-radius: 15px; margin-top: 2rem;">
        <h4>⚠️ Important Disclaimer</h4>
        <p><strong>This platform provides general career guidance for educational purposes only.</strong></p>
        <p>Not a substitute for professional career counseling. AI responses may contain errors.</p>
        <p>Always verify information independently and consult qualified professionals.</p>
        <hr style="border-color: rgba(255,255,255,0.3); margin: 1.5rem 0;">
        <p><strong>© 2025 Career Shift Analyzer Pro</strong></p>
        <p>👥 Developed by <strong>MS Hadianto</strong> & <strong>Faby</strong></p>
        <p>🌟 <a href="https://github.com/mshadianto/career_shift_analyzer" style="color: #ffd700;">View on GitHub</a></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()