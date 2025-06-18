# Configuration settings for the Baybayin app

# Navigation options
NAV_OPTIONS = [
    ("🏠", "Home", "home"),
    ("🖼️", "Image Upload", "image_upload"), 
    ("✏️", "Drawing Canvas", "drawing_canvas")
]

SOCIAL_LINKS = {
    "linkedin": "https://www.linkedin.com/in/danielshawnhammond/",
    "github": "https://github.com/dnlhmnd",
    "kaggle": "https://www.kaggle.com/danielhammond",
    "dev": "https://dev.to/dnlhmnd"
}

# Page configuration
PAGE_CONFIG = {
    "page_title": "Baybayin Natin: Sulat Suyat!",
    "layout": "wide"
}

# Model configuration
MODEL_PATH = 'models/baybayin_classifier.h5'
IMAGE_SIZE = (64, 64)

# Baybayin character categories
BAYBAYIN_CATEGORIES = [
    'a', 'b', 'ba', 'be_bi', 'bo_bu', 'd', 'da_ra', 'de_di', 'do_du', 'e_i',
    'g', 'ga', 'ge_gi', 'go_gu', 'h', 'ha', 'he_hi', 'ho_hu', 'k', 'ka',
    'ke_ki', 'ko_ku', 'l', 'la', 'le_li', 'lo_lu', 'm', 'ma', 'me_mi', 'mo_mu',
    'n', 'na', 'ne_ni', 'ng', 'nga', 'nge_ngi', 'ngo_ngu', 'no_nu', 'o_u',
    'p', 'pa', 'pe_pi', 'po_pu', 's', 'sa', 'se_si', 'so_su', 't', 'ta',
    'te_ti', 'to_tu', 'w', 'wa', 'we_wi', 'wo_wu', 'y', 'ya', 'ye_yi', 'yo_yu'
]

# Image processing parameters
PROCESSING_CONFIG = {
    'bilateral_filter': {'d': 9, 'sigmaColor': 75, 'sigmaSpace': 75},
    'clahe': {'clipLimit': 2.0, 'tileGridSize': (8, 8)},
    'gaussian_blur': {'ksize': (3, 3), 'sigmaX': 0},
    'morphology_kernels': {
        'small': (2, 2),
        'medium': (3, 3)
    },
    'crop_padding': 5,
    'thickness_threshold': 0.3
}

# UI Configuration
UI_CONFIG = {
    'upload_image_width': 350,
    'processed_image_width': 350,
    'canvas_size': {'width': 500, 'height': 500},
    'drawing_canvas_image_width': 310
}

# Asset paths
ASSET_PATHS = {
    'logo': 'assets/mainLogo.png',
    'ss1': 'assets/ss1.png',
    'preprocessing': 'assets/preprocessing.png',
    'reference': 'assets/reference.png'
}

# External links
EXTERNAL_LINKS = {
    'thesis_paper': 'https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4004853'
}