# utils/recommender.py - Enhanced with better logic and AI integration

import pandas as pd
from typing import Dict, List, Tuple
import random

def get_enhanced_job_mapping():
    """Enhanced job mapping with more comprehensive data"""
    return {
        "Artificial Intelligence": {
            "skills": ["python", "machine learning", "data", "sql", "statistics", "deep learning", "tensorflow", "pytorch"],
            "entry_jobs": ["AI Research Assistant", "Data Analyst", "ML Intern", "Junior Data Scientist"],
            "mid_jobs": ["Machine Learning Engineer", "Data Scientist", "AI Developer", "Computer Vision Engineer"],
            "senior_jobs": ["Principal ML Engineer", "AI Research Lead", "Head of Data Science", "AI Architect"],
            "salary_ranges": {"entry": (60000, 90000), "mid": (90000, 140000), "senior": (140000, 200000)},
            "remote_percentage": 85,
            "market_demand": "Very High"
        },
        "Blockchain": {
            "skills": ["solidity", "crypto", "security", "smart contract", "web3", "ethereum", "defi"],
            "entry_jobs": ["Blockchain Developer Intern", "Smart Contract Auditor Junior", "Crypto Analyst"],
            "mid_jobs": ["Blockchain Developer", "Smart Contract Developer", "DeFi Engineer", "Web3 Developer"],
            "senior_jobs": ["Blockchain Architect", "Principal Blockchain Engineer", "Head of Blockchain"],
            "salary_ranges": {"entry": (70000, 100000), "mid": (100000, 160000), "senior": (160000, 250000)},
            "remote_percentage": 90,
            "market_demand": "High"
        },
        "Renewable Energy": {
            "skills": ["solar", "electrical", "sustainability", "engineering", "grid systems", "energy storage"],
            "entry_jobs": ["Solar Energy Technician", "Renewable Energy Analyst", "Sustainability Coordinator"],
            "mid_jobs": ["Green Finance Analyst", "Energy Systems Engineer", "Solar Project Manager"],
            "senior_jobs": ["Director of Sustainability", "Principal Energy Engineer", "Chief Sustainability Officer"],
            "salary_ranges": {"entry": (45000, 65000), "mid": (65000, 95000), "senior": (95000, 140000)},
            "remote_percentage": 40,
            "market_demand": "Medium"
        },
        "Biotechnology": {
            "skills": ["biology", "genetics", "lab", "bioinformatics", "crispr", "molecular biology"],
            "entry_jobs": ["Lab Research Assistant", "Bioinformatics Analyst", "Quality Control Technician"],
            "mid_jobs": ["Biotechnology Researcher", "Bioinformatics Scientist", "Clinical Research Associate"],
            "senior_jobs": ["Principal Scientist", "Director of R&D", "Chief Scientific Officer"],
            "salary_ranges": {"entry": (50000, 70000), "mid": (70000, 110000), "senior": (110000, 180000)},
            "remote_percentage": 30,
            "market_demand": "Medium"
        },
        "Space Exploration": {
            "skills": ["physics", "engineering", "aerospace", "navigation", "satellite", "mission planning"],
            "entry_jobs": ["Aerospace Data Engineer", "Space Operations Analyst", "Mission Support Specialist"],
            "mid_jobs": ["Satellite Engineer", "Mission Planner", "Space Systems Engineer"],
            "senior_jobs": ["Chief Mission Engineer", "Director of Space Operations", "Principal Aerospace Engineer"],
            "salary_ranges": {"entry": (65000, 85000), "mid": (85000, 130000), "senior": (130000, 200000)},
            "remote_percentage": 60,
            "market_demand": "Medium"
        },
        "Cybersecurity": {
            "skills": ["network security", "penetration testing", "siem", "incident response", "ethical hacking"],
            "entry_jobs": ["Security Analyst", "Junior Penetration Tester", "SOC Analyst"],
            "mid_jobs": ["Cybersecurity Engineer", "Security Consultant", "Incident Response Specialist"],
            "senior_jobs": ["CISO", "Principal Security Architect", "Director of Cybersecurity"],
            "salary_ranges": {"entry": (55000, 75000), "mid": (75000, 120000), "senior": (120000, 180000)},
            "remote_percentage": 80,
            "market_demand": "Very High"
        }
    }

