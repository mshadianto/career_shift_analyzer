# indonesia_career_data.py
"""
Indonesian-specific career data and utilities for Career Shift Analyzer Pro
⚠️ DISCLAIMER: This data is simulated for prototype demonstration purposes.
For production use, integrate with real market research data from sources like:
- Michael Page Salary Guide, Hays Salary Survey, JobStreet reports, etc.
"""

import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

# Indonesian Salary Data (2024-2025) - From your roadmap
INDONESIA_SALARY_DATA = {
    "Artificial Intelligence": {
        "entry_level": {"min": 8000000, "max": 15000000},
        "mid_level": {"min": 15000000, "max": 35000000}, 
        "senior_level": {"min": 35000000, "max": 80000000},
        "expert_level": {"min": 80000000, "max": 150000000}
    },
    "Data Science": {
        "entry_level": {"min": 7000000, "max": 12000000},
        "mid_level": {"min": 12000000, "max": 25000000},
        "senior_level": {"min": 25000000, "max": 60000000},
        "expert_level": {"min": 60000000, "max": 120000000}
    },
    "Cybersecurity": {
        "entry_level": {"min": 6000000, "max": 10000000},
        "mid_level": {"min": 10000000, "max": 20000000},
        "senior_level": {"min": 20000000, "max": 50000000},
        "expert_level": {"min": 50000000, "max": 100000000}
    },
    "Software Engineering": {
        "entry_level": {"min": 6000000, "max": 12000000},
        "mid_level": {"min": 12000000, "max": 25000000},
        "senior_level": {"min": 25000000, "max": 55000000},
        "expert_level": {"min": 55000000, "max": 120000000}
    },
    "Product Management": {
        "entry_level": {"min": 8000000, "max": 15000000},
        "mid_level": {"min": 15000000, "max": 30000000},
        "senior_level": {"min": 30000000, "max": 65000000},
        "expert_level": {"min": 65000000, "max": 130000000}
    },
    "UI/UX Design": {
        "entry_level": {"min": 5000000, "max": 10000000},
        "mid_level": {"min": 10000000, "max": 20000000},
        "senior_level": {"min": 20000000, "max": 45000000},
        "expert_level": {"min": 45000000, "max": 85000000}
    }
}

# Indonesian Tech Cities Data
INDONESIA_TECH_CITIES = {
    "Jakarta": {
        "companies": 150,
        "avg_salary_multiplier": 1.0,
        "remote_culture": "85%",
        "description": "Pusat ekonomi digital Indonesia",
        "cost_of_living_index": 1.0
    },
    "Bandung": {
        "companies": 80,
        "avg_salary_multiplier": 0.8,
        "remote_culture": "90%", 
        "description": "Silicon Valley Indonesia",
        "cost_of_living_index": 0.7
    },
    "Surabaya": {
        "companies": 45,
        "avg_salary_multiplier": 0.75,
        "remote_culture": "70%",
        "description": "Hub industri Jawa Timur",
        "cost_of_living_index": 0.65
    },
    "Yogyakarta": {
        "companies": 35,
        "avg_salary_multiplier": 0.7,
        "remote_culture": "80%",
        "description": "Pusat startup kreatif",
        "cost_of_living_index": 0.6
    },
    "Bali": {
        "companies": 30,
        "avg_salary_multiplier": 0.9,
        "remote_culture": "95%",
        "description": "Digital nomad paradise",
        "cost_of_living_index": 0.8
    }
}

# Indonesian Tech Companies
INDONESIA_COMPANIES = {
    "Unicorn": ["Gojek", "Tokopedia", "Bukalapak", "Traveloka", "OVO"],
    "Decacorn": ["Shopee Indonesia", "Grab Indonesia"],
    "Scale-up": ["Ajaib", "Xendit", "Midtrans", "Koinworks", "Stockbit", "Flip", "DANA"],
    "Multinational": ["Google Indonesia", "Microsoft Indonesia", "Amazon Web Services", "Meta Indonesia"],
    "Banks Digital": ["Jenius", "Digibank", "Blu BCA", "Jago", "Seabank"],
    "E-commerce": ["Blibli", "Zalora", "Bhinneka", "JD.ID", "Lazada Indonesia"]
}

# Learning Resources Indonesia
INDONESIA_LEARNING = {
    "Bootcamp": {
        "Hacktiv8": {"focus": "Full-stack development, Data Science", "duration": "3-6 bulan", "price": "Rp 15-35 juta"},
        "Purwadhika": {"focus": "Digital Technology School", "duration": "3-4 bulan", "price": "Rp 12-25 juta"},
        "Algoritma": {"focus": "Data Science & AI", "duration": "2-4 bulan", "price": "Rp 8-20 juta"},
        "Binar Academy": {"focus": "Software development", "duration": "4-6 bulan", "price": "Rp 10-30 juta"},
        "Dicoding": {"focus": "Mobile & Web development", "duration": "1-3 bulan", "price": "Rp 2-8 juta"}
    },
    "Universities": [
        "Institut Teknologi Bandung (ITB)",
        "Universitas Indonesia (UI)", 
        "Institut Teknologi Sepuluh Nopember (ITS)",
        "Universitas Gadjah Mada (UGM)",
        "Binus University",
        "Telkom University"
    ],
    "Communities": [
        "Indonesia Android Kejar (IAK)",
        "JakartaJS",
        "Python Indonesia", 
        "React Indonesia",
        "AI/ML Indonesia",
        "Women in Tech Indonesia"
    ]
}

