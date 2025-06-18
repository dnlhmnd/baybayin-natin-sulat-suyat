import streamlit as st
import numpy as np
from PIL import Image
from models.model_loader import get_model
from utils.image_processing import preprocess_image
from config.settings import BAYBAYIN_CATEGORIES, UI_CONFIG, ASSET_PATHS


def show():
    """Display the image upload page"""
    st.header("Upload Baybayin Character")
    st.caption("Upload an image of a Baybayin character then click 'Classify Image' to predict the character.")
    
    # File uploader in sidebar
    uploaded_file = st.sidebar.file_uploader(
        "Choose an image...", 
        type=["jpg", "jpeg", "png"], 
        key="file_uploader"
    )
    
    if uploaded_file is not None:
        _handle_uploaded_file(uploaded_file)
    
    _show_reference_chart()


def _handle_uploaded_file(uploaded_file):
    """Handle the uploaded file and display results"""
    # Create three columns for layout
    upload_col, processed_col, results_col = st.columns([1, 1, 1], border=True)
    
    # Load and display uploaded image
    image = Image.open(uploaded_file)
    image_np = np.array(image)
    
    with upload_col:
        st.subheader("Uploaded Image")
        st.write("\n")
        _center_image(image, UI_CONFIG['upload_image_width'])
    
    # Classification button in sidebar
    if st.sidebar.button('Classify Image'):
        _classify_image(image_np, processed_col, results_col)


def _classify_image(image_np, processed_col, results_col):
    """Classify the uploaded image"""
    model = get_model()
    if model is None:
        st.error("Model not available. Please check the model file.")
        return
    
    with st.spinner('Processing image...'):
        processed_img = preprocess_image(image_np)
        
        if processed_img is not None:
            _display_processed_image(processed_img, processed_col)
            _display_predictions(model, processed_img, results_col)
        else:
            st.error("Failed to preprocess the image.")


def _display_processed_image(processed_img, processed_col):
    """Display the processed image"""
    processed_display = (processed_img[0, :, :, 0] * 255).astype(np.uint8)
    
    with processed_col:
        st.subheader("Processed Image")
        st.write("\n")
        _center_image(processed_display, UI_CONFIG['processed_image_width'])


def _display_predictions(model, processed_img, results_col):
    """Display the top 5 predictions"""
    with results_col:
        st.subheader("Top 5 Predictions:")
        prediction = model.predict(processed_img)
        top5_idx = np.argsort(prediction[0])[::-1][:5]

        # Highlight top-1 prediction
        top_idx = top5_idx[0]
        top_character = BAYBAYIN_CATEGORIES[top_idx]
        top_confidence = prediction[0][top_idx]
        
        st.success(f"Predicted Character: **{top_character}**")
        st.info(f"Confidence: {top_confidence * 100:.2f}%")

        # List remaining predictions
        st.markdown("**Other Predictions:**")
        for i, idx in enumerate(top5_idx[1:], start=2):
            character = BAYBAYIN_CATEGORIES[idx]
            confidence = prediction[0][idx] * 100
            st.write(f"{i}. {character} - {confidence:.2f}%")


def _center_image(image, width):
    """Center an image using columns"""
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(image, width=width)


def _show_reference_chart():
    """Display the collapsible guide and reference chart"""
    with st.expander("🖼️ Guide: What Makes a Good Input Image?", expanded=True):
        st.markdown(
            """
            **Tips for Best Results:**
            - This app follows a series of image processing steps (see Home page: *About the Technology*), so a good input image is important for accurate results.
            - Use images with clear, Baybayin characters.
            - Prefer white or light backgrounds with high contrast.
            - Avoid noisy, blurry, or low-resolution images.
            - Avoid images with multiple characters or excessive artifacts.

            *You can still try uploading 'bad' images to see how the model performs!*
            """
        )
        st.markdown("#### ✅ Good Example Images")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("assets/good_example_1.jpg", caption="Clear, centered, white background", width=256)
        with col2:
            st.image("assets/good_example_2.png", caption="High contrast, single character", width=256)
        with col3:
            st.image("assets/good_example_3.jpg", caption="Properly cropped, no noise", width=256)

        st.markdown("#### ❌ Bad Example Images")
        col4, col5, col6 = st.columns(3)
        with col4:
            st.image("assets/bad_example_1.jpg", caption="Noisy/blurred image", width=256)
        with col5:
            st.image("assets/bad_example_2.png", caption="Fake PNG (checkerboard bg)", width=256)
        with col6:
            st.image("assets/bad_example_3.jpg", caption="Uniquely written Baybayin characters", width=190)

    with st.expander("📖 Baybayin Character Reference Chart", expanded=False):
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.image(ASSET_PATHS['reference'])