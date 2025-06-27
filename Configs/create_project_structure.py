# PHASE 1: SETUP - Directory structure creation and Docker Compose for Kafka, Spark, PostgreSQL

# File: setup/create_project_structure.py
import os

folders = [
    "ingestion",
    "processing",
    "dashboard",
    "data/raw",
    "Loading"
    "Pipelines"
    "configs"
]

files = [
    "Readme.txt",
]
def create_structure():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created: {folder}")

if __name__ == "__main__":
    create_structure()