# Success Stories
INDONESIA_SUCCESS_STORIES = [
    {
        "name": "Andi Pratama",
        "from": "Bank Teller",
        "to": "Data Scientist at GoPang", 
        "duration": "10 bulan",
        "training": "Algoritma Data Science + Coursera",
        "salary_increase": "300%",
        "story": "Dari teller bank dengan gaji Rp 4 juta menjadi Data Scientist dengan gaji Rp 15 juta di GoPang"
    },
    {
        "name": "Sari Dewi", 
        "from": "Marketing Executive",
        "to": "Product Manager at Sotoypedia",
        "duration": "8 bulan",
        "training": "Google PM Certificate + Hacktiv8",
        "salary_increase": "250%",
        "story": "Transisi dari marketing tradisional ke Product Manager tech dengan bantuan bootcamp lokal"
    },
    {
        "name": "Budi Santoso",
        "from": "Guru SMA",
        "to": "Cybersecurity Analyst at ABC Digital",
        "duration": "12 bulan",
        "training": "Self-learning + Dicoding + CISSP",
        "salary_increase": "200%", 
        "story": "Dari mengajar di sekolah menjadi cybersecurity professional di bank digital"
    }
]

# Government Programs
GOVERNMENT_PROGRAMS = {
    "Kartu Prakerja": {
        "description": "Program pelatihan dan sertifikasi gratis",
        "budget": "Rp 3.5 juta per peserta",
        "focus": "Digital skills, programming, data analysis"
    },
    "Digital Talent Scholarship": {
        "description": "Beasiswa dari Kemkominfo",
        "categories": ["Fresh Graduate", "Professional Development"],
        "focus": "AI, Cybersecurity, Big Data, Cloud Computing"
    },
    "Beasiswa LPDP": {
        "description": "Beasiswa pendidikan tinggi",
        "coverage": "S2/S3 dalam dan luar negeri",
        "focus": "Technology and Engineering"
    }
}

# Bahasa Indonesia Translations
TRANSLATIONS = {
    "id": {
        "career_simulation": "Simulasi Karir",
        "skill_analysis": "Analisis Keahlian", 
        "ai_assistant": "Asisten AI",
        "salary_range": "Kisaran Gaji",
        "job_growth": "Pertumbuhan Pekerjaan",
        "start_analysis": "Mulai Analisis",
        "your_profile": "Profil Anda",
        "recommendations": "Rekomendasi",
        "current_role": "Peran Saat Ini",
        "target_role": "Target Karir",
        "experience_level": "Level Pengalaman",
        "preferred_city": "Kota Pilihan",
        "learning_budget": "Budget Pembelajaran",
        "timeline": "Timeline Transisi",
        "companies": "Perusahaan",
        "salary_projection": "Proyeksi Gaji",
        "learning_path": "Jalur Pembelajaran",
        "success_stories": "Kisah Sukses"
    }
}

def format_idr_currency(amount):
    """Format currency in Indonesian Rupiah"""
    if amount >= 1000000000:
        return f"Rp {amount/1000000000:.1f} M"
    elif amount >= 1000000:
        return f"Rp {amount/1000000:.0f} juta"
    else:
        return f"Rp {amount:,.0f}".replace(",", ".")

def get_adjusted_salary(base_salary, city):
    """Get salary adjusted for Indonesian city"""
    multiplier = INDONESIA_TECH_CITIES.get(city, {}).get("avg_salary_multiplier", 1.0)
    return {
        "min": int(base_salary["min"] * multiplier),
        "max": int(base_salary["max"] * multiplier)
    }

def calculate_cost_of_living_ratio(salary, city):
    """Calculate salary to cost of living ratio"""
    col_index = INDONESIA_TECH_CITIES.get(city, {}).get("cost_of_living_index", 1.0)
    return salary / col_index

