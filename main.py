import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os

# Page config
st.set_page_config(
    page_title="Career Shift Analyzer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Version management
def get_app_version():
    try:
        env_version = os.getenv('APP_VERSION')
        if env_version:
            return env_version
        base_version = "1.4"
        build_number = datetime.now().strftime("%y%m%d")
        return f"{base_version}.{build_number}"
    except:
        return "1.0.0"

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .feature-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
        transition: transform 0.3s ease;
    }
    .feature-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    }
    .stat-card {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem;
        transition: transform 0.3s ease;
    }
    .stat-card:hover {
        transform: scale(1.05);
    }
    .version-info {
        position: fixed;
        top: 10px;
        right: 10px;
        background: rgba(102, 126, 234, 0.1);
        border: 1px solid rgba(102, 126, 234, 0.3);
        border-radius: 20px;
        padding: 0.3rem 0.8rem;
        font-size: 0.8em;
        color: #667eea;
        z-index: 1000;
    }
</style>
""", unsafe_allow_html=True)

# Version display
version = get_app_version()
st.markdown(f"""
<div class="version-info">
    🚀 v{version}
</div>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🚀 Career Shift Analyzer</h1>
    <p style="font-size: 1.2em; margin: 0;">Navigate Your Future in Emerging Industries</p>
</div>
""", unsafe_allow_html=True)

# Hero section
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    ### 🎯 Transform Your Career Journey
    
    Discover opportunities in **AI, Blockchain, Renewable Energy, Biotech,** and more. 
    Get personalized insights, skill gap analysis, and AI-powered career guidance.
    """)
    
    if st.button("🚀 Get Started", type="primary", use_container_width=True):
        st.switch_page("pages/2_Skill_Gap_Analysis.py")

# Quick stats
st.markdown("### 📊 Industry Insights")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stat-card">
        <h3>🤖 AI Jobs</h3>
        <p><strong>+22%</strong> growth rate</p>
        <p>$80K-$180K salary</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-card">
        <h3>🔗 Blockchain</h3>
        <p><strong>+35%</strong> growth rate</p>
        <p>$90K-$200K salary</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-card">
        <h3>🌱 Clean Energy</h3>
        <p><strong>+8%</strong> growth rate</p>
        <p>$65K-$120K salary</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-card">
        <h3>🔒 Cybersecurity</h3>
        <p><strong>+35%</strong> growth rate</p>
        <p>$75K-$150K salary</p>
    </div>
    """, unsafe_allow_html=True)

# Features section
st.markdown("### ✨ Platform Features")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h4>🎯 Career Simulation</h4>
        <p>Interactive career path exploration with real market data and personalized recommendations.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Try Career Simulation", key="sim"):
        st.switch_page("pages/1_Career_Simulation.py")

with col2:
    st.markdown("""
    <div class="feature-card">
        <h4>📊 Skill Gap Analysis</h4>
        <p>Comprehensive skill assessment with learning roadmaps and industry benchmarks.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Analyze Your Skills", key="skills"):
        st.switch_page("pages/2_Skill_Gap_Analysis.py")

with col3:
    st.markdown("""
    <div class="feature-card">
        <h4>🤖 AI Career Assistant</h4>
        <p>24/7 AI-powered career counseling with personalized advice and industry insights.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Chat with AI Assistant", key="chat"):
        st.switch_page("pages/3_Career_Chat_Assistant.py")

# Market trends chart
st.markdown("### 📈 Emerging Industry Trends")

# Sample data for trends
trend_data = {
    'Industry': ['Artificial Intelligence', 'Blockchain & Web3', 'Renewable Energy', 
                'Biotechnology', 'Space Technology', 'Cybersecurity'],
    'Job Growth (%)': [22, 35, 8, 7, 6, 35],
    'Avg Salary (K)': [130, 145, 92, 105, 122, 112],
    'Market Size (B)': [190, 67, 300, 760, 400, 170]
}

df = pd.DataFrame(trend_data)

# Create interactive chart
fig = px.scatter(df, x='Job Growth (%)', y='Avg Salary (K)', 
                size='Market Size (B)', hover_name='Industry',
                title='Industry Growth vs Salary Potential',
                labels={'Job Growth (%)': 'Job Growth Rate (%)', 
                       'Avg Salary (K)': 'Average Salary ($K)'},
                color='Industry',
                size_max=60)

fig.update_layout(
    height=500,
    showlegend=True,
    title_x=0.5
)

st.plotly_chart(fig, use_container_width=True)

# Success stories section
st.markdown("### 🌟 Success Stories")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    **👨‍💻 From Accountant to AI Engineer**
    
    "Used Career Shift Analyzer to transition from finance to AI. 
    The skill gap analysis showed me exactly what to learn. 
    Now earning 60% more at a tech startup!"
    
    *- Sarah, AI Engineer*
    """)

with col2:
    st.success("""
    **🚀 Blockchain Developer Journey**
    
    "The platform's learning roadmap guided me from zero coding 
    experience to landing a blockchain developer role in 8 months. 
    The AI assistant was incredibly helpful!"
    
    *- Ahmad, Blockchain Developer*
    """)

# Quick actions
st.markdown("### 🎯 Quick Actions")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📋 Take Skill Assessment", use_container_width=True):
        st.switch_page("pages/2_Skill_Gap_Analysis.py")

with col2:
    if st.button("💬 Ask AI Career Question", use_container_width=True):
        st.switch_page("pages/3_Career_Chat_Assistant.py")

with col3:
    if st.button("🎓 View Learning Paths", use_container_width=True):
        st.info("Feature coming soon! 🚧")

