# AI Chatbot with Gemma3:1b

This project delivers a secure, locally-run chatbot powered by Google DeepMind’s `gemma3:1b` model, a lightweight and state-of-the-art open-source AI model. Built using LangChain and Streamlit, the chatbot runs in a single Docker container, ensuring privacy, portability, and ease of use. The `gemma3:1b` model, part of Google’s esteemed Gemma 3 family, offers reliable and efficient conversational capabilities, making this chatbot a trusted choice for developers and users seeking a private, local AI solution.

## About Gemma 3

The Gemma 3 family, introduced by **Google DeepMind** in March 2025, represents a significant advancement in open-source AI models. Built from the same research and technology as Google’s Gemini 2.0 models, Gemma 3 is designed for efficiency and performance, supporting tasks like text generation, reasoning, and (in larger variants) multimodal capabilities such as image processing. The `gemma3:1b` model, used in this chatbot, is a 1-billion-parameter text-only model optimized for low-resource environments, trained on 2 trillion tokens of diverse text data, including web documents and code in over 140 languages. Its larger siblings (4B, 12B, and 27B) support vision-language tasks, enabling image analysis, but this chatbot leverages the compact 1B model for text-based conversations. Google DeepMind’s backing ensures the model’s reliability and cutting-edge performance, making this chatbot a trustworthy tool for local AI applications.

## Features

- **Trusted Development**: Powered by `gemma3:1b`, developed by Google DeepMind, a leader in AI research.
- **Local Execution**: Runs entirely on your machine in a Docker container, ensuring data privacy.
- **Lightweight Model**: The 1B-parameter `gemma3:1b` model is optimized for low-resource devices.
- **Streamlit Interface**: Offers an intuitive web-based UI for seamless chatting.
- **LangChain Integration**: Uses `ConversationChain` with memory for context-aware conversations.
- **Offline Capability**: After initial setup, no internet is required, ideal for air-gapped environments.
- **Single Container**: Combines Ollama server and Streamlit app for simplicity.

## Prerequisites

- **Docker**: Install [Docker](https://docs.docker.com/get-docker/) on your machine.
- A machine with at least:
  - **CPU**: Any modern CPU (e.g., dual-core or better).
  - **Memory**: 2GB RAM (4GB recommended for smoother performance).
  - **Storage**: ~1.3GB for the `gemma3:1b` model (~815MB) and Docker image (~500MB).
- Basic command-line knowledge.

## Resource Requirements

The `gemma3:1b` model is designed to be lightweight, making this chatbot accessible on modest hardware:

- **CPU**: No GPU is required; a standard CPU (e.g., Intel i3/i5 or AMD equivalent) is sufficient.
- **Memory**: 2GB RAM minimum, with 4GB recommended for optimal model loading and inference.
- **Storage**: Approximately 815MB for the `gemma3:1b` model, plus ~500MB for the Docker image.
- **Offline Operation**: After the initial Docker build and model download, the chatbot runs without internet, ensuring privacy and usability in offline settings.

This makes the chatbot ideal for laptops, desktops, or low-spec servers, requiring no high-end resources, unlike larger AI models.

## Project Structure
```commandline
ai_chatbot/
├── app.py              # Streamlit chatbot application using LangChain
├── start.sh            # Script to install Ollama, pull gemma3:1b, and run the app
├── Dockerfile          # Defines the Docker container
└── requirements.txt    # Python dependencies
```

## Setup Instructions

1. **Build the Docker image**:
   ```bash
   docker build -t ai-chatbot .
   ```

2. **Run the container**:
   ```bash
   docker run -d -p 8501:8501 ai-chatbot
   ```

Access the chatbot at http://0.0.0.0:8501 in your browser.
