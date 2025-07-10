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

# Import universal footer
try:
    from utils.footer import render_universal_footer, add_disclaimer_warning
except ImportError:
    # Fallback if utils folder doesn't exist
    def render_universal_footer():
        st.markdown("**Footer not available. Please ensure utils/footer.py exists.**")
    def add_disclaimer_warning():
        pass

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
@st.cache_data(ttl=3600)  # Cache for 1 hour
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

# Enhanced data loading with caching
@st.cache_data(ttl=1800)  # Cache for 30 minutes
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
                'name': 'Sarah Chen',
                'from': 'Accountant',
                'to': 'AI Engineer',
                'duration': '8 months',
                'salary_increase': 60,
                'story': 'Used Career Shift Analyzer to transition from finance to AI. The skill gap analysis showed me exactly what to learn. Now earning 60% more at a tech startup!',
                'skills_learned': ['Python', 'Machine Learning', 'Data Science'],
                'company': 'TechStart Inc.'
            },
            {
                'name': 'Ahmad Rodriguez',
                'from': 'Marketing Manager',
                'to': 'Blockchain Developer',
                'duration': '10 months',
                'salary_increase': 80,
                'story': 'The platform\'s learning roadmap guided me from zero coding experience to landing a blockchain developer role. The AI assistant was incredibly helpful!',
                'skills_learned': ['Solidity', 'Web3', 'Smart Contracts'],
                'company': 'CryptoSolutions'
            },
            {
                'name': 'Dr. Emily Watson',
                'from': 'Research Scientist',
                'to': 'Quantum Computing Researcher',
                'duration': '6 months',
                'salary_increase': 40,
                'story': 'Leveraged my physics background to transition into quantum computing. The industry insights helped me target the right companies.',
                'skills_learned': ['Qiskit', 'Quantum Algorithms', 'IBM Quantum'],
                'company': 'Quantum Dynamics'
            }
        ]
    }

