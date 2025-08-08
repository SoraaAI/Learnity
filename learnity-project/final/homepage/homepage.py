import streamlit as st
import json
import os
from pathlib import Path

st.set_page_config(
    page_title="Learnity - Learning Made Fun",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    div.stButton > button {
        width: 100%;
        padding: 10px;
        background-color: #0d6efd;
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #0b5ed7;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2E86C1;
        font-size: 3.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .sub-header {
        text-align: center;
        color: #5D6D7E;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        font-style: italic;
    }
    
    .user-info-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .menu-button {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        border: none;
        color: white;
        padding: 1rem 2rem;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 1.1rem;
        margin: 0.5rem;
        cursor: pointer;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .menu-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 1rem 0;
    }
    
    .stat-item {
        text-align: center;
        background: rgba(255,255,255,0.1);
        padding: 1rem;
        border-radius: 10px;
        min-width: 100px;
    }
    
    .login-form {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }
    
    .sidebar .stSelectbox > div > div {
        background-color: #e8f4f8;
    }
</style>
""", unsafe_allow_html=True)

def load_user_data():
    """Load user data from JSON file"""
    try:
        with open('database/user_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("User database not found! Please check if 'database/user_data.json' exists.")
        return None
    except json.JSONDecodeError:
        st.error("Error reading user database. Please check the JSON format.")
        return None

def authenticate_user(username_or_id, password):
    """Authenticate user with username/userid and password"""
    users = load_user_data()
    if users is None:
        return None

    for user in users:
        if (user.get("username") == username_or_id or 
            user.get("userid") == username_or_id) and \
           user.get("password") == password:
            return user
    return None

def display_user_info(user_data):
    """Display user information in a styled card"""
    st.markdown(f"""
    <div class="user-info-card">
        <p><strong>Halo,</strong> {user_data['username']}! Nih, data kamu saat ini:<br></p>
        <p><strong> - Highest Score:</strong> {user_data['highest_score']}</p>
        <p><strong> - Coins:</strong> {user_data['coins']}</p>
        <p><strong> - MBTI Type:</strong> {user_data['mbti_display']}</p>
        <p><strong> - Role:</strong> {user_data['user_role'].title()}</p>
    </div>
    """, unsafe_allow_html=True)

def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'user_data' not in st.session_state:
        st.session_state.user_data = None

    with st.sidebar:
        if not st.session_state.logged_in:
            st.markdown("### 🔐 Login to Learnity")
            with st.container():
                username_input = st.text_input(
                    "Username or User ID",
                    placeholder="Enter your username or user ID",
                    help="You can use either your username or user ID to login"
                )
                
                password_input = st.text_input(
                    "Password",
                    placeholder="Enter your password"
                )
                
                if st.button("🚀 Login", use_container_width=True):
                    if username_input and password_input:
                        user_data = authenticate_user(username_input, password_input)
                        if user_data:
                            st.session_state.logged_in = True
                            st.session_state.user_data = user_data
                            st.success("Login successful!")
                            st.rerun()
                        else:
                            st.error("Invalid credentials. Please try again.")
                    else:
                        st.warning("Please fill in all fields.")
                if st.button("🚀 Buat akun", use_container_width=True):
                    pass
        else:
            st.success(f"✅ Logged in as: **{st.session_state.user_data['username']}**")
            with st.sidebar.expander("Data kamu", expanded=True):
                st.markdown(f"### Welcome, {st.session_state.user_data['username']}!")
                # st.markdown(f"Highest Score: {st.session_state.user_data['highest_score']}")
                st.markdown(f"MBTI Type: {st.session_state.user_data['mbti_display']}")
                st.markdown(f"Coins: {st.session_state.user_data['coins']}")
                mbti = st.session_state.user_data['mbti'].lower()
                mbti_image_path = f"image/char/{mbti}_char.png"
                if os.path.exists(mbti_image_path):
                    st.image(mbti_image_path, use_container_width=True)
                else:
                    st.sidebar.warning(f"⚠️ Gambar karakter untuk MBTI '{mbti.upper()}' tidak ditemukan di {mbti_image_path}.")
            if st.button("🧾 Buat akun baru", use_container_width=True):
                pass
            if st.button("🚪 Logout", use_container_width=True):
                st.session_state.logged_in = False
                st.session_state.user_data = None
                st.rerun()

    if st.session_state.logged_in:
        st.markdown('<h1 class="main-header">🎓 Learnity</h1>', unsafe_allow_html=True)
        st.markdown('<p class="sub-header">Your Personalized Learning Journey Starts Here</p>', unsafe_allow_html=True)
        display_user_info(st.session_state.user_data)
        st.markdown("### 🎯 Main Menu")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("📚 Chat dengan AI Leanity.", use_container_width=True):
                os.system("PLACEHOLDER_START_LEARNING")
                st.info("Launching learning module...")
            
            if st.button("🎮 Latihan dengan bermain kuis.", use_container_width=True):
                os.system("PLACEHOLDER_PRACTICE_QUIZ")
                st.info("Opening practice quiz...")
            
            if st.button("📊 Rencanakan sesuatu.", use_container_width=True):
                os.system("PLACEHOLDER_VIEW_PROGRESS")
                st.info("Loading progress dashboard...")
            
            if st.button("🧾 Absen dulu yuk! Sekalian cek tugas.", use_container_width=True):
                os.system("PLACEHOLDER_VIEW_PROGRESS")
                st.info("Loading progress dashboard...")
        
        with col2:
            if st.button("🏪 Belanjakan atau gunakan koinmu disini!", use_container_width=True):
                os.system("PLACEHOLDER_COIN_SHOP")
                st.info("Opening coin shop...")
            
            if st.button("⚙️ Upload file dengan tracking tangan atau langsung.", use_container_width=True):
                os.system("PLACEHOLDER_SETTINGS")
                st.info("Opening settings...")
            
            if st.button("📷 Analisa suatu foto.", use_container_width=True):
                os.system("PLACEHOLDER_ABOUT")
                st.info("Loading about page...")
            
            if st.button("ℹ️ Tentang Learnity", use_container_width=True):
                os.system("PLACEHOLDER_ABOUT")
                st.info("Loading about page...")
        
        st.markdown("---")
        st.markdown("### 🌟 Quick Actions")
        
        col3, col4, col5 = st.columns(3)
        
        with col3:
            if st.button("🎯 Daily Challenge", use_container_width=True):
                os.system("PLACEHOLDER_DAILY_CHALLENGE")
                st.info("Loading daily challenge...")
        
        with col4:
            if st.button("🏆 Leaderboard", use_container_width=True):
                os.system("PLACEHOLDER_LEADERBOARD")
                st.info("Opening leaderboard...")
        
        with col5:
            if st.button("👥 Community", use_container_width=True):
                os.system("PLACEHOLDER_COMMUNITY")
                st.info("Connecting to community...")
        
        st.markdown("---")
        st.markdown(
            '<p style="text-align: center; color: #7F8C8D; font-size: 0.9rem;">✨ Keep learning, keep growing! ✨</p>',
            unsafe_allow_html=True
        )
    
    else:
        st.markdown('<h1 class="main-header">🎓 Welcome to Learnity</h1>', unsafe_allow_html=True)
        st.markdown('<p class="sub-header">Please login from the sidebar to access your learning dashboard</p>', unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            ### 📚 Personalized Learning
            Adaptive content based on your MBTI type and learning preferences
            """)
        
        with col2:
            st.markdown("""
            ### 🎮 Gamified Experience
            Earn coins, unlock achievements, and track your progress
            """)
        
        with col3:
            st.markdown("""
            ### 🏆 Progress Tracking
            Monitor your highest scores and learning milestones
            """)
        
        st.markdown("---")
        st.markdown(
            '<p style="text-align: center; color: #E74C3C; font-size: 1.1rem; font-weight: bold;">🔒 Please login to continue</p>',
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()