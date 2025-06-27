import sqlite3
import pandas as pd

conn = sqlite3.connect("youtube_data.db")

# Preview first 5 rows
df = pd.read_sql("SELECT * FROM youtube_videos LIMIT 5;", conn)
print(df)


df = pd.read_sql("""
SELECT title, view_count, like_count, comment_count
FROM youtube_videos
ORDER BY view_count DESC
LIMIT 10
""", conn)
print(df)

# 1. Top 10 Most Viewed Videos
df = pd.read_sql("""
SELECT title, channel_title, view_count
FROM youtube_videos
ORDER BY view_count DESC
LIMIT 10;
""", conn)
print(df)

#2. Top 10 Most Liked Videos
df = pd.read_sql("""
SELECT title, channel_title, like_count
FROM youtube_videos
ORDER BY like_count DESC
LIMIT 10;
""", conn)
print(df)

# 3. Most Commented Videos
df = pd.read_sql("""
SELECT title, channel_title, comment_count
FROM youtube_videos
ORDER BY comment_count DESC
LIMIT 10;
""", conn)
print(df)

# 4. Recently Published Videos
df = pd.read_sql("""
SELECT title, channel_title, published_at
FROM youtube_videos
ORDER BY published_at DESC
LIMIT 10;
""", conn)
print(df)

# 5. Engagement Rate (Likes + Comments per 1000 Views)
df = pd.read_sql("""
SELECT 
    title,
    channel_title,
    view_count,
    like_count,
    comment_count,
    ROUND(((like_count + comment_count) * 1000.0) / NULLIF(view_count, 0), 2) AS engagement_per_1000_views
FROM youtube_videos
ORDER BY engagement_per_1000_views DESC
LIMIT 10;
""", conn)
print(df)

#6. Videos with Missing Data
df = pd.read_sql("""
SELECT * 
FROM youtube_videos
WHERE like_count IS NULL OR comment_count IS NULL OR view_count IS NULL;
""", conn)
print(df)

#7. Group by Channel – Total Views and Likes
df = pd.read_sql("""
SELECT 
    channel_title, 
    COUNT(*) AS total_videos,
    SUM(view_count) AS total_views,
    SUM(like_count) AS total_likes
FROM youtube_videos
GROUP BY channel_title
ORDER BY total_views DESC
LIMIT 10;
""", conn)
print(df)




