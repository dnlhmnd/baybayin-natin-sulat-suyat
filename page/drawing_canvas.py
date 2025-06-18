import streamlit as st
import numpy as np
from streamlit_drawable_canvas import st_canvas
from models.model_loader import get_model
from utils.image_processing import process_canvas_drawing
from config.settings import BAYBAYIN_CATEGORIES, UI_CONFIG, ASSET_PATHS


def show():
    """Display the drawing canvas page"""
    st.header("Draw Baybayin Character")
    st.caption("Draw a Baybayin character in the canvas below and click 'Classify' to predict the character.")

    # Configure canvas settings in sidebar
    canvas_config = _setup_canvas_sidebar()
    
    # Create layout columns
    canvas_col, processed_col, results_col = st.columns([1, 1, 1], border=True)
    
    # Display canvas and handle drawing
    with canvas_col:
        canvas_result = _display_canvas(canvas_config)
        predict_btn = st.button('Classify Drawing')
    
    # Handle prediction
    _handle_prediction(predict_btn, canvas_result, processed_col, results_col)
    
    # Show reference chart
    _show_reference_chart()


def _setup_canvas_sidebar():
    """Setup canvas configuration in sidebar"""
    st.sidebar.header("Canvas Settings")
    
    drawing_mode = st.sidebar.selectbox(
        "Drawing tool:", ("freedraw", "point", "line", "rect", "circle", "transform")
    )
    
    stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 15)
    point_display_radius = 15
    
    if drawing_mode == 'point':
        point_display_radius = st.sidebar.slider("Point display radius: ", 1, 25, 15)
    
    col1, col2 = st.sidebar.columns(2)
    stroke_color = col1.color_picker("Stroke color", "#000000")
    bg_color = col2.color_picker("Background color", "#F9F9F9")
    
    return {
        'drawing_mode': drawing_mode,
        'stroke_width': stroke_width,
        'point_display_radius': point_display_radius,
        'stroke_color': stroke_color,
        'bg_color': bg_color
    }


def _display_canvas(config):
    """Display the drawing canvas"""
    st.subheader("Draw Baybayin Character")
    
    col1, col2, col3 = st.columns([1, 8, 1])
    with col2:
        canvas_result = st_canvas(
            fill_color="rgba(255, 165, 0, 0.3)",
            stroke_width=config['stroke_width'],
            stroke_color=config['stroke_color'],
            background_color=config['bg_color'],
            update_streamlit=True,
            width=UI_CONFIG['canvas_size']['width'],
            height=UI_CONFIG['canvas_size']['height'],
            drawing_mode=config['drawing_mode'],
            point_display_radius=config['point_display_radius'] if config['drawing_mode'] == 'point' else 0,
            key="canvas",
        )
    
    return canvas_result


def _handle_prediction(predict_btn, canvas_result, processed_col, results_col):
    """Handle the prediction process"""
    # Initialize session state
    if 'predict_btn' not in st.session_state:
        st.session_state['predict_btn'] = False
    
    if predict_btn:
        st.session_state['predict_btn'] = True

    if st.session_state['predict_btn'] and canvas_result.image_data is not None:
        _classify_drawing(canvas_result.image_data, processed_col, results_col)


def _classify_drawing(image_data, processed_col, results_col):
    """Classify the drawn image"""
    model = get_model()
    if model is None:
        st.error("Model not available. Please check the model file.")
        return
    
    with st.spinner('Processing drawing...'):
        processed_img = process_canvas_drawing(image_data)

        if processed_img is not None:
            _display_processed_drawing(processed_img, processed_col)
            _display_drawing_predictions(model, processed_img, results_col)
        else:
            st.error("Failed to preprocess the image.")


def _display_processed_drawing(processed_img, processed_col):
    """Display the processed drawing"""
    processed_display = (processed_img[0, :, :, 0] * 255).astype(np.uint8)

    with processed_col:
        st.subheader("Processed Drawing")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        
        # Center the processed image
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(
                processed_display, 
                width=UI_CONFIG['drawing_canvas_image_width'], 
                use_container_width=False
            )


def _display_drawing_predictions(model, processed_img, results_col):
    """Display predictions for the drawing"""
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


def _show_reference_chart():
    """Display the collapsible reference chart"""
    with st.expander("Use this baybayin chart as reference", expanded=False):
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            st.image(ASSET_PATHS['reference'])