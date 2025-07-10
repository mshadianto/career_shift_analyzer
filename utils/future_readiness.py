# utils/future_readiness.py - Enhanced with advanced calculations

import math
from typing import List, Dict, Tuple
from datetime import datetime

def get_enhanced_skill_weights():
    """Enhanced skill weights with more comprehensive mapping"""
    return {
        "Artificial Intelligence": {
            "core_skills": ["python", "machine learning", "statistics", "data science", "deep learning"],
            "tools": ["tensorflow", "pytorch", "scikit-learn", "jupyter", "pandas"],
            "soft_skills": ["problem solving", "critical thinking", "research", "communication"],
            "certifications": ["google ai", "aws ml", "tensorflow developer"],
            "weight_multipliers": {"core_skills": 1.0, "tools": 0.8, "soft_skills": 0.6, "certifications": 0.9}
        },
        "Blockchain": {
            "core_skills": ["solidity", "smart contracts", "cryptography", "web3", "defi"],
            "tools": ["remix", "hardhat", "metamask", "web3.js", "truffle"],
            "soft_skills": ["security mindset", "attention to detail", "innovation", "risk assessment"],
            "certifications": ["certified bitcoin professional", "ethereum developer"],
            "weight_multipliers": {"core_skills": 1.0, "tools": 0.8, "soft_skills": 0.5, "certifications": 1.0}
        },
        "Renewable Energy": {
            "core_skills": ["solar", "sustainability", "electrical engineering", "grid systems"],
            "tools": ["autocad", "matlab", "pvsyst", "homer"],
            "soft_skills": ["environmental awareness", "project management", "communication"],
            "certifications": ["nabcep", "leed", "pmp"],
            "weight_multipliers": {"core_skills": 1.0, "tools": 0.7, "soft_skills": 0.6, "certifications": 0.8}
        },
        "Biotechnology": {
            "core_skills": ["bioinformatics", "genetics", "molecular biology", "lab skills"],
            "tools": ["r", "python", "blast", "clustal", "laboratory equipment"],
            "soft_skills": ["attention to detail", "analytical thinking", "research", "ethics"],
            "certifications": ["clinical research", "biotech certifications"],
            "weight_multipliers": {"core_skills": 1.0, "tools": 0.8, "soft_skills": 0.6, "certifications": 0.7}
        },
        "Space Exploration": {
            "core_skills": ["physics", "aerospace engineering", "navigation", "satellite systems"],
            "tools": ["matlab", "labview", "stk", "ansys"],
            "soft_skills": ["precision", "problem solving", "teamwork", "stress management"],
            "certifications": ["faa", "nasa certifications", "aerospace engineering"],
            "weight_multipliers": {"core_skills": 1.0, "tools": 0.8, "soft_skills": 0.6, "certifications": 0.9}
        },
        "Cybersecurity": {
            "core_skills": ["network security", "penetration testing", "incident response", "risk assessment"],
            "tools": ["wireshark", "metasploit", "nmap", "burp suite", "siem"],
            "soft_skills": ["ethical mindset", "attention to detail", "communication", "continuous learning"],
            "certifications": ["cissp", "ceh", "security+", "oscp"],
            "weight_multipliers": {"core_skills": 1.0, "tools": 0.8, "soft_skills": 0.6, "certifications": 1.0}
        }
    }

def calculate_skill_category_score(user_skills: List[str], required_skills: List[str], weight: float = 1.0) -> Tuple[float, List[str], List[str]]:
    """Calculate score for a specific skill category"""
    if not required_skills:
        return 0.0, [], []
    
    user_skills_normalized = [skill.lower().strip() for skill in user_skills if skill]
    required_skills_normalized = [skill.lower().strip() for skill in required_skills]
    
    # Direct matches
    matched_skills = []
    for req_skill in required_skills:
        if req_skill.lower() in user_skills_normalized:
            matched_skills.append(req_skill)
    
    # Partial matches (for compound skills)
    partial_matches = []
    for user_skill in user_skills_normalized:
        for req_skill in required_skills_normalized:
            if (user_skill not in [m.lower() for m in matched_skills] and 
                req_skill not in [m.lower() for m in matched_skills] and
                (user_skill in req_skill or req_skill in user_skill)):
                partial_matches.append(req_skill)
    
    total_matched = len(matched_skills) + (len(partial_matches) * 0.5)
    category_score = (total_matched / len(required_skills)) * 100 * weight
    
    missing_skills = [skill for skill in required_skills 
                     if skill.lower() not in [m.lower() for m in matched_skills + partial_matches]]
    
    return min(category_score, 100), matched_skills + partial_matches, missing_skills

def calculate_experience_bonus(years_experience: int, field_difficulty: str) -> float:
    """Calculate experience bonus based on years and field difficulty"""
    difficulty_multipliers = {
        "Easy": 1.0,
        "Medium": 1.2,
        "Hard": 1.5,
        "Very Hard": 2.0
    }
    
    base_bonus = min(years_experience * 3, 20)  # Max 20 points from experience
    multiplier = difficulty_multipliers.get(field_difficulty, 1.0)
    
    return base_bonus / multiplier

