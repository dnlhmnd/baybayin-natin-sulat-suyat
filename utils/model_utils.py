import tensorflow as tf
import streamlit as st
from utils.config import MODEL_PATH

@st.cache_resource
def load_model():
    """Load and cache the trained model"""
    return tf.keras.models.load_model(MODEL_PATH)

def predict_image(image):
    """Make predictions on a preprocessed image"""
    model = load_model()
    return model.predict(image)