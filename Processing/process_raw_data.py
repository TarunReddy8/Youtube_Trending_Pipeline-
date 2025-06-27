import os
import json
import pandas as pd
from datetime import datetime

RAW_DIR = "raw"
PROCESSED_DIR = "data/processed"
os.makedirs(PROCESSED_DIR, exist_ok=True)

records = []

for filename in os.listdir(RAW_DIR):
    if filename.endswith(".json"):
        file_path = os.path.join(RAW_DIR, filename)
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            snippet = data.get("snippet")
            stats = data.get("statistics")

            # Skip if required fields are missing
            if not snippet or not stats:
                print(f"Skipping (missing snippet/stats): {filename}")
                continue
            if "publishedAt" not in snippet:
                print(f"Skipping (missing publishedAt): {filename}")
                continue

            record = {
                "video_id": data.get("id"),
                "title": snippet.get("title"),
                "published_at": snippet["publishedAt"],
                "channel_title": snippet.get("channelTitle"),
                "view_count": stats.get("viewCount"),
                "like_count": stats.get("likeCount"),
                "comment_count": stats.get("commentCount"),
                "fetched_at": filename.split("_")[-1].replace(".json", ""),
            }
            records.append(record)

df = pd.DataFrame(records)
# Add fallback columns if missing
if "fetched_at" not in df.columns:
    df["fetched_at"] = datetime.now()

if "published_at" not in df.columns:
    df["published_at"] = pd.NaT

df["fetched_at"] = pd.to_datetime(df["fetched_at"], errors="coerce")
df["published_at"] = pd.to_datetime(df["published_at"], errors="coerce")

# Save cleaned data
output_file = os.path.join(PROCESSED_DIR, f"processed_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv")
df.to_csv(output_file, index=False)
print(f"Processed {len(df)} records and saved to: {output_file}")