def calculate_learning_commitment_factor(weekly_hours: int, urgency: str) -> float:
    """Calculate learning commitment impact on readiness"""
    urgency_factors = {
        "No Rush": 0.8,
        "6-12 months": 1.0,
        "3-6 months": 1.2,
        "ASAP": 1.5
    }
    
    hours_factor = min(weekly_hours / 20, 1.5)  # 20 hours/week baseline, max 1.5x
    urgency_factor = urgency_factors.get(urgency, 1.0)
    
    return hours_factor * urgency_factor

def get_field_difficulty_rating(field: str) -> str:
    """Get difficulty rating for different fields"""
    difficulty_map = {
        "Artificial Intelligence": "Hard",
        "Blockchain": "Very Hard",
        "Renewable Energy": "Medium",
        "Biotechnology": "Hard",
        "Space Exploration": "Very Hard",
        "Cybersecurity": "Hard"
    }
    return difficulty_map.get(field, "Medium")

def calculate_advanced_readiness_score(
    user_skills_by_category: Dict[str, List[str]], 
    target_fields: List[str],
    years_experience: int = 0,
    weekly_learning_hours: int = 10,
    career_urgency: str = "6-12 months",
    current_role: str = ""
) -> Dict:
    """
    Calculate advanced readiness score with detailed breakdown
    
    Args:
        user_skills_by_category: Dict with keys 'core_skills', 'tools', 'soft_skills', 'certifications'
        target_fields: List of target career fields
        years_experience: Years of relevant experience
        weekly_learning_hours: Hours per week available for learning
        career_urgency: Timeline urgency
        current_role: Current job role for context
    """
    
    skill_weights = get_enhanced_skill_weights()
    results = {}
    
    for field in target_fields:
        if field not in skill_weights:
            continue
            
        field_data = skill_weights[field]
        field_difficulty = get_field_difficulty_rating(field)
        
        # Calculate scores for each category
        category_scores = {}
        matched_skills = {}
        missing_skills = {}
        
        for category in ['core_skills', 'tools', 'soft_skills', 'certifications']:
            if category in user_skills_by_category and category in field_data:
                user_cat_skills = user_skills_by_category[category]
                required_cat_skills = field_data[category]
                weight = field_data['weight_multipliers'][category]
                
                score, matched, missing = calculate_skill_category_score(
                    user_cat_skills, required_cat_skills, weight
                )
                
                category_scores[category] = score
                matched_skills[category] = matched
                missing_skills[category] = missing
            else:
                category_scores[category] = 0
                matched_skills[category] = []
                missing_skills[category] = field_data.get(category, [])
        
        # Calculate weighted overall score
        weights = {
            'core_skills': 0.4,
            'tools': 0.25, 
            'soft_skills': 0.15,
            'certifications': 0.2
        }
        
        base_score = sum(category_scores[cat] * weights[cat] for cat in weights.keys())
        
        # Apply bonuses and penalties
        experience_bonus = calculate_experience_bonus(years_experience, field_difficulty)
        learning_factor = calculate_learning_commitment_factor(weekly_learning_hours, career_urgency)
        
        # Role relevance bonus
        role_bonus = 0
        if current_role:
            role_keywords = {
                "Artificial Intelligence": ["data", "analyst", "research", "scientist", "engineer"],
                "Blockchain": ["developer", "fintech", "crypto", "finance"],
                "Cybersecurity": ["security", "it", "network", "systems"],
                "Renewable Energy": ["energy", "engineer", "sustainability", "environmental"],
                "Biotechnology": ["lab", "research", "biology", "medical", "pharma"],
                "Space Exploration": ["engineer", "aerospace", "physics", "research"]
            }
            
            field_keywords = role_keywords.get(field, [])
            current_role_lower = current_role.lower()
            
            if any(keyword in current_role_lower for keyword in field_keywords):
                role_bonus = 10
        
        # Calculate final score
        adjusted_score = base_score + experience_bonus + role_bonus
        final_score = min(adjusted_score * learning_factor, 100)
        
        # Determine readiness level
        if final_score >= 80:
            readiness_level = "Ready"
            action_needed = "Start applying for positions"
        elif final_score >= 60:
            readiness_level = "Almost Ready"
            action_needed = "Focus on key gaps"
        elif final_score >= 40:
            readiness_level = "Developing"
            action_needed = "Structured learning needed"
        else:
            readiness_level = "Beginner"
            action_needed = "Foundation building required"
        
        # Calculate estimated timeline
        skill_gap = 100 - base_score
        base_months = max(3, skill_gap / 15)  # 15 points per month baseline
        timeline_months = base_months / learning_factor
        
        urgency_adjustments = {
            "ASAP": 0.7,
            "3-6 months": 0.8,
            "6-12 months": 1.0,
            "No Rush": 1.3
        }
        
        final_timeline = timeline_months * urgency_adjustments.get(career_urgency, 1.0)
        
        results[field] = {
            "overall_score": round(final_score, 1),
            "base_score": round(base_score, 1),
            "category_scores": {k: round(v, 1) for k, v in category_scores.items()},
            "matched_skills": matched_skills,
            "missing_skills": missing_skills,
            "readiness_level": readiness_level,
            "action_needed": action_needed,
            "estimated_timeline_months": round(final_timeline, 1),
            "experience_bonus": round(experience_bonus, 1),
            "role_relevance_bonus": role_bonus,
            "learning_factor": round(learning_factor, 2),
            "field_difficulty": field_difficulty,
            "total_skills_needed": sum(len(field_data[cat]) for cat in ['core_skills', 'tools', 'soft_skills', 'certifications']),
            "skills_acquired": sum(len(matched_skills[cat]) for cat in matched_skills.keys()),
            "completion_percentage": round((sum(len(matched_skills[cat]) for cat in matched_skills.keys()) / 
                                          sum(len(field_data[cat]) for cat in ['core_skills', 'tools', 'soft_skills', 'certifications'])) * 100, 1)
        }
    
    return results

