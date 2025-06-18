import streamlit as st
import tensorflow as tf
from tensorflow.keras.optimizers.schedules import CosineDecay
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
        # Register the CosineDecay schedule as a custom object
        model = tf.keras.models.load_model(
            MODEL_PATH,
            custom_objects={'CosineDecay': CosineDecay}
        )
        return model
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        st.error(f"Make sure the model file exists at: {MODEL_PATH}")
        st.error("If using custom learning rate schedules, they must be registered.")
        return None

def get_model():
    """
    Get the loaded model instance.
    
    Returns:
        tensorflow.keras.Model or None: The loaded model or None if loading failed
    """
    return load_baybayin_model()