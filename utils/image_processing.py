import numpy as np
import cv2
from PIL import Image
import streamlit as st
from config.settings import IMAGE_SIZE, PROCESSING_CONFIG


def preprocess_image(image, target_size=IMAGE_SIZE):
    """
    Enhanced image processing function for Baybayin character recognition.
    
    Args:
        image: Input image (PIL Image or numpy array)
        target_size: Target size for the processed image (width, height)
    
    Returns:
        numpy.ndarray: Preprocessed image ready for model prediction
    """
    try:
        # Convert PIL Image to numpy array if needed
        if isinstance(image, Image.Image):
            image = np.array(image)
            # Convert RGBA to RGB if needed
            if image.shape[-1] == 4:
                image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
        
        # Ensure image is in uint8 format
        if image.dtype != np.uint8:
            if image.dtype == bool:
                image = image.astype(np.uint8) * 255
            else:
                image = image.astype(np.uint8)
        
        # Convert to grayscale if needed
        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        else:
            gray = image.copy()
        
        # Apply noise reduction
        denoised = cv2.bilateralFilter(gray, **PROCESSING_CONFIG['bilateral_filter'])
        
        # Enhance contrast
        clahe = cv2.createCLAHE(**PROCESSING_CONFIG['clahe'])
        enhanced = clahe.apply(denoised)
        
        # Apply smoothing
        blurred = cv2.GaussianBlur(enhanced, **PROCESSING_CONFIG['gaussian_blur'])
        
        # Apply adaptive thresholding
        binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        
        # Apply morphological operations
        kernel_small = np.ones(PROCESSING_CONFIG['morphology_kernels']['small'], np.uint8)
        cleaned = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel_small)
        
        kernel_medium = np.ones(PROCESSING_CONFIG['morphology_kernels']['medium'], np.uint8)
        filled = cv2.morphologyEx(cleaned, cv2.MORPH_CLOSE, kernel_medium)
        
        # Check and fix foreground/background
        black_pixels = np.sum(filled == 0)
        white_pixels = np.sum(filled == 255)
        
        if black_pixels > white_pixels:
            filled = cv2.bitwise_not(filled)
        
        # Crop to content
        cropped = crop_to_content(filled)
        
        # Resize with padding
        final = resize_with_padding(cropped, target_size)
        
        # Final cleanup
        final = thin_strokes(final)
        
        # Normalize and add dimensions for model
        final = final.astype('float32') / 255.0
        final = np.expand_dims(final, axis=-1)  # Add channel dimension
        final = np.expand_dims(final, axis=0)   # Add batch dimension
        
        return final
    
    except Exception as e:
        st.error(f"Error during image processing: {str(e)}")
        return None


def crop_to_content(image, padding=None):
    """
    Crop image to actual content with optional padding.
    
    Args:
        image: Input binary image
        padding: Padding around the content (default from config)
    
    Returns:
        numpy.ndarray: Cropped image
    """
    if padding is None:
        padding = PROCESSING_CONFIG['crop_padding']
    
    coords = np.column_stack(np.where(image < 255))
    if len(coords) == 0:
        return image
    
    y_min, x_min = coords.min(axis=0)
    y_max, x_max = coords.max(axis=0)
    
    h, w = image.shape
    y_min = max(0, y_min - padding)
    x_min = max(0, x_min - padding)
    y_max = min(h, y_max + padding)
    x_max = min(w, x_max + padding)
    
    return image[y_min:y_max, x_min:x_max]


def resize_with_padding(image, target_size):
    """
    Resize image while maintaining aspect ratio and adding padding.
    
    Args:
        image: Input image
        target_size: Target size (width, height)
    
    Returns:
        numpy.ndarray: Resized image with padding
    """
    h, w = image.shape
    target_w, target_h = target_size
    
    scale = min(target_w / w, target_h / h)
    
    new_w = int(w * scale)
    new_h = int(h * scale)
    resized = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)
    
    result = np.ones((target_h, target_w), dtype=np.uint8) * 255
    
    y_offset = (target_h - new_h) // 2
    x_offset = (target_w - new_w) // 2
    result[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = resized
    
    return result


def thin_strokes(image):
    """
    Thin strokes if they are too thick.
    
    Args:
        image: Input binary image
    
    Returns:
        numpy.ndarray: Image with thinned strokes if needed
    """
    char_pixels = np.sum(image == 0)
    total_pixels = image.shape[0] * image.shape[1]
    
    if char_pixels / total_pixels > PROCESSING_CONFIG['thickness_threshold']:
        kernel = np.ones((2, 2), np.uint8)
        return cv2.erode(image, kernel, iterations=1)
    
    return image


def process_canvas_drawing(canvas_data):
    """
    Process drawing from canvas for classification.
    
    Args:
        canvas_data: Canvas image data
    
    Returns:
        numpy.ndarray: Processed image ready for classification
    """
    drawn_image = cv2.cvtColor(np.array(canvas_data), cv2.COLOR_RGBA2GRAY)
    _, drawn_image = cv2.threshold(drawn_image, 127, 255, cv2.THRESH_BINARY_INV)
    return preprocess_image(drawn_image)