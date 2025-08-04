import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
import os
import shutil
from datetime import datetime
import tempfile
import socket
import threading
import time

try:
    import requests
    import flask
    from flask import Flask, request, jsonify, send_file
    HTTP_AVAILABLE = True
except ImportError:
    HTTP_AVAILABLE = False

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

UPLOAD_DIR = "uploaded_files"
DOWNLOAD_DIR = "downloads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "127.0.0.1"

def get_uploaded_files():
    files = []
    if os.path.exists(UPLOAD_DIR):
        files = [f for f in os.listdir(UPLOAD_DIR) if os.path.isfile(os.path.join(UPLOAD_DIR, f))]
    return files

def upload_file_to_localhost(file_data, filename):
    filepath = os.path.join(UPLOAD_DIR, filename)
    with open(filepath, 'wb') as f:
        f.write(file_data)
    return filepath

def download_file_from_localhost(filename):
    src_path = os.path.join(UPLOAD_DIR, filename)
    dst_path = os.path.join(DOWNLOAD_DIR, filename)
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        return dst_path
    return None

def delete_uploaded_file(filename):
    filepath = os.path.join(UPLOAD_DIR, filename)
    if os.path.exists(filepath):
        os.remove(filepath)
        return True
    return False

def upload_file_to_localhost_http(file_data, filename, server_url):
    if not HTTP_AVAILABLE:
        return False, "HTTP libraries not available"
    try:
        files = {'file': (filename, file_data)}
        response = requests.post(f"{server_url}/upload", files=files, timeout=10)
        return response.status_code == 200, response.json().get('message', 'Upload failed')
    except Exception as e:
        return False, str(e)

def download_file_from_localhost_http(filename, server_url):
    if not HTTP_AVAILABLE:
        return False, "HTTP libraries not available"
    try:
        response = requests.get(f"{server_url}/download/{filename}", timeout=10)
        if response.status_code == 200:
            dst_path = os.path.join(DOWNLOAD_DIR, filename)
            with open(dst_path, 'wb') as f:
                f.write(response.content)
            return True, f"Downloaded {filename}"
        else:
            return False, "File not found"
    except Exception as e:
        return False, str(e)

def get_files_from_localhost_http(server_url):
    if not HTTP_AVAILABLE:
        return []
    try:
        response = requests.get(f"{server_url}/files", timeout=10)
        if response.status_code == 200:
            return response.json().get('files', [])
        return []
    except Exception:
        return []

