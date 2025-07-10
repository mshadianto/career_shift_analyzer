# utils/footer.py - Enhanced with Dark Purple Neon Theme
import streamlit as st
from datetime import datetime
import os

def get_app_version():
    """Get application version"""
    try:
        env_version = os.getenv('APP_VERSION')
        if env_version:
            return env_version
        base_version = "2.0"
        build_number = datetime.now().strftime("%y%m%d")
        return f"{base_version}.{build_number}"
    except Exception:
        return "2.0.0"

def render_universal_footer():
    """Render comprehensive universal footer with dark purple neon theme"""
    current_year = datetime.now().year
    last_updated = datetime.now().strftime("%B %d, %Y")
    version = get_app_version()
    
    # Footer CSS with dark purple neon theme
    st.markdown("""
    <style>
        .universal-footer {
            background: linear-gradient(135deg, rgba(13, 13, 13, 0.95), rgba(26, 14, 46, 0.95));
            border: 2px solid #8b45ff;
            color: #e0e0ff;
            padding: 4rem 2rem;
            border-radius: 25px;
            margin-top: 4rem;
            box-shadow: 
                0 0 40px rgba(139, 69, 255, 0.4),
                inset 0 0 40px rgba(139, 69, 255, 0.1);
            backdrop-filter: blur(20px);
            position: relative;
            overflow: hidden;
        }
        
        .universal-footer::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(circle at 20% 50%, rgba(139, 69, 255, 0.05) 0%, transparent 50%),
                radial-gradient(circle at 80% 20%, rgba(255, 69, 255, 0.05) 0%, transparent 50%);
            animation: footerGlow 8s ease-in-out infinite;
            pointer-events: none;
        }
        
        @keyframes footerGlow {
            0%, 100% { opacity: 0.5; }
            50% { opacity: 1; }
        }
        
        .footer-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 3rem;
            margin-bottom: 3rem;
            position: relative;
            z-index: 1;
        }
        
        .footer-section {
            position: relative;
            z-index: 1;
        }
        
        .footer-section h4 {
            color: #ff45ff;
            margin-bottom: 1.5rem;
            font-size: 1.2em;
            font-family: 'Orbitron', monospace;
            text-shadow: 0 0 10px #ff45ff;
            border-bottom: 2px solid rgba(255, 69, 255, 0.3);
            padding-bottom: 0.5rem;
        }
        
        .disclaimer-box {
            background: rgba(139, 69, 255, 0.1);
            border: 1px solid rgba(139, 69, 255, 0.3);
            border-radius: 12px;
            padding: 1.5rem;
            margin: 1rem 0;
            font-size: 0.9em;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }
        
        .disclaimer-box:hover {
            background: rgba(139, 69, 255, 0.15);
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(139, 69, 255, 0.2);
        }
        
        .team-section {
            background: rgba(139, 69, 255, 0.1);
            border: 2px solid #8b45ff;
            border-radius: 20px;
            padding: 2.5rem;
            margin: 2rem 0;
            backdrop-filter: blur(15px);
            transition: all 0.4s ease;
        }
        
        .team-section:hover {
            border-color: #ff45ff;
            transform: translateY(-5px);
            box-shadow: 0 15px 30px rgba(255, 69, 255, 0.3);
        }
        
        .team-members {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin: 1.5rem 0;
            flex-wrap: wrap;
        }
        
        .team-member {
            background: rgba(255, 69, 255, 0.1);
            padding: 1.5rem 2rem;
            border-radius: 25px;
            border: 2px solid #ff45ff;
            transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
            backdrop-filter: blur(10px);
            text-align: center;
            min-width: 160px;
            position: relative;
            overflow: hidden;
        }
        
        .team-member::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 69, 255, 0.2), transparent);
            transition: left 0.6s;
        }
        
        .team-member:hover::before {
            left: 100%;
        }
        
        .team-member:hover {
            transform: translateY(-8px) scale(1.05);
            border-color: #8b45ff;
            box-shadow: 0 15px 30px rgba(255, 69, 255, 0.4);
            background: rgba(255, 69, 255, 0.15);
        }
        
        .team-member strong {
            color: #ff45ff;
            font-size: 1.1em;
            display: block;
            margin-bottom: 0.5rem;
            text-shadow: 0 0 5px #ff45ff;
            font-family: 'Orbitron', monospace;
        }
        
        .footer-bottom {
            border-top: 2px solid rgba(139, 69, 255, 0.3);
            padding-top: 2rem;
            text-align: center;
            font-size: 0.9em;
            color: #e0e0ff;
            position: relative;
            z-index: 1;
        }
        
        .status-indicator {
            display: inline-block;
            width: 10px;
            height: 10px;
            background: #00ff88;
            border-radius: 50%;
            margin-right: 0.8rem;
            animation: pulse 2s infinite;
            box-shadow: 0 0 10px #00ff88;
        }
        
        @keyframes pulse {
            0% { opacity: 1; transform: scale(1); }
            50% { opacity: 0.5; transform: scale(1.2); }
            100% { opacity: 1; transform: scale(1); }
        }
        
        .footer-link {
            color: #ff45ff;
            text-decoration: none;
            transition: all 0.3s ease;
            padding: 0.2rem 0.5rem;
            border-radius: 5px;
        }
        
        .footer-link:hover {
            color: #8b45ff;
            background: rgba(255, 69, 255, 0.1);
            text-shadow: 0 0 10px #ff45ff;
            transform: translateY(-1px);
        }
        
        .warning-box {
            background: rgba(255, 193, 7, 0.1);
            border: 2px solid rgba(255, 193, 7, 0.3);
            border-radius: 12px;
            padding: 1.5rem;
            margin: 1rem 0;
            color: #ffcc00;
        }
        
        .danger-box {
            background: rgba(255, 69, 69, 0.1);
            border: 2px solid rgba(255, 69, 69, 0.3);
            border-radius: 12px;
            padding: 1.5rem;
            margin: 1rem 0;
            color: #ff4545;
        }
        
        .info-box {
            background: rgba(0, 255, 136, 0.1);
            border: 2px solid rgba(0, 255, 136, 0.3);
            border-radius: 12px;
            padding: 1.5rem;
            margin: 1rem 0;
            color: #00ff88;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .universal-footer {
                padding: 3rem 1rem;
                border-radius: 15px;
            }
            .footer-grid {
                grid-template-columns: 1fr;
                gap: 2rem;
            }
            .team-members {
                flex-direction: column;
                align-items: center;
            }
            .team-member {
                min-width: 200px;
            }
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Footer HTML content
    footer_html = f"""
    <div class="universal-footer">
        <div class="footer-grid">
            <!-- Platform Information -->
            <div class="footer-section">
                <h4>🚀 Career Shift Analyzer Pro</h4>
                <p><span class="status-indicator"></span><strong>Status:</strong> Online & Active</p>
                <p><strong>Version:</strong> v{version}</p>
                <p><strong>Last Updated:</strong> {last_updated}</p>
                <p><strong>Platform:</strong> Streamlit Cloud</p>
                <p><strong>AI Model:</strong> Meta Llama 3.2</p>
                
                <div class="team-section">
                    <h5 style="color: #ff45ff; margin-bottom: 1.5rem; text-align: center; font-size: 1.1em;">👥 Development Team</h5>
                    <div class="team-members">
                        <div class="team-member">
                            <strong>🎯 MS Hadianto</strong>
                            <span style="font-size: 0.9em; color: #c0c0ff;">Lead Project &<br>Architecture</span>
                        </div>
                        <div class="team-member">
                            <strong>🤝 Faby</strong>
                            <span style="font-size: 0.9em; color: #c0c0ff;">Co-Lead &<br>Development</span>
                        </div>
                    </div>
                    <p style="margin-top: 1.5rem; font-size: 0.9em; color: #c0c0ff; text-align: center;">
                        <em>Collaborative innovation for empowering career advancement worldwide</em>
                    </p>
                </div>
            </div>
            
            <!-- AI & Career Advice Disclaimers -->
            <div class="footer-section">
                <h4>⚖️ Important Legal Disclaimers</h4>
                
                <div class="danger-box">
                    <p style="margin-bottom: 1rem;"><strong>⚠️ CRITICAL - Please Read Carefully:</strong></p>
                    <ul style="list-style: none; padding: 0; font-size: 0.85em; line-height: 1.6;">
                        <li>• <strong>NOT PROFESSIONAL ADVICE:</strong> All content is for informational and educational purposes only</li>
                        <li>• <strong>AI LIMITATIONS:</strong> AI responses are automated and may contain errors or outdated information</li>
                        <li>• <strong>NO GUARANTEES:</strong> Career outcomes, salary ranges, and job prospects cannot be guaranteed</li>
                        <li>• <strong>INDIVIDUAL RESULTS VARY:</strong> Success depends on personal circumstances, market conditions, and effort</li>
                        <li>• <strong>VERIFY INFORMATION:</strong> Always cross-check with official industry sources and professionals</li>
                        <li>• <strong>CONSULT PROFESSIONALS:</strong> This platform does not replace qualified career counselors, financial advisors, or legal experts</li>
                    </ul>
                </div>
                
                <div class="warning-box">
                    <p><strong>🤖 AI-Specific Disclaimers:</strong></p>
                    <ul style="list-style: none; padding: 0; font-size: 0.85em; line-height: 1.5;">
                        <li>• AI responses are generated based on training data and may not reflect current market conditions</li>
                        <li>• The AI cannot provide personalized professional advice for your specific situation</li>
                        <li>• AI-generated content should be treated as general guidance, not definitive career strategy</li>
                        <li>• Technology and job market landscapes change rapidly; verify current trends independently</li>
                    </ul>
                </div>
            </div>
            
            <!-- Privacy & Data Protection -->
            <div class="footer-section">
                <h4>🔒 Privacy & Data Protection</h4>
                
                <div class="info-box">
                    <p style="margin-bottom: 1rem;"><strong>🛡️ Your Data Security & Privacy:</strong></p>
                    <ul style="list-style: none; padding: 0; font-size: 0.85em; line-height: 1.6;">
                        <li>• <strong>NO PERMANENT STORAGE:</strong> Personal data is not permanently stored on our servers</li>
                        <li>• <strong>SESSION-BASED:</strong> Chat conversations and assessments are temporary and session-based only</li>
                        <li>• <strong>LOCAL PROCESSING:</strong> Skill assessments processed locally in your browser when possible</li>
                        <li>• <strong>THIRD-PARTY APIs:</strong> AI features use external APIs governed by separate privacy policies</li>
                        <li>• <strong>AUTO-CLEAR:</strong> All session data automatically cleared when browser is closed</li>
                        <li>• <strong>NO TRACKING:</strong> We do not use tracking cookies or collect analytics beyond basic usage</li>
                        <li>• <strong>DATA RETENTION:</strong> No conversation history retained after session ends</li>
                        <li>• <strong>ENCRYPTION:</strong> All data transmission is encrypted using industry-standard protocols</li>
                    </ul>
                </div>
                
                <div class="disclaimer-box">
                    <p><strong>🌐 External Services:</strong></p>
                    <p style="font-size: 0.85em;">When using AI chat features, your messages are processed by OpenRouter/Meta Llama 3.2. Please review their privacy policies for external data handling practices.</p>
                </div>
            </div>
            
            <!-- Technical & Limitation Disclaimers -->
            <div class="footer-section">
                <h4>🛠️ Technical Information & Limitations</h4>
                
                <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.5rem; margin: 1rem 0;">
                    <div style="background: rgba(139, 69, 255, 0.1); padding: 0.5rem; border-radius: 8px; text-align: center; font-size: 0.8em; border: 1px solid #8b45ff;">🐍 Python 3.11+</div>
                    <div style="background: rgba(139, 69, 255, 0.1); padding: 0.5rem; border-radius: 8px; text-align: center; font-size: 0.8em; border: 1px solid #8b45ff;">⚡ Streamlit 1.28+</div>
                    <div style="background: rgba(139, 69, 255, 0.1); padding: 0.5rem; border-radius: 8px; text-align: center; font-size: 0.8em; border: 1px solid #8b45ff;">📊 Plotly 5.17+</div>
                    <div style="background: rgba(139, 69, 255, 0.1); padding: 0.5rem; border-radius: 8px; text-align: center; font-size: 0.8em; border: 1px solid #8b45ff;">🤖 Llama 3.2</div>
                </div>
                
                <div class="disclaimer-box">
                    <p style="margin-bottom: 1rem;"><strong>⚙️ System Limitations:</strong></p>
                    <ul style="list-style: none; padding: 0; font-size: 0.85em; line-height: 1.5;">
                        <li>• Platform availability subject to cloud hosting uptime</li>
                        <li>• AI responses depend on external API availability</li>
                        <li>• Features may be temporarily unavailable during maintenance</li>
                        <li>• Response times may vary based on server load</li>
                        <li>• Some features require stable internet connection</li>
                        <li>• Browser compatibility: Chrome, Firefox, Safari, Edge (latest versions)</li>
                    </ul>
                </div>
                
                <div style="margin-top: 1.5rem; font-size: 0.9em;">
                    <p><strong>🏗️ Architecture:</strong></p>
                    <p>• <strong>Hosting:</strong> Streamlit Cloud Platform</p>
                    <p>• <strong>AI Backend:</strong> OpenRouter with Meta Llama 3.2</p>
                    <p>• <strong>Data Visualization:</strong> Plotly Interactive Charts</p>
                    <p>• <strong>Updates:</strong> Continuous deployment pipeline</p>
                    <p>• <strong>Monitoring:</strong> Real-time performance tracking</p>
                </div>
            </div>
        </div>
        
        <!-- Footer Bottom -->
        <div class="footer-bottom">
            <p style="font-size: 1.1em; margin-bottom: 1rem; font-weight: bold;">
                <strong>© {current_year} Career Shift Analyzer Pro v{version}</strong>
            </p>
            <p style="margin: 0.8rem 0; font-size: 1em;">
                <strong>👥 Proudly Developed by:</strong> 
                <span style="color: #ff45ff; font-weight: bold;">MS Hadianto</span> (Lead Project) & 
                <span style="color: #ff45ff; font-weight: bold;">Faby</span> (Co-Lead)
            </p>
            <p style="margin: 1.5rem 0; font-size: 0.85em; line-height: 1.6; color: #c0c0ff; max-width: 800px; margin-left: auto; margin-right: auto;">
                <em><strong>COMPREHENSIVE LEGAL NOTICE:</strong> This platform provides general career guidance and educational content for informational purposes only. 
                It is not a substitute for professional career counseling, financial planning, legal advice, or job placement services. 
                All AI-generated content should be verified independently. Users acknowledge that career outcomes depend on individual effort, market conditions, and numerous external factors. 
                The developers disclaim all liability for decisions made based on platform content. 
                Use of this platform constitutes acceptance of these terms and all disclaimers provided herein.</em>
            </p>
            <p style="margin-top: 2rem; font-size: 0.95em;">
                🌟 <strong>Open Source Project</strong> | 
                <a href="https://github.com/mshadianto/career_shift_analyzer" target="_blank" class="footer-link">
                    📚 View on GitHub
                </a> | 
                <a href="mailto:support@careershiftanalyzer.com" class="footer-link">
                    📧 Contact Support
                </a> | 
                <a href="#" class="footer-link" onclick="alert('Terms of Service: Please review all disclaimers above. By using this platform, you acknowledge and accept these terms.')">
                    📋 Terms of Service
                </a>
            </p>
            <p style="margin-top: 1rem; font-size: 1em; color: #ff45ff; font-weight: 500;">
                Built with ❤️ for empowering career advancement worldwide
            </p>
            <p style="margin-top: 1rem; font-size: 0.8em; color: #c0c0ff;">
                🔒 Your privacy is protected • 🤖 AI-powered insights • 🌍 Global career guidance • ⚡ Real-time data
            </p>
        </div>
    </div>
    """
    
    # Add some spacing before footer
    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Render the footer
    st.markdown(footer_html, unsafe_allow_html=True)

def render_simple_footer():
    """Render a simplified version of the footer with dark theme"""
    current_year = datetime.now().year
    version = get_app_version()
    
    st.markdown("---")
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem; background: linear-gradient(135deg, rgba(139, 69, 255, 0.1), rgba(255, 69, 255, 0.1)); 
         border: 1px solid #8b45ff; border-radius: 15px; margin-top: 2rem;">
        <p style="margin: 0; color: #e0e0ff;">
            <strong>© {current_year} Career Shift Analyzer Pro v{version}</strong><br>
            ⚠️ For informational purposes only • Not professional advice • Verify all information independently<br>
            Built by <strong style="color: #ff45ff;">MS Hadianto</strong> & <strong style="color: #ff45ff;">Faby</strong> • 
            <a href="https://github.com/mshadianto/career_shift_analyzer" style="color: #8b45ff;">GitHub</a>
        </p>
    </div>
    """, unsafe_allow_html=True)

def add_disclaimer_warning():
    """Add a quick disclaimer warning at the top of sensitive pages"""
    st.warning("""
    ⚠️ **Important Disclaimer**: This platform provides general career guidance for educational purposes only. 
    It is not a substitute for professional career counseling. AI responses may contain errors. 
    Always verify information independently and consult qualified professionals for personalized advice.
    """)