def calculate_skill_match_score(user_skills: List[str], field_skills: List[str]) -> float:
    """Calculate more sophisticated skill matching score"""
    if not field_skills or not user_skills:
        return 0.0
    
    user_skills_lower = [skill.lower().strip() for skill in user_skills]
    field_skills_lower = [skill.lower().strip() for skill in field_skills]
    
    # Direct matches
    direct_matches = sum(1 for skill in field_skills_lower if skill in user_skills_lower)
    
    # Partial matches (for compound skills)
    partial_matches = 0
    for user_skill in user_skills_lower:
        for field_skill in field_skills_lower:
            if user_skill != field_skill and (user_skill in field_skill or field_skill in user_skill):
                partial_matches += 0.5
    
    total_matches = direct_matches + partial_matches
    return min((total_matches / len(field_skills)) * 100, 100)

def determine_experience_level(user_skills: List[str], years_experience: int) -> str:
    """Determine user's experience level based on skills and years"""
    skill_count = len(user_skills)
    
    if years_experience >= 5 or skill_count >= 8:
        return "senior"
    elif years_experience >= 2 or skill_count >= 4:
        return "mid"
    else:
        return "entry"

def get_learning_path(missing_skills: List[str], target_field: str) -> Dict:
    """Generate learning path for missing skills"""
    learning_resources = {
        "Artificial Intelligence": {
            "Python": {"time": "2-3 months", "resources": ["Python.org Tutorial", "Codecademy Python"], "priority": "High"},
            "Machine Learning": {"time": "3-4 months", "resources": ["Coursera ML Course", "Kaggle Learn"], "priority": "High"},
            "Deep Learning": {"time": "4-6 months", "resources": ["Deep Learning Specialization", "Fast.ai"], "priority": "Medium"},
            "TensorFlow": {"time": "2-3 months", "resources": ["TensorFlow.org", "Google AI Education"], "priority": "Medium"}
        },
        "Blockchain": {
            "Solidity": {"time": "2-3 months", "resources": ["Solidity Docs", "CryptoZombies"], "priority": "High"},
            "Smart Contract": {"time": "3-4 months", "resources": ["Ethereum.org", "Hardhat Tutorial"], "priority": "High"},
            "Web3": {"time": "2-3 months", "resources": ["Web3.js Docs", "Moralis Academy"], "priority": "Medium"}
        },
        "Cybersecurity": {
            "Network Security": {"time": "2-3 months", "resources": ["Cisco Networking", "CompTIA Security+"], "priority": "High"},
            "Penetration Testing": {"time": "3-4 months", "resources": ["OSCP Course", "Metasploit Unleashed"], "priority": "High"},
            "SIEM": {"time": "1-2 months", "resources": ["Splunk Fundamentals", "ELK Stack Tutorial"], "priority": "Medium"}
        }
    }
    
    path = {}
    field_resources = learning_resources.get(target_field, {})
    
    for skill in missing_skills:
        skill_key = next((k for k in field_resources.keys() if k.lower() in skill.lower()), None)
        if skill_key:
            path[skill] = field_resources[skill_key]
        else:
            path[skill] = {
                "time": "1-2 months",
                "resources": ["General online courses", "YouTube tutorials"],
                "priority": "Medium"
            }
    
    return path

