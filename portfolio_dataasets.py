import yfinance as yf
import pandas as pd
import os



tickers = ["AAPL", "JNJ", "XOM", "BTC-USD"]


data = yf.download(
    tickers,
    start="2020-01-01",
    end="2025-01-01",
    auto_adjust=True,
    progress=False
)

prices = data["Close"].copy()
prices.reset_index(inplace=True)

prices.drop_duplicates(inplace=True)
prices.ffill(inplace=True)
prices.dropna(inplace=True)


for col in prices.columns[1:]:
    prices[col] = prices[col].round(2)



current_folder = os.getcwd()
file_path = os.path.join(current_folder, "Strategic_Portfolio_Cleaned_Data.csv")

prices.to_csv(file_path, index=False, float_format="%.2f")

print("✅ Dataset saved successfully!")
print("📂 File location:", file_path)
