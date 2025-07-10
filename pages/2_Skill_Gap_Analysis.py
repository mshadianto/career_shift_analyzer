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

# Simplified CSS for better performance
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Exo+2:wght@300;400;600&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a0e2e 50%, #0a0a0a 100%);
        color: #e0e0ff;
    }
    
    .main-header {
        text-align: center;
        padding: 2rem;
        background: linear-gradient(135deg, rgba(139, 69, 255, 0.2), rgba(255, 69, 255, 0.2));
        border: 2px solid #8b45ff;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 0 20px rgba(139, 69, 255, 0.3);
    }
    
    .main-header h1 {
        font-family: 'Orbitron', monospace;
        color: #ff45ff;
        text-shadow: 0 0 10px #8b45ff;
        margin: 0;
    }
    
    .skill-card {
        background: linear-gradient(145deg, rgba(13, 13, 13, 0.9), rgba(26, 14, 46, 0.9));
        border: 1px solid #8b45ff;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 0 15px rgba(139, 69, 255, 0.2);
    }
    
    .metric-card {
        background: linear-gradient(135deg, rgba(139, 69, 255, 0.2), rgba(255, 69, 255, 0.2));
        border: 1px solid #8b45ff;
        border-radius: 10px;
        padding: 1.5rem;
        text-align: center;
        margin: 0.5rem;
        box-shadow: 0 0 15px rgba(139, 69, 255, 0.3);
    }
    
    .skill-badge {
        display: inline-block;
        background: rgba(139, 69, 255, 0.2);
        color: #8b45ff;
        padding: 0.3rem 0.8rem;
        border-radius: 15px;
        margin: 0.2rem;
        font-size: 0.9em;
        border: 1px solid rgba(139, 69, 255, 0.3);
    }
    
    .skill-badge.missing {
        background: rgba(255, 69, 69, 0.2);
        color: #ff4545;
        border-color: rgba(255, 69, 69, 0.3);
    }
    
    .recommendation-box {
        background: linear-gradient(145deg, rgba(0, 255, 136, 0.1), rgba(0, 200, 100, 0.1));
        border: 1px solid rgba(0, 255, 136, 0.3);
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #00ff88;
    }
    
    h1, h2, h3, h4 {
        font-family: 'Orbitron', monospace;
        color: #e0e0ff;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #8b45ff, #ff45ff);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)

# Skill database
@st.cache_data
def get_skill_database():
    return {
        "Artificial Intelligence": {
            "core_skills": ["Python", "Machine Learning", "Deep Learning", "Statistics", "Data Science", "Neural Networks"],
            "tools": ["TensorFlow", "PyTorch", "Scikit-learn", "Jupyter", "Git", "Docker"],
            "soft_skills": ["Problem Solving", "Critical Thinking", "Communication", "Research"],
            "certifications": ["Google AI", "AWS ML", "TensorFlow Developer", "Azure AI"],
            "growth_rate": 22,
            "difficulty": "High",
            "salary_range": "$80K-$180K"
        },
        "Blockchain & Web3": {
            "core_skills": ["Solidity", "Smart Contracts", "Ethereum", "Cryptography", "DeFi", "Web3"],
            "tools": ["Remix", "Hardhat", "Web3.js", "MetaMask", "Git", "Truffle"],
            "soft_skills": ["Security Mindset", "Innovation", "Risk Assessment", "Communication"],
            "certifications": ["Certified Bitcoin Professional", "Ethereum Developer", "Blockchain Council"],
            "growth_rate": 35,
            "difficulty": "Very High",
            "salary_range": "$90K-$200K"
        },
        "Cybersecurity": {
            "core_skills": ["Network Security", "Penetration Testing", "Risk Assessment", "Incident Response", "SIEM"],
            "tools": ["Wireshark", "Metasploit", "Nmap", "Kali Linux", "Burp Suite"],
            "soft_skills": ["Attention to Detail", "Critical Thinking", "Communication", "Ethics"],
            "certifications": ["CISSP", "CEH", "Security+", "CISM", "OSCP"],
            "growth_rate": 35,
            "difficulty": "High",
            "salary_range": "$75K-$150K"
        },
        "Data Science": {
            "core_skills": ["Python", "R", "SQL", "Statistics", "Machine Learning", "Data Analysis"],
            "tools": ["Pandas", "NumPy", "Tableau", "Power BI", "Jupyter", "Apache Spark"],
            "soft_skills": ["Analytical Thinking", "Communication", "Business Acumen", "Curiosity"],
            "certifications": ["Google Data Analytics", "IBM Data Science", "Microsoft Azure Data"],
            "growth_rate": 15,
            "difficulty": "Medium-High",
            "salary_range": "$70K-$140K"
        },
        "Cloud Computing": {
            "core_skills": ["AWS", "Azure", "DevOps", "Kubernetes", "Docker", "Infrastructure as Code"],
            "tools": ["Terraform", "Ansible", "Jenkins", "Git", "Linux", "Prometheus"],
            "soft_skills": ["Problem Solving", "Collaboration", "Continuous Learning", "Innovation"],
            "certifications": ["AWS Solutions Architect", "Azure Solutions Architect", "Google Cloud"],
            "growth_rate": 20,
            "difficulty": "Medium-High",
            "salary_range": "$70K-$160K"
        }
    }

def calculate_skill_match(user_skills, field_skills):
    if not field_skills:
        return 0, [], field_skills
    
    user_skills_lower = [skill.lower().strip() for skill in user_skills if skill]
    field_skills_lower = [skill.lower().strip() for skill in field_skills]
    
    matched = [skill for skill in field_skills if skill.lower() in user_skills_lower]
    missing = [skill for skill in field_skills if skill.lower() not in user_skills_lower]
    
    match_percentage = (len(matched) / len(field_skills)) * 100
    return match_percentage, matched, missing

def create_radar_chart(scores, categories):
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=scores,
        theta=categories,
        fill='toself',
        name='Your Skills',
        line_color='rgb(139, 69, 255)',
        fillcolor='rgba(139, 69, 255, 0.3)'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=[100] * len(categories),
        theta=categories,
        fill='toself',
        name='Target Level',
        line_color='rgb(255, 69, 255)',
        fillcolor='rgba(255, 69, 255, 0.1)'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], gridcolor='rgba(139, 69, 255, 0.2)'),
            angularaxis=dict(gridcolor='rgba(139, 69, 255, 0.2)')
        ),
        showlegend=True,
        title="🎯 Skill Assessment Overview",
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e0ff')
    )
    
    return fig

