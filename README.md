# Baybayin Natin: Sulat Suyat!

A Streamlit web application for recognizing and classifying Baybayin characters using Convolutional Neural Networks (CNN). This project aims to preserve the ancient Filipino script through modern AI technology.

## 🌟 Features

- **Image Upload Classification**: Upload images of Baybayin characters for recognition
- **Interactive Drawing Canvas**: Draw characters directly in the browser for real-time classification
- **Advanced Image Processing**: Sophisticated preprocessing pipeline for optimal character recognition
- **Top-5 Predictions**: Shows confidence scores for multiple possible character matches
- **Reference Charts**: Built-in Baybayin character reference guides

## 🏗️ Project Structure

```
baybayin-natin/
├── main.py                    # Main Streamlit application entry point
├── requirements.txt           # Python dependencies
├── README.md                 # Project documentation
├── config/
│   └── settings.py           # Configuration constants and settings
├── models/
│   ├── model_loader.py       # Model loading utilities
│   └── baybayin_classifier.h5 # Trained CNN model (not included)
├── utils/
│   ├── __init__.py
│   └── image_processing.py   # Image preprocessing functions
├── pages/
│   ├── __init__.py
│   ├── home.py              # Home page content
│   ├── image_upload.py      # Image upload functionality
│   └── drawing_canvas.py    # Drawing canvas interface
└── assets/
    ├── mainLogo.png      
    ├── ss1.png           
    ├── preprocessing.png   
    └── reference.png      
```

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd baybayin-natin
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add required assets:**
   - Place your trained model file (`baybayin_classifier.h5`) in the `models/` directory

4. **Run the application:**
   ```bash
   streamlit run main.py
   ```

## 📖 Usage

### Home Page
- Overview of the Baybayin Natin project
- Information about the technology and methodology
- Character reference chart

### Image Upload
1. Navigate to "Image Upload" in the sidebar
2. Upload an image file (JPG, JPEG, or PNG)
3. Click "Classify Image" to get predictions
4. View the processed image and top-5 character predictions

### Drawing Canvas
1. Navigate to "Drawing Canvas" in the sidebar
2. Configure drawing settings in the sidebar (brush size, colors, etc.)
3. Draw a Baybayin character on the canvas
4. Click "Classify Drawing" to get predictions
5. View the processed drawing and predictions

## 🔧 Configuration

The application is highly configurable through the `config/settings.py` file:

- **Model settings**: Path to model file, image dimensions
- **Image processing parameters**: Filter settings, morphological operations
- **UI configuration**: Image sizes, canvas dimensions
- **Asset paths**: Locations of images and resources

## 🧠 Model Information

The application uses a Convolutional Neural Network trained to recognize 59 different Baybayin characters and character combinations:

- **Input**: 64x64 grayscale images
- **Architecture**: CNN with multiple convolutional and pooling layers
- **Output**: Classification scores for 59 character categories
- **Categories**: Includes basic vowels, consonants, and consonant-vowel combinations

## 🔄 Image Processing Pipeline

The application includes a sophisticated image processing pipeline:

1. **Format Conversion**: Handle various input formats (PIL, numpy arrays, RGBA/RGB)
2. **Noise Reduction**: Bilateral filtering to reduce noise while preserving edges
3. **Contrast Enhancement**: CLAHE (Contrast Limited Adaptive Histogram Equalization)
4. **Smoothing**: Gaussian blur for stroke consistency
5. **Binarization**: Adaptive thresholding using Otsu's method
6. **Morphological Operations**: Opening and closing to clean up artifacts
7. **Foreground Detection**: Automatic detection and correction of inverted images
8. **Content Cropping**: Remove excess whitespace around characters
9. **Aspect Ratio Preservation**: Resize with padding to maintain character proportions
10. **Stroke Optimization**: Thin overly thick strokes if necessary

## 🛠️ Development

### Adding New Features

1. **New Pages**: Add new page modules in the `pages/` directory
2. **Processing Functions**: Extend `utils/image_processing.py` for new preprocessing methods
3. **Configuration**: Update `config/settings.py` for new parameters
4. **Models**: Modify `models/model_loader.py` for different model types

### Code Style

- Follow PEP 8 style guidelines
- Use type hints where appropriate
- Add docstrings to all functions and classes
- Keep functions focused and modular

## 📊 Performance Considerations

- **Model Caching**: Uses Streamlit's `@st.cache_resource` for efficient model loading
- **Image Processing**: Optimized OpenCV operations for fast preprocessing
- **Memory Management**: Efficient handling of image arrays and model predictions

## 📝 License

This project is part of academic research on Baybayin script recognition. Please refer to the original thesis paper for academic citations.

## 🔗 References

- [Baybayin Script Word Recognition and Transliteration Using a Convolutional Neural Network](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4004853)
- Original thesis work that forms the foundation of this application

## 📞 Support

For questions, issues, or contributions, please:
1. Check the existing issues in the repository
2. Create a new issue with detailed information
3. Contact the development team

---

**Baybayin Natin: Sulat Suyat!** - Preserving Filipino heritage through technology 🇵🇭