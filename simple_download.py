#!/usr/bin/env python3
"""
Simple script to download sentence transformer models
"""

from sentence_transformers import SentenceTransformer

print("Downloading all-MiniLM-L6-v2...")
try:
    model1 = SentenceTransformer('all-MiniLM-L6-v2')
    print("✓ Successfully downloaded all-MiniLM-L6-v2")
except Exception as e:
    print(f"✗ Error downloading all-MiniLM-L6-v2: {e}")

print("\nDownloading msmarco-MiniLM-L-6-v3...")
try:
    model2 = SentenceTransformer('msmarco-MiniLM-L-6-v3')
    print("✓ Successfully downloaded msmarco-MiniLM-L-6-v3")
except Exception as e:
    print(f"✗ Error downloading msmarco-MiniLM-L-6-v3: {e}")

print("\nModel download complete!")