with col4:
    if st.button("📊 Industry Reports", use_container_width=True):
        st.info("Premium feature - coming soon! 💎")

# Universal Footer
def render_universal_footer():
    current_year = datetime.now().year
    last_updated = datetime.now().strftime("%B %d, %Y")
    
    # Footer CSS
    st.markdown("""
    <style>
    .universal-footer {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem 1rem;
        border-radius: 15px;
        margin-top: 3rem;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.3);
    }
    .footer-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 2rem;
        margin-bottom: 2rem;
    }
    .footer-section h4 {
        color: #ffd700;
        margin-bottom: 1rem;
        font-size: 1.1em;
    }
    .disclaimer-box {
        background: rgba(255,255,255,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        font-size: 0.85em;
    }
    .team-section {
        background: rgba(255,255,255,0.15);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid rgba(255,215,0,0.3);
    }
    .team-members {
        display: flex;
        justify-content: center;
        gap: 1.5rem;
        margin: 1rem 0;
        flex-wrap: wrap;
    }
    .team-member {
        background: rgba(255,255,255,0.2);
        padding: 1rem 1.5rem;
        border-radius: 20px;
        border: 2px solid rgba(255,215,0,0.5);
        transition: all 0.3s ease;
        text-align: center;
        min-width: 140px;
    }
    .team-member:hover {
        transform: translateY(-5px);
        border-color: #ffd700;
        box-shadow: 0 10px 25px rgba(255,215,0,0.3);
    }
    .team-member strong {
        color: #ffd700;
        font-size: 1em;
        display: block;
        margin-bottom: 0.3rem;
    }
    .footer-bottom {
        border-top: 1px solid rgba(255,255,255,0.2);
        padding-top: 1.5rem;
        text-align: center;
        font-size: 0.85em;
        color: rgba(255,255,255,0.95);
    }
    .status-indicator {
        display: inline-block;
        width: 8px;
        height: 8px;
        background: #00ff00;
        border-radius: 50%;
        margin-right: 0.5rem;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    .footer-link {
        color: #ffd700;
        text-decoration: none;
        transition: all 0.3s ease;
    }
    .footer-link:hover {
        color: #fff;
        text-shadow: 0 0 10px #ffd700;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Footer HTML
    footer_html = f"""
    <div class="universal-footer">
        <div class="footer-grid">
            <div class="footer-section">
                <h4>🚀 Career Shift Analyzer</h4>
                <p><span class="status-indicator"></span><strong>Status:</strong> Online</p>
                <p><strong>Version:</strong> v{version}</p>
                <p><strong>Updated:</strong> {last_updated}</p>
                
                <div class="team-section">
                    <h5 style="color: #ffd700; margin-bottom: 1rem; text-align: center;">👥 Development Team</h5>
                    <div class="team-members">
                        <div class="team-member">
                            <strong>🎯 MS Hadianto</strong>
                            <span style="font-size: 0.8em;">Lead Project</span>
                        </div>
                        <div class="team-member">
                            <strong>🤝 Faby</strong>
                            <span style="font-size: 0.8em;">Co-Lead</span>
                        </div>
                    </div>
                    <p style="text-align: center; font-size: 0.85em; color: rgba(255,255,255,0.8); margin-top: 1rem;">
                        <em>Collaborative innovation for career advancement</em>
                    </p>
                </div>
            </div>
            
            <div class="footer-section">
                <h4>⚖️ Legal Disclaimer</h4>
                <div class="disclaimer-box">
                    <ul style="list-style: none; padding: 0; font-size: 0.85em;">
                        <li>• Career advice for informational purposes only</li>
                        <li>• AI responses are automated, not professional counseling</li>
                        <li>• Salary data are estimates, actual may vary</li>
                        <li>• Always verify with official sources</li>
                    </ul>
                </div>
            </div>
            
            <div class="footer-section">
                <h4>🔒 Privacy & Data</h4>
                <div class="disclaimer-box">
                    <ul style="list-style: none; padding: 0; font-size: 0.85em;">
                        <li>• No personal data permanently stored</li>
                        <li>• Chat sessions are temporary</li>
                        <li>• Skill assessments processed locally</li>
                        <li>• Session data cleared on browser close</li>
                    </ul>
                </div>
            </div>
            
            <div class="footer-section">
                <h4>🛠️ Technical</h4>
                <p><strong>Frontend:</strong> Streamlit, Plotly</p>
                <p><strong>AI:</strong> Meta Llama 3.2</p>
                <p><strong>Hosting:</strong> Streamlit Cloud</p>
                <p><strong>Language:</strong> Python 3.11</p>
            </div>
        </div>
        
        <div class="footer-bottom">
            <p><strong>© {current_year} Career Shift Analyzer v{version}</strong></p>
            <p style="margin: 0.5rem 0;">
                <strong>👥 Developed by:</strong> 
                <span style="color: #ffd700;">MS Hadianto</span> (Lead) & 
                <span style="color: #ffd700;">Faby</span> (Co-Lead)
            </p>
            <p style="margin: 1rem 0; font-size: 0.8em;">
                <em>This platform provides general career guidance. Not a substitute for professional counseling.</em>
            </p>
            <p>
                🌟 <a href="https://github.com/mshadianto/career_shift_analyzer" target="_blank" class="footer-link">View on GitHub</a> | 
                Built with ❤️ for career advancement
            </p>
        </div>
    </div>
    """
    
    st.markdown("---")
    st.markdown(footer_html, unsafe_allow_html=True)

# Render footer
render_universal_footer()