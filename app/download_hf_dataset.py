# app/download_hf_dataset.py

from datasets import load_dataset
import pandas as pd

def download_and_save():
    print("📥 Downloading dataset from Hugging Face...")
    ds = load_dataset("ealvaradob/phishing-dataset", "combined_reduced", trust_remote_code=True)
    df = ds['train'].to_pandas()
    
    print("🧹 Cleaning and selecting columns...")
    df = df[['text', 'label']]  # keep only relevant columns
    
    print("💾 Saving to data/huggingface_dataset.csv...")
    df.to_csv("data/huggingface_dataset.csv", index=False)
    print("✅ Done!")

if __name__ == "__main__":
    download_and_save()
