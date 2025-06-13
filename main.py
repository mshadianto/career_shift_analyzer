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
    """Get app version dynamically"""
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
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }
    .feature-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.2);
        border-left-color: #764ba2;
    }
    .stat-card {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 0.5rem;
        transition: all 0.3s ease;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
        position: relative;
        overflow: hidden;
    }
    .stat-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        transition: left 0.5s;
    }
    .stat-card:hover::before {
        left: 100%;
    }
    .stat-card:hover {
        transform: scale(1.05) rotateY(5deg);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.4);
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
        backdrop-filter: blur(10px);
    }
    .success-story {
        background: linear-gradient(135deg, #f8f9fa, #e9ecef);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #28a745;
        transition: all 0.3s ease;
    }
    .success-story:hover {
        transform: translateX(10px);
        box-shadow: 0 10px 25px rgba(40, 167, 69, 0.2);
    }
    .quick-action-btn {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        border: none;
        padding: 1rem 1.5rem;
        border-radius: 25px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
    }
    .quick-action-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.4);
    }
    .footer-container {
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
        backdrop-filter: blur(5px);
    }
    .footer-bottom {
        border-top: 1px solid rgba(255,255,255,0.2);
        padding-top: 1rem;
        text-align: center;
        font-size: 0.8em;
        color: rgba(255,255,255,0.9);
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
    .team-section {
        margin: 1rem 0;
        padding: 1.5rem;
        background: rgba(255,255,255,0.15);
        border-radius: 12px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,215,0,0.3);
    }
    .team-members {
        display: flex;
        justify-content: center;
        gap: 2rem;
        margin: 1rem 0;
        flex-wrap: wrap;
    }
    .team-member {
        background: rgba(255,255,255,0.2);
        padding: 1rem 2rem;
        border-radius: 25px;
        border: 2px solid rgba(255,215,0,0.5);
        transition: all 0.3s ease;
        backdrop-filter: blur(5px);
    }
    .team-member:hover {
        transform: translateY(-5px);
        border-color: #ffd700;
        box-shadow: 0 10px 25px rgba(255,215,0,0.3);
    }
    .team-member strong {
        color: #ffd700;
        font-size: 1.1em;
    }
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.5; }
        100% { opacity: 1; }
    }
    .chart-container {
        background: white;
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Version display
version = get_app_version()
st.markdown(f"""
<div class="version-info">
    🚀 v{version} Pro
</div>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🚀 Career Shift Analyzer</h1>
    <p style="font-size: 1.2em; margin: 0;">Navigate Your Future in Emerging Industries</p>
    <p style="font-size: 0.9em; margin-top: 0.5rem; opacity: 0.9;">
        Professional Career Guidance Platform with AI-Powered Insights
    </p>
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

# Quick stats with enhanced animations
st.markdown("### 📊 Industry Insights")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stat-card">
        <h3>🤖 AI Jobs</h3>
        <p><strong>+22%</strong> growth rate</p>
        <p>$80K-$180K salary</p>
        <p style="font-size: 0.8em; margin-top: 0.5rem;">🔥 High Demand</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-card">
        <h3>🔗 Blockchain</h3>
        <p><strong>+35%</strong> growth rate</p>
        <p>$90K-$200K salary</p>
        <p style="font-size: 0.8em; margin-top: 0.5rem;">🚀 Emerging</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-card">
        <h3>🌱 Clean Energy</h3>
        <p><strong>+8%</strong> growth rate</p>
        <p>$65K-$120K salary</p>
        <p style="font-size: 0.8em; margin-top: 0.5rem;">🌍 Sustainable</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-card">
        <h3>🔒 Cybersecurity</h3>
        <p><strong>+35%</strong> growth rate</p>
        <p>$75K-$150K salary</p>
        <p style="font-size: 0.8em; margin-top: 0.5rem;">🛡️ Critical</p>
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
        <p style="font-size: 0.8em; color: #667eea;"><strong>💡 Smart Analytics</strong></p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Try Career Simulation", key="sim"):
        st.switch_page("pages/1_Career_Simulation.py")

with col2:
    st.markdown("""
    <div class="feature-card">
        <h4>📊 Skill Gap Analysis</h4>
        <p>Comprehensive skill assessment with learning roadmaps and industry benchmarks.</p>
        <p style="font-size: 0.8em; color: #667eea;"><strong>📈 Data-Driven</strong></p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Analyze Your Skills", key="skills"):
        st.switch_page("pages/2_Skill_Gap_Analysis.py")

with col3:
    st.markdown("""
    <div class="feature-card">
        <h4>🤖 AI Career Assistant</h4>
        <p>24/7 AI-powered career counseling with personalized advice and industry insights.</p>
        <p style="font-size: 0.8em; color: #667eea;"><strong>🧠 AI-Powered</strong></p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Chat with AI Assistant", key="chat"):
        st.switch_page("pages/3_Career_Chat_Assistant.py")

# Enhanced Market trends chart with Plotly
st.markdown("### 📈 Emerging Industry Trends")

# Sample data for trends
trend_data = {
    'Industry': ['Artificial Intelligence', 'Blockchain & Web3', 'Renewable Energy', 
                'Biotechnology', 'Space Technology', 'Cybersecurity'],
    'Job Growth (%)': [22, 35, 8, 7, 6, 35],
    'Avg Salary (K)': [130, 145, 92, 105, 122, 112],
    'Market Size (B)': [190, 67, 300, 760, 400, 170],
    'Difficulty': ['High', 'Very High', 'Medium', 'High', 'Very High', 'High']
}

df = pd.DataFrame(trend_data)

# Create interactive bubble chart
fig = px.scatter(df, x='Job Growth (%)', y='Avg Salary (K)', 
                size='Market Size (B)', hover_name='Industry',
                title='🎯 Industry Growth vs Salary Potential vs Market Size',
                labels={'Job Growth (%)': 'Job Growth Rate (%)', 
                       'Avg Salary (K)': 'Average Salary ($K)',
                       'Market Size (B)': 'Market Size ($B)'},
                color='Difficulty',
                color_discrete_map={
                    'Medium': '#28a745',
                    'High': '#ffc107', 
                    'Very High': '#dc3545'
                },
                size_max=60)

fig.update_layout(
    height=600,
    showlegend=True,
    title_x=0.5,
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    font=dict(size=12),
    title_font=dict(size=16, color='#333')
)

fig.update_traces(
    marker=dict(line=dict(width=2, color='white')),
    selector=dict(mode='markers')
)

st.markdown('<div class="chart-container">', unsafe_allow_html=True)
st.plotly_chart(fig, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Industry breakdown with radar chart
st.markdown("### 🔍 Industry Skill Requirements")

col1, col2 = st.columns(2)

with col1:
    # Radar chart for skill requirements
    categories = ['Technical Skills', 'Soft Skills', 'Experience Required', 
                 'Learning Curve', 'Market Demand', 'Salary Potential']
    
    ai_scores = [9, 7, 8, 8, 10, 9]
    blockchain_scores = [10, 6, 7, 9, 8, 10]
    
    fig_radar = go.Figure()
    
    fig_radar.add_trace(go.Scatterpolar(
        r=ai_scores,
        theta=categories,
        fill='toself',
        name='AI/ML',
        line_color='rgb(102, 126, 234)'
    ))
    
    fig_radar.add_trace(go.Scatterpolar(
        r=blockchain_scores,
        theta=categories,
        fill='toself',
        name='Blockchain',
        line_color='rgb(118, 75, 162)'
    ))
    
    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            )),
        showlegend=True,
        title="AI vs Blockchain Skill Requirements",
        height=400
    )
    
    st.plotly_chart(fig_radar, use_container_width=True)

with col2:
    # Bar chart for salary comparison
    salary_data = {
        'Industry': ['AI/ML', 'Blockchain', 'Cybersecurity', 'Biotech', 'Clean Energy', 'Space Tech'],
        'Min Salary': [80, 90, 75, 70, 65, 85],
        'Max Salary': [180, 200, 150, 140, 120, 160]
    }
    
    salary_df = pd.DataFrame(salary_data)
    
    fig_salary = go.Figure()
    
    fig_salary.add_trace(go.Bar(
        name='Min Salary',
        x=salary_df['Industry'],
        y=salary_df['Min Salary'],
        marker_color='rgba(102, 126, 234, 0.7)'
    ))
    
    fig_salary.add_trace(go.Bar(
        name='Max Salary',
        x=salary_df['Industry'],
        y=salary_df['Max Salary'],
        marker_color='rgba(118, 75, 162, 0.7)'
    ))
    
    fig_salary.update_layout(
        title='💰 Salary Ranges by Industry',
        xaxis_title='Industry',
        yaxis_title='Salary ($K)',
        barmode='group',
        height=400
    )
    
    st.plotly_chart(fig_salary, use_container_width=True)

# Enhanced Success stories section
st.markdown("### 🌟 Success Stories")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="success-story">
        <h4>👨‍💻 From Accountant to AI Engineer</h4>
        <p>"Used Career Shift Analyzer to transition from finance to AI. 
        The skill gap analysis showed me exactly what to learn. 
        Now earning 60% more at a tech startup!"</p>
        <p><em>- Sarah, AI Engineer</em></p>
        <div style="margin-top: 1rem;">
            <span style="background: #28a745; color: white; padding: 0.2rem 0.5rem; border-radius: 10px; font-size: 0.8em;">
                ✅ 8 months transition
            </span>
            <span style="background: #17a2b8; color: white; padding: 0.2rem 0.5rem; border-radius: 10px; font-size: 0.8em; margin-left: 0.5rem;">
                💰 +60% salary
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="success-story">
        <h4>🚀 Blockchain Developer Journey</h4>
        <p>"The platform's learning roadmap guided me from zero coding 
        experience to landing a blockchain developer role in 8 months. 
        The AI assistant was incredibly helpful!"</p>
        <p><em>- Ahmad, Blockchain Developer</em></p>
        <div style="margin-top: 1rem;">
            <span style="background: #6f42c1; color: white; padding: 0.2rem 0.5rem; border-radius: 10px; font-size: 0.8em;">
                🚀 Zero to Hero
            </span>
            <span style="background: #fd7e14; color: white; padding: 0.2rem 0.5rem; border-radius: 10px; font-size: 0.8em; margin-left: 0.5rem;">
                🎯 Remote Job
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Quick actions with enhanced styling
st.markdown("### 🎯 Quick Actions")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📋 Take Skill Assessment", use_container_width=True, type="secondary"):
        st.switch_page("pages/2_Skill_Gap_Analysis.py")

with col2:
    if st.button("💬 Ask AI Career Question", use_container_width=True, type="secondary"):
        st.switch_page("pages/3_Career_Chat_Assistant.py")

with col3:
    if st.button("🎓 View Learning Paths", use_container_width=True, type="secondary"):
        st.info("🚧 Advanced feature coming soon!")

with col4:
    if st.button("📊 Industry Reports", use_container_width=True, type="secondary"):
        st.info("💎 Premium feature - coming soon!")

# Enhanced Dynamic Footer with Team Credits
def render_enhanced_footer():
    current_year = datetime.now().year
    last_updated = datetime.now().strftime("%B %d, %Y")
    
    footer_html = f"""
    <div class="footer-container">
        <div class="footer-grid">
            <div class="footer-section">
                <h4>🚀 Career Shift Analyzer Pro</h4>
                <p><span class="status-indicator"></span><strong>Status:</strong> Online & Active</p>
                <p><strong>Version:</strong> v{version}</p>
                <p><strong>Last Updated:</strong> {last_updated}</p>
                <p><strong>Build:</strong> Production</p>
                <div class="team-section">
                    <h5 style="color: #ffd700; margin-bottom: 1rem;">👥 Development Team</h5>
                    <div class="team-members">
                        <div class="team-member">
                            <strong>🎯 MS Hadianto</strong><br>
                            <span style="font-size: 0.9em;">Lead Project & Architecture</span>
                        </div>
                        <div class="team-member">
                            <strong>🤝 Faby</strong><br>
                            <span style="font-size: 0.9em;">Co-Lead & Development</span>
                        </div>
                    </div>
                    <p style="margin-top: 1rem; font-size: 0.9em; color: rgba(255,255,255,0.8);">
                        <em>Collaborative innovation for career advancement</em>
                    </p>
                </div>
            </div>
            
            <div class="footer-section">
                <h4>⚖️ Important Disclaimer</h4>
                <div class="disclaimer-box">
                    <p><strong>⚠️ Please Read:</strong></p>
                    <ul style="list-style: none; padding: 0; font-size: 0.85em;">
                        <li>• Career advice for informational purposes only</li>
                        <li>• AI responses are automated, not professional counseling</li>
                        <li>• Salary data are market estimates, actual may vary</li>
                        <li>• Individual results depend on personal circumstances</li>
                        <li>• Always verify with official sources</li>
                    </ul>
                </div>
            </div>
            
            <div class="footer-section">
                <h4>🔒 Privacy & Data Policy</h4>
                <div class="disclaimer-box">
                    <ul style="list-style: none; padding: 0; font-size: 0.85em;">
                        <li>• No personal data permanently stored</li>
                        <li>• Chat sessions are temporary</li>
                        <li>• Skill assessments processed locally</li>
                        <li>• Third-party APIs have separate policies</li>
                        <li>• Session data cleared on browser close</li>
                    </ul>
                </div>
            </div>
            
            <div class="footer-section">
                <h4>🛠️ Technical Stack</h4>
                <p><strong>Frontend:</strong> Streamlit, Plotly</p>
                <p><strong>AI Model:</strong> Meta Llama 3.2</p>
                <p><strong>Hosting:</strong> Streamlit Cloud</p>
                <p><strong>Language:</strong> Python 3.11</p>
                <p><strong>Analytics:</strong> Interactive Visualizations</p>
                <p><strong>Data:</strong> Real-time industry research</p>
            </div>
        </div>
        
        <div class="footer-bottom">
            <p><strong>© {current_year} Career Shift Analyzer Pro v{version}</strong></p>
            <p style="margin: 0.3rem 0;">
                <strong>👥 Proudly Developed by:</strong> 
                <span style="color: #ffd700;">MS Hadianto</span> (Lead Project) & 
                <span style="color: #ffd700;">Faby</span> (Co-Lead)
            </p>
            <p style="margin: 0.5rem 0;">
                <em><strong>Legal Notice:</strong> This platform provides general career guidance and educational content. 
                It is not a substitute for professional career counseling, financial advice, or job placement services. 
                Users should independently verify all information and consult qualified professionals for personalized advice.</em>
            </p>
            <p style="margin-top: 1rem;">
                🌟 <strong>Open Source Project</strong> | 
                <a href="https://github.com/mshadianto/career_shift_analyzer" target="_blank" style="color: #ffd700;">
                    View on GitHub
                </a> | 
                Built with ❤️ for career advancement
            </p>
        </div>
    </div>
    """
    
    st.markdown(footer_html, unsafe_allow_html=True)

# Render enhanced footer
render_enhanced_footer()

# footer_component.py - Universal Footer for All Pages
# Place this code at the bottom of EVERY page file

import streamlit as st
from datetime import datetime
import os

def render_universal_footer():
    """Universal Footer Component with Team Credits and Disclaimer"""
    
    def get_app_version():
        """Get app version dynamically"""
        try:
            env_version = os.getenv('APP_VERSION')
            if env_version:
                return env_version
            base_version = "1.4"
            build_number = datetime.now().strftime("%y%m%d")
            return f"{base_version}.{build_number}"
        except:
            return "1.0.0"
    
    version = get_app_version()
    current_year = datetime.now().year
    last_updated = datetime.now().strftime("%B %d, %Y")
    
    # Universal Footer CSS
    st.markdown("""
    <style>
    .universal-footer {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem 1rem;
        border-radius: 15px;
        margin-top: 3rem;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.3);
        backdrop-filter: blur(10px);
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
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .disclaimer-box {
        background: rgba(255,255,255,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        font-size: 0.85em;
        backdrop-filter: blur(5px);
    }
    .team-section {
        background: rgba(255,255,255,0.15);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        backdrop-filter: blur(10px);
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
        backdrop-filter: blur(5px);
        text-align: center;
        min-width: 140px;
    }
    .team-member:hover {
        transform: translateY(-5px);
        border-color: #ffd700;
        box-shadow: 0 10px 25px rgba(255,215,0,0.3);
        background: rgba(255,255,255,0.25);
    }
    .team-member strong {
        color: #ffd700;
        font-size: 1em;
        display: block;
        margin-bottom: 0.3rem;
    }
    .team-member span {
        font-size: 0.8em;
        color: rgba(255,255,255,0.9);
        line-height: 1.2;
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
    .tech-stack {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        gap: 0.5rem;
        margin: 0.5rem 0;
    }
    .tech-item {
        background: rgba(255,255,255,0.1);
        padding: 0.3rem 0.6rem;
        border-radius: 15px;
        font-size: 0.8em;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.2);
    }
    @keyframes pulse {
        0% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.5; transform: scale(1.1); }
        100% { opacity: 1; transform: scale(1); }
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
    .version-badge {
        background: rgba(255,215,0,0.2);
        color: #ffd700;
        padding: 0.2rem 0.6rem;
        border-radius: 12px;
        font-weight: bold;
        border: 1px solid rgba(255,215,0,0.3);
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Footer HTML Content
    footer_html = f"""
    <div class="universal-footer">
        <div class="footer-grid">
            <!-- App Info Section -->
            <div class="footer-section">
                <h4>🚀 Career Shift Analyzer</h4>
                <p><span class="status-indicator"></span><strong>Status:</strong> Online & Active</p>
                <p><strong>Version:</strong> <span class="version-badge">v{version}</span></p>
                <p><strong>Last Updated:</strong> {last_updated}</p>
                <p><strong>Environment:</strong> Production</p>
                
                <div class="team-section">
                    <h5 style="color: #ffd700; margin-bottom: 1rem; text-align: center;">👥 Development Team</h5>
                    <div class="team-members">
                        <div class="team-member">
                            <strong>🎯 MS Hadianto</strong>
                            <span>Lead Project &<br>Architecture</span>
                        </div>
                        <div class="team-member">
                            <strong>🤝 Faby</strong>
                            <span>Co-Lead &<br>Development</span>
                        </div>
                    </div>
                    <p style="text-align: center; font-size: 0.85em; color: rgba(255,255,255,0.8); margin-top: 1rem;">
                        <em>Collaborative innovation for career advancement</em>
                    </p>
                </div>
            </div>
            
            <!-- Legal Disclaimer Section -->
            <div class="footer-section">
                <h4>⚖️ Legal Disclaimer</h4>
                <div class="disclaimer-box">
                    <p><strong>⚠️ Important Notice:</strong></p>
                    <ul style="list-style: none; padding: 0; font-size: 0.85em; line-height: 1.4;">
                        <li>• Career advice for informational purposes only</li>
                        <li>• AI responses are automated, not professional counseling</li>
                        <li>• Salary estimates based on market research, may vary</li>
                        <li>• Individual results depend on personal circumstances</li>
                        <li>• Always verify information with official sources</li>
                        <li>• Not a substitute for professional career counseling</li>
                    </ul>
                </div>
            </div>
            
            <!-- Privacy & Data Section -->
            <div class="footer-section">
                <h4>🔒 Privacy & Data</h4>
                <div class="disclaimer-box">
                    <p><strong>🛡️ Data Protection:</strong></p>
                    <ul style="list-style: none; padding: 0; font-size: 0.85em; line-height: 1.4;">
                        <li>• No personal data permanently stored</li>
                        <li>• Chat sessions are temporary & session-based</li>
                        <li>• Skill assessments processed locally</li>
                        <li>• Third-party APIs governed by separate policies</li>
                        <li>• All session data cleared on browser close</li>
                        <li>• No tracking or analytics cookies</li>
                    </ul>
                </div>
            </div>
            
            <!-- Technical Stack Section -->
            <div class="footer-section">
                <h4>🛠️ Technical Stack</h4>
                <div class="tech-stack">
                    <div class="tech-item">🐍 Python 3.11</div>
                    <div class="tech-item">⚡ Streamlit</div>
                    <div class="tech-item">📊 Plotly</div>
                    <div class="tech-item">🤖 Llama 3.2</div>
                    <div class="tech-item">☁️ Cloud Hosted</div>
                    <div class="tech-item">📱 Responsive</div>
                </div>
                <div style="margin-top: 1rem;">
                    <p><strong>AI Model:</strong> Meta Llama 3.2 via OpenRouter</p>
                    <p><strong>Hosting:</strong> Streamlit Cloud Platform</p>
                    <p><strong>Data Source:</strong> Real-time industry research</p>
                    <p><strong>Updates:</strong> Continuous deployment</p>
                </div>
            </div>
        </div>
        
        <!-- Footer Bottom -->
        <div class="footer-bottom">
            <p style="font-size: 1em; margin-bottom: 0.8rem;">
                <strong>© {current_year} Career Shift Analyzer v{version}</strong>
            </p>
            <p style="margin: 0.5rem 0; font-size: 0.95em;">
                <strong>👥 Proudly Developed by:</strong> 
                <span style="color: #ffd700; font-weight: bold;">MS Hadianto</span> (Lead Project) & 
                <span style="color: #ffd700; font-weight: bold;">Faby</span> (Co-Lead)
            </p>
            <p style="margin: 1rem 0; font-size: 0.8em; line-height: 1.4; color: rgba(255,255,255,0.9);">
                <em><strong>Legal Notice:</strong> This platform provides general career guidance and educational content. 
                It is not a substitute for professional career counseling, financial advice, or job placement services. 
                Users should independently verify all information and consult qualified professionals for personalized advice. 
                Use of this platform constitutes acceptance of our terms and disclaimer.</em>
            </p>
            <p style="margin-top: 1.5rem;">
                🌟 <strong>Open Source Project</strong> | 
                <a href="https://github.com/mshadianto/career_shift_analyzer" target="_blank" class="footer-link">
                    📚 View on GitHub
                </a> | 
                <a href="mailto:support@careershiftanalyzer.com" class="footer-link">
                    📧 Contact Support
                </a>
            </p>
            <p style="margin-top: 0.5rem; font-size: 0.9em; color: #ffd700;">
                Built with ❤️ for empowering career advancement worldwide
            </p>
        </div>
    </div>
    """
    
    # Render the footer
    st.markdown("---")  # Separator line
    st.markdown(footer_html, unsafe_allow_html=True)

# =============================================================================
# USAGE INSTRUCTIONS:
# =============================================================================
# 
# Add this code at the BOTTOM of EVERY page file:
#
# # At the end of main.py:
# render_universal_footer()
#
# # At the end of pages/1_Career_Simulation.py:
# render_universal_footer()
#
# # At the end of pages/2_Skill_Gap_Analysis.py:
# render_universal_footer()
#
# # At the end of pages/3_Career_Chat_Assistant.py:
# render_universal_footer()
#
# =============================================================================