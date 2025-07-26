import streamlit as st

# Set page config
st.set_page_config(page_title="Chatbot Learnity", page_icon=":speech_balloon:")

# CSS untuk styling
st.markdown("""
    <style>
    #MainMenu {
        visibility: hidden;
    }
    
    .footer {
        visibility: hidden;
    }
    .block-container {
        margin-top: 0rem; !important
        margin-bottom: 0rem; !important
        padding: 0rem; !important
    }
    body {
        background-color: #fefefe;
        font-family: 'Arial', sans-serif;
        text-align: center;
    }
    .chat-container {
        align-items: center;
        margin-top: 50px;
    }
    .bluppy-chat {
        display: flex;
    }
    .chat-bubble {
        background-color: #f7f7f7;
        color: #555;
        padding: 15px 20px;
        border-radius: 15px;
        font-size: 18px;
        max-width: 400px;
        margin-top: -120px;
        margin-left: 190px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .chat-bubble span {
        color: #8ecae6;
        font-weight: bold;
    }
    .header {
        margin-top: 0px;
    }

    </style>
""", unsafe_allow_html=True)

# gambar = st.image("image/bluppy.png", width=100)

st.markdown(
    """
        <div class="header">
    """,
    unsafe_allow_html=True
)

st.image("image/logo.svg", width=50)

st.markdown(
    """
        </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
        <div class="chat-container">
          <div class="blupyy-chat">
            <div class="bluppy-img">
    """,
    unsafe_allow_html=True
)

st.image("image/bluppy.png", width=200)


# Konten chatbot
st.markdown(f"""
        
            <div class="chat-bubble">Halo aku <span>BLUPPY</span> yang siap jadi partner belajarmu!</div>
          </div>
        </div>
""", unsafe_allow_html=True)
