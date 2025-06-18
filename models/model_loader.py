import streamlit as st
import tensorflow as tf
from config.settings import MODEL_PATH

@st.cache_resource
def load_baybayin_model():
    """
    Load the trained Baybayin classifier model.
    Uses Streamlit's cache_resource decorator for efficient loading.
    
    Returns:
        tensorflow.keras.Model: Loaded Baybayin classifier model
    """
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        return model
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        st.error(f"Make sure the model file exists at: {MODEL_PATH}")
        return None

def get_model():
    """
    Get the loaded model instance.
    
    Returns:
        tensorflow.keras.Model or None: The loaded model or None if loading failed
    """
    return load_baybayin_model()