#!/usr/bin/env python3
"""
Download models using huggingface-hub
"""

from huggingface_hub import snapshot_download
import os

def download_model(repo_id, local_dir):
    """Download a model from HuggingFace Hub"""
    print(f"Downloading {repo_id}...")
    try:
        snapshot_download(
            repo_id=repo_id,
            local_dir=local_dir,
            local_dir_use_symlinks=False
        )
        print(f"✓ Successfully downloaded {repo_id} to {local_dir}")
        return True
    except Exception as e:
        print(f"✗ Error downloading {repo_id}: {e}")
        return False

def main():
    """Download the specified models"""
    models = [
        ("sentence-transformers/all-MiniLM-L6-v2", "./all-MiniLM-L6-v2"),
        ("sentence-transformers/msmarco-MiniLM-L-6-v3", "./msmarco-MiniLM-L-6-v3")
    ]
    
    print("Starting model downloads...")
    print("-" * 50)
    
    success_count = 0
    for repo_id, local_dir in models:
        if download_model(repo_id, local_dir):
            success_count += 1
    
    print("-" * 50)
    print(f"Download complete: {success_count}/{len(models)} models downloaded successfully")

if __name__ == "__main__":
    main()