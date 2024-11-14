import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

assets = {
    "AAPL (NASDAQ)": "AAPL:NASDAQ",
    "MSFT (NASDAQ)": "MSFT:NASDAQ",
    "GOOGL (NASDAQ)": "GOOGL:NASDAQ",
    "AMZN (NASDAQ)": "AMZN:NASDAQ",
    "TSLA (NASDAQ)": "TSLA:NASDAQ",
    "IBM (NYSE)":"IBM:NYSE",
    "ORCL (NYSE)": "ORCL:NYSE",
    
    "RELIANCE (NSE)": "RELIANCE:NSE",
    "TCS (NSE)": "TCS:NSE",
    "INFY (NSE)": "INFY:NSE",
    "ICICIBANK (NSE)": "ICICIBANK:NSE",
    "HINDUNILVR (NSE)": "HINDUNILVR:NSE",
    "Nifty 50 (NSE)": "NIFTY_50:INDEXNSE",
    "SENSEX (BOM)": "SENSEX:INDEXBOM",
    "SBI (NSE)": "SBIN:NSE",
    "BHEL (NSE)": "BHEL:NSE",

    "Bitcoin (BTC)": "BTC-INR",
    "Ethereum (ETH)": "ETH-INR",
    "Ripple (XRP)": "XRP-INR",
    "Litecoin (LTC)": "LTC-INR",
    "Tether (USDT)": "USDT-INR"
}

def fetch_stock_price_google(ticker_symbol):
    url = f"https://www.google.com/finance/quote/{ticker_symbol}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    price_element = soup.find("div", {"class": "YMlKec fxKbKc"})
    if price_element:
        return float(price_element.text.replace(",", "").replace("₹", "").replace("$", ""))
    return None

def fetch_usd_to_inr():
    url = "https://www.google.com/finance/quote/USD-INR"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    rate_element = soup.find("div", {"class": "YMlKec fxKbKc"})
    if rate_element:
        return float(rate_element.text.replace(",", ""))
    return None

def fetch_all_prices(assets, usd_to_inr=None):
    prices = {}
    for name, ticker in assets.items():
        price = fetch_stock_price_google(ticker)
        # Convert to INR if it's an international stock
        if price and usd_to_inr and (ticker.endswith("NASDAQ") or ticker.endswith("NYSE")):
            price *= usd_to_inr
        prices[name] = price
    return prices

def add_stock(ticker, shares, usd_to_inr):
    purchase_price = fetch_stock_price_google(ticker)
    if purchase_price:
        if ticker.endswith("NASDAQ") or ticker.endswith("NYSE"):
            purchase_price_inr = purchase_price * usd_to_inr
        else:
            purchase_price_inr = purchase_price
        
        st.session_state.portfolio[ticker] = {
            "shares": shares,
            "purchase_price": purchase_price_inr,
            "current_price": purchase_price_inr
        }
        st.success(f"Added {ticker} to portfolio with purchase price ₹{purchase_price_inr:.2f}!")
    else:
        st.error("Invalid ticker symbol or unable to fetch data. Please try again.")

def remove_stock(ticker):
    if ticker in st.session_state.portfolio:
        del st.session_state.portfolio[ticker]
        st.success(f"Removed {ticker} from portfolio!")
    else:
        st.error("Stock not found in portfolio.")

if "portfolio" not in st.session_state:
    st.session_state.portfolio = {}

st.set_page_config("Stock Price Tracker")

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select Page", ["Portfolio Tracker", "Current Prices"])

usd_to_inr = fetch_usd_to_inr()


if page == "Portfolio Tracker":
    st.title("Stock & Crypto Price Tracker in INR")

    st.header("Add Stock")

    selected_stock = st.selectbox("Select Stock Ticker", ["Custom"] + list(assets.keys()))
    if selected_stock == "Custom":
        ticker_input = st.text_input("Enter Stock Ticker with Exchange (e.g., TCS:NSE, AAPL:NASDAQ)", "").upper()
    else:
        ticker_input = assets[selected_stock]

    shares_input = st.number_input("Number of Shares", min_value=1, value=1)
    add_button = st.button("Add Stock")

    if add_button and ticker_input and usd_to_inr:
        add_stock(ticker_input, shares_input, usd_to_inr)

    st.header("Remove Stock")
    with st.form("remove_stock_form"):
        ticker_remove = st.selectbox("Select Stock to Remove", list(st.session_state.portfolio.keys()))
        remove_button = st.form_submit_button("Remove Stock")
        
        if remove_button and ticker_remove:
            remove_stock(ticker_remove)

    if st.session_state.portfolio:
        st.header("Portfolio Summary")
        
        portfolio_data = []
        for ticker, info in st.session_state.portfolio.items():
            current_price = fetch_stock_price_google(ticker)
            if ticker.endswith("NASDAQ") or ticker.endswith("NYSE"):
                current_price_inr = current_price * usd_to_inr
            else:
                current_price_inr = current_price
            
            st.session_state.portfolio[ticker]["current_price"] = current_price_inr
            
            shares = info["shares"]
            purchase_price = info["purchase_price"]
            total_purchase_value = shares * purchase_price
            current_value = shares * current_price_inr
            gain_loss = current_value - total_purchase_value

            portfolio_data.append({
                "Ticker": ticker,
                "Shares": shares,
                "Purchase Price (INR)": purchase_price,
                "Current Price (INR)": current_price_inr,
                "Total Purchase Value (INR)": total_purchase_value,
                "Current Value (INR)": current_value,
                "Gain/Loss (INR)": gain_loss
            })

        portfolio_df = pd.DataFrame(portfolio_data)
        
        st.dataframe(portfolio_df)

        total_value = portfolio_df["Current Value (INR)"].sum()
        total_gain_loss = portfolio_df["Gain/Loss (INR)"].sum()
        st.write(f"**Total Portfolio Value (INR):** ₹{total_value:,.2f}")
        st.write(f"**Total Gain/Loss (INR):** ₹{total_gain_loss:,.2f}")

        st.header("Portfolio Gain/Loss by Stock")
        st.bar_chart(portfolio_df.set_index("Ticker")["Gain/Loss (INR)"])

    else:
        st.write("Your portfolio is empty. Add some stocks to get started!")
elif page == "Current Prices":
    st.title("Current Prices of Top Assets in INR")

    indian_prices = fetch_all_prices(assets,usd_to_inr)
    indian_df = pd.DataFrame(list(indian_prices.items()), columns=["Stock", "Current Price (INR)"])
    st.dataframe(indian_df)