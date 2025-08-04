import subprocess
import sys
import importlib
import time
from typing import List, Tuple, Dict

try:
    import streamlit as st
except ImportError:
    subprocess.run([sys.executable, "-m", "pip", "install", "streamlit==1.45.1"])

st.set_page_config(
    page_title="Learnity Dependencies",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 20px;
        margin-bottom: 2rem;
        color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }
    .status-installed {
        background: linear-gradient(135deg, #4CAF50, #45a049);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        display: inline-block;
        margin: 0.2rem;
        box-shadow: 0 2px 10px rgba(76, 175, 80, 0.3);
    }
    .status-missing {
        background: linear-gradient(135deg, #f44336, #d32f2f);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        display: inline-block;
        margin: 0.2rem;
        box-shadow: 0 2px 10px rgba(244, 67, 54, 0.3);
    }
    .status-checking {
        background: linear-gradient(135deg, #ff9800, #f57c00);
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: bold;
        display: inline-block;
        margin: 0.2rem;
        animation: pulse 1.5s infinite;
        box-shadow: 0 2px 10px rgba(255, 152, 0, 0.3);
    }
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.7; }
        100% { opacity: 1; }
    }
    .package-card {
        border-radius: 15px;
        padding: 1rem;
        margin: 0.5rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border: 2px solid #667eea;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .package-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
        border-color: #5a6fd8;
    }
    .package-card.missing {
        border-color: #f44336;
    }
    .package-card.missing:hover {
        border-color: #d32f2f;
    }
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: bold;
        font-size: 1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }
    .stProgress > div > div > div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    .info-box {
        background: linear-gradient(135deg, #e3f2fd, #bbdefb);
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 5px solid #2196f3;
    }
    .stats-container {
        display: flex;
        justify-content: space-around;
        margin: 2rem 0;
        flex-wrap: wrap;
    }
    .stat-card {
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        min-width: 150px;
        margin: 0.5rem;
        border: 2px solid #667eea;
        transition: transform 0.3s ease, border-color 0.3s ease;
    }
    .stat-card:hover {
        transform: translateY(-2px);
        border-color: #5a6fd8;
    }
    .stat-number {
        font-size: 2rem;
        font-weight: bold;
        color: #667eea;
    }
    .stat-label {
        color: #666;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

modules_to_check = [
    ("google-generativeai", "google.generativeai"),
    ("SpeechRecognition", "speech_recognition"),
    ("pyttsx3", "pyttsx3"),
    ("pyaudio", "pyaudio"),
    ("requests", "requests"),
    ("streamlit", "streamlit"),
    ("Pillow", "PIL"),
    ("pywebview", "webview"),
    ("opencv-python", "cv2"),
    ("mediapipe", "mediapipe"),
    ("pygetwindow", "pygetwindow"),
    ("pyautogui", "pyautogui"),
    ("flask", "flask"),
    ("numpy", "numpy"),
    ("ErrorTest", "Err")
]

def check_package_status(package_name: str, import_name: str) -> bool:
    try:
        importlib.import_module(import_name)
        return True
    except ImportError:
        return False

def install_package(package_name: str) -> Tuple[bool, str]:
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", package_name],
            capture_output=True,
            text=True,
            check=True
        )
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, e.stderr

def get_package_statistics(modules: List[Tuple[str, str]]) -> Dict[str, int]:
    installed = sum(1 for pkg_name, import_name in modules if check_package_status(pkg_name, import_name))
    missing = len(modules) - installed
    return {
        "total": len(modules),
        "installed": installed,
        "missing": missing,
        "percentage": int((installed / len(modules)) * 100) if modules else 0
    }

if 'package_status' not in st.session_state:
    st.session_state.package_status = {}
if 'checking' not in st.session_state:
    st.session_state.checking = False
if 'installing' not in st.session_state:
    st.session_state.installing = False

st.markdown("""
<div class="main-header">
    <h1>- Learnity Installer -</h1>
    <p>Sebelum mulai, ayo cek dan install dependensi dulu yuk! Ini bertujuan agar Learnity dapat berjalan dengan baik.</p>
</div>
""", unsafe_allow_html=True)

stats = get_package_statistics(modules_to_check)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number">{stats['total']}</div>
        <div class="stat-label">Total Packages</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number" style="color: #4CAF50;">{stats['installed']}</div>
        <div class="stat-label">Installed</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number" style="color: #f44336;">{stats['missing']}</div>
        <div class="stat-label">Missing</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="stat-card">
        <div class="stat-number" style="color: #667eea;">{stats['percentage']}%</div>
        <div class="stat-label">Complete</div>
    </div>
    """, unsafe_allow_html=True)

if stats['total'] > 0:
    progress = stats['installed'] / stats['total']
    st.progress(progress)

st.markdown("---")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    button_col1, button_col2 = st.columns(2)
    
    with button_col1:
        if st.button("🔍 Check Dependencies", disabled=st.session_state.checking or st.session_state.installing, use_container_width=True):
            st.session_state.checking = True
            st.session_state.package_status = {}
            progress_placeholder = st.empty()
            status_container = st.container()
            with progress_placeholder:
                st.info("🔄 Checking dependencies... Please wait.")
                check_progress = st.progress(0)
            for i, (package_name, import_name) in enumerate(modules_to_check):
                progress = (i + 1) / len(modules_to_check)
                check_progress.progress(progress)
                is_installed = check_package_status(package_name, import_name)
                st.session_state.package_status[package_name] = is_installed
            progress_placeholder.empty()
            st.session_state.checking = False
            st.success("✅ Dependency check completed!")
            st.rerun()

    with button_col2:
        missing_packages = [pkg for pkg, status in st.session_state.package_status.items() if not status]
        
        if st.button("📦 Install Missing", disabled=st.session_state.checking or st.session_state.installing or not missing_packages, use_container_width=True):
            if not missing_packages:
                st.warning("⚠️ Please check dependencies first!")
            else:
                st.session_state.installing = True
                install_info = st.empty()
                install_progress = st.progress(0)
                successful_installs = 0
                failed_installs = []
                for i, package_name in enumerate(missing_packages):
                    progress = i / len(missing_packages)
                    install_progress.progress(progress)
                    install_info.info(f"🔄 Installing {package_name}... ({i+1}/{len(missing_packages)})")
                    original_package = next((pkg for pkg, _ in modules_to_check if pkg == package_name), package_name)
                    success, message = install_package(original_package)
                    if success:
                        successful_installs += 1
                        st.session_state.package_status[package_name] = True
                    else:
                        failed_installs.append((package_name, message))
                install_progress.progress(1.0)
                install_info.empty()
                install_progress.empty()
                if successful_installs > 0:
                    st.success(f"✅ Successfully installed {successful_installs} package(s)!")
                if failed_installs:
                    st.error(f"❌ Failed to install {len(failed_installs)} package(s):")
                    for pkg, error in failed_installs:
                        with st.expander(f"Error installing {pkg}"):
                            st.code(error)
                st.session_state.installing = False
                st.rerun()

if st.session_state.package_status:
    st.markdown("## 📋 Package Status")
    for package_name, import_name in modules_to_check:
        if package_name in st.session_state.package_status:
            is_installed = st.session_state.package_status[package_name]
            status_class = "status-installed" if is_installed else "status-missing"
            status_text = "✅ Installed" if is_installed else "❌ Missing"
            icon = "📦" if is_installed else "📭"
            card_class = "package-card" if is_installed else "package-card missing"
            st.markdown(f"""
            <div class="{card_class}">
                {icon} <strong>{package_name}</strong> 
                <span style="color: #666; font-size: 0.9rem;">(imports as: {import_name})</span>
                <br>
                <span class="{status_class}">{status_text}</span>
            </div>
            """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>💡 <strong>Pro Tip:</strong> Make sure you have the necessary permissions to install packages.</p>
    <p>Some packages like <code>pyaudio</code> might require additional system dependencies.</p>
</div>
""", unsafe_allow_html=True)
