import streamlit as st
from config.settings import SOCIAL_LINKS, EXTERNAL_LINKS, ASSET_PATHS


def show():
    """Display the home page content"""
    st.title("Baybayin Natin: Sulat Suyat!")
    st.subheader("Preserving the Ancient Filipino Script through AI")
    
    st.image(ASSET_PATHS['ss1'], use_container_width=True)
    
    _setup_home_sidebar()  # Call sidebar setup
    
    _show_about_section()
    _show_usage_guide()
    _show_technology_section()
    _show_reference_chart()

def _setup_home_sidebar():
    """Setup canvas configuration in sidebar"""
    st.sidebar.title("Check out my socials!")
    # Social links (horizontal row)
    st.sidebar.markdown(
        f"""
        <div style="display: flex; gap: 8px;">
            <a href={SOCIAL_LINKS['linkedin']} target="_blank">
                <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white" alt="LinkedIn">
            </a>
            <a href={SOCIAL_LINKS['github']} target="_blank">
                <img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white" alt="GitHub">
            </a>
            <a href={SOCIAL_LINKS['kaggle']} target="_blank">
                <img src="https://img.shields.io/badge/Kaggle-20BEFF?style=flat&logo=kaggle&logoColor=white" alt="Kaggle">
            </a>
            <a href={SOCIAL_LINKS['dev']} target="_blank">
                <img src="https://img.shields.io/badge/DEV.to-0A0A0A?style=flat&logo=devdotto&logoColor=white" alt="DEV.to">
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    st.sidebar.divider()
    st.sidebar.title("View the code on GitHub!")
    st.sidebar.markdown(
        "[View Source on GitHub](https://github.com/dnlhmnd/baybayin-natin-sulat-suyat)"
    )

    st.sidebar.divider()
    st.sidebar.title("Buy Me a Coffee!")
    st.sidebar.markdown("""
    <div style="text-align: center;">
        <a href="https://www.buymeacoffee.com/dnlhmnd" target="_blank">
            <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" 
                alt="Buy Me A Coffee" 
                style="height: 45px; width: 162px;">
        </a>
    </div>
    """, unsafe_allow_html=True)

def _show_about_section():
    """Display the about section"""
    st.markdown(f"""
    ## About Baybayin Natin
        
    **Baybayin Natin** is a project born from our college thesis work titled 
    [Baybayin Script Word Recognition and Transliteration Using a Convolutional Neural Network]({EXTERNAL_LINKS['thesis_paper']}). 
    This version, **Sulat Suyat**, focuses on single character classification of the ancient Filipino script - Baybayin.
        
    Baybayin was the pre-colonial writing system used in the Philippines before being replaced by the Latin alphabet. 
    Our goal is to help preserve this important cultural heritage through modern technology.
    """)


def _show_usage_guide():
    """Display the usage guide section"""
    st.markdown("""
    ## How to Use This App
        
    1. **Image Upload** - Upload an image of a Baybayin character for classification
    2. **Drawing Canvas** - Draw a Baybayin character and get real-time classification
        
    ### Navigation Guide:
    - Use the sidebar to switch between different pages
    - Each page has specific instructions for that functionality
    - Reference charts are available on each page to help with character identification
    """)


def _show_technology_section():
    """Display the technology section"""
    st.markdown("""
    ## About the Technology
        
    This app uses a **Convolutional Neural Network (CNN)** trained on thousands of Baybayin character samples. 
    The model can recognize 59 different Baybayin characters and character combinations with high accuracy.
        
    The image processing pipeline includes:
    - **Adaptive thresholding** - Handles varying paper/lighting conditions
    - **Automatic inversion detection** - Ensures black characters on white background
    - **Content-aware cropping** - Removes excess whitespace around characters
    - **Aspect ratio preservation** - Maintains character proportions
    - **Morphological cleaning** - Removes noise while preserving character strokes
    """)


def _show_reference_chart():
    """Display the collapsible reference chart"""
    with st.expander("Baybayin Character Reference Chart", expanded=False):
        st.image(ASSET_PATHS['preprocessing'], use_container_width=True)