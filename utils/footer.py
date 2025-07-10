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
        
        .
