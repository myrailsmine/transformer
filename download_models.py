#!/usr/bin/env python3
"""
Script to download sentence transformer models
"""

import os
from sentence_transformers import SentenceTransformer

def download_model(model_name, cache_folder):
    """Download a sentence transformer model"""
    print(f"Downloading {model_name}...")
    try:
        model = SentenceTransformer(model_name, cache_folder=cache_folder)
        model_path = os.path.join(cache_folder, model_name.replace('/', '_'))
        model.save(model_path)
        print(f"✓ Successfully downloaded {model_name} to {model_path}")
        return True
    except Exception as e:
        print(f"✗ Error downloading {model_name}: {e}")
        return False

def main():
    """Download the specified models"""
    models = [
        "all-MiniLM-L6-v2",
        "msmarco-MiniLM-L-6-v3"
    ]
    
    # Use current directory for cache
    cache_folder = "./models_cache"
    os.makedirs(cache_folder, exist_ok=True)
    
    print("Starting model downloads...")
    print(f"Download location: {os.path.abspath(cache_folder)}")
    print("-" * 50)
    
    success_count = 0
    for model_name in models:
        if download_model(model_name, cache_folder):
            success_count += 1
    
    print("-" * 50)
    print(f"Download complete: {success_count}/{len(models)} models downloaded successfully")

if __name__ == "__main__":
    main()