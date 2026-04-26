# AES Image Encryption & Mode Analysis

## Overview
This project demonstrates how different AES encryption modes behave when applied to structured data such as images.

Using ECB, CBC, and CTR modes, the program encrypts the raw pixel data of an image and reconstructs encrypted images to visually compare how each mode affects data confidentiality.

---

## Objectives
- Understand how AES encryption works on real-world data  
- Compare ECB, CBC, and CTR encryption modes  
- Visualize security weaknesses in ECB mode  
- Demonstrate why CBC and CTR provide stronger confidentiality  

---

## Features
- Loads and processes image pixel data  
- Encrypts image using:
  - AES-ECB  
  - AES-CBC  
  - AES-CTR  
- Reconstructs encrypted images from ciphertext  
- Prints first 32 bytes of ciphertext for each mode  
- Saves output images for visual comparison  

---

## Technologies Used
- Python  
- PyCryptodome  
- Pillow (PIL)  
- AES Encryption  

---

## Results (Key Insight)

### ECB Mode (Insecure)
![ECB](screenshots/ecb_encrypted.png)

- Visible patterns from the original image remain  
- Demonstrates why ECB is insecure for structured data  

---

### CBC Mode
![CBC](screenshots/cbc_encrypted.png)

- Patterns are removed  
- Output appears randomized  

---

### CTR Mode
![CTR](screenshots/ctr_encrypted.png)

- Also produces randomized output  
- Behaves like a stream cipher  

---

## How It Works
1. Load image and extract RGB pixel bytes  
2. Encrypt pixel data using AES in different modes  
3. Reconstruct image using encrypted bytes  
4. Compare visual output  

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/raperzac05-crypto/aes-image-encryption.git
cd aes-image-encryption

### 2. Install dependancies
pip install pycryptodome pillow

### 3. Run the program
py image_encryption.py
