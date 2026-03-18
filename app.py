import streamlit as st
from generator import generate_video_content

st.set_page_config(
    page_title="AI Video Studio Pro",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background-color: #4F46E5;
        color: white;
        font-weight: 600;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #4338CA;
        border: none;
    }
    .main-header {
        font-size: 36px;
        font-weight: 800;
        color: #1E293B;
        margin-bottom: 0px;
    }
    </style>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.title("⚙️ Studio Settings")
    st.write("Configure your video parameters below.")
    st.divider()
    
    video_topic = st.text_input("Video Topic", placeholder="e.g., The Future of Quantum Computing")
    
    col1, col2 = st.columns(2)
    with col1:
        video_duration = st.selectbox("Duration", ["Shorts", "5 Minutes", "10+ Minutes"])
    with col2:
        video_tone = st.selectbox("Vibe/Tone", ["Professional", "Humorous", "Dramatic", "Educational"])
    
    st.divider()
    process_request = st.button("Generate Content ✨")

st.markdown('<p class="main-header">🚀 AI Video Creator Studio</p>', unsafe_allow_html=True)
st.caption("Advanced Content Engine Powered by Groq Llama-3.3")

if process_request:
    if video_topic:
        with st.spinner("AI is architecting your content..."):
            final_output = generate_video_content(video_topic, video_duration, video_tone)
            
            content_tab, summary_tab = st.tabs(["📝 Complete Package", "📊 Metadata Summary"])
            
            with content_tab:
                st.markdown("### 🎬 Generated Package")
                st.info("Your script and SEO metadata are ready.")
                st.markdown(final_output)
                
                st.divider()
                st.download_button(
                    label="📥 Download as Text File",
                    data=final_output,
                    file_name=f"{video_topic.replace(' ', '_')}_script.txt",
                    mime="text/plain"
                )
            
            with summary_tab:
                st.success("Generation Successful!")
                st.write(f"**Topic:** {video_topic}")
                st.write(f"**Tone:** {video_tone}")
    else:
        st.error("Please provide a video topic.")

else:
    st.markdown("---")
    st.subheader("Ready to create your next viral video?")
    st.write("Enter your topic in the sidebar and click Generate to start.")