import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, timedelta
import os
import numpy as np
import time
from typing import Dict, List, Tuple

# Page config with enhanced settings
st.set_page_config(
    page_title="Career Shift Analyzer Pro",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/mshadianto/career_shift_analyzer',
        'Report a bug': 'https://github.com/mshadianto/career_shift_analyzer/issues',
        'About': "Career Shift Analyzer Pro - AI-powered career guidance platform"
    }
)

# Enhanced Version Management
@st.cache_data(ttl=3600)
def get_app_version() -> str:
    """Get application version with enhanced logic"""
    try:
        env_version = os.getenv('APP_VERSION')
        if env_version:
            return env_version
        base_version = "2.0"
        build_number = datetime.now().strftime("%y%m%d")
        return f"{base_version}.{build_number}"
    except Exception:
        return "2.0.0"

# Enhanced data loading with caching - FIXED SYNTAX ERROR
@st.cache_data(ttl=1800)
def load_industry_data() -> Dict:
    """Load and process industry data with enhanced metrics"""
    return {
        'industries': {
            'Artificial Intelligence': {
                'growth': 22, 'min_salary': 80, 'max_salary': 180, 'market_size': 190,
                'difficulty': 'High', 'remote_friendly': 95, 'job_security': 9,
                'skills': ['Python', 'Machine Learning', 'Deep Learning', 'TensorFlow', 'PyTorch'],
                'description': 'Revolutionary technology transforming industries worldwide'
            },
            'Blockchain & Web3': {
                'growth': 35, 'min_salary': 90, 'max_salary': 200, 'market_size': 67,
                'difficulty': 'Very High', 'remote_friendly': 90, 'job_security': 7,
                'skills': ['Solidity', 'Smart Contracts', 'DeFi', 'Ethereum', 'Rust'],
                'description': 'Decentralized future of finance and applications'
            },
            'Renewable Energy': {
                'growth': 8, 'min_salary': 65, 'max_salary': 120, 'market_size': 300,
                'difficulty': 'Medium', 'remote_friendly': 40, 'job_security': 8,
                'skills': ['Solar Tech', 'Sustainability', 'Engineering', 'Grid Systems'],
                'description': 'Sustainable energy solutions for climate change'
            },
            'Biotechnology': {
                'growth': 7, 'min_salary': 70, 'max_salary': 140, 'market_size': 760,
                'difficulty': 'High', 'remote_friendly': 30, 'job_security': 8,
                'skills': ['Bioinformatics', 'Genetics', 'Lab Skills', 'CRISPR'],
                'description': 'Life sciences innovation and medical breakthroughs'
            },
            'Space Technology': {
                'growth': 6, 'min_salary': 85, 'max_salary': 160, 'market_size': 400,
                'difficulty': 'Very High', 'remote_friendly': 60, 'job_security': 7,
                'skills': ['Aerospace', 'Physics', 'Navigation', 'Satellites'],
                'description': 'Final frontier exploration and commercialization'
            },
            'Cybersecurity': {
                'growth': 35, 'min_salary': 75, 'max_salary': 150, 'market_size': 170,
                'difficulty': 'High', 'remote_friendly': 85, 'job_security': 9,
                'skills': ['Network Security', 'Penetration Testing', 'CISSP', 'Incident Response'],
                'description': 'Critical protection for digital infrastructure'
            },
            'Quantum Computing': {
                'growth': 25, 'min_salary': 120, 'max_salary': 250, 'market_size': 65,
                'difficulty': 'Very High', 'remote_friendly': 80, 'job_security': 6,
                'skills': ['Quantum Physics', 'Qiskit', 'Linear Algebra', 'Python'],
                'description': 'Next-generation computing paradigm'
            },
            'IoT & Edge Computing': {
                'growth': 18, 'min_salary': 70, 'max_salary': 140, 'market_size': 200,
                'difficulty': 'Medium', 'remote_friendly': 70, 'job_security': 8,
                'skills': ['Embedded Systems', 'Sensors', 'Cloud', 'Real-time Systems'],
                'description': 'Connected devices and distributed computing'
            }
        },
        'success_stories': [
            {
                'name': 'Alex Chen',
                'from': 'Marketing Manager',
                'to': 'AI/ML Engineer',
                'company': 'Google',
                'duration': '18 months',
                'salary_increase': 85,
                'story': 'Transitioned from marketing to AI by taking online courses and building personal projects.',
                'skills_learned': ['Python', 'TensorFlow', 'Data Science', 'Machine Learning']
            },
            {
                'name': 'Sarah Johnson',
                'from': 'Finance Analyst',
                'to': 'Blockchain Developer',
                'company': 'ConsenSys',
                'duration': '14 months',
                'salary_increase': 120,
                'story': 'Self-taught blockchain development through bootcamps and open-source contributions.',
                'skills_learned': ['Solidity', 'Smart Contracts', 'Web3', 'DeFi']
            },
            {
                'name': 'Michael Torres',
                'from': 'Teacher',
                'to': 'Cybersecurity Specialist',
                'company': 'Microsoft',
                'duration': '12 months',
                'salary_increase': 95,
                'story': 'Leveraged teaching skills to transition into cybersecurity training and consulting.',
                'skills_learned': ['Network Security', 'Penetration Testing', 'CISSP', 'Security Analysis']
            }
        ]
    }

