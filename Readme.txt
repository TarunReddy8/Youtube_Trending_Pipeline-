# 📈 YouTube Trending Data Automation and Power BI Dashboard
🚀 Project Overview
This project automates fetching trending YouTube videos using the YouTube Data API, processes and cleans the data, stores it in SQLite, and visualizes insights using Power BI with automated hourly refresh for near-real-time monitoring.

🛠️ Tech Stack
Python: Data ingestion, processing, and pipeline scripting

Apache Kafka: For scalable ingestion pipeline

SQLite (via ODBC): Lightweight storage for Power BI

Power BI: Advanced dashboard with auto-refresh

Windows Task Scheduler: Automation of ETL pipelines

Docker Compose: Container orchestration

🗂️ Project Workflow
1️⃣ Data Ingestion
youtube_kafka_producer.py fetches trending video data via YouTube API.

kafka_to_raw_storage.py consumes and stores raw JSON data.

2️⃣ Data Processing
process_raw_data.py cleans, flattens, and converts raw data into structured CSV.

verify_data.py verifies data quality before loading.

3️⃣ Data Loading
load_csv_to_sqlite.py loads the cleaned CSV into SQLite database (youtube_data.db).

4️⃣ Visualization
Built an advanced Power BI dashboard with:

Top 10 trending videos by views

Channel-wise performance

Views vs likes scatter analysis

Publishing time heatmaps

KPI Cards (Total Views, Total Likes, Most Active Channel)

Custom dark theme and slicers for interactivity

Hourly auto-refresh using Power BI Gateway

5️⃣ Automation
Created two pipelines:

pipeline_fetch_store.bat: Fetch and store data.

pipeline_load_process.bat: Load and process data into SQLite.

Scheduled these pipelines using Windows Task Scheduler.

Configured Power BI Gateway for auto-refresh aligned with pipeline updates.

⚡ Features
✅ Automated ETL pipeline for trending YouTube data
✅ Clean data processing and verification scripts
✅ Advanced Power BI dashboard for near-real-time monitoring
✅ Fully automated refresh using Power BI Gateway
✅ Organized for scalable enhancements (e.g., Snowflake/AWS pipeline migration)