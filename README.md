# codealpha_tasks
## LLaMA 2 Chatbot

This project is a chatbot application built with the LLaMA 2 language model, utilizing the **Ollama** library for model interaction and **Streamlit** for the user interface. With this application, users can chat interactively with the LLaMA 2 model through a simple web interface.

### Features

- **Interactive Chat Interface**: Users can type messages and receive responses from LLaMA 2.
- **Session Memory**: Maintains conversation history within the chat session.
- **Local Setup**: Runs entirely on your local machine using Ollama, so no external API calls are required.

### Prerequisites

- **Python 3.x**: Make sure Python is installed on your machine.
- **Streamlit**: For the web interface.
- **Ollama**: For running LLaMA models locally.

### Installation

1. **Install required packages**:
```bash
pip install streamlit ollama
```
2. **Download the LLaMA 2 Model**: To use the LLaMA 2 model locally, download it via Ollama by running the following command in your terminal:
```bash
ollama pull llama2
```
This command will download and prepare the LLaMA 2 model for local use. You only need to do this once.
3. **Start Ollama**: Ensure that Ollama’s server is running so it can serve the LLaMA 2 model. If it’s not running, start it with:
```bash
ollama start
```

### Usage

1. **Run the Chatbot Application**: In the project directory, launch the Streamlit app by running:
```bash
streamlit run chatbot.py
```
2. **Interact with the Chatbot**:

- Open the provided URL in your browser (typically http://localhost:8501).
- Type a message in the input field and press Enter.
- The chatbot will respond using the LLaMA 2 model, and the conversation history will be displayed.

### Troubleshooting

- **404 Errors**: Ensure that Ollama is running, and that the LLaMA model is available.
- **Connection Issues**: Double-check that your Ollama server is accessible and running on the default port.
- **Model Errors**: Ensure that you’ve downloaded the model correctly with ollama pull llama2.
