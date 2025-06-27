import pandas as pd
import sqlite3

# Path to your CSV
csv_path = "C:/Users/tarun/OneDrive/Desktop/Youtube_Data_API/data/processed_2025-06-24_23-56-17.csv"
df = pd.read_csv(csv_path, parse_dates=["published_at", "fetched_at"])

# Connect to SQLite (it creates the DB file if it doesn't exist)
conn = sqlite3.connect("youtube_data.db")

# Load data into SQLite
df.to_sql("youtube_videos", conn, if_exists="append", index=False)

print("Data loaded into SQLite!")

