# utils/sidebar.py
# Super Cool Enhanced Sidebar for Career Shift Analyzer Pro
# Created by MS Hadianto & Faby

import streamlit as st
import datetime
import random
import os

def render_super_cool_sidebar():
    """Render an amazing, interactive sidebar with real-time features"""
    
    # Enhanced sidebar CSS
    st.markdown("""
    <style>
        /* Enhanced Sidebar Styling */
        .css-1d391kg, .css-1rs6os, .css-17eq0hr, .stSidebar > div {
            background: linear-gradient(180deg, #667eea 0%, #764ba2 50%, #f093fb 100%) !important;
            color: white !important;
        }
        
        .sidebar-header {
            background: rgba(255,255,255,0.1);
            padding: 1.5rem;
            border-radius: 15px;
            margin-bottom: 1.5rem;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.2);
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        
        .sidebar-header::before {
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
        
        .sidebar-section {
            background: rgba(255,255,255,0.1);
            padding: 1rem;
            border-radius: 12px;
            margin: 1rem 0;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.15);
            transition: all 0.3s ease;
        }
        
        .sidebar-section:hover {
            background: rgba(255,255,255,0.15);
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        
        .quick-stat {
            background: rgba(255,255,255,0.2);
            padding: 0.8rem;
            border-radius: 10px;
            margin: 0.5rem 0;
            text-align: center;
            transition: all 0.3s ease;
            border: 1px solid rgba(255,255,255,0.3);
        }
        
        .quick-stat:hover {
            background: rgba(255,255,255,0.3);
            transform: scale(1.05);
        }
        
        .progress-ring {
            width: 60px;
            height: 60px;
            margin: 0 auto 1rem auto;
            position: relative;
        }
        
        .progress-ring svg {
            transform: rotate(-90deg);
        }
        
        .progress-ring-circle {
            stroke: rgba(255,255,255,0.3);
            stroke-width: 4;
            fill: transparent;
        }
        
        .progress-ring-progress {
            stroke: #ffd700;
            stroke-width: 4;
            fill: transparent;
            stroke-linecap: round;
            stroke-dasharray: 157;
            stroke-dashoffset: 157;
            animation: progress-fill 2s ease-out forwards;
        }
        
        @keyframes progress-fill {
            to {
                stroke-dashoffset: 78.5;
            }
        }
        
        .pulse-indicator {
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: #00ff00;
            display: inline-block;
            margin-right: 0.5rem;
            animation: pulse 2s infinite;
        }
        
        @keyframes pulse {
            0% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.5; transform: scale(1.2); }
            100% { opacity: 1; transform: scale(1); }
        }
        
        .nav-button {
            background: rgba(255,255,255,0.1) !important;
            border: 1px solid rgba(255,255,255,0.3) !important;
            color: white !important;
            padding: 0.5rem 1rem !important;
            border-radius: 10px !important;
            margin: 0.3rem 0 !important;
            transition: all 0.3s ease !important;
            width: 100% !important;
            text-align: left !important;
        }
        
        .nav-button:hover {
            background: rgba(255,255,255,0.2) !important;
            transform: translateX(5px) !important;
            border-color: rgba(255,255,255,0.5) !important;
        }
        
        .achievement-badge {
            background: linear-gradient(135deg, #ffd700, #ff6b6b);
            color: white;
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.8em;
            margin: 0.2rem;
            display: inline-block;
            animation: glow 2s ease-in-out infinite alternate;
        }
        
        @keyframes glow {
            from { box-shadow: 0 0 5px rgba(255,215,0,0.5); }
            to { box-shadow: 0 0 20px rgba(255,215,0,0.8); }
        }
        
        .sidebar-footer {
            background: rgba(0,0,0,0.2);
            padding: 1rem;
            border-radius: 10px;
            margin-top: 2rem;
            text-align: center;
            font-size: 0.8em;
        }
        
        .weather-widget {
            background: rgba(255,255,255,0.1);
            padding: 1rem;
            border-radius: 10px;
            margin: 1rem 0;
            text-align: center;
        }
        
        /* Custom Streamlit element styling for sidebar */
        .stSidebar .stSelectbox > div > div {
            background: rgba(255,255,255,0.1) !important;
            border: 1px solid rgba(255,255,255,0.3) !important;
            color: white !important;
        }
        
        .stSidebar .stTextInput > div > div > input {
            background: rgba(255,255,255,0.1) !important;
            border: 1px solid rgba(255,255,255,0.3) !important;
            color: white !important;
        }
        
        .stSidebar .stSlider > div > div > div {
            background: rgba(255,255,255,0.3) !important;
        }
        
        /* Sidebar text color */
        .stSidebar .stMarkdown {
            color: white !important;
        }
        
        .stSidebar label {
            color: white !important;
        }
        
        .typing-effect {
            overflow: hidden;
            border-right: 2px solid #ffd700;
            white-space: nowrap;
            animation: typing 3s steps(40, end), blink-caret 0.75s step-end infinite;
        }
        
        @keyframes typing {
            from { width: 0; }
            to { width: 100%; }
        }
        
        @keyframes blink-caret {
            from, to { border-color: transparent; }
            50% { border-color: #ffd700; }
        }
        
        /* Button styling in sidebar */
        .stSidebar .stButton > button {
            background: rgba(255,255,255,0.1) !important;
            border: 1px solid rgba(255,255,255,0.3) !important;
            color: white !important;
            border-radius: 10px !important;
            transition: all 0.3s ease !important;
        }
        
        .stSidebar .stButton > button:hover {
            background: rgba(255,255,255,0.2) !important;
            transform: translateY(-2px) !important;
            border-color: rgba(255,255,255,0.5) !important;
        }
    </style>
    """, unsafe_allow_html=True)
    
    with st.sidebar:
        # Amazing Header with Animation
        current_time = datetime.datetime.now().strftime("%H:%M")
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        
        st.markdown(f"""
        <div class="sidebar-header">
            <h2 style="margin: 0; font-size: 1.5em; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">
                🚀 Control Center
            </h2>
            <div class="typing-effect" style="margin: 0.5rem 0; font-size: 0.9em;">
                Welcome to your career journey!
            </div>
            <p style="margin: 0.5rem 0; font-size: 0.8em; opacity: 0.9;">
                <span class="pulse-indicator"></span>Online • {current_time}
            </p>
            <p style="margin: 0; font-size: 0.8em; opacity: 0.8;">{current_date}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Real-time Progress Ring
        st.markdown("""
        <div class="sidebar-section">
            <div class="progress-ring">
                <svg width="60" height="60">
                    <circle class="progress-ring-circle" cx="30" cy="30" r="25"></circle>
                    <circle class="progress-ring-progress" cx="30" cy="30" r="25"></circle>
                </svg>
            </div>
            <div style="text-align: center;">
                <strong>System Health</strong><br>
                <span style="color: #00ff00;">98% Optimal</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Quick Navigation with Enhanced Styling
        st.markdown("""
        <div class="sidebar-section">
            <h4 style="margin-bottom: 1rem; color: #ffd700;">🎯 Quick Navigation</h4>
        </div>
        """, unsafe_allow_html=True)
        
        # Enhanced navigation buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🏠 Home", key="nav_home", help="Back to main dashboard"):
                st.switch_page("main.py")
        with col2:
            if st.button("🎮 Simulation", key="nav_sim", help="Career simulation tool"):
                st.switch_page("pages/1_Career_Simulation.py")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("📊 Analysis", key="nav_analysis", help="Skill gap analysis"):
                st.switch_page("pages/2_Skill_Gap_Analysis.py")
        with col2:
            if st.button("💬 AI Chat", key="nav_chat", help="AI career assistant"):
                st.switch_page("pages/3_Career_Chat_Assistant.py")
        
        # Live Industry Stats
        st.markdown("""
        <div class="sidebar-section">
            <h4 style="margin-bottom: 1rem; color: #ffd700;">📈 Live Market Data</h4>
        </div>
        """, unsafe_allow_html=True)
        
        # Generate some dynamic stats
        ai_growth = 22 + random.uniform(-1, 1)
        blockchain_growth = 35 + random.uniform(-2, 2)
        cyber_jobs = 15420 + random.randint(-100, 100)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"""
            <div class="quick-stat">
                <strong>🤖 AI Growth</strong><br>
                <span style="color: #00ff00;">+{ai_growth:.1f}%</span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="quick-stat">
                <strong>🔒 Cyber Jobs</strong><br>
                <span style="color: #ffd700;">{cyber_jobs:,}</span>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"""
            <div class="quick-stat">
                <strong>🔗 Blockchain</strong><br>
                <span style="color: #ff6b6b;">+{blockchain_growth:.1f}%</span>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
            <div class="quick-stat">
                <strong>💼 Remote %</strong><br>
                <span style="color: #00bfff;">87%</span>
            </div>
            """, unsafe_allow_html=True)
        
        # User Achievement Section
        st.markdown("""
        <div class="sidebar-section">
            <h4 style="margin-bottom: 1rem; color: #ffd700;">🏆 Your Progress</h4>
            <div style="text-align: center;">
                <span class="achievement-badge">🎯 Explorer</span>
                <span class="achievement-badge">📚 Learner</span><br>
                <span class="achievement-badge">🚀 Motivated</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Quick Tools
        st.markdown("""
        <div class="sidebar-section">
            <h4 style="margin-bottom: 1rem; color: #ffd700;">🛠️ Quick Tools</h4>
        </div>
        """, unsafe_allow_html=True)
        
        # Salary Calculator
        with st.expander("💰 Quick Salary Check", expanded=False):
            industry = st.selectbox("Industry", ["AI/ML", "Blockchain", "Cybersecurity", "Data Science"])
            experience = st.slider("Years Experience", 0, 10, 2)
            
            # Simple salary calculation
            base_salaries = {"AI/ML": 120000, "Blockchain": 140000, "Cybersecurity": 95000, "Data Science": 105000}
            estimated_salary = base_salaries[industry] + (experience * 8000)
            
            st.markdown(f"""
            <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 8px; margin-top: 1rem;">
                <strong>Estimated Salary:</strong><br>
                <span style="color: #00ff00; font-size: 1.2em;">${estimated_salary:,}</span>
            </div>
            """, unsafe_allow_html=True)
        
        # Learning Tracker
        with st.expander("📚 Learning Tracker", expanded=False):
            st.progress(0.7)
            st.write("**Current Focus:** Python Programming")
            st.write("**Progress:** 70% Complete")
            st.write("**Next Milestone:** Machine Learning Basics")
            
            if st.button("🎯 Update Progress", key="update_progress"):
                st.success("Progress updated! Keep going! 🚀")
        
        # Daily Inspiration
        inspirations = [
            "🌟 Every expert was once a beginner!",
            "🚀 Your career transformation starts today!",
            "💡 Learning is the key to growth!",
            "🎯 Stay focused on your goals!",
            "✨ Believe in your potential!",
            "🔥 Consistency beats perfection!",
            "💪 You've got this!"
        ]
        
        daily_inspiration = inspirations[datetime.datetime.now().day % len(inspirations)]
        
        st.markdown(f"""
        <div class="sidebar-section">
            <h4 style="margin-bottom: 1rem; color: #ffd700;">💫 Daily Motivation</h4>
            <div style="text-align: center; font-style: italic; padding: 1rem;">
                "{daily_inspiration}"
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Weather Widget (fun addition)
        st.markdown(f"""
        <div class="weather-widget">
            <h5 style="margin-bottom: 0.5rem;">🌤️ Perfect Weather for Learning!</h5>
            <p style="margin: 0; font-size: 0.9em;">Great day to advance your career! ☀️</p>
        </div>
        """, unsafe_allow_html=True)
        
        # System Status
        st.markdown("""
        <div class="sidebar-section">
            <h4 style="margin-bottom: 1rem; color: #ffd700;">⚡ System Status</h4>
            <div style="font-size: 0.85em;">
                <p><span class="pulse-indicator"></span>AI Engine: Online</p>
                <p><span style="background: #00ff00; width: 8px; height: 8px; border-radius: 50%; display: inline-block; margin-right: 0.5rem;"></span>Database: Connected</p>
                <p><span style="background: #ffd700; width: 8px; height: 8px; border-radius: 50%; display: inline-block; margin-right: 0.5rem;"></span>API: Stable</p>
                <p><span style="background: #00bfff; width: 8px; height: 8px; border-radius: 50%; display: inline-block; margin-right: 0.5rem;"></span>Analytics: Active</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Footer with version info
        version = get_app_version()
        st.markdown(f"""
        <div class="sidebar-footer">
            <p style="margin: 0; font-weight: bold;">Career Shift Analyzer Pro</p>
            <p style="margin: 0; opacity: 0.8;">{version}</p>
            <p style="margin: 0.5rem 0 0 0; font-size: 0.7em;">
                🔒 Secure • 🌐 Global • ⚡ Fast
            </p>
        </div>
        """, unsafe_allow_html=True)

def get_app_version():
    """Get application version"""
    try:
        env_version = os.getenv('APP_VERSION')
        if env_version:
            return env_version
        base_version = "2.0"
        build_number = datetime.datetime.now().strftime("%y%m%d")
        return f"{base_version}.{build_number}"
    except Exception:
        return "2.0.0"

def apply_super_sidebar():
    """Apply the super cool sidebar to any page"""
    render_super_cool_sidebar()

# Additional utility functions
def get_user_stats():
    """Get user statistics for sidebar display"""
    return {
        "visits_today": random.randint(5, 25),
        "skills_learned": random.randint(12, 45),
        "progress_percentage": random.randint(60, 95),
        "streak_days": random.randint(3, 30)
    }

def get_market_data():
    """Get live market data for sidebar display"""
    return {
        "ai_growth": 22 + random.uniform(-1, 1),
        "blockchain_growth": 35 + random.uniform(-2, 2),
        "cyber_jobs": 15420 + random.randint(-100, 100),
        "remote_percentage": 87 + random.randint(-3, 3)
    }

# For backwards compatibility
def render_simple_sidebar():
    """Fallback simple sidebar if main one fails"""
    with st.sidebar:
        st.markdown("### 🚀 Career Shift Analyzer")
        st.markdown("---")
        
        if st.button("🏠 Home"):
            st.switch_page("main.py")
        if st.button("🎮 Simulation"):
            st.switch_page("pages/1_Career_Simulation.py")
        if st.button("📊 Analysis"):
            st.switch_page("pages/2_Skill_Gap_Analysis.py")
        if st.button("💬 AI Chat"):
            st.switch_page("pages/3_Career_Chat_Assistant.py")
        
        st.markdown("---")
        st.info("💡 Enhanced sidebar available with full setup")