# utils/sidebar.py
"""
Enhanced sidebar functionality for Career Shift Analyzer Pro
"""

import streamlit as st
from datetime import datetime

def apply_super_sidebar():
    """Apply enhanced sidebar with navigation and features"""
    
    with st.sidebar:
        # Header
        st.markdown("""
        <div style="text-align: center; padding: 1rem; background: linear-gradient(135deg, rgba(139, 69, 255, 0.2), rgba(255, 69, 255, 0.2)); border-radius: 10px; margin-bottom: 2rem;">
            <h3 style="color: #ff45ff; margin: 0;">🚀 Navigation</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Quick Stats
        st.markdown("### 📊 Quick Stats")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Industries", "8", "+2")
        with col2:
            st.metric("Success Stories", "3", "+1")
        
        # Indonesian Market Section
        st.markdown("### 🇮🇩 Indonesian Market")
        if st.button("🏢 Local Companies", use_container_width=True):
            st.info("Check out our Indonesian companies database!")
        
        if st.button("💰 Salary Indonesia", use_container_width=True):
            st.info("Explore Indonesian salary ranges!")
        
        # Quick Actions
        st.markdown("### ⚡ Quick Actions")
        
        # Language Toggle
        language = st.selectbox(
            "🌐 Language",
            ["🇺🇸 English", "🇮🇩 Indonesia"],
            key="sidebar_language"
        )
        
        # Currency Toggle
        currency = st.selectbox(
            "💱 Currency",
            ["💵 USD", "🇮🇩 IDR"],
            key="sidebar_currency"
        )
        
        # Theme Toggle
        if st.checkbox("🌙 Dark Mode", value=True):
            st.session_state.dark_mode = True
        else:
            st.session_state.dark_mode = False
        
        # Notifications
        if st.checkbox("🔔 Notifications"):
            st.success("✅ New Indonesian salary data available!")
            st.info("💡 AI assistant updates ready")
        
        # Progress Tracker
        st.markdown("### 📈 Your Progress")
        
        progress_data = {
            "Profile Complete": 75,
            "Skills Assessed": 60,
            "Career Plan": 40
        }
        
        for item, progress in progress_data.items():
            st.write(f"**{item}**")
            st.progress(progress / 100)
            st.write(f"{progress}%")
        
        # Recent Activity
        st.markdown("### 🕒 Recent Activity")
        activities = [
            "✅ Completed AI assessment",
            "📊 Viewed salary trends",
            "🏢 Explored tech companies",
            "🎓 Started learning path"
        ]
        
        for activity in activities:
            st.write(f"• {activity}")
        
        # Resources
        st.markdown("### 📚 Resources")
        
        resources = {
            "📖 Learning Guide": "https://example.com/guide",
            "💼 Job Boards": "https://jobstreet.co.id",
            "🎓 Bootcamps": "https://hacktiv8.com",
            "🏛️ Gov Programs": "https://prakerja.go.id"
        }
        
        for resource, url in resources.items():
            if st.button(resource, use_container_width=True):
                st.write(f"Opening: {url}")
        
        # Footer info
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; font-size: 0.8em; color: #888;">
            <p>🇮🇩 Indonesian Edition</p>
            <p>Last updated: """ + datetime.now().strftime("%H:%M") + """</p>
        </div>
        """, unsafe_allow_html=True)

def add_navigation_menu():
    """Add enhanced navigation menu"""
    
    pages = {
        "🏠 Home": "main",
        "🎯 Career Simulation": "1_Career_Simulation", 
        "📊 Skill Analysis": "2_Skill_Gap_Analysis",
        "💬 AI Assistant": "3_Career_Chat_Assistant",
        "🇮🇩 Indonesia Edition": "4_Indonesia_Career_Analyzer"
    }
    
    st.sidebar.markdown("### 🧭 Navigation")
    
    for page_name, page_file in pages.items():
        if st.sidebar.button(page_name, use_container_width=True):
            if page_file == "main":
                st.rerun()
            else:
                st.switch_page(f"pages/{page_file}.py")

def show_feature_status():
    """Show development status of features"""
    
    st.sidebar.markdown("### 🚧 Feature Status")
    
    features = {
        "Career Simulation": "✅ Live",
        "Skill Analysis": "✅ Live", 
        "AI Assistant": "✅ Live",
        "Indonesia Edition": "🆕 New",
        "Job Board API": "🔄 In Progress",
        "Mobile App": "📋 Planned"
    }
    
    for feature, status in features.items():
        st.sidebar.write(f"**{feature}**: {status}")

def add_user_feedback():
    """Add user feedback section"""
    
    st.sidebar.markdown("### 💬 Feedback")
    
    feedback_type = st.sidebar.selectbox(
        "Type",
        ["🐛 Bug Report", "💡 Feature Request", "⭐ General Feedback"]
    )
    
    feedback_text = st.sidebar.text_area("Your feedback:", max_chars=200)
    
    if st.sidebar.button("📤 Send Feedback"):
        if feedback_text:
            st.sidebar.success("✅ Feedback sent! Thank you!")
        else:
            st.sidebar.error("❌ Please enter your feedback first")

# Store sidebar state
def init_sidebar_state():
    """Initialize sidebar state variables"""
    if 'sidebar_language' not in st.session_state:
        st.session_state.sidebar_language = "🇺🇸 English"
    
    if 'sidebar_currency' not in st.session_state:
        st.session_state.sidebar_currency = "💵 USD"
    
    if 'dark_mode' not in st.session_state:
        st.session_state.dark_mode = True