def create_flask_server():
    if not HTTP_AVAILABLE:
        return None
        
    app = Flask(__name__)
    
    @app.route('/upload', methods=['POST'])
    def upload_file():
        try:
            if 'file' not in request.files:
                return jsonify({'error': 'No file provided'}), 400
            file = request.files['file']
            if file.filename == '':
                return jsonify({'error': 'No file selected'}), 400
            existing_files = get_uploaded_files()
            if len(existing_files) > 0:
                return jsonify({'error': 'File already exists. Delete first.'}), 400
            filepath = os.path.join(UPLOAD_DIR, file.filename)
            file.save(filepath)
            return jsonify({'message': f'File {file.filename} uploaded successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @app.route('/download/<filename>', methods=['GET'])
    def download_file(filename):
        try:
            filepath = os.path.join(UPLOAD_DIR, filename)
            if os.path.exists(filepath):
                dst_path = os.path.join(DOWNLOAD_DIR, filename)
                shutil.copy2(filepath, dst_path)
                return send_file(filepath, as_attachment=True)
            else:
                return jsonify({'error': 'File not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @app.route('/files', methods=['GET'])
    def list_files():
        try:
            files = get_uploaded_files()
            return jsonify({'files': files}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @app.route('/delete/<filename>', methods=['DELETE'])
    def delete_file(filename):
        try:
            if delete_uploaded_file(filename):
                return jsonify({'message': f'File {filename} deleted successfully'}), 200
            else:
                return jsonify({'error': 'File not found'}), 404
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return app

def start_flask_server(app, host, port):
    app.run(host=host, port=port, debug=False, use_reloader=False)

class FingerDetector:
    def __init__(self):
        self.hands = mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.3
        )
        
    def count_fingers(self, landmarks):
        if not landmarks:
            return 0
        tip_ids = [4, 8, 12, 16, 20]
        pip_ids = [3, 6, 10, 14, 18]
        mcp_ids = [2, 5, 9, 13, 17]
        fingers = []
        if landmarks[tip_ids[0]].x > landmarks[pip_ids[0]].x:
            fingers.append(1)
        else:
            fingers.append(0)
        for i in range(1, 5):
            tip_y = landmarks[tip_ids[i]].y
            pip_y = landmarks[pip_ids[i]].y
            mcp_y = landmarks[mcp_ids[i]].y
            if tip_y < pip_y - 0.02:
                fingers.append(1)
            else:
                fingers.append(0)
        return sum(fingers)
    
    def detect_gesture(self, frame):
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                finger_count = self.count_fingers(hand_landmarks.landmark)
                return finger_count, True
        return 0, False

def main():
    st.set_page_config(page_title="Finger Detection File Manager", layout="wide")
    
    if 'detector' not in st.session_state:
        st.session_state.detector = FingerDetector()
    if 'camera_running' not in st.session_state:
        st.session_state.camera_running = False
    if 'uploaded_file_data' not in st.session_state:
        st.session_state.uploaded_file_data = None
    if 'uploaded_filename' not in st.session_state:
        st.session_state.uploaded_filename = None
    if 'server_running' not in st.session_state:
        st.session_state.server_running = False
    if 'server_thread' not in st.session_state:
        st.session_state.server_thread = None
    if 'local_ip' not in st.session_state:
        st.session_state.local_ip = get_local_ip()
    if 'server_port' not in st.session_state:
        st.session_state.server_port = 5000
    if 'use_http' not in st.session_state:
        st.session_state.use_http = False
    if 'detection_mode' not in st.session_state:
        st.session_state.detection_mode = "Gesture Detection"
    
    st.sidebar.subheader("🎮 Operation Mode")
    detection_mode = st.sidebar.radio(
        "Choose Mode:",
        ["Gesture Detection", "Manual Mode"],
        index=0 if st.session_state.detection_mode == "Gesture Detection" else 1
    )
    st.session_state.detection_mode = detection_mode
    
    st.title("🤚 Finger Detection File Manager")
    
    if st.session_state.detection_mode == "Gesture Detection":
        st.markdown("**Gesture Mode Instructions:**")
        st.markdown("- **1 finger raised**: Upload the selected file")
        st.markdown("- **3 fingers raised**: Download available files")
    else:
        st.markdown("**Manual Mode Instructions:**")
        st.markdown("- Use buttons to upload and download files manually")
        st.markdown("- No camera or gesture detection needed")
    
    st.sidebar.subheader("🌐 Server Configuration")
    st.sidebar.text(f"Local IP: {st.session_state.local_ip}")
    
    if HTTP_AVAILABLE:
        use_http = st.sidebar.checkbox("Use HTTP Localhost Server", value=st.session_state.use_http)
        st.session_state.use_http = use_http
    else:
        st.sidebar.warning("⚠️ Install 'requests' and 'flask' for HTTP mode")
        st.sidebar.text("pip install requests flask")
        st.session_state.use_http = False
        use_http = False
    
    if use_http:
        server_port = st.sidebar.number_input("Server Port", min_value=1000, max_value=9999, value=5000)
        st.session_state.server_port = server_port
        server_url = f"http://{st.session_state.local_ip}:{server_port}"
        st.sidebar.text(f"Server URL: {server_url}")
        col_start_server, col_stop_server = st.sidebar.columns(2)
        with col_start_server:
            if st.button("🚀 Start Server") and not st.session_state.server_running:
                try:
                    app = create_flask_server()
                    st.session_state.server_thread = threading.Thread(
                        target=start_flask_server, 
                        args=(app, st.session_state.local_ip, server_port),
                        daemon=True
                    )
                    st.session_state.server_thread.start()
                    st.session_state.server_running = True
                    time.sleep(1)
                    st.sidebar.success("✅ Server started!")
                except Exception as e:
                    st.sidebar.error(f"❌ Failed to start server: {e}")
        with col_stop_server:
            if st.button("⏹️ Stop Server") and st.session_state.server_running:
                st.session_state.server_running = False
                st.sidebar.info("Server stopped!")
    else:
        st.sidebar.info("Using local file system (no network)")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📁 File Selection")
        uploaded_file = st.file_uploader("Choose a file to upload", type=None)
        if uploaded_file is not None:
            st.session_state.uploaded_file_data = uploaded_file.read()
            st.session_state.uploaded_filename = uploaded_file.name
            st.success(f"File ready: {uploaded_file.name}")
            st.info(f"File size: {len(st.session_state.uploaded_file_data)} bytes")
        if st.session_state.detection_mode == "Manual Mode":
            st.subheader("📤 Manual Upload")
            if st.button("🚀 Upload File", disabled=(st.session_state.uploaded_file_data is None)):
                if st.session_state.use_http and st.session_state.server_running:
                    server_url = f"http://{st.session_state.local_ip}:{st.session_state.server_port}"
                    existing_files = get_files_from_localhost_http(server_url)
                else:
                    existing_files = get_uploaded_files()
                if len(existing_files) == 0:
                    if st.session_state.use_http and st.session_state.server_running:
                        success, message = upload_file_to_localhost_http(
                            st.session_state.uploaded_file_data,
                            st.session_state.uploaded_filename,
                            server_url
                        )
                        if success:
                            st.success(f"✅ HTTP Upload: {st.session_state.uploaded_filename}")
                        else:
                            st.error(f"❌ Upload failed: {message}")
                    else:
                        upload_file_to_localhost(
                            st.session_state.uploaded_file_data, 
                            st.session_state.uploaded_filename
                        )
                        st.success(f"✅ File Upload: {st.session_state.uploaded_filename}")
                    st.rerun()
                else:
                    st.warning("❌ Delete existing file first!")
        if st.session_state.detection_mode == "Manual Mode":
            st.subheader("📥 Manual Download")
            if st.button("⬇️ Download Files"):
                if st.session_state.use_http and st.session_state.server_running:
                    server_url = f"http://{st.session_state.local_ip}:{st.session_state.server_port}"
                    existing_files = get_files_from_localhost_http(server_url)
                else:
                    existing_files = get_uploaded_files()
                if existing_files:
                    for file in existing_files:
                        if st.session_state.use_http and st.session_state.server_running:
                            success, message = download_file_from_localhost_http(file, server_url)
                            if success:
                                st.success(f"✅ HTTP Download: {file}")
                            else:
                                st.error(f"❌ Download failed: {message}")
                        else:
                            downloaded_path = download_file_from_localhost(file)
                            if downloaded_path:
                                st.success(f"✅ File Download: {file}")
                    st.rerun()
                else:
                    st.info("ℹ️ No files to download")
        st.subheader("📤 Files on Localhost")
        if st.session_state.use_http and st.session_state.server_running:
            server_url = f"http://{st.session_state.local_ip}:{st.session_state.server_port}"
            uploaded_files = get_files_from_localhost_http(server_url)
        else:
            uploaded_files = get_uploaded_files()
        if uploaded_files:
            for file in uploaded_files:
                if st.session_state.use_http:
                    st.text(f"📄 {file}")
                    if st.button(f"🗑️", key=f"delete_{file}"):
                        try:
                            response = requests.delete(f"{server_url}/delete/{file}", timeout=10)
                            if response.status_code == 200:
                                st.success(f"Deleted {file}")
                                st.rerun()
                            else:
                                st.error("Failed to delete file")
                        except Exception as e:
                            st.error(f"Error: {e}")
                else:
                    file_path = os.path.join(UPLOAD_DIR, file)
                    file_size = os.path.getsize(file_path)
                    col_file, col_delete = st.columns([3, 1])
                    with col_file:
                        st.text(f"📄 {file} ({file_size} bytes)")
                    with col_delete:
                        if st.button(f"🗑️", key=f"delete_{file}"):
                            if delete_uploaded_file(file):
                                st.success(f"Deleted {file}")
                                st.rerun()
        else:
            st.info("No files uploaded yet")
    
    with col2:
        if st.session_state.detection_mode == "Gesture Detection":
            st.subheader("📷 Camera Feed")
            col_start, col_stop = st.columns(2)
            with col_start:
                if st.button("🎥 Start Camera"):
                    st.session_state.camera_running = True
            with col_stop:
                if st.button("⏹️ Stop Camera"):
                    st.session_state.camera_running = False
            if st.session_state.camera_running:
                frame_placeholder = st.empty()
                status_placeholder = st.empty()
                cap = cv2.VideoCapture(0)
                if not cap.isOpened():
                    st.error("Could not open camera")
                    st.session_state.camera_running = False
                else:
                    gesture_history = []
                    stable_gesture_count = 0
                    required_stable_frames = 15
                    while st.session_state.camera_running:
                        ret, frame = cap.read()
                        if not ret:
                            st.error("Failed to read from camera")
                            break
                        frame = cv2.flip(frame, 1)
                        finger_count, hand_detected = st.session_state.detector.detect_gesture(frame)
                        if hand_detected:
                            cv2.putText(frame, f"Fingers: {finger_count}", (10, 50), 
                                      cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                            if finger_count == 1:
                                cv2.putText(frame, "UPLOAD GESTURE", (10, 90), 
                                          cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
                            elif finger_count == 3:
                                cv2.putText(frame, "DOWNLOAD GESTURE", (10, 90), 
                                          cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
                            if len(gesture_history) == 0 or gesture_history[-1] == finger_count:
                                stable_gesture_count += 1
                            else:
                                stable_gesture_count = 1
                            progress = min(stable_gesture_count / required_stable_frames, 1.0)
                            cv2.putText(frame, f"Stability: {stable_gesture_count}/{required_stable_frames}", 
                                      (10, 130), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
                            gesture_history.append(finger_count)
                            if len(gesture_history) > 30:
                                gesture_history.pop(0)
                            if stable_gesture_count >= required_stable_frames:
                                if st.session_state.use_http and st.session_state.server_running:
                                    server_url = f"http://{st.session_state.local_ip}:{st.session_state.server_port}"
                                    existing_files = get_files_from_localhost_http(server_url)
                                else:
                                    existing_files = get_uploaded_files()
                                if finger_count == 1 and hand_detected:
                                    if len(existing_files) == 0:
                                        if (st.session_state.uploaded_file_data is not None and 
                                            st.session_state.uploaded_filename is not None):
                                            if st.session_state.use_http and st.session_state.server_running:
                                                success, message = upload_file_to_localhost_http(
                                                    st.session_state.uploaded_file_data,
                                                    st.session_state.uploaded_filename,
                                                    server_url
                                                )
                                                if success:
                                                    status_placeholder.success(f"✅ HTTP Upload: {st.session_state.uploaded_filename}")
                                                else:
                                                    status_placeholder.error(f"❌ Upload failed: {message}")
                                            else:
                                                upload_file_to_localhost(
                                                    st.session_state.uploaded_file_data, 
                                                    st.session_state.uploaded_filename
                                                )
                                                status_placeholder.success(f"✅ File Upload: {st.session_state.uploaded_filename}")
                                            stable_gesture_count = 0
                                        else:
                                            status_placeholder.warning("❌ No file selected for upload!")
                                elif finger_count == 3 and hand_detected:
                                    if existing_files:
                                        for file in existing_files:
                                            if st.session_state.use_http and st.session_state.server_running:
                                                success, message = download_file_from_localhost_http(file, server_url)
                                                if success:
                                                    status_placeholder.success(f"✅ HTTP Download: {file}")
                                                else:
                                                    status_placeholder.error(f"❌ Download failed: {message}")
                                            else:
                                                downloaded_path = download_file_from_localhost(file)
                                                if downloaded_path:
                                                    status_placeholder.success(f"✅ File Download: {file}")
                                        stable_gesture_count = 0
                                    else:
                                        status_placeholder.info("ℹ️ No files to download")
                        else:
                            cv2.putText(frame, "No hand detected", (10, 50), 
                                      cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                        frame_placeholder.image(frame_rgb, channels="RGB", use_container_width=True)
                    cap.release()
            else:
                st.subheader("📋 Manual Mode")
                st.info("🎮 Manual mode active - use the buttons in the left panel to upload and download files")
                st.markdown("### Benefits of Manual Mode:")
                st.markdown("- 🚫 No camera required")
                st.markdown("- ⚡ Instant file operations")
                st.markdown("- 🎯 Precise control")
                st.markdown("- 💻 Works on any device")
    
    st.subheader("📥 Downloaded Files")
    if os.path.exists(DOWNLOAD_DIR):
        downloaded_files = [f for f in os.listdir(DOWNLOAD_DIR) 
                          if os.path.isfile(os.path.join(DOWNLOAD_DIR, f))]
        if downloaded_files:
            col_header, col_clear = st.columns([3, 1])
            with col_header:
                st.markdown("**Available Downloads:**")
            with col_clear:
                if st.button("🗑️ Clear All"):
                    try:
                        for file in downloaded_files:
                            file_path = os.path.join(DOWNLOAD_DIR, file)
                            if os.path.exists(file_path):
                                os.remove(file_path)
                        st.success("✅ All downloaded files cleared!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"❌ Error clearing files: {e}")
            for file in downloaded_files:
                file_path = os.path.join(DOWNLOAD_DIR, file)
                file_size = os.path.getsize(file_path)
                col_file, col_download = st.columns([3, 1])
                with col_file:
                    st.text(f"📄 {file} ({file_size} bytes)")
                with col_download:
                    with open(file_path, 'rb') as f:
                        st.download_button(
                            label="⬇️",
                            data=f.read(),
                            file_name=file,
                            key=f"download_{file}"
                        )
        else:
            st.info("No files downloaded yet")

if __name__ == "__main__":
    main()