# Enhanced custom CSS with new features
def load_custom_css():
    """Load enhanced custom CSS with modern animations and responsive design"""
    st.markdown("""
    <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* Global Styles */
        * {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        
        .main-header {
            text-align: center;
            padding: 4rem 2rem;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #f093fb 50%, #f5576c 75%, #4facfe 100%);
            color: white;
            border-radius: 25px;
            margin-bottom: 3rem;
            box-shadow: 0 25px 50px rgba(102, 126, 234, 0.4);
            position: relative;
            overflow: hidden;
            animation: headerPulse 6s ease-in-out infinite;
        }
        
        @keyframes headerPulse {
            0%, 100% { box-shadow: 0 25px 50px rgba(102, 126, 234, 0.4); }
            50% { box-shadow: 0 35px 70px rgba(102, 126, 234, 0.6); }
        }
        
        .main-header::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
            animation: shine 4s infinite;
        }
        
        @keyframes shine {
            0% { left: -100%; }
            100% { left: 100%; }
        }
        
        /* Enhanced Feature Cards */
        .feature-card {
            background: linear-gradient(145deg, #ffffff, #f8f9ff);
            padding: 2.5rem 2rem;
            border-radius: 25px;
            border: 2px solid transparent;
            margin: 2rem 0;
            transition: all 0.5s cubic-bezier(0.25, 0.8, 0.25, 1);
            box-shadow: 0 15px 35px rgba(0,0,0,0.08), 0 5px 15px rgba(0,0,0,0.12);
            position: relative;
            overflow: hidden;
            cursor: pointer;
        }
        
        .feature-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 4px;
            height: 100%;
            background: linear-gradient(135deg, #667eea, #764ba2);
            transition: all 0.4s ease;
        }
        
        .feature-card:hover {
            transform: translateY(-20px) scale(1.02);
            box-shadow: 0 35px 70px rgba(102, 126, 234, 0.25), 0 15px 30px rgba(0,0,0,0.15);
            border-color: rgba(102, 126, 234, 0.3);
        }
        
        .feature-card:hover::before {
            width: 100%;
            opacity: 0.05;
        }
        
        /* Enhanced Stat Cards */
        .stat-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            color: white;
            padding: 2.5rem 1.5rem;
            border-radius: 25px;
            text-align: center;
            margin: 1rem 0.5rem;
            transition: all 0.5s cubic-bezier(0.25, 0.8, 0.25, 1);
            box-shadow: 0 20px 40px rgba(102, 126, 234, 0.4);
            position: relative;
            overflow: hidden;
            cursor: pointer;
            border: 2px solid rgba(255,255,255,0.1);
        }
        
        .stat-card::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            background: radial-gradient(circle, rgba(255,255,255,0.2), transparent);
            transition: all 0.6s ease;
            transform: translate(-50%, -50%);
            border-radius: 50%;
        }
        
        .stat-card:hover::before {
            width: 400px;
            height: 400px;
        }
        
        .stat-card:hover {
            transform: translateY(-15px) rotateY(8deg) scale(1.05);
            box-shadow: 0 35px 70px rgba(102, 126, 234, 0.5);
        }
        
        /* Enhanced Version Info */
        .version-info {
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(102, 126, 234, 0.1);
            border: 2px solid rgba(102, 126, 234, 0.3);
            border-radius: 30px;
            padding: 0.8rem 1.5rem;
            font-size: 0.9em;
            color: #667eea;
            z-index: 1000;
            backdrop-filter: blur(20px);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.2);
            transition: all 0.4s ease;
            font-weight: 600;
        }
        
        .version-info:hover {
            transform: scale(1.1) rotate(2deg);
            background: rgba(102, 126, 234, 0.2);
            color: #4c63d2;
        }
        
        /* Enhanced Success Stories */
        .success-story {
            background: linear-gradient(145deg, #f8fffe, #e8f5f3);
            border-radius: 25px;
            padding: 2.5rem;
            margin: 2rem 0;
            border-left: 8px solid #28a745;
            transition: all 0.5s cubic-bezier(0.25, 0.8, 0.25, 1);
            box-shadow: 0 15px 35px rgba(0,0,0,0.08);
            position: relative;
            overflow: hidden;
        }
        
        .success-story::before {
            content: '';
            position: absolute;
            top: 0;
            right: 0;
            width: 120px;
            height: 120px;
            background: linear-gradient(135deg, #28a745, #20c997);
            border-radius: 50%;
            transform: translate(60%, -60%);
            opacity: 0.1;
        }
        
        .success-story:hover {
            transform: translateX(20px) scale(1.02);
            box-shadow: 0 25px 50px rgba(40, 167, 69, 0.2);
            border-left-width: 12px;
        }
        
        /* Enhanced Industry Grid */
        .industry-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
            margin: 2rem 0;
        }
        
        .industry-item {
            background: linear-gradient(145deg, #ffffff, #f8f9ff);
            border: 2px solid transparent;
            border-radius: 20px;
            padding: 2rem;
            text-align: center;
            transition: all 0.5s cubic-bezier(0.25, 0.8, 0.25, 1);
            box-shadow: 0 10px 30px rgba(0,0,0,0.08);
            position: relative;
            overflow: hidden;
            cursor: pointer;
        }
        
        .industry-item::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 6px;
            background: linear-gradient(90deg, #667eea, #764ba2);
            transform: scaleX(0);
            transition: transform 0.4s ease;
        }
        
        .industry-item:hover::before {
            transform: scaleX(1);
        }
        
        .industry-item:hover {
            border-color: rgba(102, 126, 234, 0.4);
            transform: translateY(-15px) scale(1.03);
            box-shadow: 0 25px 50px rgba(102, 126, 234, 0.2);
        }
        
        /* Enhanced Chart Container */
        .chart-container {
            background: linear-gradient(145deg, #ffffff, #f8f9ff);
            padding: 2.5rem;
            border-radius: 25px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
            margin: 2rem 0;
            transition: all 0.4s ease;
            border: 2px solid rgba(102, 126, 234, 0.1);
            position: relative;
            overflow: hidden;
        }
        
        .chart-container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: linear-gradient(45deg, transparent 30%, rgba(102, 126, 234, 0.02) 50%, transparent 70%);
            pointer-events: none;
        }
        
        .chart-container:hover {
            transform: translateY(-8px);
            box-shadow: 0 30px 60px rgba(0,0,0,0.15);
            border-color: rgba(102, 126, 234, 0.3);
        }
        
        /* Disclaimer Banner */
        .disclaimer-banner {
            background: linear-gradient(135deg, #ffc107, #fd7e14);
            color: white;
            padding: 1rem 2rem;
            border-radius: 15px;
            margin: 1rem 0;
            text-align: center;
            box-shadow: 0 5px 15px rgba(255, 193, 7, 0.3);
            font-weight: 500;
        }
        
        /* Enhanced Responsive Design */
        @media (max-width: 1200px) {
            .main-header { padding: 3rem 1.5rem; }
            .chart-container { padding: 2rem; }
        }
        
        @media (max-width: 768px) {
            .main-header { 
                padding: 2rem 1rem; 
                border-radius: 15px;
            }
            .feature-card, .stat-card { 
                margin: 1rem 0; 
                padding: 2rem 1.5rem;
            }
            .industry-grid { 
                grid-template-columns: 1fr; 
                gap: 1.5rem; 
            }
            .version-info {
                position: relative;
                top: auto;
                right: auto;
                margin: 1rem 0;
                display: block;
                text-align: center;
            }
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
    """Create an advanced interactive bubble chart"""
    fig = px.scatter(
        df, 
        x='Job Growth (%)', 
        y='Avg Salary (K)', 
        size='Market Size (B)', 
        hover_name='Industry',
        title='🎯 Industry Growth vs Salary vs Market Size Analysis',
        labels={
            'Job Growth (%)': 'Job Growth Rate (%)', 
            'Avg Salary (K)': 'Average Salary ($K)',
            'Market Size (B)': 'Market Size ($B)'
        },
        color='Remote Friendly (%)',
        color_continuous_scale='Viridis',
        size_max=80,
        hover_data={
            'Job Security': True,
            'Remote Friendly (%)': True,
            'Market Size (B)': ':,.0f'
        }
    )
    
    fig.update_layout(
        height=700,
        showlegend=True,
        title_x=0.5,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=12, family="Inter"),
        title_font=dict(size=18, color='#333', family="Inter"),
        coloraxis_colorbar=dict(
            title="Remote Friendly %",
            title_font=dict(size=12),
            tickfont=dict(size=10)
        )
    )
    
    fig.update_traces(
        marker=dict(
            line=dict(width=2, color='white'),
            opacity=0.8
        ),
        selector=dict(mode='markers')
    )
    
    return fig

def create_salary_comparison_chart(df: pd.DataFrame) -> go.Figure:
    """Create enhanced salary comparison chart"""
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Min Salary',
        x=df['Industry'],
        y=df['Min Salary'],
        marker_color='rgba(102, 126, 234, 0.7)',
        text=df['Min Salary'],
        textposition='auto',
        hovertemplate='<b>%{x}</b><br>Min Salary: $%{y}K<extra></extra>'
    ))
    
    fig.add_trace(go.Bar(
        name='Max Salary',
        x=df['Industry'],
        y=df['Max Salary'],
        marker_color='rgba(118, 75, 162, 0.7)',
        text=df['Max Salary'],
        textposition='auto',
        hovertemplate='<b>%{x}</b><br>Max Salary: $%{y}K<extra></extra>'
    ))
    
    fig.update_layout(
        title='💰 Salary Ranges by Industry (2024)',
        xaxis_title='Industry',
        yaxis_title='Salary ($K)',
        barmode='group',
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Inter"),
        title_font=dict(size=16, color='#333'),
        xaxis=dict(tickangle=45)
    )
    
    return fig

def create_skill_radar_chart() -> go.Figure:
    """Create enhanced skill requirements radar chart"""
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
        r=ai_scores,
        theta=categories,
        fill='toself',
        name='AI/ML',
        line_color='rgb(102, 126, 234)',
        fillcolor='rgba(102, 126, 234, 0.3)'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=blockchain_scores,
        theta=categories,
        fill='toself',
        name='Blockchain',
        line_color='rgb(118, 75, 162)',
        fillcolor='rgba(118, 75, 162, 0.3)'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=cybersec_scores,
        theta=categories,
        fill='toself',
        name='Cybersecurity',
        line_color='rgb(244, 147, 66)',
        fillcolor='rgba(244, 147, 66, 0.3)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10],
                tickfont=dict(size=10)
            )
        ),
        showlegend=True,
        title="Industry Skill Requirements Comparison",
        height=500,
        font=dict(family="Inter"),
        title_font=dict(size=16, color='#333')
    )
    
    return fig

def create_growth_timeline_chart(df: pd.DataFrame) -> go.Figure:
    """Create growth timeline projection chart"""
    years = list(range(2024, 2030))
    
    fig = go.Figure()
    
    # Select top 4 growing industries
    top_industries = df.nlargest(4, 'Job Growth (%)')
    
    colors = ['#667eea', '#764ba2', '#f093fb', '#f5576c']
    
    for idx, (_, row) in enumerate(top_industries.iterrows()):
        growth_rate = row['Job Growth (%)'] / 100
        # Project growth with some realistic variation
        projected_jobs = [100]  # Base index
        for year in range(1, len(years)):
            next_val = projected_jobs[-1] * (1 + growth_rate + np.random.normal(0, 0.02))
            projected_jobs.append(max(next_val, projected_jobs[-1] * 0.95))  # Prevent negative growth
        
        fig.add_trace(go.Scatter(
            x=years,
            y=projected_jobs,
            mode='lines+markers',
            name=row['Industry'],
            line=dict(color=colors[idx], width=3),
            marker=dict(size=8),
            hovertemplate=f'<b>{row["Industry"]}</b><br>Year: %{{x}}<br>Job Index: %{{y:.1f}}<extra></extra>'
        ))
    
    fig.update_layout(
        title='📈 Job Growth Projections (2024-2030)',
        xaxis_title='Year',
        yaxis_title='Job Availability Index',
        height=500,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Inter"),
        title_font=dict(size=16, color='#333'),
        hovermode='x unified'
    )
    
    return fig

# Main application
def main():
    """Main application function with enhanced features"""
    
    # Load custom CSS
    load_custom_css()
    
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
    
    # Enhanced Header with real-time stats
    current_time = datetime.now().strftime("%H:%M UTC")
    st.markdown(f"""
    <div class="main-header">
        <h1 style="margin: 0; font-size: 3.5em; font-weight: 700; text-shadow: 0 4px 8px rgba(0,0,0,0.3);">
            🚀 Career Shift Analyzer Pro
        </h1>
        <p style="font-size: 1.4em; margin: 1.5rem 0; opacity: 0.95; text-shadow: 0 2px 4px rgba(0,0,0,0.3);">
            Navigate Your Future in Emerging Industries
        </p>
        <p style="font-size: 1.1em; margin: 1rem 0; opacity: 0.85;">
            AI-Powered Career Guidance Platform with Real-Time Industry Insights
        </p>
        <div style="margin-top: 2rem; font-size: 0.9em; opacity: 0.8;">
            <span style="margin-right: 2rem;">🌍 Global Coverage</span>
            <span style="margin-right: 2rem;">⏰ Last Updated: {current_time}</span>
            <span>👥 {len(industry_data['industries'])} Industries Tracked</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Hero section with enhanced CTA
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        ### 🎯 Transform Your Career Journey Today
        
        Discover high-growth opportunities in **AI, Blockchain, Quantum Computing, Renewable Energy, Biotech,** and more. 
        Get personalized insights, comprehensive skill gap analysis, and AI-powered career guidance tailored to your goals.
        
        **✨ What makes us different:**
        - Real-time industry data and salary insights
        - AI-powered personalized recommendations
        - Interactive skill assessments and learning paths
        - Success stories from real career transitions
        """)
        
        col_a, col_b = st.columns(2)
        with col_a:
            if st.button("🚀 Start Your Analysis", type="primary", use_container_width=True):
                st.switch_page("pages/2_Skill_Gap_Analysis.py")
        with col_b:
            if st.button("💬 Chat with AI Assistant", type="secondary", use_container_width=True):
                st.switch_page("pages/3_Career_Chat_Assistant.py")
    
    # Enhanced Quick stats with real data
    st.markdown("### 📊 Live Industry Insights")
    
    # Process data for stats
    df = process_trend_data()
    
    col1, col2, col3, col4 = st.columns(4)
    
    # AI Stats
    ai_data = df[df['Industry'] == 'Artificial Intelligence'].iloc[0]
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <h3 style="margin: 0 0 1rem 0;">🤖 AI/ML</h3>
            <p style="font-size: 1.8em; margin: 0.5rem 0; font-weight: bold;">+{ai_data['Job Growth (%)']}%</p>
            <p style="margin: 0.5rem 0;">annual growth</p>
            <p style="margin: 0.5rem 0;">${ai_data['Min Salary']:.0f}K-${ai_data['Max Salary']:.0f}K salary</p>
            <p style="font-size: 0.9em; margin-top: 1rem; opacity: 0.9;">🔥 {ai_data['Remote Friendly (%)']}% Remote Friendly</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Blockchain Stats
    blockchain_data = df[df['Industry'] == 'Blockchain & Web3'].iloc[0]
    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <h3 style="margin: 0 0 1rem 0;">🔗 Blockchain</h3>
            <p style="font-size: 1.8em; margin: 0.5rem 0; font-weight: bold;">+{blockchain_data['Job Growth (%)']}%</p>
            <p style="margin: 0.5rem 0;">annual growth</p>
            <p style="margin: 0.5rem 0;">${blockchain_data['Min Salary']:.0f}K-${blockchain_data['Max Salary']:.0f}K salary</p>
            <p style="font-size: 0.9em; margin-top: 1rem; opacity: 0.9;">🚀 {blockchain_data['Remote Friendly (%)']}% Remote Friendly</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Cybersecurity Stats
    cyber_data = df[df['Industry'] == 'Cybersecurity'].iloc[0]
    with col3:
        st.markdown(f"""
        <div class="stat-card">
            <h3 style="margin: 0 0 1rem 0;">🔒 Cybersecurity</h3>
            <p style="font-size: 1.8em; margin: 0.5rem 0; font-weight: bold;">+{cyber_data['Job Growth (%)']}%</p>
            <p style="margin: 0.5rem 0;">annual growth</p>
            <p style="margin: 0.5rem 0;">${cyber_data['Min Salary']:.0f}K-${cyber_data['Max Salary']:.0f}K salary</p>
            <p style="font-size: 0.9em; margin-top: 1rem; opacity: 0.9;">🛡️ {cyber_data['Remote Friendly (%)']}% Remote Friendly</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Quantum Computing Stats
    quantum_data = df[df['Industry'] == 'Quantum Computing'].iloc[0]
    with col4:
        st.markdown(f"""
        <div class="stat-card">
            <h3 style="margin: 0 0 1rem 0;">⚛️ Quantum</h3>
            <p style="font-size: 1.8em; margin: 0.5rem 0; font-weight: bold;">+{quantum_data['Job Growth (%)']}%</p>
            <p style="margin: 0.5rem 0;">annual growth</p>
            <p style="margin: 0.5rem 0;">${quantum_data['Min Salary']:.0f}K-${quantum_data['Max Salary']:.0f}K salary</p>
            <p style="font-size: 0.9em; margin-top: 1rem; opacity: 0.9;">🌟 {quantum_data['Remote Friendly (%)']}% Remote Friendly</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Enhanced Features section
    st.markdown("### ✨ Advanced Platform Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4 style="color: #667eea; margin-bottom: 1.5rem; font-size: 1.3em;">🎯 AI Career Simulation</h4>
            <p style="line-height: 1.8; margin-bottom: 1.5rem;">
                Experience interactive career path exploration with real market data, 
                salary projections, and personalized growth recommendations powered by machine learning.
            </p>
            <div style="margin-top: 1.5rem;">
                <span style="background: rgba(102, 126, 234, 0.1); color: #667eea; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.8em; margin-right: 0.5rem;">
                    💡 AI-Powered
                </span>
                <span style="background: rgba(40, 167, 69, 0.1); color: #28a745; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.8em;">
                    📊 Real-Time Data
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("🎮 Try Career Simulation", key="sim", use_container_width=True):
            st.switch_page("pages/1_Career_Simulation.py")
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4 style="color: #667eea; margin-bottom: 1.5rem; font-size: 1.3em;">📊 Advanced Skill Analysis</h4>
            <p style="line-height: 1.8; margin-bottom: 1.5rem;">
                Comprehensive 360° skill assessment with learning roadmaps, industry benchmarks, 
                and personalized recommendations based on your current abilities and career goals.
            </p>
            <div style="margin-top: 1.5rem;">
                <span style="background: rgba(102, 126, 234, 0.1); color: #667eea; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.8em; margin-right: 0.5rem;">
                    📈 Data-Driven
                </span>
                <span style="background: rgba(220, 53, 69, 0.1); color: #dc3545; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.8em;">
                    🎯 Personalized
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("📋 Analyze Your Skills", key="skills", use_container_width=True):
            st.switch_page("pages/2_Skill_Gap_Analysis.py")
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h4 style="color: #667eea; margin-bottom: 1.5rem; font-size: 1.3em;">🤖 AI Career Mentor</h4>
            <p style="line-height: 1.8; margin-bottom: 1.5rem;">
                24/7 intelligent career counseling with natural language processing, 
                industry expertise, and personalized guidance for your unique career journey.
            </p>
            <div style="margin-top: 1.5rem;">
                <span style="background: rgba(102, 126, 234, 0.1); color: #667eea; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.8em; margin-right: 0.5rem;">
                    🧠 LLM-Powered
                </span>
                <span style="background: rgba(255, 193, 7, 0.1); color: #ffc107; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.8em;">
                    ⚡ Instant
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("💬 Chat with AI Mentor", key="chat", use_container_width=True):
            st.switch_page("pages/3_Career_Chat_Assistant.py")
    
    # Enhanced visualizations section
    st.markdown("### 📈 Interactive Industry Analytics")
    
    # Main bubble chart
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    bubble_fig = create_advanced_bubble_chart(df)
    st.plotly_chart(bubble_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Additional charts in columns
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
    
    # Growth timeline chart
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    timeline_fig = create_growth_timeline_chart(df)
    st.plotly_chart(timeline_fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Enhanced Success stories section
    st.markdown("### 🌟 Real Success Stories")
    
    success_stories = industry_data['success_stories']
    
    for i, story in enumerate(success_stories):
        col1, col2 = st.columns([2, 1]) if i % 2 == 0 else st.columns([1, 2])
        
        with col1 if i % 2 == 0 else col2:
            st.markdown(f"""
            <div class="success-story">
                <h4 style="color: #28a745; margin-bottom: 1.5rem; font-size: 1.2em;">
                    👨‍💻 {story['from']} → {story['to']}
                </h4>
                <p style="line-height: 1.7; margin-bottom: 1.5rem; font-style: italic;">
                    "{story['story']}"
                </p>
                <p style="font-weight: 600; margin-bottom: 1rem; color: #333;">
                    — {story['name']}, {story['to']} at {story['company']}
                </p>
                <div style="margin-top: 1.5rem;">
                    <span style="background: #28a745; color: white; padding: 0.4rem 1rem; border-radius: 20px; font-size: 0.85em; margin-right: 0.8rem;">
                        ✅ {story['duration']} transition
                    </span>
                    <span style="background: #17a2b8; color: white; padding: 0.4rem 1rem; border-radius: 20px; font-size: 0.85em; margin-right: 0.8rem;">
                        💰 +{story['salary_increase']}% salary
                    </span>
                    <span style="background: #6f42c1; color: white; padding: 0.4rem 1rem; border-radius: 20px; font-size: 0.85em;">
                        🎓 {len(story['skills_learned'])} skills
                    </span>
                </div>
                <div style="margin-top: 1rem; font-size: 0.9em; color: #666;">
                    <strong>Skills learned:</strong> {', '.join(story['skills_learned'])}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Enhanced Industry overview
    st.markdown("### 🌟 Complete Industry Overview")
    
    industries = industry_data['industries']
    
    # Create responsive grid
    num_cols = 3 if len(industries) >= 6 else 2
    cols = st.columns(num_cols)
    
    for idx, (industry, data) in enumerate(industries.items()):
        col_idx = idx % num_cols
        with cols[col_idx]:
            # Determine emoji based on industry
            emoji_map = {
                'Artificial Intelligence': '🤖',
                'Blockchain & Web3': '🔗',
                'Renewable Energy': '🌱',
                'Biotechnology': '🧬',
                'Space Technology': '🚀',
                'Cybersecurity': '🔒',
                'Quantum Computing': '⚛️',
                'IoT & Edge Computing': '📡'
            }
            emoji = emoji_map.get(industry, '💼')
            
            difficulty_color = {
                'Medium': '#28a745',
                'High': '#ffc107',
                'Very High': '#dc3545'
            }.get(data['difficulty'], '#6c757d')
            
            st.markdown(f"""
            <div class="industry-item">
                <h4 style="color: #667eea; margin-bottom: 1.5rem; font-size: 1.2em;">
                    {emoji} {industry}
                </h4>
                <p style="line-height: 1.6; margin-bottom: 1rem; font-size: 0.9em; color: #666;">
                    {data['description']}
                </p>
                <div style="margin: 1rem 0;">
                    <p><strong>Growth Rate:</strong> +{data['growth']}% annually</p>
                    <p><strong>Salary Range:</strong> ${data['min_salary']}K-${data['max_salary']}K</p>
                    <p><strong>Remote Work:</strong> {data['remote_friendly']}% of positions</p>
                    <p><strong>Job Security:</strong> {data['job_security']}/10</p>
                </div>
                <div style="margin-top: 1.5rem;">
                    <span style="background: {difficulty_color}; color: white; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.8em; margin-right: 0.5rem;">
                        {data['difficulty']} Entry
                    </span>
                    <span style="background: rgba(102, 126, 234, 0.1); color: #667eea; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.8em;">
                        ${data['market_size']}B Market
                    </span>
                </div>
                <div style="margin-top: 1rem; font-size: 0.8em; color: #888;">
                    <strong>Key Skills:</strong> {', '.join(data['skills'][:3])}{'...' if len(data['skills']) > 3 else ''}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Enhanced Quick actions
    st.markdown("### 🎯 Quick Actions & Tools")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📋 Complete Skill Assessment", use_container_width=True, type="secondary"):
            st.switch_page("pages/2_Skill_Gap_Analysis.py")
    
    with col2:
        if st.button("💬 Ask AI Career Question", use_container_width=True, type="secondary"):
            st.switch_page("pages/3_Career_Chat_Assistant.py")
    
    with col3:
        if st.button("🎓 View Learning Paths", use_container_width=True, type="secondary"):
            st.info("🚧 Advanced learning recommendations coming soon!")
    
    with col4:
        if st.button("📊 Industry Deep Dive", use_container_width=True, type="secondary"):
            st.info("💎 Premium detailed reports - coming soon!")
    
    # Market insights section
    st.markdown("### 🔍 Key Market Insights")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("""
        **🎯 Fastest Growing Sectors**
        
        1. **Blockchain & Web3** (+35%)
        2. **Cybersecurity** (+35%)
        3. **Quantum Computing** (+25%)
        4. **AI/Machine Learning** (+22%)
        
        *Remote work availability: 80%+ average*
        """)
    
    with col2:
        st.success("""
        **💰 Highest Paying Fields**
        
        1. **Quantum Computing** ($120K-$250K)
        2. **Blockchain** ($90K-$200K)
        3. **AI/ML** ($80K-$180K)
        4. **Space Tech** ($85K-$160K)
        
        *Entry-level to senior ranges*
        """)
    
    with col3:
        st.warning("""
        **🎓 Skills in High Demand**
        
        - **Programming:** Python, Rust, Solidity
        - **AI/ML:** TensorFlow, PyTorch, NLP
        - **Security:** Penetration Testing, CISSP
        - **Cloud:** AWS, Azure, Kubernetes
        
        *Based on job market analysis*
        """)
    
    # Add disclaimer before footer
    st.markdown("""
    <div class="disclaimer-banner">
        ⚠️ <strong>Disclaimer:</strong> All career guidance, salary data, and AI recommendations are for informational purposes only. 
        Individual results may vary. Always verify information with professional sources and consult qualified career counselors for personalized advice.
    </div>
    """, unsafe_allow_html=True)
    
    # Enhanced footer with comprehensive disclaimers
    render_universal_footer()

if __name__ == "__main__":
    main()