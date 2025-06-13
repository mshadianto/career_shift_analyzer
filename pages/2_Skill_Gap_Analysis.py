import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Skill Gap Analysis", layout="wide")
st.title("📊 Skill Gap Analysis")
st.markdown("""
Bandingkan skill yang Anda miliki dengan skill yang dibutuhkan di industri masa depan.
Dapatkan analisis mendalam dan roadmap pembelajaran yang personal! 🎯
""")

# Enhanced skill mapping with more details
skill_targets = {
    "Artificial Intelligence": {
        "technical": ["python", "tensorflow", "pytorch", "machine learning", "deep learning", "sql", "statistics"],
        "soft": ["problem solving", "critical thinking", "research"],
        "tools": ["jupyter", "git", "docker", "aws", "google cloud"],
        "salary_range": "$80,000 - $180,000",
        "growth_rate": "22% (Much faster than average)"
    },
    "Blockchain & Web3": {
        "technical": ["solidity", "smart contracts", "cryptography", "defi", "nft", "ethereum", "javascript"],
        "soft": ["attention to detail", "security mindset", "innovation"],
        "tools": ["remix", "truffle", "metamask", "hardhat"],
        "salary_range": "$90,000 - $200,000",
        "growth_rate": "35% (Extremely fast growth)"
    },
    "Renewable Energy": {
        "technical": ["solar technology", "wind energy", "energy storage", "electrical engineering", "sustainability"],
        "soft": ["environmental awareness", "project management", "collaboration"],
        "tools": ["autocad", "matlab", "pvsyst", "homer"],
        "salary_range": "$65,000 - $120,000",
        "growth_rate": "8% (Much faster than average)"
    },
    "Biotechnology": {
        "technical": ["bioinformatics", "genetics", "molecular biology", "lab techniques", "data analysis"],
        "soft": ["attention to detail", "patience", "scientific method"],
        "tools": ["r", "python", "blast", "laboratory equipment"],
        "salary_range": "$70,000 - $140,000",
        "growth_rate": "7% (Faster than average)"
    },
    "Space Technology": {
        "technical": ["aerospace engineering", "physics", "mathematics", "navigation", "satellite technology"],
        "soft": ["precision", "teamwork", "problem solving"],
        "tools": ["matlab", "simulink", "cad software", "mission planning"],
        "salary_range": "$85,000 - $160,000",
        "growth_rate": "6% (As fast as average, but high impact)"
    },
    "Cybersecurity": {
        "technical": ["network security", "penetration testing", "incident response", "risk assessment", "compliance"],
        "soft": ["analytical thinking", "continuous learning", "communication"],
        "tools": ["wireshark", "metasploit", "nmap", "burp suite"],
        "salary_range": "$75,000 - $150,000",
        "growth_rate": "35% (Much faster than average)"
    }
}

# Sidebar for field selection
st.sidebar.header("🎯 Pilih Bidang Karir")
selected_field = st.sidebar.selectbox(
    "Industri masa depan:",
    list(skill_targets.keys()),
    help="Pilih bidang yang ingin Anda analisis"
)

# Display field info
field_data = skill_targets[selected_field]
st.sidebar.markdown(f"""
### 📈 Info Industri
**💰 Salary Range:** {field_data['salary_range']}  
**📊 Growth Rate:** {field_data['growth_rate']}
""")

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader(f"🔍 Analisis untuk {selected_field}")
    
    # Skill input
    skills_user = st.text_area(
        "Masukkan skill yang Anda miliki (pisahkan dengan koma):",
        placeholder="Contoh: python, teamwork, excel, problem solving, git",
        help="Tulis semua skill Anda, baik technical maupun soft skills"
    )

with col2:
    st.subheader("💡 Tips Input")
    st.info("""
    **Include both:**
    - Technical skills (programming, tools)
    - Soft skills (communication, leadership)
    - Tools & platforms you've used
    """)

