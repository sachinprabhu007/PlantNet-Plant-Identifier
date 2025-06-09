# app.py - Main Streamlit application
import streamlit as st
import requests
import json
from PIL import Image
import io
import base64
import os

# Page configuration
st.set_page_config(
    page_title="🌱 PlantNet Plant Identifier",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #2E8B57;
        text-align: center;
        margin-bottom: 2rem;
    }
    .stAlert > div {
        padding: 1rem;
        border-radius: 10px;
    }
    .upload-section {
        border: 2px dashed #2E8B57;
        border-radius: 10px;
        padding: 2rem;
        text-align: center;
        margin: 1rem 0;
    }
    .result-card {
        background-color: #f0f8f0;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        border-left: 5px solid #2E8B57;
    }
</style>
""", unsafe_allow_html=True)

# PlantNet API configuration
PLANTNET_API_URL = "https://my-api.plantnet.org/v2/identify"

def identify_plant(image, api_key, project="all", organ="leaf"):
    """
    Send image to PlantNet API v2 for plant identification
    """
    try:
        # Convert image to bytes
        img_buffer = io.BytesIO()
        if image.mode != 'RGB':
            image = image.convert('RGB')
        image.save(img_buffer, format='JPEG', quality=85)
        img_buffer.seek(0)
        
        # Prepare files for multipart form data
        files = {
            'images': ('plant.jpg', img_buffer.getvalue(), 'image/jpeg')
        }
        
        # Form data - only valid parameters
        data = {
            'organs': organ
        }
        
        # API endpoint with project
        url = f"{PLANTNET_API_URL}/{project}"
        
        # Parameters
        params = {
            'api-key': api_key
        }
        
        # Make the API request
        response = requests.post(url, files=files, data=data, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"API request failed with status code: {response.status_code}"}
            
    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}

def display_results(results):
    """Display the plant identification results in a nice format"""
    if "error" in results:
        st.error(f"❌ {results['error']}")
        return
    
    if "results" not in results or not results["results"]:
        st.warning("⚠️ No plants identified. Try a clearer image or different angle.")
        return
    
    st.success(f"✅ Found {len(results['results'])} possible matches!")
    
    # Display results with confidence scores
    for i, result in enumerate(results["results"][:5]):  # Show top 5 results
        confidence = result['score']
        species_name = result['species']['scientificNameWithoutAuthor']
        
        # Confidence color coding
        if confidence > 0.7:
            confidence_color = "🟢"
        elif confidence > 0.4:
            confidence_color = "🟡"
        else:
            confidence_color = "🔴"
        
        with st.expander(f"{confidence_color} **{species_name}** ({confidence:.1%} confidence)", expanded=(i==0)):
            col1, col2 = st.columns([1, 2])
            
            with col1:
                # Display reference image if available
                if result.get('images'):
                    try:
                        ref_img_url = result['images'][0]['url']['m']
                        st.image(ref_img_url, caption="Reference Image", use_column_width=True)
                    except:
                        st.info("Reference image not available")
            
            with col2:
                st.markdown(f"**🔬 Scientific Name:** {species_name}")
                
                # Common names
                if result['species'].get('commonNames'):
                    common_names = [name for name in result['species']['commonNames'] if name]
                    if common_names:
                        st.markdown(f"**🏷️ Common Names:** {', '.join(common_names[:3])}")
                
                # Family
                if result['species'].get('family'):
                    st.markdown(f"**👨‍👩‍👧‍👦 Family:** {result['species']['family']['scientificNameWithoutAuthor']}")
                
                # Genus
                if result['species'].get('genus'):
                    st.markdown(f"**🧬 Genus:** {result['species']['genus']['scientificNameWithoutAuthor']}")
                
                # Confidence with progress bar
                st.markdown(f"**📊 Confidence Score:** {confidence:.2%}")
                st.progress(confidence)

def main():
    # Header
    st.markdown('<h1 class="main-header">🌱 PlantNet Plant Identifier</h1>', unsafe_allow_html=True)
    st.markdown("**Identify plants from photos using AI-powered PlantNet API**")
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # API Key input
        api_key = st.text_input(
            "🔑 PlantNet API Key", 
            type="password",
            help="Get your free API key from https://my.plantnet.org/",
            placeholder= "2b10jv62kgvLEuWwJaBWZzsM"
        )
        
        # Project selection
        project_options = {
            "all": "🌍 All flora (worldwide)",
            "weurope": "🇪🇺 Western Europe", 
            "k-world-flora": "🌺 K World Flora",
            "weeds": "🌿 Weeds",
            "crop": "🌾 Crops"
        }
        
        project = st.selectbox(
            "🗺️ Select Project/Region",
            options=list(project_options.keys()),
            format_func=lambda x: project_options[x],
            help="Choose the appropriate flora database for your region"
        )
        
        # Organ type selection
        organ_options = {
            "leaf": "🍃 Leaf",
            "flower": "🌸 Flower", 
            "fruit": "🍎 Fruit",
            "bark": "🌳 Bark",
            "habit": "🌱 Habit (whole plant)"
        }
        
        organ_type = st.selectbox(
            "🔍 Plant Part",
            options=list(organ_options.keys()),
            format_func=lambda x: organ_options[x],
            help="What part of the plant is shown in your image?"
        )
        
        st.markdown("---")
        
        # Tips section
        with st.expander("💡 Tips for Better Results"):
            st.markdown("""
            - **Use clear, well-lit photos** 📸
            - **Focus on distinctive features** 🎯
            - **Avoid blurry or dark images** ❌
            - **Try different angles** 🔄
            - **Include multiple plant parts** 📋
            """)
        
        # About section
        with st.expander("ℹ️ About PlantNet"):
            st.markdown("""
            PlantNet is a collaborative platform that helps identify plants through photos using advanced AI.
            
            **Get your free API key:** [my.plantnet.org](https://my.plantnet.org/)
            """)
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # File upload section
        st.markdown('<div class="upload-section">', unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            "📸 Choose a plant image...",
            type=['png', 'jpg', 'jpeg'],
            help="Upload a clear photo of the plant you want to identify"
        )
        st.markdown('</div>', unsafe_allow_html=True)
        
        if uploaded_file is not None:
            # Display the uploaded image
            image = Image.open(uploaded_file)
            st.image(image, caption="📷 Uploaded Image", use_column_width=True)
            
            # Image details
            with st.expander("📋 Image Details"):
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric("Width", f"{image.size[0]}px")
                with col_b:
                    st.metric("Height", f"{image.size[1]}px")
                with col_c:
                    st.metric("Format", image.format)
    
    with col2:
        # Instructions and examples
        st.markdown("### 📖 How to Use")
        st.markdown("""
        1. **Get API Key** 🔑  
           Sign up at [my.plantnet.org](https://my.plantnet.org/)
        
        2. **Enter Key** ✍️  
           Paste it in the sidebar
        
        3. **Configure** ⚙️  
           Choose region and plant part
        
        4. **Upload Photo** 📸  
           Select a clear plant image
        
        5. **Identify** 🔍  
           Click the button below!
        """)
    
    # Identify button (full width)
    if uploaded_file is not None:
        if st.button("🔍 **Identify Plant**", type="primary", use_container_width=True):
            if not api_key:
                st.error("🔑 Please enter your PlantNet API key in the sidebar.")
                st.info("👉 Get your free API key from: https://my.plantnet.org/")
            else:
                with st.spinner("🔍 Analyzing image... This may take a few seconds"):
                    # Resize image if too large
                    if max(image.size) > 1024:
                        image.thumbnail((1024, 1024), Image.Resampling.LANCZOS)
                        st.info(f"📏 Image resized for optimal processing")
                    
                    # Identify the plant
                    results = identify_plant(image, api_key, project, organ_type)
                    
                    # Display results
                    st.markdown("---")
                    st.markdown("## 📊 Identification Results")
                    display_results(results)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 2rem;'>
        <p>🌱 <strong>PlantNet Plant Identifier</strong> | Powered by PlantNet API & Streamlit</p>
        <p>Made with ❤️ for plant enthusiasts</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