def calculate_readiness_score(user_skills: List[str], interest_fields: List[str], waktu_belajar: int = 10) -> int:
    """
    Simplified version for backward compatibility
    Legacy function maintained for existing integrations
    """
    base_weights = {
        "Artificial Intelligence": ["python", "sql", "machine learning", "data science"],
        "Blockchain": ["crypto", "solidity", "smart contract", "web3"],
        "Renewable Energy": ["solar", "sustainability", "electrical"],
        "Biotechnology": ["bioinformatics", "genetics", "lab"],
        "Space Exploration": ["physics", "engineering", "navigation"],
        "Cybersecurity": ["network security", "penetration testing", "incident response"]
    }

    matched_skills = 0
    total_required = 0

    for field in interest_fields:
        required = base_weights.get(field, [])
        total_required += len(required)
        for skill in user_skills:
            if any(req_skill in skill.lower() for req_skill in required):
                matched_skills += 1

    # Base score from skill matching
    if total_required == 0:
        skill_score = 0
    else:
        skill_score = matched_skills / total_required

    # Learning time boost
    learning_boost = min(waktu_belajar / 20, 1.0)  # 20 hours/week baseline

    # Combined score
    total_score = round((0.7 * skill_score + 0.3 * learning_boost) * 100)

    return min(total_score, 100)

def get_skill_recommendations(missing_skills: Dict[str, List[str]], field: str) -> Dict[str, Dict]:
    """Generate detailed recommendations for missing skills"""
    recommendations = {}
    
    priority_order = ['core_skills', 'tools', 'certifications', 'soft_skills']
    
    for category in priority_order:
        if category in missing_skills and missing_skills[category]:
            for skill in missing_skills[category][:3]:  # Top 3 per category
                recommendations[skill] = {
                    "category": category,
                    "priority": "High" if category == "core_skills" else "Medium" if category == "tools" else "Low",
                    "estimated_time": "2-4 weeks" if category == "tools" else "4-8 weeks" if category == "core_skills" else "1-2 weeks",
                    "resources": get_learning_resources(skill, field),
                    "practice_projects": get_practice_projects(skill, field)
                }
    
    return recommendations

def get_learning_resources(skill: str, field: str) -> List[str]:
    """Get learning resources for specific skills"""
    skill_lower = skill.lower()
    
    resource_map = {
        "python": ["Python.org Tutorial", "Codecademy Python", "automate the Boring Stuff"],
        "machine learning": ["Coursera ML Course", "Kaggle Learn", "scikit-learn docs"],
        "solidity": ["Solidity Documentation", "CryptoZombies", "Hardhat Tutorial"],
        "network security": ["Cisco Networking Academy", "CompTIA Security+", "Cybrary"],
        "bioinformatics": ["Rosalind Problems", "Coursera Bioinformatics", "NCBI Tutorials"]
    }
    
    return resource_map.get(skill_lower, ["General online courses", "YouTube tutorials", "Official documentation"])

def get_practice_projects(skill: str, field: str) -> List[str]:
    """Get practice project ideas for skills"""
    skill_lower = skill.lower()
    
    project_map = {
        "python": ["Build a calculator", "Web scraper project", "Data analysis with pandas"],
        "machine learning": ["Iris classification", "House price prediction", "Customer segmentation"],
        "solidity": ["Simple token contract", "Voting system", "NFT marketplace"],
        "network security": ["Home network audit", "Vulnerability assessment", "Security monitoring setup"]
    }
    
    return project_map.get(skill_lower, ["Research project", "Tutorial follow-along", "Basic implementation"])

# Export functions
__all__ = [
    'calculate_readiness_score',
    'calculate_advanced_readiness_score',
    'get_skill_recommendations',
    'calculate_skill_category_score'
]