if st.button("🔎 Lihat Analisis Skill Gap", type="primary"):
    if skills_user.strip():
        user_skills = [s.strip().lower() for s in skills_user.split(",")]
        
        # Combine all required skills
        all_required = field_data["technical"] + field_data["soft"] + field_data["tools"]
        
        # Calculate matches
        technical_match = [s for s in user_skills if s in [skill.lower() for skill in field_data["technical"]]]
        soft_match = [s for s in user_skills if s in [skill.lower() for skill in field_data["soft"]]]
        tools_match = [s in user_skills if s in [skill.lower() for skill in field_data["tools"]]]
        
        # Calculate gaps
        technical_gap = [s for s in field_data["technical"] if s.lower() not in [skill.lower() for skill in user_skills]]
        soft_gap = [s for s in field_data["soft"] if s.lower() not in [skill.lower() for skill in user_skills]]
        tools_gap = [s for s in field_data["tools"] if s.lower() not in [skill.lower() for skill in user_skills]]
        
        # Overall score
        total_required = len(all_required)
        total_matched = len(technical_match) + len(soft_match) + len(tools_match)
        skill_percentage = (total_matched / total_required * 100) if total_required > 0 else 0
        
        # Results section
        st.markdown("---")
        st.subheader("📊 Hasil Analisis")
        
        # Score display
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("📈 Overall Score", f"{skill_percentage:.1f}%")
        with col2:
            st.metric("✅ Skills Matched", f"{total_matched}/{total_required}")
        with col3:
            st.metric("🔧 Technical Skills", f"{len(technical_match)}/{len(field_data['technical'])}")
        with col4:
            st.metric("🤝 Soft Skills", f"{len(soft_match)}/{len(field_data['soft'])}")
        
        # Progress bar
        st.progress(skill_percentage / 100)
        
        # Detailed breakdown
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("✅ Skills yang Sudah Dimiliki")
            if technical_match:
                st.success("**🔧 Technical Skills:**")
                for skill in technical_match:
                    st.write(f"• {skill.title()}")
            
            if soft_match:
                st.success("**🤝 Soft Skills:**")
                for skill in soft_match:
                    st.write(f"• {skill.title()}")
            
            if tools_match:
                st.success("**🛠️ Tools:**")
                for skill in tools_match:
                    st.write(f"• {skill.title()}")
        
        with col2:
            st.subheader("❌ Skills yang Perlu Dipelajari")
            if technical_gap:
                st.error("**🔧 Technical Skills:**")
                for skill in technical_gap:
                    st.write(f"• {skill.title()}")
            
            if soft_gap:
                st.error("**🤝 Soft Skills:**")
                for skill in soft_gap:
                    st.write(f"• {skill.title()}")
            
            if tools_gap:
                st.error("**🛠️ Tools:**")
                for skill in tools_gap:
                    st.write(f"• {skill.title()}")
        
        # Radar chart
        if total_required > 0:
            st.subheader("🎯 Skill Radar Chart")
            
            categories = ['Technical', 'Soft Skills', 'Tools']
            current_scores = [
                len(technical_match) / len(field_data["technical"]) * 100 if field_data["technical"] else 0,
                len(soft_match) / len(field_data["soft"]) * 100 if field_data["soft"] else 0,
                len(tools_match) / len(field_data["tools"]) * 100 if field_data["tools"] else 0
            ]
            target_scores = [100, 100, 100]
            
            fig = go.Figure()
            
            fig.add_trace(go.Scatterpolar(
                r=current_scores,
                theta=categories,
                fill='toself',
                name='Current Level',
                line_color='rgb(0, 123, 255)'
            ))
            
            fig.add_trace(go.Scatterpolar(
                r=target_scores,
                theta=categories,
                fill='toself',
                name='Target Level',
                line_color='rgb(255, 99, 132)',
                opacity=0.3
            ))
            
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(
                        visible=True,
                        range=[0, 100]
                    )),
                showlegend=True,
                title="Skill Level Comparison"
            )
            
            st.plotly_chart(fig, use_container_width=True)
        
        # Learning recommendations
        st.subheader("🎓 Rekomendasi Learning Path")
        
        priority_skills = technical_gap[:3] + soft_gap[:2] + tools_gap[:2]
        
        if priority_skills:
            st.info("**🚀 Priority Skills to Learn (Top recommendations):**")
            
            learning_resources = {
                "python": "https://www.codecademy.com/learn/learn-python-3",
                "machine learning": "https://www.coursera.org/learn/machine-learning",
                "javascript": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/",
                "solidity": "https://cryptozombies.io/",
                "problem solving": "https://www.coursera.org/learn/creative-problem-solving",
                "git": "https://learngitbranching.js.org/"
            }
            
            for i, skill in enumerate(priority_skills[:5], 1):
                resource_url = learning_resources.get(skill.lower(), f"https://www.coursera.org/search?query={skill}")
                st.markdown(f"**{i}. {skill.title()}** → [📚 Learn Here]({resource_url})")
        else:
            st.success("🎉 Congratulations! You have all the essential skills for this field!")
            st.balloons()
    
    else:
        st.warning("⚠️ Please enter your skills to get analysis.")

st.markdown("---")
st.caption("© 2025 Career Shift Analyzer | Data based on industry research and job market trends")