def create_skill_progress_chart(category_scores):
    categories = list(category_scores.keys())
    scores = list(category_scores.values())
    
    display_names = {
        'core_skills': 'Core Skills',
        'tools': 'Tools & Frameworks',
        'soft_skills': 'Soft Skills',
        'certifications': 'Certifications'
    }
    
    display_categories = [display_names.get(cat, cat) for cat in categories]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        y=display_categories,
        x=scores,
        orientation='h',
        marker=dict(
            color=scores,
            colorscale=[[0, '#ff4545'], [0.5, '#ffaa00'], [1, '#00ff88']],
            showscale=True
        ),
        text=[f"{score:.1f}%" for score in scores],
        textposition='auto'
    ))
    
    fig.update_layout(
        title='📊 Skill Category Breakdown',
        xaxis_title='Proficiency Percentage',
        height=350,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e0ff'),
        xaxis=dict(range=[0, 100])
    )
    
    return fig

def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>📊 SKILL GAP ANALYSIS</h1>
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
        
        st.markdown("---")
        
        # Additional assessments
        st.subheader("🎯 Self Assessment")
        coding_experience = st.selectbox("Coding Experience", ["Beginner", "Intermediate", "Advanced", "Expert"])
        learning_time = st.slider("Weekly Learning Time (hours)", 0, 40, 10)
        career_urgency = st.selectbox("Career Change Urgency", ["No Rush", "6-12 months", "3-6 months", "ASAP"])
        
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
        
        # Experience bonus
        exp_bonus = min(experience_years * 2, 20)
        adjusted_score = min(overall_score + exp_bonus, 100)
        
        # Results
        st.header("📈 Analysis Results")
        
        # Metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class="metric-card">
                <h3>🎯 Overall Readiness</h3>
                <p style="font-size: 2em; margin: 0; font-weight: bold; color: #00ff88;">{adjusted_score:.1f}%</p>
                <p style="margin: 0;">Career Ready Score</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            level = "Expert" if adjusted_score >= 80 else "Advanced" if adjusted_score >= 60 else "Intermediate" if adjusted_score >= 40 else "Beginner"
            level_color = "#00ff88" if level == "Expert" else "#ffaa00" if level == "Advanced" else "#ff8800" if level == "Intermediate" else "#ff4545"
            st.markdown(f"""
            <div class="metric-card">
                <h3>📊 Level</h3>
                <p style="font-size: 1.5em; margin: 0; font-weight: bold; color: {level_color};">{level}</p>
                <p style="margin: 0;">Proficiency Level</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            field_data = skill_db[target_field]
            st.markdown(f"""
            <div class="metric-card">
                <h3>📈 Growth Rate</h3>
                <p style="font-size: 1.5em; margin: 0; font-weight: bold; color: #00ff88;">+{field_data['growth_rate']}%</p>
                <p style="margin: 0;">Industry Growth</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class="metric-card">
                <h3>💰 Salary Range</h3>
                <p style="font-size: 1.2em; margin: 0; font-weight: bold; color: #ffaa00;">{field_data['salary_range']}</p>
                <p style="margin: 0;">Expected Range</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Visualizations
        col1, col2 = st.columns([1, 1])
        
        with col1:
            categories = ['Core Skills', 'Tools', 'Soft Skills', 'Certifications']
            scores = [category_scores['core_skills'], category_scores['tools'], 
                     category_scores['soft_skills'], category_scores['certifications']]
            
            radar_fig = create_radar_chart(scores, categories)
            st.plotly_chart(radar_fig, use_container_width=True)
        
        with col2:
            progress_fig = create_skill_progress_chart(category_scores)
            st.plotly_chart(progress_fig, use_container_width=True)
        
        # Detailed breakdown
        st.header("🔍 Detailed Skill Analysis")
        
        for category, display_name in zip(['core_skills', 'tools', 'soft_skills', 'certifications'], 
                                         ['Core Skills', 'Tools & Frameworks', 'Soft Skills', 'Certifications']):
            with st.expander(f"{display_name} - {category_scores[category]:.1f}% Match", expanded=False):
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
        st.header("💡 Personalized Recommendations")
        
        if adjusted_score >= 80:
            st.success("""
            ### 🎉 Excellent! You're ready for this field.
            **Immediate Actions:**
            - Start applying for positions in your target field
            - Build an impressive portfolio showcasing your skills
            - Network with professionals and attend industry events
            - Consider advanced certifications to stand out
            """)
        elif adjusted_score >= 60:
            st.warning("""
            ### ⚡ Good foundation! Focus on key gaps.
            **Priority Actions:**
            - Complete missing core skills through targeted learning
            - Work on 2-3 hands-on projects to demonstrate abilities
            - Join professional communities and online forums
            - Get at least one relevant certification
            """)
        else:
            st.info("""
            ### 🚀 Great start! Clear path ahead.
            **Foundation Building:**
            - Focus on fundamental skills first - don't rush
            - Take structured courses or consider a bootcamp
            - Practice with small projects and build gradually
            - Find a mentor or study group for guidance
            """)
        
        # Career timeline
        st.header("⏰ Career Transition Timeline")
        
        time_factors = {"No Rush": 1.5, "6-12 months": 1.0, "3-6 months": 0.7, "ASAP": 0.5}
        base_months = max(3, (100 - adjusted_score) / 10)
        urgency_factor = time_factors[career_urgency]
        learning_factor = min(learning_time / 15, 1.5)
        estimated_months = max(2, base_months * urgency_factor / learning_factor)
        
        timeline_html = f"""
        <div class="recommendation-box">
            <h4 style="color: #00ff88; margin-bottom: 1rem;">🗓️ Estimated Timeline: {estimated_months:.0f} months</h4>
            <p><strong>Based on:</strong></p>
            <ul>
                <li>Current readiness: {adjusted_score:.1f}%</li>
                <li>Learning commitment: {learning_time} hours/week</li>
                <li>Target urgency: {career_urgency}</li>
                <li>Experience level: {experience_years} years</li>
            </ul>
            <p><strong>💡 Pro Tip:</strong> Increase your weekly learning time to accelerate your timeline!</p>
        </div>
        """
        st.markdown(timeline_html, unsafe_allow_html=True)
        
        # Learning resources
        st.header("📚 Recommended Learning Resources")
        
        learning_resources = {
            "Artificial Intelligence": {
                "courses": ["CS229 Machine Learning (Stanford)", "Deep Learning Specialization (Coursera)", "Fast.ai"],
                "books": ["Hands-On Machine Learning", "Pattern Recognition and ML", "Deep Learning (Goodfellow)"],
                "practice": ["Kaggle Competitions", "Google Colab Projects", "OpenAI Gym"]
            },
            "Blockchain & Web3": {
                "courses": ["Ethereum and Solidity (Udemy)", "Blockchain Specialization (Coursera)", "CryptoZombies"],
                "books": ["Mastering Ethereum", "Blockchain Basics", "Programming Bitcoin"],
                "practice": ["Build DApps", "Contribute to DeFi protocols", "Smart contract audits"]
            },
            "Cybersecurity": {
                "courses": ["CISSP Training", "Ethical Hacking (EC-Council)", "Security+ (CompTIA)"],
                "books": ["Web Application Hacker's Handbook", "Network Security Essentials", "CISSP Study Guide"],
                "practice": ["HackTheBox", "TryHackMe", "OWASP WebGoat"]
            },
            "Data Science": {
                "courses": ["Data Science Specialization (Johns Hopkins)", "Python for Data Science", "Applied Data Science"],
                "books": ["Python for Data Analysis", "Elements of Statistical Learning", "Storytelling with Data"],
                "practice": ["Kaggle", "DataCamp Projects", "GitHub Portfolio"]
            },
            "Cloud Computing": {
                "courses": ["AWS Solutions Architect", "Azure Fundamentals", "Google Cloud Professional"],
                "books": ["AWS Certified Solutions Architect", "Azure for Architects", "GCP in Action"],
                "practice": ["AWS Free Tier", "Azure DevOps", "Kubernetes clusters"]
            }
        }
        
        resources = learning_resources.get(target_field, {})
        
        if resources:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown(f"""
                <div class="skill-card">
                    <h4 style="color: #ff45ff;">📖 Top Courses</h4>
                    <ul>
                        {''.join([f'<li>{course}</li>' for course in resources.get('courses', [])])}
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="skill-card">
                    <h4 style="color: #ff45ff;">📚 Essential Books</h4>
                    <ul>
                        {''.join([f'<li>{book}</li>' for book in resources.get('books', [])])}
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                <div class="skill-card">
                    <h4 style="color: #ff45ff;">🛠️ Practice Platforms</h4>
                    <ul>
                        {''.join([f'<li>{platform}</li>' for platform in resources.get('practice', [])])}
                    </ul>
                </div>
                """, unsafe_allow_html=True)
        
        # Next steps
        st.header("🚀 Next Steps")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("🎮 Career Simulation", use_container_width=True):
                st.switch_page("pages/1_Career_Simulation.py")
        
        with col2:
            if st.button("💬 AI Career Assistant", use_container_width=True):
                st.switch_page("pages/3_Career_Chat_Assistant.py")
        
        with col3:
            if st.button("🏠 Back to Home", use_container_width=True):
                st.switch_page("main.py")

if __name__ == "__main__":
    main()
