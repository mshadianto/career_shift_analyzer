# 4_Indonesia_Career_Analyzer.py
"""
Indonesian Career Analyzer Page
Dedicated page for Indonesian market with localized data and features
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from indonesia_career_data import *

def main():
    """Main Indonesian Career Analyzer function"""
    
    # Page configuration
    st.set_page_config(
        page_title="Career Shift Analyzer - Indonesia",
        page_icon="🇮🇩",
        layout="wide"
    )
    
    # Custom CSS for Indonesian theme
    st.markdown("""
    <style>
    .indonesia-header {
        background: linear-gradient(90deg, #FF0000 0%, #FFFFFF 50%, #FF0000 100%);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #dc3545;
    }
    .success-story {
        background: #e8f5e8;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Header
    st.markdown("""
    <div class="indonesia-header">
        <h1>🇮🇩 Career Shift Analyzer Pro - Indonesia</h1>
        <p style="font-size: 1.2em; margin: 0;">Panduan Karir Tech Indonesia Terlengkap</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Language selector
    col1, col2 = st.columns([3, 1])
    with col2:
        language = st.selectbox("Bahasa / Language", ["🇮🇩 Indonesia", "🇺🇸 English"], key="lang_selector")
        use_indonesian = language.startswith("🇮🇩")
    
    # Main content tabs
    if use_indonesian:
        tab_names = ["Analisis Gaji", "Kota Tech", "Perusahaan", "Jalur Pembelajaran", "Kisah Sukses", "Program Pemerintah"]
    else:
        tab_names = ["Salary Analysis", "Tech Cities", "Companies", "Learning Paths", "Success Stories", "Government Programs"]
    
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(tab_names)
    
    # Tab 1: Salary Analysis
    with tab1:
        if use_indonesian:
            st.header("💰 Analisis Gaji Tech Indonesia")
            st.subheader("Proyeksi Gaji Berdasarkan Peran dan Lokasi")
        else:
            st.header("💰 Indonesian Tech Salary Analysis")
            st.subheader("Salary Projections by Role and Location")
        
        # Salary analysis inputs
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if use_indonesian:
                career_field = st.selectbox("Pilih Bidang Karir", list(INDONESIA_SALARY_DATA.keys()))
            else:
                career_field = st.selectbox("Choose Career Field", list(INDONESIA_SALARY_DATA.keys()))
        
        with col2:
            if use_indonesian:
                city = st.selectbox("Pilih Kota", list(INDONESIA_TECH_CITIES.keys()))
            else:
                city = st.selectbox("Choose City", list(INDONESIA_TECH_CITIES.keys()))
        
        with col3:
            if use_indonesian:
                experience = st.selectbox("Level Pengalaman", 
                    ["entry_level", "mid_level", "senior_level", "expert_level"],
                    format_func=lambda x: {
                        "entry_level": "Entry Level (0-2 tahun)",
                        "mid_level": "Mid Level (2-5 tahun)", 
                        "senior_level": "Senior Level (5-10 tahun)",
                        "expert_level": "Expert Level (10+ tahun)"
                    }[x]
                )
            else:
                experience = st.selectbox("Experience Level", 
                    ["entry_level", "mid_level", "senior_level", "expert_level"],
                    format_func=lambda x: x.replace("_", " ").title()
                )
        
        # Display salary chart
        fig = create_indonesia_salary_chart(career_field, city)
        st.plotly_chart(fig, use_container_width=True)
        
        # Current salary details
        if career_field in INDONESIA_SALARY_DATA and experience in INDONESIA_SALARY_DATA[career_field]:
            salary_range = get_adjusted_salary(INDONESIA_SALARY_DATA[career_field][experience], city)
            avg_salary = (salary_range["min"] + salary_range["max"]) / 2
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                if use_indonesian:
                    st.metric("Gaji Minimum", format_idr_currency(salary_range["min"]))
                else:
                    st.metric("Minimum Salary", format_idr_currency(salary_range["min"]))
            
            with col2:
                if use_indonesian:
                    st.metric("Gaji Maksimum", format_idr_currency(salary_range["max"]))
                else:
                    st.metric("Maximum Salary", format_idr_currency(salary_range["max"]))
            
            with col3:
                if use_indonesian:
                    st.metric("Rata-rata", format_idr_currency(avg_salary))
                else:
                    st.metric("Average", format_idr_currency(avg_salary))
            
            with col4:
                city_info = INDONESIA_TECH_CITIES[city]
                if use_indonesian:
                    st.metric("Jumlah Perusahaan", f"{city_info['companies']}+")
                else:
                    st.metric("Companies", f"{city_info['companies']}+")
            
            # PPh 21 Tax Calculator
            if use_indonesian:
                st.subheader("🧮 Kalkulator PPh 21")
                st.write("Simulasi pajak penghasilan tahunan:")
            else:
                st.subheader("🧮 PPh 21 Tax Calculator")
                st.write("Annual income tax simulation:")
            
            annual_salary = avg_salary * 12
            tax_calc = indonesia_pph21_calculator(annual_salary)
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                if use_indonesian:
                    st.metric("Gaji Kotor/Tahun", format_idr_currency(annual_salary))
                else:
                    st.metric("Gross Annual", format_idr_currency(annual_salary))
            with col2:
                if use_indonesian:
                    st.metric("PPh 21/Tahun", format_idr_currency(tax_calc["annual_tax"]))
                else:
                    st.metric("Annual Tax", format_idr_currency(tax_calc["annual_tax"]))
            with col3:
                if use_indonesian:
                    st.metric("Take Home/Tahun", format_idr_currency(tax_calc["net_annual"]))
                else:
                    st.metric("Net Annual", format_idr_currency(tax_calc["net_annual"]))
            with col4:
                if use_indonesian:
                    st.metric("Take Home/Bulan", format_idr_currency(tax_calc["net_monthly"]))
                else:
                    st.metric("Net Monthly", format_idr_currency(tax_calc["net_monthly"]))
    
    # Tab 2: Tech Cities Comparison
    with tab2:
        if use_indonesian:
            st.header("🌆 Perbandingan Kota Tech Indonesia")
        else:
            st.header("🌆 Indonesian Tech Cities Comparison")
        
        # City comparison chart
        fig = create_city_comparison_chart()
        st.plotly_chart(fig, use_container_width=True)
        
        # City details
        if use_indonesian:
            st.subheader("Detail Kota")
        else:
            st.subheader("City Details")
        
        for city, info in INDONESIA_TECH_CITIES.items():
            with st.expander(f"{city} - {info['description']}"):
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    if use_indonesian:
                        st.metric("Perusahaan Tech", f"{info['companies']}+")
                    else:
                        st.metric("Tech Companies", f"{info['companies']}+")
                with col2:
                    if use_indonesian:
                        st.metric("Multiplier Gaji", f"{info['avg_salary_multiplier']:.1f}x")
                    else:
                        st.metric("Salary Multiplier", f"{info['avg_salary_multiplier']:.1f}x")
                with col3:
                    if use_indonesian:
                        st.metric("Budaya Remote", info['remote_culture'])
                    else:
                        st.metric("Remote Culture", info['remote_culture'])
                with col4:
                    if use_indonesian:
                        st.metric("Cost of Living", f"{info['cost_of_living_index']:.1f}x Jakarta")
                    else:
                        st.metric("Cost of Living", f"{info['cost_of_living_index']:.1f}x Jakarta")
    
    # Tab 3: Companies
    with tab3:
        if use_indonesian:
            st.header("🏢 Ekosistem Perusahaan Tech Indonesia")
        else:
            st.header("🏢 Indonesian Tech Company Ecosystem")
        
        display_indonesia_companies()
        
        # Company growth visualization
        company_counts = {category: len(companies) for category, companies in INDONESIA_COMPANIES.items()}
        
        fig = px.pie(
            values=list(company_counts.values()),
            names=list(company_counts.keys()),
            title="Distribusi Perusahaan per Kategori" if use_indonesian else "Company Distribution by Category"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Tab 4: Learning Paths
    with tab4:
        if use_indonesian:
            st.header("🎓 Jalur Pembelajaran Indonesia")
        else:
            st.header("🎓 Indonesian Learning Paths")
        
        display_learning_resources()
        
        # Learning recommendation based on career field
        if use_indonesian:
            st.subheader("Rekomendasi Pembelajaran")
            selected_field = st.selectbox("Pilih target karir:", list(INDONESIA_SALARY_DATA.keys()))
        else:
            st.subheader("Learning Recommendations")
            selected_field = st.selectbox("Choose target career:", list(INDONESIA_SALARY_DATA.keys()))
        
        # Provide specific recommendations based on field
        recommendations = {
            "Artificial Intelligence": ["Algoritma Data Science", "Dicoding AI/ML", "Coursera Deep Learning"],
            "Data Science": ["Algoritma", "Hacktiv8 Data Science", "Python Indonesia Community"],
            "Cybersecurity": ["Dicoding Cybersecurity", "CISSP Certification", "Ethical Hacker Community"],
            "Software Engineering": ["Hacktiv8 Full-stack", "Binar Academy", "JakartaJS Community"],
            "Product Management": ["Google PM Certificate", "Purwadhika PM Track", "Product Management ID"],
            "UI/UX Design": ["BuildWith Angga", "Google UX Certificate", "UXID Community"]
        }
        
        if selected_field in recommendations:
            if use_indonesian:
                st.write("**Rekomendasi untuk", selected_field + ":**")
            else:
                st.write("**Recommendations for", selected_field + ":**")
            
            for i, rec in enumerate(recommendations[selected_field], 1):
                st.write(f"{i}. {rec}")
    
    # Tab 5: Success Stories
    with tab5:
        if use_indonesian:
            st.header("🌟 Kisah Sukses Transisi Karir Indonesia")
        else:
            st.header("🌟 Indonesian Career Transition Success Stories")
        
        display_success_stories()
        
        # Success metrics visualization
        durations = [int(story["duration"].split()[0]) for story in INDONESIA_SUCCESS_STORIES]
        increases = [int(story["salary_increase"].replace("%", "")) for story in INDONESIA_SUCCESS_STORIES]
        names = [story["name"] for story in INDONESIA_SUCCESS_STORIES]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=durations,
            y=increases,
            mode='markers+text',
            text=names,
            textposition="top center",
            marker=dict(size=15, color='red'),
            name='Success Stories'
        ))
        
        fig.update_layout(
            title='Durasi vs Peningkatan Gaji' if use_indonesian else 'Duration vs Salary Increase',
            xaxis_title='Durasi (bulan)' if use_indonesian else 'Duration (months)',
            yaxis_title='Peningkatan Gaji (%)' if use_indonesian else 'Salary Increase (%)',
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Tab 6: Government Programs
    with tab6:
        if use_indonesian:
            st.header("🏛️ Program Pemerintah Indonesia")
        else:
            st.header("🏛️ Indonesian Government Programs")
        
        for program, details in GOVERNMENT_PROGRAMS.items():
            with st.expander(program):
                if use_indonesian:
                    st.write(f"**Deskripsi:** {details['description']}")
                else:
                    st.write(f"**Description:** {details['description']}")
                
                if 'budget' in details:
                    if use_indonesian:
                        st.write(f"**Budget:** {details['budget']}")
                    else:
                        st.write(f"**Budget:** {details['budget']}")
                
                if 'categories' in details:
                    if use_indonesian:
                        st.write(f"**Kategori:** {', '.join(details['categories'])}")
                    else:
                        st.write(f"**Categories:** {', '.join(details['categories'])}")
                
                if 'coverage' in details:
                    if use_indonesian:
                        st.write(f"**Cakupan:** {details['coverage']}")
                    else:
                        st.write(f"**Coverage:** {details['coverage']}")
                
                if 'focus' in details:
                    if use_indonesian:
                        st.write(f"**Fokus:** {details['focus']}")
                    else:
                        st.write(f"**Focus:** {details['focus']}")
        
        # Additional info box
        if use_indonesian:
            st.info("""
            💡 **Tips Mengakses Program Pemerintah:**
            1. Daftar secara online melalui platform resmi
            2. Lengkapi dokumen yang diperlukan
            3. Ikuti seleksi dengan serius
            4. Manfaatkan program secara maksimal
            5. Networking dengan sesama peserta
            """)
        else:
            st.info("""
            💡 **Tips for Accessing Government Programs:**
            1. Register online through official platforms
            2. Complete required documentation
            3. Take selection process seriously
            4. Maximize program utilization
            5. Network with fellow participants
            """)
    
    # Footer
    if use_indonesian:
        st.markdown("---")
        st.markdown("""
        <div style='text-align: center; color: #666;'>
            <p>🇮🇩 Career Shift Analyzer Pro - Indonesia Edition</p>
            <p>Data terbaru: """ + format_indonesian_date() + """</p>
            <p>Sumber: Riset pasar Indonesia 2024-2025</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("---")
        st.markdown("""
        <div style='text-align: center; color: #666;'>
            <p>🇮🇩 Career Shift Analyzer Pro - Indonesia Edition</p>
            <p>Latest data: """ + format_indonesian_date() + """</p>
            <p>Source: Indonesian market research 2024-2025</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()