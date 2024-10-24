# 🤖 Gemini AI Chat Interface

A sleek and interactive chat interface built with Streamlit for Google's Gemini AI model, featuring real-time parameter tuning and response generation.

![Gemini AI Chat Interface Demo](https://github.com/user-attachments/assets/e4ee86ea-0bac-478e-9495-077e8561485e)

## ✨ Features

- 💬 Interactive chat interface with Gemini AI
- 🎛️ Real-time temperature adjustment (0.0 to 1.0)
- 📝 Configurable max token length
- 🎯 Clean and intuitive user interface
- ✍️ Markdown rendering of responses
- 🔄 Dynamic model configuration updates

## 🛠️ Tech Stack

- Python 3.12
- Streamlit
- Google Generative AI
- Python-dotenv

## 📁 Project Structure

```
Project1/
├── src/
│   ├── config.py          # Configuration and environment setup
│   ├── gemini_adapter.py  # Gemini AI integration adapter
│   └── streamlit_app.py   # Main Streamlit application
├── .env                   # Environment variables (not in repo)
└── README.md             # Project documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- Google Cloud Gemini API key
- Git (optional)

### Installation

1. Clone the repository
```bash
git clone [https://github.com/yourusername/gemini-chat.git](https://github.com/sohail000/Simple-use-of-Gemini-pro-api.git)
cd gemini-chat
```

2. Install required packages
```bash
pip install -r requirements.txt
```

3. Set up environment variables
   - Create a `.env` file in the root directory
   - Add your Gemini API key:
```
GOOGLE_API_KEY=your_api_key_here
```

### 🎮 Usage

1. Navigate to the project directory
```bash
cd src
```

2. Run the Streamlit application
```bash
streamlit run streamlit_app.py
```

3. Access the interface at `http://localhost:8501`

## ⚙️ Configuration Options

### Temperature
- Range: 0.0 to 1.0
- Controls response creativity and randomness
- Higher values (e.g., 0.8) = more creative responses
- Lower values (e.g., 0.2) = more focused responses

### Max Tokens
- Range: 50 to 1000
- Controls maximum response length
- Adjust based on your needs

## 📝 Example Usage

1. Adjust temperature and max tokens in the sidebar
2. Enter your prompt in the text area
3. Click "Generate" to get AI response
4. Response will be displayed with markdown formatting

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Open issues
- Submit Pull Requests
- Suggest improvements

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Generative AI team for Gemini
- Streamlit team for the awesome framework

## 📧 Contact

Your Name - [Your Email/GitHub Profile]

Project Link: [[https://github.com/yourusername/gemini-chat](https://github.com/yourusername/gemini-chat](https://github.com/sohail000/Simple-use-of-Gemini-pro-api.git))

---
⭐ If you find this project helpful, don't forget to give it a star!
