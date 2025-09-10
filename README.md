# Ubuntu Requests - Image Fetcher

> *"I am because we are"* – Ubuntu Philosophy  

The **Ubuntu Image Fetcher** is a Python script that mindfully collects images from the web.  
It reflects the Ubuntu principles of **community, respect, sharing, and practicality** while teaching how to work with Python libraries like `requests` and `os`.

---

## 🌍 Project Overview

This program allows users to:
- Fetch images from one or more URLs.
- Save them into a dedicated directory (`Fetched_Images`).
- Respectfully handle errors and non-image URLs.
- Prevent duplicate downloads.
- Organize images for future sharing.

---

## ✨ Features

- ✅ Fetch multiple image URLs at once.  
- ✅ Auto-create `Fetched_Images` directory if missing.  
- ✅ Verify that downloads are valid **images** (via HTTP headers).  
- ✅ Prevent duplicate images using **SHA-256 hashing**.  
- ✅ Auto-generate filenames if not present in the URL.  
- ✅ Graceful error handling (connection failures, invalid URLs, etc.).  

---

## 🛠️ Requirements

- Python 3.7+  
- Libraries:
  - `requests` (for fetching images)

Install dependencies:
```bash
pip install requests