def create_indonesia_salary_chart(career_field, city="Jakarta"):
    """Create salary progression chart for Indonesian market"""
    levels = ["entry_level", "mid_level", "senior_level", "expert_level"]
    level_names = ["Entry Level", "Mid Level", "Senior Level", "Expert Level"]
    
    salary_data = INDONESIA_SALARY_DATA.get(career_field, {})
    min_salaries = []
    max_salaries = []
    avg_salaries = []
    
    for level in levels:
        if level in salary_data:
            adjusted = get_adjusted_salary(salary_data[level], city)
            min_salaries.append(adjusted["min"])
            max_salaries.append(adjusted["max"])
            avg_salaries.append((adjusted["min"] + adjusted["max"]) / 2)
        else:
            min_salaries.append(0)
            max_salaries.append(0)
            avg_salaries.append(0)
    
    fig = go.Figure()
    
    # Add salary range
    fig.add_trace(go.Scatter(
        x=level_names,
        y=max_salaries,
        fill=None,
        mode='lines',
        line_color='rgba(0,100,80,0)',
        showlegend=False
    ))
    
    fig.add_trace(go.Scatter(
        x=level_names,
        y=min_salaries,
        fill='tonexty',
        mode='lines',
        line_color='rgba(0,100,80,0)',
        name='Kisaran Gaji',
        fillcolor='rgba(0,100,80,0.2)'
    ))
    
    # Add average line
    fig.add_trace(go.Scatter(
        x=level_names,
        y=avg_salaries,
        mode='lines+markers',
        name='Rata-rata',
        line=dict(color='rgb(0,100,80)', width=3),
        marker=dict(size=8)
    ))
    
    fig.update_layout(
        title=f'Proyeksi Gaji {career_field} di {city}',
        xaxis_title='Level Karir',
        yaxis_title='Gaji (IDR)',
        hovermode='x unified',
        yaxis=dict(tickformat=',.0f', tickprefix='Rp ')
    )
    
    return fig

def display_indonesia_companies():
    """Display Indonesian tech companies by category"""
    st.subheader("🏢 Ekosistem Perusahaan Tech Indonesia")
    
    for category, companies in INDONESIA_COMPANIES.items():
        with st.expander(f"{category} ({len(companies)} perusahaan)"):
            cols = st.columns(3)
            for i, company in enumerate(companies):
                with cols[i % 3]:
                    st.write(f"• {company}")

def display_learning_resources():
    """Display Indonesian learning resources"""
    st.subheader("🎓 Sumber Belajar Indonesia")
    
    tab1, tab2, tab3 = st.tabs(["Bootcamp", "Universitas", "Komunitas"])
    
    with tab1:
        for bootcamp, details in INDONESIA_LEARNING["Bootcamp"].items():
            with st.expander(bootcamp):
                st.write(f"**Focus:** {details['focus']}")
                st.write(f"**Durasi:** {details['duration']}")
                st.write(f"**Biaya:** {details['price']}")
    
    with tab2:
        for uni in INDONESIA_LEARNING["Universities"]:
            st.write(f"• {uni}")
    
    with tab3:
        for community in INDONESIA_LEARNING["Communities"]:
            st.write(f"• {community}")

def display_success_stories():
    """Display Indonesian success stories"""
    st.subheader("🌟 Kisah Sukses Indonesia")
    
    for story in INDONESIA_SUCCESS_STORIES:
        with st.expander(f"{story['name']}: {story['from']} → {story['to']}"):
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Durasi Transisi", story["duration"])
                st.metric("Peningkatan Gaji", story["salary_increase"])
            with col2:
                st.write(f"**Training:** {story['training']}")
                st.write(story["story"])

def create_city_comparison_chart():
    """Create comparison chart of Indonesian tech cities"""
    cities = list(INDONESIA_TECH_CITIES.keys())
    companies = [INDONESIA_TECH_CITIES[city]["companies"] for city in cities]
    salary_mult = [INDONESIA_TECH_CITIES[city]["avg_salary_multiplier"] for city in cities]
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        name='Jumlah Perusahaan',
        x=cities,
        y=companies,
        yaxis='y',
        offsetgroup=1
    ))
    
    fig.add_trace(go.Scatter(
        name='Multiplier Gaji',
        x=cities,
        y=salary_mult,
        yaxis='y2',
        mode='lines+markers',
        line=dict(color='red', width=3)
    ))
    
    fig.update_layout(
        title='Perbandingan Kota Tech Indonesia',
        xaxis=dict(title='Kota'),
        yaxis=dict(title='Jumlah Perusahaan', side='left'),
        yaxis2=dict(title='Multiplier Gaji', side='right', overlaying='y'),
        legend=dict(x=0.7, y=1)
    )
    
    return fig

def indonesia_pph21_calculator(annual_salary):
    """Calculate Indonesian PPh 21 tax"""
    # Simplified PPh 21 calculation (2024 rates)
    ptkp = 54000000  # Basic tax-free income
    taxable_income = max(0, annual_salary - ptkp)
    
    # Progressive tax rates
    if taxable_income <= 60000000:
        tax = taxable_income * 0.05
    elif taxable_income <= 250000000:
        tax = 60000000 * 0.05 + (taxable_income - 60000000) * 0.15
    elif taxable_income <= 500000000:
        tax = 60000000 * 0.05 + 190000000 * 0.15 + (taxable_income - 250000000) * 0.25
    else:
        tax = 60000000 * 0.05 + 190000000 * 0.15 + 250000000 * 0.25 + (taxable_income - 500000000) * 0.30
    
    return {
        "annual_tax": tax,
        "monthly_tax": tax / 12,
        "net_annual": annual_salary - tax,
        "net_monthly": (annual_salary - tax) / 12
    }

# Language support functions
def get_translation(key, lang="id"):
    """Get translation for given key"""
    return TRANSLATIONS.get(lang, {}).get(key, key)

def format_indonesian_date():
    """Format date in Indonesian"""
    months = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
              "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    now = datetime.now()
    return f"{now.day} {months[now.month-1]} {now.year}"