# Add disclaimer warning function
def add_disclaimer_warning():
    """Add disclaimer warning at the top of the page"""
    st.warning("""
    ⚠️ **Disclaimer**: This platform provides career guidance for educational purposes only. 
    AI responses may contain errors. Always verify information independently and consult with 
    professional career counselors for personalized advice.
    """)

# Dark Purple Neon Sci-Fi Theme CSS
def load_custom_css():
    """Load dark purple neon sci-fi themed CSS"""
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
        
        /* Neon Header */
        .main-header {
            text-align: center;
            padding: 4rem 2rem;
            background: linear-gradient(135deg, rgba(139, 69, 255, 0.2), rgba(255, 69, 255, 0.2));
            border: 2px solid #8b45ff;
            border-radius: 20px;
            margin-bottom: 3rem;
            box-shadow: 
                0 0 30px rgba(139, 69, 255, 0.5),
                inset 0 0 30px rgba(139, 69, 255, 0.1);
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(10px);
        }
        
        .main-header::before {
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
        
        .main-header h1 {
            font-family: 'Orbitron', monospace;
            font-weight: 900;
            text-shadow: 
                0 0 10px #8b45ff,
                0 0 20px #8b45ff,
                0 0 30px #8b45ff;
            animation: glow 2s ease-in-out infinite alternate;
        }
        
        @keyframes glow {
            from { text-shadow: 0 0 10px #8b45ff, 0 0 20px #8b45ff, 0 0 30px #8b45ff; }
            to { text-shadow: 0 0 20px #8b45ff, 0 0 30px #8b45ff, 0 0 40px #8b45ff; }
        }
        
        /* Neon Cards */
        .neon-card {
            background: linear-gradient(145deg, rgba(13, 13, 13, 0.9), rgba(26, 14, 46, 0.9));
            border: 1px solid #8b45ff;
            border-radius: 15px;
            padding: 2rem;
            margin: 1rem 0;
            box-shadow: 
                0 0 20px rgba(139, 69, 255, 0.3),
                inset 0 0 20px rgba(139, 69, 255, 0.05);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            backdrop-filter: blur(10px);
        }
        
        .neon-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(139, 69, 255, 0.2), transparent);
            transition: left 0.5s;
        }
        
        .neon-card:hover::before {
            left: 100%;
        }
        
        .neon-card:hover {
            transform: translateY(-5px);
            border-color: #ff45ff;
            box-shadow: 
                0 10px 30px rgba(255, 69, 255, 0.4),
                inset 0 0 30px rgba(255, 69, 255, 0.1);
        }
        
        /* Stat Cards */
        .stat-card {
            background: linear-gradient(135deg, rgba(139, 69, 255, 0.2), rgba(255, 69, 255, 0.2));
            border: 1px solid #8b45ff;
            border-radius: 15px;
            padding: 2rem 1.5rem;
            text-align: center;
            margin: 1rem 0.5rem;
            box-shadow: 0 0 25px rgba(139, 69, 255, 0.4);
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        
        .stat-card:hover {
            transform: scale(1.05) rotateY(5deg);
            border-color: #ff45ff;
            box-shadow: 0 0 35px rgba(255, 69, 255, 0.6);
        }
        
        .stat-card h3 {
            font-family: 'Orbitron', monospace;
            color: #ff45ff;
            text-shadow: 0 0 10px #ff45ff;
        }
        
        /* Feature Cards */
        .feature-card {
            background: linear-gradient(145deg, rgba(13, 13, 13, 0.8), rgba(26, 14, 46, 0.8));
            border: 1px solid #8b45ff;
            border-radius: 15px;
            padding: 2rem;
            margin: 2rem 0;
            transition: all 0.3s ease;
            box-shadow: 0 0 20px rgba(139, 69, 255, 0.2);
            position: relative;
            overflow: hidden;
        }
        
        .feature-card:hover {
            transform: translateY(-10px);
            border-color: #ff45ff;
            box-shadow: 0 20px 40px rgba(255, 69, 255, 0.3);
        }
        
        /* Version Info */
        .version-info {
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(139, 69, 255, 0.2);
            border: 1px solid #8b45ff;
            border-radius: 20px;
            padding: 0.8rem 1.5rem;
            font-family: 'Orbitron', monospace;
            color: #8b45ff;
            z-index: 1000;
            backdrop-filter: blur(10px);
            box-shadow: 0 0 15px rgba(139, 69, 255, 0.3);
            text-shadow: 0 0 5px #8b45ff;
        }
        
        /* Success Stories */
        .success-story {
            background: linear-gradient(145deg, rgba(13, 13, 13, 0.9), rgba(0, 40, 20, 0.9));
            border: 1px solid #00ff88;
            border-radius: 15px;
            padding: 2rem;
            margin: 2rem 0;
            border-left: 4px solid #00ff88;
            box-shadow: 0 0 20px rgba(0, 255, 136, 0.2);
            transition: all 0.3s ease;
        }
        
        .success-story:hover {
            transform: translateX(10px);
            box-shadow: 0 0 30px rgba(0, 255, 136, 0.4);
        }
        
        /* Industry Grid */
        .industry-item {
            background: linear-gradient(145deg, rgba(13, 13, 13, 0.8), rgba(26, 14, 46, 0.8));
            border: 1px solid #8b45ff;
            border-radius: 15px;
            padding: 2rem;
            text-align: center;
            transition: all 0.3s ease;
            box-shadow: 0 0 15px rgba(139, 69, 255, 0.2);
            position: relative;
            overflow: hidden;
        }
        
        .industry-item:hover {
            transform: translateY(-10px) scale(1.02);
            border-color: #ff45ff;
            box-shadow: 0 20px 40px rgba(255, 69, 255, 0.3);
        }
        
        /* Chart Container */
        .chart-container {
            background: linear-gradient(145deg, rgba(13, 13, 13, 0.9), rgba(26, 14, 46, 0.9));
            border: 1px solid #8b45ff;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 0 25px rgba(139, 69, 255, 0.2);
            margin: 2rem 0;
            backdrop-filter: blur(10px);
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
        
        /* Text Elements */
        h1, h2, h3, h4 {
            font-family: 'Orbitron', monospace;
            color: #e0e0ff;
        }
        
        p, span, div {
            font-family: 'Exo 2', sans-serif;
            color: #c0c0ff;
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .main-header { padding: 2rem 1rem; }
            .neon-card, .stat-card { margin: 1rem 0; padding: 1.5rem; }
            .version-info { position: relative; top: auto; right: auto; margin: 1rem 0; }
        }
    </style>
    """, unsafe_allow_html=True)

# Enhanced data processing functions
@st.cache_data(ttl=1800)
def process_trend_data() -> pd.DataFrame:
    """Process and return enhanced trend data"""
    data = load_industry_data()['industries']
    
    df_data = []
    for industry, metrics in data.items():
        df_data.append({
            'Industry': industry,
            'Job Growth (%)': metrics['growth'],
            'Avg Salary (K)': (metrics['min_salary'] + metrics['max_salary']) / 2,
            'Market Size (B)': metrics['market_size'],
            'Difficulty': metrics['difficulty'],
            'Remote Friendly (%)': metrics['remote_friendly'],
            'Job Security': metrics['job_security'],
            'Min Salary': metrics['min_salary'],
            'Max Salary': metrics['max_salary']
        })
    
    return pd.DataFrame(df_data)

# Enhanced visualization functions
def create_advanced_bubble_chart(df: pd.DataFrame) -> go.Figure:
    """Create an advanced interactive bubble chart with dark theme"""
    fig = px.scatter(
        df, 
        x='Job Growth (%)', 
        y='Avg Salary (K)', 
        size='Market Size (B)', 
        hover_name='Industry',
        title='🎯 Industry Growth vs Salary vs Market Size Analysis',
        color='Remote Friendly (%)',
        color_continuous_scale='Viridis',
        size_max=80
    )
    
    fig.update_layout(
        height=600,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e0ff', family="Exo 2"),
        title_font=dict(size=18, color='#ff45ff', family="Orbitron"),
        xaxis=dict(gridcolor='rgba(139, 69, 255, 0.2)'),
        yaxis=dict(gridcolor='rgba(139, 69, 255, 0.2)')
    )
    
    return fig

def create_salary_comparison_chart(df: pd.DataFrame) -> go.Figure:
    """Create enhanced salary comparison chart with dark theme"""
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Min Salary',
        x=df['Industry'],
        y=df['Min Salary'],
        marker_color='rgba(139, 69, 255, 0.7)',
        text=df['Min Salary'],
        textposition='auto'
    ))
    
    fig.add_trace(go.Bar(
        name='Max Salary',
        x=df['Industry'],
        y=df['Max Salary'],
        marker_color='rgba(255, 69, 255, 0.7)',
        text=df['Max Salary'],
        textposition='auto'
    ))
    
    fig.update_layout(
        title='💰 Salary Ranges by Industry (2024)',
        xaxis_title='Industry',
        yaxis_title='Salary ($K)',
        barmode='group',
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e0ff', family="Exo 2"),
        title_font=dict(color='#ff45ff', family="Orbitron"),
        xaxis=dict(tickangle=45, gridcolor='rgba(139, 69, 255, 0.2)'),
        yaxis=dict(gridcolor='rgba(139, 69, 255, 0.2)')
    )
    
    return fig

def create_skill_radar_chart() -> go.Figure:
    """Create enhanced skill requirements radar chart with dark theme"""
    categories = [
        'Technical Skills', 'Soft Skills', 'Experience Required', 
        'Learning Curve', 'Market Demand', 'Salary Potential',
        'Remote Opportunities', 'Job Security'
    ]
    
    ai_scores = [9, 7, 8, 8, 10, 9, 9, 9]
    blockchain_scores = [10, 6, 7, 9, 8, 10, 9, 7]
    cybersec_scores = [8, 8, 7, 7, 9, 8, 8, 9]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=ai_scores, theta=categories, fill='toself', name='AI/ML',
        line_color='rgb(139, 69, 255)', fillcolor='rgba(139, 69, 255, 0.3)'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=blockchain_scores, theta=categories, fill='toself', name='Blockchain',
        line_color='rgb(255, 69, 255)', fillcolor='rgba(255, 69, 255, 0.3)'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=cybersec_scores, theta=categories, fill='toself', name='Cybersecurity',
        line_color='rgb(0, 255, 136)', fillcolor='rgba(0, 255, 136, 0.3)'
    ))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 10], gridcolor='rgba(139, 69, 255, 0.2)')),
        showlegend=True, title="🎯 Industry Skill Requirements Comparison", height=500,
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e0ff', family="Exo 2"),
        title_font=dict(color='#ff45ff', family="Orbitron")
    )
    
    return fig

# Main application
def main():
    """Main application function with enhanced sci-fi theme"""
    
    # Load custom CSS
    load_custom_css()
    
    # Apply enhanced sidebar (optional - only if utils/sidebar.py exists)
    try:
        from utils.sidebar import apply_super_sidebar
        apply_super_sidebar()
    except ImportError:
        st.sidebar.info("🔄 Loading enhanced sidebar...")
    except Exception as e:
        st.sidebar.error(f"Sidebar error: {e}")
    
    # Add disclaimer warning at the top
    add_disclaimer_warning()
    
    # Get version and data
    version = get_app_version()
    industry_data = load_industry_data()
    
    # Version display
    st.markdown(f"""
    <div class="version-info">
        🚀 v{version} Pro
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced Header
    current_time = datetime.now().strftime("%H:%M UTC")
    st.markdown(f"""
    <div class="main-header">
        <h1 style="margin: 0; font-size: 3.5em; font-weight: 900;">
            🚀 CAREER SHIFT ANALYZER
        </h1>
        <p style="font-size: 1.4em; margin: 1.5rem 0; opacity: 0.95;">
            Navigate Your Future in Emerging Industries
        </p>
        <p style="font-size: 1.1em; margin: 1rem 0; opacity: 0.85;">
            AI-Powered Career Guidance Platform with Real-Time Industry Insights
        </p>
        <div style="margin-top: 2rem; font-size: 0.9em; opacity: 0.8;">
            <span style="margin-right: 2rem;">🌍 Global Coverage</span>
            <span style="margin-right: 2rem;">⏰ {current_time}</span>
            <span>👥 {len(industry_data['industries'])} Industries</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Hero section
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="neon-card">
            <h3 style="color: #ff45ff; text-align: center; margin-bottom: 1.5rem;">🎯 Transform Your Career Journey</h3>
            <p style="text-align: center; line-height: 1.8; margin-bottom: 2rem;">
                Discover high-growth opportunities in <strong>AI, Blockchain, Quantum Computing, 
                Renewable Energy, Biotech,</strong> and more. Get personalized insights with 
                AI-powered career guidance.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("🚀 Start Analysis", type="primary", use_container_width=True):
                st.info("🚧 Feature coming soon!")
        with col_b:
            if st.button("💬 AI Assistant", type="secondary", use_container_width=True):
                st.info("🚧 Feature coming soon!")
    
    # Quick stats
    st.markdown("### 📊 Live Industry Insights")
    df = process_trend_data()
    
    col1, col2, col3, col4 = st.columns(4)
    
    # Display top 4 industries
    top_industries = ['Artificial Intelligence', 'Blockchain & Web3', 'Cybersecurity', 'Quantum Computing']
    
    for idx, industry in enumerate(top_industries):
        data = df[df['Industry'] == industry].iloc[0]
        with [col1, col2, col3, col4][idx]:
            emoji = ['🤖', '🔗', '🔒', '⚛️'][idx]
            st.markdown(f"""
            <div class="stat-card">
                <h3>{emoji} {industry.split(' ')[0]}</h3>
                <p style="font-size: 1.8em; font-weight: bold; color: #ff45ff;">+{data['Job Growth (%)']}%</p>
                <p>annual growth</p>
                <p>${data['Min Salary']:.0f}K-${data['Max Salary']:.0f}K</p>
                <p style="font-size: 0.9em; opacity: 0.9;">🔥 {data['Remote Friendly (%)']}% Remote</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Features section
    st.markdown("### ✨ Platform Features")
    
    col1, col2, col3 = st.columns(3)
    
    features = [
        {
            'title': '🎯 AI Career Simulation',
            'desc': 'Interactive career path exploration with real market data and ML-powered recommendations.',
            'tags': ['💡 AI-Powered', '📊 Real-Time']
        },
        {
            'title': '📊 Advanced Analysis',
            'desc': 'Comprehensive skill assessment with learning roadmaps and industry benchmarks.',
            'tags': ['📈 Data-Driven', '🎯 Personalized']
        },
        {
            'title': '🤖 AI Career Mentor',
            'desc': '24/7 intelligent career counseling with natural language processing.',
            'tags': ['🧠 LLM-Powered', '⚡ Instant']
        }
    ]
    
    for idx, feature in enumerate(features):
        with [col1, col2, col3][idx]:
            st.markdown(f"""
            <div class="feature-card">
                <h4 style="color: #ff45ff; margin-bottom: 1rem;">{feature['title']}</h4>
                <p style="line-height: 1.6; margin-bottom: 1.5rem;">{feature['desc']}</p>
                <div>
                    {' '.join([f'<span style="background: rgba(139, 69, 255, 0.2); color: #8b45ff; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.8em; margin-right: 0.5rem;">{tag}</span>' for tag in feature['tags']])}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Visualizations
    st.markdown("### 📈 Interactive Analytics")
    
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    bubble_fig = create_advanced_bubble_chart(df)
    st.plotly_chart(bubble_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        radar_fig = create_skill_radar_chart()
        st.plotly_chart(radar_fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        salary_fig = create_salary_comparison_chart(df)
        st.plotly_chart(salary_fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Success stories
    st.markdown("### 🌟 Success Stories")
    
    success_stories = industry_data['success_stories']
    
    for story in success_stories:
        st.markdown(f"""
        <div class="success-story">
            <h4 style="color: #00ff88; margin-bottom: 1rem;">
                👨‍💻 {story['from']} → {story['to']}
            </h4>
            <p style="font-style: italic; margin-bottom: 1rem;">"{story['story']}"</p>
            <p style="font-weight: 600; color: #e0e0ff;">
                — {story['name']}, {story['to']} at {story['company']}
            </p>
            <div style="margin-top: 1rem;">
                <span style="background: #00ff88; color: black; padding: 0.3rem 0.8rem; border-radius: 15px; margin-right: 0.5rem;">
                    ✅ {story['duration']}
                </span>
                <span style="background: #ff45ff; color: white; padding: 0.3rem 0.8rem; border-radius: 15px; margin-right: 0.5rem;">
                    💰 +{story['salary_increase']}%
                </span>
                <span style="background: #8b45ff; color: white; padding: 0.3rem 0.8rem; border-radius: 15px;">
                    🎓 {len(story['skills_learned'])} skills
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Industry overview
    st.markdown("### 🌟 Industry Overview")
    
    industries = industry_data['industries']
    cols = st.columns(3)
    
    for idx, (industry, data) in enumerate(industries.items()):
        col_idx = idx % 3
        with cols[col_idx]:
            emoji_map = {
                'Artificial Intelligence': '🤖', 'Blockchain & Web3': '🔗',
                'Renewable Energy': '🌱', 'Biotechnology': '🧬',
                'Space Technology': '🚀', 'Cybersecurity': '🔒',
                'Quantum Computing': '⚛️', 'IoT & Edge Computing': '📡'
            }
            emoji = emoji_map.get(industry, '💼')
            
            difficulty_colors = {'Medium': '#00ff88', 'High': '#ffaa00', 'Very High': '#ff4455'}
            difficulty_color = difficulty_colors.get(data['difficulty'], '#888888')
            
            st.markdown(f"""
            <div class="industry-item">
                <h4 style="color: #ff45ff; margin-bottom: 1rem;">{emoji} {industry}</h4>
                <p style="font-size: 0.9em; margin-bottom: 1rem;">{data['description']}</p>
                <div style="text-align: left;">
                    <p><strong>Growth:</strong> +{data['growth']}%</p>
                    <p><strong>Salary:</strong> ${data['min_salary']}K-${data['max_salary']}K</p>
                    <p><strong>Remote:</strong> {data['remote_friendly']}%</p>
                    <p><strong>Security:</strong> {data['job_security']}/10</p>
                </div>
                <div style="margin-top: 1rem;">
                    <span style="background: {difficulty_color}; color: white; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.8em;">
                        {data['difficulty']} Entry
                    </span>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Quick actions
    st.markdown("### 🎯 Quick Actions")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📋 Skill Assessment", use_container_width=True):
            st.info("🚧 Feature in development!")
    
    with col2:
        if st.button("💬 AI Chat", use_container_width=True):
            st.info("🚧 Feature in development!")
    
    with col3:
        if st.button("🎓 Learning Paths", use_container_width=True):
            st.info("🚧 Feature in development!")
    
    with col4:
        if st.button("📊 Deep Dive", use_container_width=True):
            st.info("💎 Premium feature coming soon!")
    
    # Footer
    st.markdown("""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(139, 69, 255, 0.1), rgba(255, 69, 255, 0.1)); 
         border: 1px solid #8b45ff; border-radius: 15px; margin-top: 3rem;">
        <h4 style="color: #ff45ff;">⚠️ Important Disclaimer</h4>
        <p><strong>Educational purposes only. Not professional career counseling.</strong></p>
        <p>AI responses may contain errors. Verify information independently.</p>
        <hr style="border-color: rgba(139, 69, 255, 0.3); margin: 1.5rem 0;">
        <p><strong>© 2025 Career Shift Analyzer Pro</strong></p>
        <p>👥 Developed by <strong>MS Hadianto</strong> & <strong>Faby</strong></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()