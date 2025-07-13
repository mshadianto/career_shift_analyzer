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

# Enhanced Futuristic Theme CSS with Glassmorphism and Animations
def load_custom_css():
    """Load enhanced futuristic CSS with glassmorphism effects and animations"""
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Orbitron:wght@400;700;900&family=Exo+2:wght@300;400;500;600;700&display=swap');
        
        /* Global Variables */
        :root {
            --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            --secondary-gradient: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            --success-gradient: linear-gradient(135deg, #00d4aa 0%, #01a3a4 100%);
            --warning-gradient: linear-gradient(135deg, #feca57 0%, #ff9ff3 100%);
            --cyber-glow: 0 0 20px rgba(102, 126, 234, 0.5);
            --neon-blue: #00f0ff;
            --neon-purple: #b347d9;
            --neon-pink: #ff006e;
        }
        
        /* Enhanced Global Dark Theme */
        .stApp {
            background: linear-gradient(135deg, #0a0a0a 0%, #1a0e2e 25%, #2d1b3d 50%, #1a0e2e 75%, #0a0a0a 100%);
            color: #e0e0ff;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        
        /* Animated Background with Network Pattern */
        .stApp::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(circle at 20% 50%, rgba(0, 240, 255, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(179, 71, 217, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 40% 80%, rgba(255, 0, 110, 0.1) 0%, transparent 50%);
            animation: nebula 15s ease-in-out infinite;
            pointer-events: none;
            z-index: -1;
        }
        
        @keyframes nebula {
            0%, 100% { opacity: 0.7; }
            50% { opacity: 1; }
        }
        
        /* Futuristic Header with Enhanced Animation */
        .main-header {
            text-align: center;
            padding: 4rem 2rem;
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(20px);
            border: 2px solid rgba(0, 240, 255, 0.3);
            border-radius: 20px;
            margin-bottom: 3rem;
            box-shadow: 
                0 0 30px rgba(0, 240, 255, 0.5),
                inset 0 0 30px rgba(0, 240, 255, 0.1);
            position: relative;
            overflow: hidden;
        }
        
        .main-header::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, transparent, rgba(0, 240, 255, 0.1), transparent);
            animation: scan 4s linear infinite;
        }
        
        @keyframes scan {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .main-header h1 {
            font-family: 'Orbitron', monospace;
            font-weight: 900;
            font-size: 4rem;
            background: linear-gradient(45deg, #00f0ff, #b347d9, #ff006e, #00f0ff);
            background-size: 400% 400%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: gradientShift 3s ease-in-out infinite, glow 2s ease-in-out infinite alternate;
            margin: 0;
            letter-spacing: -0.02em;
        }
        
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        @keyframes glow {
            from { 
                text-shadow: 0 0 20px rgba(0, 240, 255, 0.5);
                filter: drop-shadow(0 0 10px rgba(0, 240, 255, 0.3));
            }
            to { 
                text-shadow: 0 0 30px rgba(179, 71, 217, 0.8), 0 0 40px rgba(255, 0, 110, 0.6);
                filter: drop-shadow(0 0 20px rgba(179, 71, 217, 0.5));
            }
        }
        
        /* Rotating Network Visualization */
        .hero-network {
            position: relative;
            width: 100%;
            height: 400px;
            background: radial-gradient(circle at center, rgba(0, 17, 34, 0.8) 0%, rgba(0, 8, 17, 0.9) 70%, rgba(0, 0, 0, 0.95) 100%);
            border-radius: 20px;
            overflow: hidden;
            margin: 2rem 0;
            box-shadow: 0 15px 50px rgba(0, 240, 255, 0.3);
            backdrop-filter: blur(10px);
        }
        
        .network-visualization {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 350px;
            height: 350px;
            background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400"><defs><radialGradient id="centerGlow" cx="50%" cy="50%" r="50%"><stop offset="0%" style="stop-color:%23ffffff;stop-opacity:1" /><stop offset="50%" style="stop-color:%2300f0ff;stop-opacity:0.8" /><stop offset="100%" style="stop-color:%23001122;stop-opacity:0.2" /></radialGradient><filter id="glow"><feGaussianBlur stdDeviation="3" result="coloredBlur"/><feMerge><feMergeNode in="coloredBlur"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs><circle cx="200" cy="200" r="150" fill="none" stroke="%2300f0ff" stroke-width="1" opacity="0.6"/><circle cx="200" cy="200" r="100" fill="none" stroke="%23b347d9" stroke-width="1" opacity="0.8"/><circle cx="200" cy="200" r="50" fill="url(%23centerGlow)" opacity="0.9"/><g filter="url(%23glow)"><circle cx="200" cy="80" r="8" fill="%2300f0ff" opacity="0.9"><animate attributeName="opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite"/></circle><circle cx="320" cy="200" r="6" fill="%23ff006e" opacity="0.8"><animate attributeName="opacity" values="0.3;0.9;0.3" dur="1.5s" repeatCount="indefinite"/></circle><circle cx="200" cy="320" r="7" fill="%23b347d9" opacity="0.9"><animate attributeName="opacity" values="0.6;1;0.6" dur="2.2s" repeatCount="indefinite"/></circle><circle cx="80" cy="200" r="5" fill="%2300ff88" opacity="0.7"><animate attributeName="opacity" values="0.4;0.8;0.4" dur="1.8s" repeatCount="indefinite"/></circle><line x1="200" y1="200" x2="200" y2="80" stroke="%2300f0ff" stroke-width="1" opacity="0.4"><animate attributeName="opacity" values="0.2;0.6;0.2" dur="3s" repeatCount="indefinite"/></line><line x1="200" y1="200" x2="320" y2="200" stroke="%23ff006e" stroke-width="1" opacity="0.4"><animate attributeName="opacity" values="0.1;0.5;0.1" dur="2.5s" repeatCount="indefinite"/></line><line x1="200" y1="200" x2="200" y2="320" stroke="%23b347d9" stroke-width="1" opacity="0.4"><animate attributeName="opacity" values="0.3;0.7;0.3" dur="2.8s" repeatCount="indefinite"/></line><line x1="200" y1="200" x2="80" y2="200" stroke="%2300ff88" stroke-width="1" opacity="0.4"><animate attributeName="opacity" values="0.2;0.6;0.2" dur="2.2s" repeatCount="indefinite"/></line></g></svg>');
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
            animation: rotateNetwork 20s linear infinite;
            filter: drop-shadow(0 0 20px rgba(0, 240, 255, 0.6));
        }
        
        @keyframes rotateNetwork {
            0% { transform: translate(-50%, -50%) rotate(0deg); }
            100% { transform: translate(-50%, -50%) rotate(360deg); }
        }
        
        .network-overlay {
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at center, transparent 40%, rgba(0, 240, 255, 0.1) 60%, rgba(179, 71, 217, 0.15) 80%);
            animation: pulse 4s ease-in-out infinite;
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 0.5; }
            50% { opacity: 1; }
        }
        
        /* Enhanced Glassmorphism Cards */
        .glass-card, .neon-card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(0, 240, 255, 0.2);
            border-radius: 20px;
            padding: 2rem;
            margin: 1rem 0;
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.3);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }
        
        .glass-card:hover, .neon-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 25px 50px rgba(0, 240, 255, 0.3);
            border-color: rgba(0, 240, 255, 0.5);
        }
        
        .glass-card::before, .neon-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.1), transparent);
            transition: left 0.5s;
        }
        
        .glass-card:hover::before, .neon-card:hover::before {
            left: 100%;
        }
        
        /* Enhanced Metric Cards */
        .metric-card, .stat-card {
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(0, 240, 255, 0.2);
            border-radius: 16px;
            padding: 1.5rem;
            text-align: center;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
            margin: 1rem 0.5rem;
        }
        
        .metric-card:hover, .stat-card:hover {
            border-color: rgba(0, 240, 255, 0.5);
            box-shadow: 0 10px 30px rgba(0, 240, 255, 0.2);
            transform: scale(1.05);
        }
        
        .metric-number {
            font-size: 2.5rem;
            font-weight: 800;
            background: var(--primary-gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .stat-card h3 {
            font-family: 'Orbitron', monospace;
            color: #00f0ff;
            text-shadow: 0 0 10px #00f0ff;
        }
        
        .metric-label {
            color: #b0b3b8;
            font-size: 0.9rem;
            margin-top: 0.5rem;
        }
        
        /* Hero Container with Glassmorphism */
        .hero-container {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 3rem 2rem;
            text-align: center;
            margin: 2rem 0;
        }
        
        /* Enhanced Feature Cards */
        .feature-card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(0, 240, 255, 0.2);
            border-radius: 15px;
            padding: 2rem;
            margin: 2rem 0;
            transition: all 0.3s ease;
            box-shadow: 0 0 20px rgba(0, 240, 255, 0.2);
            position: relative;
            overflow: hidden;
        }
        
        .feature-card:hover {
            transform: translateY(-10px);
            border-color: rgba(179, 71, 217, 0.5);
            box-shadow: 0 20px 40px rgba(179, 71, 217, 0.3);
        }
        
        /* Enhanced Industry Cards */
        .industry-item {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(0, 240, 255, 0.2);
            border-radius: 15px;
            padding: 2rem;
            text-align: center;
            transition: all 0.3s ease;
            box-shadow: 0 0 15px rgba(0, 240, 255, 0.2);
            position: relative;
            overflow: hidden;
        }
        
        .industry-item:hover {
            transform: translateY(-10px) scale(1.02);
            border-color: rgba(255, 0, 110, 0.5);
            box-shadow: 0 20px 40px rgba(255, 0, 110, 0.3);
        }
        
        /* Success Stories with Enhanced Design */
        .success-story {
            background: rgba(0, 212, 170, 0.05);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(0, 212, 170, 0.3);
            border-radius: 15px;
            padding: 2rem;
            margin: 2rem 0;
            border-left: 4px solid #00d4aa;
            box-shadow: 0 0 20px rgba(0, 255, 136, 0.2);
            transition: all 0.3s ease;
        }
        
        .success-story:hover {
            transform: translateX(10px);
            box-shadow: 0 0 30px rgba(0, 255, 136, 0.4);
        }
        
        /* Enhanced Chart Container */
        .chart-container {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(0, 240, 255, 0.2);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 0 25px rgba(0, 240, 255, 0.2);
            margin: 2rem 0;
        }
        
        /* Enhanced Buttons */
        .stButton > button {
            background: linear-gradient(135deg, #00f0ff, #b347d9);
            color: white;
            border: none;
            border-radius: 12px;
            padding: 0.75rem 2rem;
            font-family: 'Exo 2', sans-serif;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: all 0.3s ease;
            box-shadow: 0 0 15px rgba(0, 240, 255, 0.4);
            position: relative;
            overflow: hidden;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 25px rgba(179, 71, 217, 0.5);
        }
        
        /* Version Info with Glassmorphism */
        .version-info {
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(0, 240, 255, 0.1);
            backdrop-filter: blur(15px);
            border: 1px solid rgba(0, 240, 255, 0.3);
            border-radius: 20px;
            padding: 0.8rem 1.5rem;
            font-family: 'Orbitron', monospace;
            color: #00f0ff;
            z-index: 1000;
            box-shadow: 0 0 15px rgba(0, 240, 255, 0.3);
            text-shadow: 0 0 5px #00f0ff;
        }
        
        /* Enhanced Sidebar */
        .css-1d391kg {
            background: rgba(10, 14, 26, 0.95);
            backdrop-filter: blur(20px);
            border-right: 1px solid rgba(0, 240, 255, 0.1);
        }
        
        /* Text Elements Enhancement */
        h1, h2, h3, h4 {
            font-family: 'Orbitron', monospace;
            color: #e0e0ff;
        }
        
        p, span, div {
            font-family: 'Exo 2', sans-serif;
            color: #c0c0ff;
        }
        
        /* Loading Animation */
        .loading-spinner {
            border: 3px solid rgba(0, 240, 255, 0.3);
            border-radius: 50%;
            border-top: 3px solid #00f0ff;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 20px auto;
        }
        
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        /* Enhanced Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: rgba(255, 255, 255, 0.05);
        }
        
        ::-webkit-scrollbar-thumb {
            background: rgba(0, 240, 255, 0.5);
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: rgba(0, 240, 255, 0.8);
        }
        
        /* Mobile Responsiveness */
        @media (max-width: 768px) {
            .main-header h1 { font-size: 2.5rem; }
            .hero-network { height: 250px; }
            .network-visualization { width: 200px; height: 200px; }
            .glass-card, .neon-card { padding: 1rem; }
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
        title_font=dict(size=18, color='#00f0ff', family="Orbitron"),
        xaxis=dict(gridcolor='rgba(0, 240, 255, 0.2)'),
        yaxis=dict(gridcolor='rgba(0, 240, 255, 0.2)')
    )
    
    return fig

def create_salary_comparison_chart(df: pd.DataFrame) -> go.Figure:
    """Create enhanced salary comparison chart with dark theme"""
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Min Salary',
        x=df['Industry'],
        y=df['Min Salary'],
        marker_color='rgba(0, 240, 255, 0.7)',
        text=df['Min Salary'],
        textposition='auto'
    ))
    
    fig.add_trace(go.Bar(
        name='Max Salary',
        x=df['Industry'],
        y=df['Max Salary'],
        marker_color='rgba(179, 71, 217, 0.7)',
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
        title_font=dict(color='#00f0ff', family="Orbitron"),
        xaxis=dict(tickangle=45, gridcolor='rgba(0, 240, 255, 0.2)'),
        yaxis=dict(gridcolor='rgba(0, 240, 255, 0.2)')
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
        line_color='rgb(0, 240, 255)', fillcolor='rgba(0, 240, 255, 0.3)'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=blockchain_scores, theta=categories, fill='toself', name='Blockchain',
        line_color='rgb(179, 71, 217)', fillcolor='rgba(179, 71, 217, 0.3)'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=cybersec_scores, theta=categories, fill='toself', name='Cybersecurity',
        line_color='rgb(0, 255, 136)', fillcolor='rgba(0, 255, 136, 0.3)'
    ))
    
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 10], gridcolor='rgba(0, 240, 255, 0.2)')),
        showlegend=True, title="🎯 Industry Skill Requirements Comparison", height=500,
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e0ff', family="Exo 2"),
        title_font=dict(color='#00f0ff', family="Orbitron")
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
    
    # Enhanced Header with Network Visualization
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
    
    # Add Network Visualization Hero Section
    st.markdown("""
    <div class="hero-network">
        <div class="network-visualization"></div>
        <div class="network-overlay"></div>
    </div>
    """, unsafe_allow_html=True)
    
    # Hero section with enhanced glassmorphism
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="glass-card">
            <h3 style="color: #00f0ff; text-align: center; margin-bottom: 1.5rem;">🎯 Transform Your Career Journey</h3>
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
    
    # Quick stats with enhanced metrics
    st.markdown("### 📊 Live Industry Insights")
    df = process_trend_data()
    
    col1, col2, col3, col4 = st.columns(4)
    
    # Display top 4 industries with enhanced styling
    top_industries = ['Artificial Intelligence', 'Blockchain & Web3', 'Cybersecurity', 'Quantum Computing']
    
    for idx, industry in enumerate(top_industries):
        data = df[df['Industry'] == industry].iloc[0]
        with [col1, col2, col3, col4][idx]:
            emoji = ['🤖', '🔗', '🔒', '⚛️'][idx]
            st.markdown(f"""
            <div class="stat-card">
                <h3>{emoji} {industry.split(' ')[0]}</h3>
                <p class="metric-number">+{data['Job Growth (%)']}%</p>
                <p class="metric-label">annual growth</p>
                <p>${data['Min Salary']:.0f}K-${data['Max Salary']:.0f}K</p>
                <p style="font-size: 0.9em; opacity: 0.9;">🔥 {data['Remote Friendly (%)']}% Remote</p>
            </div>
            """, unsafe_allow_html=True)
    
    # Features section with enhanced cards
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
                <h4 style="color: #00f0ff; margin-bottom: 1rem;">{feature['title']}</h4>
                <p style="line-height: 1.6; margin-bottom: 1.5rem;">{feature['desc']}</p>
                <div>
                    {' '.join([f'<span style="background: rgba(0, 240, 255, 0.2); color: #00f0ff; padding: 0.3rem 0.8rem; border-radius: 15px; font-size: 0.8em; margin-right: 0.5rem;">{tag}</span>' for tag in feature['tags']])}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # Visualizations with enhanced containers
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
    
    # Success stories with enhanced styling
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
                <span style="background: #b347d9; color: white; padding: 0.3rem 0.8rem; border-radius: 15px; margin-right: 0.5rem;">
                    💰 +{story['salary_increase']}%
                </span>
                <span style="background: #00f0ff; color: black; padding: 0.3rem 0.8rem; border-radius: 15px;">
                    🎓 {len(story['skills_learned'])} skills
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Industry overview with enhanced cards
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
                <h4 style="color: #00f0ff; margin-bottom: 1rem;">{emoji} {industry}</h4>
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
    
    # Quick actions with enhanced buttons
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
    
    # Enhanced Footer
    st.markdown("""
    <div style="text-align: center; padding: 3rem 2rem; background: rgba(255, 255, 255, 0.03); 
         backdrop-filter: blur(20px); border: 1px solid rgba(0, 240, 255, 0.2); border-radius: 20px; margin-top: 3rem;">
        <h4 style="color: #00f0ff; margin-bottom: 1.5rem;">⚠️ Important Disclaimer</h4>
        <p style="margin-bottom: 1rem;"><strong>Educational purposes only. Not professional career counseling.</strong></p>
        <p style="margin-bottom: 2rem;">AI responses may contain errors. Verify information independently.</p>
        <hr style="border-color: rgba(0, 240, 255, 0.3); margin: 2rem 0;">
        <p style="font-size: 1.1em; margin-bottom: 0.5rem;"><strong>© 2025 Career Shift Analyzer Pro</strong></p>
        <p style="opacity: 0.8;">👥 Developed by <strong>MS Hadianto</strong> & <strong>Faby</strong></p>
        <div style="margin-top: 2rem;">
            <span style="background: rgba(0, 240, 255, 0.2); color: #00f0ff; padding: 0.5rem 1rem; border-radius: 20px; margin: 0 0.5rem;">
                🚀 Future Ready
            </span>
            <span style="background: rgba(179, 71, 217, 0.2); color: #b347d9; padding: 0.5rem 1rem; border-radius: 20px; margin: 0 0.5rem;">
                🤖 AI-Powered
            </span>
            <span style="background: rgba(0, 255, 136, 0.2); color: #00ff88; padding: 0.5rem 1rem; border-radius: 20px; margin: 0 0.5rem;">
                ✨ Enhanced UI
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
