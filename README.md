# Transformer Models Repository

This repository contains pre-trained sentence transformer models for various NLP tasks.

## Models Included

### 1. all-MiniLM-L6-v2
- **Size**: ~1GB
- **Purpose**: General-purpose sentence embeddings
- **Description**: A versatile model for semantic similarity, clustering, and information retrieval tasks

### 2. msmarco-MiniLM-L-6-v3  
- **Size**: ~976MB
- **Purpose**: MS MARCO optimized sentence embeddings
- **Description**: Optimized for passage ranking and information retrieval tasks

## Important: Downloading Large Files

⚠️ **This repository uses Git LFS (Large File Storage) for model files**

To properly download all model files with correct sizes:

### Option 1: Clone with Git LFS (Recommended)
```bash
# Install Git LFS first
git lfs install

# Clone the repository
git clone https://github.com/myrailsmine/transformer.git
cd transformer

# Verify file sizes
du -sh all-MiniLM-L6-v2/ msmarco-MiniLM-L-6-v3/
```

### Option 2: Download Individual Models
If you don't want to install Git LFS, you can download models directly:

```python
from sentence_transformers import SentenceTransformer

# Download all-MiniLM-L6-v2
model1 = SentenceTransformer('all-MiniLM-L6-v2')

# Download msmarco-MiniLM-L-6-v3  
model2 = SentenceTransformer('msmarco-MiniLM-L-6-v3')
```

## Usage

```python
from sentence_transformers import SentenceTransformer

# Load local model
model = SentenceTransformer('./all-MiniLM-L6-v2')

# Generate embeddings
sentences = ['This is an example sentence', 'Each sentence is converted']
embeddings = model.encode(sentences)
print(embeddings.shape)
```

## File Structure

Each model directory contains:
- `pytorch_model.bin` - PyTorch model weights
- `tf_model.h5` - TensorFlow model weights  
- `model.safetensors` - SafeTensors format
- `config.json` - Model configuration
- `tokenizer.json` - Tokenizer configuration
- `onnx/` - ONNX optimized models
- `openvino/` - OpenVINO optimized models

## Troubleshooting

**Problem**: Model files are small (few KB) after download
**Solution**: Install Git LFS and re-clone the repository

**Problem**: "Git LFS not found" error
**Solution**: Install Git LFS: 
- macOS: `brew install git-lfs`
- Ubuntu: `sudo apt install git-lfs`
- Windows: Download from https://git-lfs.github.io/

## Scripts Included

- `hf_download.py` - Script to download models from HuggingFace Hub
- `simple_download.py` - Simple download script
- Download scripts for reproducibility