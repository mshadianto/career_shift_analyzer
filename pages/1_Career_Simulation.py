import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import random

# Page config
st.set_page_config(
    page_title="Career Simulation",
    page_icon="🎮",
    layout="wide"
)

# Enhanced Custom CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    .simulation-header {
        text-align: center;
        padding: 3rem 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        color: white;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 20px 40px rgba(102, 126, 234, 0.3);
        position: relative;
        overflow: hidden;
    }
    
    .simulation-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.1), transparent);
        animation: shine 3s infinite;
    }
    
    @keyframes shine {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    
    .simulation-card {
        background: linear-gradient(145deg, #ffffff, #f8f9ff);
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin: 1rem 0;
        border-left: 5px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .simulation-card:hover {
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
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 25px 50px rgba(102, 126, 234, 0.4);
    }
    
    .path-step {
        background: rgba(102, 126, 234, 0.1);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #667eea;
        transition: all 0.3s ease;
    }
    
    .path-step:hover {
        background: rgba(102, 126, 234, 0.15);
        transform: translateX(10px);
    }
    
    .progress-container {
        background: #f0f2f6;
        border-radius: 10px;
        padding: 0.3rem;
        margin: 0.5rem 0;
    }
    
    .progress-bar {
        background: linear-gradient(90deg, #667eea, #764ba2);
        height: 20px;
        border-radius: 8px;
        transition: width 0.8s ease-in-out;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 600;
        font-size: 0.8em;
    }
    
    .scenario-option {
        background: #f8f9ff;
        border: 2px solid rgba(102, 126, 234, 0.2);
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .scenario-option:hover {
        border-color: #667eea;
        background: rgba(102, 126, 234, 0.05);
        transform: scale(1.02);
    }
    
    .scenario-option.selected {
        border-color: #667eea;
        background: rgba(102, 126, 234, 0.1);
    }
    
    .timeline-item {
        border-left: 3px solid #667eea;
        padding-left: 1.5rem;
        margin: 1rem 0;
        position: relative;
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -8px;
        top: 0.5rem;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        background: #667eea;
    }
    
    .warning-box {
        background: rgba(255, 193, 7, 0.1);
        border: 1px solid rgba(255, 193, 7, 0.3);
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        color: #856404;
    }
    
    .success-box {
        background: rgba(40, 167, 69, 0.1);
        border: 1px solid rgba(40, 167, 69, 0.3);
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        color: #155724;
    }
</style>
""", unsafe_allow_html=True)

# Career simulation data
@st.cache_data
def get_simulation_data():
    """Get career simulation scenarios and data"""
    return {
        "scenarios": {
            "AI Transition": {
                "description": "Transition from traditional role to AI/ML Engineer",
                "duration": "8-12 months",
                "difficulty": "High",
                "investment": "$2,000-$5,000",
                "success_rate": 75,
                "steps": [
                    {"month": 1, "activity": "Python Fundamentals", "cost": 500, "time_hours": 80},
                    {"month": 2, "activity": "Statistics & Math", "cost": 300, "time_hours": 60},
                    {"month": 3, "activity": "Machine Learning Basics", "cost": 600, "time_hours": 100},
                    {"month": 4, "activity": "Deep Learning Course", "cost": 800, "time_hours": 120},
                    {"month": 5, "activity": "Portfolio Projects", "cost": 200, "time_hours": 80},
                    {"month": 6, "activity": "Advanced Projects", "cost": 300, "time_hours": 100},
                    {"month": 7, "activity": "Job Applications", "cost": 100, "time_hours": 40},
                    {"month": 8, "activity": "Interview Preparation", "cost": 200, "time_hours": 60}
                ],
                "salary_progression": [50000, 52000, 55000, 60000, 70000, 85000, 95000, 110000],
                "skills_gained": ["Python", "Machine Learning", "Data Science", "TensorFlow", "Statistics"]
            },
            "Blockchain Developer": {
                "description": "Become a Blockchain/Web3 Developer",
                "duration": "6-10 months",
                "difficulty": "Very High",
                "investment": "$3,000-$7,000",
                "success_rate": 65,
                "steps": [
                    {"month": 1, "activity": "JavaScript/Node.js", "cost": 400, "time_hours": 80},
                    {"month": 2, "activity": "Blockchain Fundamentals", "cost": 600, "time_hours": 100},
                    {"month": 3, "activity": "Solidity Programming", "cost": 800, "time_hours": 120},
                    {"month": 4, "activity": "Smart Contract Development", "cost": 1000, "time_hours": 140},
                    {"month": 5, "activity": "DeFi Protocols", "cost": 700, "time_hours": 100},
                    {"month": 6, "activity": "Portfolio & Projects", "cost": 500, "time_hours": 120},
                    {"month": 7, "activity": "Network & Job Search", "cost": 200, "time_hours": 60}
                ],
                "salary_progression": [55000, 58000, 65000, 75000, 90000, 110000, 130000],
                "skills_gained": ["Solidity", "Web3.js", "Smart Contracts", "DeFi", "Ethereum"]
            },
            "Cybersecurity Analyst": {
                "description": "Enter Cybersecurity field",
                "duration": "6-9 months",
                "difficulty": "Medium-High",
                "investment": "$1,500-$4,000",
                "success_rate": 80,
                "steps": [
                    {"month": 1, "activity": "Security Fundamentals", "cost": 400, "time_hours": 60},
                    {"month": 2, "activity": "Network Security", "cost": 500, "time_hours": 80},
                    {"month": 3, "activity": "Ethical Hacking Course", "cost": 800, "time_hours": 100},
                    {"month": 4, "activity": "Security Tools Training", "cost": 600, "time_hours": 80},
                    {"month": 5, "activity": "Certification Prep", "cost": 400, "time_hours": 60},
                    {"month": 6, "activity": "Hands-on Labs", "cost": 300, "time_hours": 80},
                    {"month": 7, "activity": "Job Search & Applications", "cost": 100, "time_hours": 40}
                ],
                "salary_progression": [45000, 48000, 52000, 58000, 68000, 78000, 88000],
                "skills_gained": ["Network Security", "Penetration Testing", "SIEM", "Risk Assessment", "Incident Response"]
            },
            "Data Scientist": {
                "description": "Transition to Data Science role",
                "duration": "7-10 months",
                "difficulty": "Medium-High",
                "investment": "$2,500-$6,000",
                "success_rate": 70,
                "steps": [
                    {"month": 1, "activity": "Python & R Basics", "cost": 500, "time_hours": 80},
                    {"month": 2, "activity": "Statistics & Probability", "cost": 400, "time_hours": 80},
                    {"month": 3, "activity": "Data Analysis & Pandas", "cost": 600, "time_hours": 100},
                    {"month": 4, "activity": "Machine Learning", "cost": 700, "time_hours": 120},
                    {"month": 5, "activity": "Data Visualization", "cost": 500, "time_hours": 80},
                    {"month": 6, "activity": "SQL & Databases", "cost": 300, "time_hours": 60},
                    {"month": 7, "activity": "Portfolio Projects", "cost": 400, "time_hours": 100},
                    {"month": 8, "activity": "Job Applications", "cost": 100, "time_hours": 40}
                ],
                "salary_progression": [48000, 50000, 55000, 62000, 72000, 85000, 95000, 105000],
                "skills_gained": ["Python", "R", "SQL", "Machine Learning", "Data Visualization", "Statistics"]
            }
        }
    }

def simulate_career_path(scenario_data, user_params):
    """Simulate career path with user parameters"""
    # Adjust based on user parameters
    time_multiplier = user_params.get('time_commitment', 1.0)
    budget_multiplier = user_params.get('budget_factor', 1.0)
    experience_bonus = user_params.get('experience_level', 0)
    
    adjusted_scenario = scenario_data.copy()
    
    # Adjust timeline based on time commitment
    if time_multiplier < 0.5:  # Part-time
        for step in adjusted_scenario['steps']:
            step['month'] = int(step['month'] * 1.5)
    elif time_multiplier > 1.5:  # Intensive
        for step in adjusted_scenario['steps']:
            step['month'] = max(1, int(step['month'] * 0.7))
    
    # Adjust success rate based on experience
    base_success_rate = adjusted_scenario['success_rate']
    adjusted_scenario['success_rate'] = min(95, base_success_rate + experience_bonus * 10)
    
    return adjusted_scenario

def create_timeline_chart(scenario_data):
    """Create interactive timeline chart"""
    steps = scenario_data['steps']
    
    fig = go.Figure()
    
    # Add timeline bars
    fig.add_trace(go.Bar(
        x=[step['month'] for step in steps],
        y=[step['time_hours'] for step in steps],
        text=[step['activity'] for step in steps],
        textposition='auto',
        name='Learning Hours',
        marker_color='rgba(102, 126, 234, 0.7)',
        hovertemplate='<b>%{text}</b><br>Month: %{x}<br>Hours: %{y}<extra></extra>'
    ))
    
    fig.update_layout(
        title='Learning Timeline & Time Investment',
        xaxis_title='Month',
        yaxis_title='Hours Required',
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig

def create_cost_breakdown_chart(scenario_data):
    """Create cost breakdown chart"""
    steps = scenario_data['steps']
    
    activities = [step['activity'] for step in steps]
    costs = [step['cost'] for step in steps]
    
    fig = go.Figure(data=[go.Pie(
        labels=activities,
        values=costs,
        hole=0.4,
        hovertemplate='<b>%{label}</b><br>Cost: $%{value}<br>Percentage: %{percent}<extra></extra>'
    )])
    
    fig.update_layout(
        title='Cost Breakdown by Activity',
        height=400,
        annotations=[dict(text='Total Cost', x=0.5, y=0.5, font_size=16, showarrow=False)]
    )
    
    return fig

def create_salary_projection_chart(scenario_data):
    """Create salary projection chart"""
    months = list(range(len(scenario_data['salary_progression'])))
    salaries = scenario_data['salary_progression']
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=months,
        y=salaries,
        mode='lines+markers',
        name='Projected Salary',
        line=dict(color='#667eea', width=3),
        marker=dict(size=8),
        hovertemplate='Month: %{x}<br>Salary: $%{y:,.0f}<extra></extra>'
    ))
    
    fig.update_layout(
        title='Salary Progression Projection',
        xaxis_title='Month',
        yaxis_title='Annual Salary ($)',
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig

def main():
    """Main career simulation function"""
    
    # Header
    st.markdown("""
    <div class="simulation-header">
        <h1 style="margin: 0; font-size: 2.5em; font-weight: 700;">🎮 Career Simulation</h1>
        <p style="font-size: 1.2em; margin: 1rem 0; opacity: 0.9;">
            Interactive Career Path Planning & Outcome Modeling
        </p>
        <p style="font-size: 1em; margin: 0; opacity: 0.8;">
            Simulate different career transitions with realistic timelines, costs, and outcomes
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load simulation data
    sim_data = get_simulation_data()
    
    # Sidebar for simulation parameters
    with st.sidebar:
        st.header("🎯 Simulation Parameters")
        
        # Basic parameters
        st.subheader("Personal Profile")
        current_salary = st.number_input("Current Annual Salary ($)", min_value=30000, max_value=200000, value=50000, step=5000)
        experience_level = st.selectbox("Experience Level", ["Entry Level (0-2 years)", "Mid Level (2-5 years)", "Senior Level (5+ years)"])
        location = st.selectbox("Location", ["San Francisco, CA", "New York, NY", "Austin, TX", "Seattle, WA", "Remote", "Other"])
        
        # Learning preferences
        st.subheader("Learning Preferences")
        time_commitment = st.radio(
            "Time Commitment",
            ["Part-time (10-15 hrs/week)", "Standard (20-25 hrs/week)", "Intensive (30+ hrs/week)"]
        )
        
        budget_limit = st.slider("Learning Budget ($)", min_value=1000, max_value=10000, value=3000, step=500)
        
        # Risk tolerance
        st.subheader("Risk Assessment")
        risk_tolerance = st.selectbox("Risk Tolerance", ["Conservative", "Moderate", "Aggressive"])
        family_situation = st.radio("Family Situation", ["Single", "Married/No Kids", "Married/With Kids"])
        
        st.markdown("---")
        st.info("""
        **💡 Simulation Features:**
        - Realistic timeline projections
        - Cost-benefit analysis
        - Success probability modeling
        - Market-based salary data
        - Personalized recommendations
        """)
    
    # Main simulation interface
    st.header("🚀 Choose Your Career Path")
    
    # Scenario selection
    col1, col2 = st.columns([2, 1])
    
    with col1:
        scenario_names = list(sim_data["scenarios"].keys())
        selected_scenario = st.selectbox("Select Career Transition Scenario:", scenario_names)
        
        scenario_data = sim_data["scenarios"][selected_scenario]
        
        scenario_card_html = f"""
        <div class="simulation-card">
            <h3 style="color: #667eea; margin-bottom: 1rem;">{selected_scenario}</h3>
            <p style="margin-bottom: 1rem;">{scenario_data['description']}</p>
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem;">
                <div>
                    <strong>Duration:</strong> {scenario_data['duration']}<br>
                    <strong>Difficulty:</strong> {scenario_data['difficulty']}<br>
                </div>
                <div>
                    <strong>Investment:</strong> {scenario_data['investment']}<br>
                    <strong>Success Rate:</strong> {scenario_data['success_rate']}%
                </div>
            </div>
        </div>
        """
        st.markdown(scenario_card_html, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🎯 Quick Stats")
        
        # Convert experience level to numeric
        exp_mapping = {"Entry Level (0-2 years)": 0, "Mid Level (2-5 years)": 1, "Senior Level (5+ years)": 2}
        time_mapping = {"Part-time (10-15 hrs/week)": 0.5, "Standard (20-25 hrs/week)": 1.0, "Intensive (30+ hrs/week)": 1.5}
        
        user_params = {
            'experience_level': exp_mapping[experience_level],
            'time_commitment': time_mapping[time_commitment],
            'budget_factor': budget_limit / 3000,  # Normalized to base budget
            'current_salary': current_salary
        }
        
        # Simulate adjusted scenario
        adjusted_scenario = simulate_career_path(scenario_data, user_params)
        
        total_cost = sum(step['cost'] for step in adjusted_scenario['steps'])
        total_time = sum(step['time_hours'] for step in adjusted_scenario['steps'])
        final_salary = adjusted_scenario['salary_progression'][-1]
        roi_period = len(adjusted_scenario['steps'])
        
        st.metric("Total Investment", f"${total_cost:,}")
        st.metric("Total Learning Hours", f"{total_time:,}")
        st.metric("Success Probability", f"{adjusted_scenario['success_rate']}%")
        st.metric("Expected Final Salary", f"${final_salary:,}")
    
    # Run simulation button
    if st.button("🎮 Run Career Simulation", type="primary", use_container_width=True):
        
        # Simulation results
        st.header("📊 Simulation Results")
        
        # Key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            salary_increase = final_salary - current_salary
            increase_percentage = (salary_increase / current_salary) * 100
            metric_html = f"""
            <div class="metric-card">
                <h3>💰 Salary Increase</h3>
                <p style="font-size: 1.5em; margin: 0.5rem 0; font-weight: bold;">+${salary_increase:,}</p>
                <p style="margin: 0;">(+{increase_percentage:.1f}%)</p>
            </div>
            """
            st.markdown(metric_html, unsafe_allow_html=True)
        
        with col2:
            roi = (salary_increase / total_cost) if total_cost > 0 else 0
            metric_html = f"""
            <div class="metric-card">
                <h3>📈 ROI Multiple</h3>
                <p style="font-size: 1.5em; margin: 0.5rem 0; font-weight: bold;">{roi:.1f}x</p>
                <p style="margin: 0;">Return on Investment</p>
            </div>
            """
            st.markdown(metric_html, unsafe_allow_html=True)
        
        with col3:
            payback_months = (total_cost / (salary_increase / 12)) if salary_increase > 0 else float('inf')
            metric_html = f"""
            <div class="metric-card">
                <h3>⏰ Payback Period</h3>
                <p style="font-size: 1.5em; margin: 0.5rem 0; font-weight: bold;">{payback_months:.1f}</p>
                <p style="margin: 0;">months</p>
            </div>
            """
            st.markdown(metric_html, unsafe_allow_html=True)
        
        with col4:
            risk_score = 100 - adjusted_scenario['success_rate']
            risk_level = "Low" if risk_score < 20 else "Medium" if risk_score < 40 else "High"
            metric_html = f"""
            <div class="metric-card">
                <h3>⚠️ Risk Level</h3>
                <p style="font-size: 1.5em; margin: 0.5rem 0; font-weight: bold;">{risk_level}</p>
                <p style="margin: 0;">({risk_score}% risk)</p>
            </div>
            """
            st.markdown(metric_html, unsafe_allow_html=True)
        
        # Detailed timeline and costs
        st.header("📅 Detailed Learning Path")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Timeline chart
            timeline_fig = create_timeline_chart(adjusted_scenario)
            st.plotly_chart(timeline_fig, use_container_width=True)
        
        with col2:
            # Cost breakdown
            cost_fig = create_cost_breakdown_chart(adjusted_scenario)
            st.plotly_chart(cost_fig, use_container_width=True)
        
        # Salary projection
        salary_fig = create_salary_projection_chart(adjusted_scenario)
        st.plotly_chart(salary_fig, use_container_width=True)
        
        # Step-by-step breakdown
        st.header("📋 Month-by-Month Breakdown")
        
        for i, step in enumerate(adjusted_scenario['steps'], 1):
            with st.expander(f"Month {step['month']}: {step['activity']}", expanded=False):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Cost", f"${step['cost']}")
                
                with col2:
                    st.metric("Time Required", f"{step['time_hours']} hours")
                
                with col3:
                    st.metric("Weekly Commitment", f"{step['time_hours']/4:.1f} hrs/week")
                
                # Progress indicator with proper HTML formatting
                progress = (i / len(adjusted_scenario['steps'])) * 100
                progress_html = f"""
                <div class="progress-container">
                    <div class="progress-bar" style="width: {progress:.0f}%;">
                        {progress:.0f}% Complete
                    </div>
                </div>
                """
                st.markdown(progress_html, unsafe_allow_html=True)
        
        # Risk assessment and recommendations
        st.header("⚖️ Risk Assessment & Recommendations")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Risk factors
            st.subheader("🚨 Risk Factors")
            
            risk_factors = []
            if total_cost > budget_limit:
                risk_factors.append("Budget exceeds your limit")
            if adjusted_scenario['success_rate'] < 70:
                risk_factors.append("Lower than average success rate")
            if family_situation == "Married/With Kids" and time_commitment == "Intensive (30+ hrs/week)":
                risk_factors.append("Time commitment may conflict with family responsibilities")
            if current_salary > 80000 and selected_scenario in ["Cybersecurity Analyst"]:
                risk_factors.append("Potential salary decrease during transition")
            
            if risk_factors:
                for factor in risk_factors:
                    warning_html = f"""
                    <div class="warning-box">
                        ⚠️ <strong>Risk:</strong> {factor}
                    </div>
                    """
                    st.markdown(warning_html, unsafe_allow_html=True)
            else:
                success_html = """
                <div class="success-box">
                    ✅ <strong>Low Risk:</strong> Favorable conditions for career transition
                </div>
                """
                st.markdown(success_html, unsafe_allow_html=True)
        
        with col2:
            # Recommendations
            st.subheader("💡 Recommendations")
            
            recommendations = []
            
            if total_cost > budget_limit:
                recommendations.append("Consider part-time learning to spread costs")
            if adjusted_scenario['success_rate'] < 70:
                recommendations.append("Focus on building strong portfolio projects")
            if experience_level == "Entry Level (0-2 years)":
                recommendations.append("Consider finding a mentor in the field")
            if risk_tolerance == "Conservative":
                recommendations.append("Start with free resources before investing")
            
            # Add positive recommendations
            recommendations.append("Join relevant online communities and forums")
            recommendations.append("Network with professionals in your target field")
            recommendations.append("Consider remote work opportunities to expand job market")
            
            for rec in recommendations[:5]:
                rec_html = f"""
                <div class="path-step">
                    💡 {rec}
                </div>
                """
                st.markdown(rec_html, unsafe_allow_html=True)
        
        # Skills development timeline
        st.header("🎓 Skills Development Timeline")
        
        skills = adjusted_scenario.get('skills_gained', [])
        for i, skill in enumerate(skills):
            month = (i + 1) * (len(adjusted_scenario['steps']) // len(skills))
            timeline_html = f"""
            <div class="timeline-item">
                <strong>Month {month}:</strong> Master {skill}
            </div>
            """
            st.markdown(timeline_html, unsafe_allow_html=True)
        
        # Next steps
        st.header("🚀 Next Steps")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("📊 Detailed Skill Analysis", use_container_width=True):
                st.switch_page("pages/2_Skill_Gap_Analysis.py")
        
        with col2:
            if st.button("💬 Get AI Career Advice", use_container_width=True):
                st.switch_page("pages/3_Career_Chat_Assistant.py")
        
        with col3:
            if st.button("🔄 Try Different Scenario", use_container_width=True):
                st.rerun()
        
        # Export simulation results
        st.header("💾 Export Results")
        
        simulation_summary = {
            "scenario": selected_scenario,
            "user_profile": {
                "current_salary": current_salary,
                "experience_level": experience_level,
                "time_commitment": time_commitment,
                "budget_limit": budget_limit
            },
            "results": {
                "total_cost": total_cost,
                "total_hours": total_time,
                "success_rate": adjusted_scenario['success_rate'],
                "final_salary": final_salary,
                "salary_increase": salary_increase,
                "roi_multiple": roi,
                "payback_months": payback_months
            },
            "timeline": adjusted_scenario['steps'],
            "skills_gained": skills,
            "generated_on": datetime.now().isoformat()
        }
        
        import json
        
        col1, col2 = st.columns(2)
        with col1:
            st.download_button(
                label="📥 Download Simulation Report (JSON)",
                data=json.dumps(simulation_summary, indent=2),
                file_name=f"career_simulation_{selected_scenario.lower().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.json",
                mime="application/json"
            )
        
        with col2:
            # Simple text summary for copying
            text_summary = f"""
Career Simulation Report: {selected_scenario}
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}

Profile:
- Current Salary: ${current_salary:,}
- Experience Level: {experience_level}
- Time Commitment: {time_commitment}

Results:
- Total Investment: ${total_cost:,}
- Expected Final Salary: ${final_salary:,}
- Salary Increase: +${salary_increase:,} (+{increase_percentage:.1f}%)
- Success Probability: {adjusted_scenario['success_rate']}%
- ROI Multiple: {roi:.1f}x
- Payback Period: {payback_months:.1f} months

Skills to Gain: {', '.join(skills)}
            """
            
            st.download_button(
                label="📄 Download Summary (TXT)",
                data=text_summary,
                file_name=f"career_simulation_summary_{datetime.now().strftime('%Y%m%d')}.txt",
                mime="text/plain"
            )
    
    else:
        # Initial state - show overview
        st.header("🎯 How Career Simulation Works")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            card_html = """
            <div class="simulation-card">
                <h4 style="color: #667eea;">1️⃣ Choose Scenario</h4>
                <p>Select from realistic career transition paths in AI, Blockchain, Cybersecurity, and Data Science.</p>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
        
        with col2:
            card_html = """
            <div class="simulation-card">
                <h4 style="color: #667eea;">2️⃣ Set Parameters</h4>
                <p>Configure your personal situation, learning preferences, and risk tolerance for accurate modeling.</p>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
        
        with col3:
            card_html = """
            <div class="simulation-card">
                <h4 style="color: #667eea;">3️⃣ Analyze Results</h4>
                <p>Review detailed projections, timelines, costs, and success probabilities to make informed decisions.</p>
            </div>
            """
            st.markdown(card_html, unsafe_allow_html=True)
        
        st.info("👈 **Configure your parameters in the sidebar and select a career scenario above to begin simulation**")
        
        # Show sample scenarios overview
        st.header("🌟 Available Career Scenarios")
        
        for scenario_name, scenario_data in sim_data["scenarios"].items():
            with st.expander(f"{scenario_name} - {scenario_data['difficulty']} Difficulty", expanded=False):
                col1, col2 = st.columns([2, 1])
                
                with col1:
                    st.write(f"**Description:** {scenario_data['description']}")
                    st.write(f"**Duration:** {scenario_data['duration']}")
                    st.write(f"**Investment Range:** {scenario_data['investment']}")
                    st.write(f"**Skills Gained:** {', '.join(scenario_data.get('skills_gained', []))}")
                
                with col2:
                    st.metric("Success Rate", f"{scenario_data['success_rate']}%")
                    st.metric("Learning Steps", len(scenario_data['steps']))
                    final_salary = scenario_data['salary_progression'][-1]
                    st.metric("Target Salary", f"${final_salary:,}")
    
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