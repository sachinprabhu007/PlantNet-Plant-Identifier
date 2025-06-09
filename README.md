# 🌱 PlantNet Plant Identifier

A beautiful Streamlit web application that identifies plants from photos using the PlantNet API.

![PlantNet Plant Identifier](https://img.shields.io/badge/Plant-Identifier-green?style=for-the-badge&logo=leaf)

## 🌟 Features

- **AI-Powered Plant Identification** using PlantNet's advanced machine learning
- **Multiple Flora Databases** (Worldwide, Europe, Weeds, Crops)
- **Beautiful User Interface** with modern design
- **Confidence Scoring** with color-coded results
- **Reference Images** for each identification
- **Responsive Design** that works on all devices

## 🚀 Live Demo

Visit the live application: https://plantnet-plant-identifier.onrender.com/

## 📸 Screenshots

![plantnet_1](https://github.com/user-attachments/assets/b4cefab2-abed-4da5-bc11-bb0572a8d05d)
![plantnet_2](https://github.com/user-attachments/assets/882b5048-6aa0-4be0-93af-63c260550267)
![plantnet_3](https://github.com/user-attachments/assets/d81caa93-aec3-47d9-9107-146acce9cb1e)

## 🛠️ Installation & Setup

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/plantnet-identifier.git
   cd plantnet-identifier
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Get PlantNet API Key**
   - Visit [my.plantnet.org](https://my.plantnet.org/)
   - Create a free account
   - Generate your API key

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

### Deploy on Render

1. **Fork this repository** to your GitHub account

2. **Create a new Web Service** on [Render](https://render.com/)
   - Connect your GitHub repository
   - Use the following settings:
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`

3. **Deploy** and your app will be live!

## 🔧 Configuration

The app supports multiple configuration options:

- **Flora Projects:**
  - All flora (worldwide)
  - Western Europe
  - K World Flora
  - Weeds
  - Crops

- **Plant Parts:**
  - Leaf
  - Flower
  - Fruit
  - Bark
  - Habit (whole plant)

## 📱 Usage

1. **Enter your PlantNet API key** in the sidebar
2. **Select the appropriate flora database** for your region
3. **Choose the plant part** shown in your image
4. **Upload a clear photo** of the plant
5. **Click "Identify Plant"** to get results

## 💡 Tips for Best Results

- Use clear, well-lit photos
- Focus on distinctive plant features
- Avoid blurry or dark images
- Try different angles if first attempt fails
- Include close-up shots of leaves, flowers, or fruits

## 🌍 Supported Regions

- **Worldwide** - Global flora database
- **Western Europe** - European plants
- **K World Flora** - Extended world flora
- **Weeds** - Common weeds
- **Crops** - Agricultural plants

## 🔑 API Key

This app requires a free PlantNet API key:

1. Visit [my.plantnet.org](https://my.plantnet.org/)
2. Create an account
3. Go to your account settings
4. Generate your private API key
5. Enter it in the app's sidebar

## 🏗️ Architecture

```
plantnet-identifier/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── .gitignore         # Git ignore file
└── assets/            # Static assets (optional)
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [PlantNet](https://plantnet.org/) for providing the amazing plant identification API
- [Streamlit](https://streamlit.io/) for the fantastic web app framework
- The plant photography community for inspiration

## 📧 Contact

Project Link: [https://github.com/sachinprabhu007/Plant_Detection](https://github.com/sachinprabhu007/PlantNet-Plant-Identifier)

---

Made with ❤️ for plant enthusiasts 🌱
