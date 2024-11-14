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

1. **Install required packages**: Install required packages: Run the following command to install the necessary dependencies:
```bash
pip install -r requirements.txt
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
- Use the Settings sidebar to adjust the chatbot's personality.
- Type a message in the input field and press Enter.
- Click Clear Chat History to reset the conversation.

### Troubleshooting

- **404 Errors**: Ensure that Ollama is running, and that the LLaMA model is available.
- **Connection Issues**: Double-check that your Ollama server is accessible and running on the default port.
- **Model Errors**: Ensure that you’ve downloaded the model correctly with ollama pull llama2.

## Stock & Crypto Price Tracker in INR

This application is a stock and cryptocurrency portfolio tracker built using Streamlit, which allows users to track and manage investments in various assets. It uses Google Finance for real-time prices and supports automatic conversion to INR for U.S. and Indian stock exchanges.

### Features

- **Portfolio Tracker**: Add and remove stocks/cryptocurrencies from your portfolio.
- **Current Prices**: Display the latest prices of top stocks and cryptocurrencies in INR.
- **Gain/Loss Tracking**: Real-time gain/loss calculations based on current and purchase prices.
- **Automatic Currency Conversion**: Convert USD-based stocks to INR based on the current USD-INR exchange rate.

### Requirements

- Python 3.7+
- Streamlit
- Requests
- BeautifulSoup (bs4)
- Pandas

### Installation

1. **Install the dependencies**:
```bash
pip install -r requirements.txt
```

2. **Run the Streamlit app**:
```bash
streamlit run PortFolioTracker.py
```

### Usage

1. **Portfolio Tracker**:
- Select a stock or cryptocurrency from the dropdown menu or add a custom ticker.
- Enter the number of shares and add it to your portfolio.
- View a summary of your portfolio, including gain/loss calculations and portfolio value.
- You can also remove the assets from your portfolio.

2. **Current Prices**:
- View a table of current prices for top assets in INR.
