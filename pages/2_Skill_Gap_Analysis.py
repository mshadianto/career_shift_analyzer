import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Skill Gap Analysis",
    page_icon="📊",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 3rem 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        color: white;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.3);
    }
    
    .skill-card {
        background: linear-gradient(145deg, #ffffff, #f8f9ff);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 5px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .skill-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.2);
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.3);
    }
    
    .skill-badge {
        display: inline-block;
        background: rgba(102, 126, 234, 0.1);
        color: #667eea;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        margin: 0.2rem;
        font-size: 0.9em;
        font-weight: 500;
        border: 1px solid rgba(102, 126, 234, 0.2);
    }
    
    .skill-badge.missing {
        background: rgba(220, 53, 69, 0.1);
        color: #dc3545;
        border-color: rgba(220, 53, 69, 0.2);
    }
    
    .recommendation-box {
        background: linear-gradient(145deg, #f8f9fa, #e9ecef);
        border-radius: 15px;
        padding: 2rem;
        margin: 1.5rem 0;
        border-left: 6px solid #28a745;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Skill database
@st.cache_data
def get_skill_database():
    """Simple skill database"""
    return {
        "Artificial Intelligence": {
            "core_skills": ["Python", "Machine Learning", "Deep Learning", "Statistics", "Data Science"],
            "tools": ["TensorFlow", "PyTorch", "Scikit-learn", "Jupyter", "Git"],
            "soft_skills": ["Problem Solving", "Critical Thinking", "Communication", "Teamwork"],
            "certifications": ["Google AI", "AWS ML", "TensorFlow Developer"],
            "growth_rate": 22,
            "difficulty": "High",
            "salary_range": "$80K-$180K"
        },
        "Blockchain & Web3": {
            "core_skills": ["Solidity", "Smart Contracts", "Ethereum", "Cryptography", "DeFi"],
            "tools": ["Remix", "Hardhat", "Web3.js", "MetaMask", "Git"],
            "soft_skills": ["Security Mindset", "Innovation", "Risk Assessment", "Communication"],
            "certifications": ["Certified Bitcoin Professional", "Ethereum Developer"],
            "growth_rate": 35,
            "difficulty": "Very High",
            "salary_range": "$90K-$200K"
        },
        "Cybersecurity": {
            "core_skills": ["Network Security", "Penetration Testing", "Risk Assessment", "Incident Response"],
            "tools": ["Wireshark", "Metasploit", "Nmap", "Kali Linux", "SIEM"],
            "soft_skills": ["Attention to Detail", "Critical Thinking", "Communication", "Ethics"],
            "certifications": ["CISSP", "CEH", "Security+", "CISM"],
            "growth_rate": 35,
            "difficulty": "High",
            "salary_range": "$75K-$150K"
        },
        "Data Science": {
            "core_skills": ["Python", "R", "SQL", "Statistics", "Machine Learning"],
            "tools": ["Pandas", "NumPy", "Tableau", "Power BI", "Jupyter"],
            "soft_skills": ["Analytical Thinking", "Communication", "Business Acumen", "Curiosity"],
            "certifications": ["Google Data Analytics", "IBM Data Science", "Microsoft Azure Data"],
            "growth_rate": 15,
            "difficulty": "Medium-High",
            "salary_range": "$70K-$140K"
        },
        "Cloud Computing": {
            "core_skills": ["AWS", "Azure", "DevOps", "Kubernetes", "Docker"],
            "tools": ["Terraform", "Ansible", "Jenkins", "Git", "Linux"],
            "soft_skills": ["Problem Solving", "Collaboration", "Continuous Learning", "Innovation"],
            "certifications": ["AWS Solutions Architect", "Azure Solutions Architect", "Google Cloud"],
            "growth_rate": 20,
            "difficulty": "Medium-High",
            "salary_range": "$70K-$160K"
        }
    }

def calculate_skill_match(user_skills, field_skills):
    """Calculate skill match percentage"""
    if not field_skills:
        return 0, [], field_skills
    
    user_skills_lower = [skill.lower().strip() for skill in user_skills if skill]
    field_skills_lower = [skill.lower().strip() for skill in field_skills]
    
    matched = [skill for skill in field_skills if skill.lower() in user_skills_lower]
    missing = [skill for skill in field_skills if skill.lower() not in user_skills_lower]
    
    match_percentage = (len(matched) / len(field_skills)) * 100
    
    return match_percentage, matched, missing

def create_radar_chart(scores, categories):
    """Create radar chart for skill categories"""
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=scores,
        theta=categories,
        fill='toself',
        name='Your Skills',
        line_color='rgb(102, 126, 234)',
        fillcolor='rgba(102, 126, 234, 0.3)'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=[100] * len(categories),
        theta=categories,
        fill='toself',
        name='Target Level',
        line_color='rgb(220, 53, 69)',
        fillcolor='rgba(220, 53, 69, 0.1)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )
        ),
        showlegend=True,
        title="Skill Assessment Overview",
        height=400
    )
    
    return fig

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1 style="margin: 0; font-size: 2.5em; font-weight: 700;">📊 Skill Gap Analysis</h1>
        <p style="font-size: 1.2em; margin: 1rem 0; opacity: 0.9;">
            Discover your strengths and identify areas for growth
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load data
    skill_db = get_skill_database()
    
    # Sidebar
    with st.sidebar:
        st.header("📋 Your Profile")
        
        # Basic info
        current_role = st.text_input("Current Role", placeholder="e.g., Software Developer")
        experience_years = st.slider("Years of Experience", 0, 20, 2)
        
        # Target field
        target_field = st.selectbox("Target Career Field:", list(skill_db.keys()))
        
        # Skills input
        st.subheader("Current Skills")
        user_skills = {}
        
        for category in ['core_skills', 'tools', 'soft_skills', 'certifications']:
            category_name = category.replace('_', ' ').title()
            st.write(f"**{category_name}:**")
            
            field_skills = skill_db[target_field][category]
            selected_skills = []
            
            for skill in field_skills:
                if st.checkbox(skill, key=f"{category}_{skill}"):
                    selected_skills.append(skill)
            
            user_skills[category] = selected_skills
        
        analyze_button = st.button("🔍 Analyze My Skills", type="primary")
    
    # Main content
    if analyze_button:
        # Calculate scores
        category_scores = {}
        category_details = {}
        
        for category in ['core_skills', 'tools', 'soft_skills', 'certifications']:
            user_category_skills = user_skills[category]
            field_category_skills = skill_db[target_field][category]
            
            score, matched, missing = calculate_skill_match(user_category_skills, field_category_skills)
            category_scores[category] = score
            category_details[category] = {'matched': matched, 'missing': missing}
        
        # Overall score (weighted)
        weights = {'core_skills': 0.4, 'tools': 0.3, 'soft_skills': 0.2, 'certifications': 0.1}
        overall_score = sum(category_scores[cat] * weights[cat] for cat in weights.keys())
        
        # Results
        st.header("📈 Analysis Results")
        
        # Metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>🎯 Overall Readiness</h3>
                <p style="font-size: 2em; margin: 0; font-weight: bold;">{overall_score:.1f}%</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            level = "Expert" if overall_score >= 80 else "Advanced" if overall_score >= 60 else "Intermediate" if overall_score >= 40 else "Beginner"
            st.markdown(f"""
            <div class="metric-card">
                <h3>📊 Level</h3>
                <p style="font-size: 1.5em; margin: 0; font-weight: bold;">{level}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            field_data = skill_db[target_field]
            st.markdown(f"""
            <div class="metric-card">
                <h3>📈 Growth Rate</h3>
                <p style="font-size: 1.5em; margin: 0; font-weight: bold;">+{field_data['growth_rate']}%</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="metric-card">
                <h3>💰 Salary Range</h3>
                <p style="font-size: 1.2em; margin: 0; font-weight: bold;">{field_data['salary_range']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Radar chart
        col1, col2 = st.columns([1, 1])
        
        with col1:
            categories = ['Core Skills', 'Tools', 'Soft Skills', 'Certifications']
            scores = [category_scores['core_skills'], category_scores['tools'], 
                     category_scores['soft_skills'], category_scores['certifications']]
            
            radar_fig = create_radar_chart(scores, categories)
            st.plotly_chart(radar_fig, use_container_width=True)
        
        with col2:
            # Progress bars
            st.subheader("📊 Category Breakdown")
            for category, display_name in zip(['core_skills', 'tools', 'soft_skills', 'certifications'], 
                                             ['Core Skills', 'Tools', 'Soft Skills', 'Certifications']):
                score = category_scores[category]
                st.metric(display_name, f"{score:.1f}%")
                st.progress(score / 100)
        
        # Detailed breakdown
        st.header("🔍 Detailed Skill Analysis")
        
        for category, display_name in zip(['core_skills', 'tools', 'soft_skills', 'certifications'], 
                                         ['Core Skills', 'Tools', 'Soft Skills', 'Certifications']):
            with st.expander(f"{display_name} - {category_scores[category]:.1f}% Match"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("✅ Your Skills")
                    matched = category_details[category]['matched']
                    if matched:
                        for skill in matched:
                            st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)
                    else:
                        st.info("No skills in this category yet")
                
                with col2:
                    st.subheader("🎯 Skills to Learn")
                    missing = category_details[category]['missing']
                    if missing:
                        for skill in missing:
                            st.markdown(f'<span class="skill-badge missing">{skill}</span>', unsafe_allow_html=True)
                    else:
                        st.success("All skills covered!")
        
        # Recommendations
        st.header("💡 Recommendations")
        
        if overall_score >= 80:
            st.success("""
            🎉 **Excellent! You're ready for this field.**
            - Start applying for positions
            - Build a portfolio
            - Network with professionals
            - Consider advanced certifications
            """)
        elif overall_score >= 60:
            st.warning("""
            ⚡ **Good foundation! Focus on key gaps.**
            - Complete missing core skills
            - Work on practical projects
            - Join communities
            - Get relevant certifications
            """)
        else:
            st.info("""
            🚀 **Great start! Clear path ahead.**
            - Focus on fundamentals first
            - Take courses or bootcamps
            - Practice with projects
            - Find a mentor
            """)
        
        # Learning resources
        st.header("📚 Learning Resources")
        
        st.markdown(f"""
        <div class="recommendation-box">
            <h4>🎓 Recommended for {target_field}</h4>
            <p><strong>Online Platforms:</strong></p>
            <ul>
                <li>Coursera - Industry certificates</li>
                <li>Udacity - Hands-on nanodegrees</li>
                <li>Pluralsight - Technology skills</li>
                <li>LinkedIn Learning - Professional development</li>
            </ul>
            <p><strong>Top Certifications:</strong> {', '.join(skill_db[target_field]['certifications'])}</p>
        </div>
        """, unsafe_allow_html=True)
    
    else:
        # Initial state
        st.header("🎯 How It Works")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="skill-card">
                <h4>1️⃣ Assessment</h4>
                <p>Select your target field and mark your current skills across different categories.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="skill-card">
                <h4>2️⃣ Analysis</h4>
                <p>Get detailed insights into your readiness level and skill gaps for your target career.</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="skill-card">
                <h4>3️⃣ Roadmap</h4>
                <p>Receive personalized recommendations and learning resources to bridge your gaps.</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.info("👈 **Get started by filling out the sidebar and clicking 'Analyze My Skills'**")
    
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
    
    # Method 2: Try to load universal footer with error handling
    try:
        from utils.footer import render_universal_footer
        # Only render if the simple footer above didn't work
        # render_universal_footer()
    except ImportError:
        pass
    except Exception as e:
        st.error(f"Footer loading error: {e}")

if __name__ == "__main__":
    main()