def advanced_recommender(user_skills: List[str], interest_fields: List[str], years_experience: int = 0) -> Dict:
    """Advanced recommendation engine with detailed analysis"""
    job_mapping = get_enhanced_job_mapping()
    recommendations = {}
    
    for field in interest_fields:
        if field not in job_mapping:
            continue
            
        field_data = job_mapping[field]
        
        # Calculate skill match
        skill_match_score = calculate_skill_match_score(user_skills, field_data["skills"])
        
        # Determine experience level
        exp_level = determine_experience_level(user_skills, years_experience)
        
        # Get appropriate jobs
        jobs = field_data[f"{exp_level}_jobs"]
        salary_range = field_data["salary_ranges"][exp_level]
        
        # Find missing skills
        user_skills_lower = [skill.lower() for skill in user_skills]
        missing_skills = [skill for skill in field_data["skills"] 
                         if skill.lower() not in user_skills_lower]
        
        # Generate learning path
        learning_path = get_learning_path(missing_skills[:5], field)  # Top 5 missing skills
        
        # Calculate transition difficulty
        if skill_match_score >= 70:
            difficulty = "Easy"
            timeline = "3-6 months"
        elif skill_match_score >= 40:
            difficulty = "Medium"
            timeline = "6-12 months"
        else:
            difficulty = "Hard"
            timeline = "12-18 months"
        
        recommendations[field] = {
            "skill_match_score": round(skill_match_score, 1),
            "recommended_jobs": jobs,
            "experience_level": exp_level,
            "salary_range": f"${salary_range[0]:,} - ${salary_range[1]:,}",
            "missing_skills": missing_skills[:5],
            "learning_path": learning_path,
            "transition_difficulty": difficulty,
            "estimated_timeline": timeline,
            "remote_percentage": field_data["remote_percentage"],
            "market_demand": field_data["market_demand"],
            "next_steps": generate_next_steps(skill_match_score, missing_skills, field)
        }
    
    return recommendations

def generate_next_steps(skill_score: float, missing_skills: List[str], field: str) -> List[str]:
    """Generate personalized next steps"""
    steps = []
    
    if skill_score >= 70:
        steps = [
            "Start applying for entry-level positions",
            "Build a portfolio showcasing your skills",
            "Network with professionals in the field",
            "Consider getting relevant certifications"
        ]
    elif skill_score >= 40:
        steps = [
            f"Focus on learning {missing_skills[0] if missing_skills else 'core skills'}",
            "Work on 2-3 practical projects",
            "Join online communities and forums",
            "Consider bootcamps or intensive courses"
        ]
    else:
        steps = [
            "Start with fundamentals and basic concepts",
            "Take structured online courses",
            "Practice with beginner-friendly projects",
            "Find a mentor or study group"
        ]
    
    # Add field-specific advice
    field_advice = {
        "Artificial Intelligence": "Focus on Python and statistics first",
        "Blockchain": "Understand blockchain fundamentals before coding",
        "Cybersecurity": "Practice on platforms like TryHackMe",
        "Biotechnology": "Gain hands-on lab experience",
        "Space Exploration": "Consider aerospace engineering background"
    }
    
    if field in field_advice:
        steps.append(field_advice[field])
    
    return steps

def simple_recommender(user_skills: List[str], interest_fields: List[str]) -> Dict:
    """Simplified version for backward compatibility"""
    job_mapping = get_enhanced_job_mapping()
    recommendations = {}

    for field in interest_fields:
        if field not in job_mapping:
            recommendations[field] = ["(Field not recognized - please check spelling)"]
            continue
            
        field_data = job_mapping[field]
        matched = any(skill.lower() in [s.lower() for s in field_data["skills"]] for skill in user_skills)
        
        if matched:
            recommendations[field] = field_data["entry_jobs"]
        else:
            missing_count = len(field_data["skills"])
            recommendations[field] = [f"(Need to learn {missing_count} core skills - significant training required)"]

    return recommendations

def get_market_insights(field: str) -> Dict:
    """Get market insights for a specific field"""
    job_mapping = get_enhanced_job_mapping()
    
    if field not in job_mapping:
        return {}
    
    field_data = job_mapping[field]
    
    return {
        "remote_work_availability": f"{field_data['remote_percentage']}% of jobs offer remote work",
        "market_demand": field_data["market_demand"],
        "entry_salary": f"${field_data['salary_ranges']['entry'][0]:,} - ${field_data['salary_ranges']['entry'][1]:,}",
        "senior_salary": f"${field_data['salary_ranges']['senior'][0]:,} - ${field_data['salary_ranges']['senior'][1]:,}",
        "key_skills": field_data["skills"][:5],
        "career_progression": f"Entry → Mid → Senior level positions available"
    }

# Export functions for external use
__all__ = [
    'simple_recommender',
    'advanced_recommender', 
    'get_market_insights',
    'calculate_skill_match_score',
    'get_learning_path'
]
