# app/load_dataset.py

import os
import pandas as pd
from datasets import load_dataset

def load_zenodo():
    
    df = pd.read_csv("data/Phishing_validation_emails.csv")
    df = df.rename(columns={'Email Text': 'text', 'Email Type': 'label'})
    df['label'] = df['label'].apply(lambda x: 1 if x=='Phishing Email' else 0)
    return df

def load_hf():
    df = pd.read_csv("data/huggingface_dataset.csv")
    df = df[['text', 'label']]
    return df


def load_ceas():
    df = pd.read_csv("data/CEAS_08.csv")
    df = df.rename(columns={'body': 'text'})
    df = df[['text','label']]
    return df

def save_combined(dfs):
    df = pd.concat(dfs, ignore_index=True).sample(frac=1).reset_index(drop=True)
    df.to_csv("data/combined_emails.csv", index=False)
    print("✅ Saved combined dataset with", len(df), "rows.")

if __name__ == "__main__":
    dfs = [load_zenodo(), load_hf(), load_ceas()]
    save_combined(dfs)
