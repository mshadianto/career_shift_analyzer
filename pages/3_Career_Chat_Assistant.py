import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page config
st.set_page_config(
    page_title="Career Shift Analyzer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

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
    }
    .stat-card {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin: 0.5rem;
    }
</style>
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

# Footer
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div style="text-align: center; color: #666;">
        <p>© 2025 Career Shift Analyzer | Built with ❤️ using Streamlit</p>
        <p>🚀 Empowering careers in the age of AI and emerging technologies</p>
    </div>
    """, unsafe_allow_html=True)