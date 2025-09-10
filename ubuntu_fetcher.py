import requests
import os
import hashlib
from urllib.parse import urlparse

def sanitize_filename(filename: str) -> str:
    """
    Ensure the filename is safe for saving.
    If empty or invalid, return a default filename.
    """
    if not filename or filename.isspace():
        return "downloaded_image.jpg"
    return filename

def generate_hash(content: bytes) -> str:
    """
    Generate a hash of the image content to detect duplicates.
    """
    return hashlib.sha256(content).hexdigest()

def fetch_and_save_image(url: str, save_dir="Fetched_Images", seen_hashes=None) -> None:
    """
    Fetch an image from the given URL and save it to the save_dir.
    Avoids duplicates and handles errors gracefully.
    """
    try:
        # Ensure save directory exists
        os.makedirs(save_dir, exist_ok=True)

        # Fetch image with timeout and headers
        headers = {"User-Agent": "UbuntuImageFetcher/1.0"}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Check Content-Type to confirm it's an image
        content_type = response.headers.get("Content-Type", "")
        if not content_type.startswith("image/"):
            print(f"✗ Skipped (not an image): {url}")
            return

        # Extract filename or fallback
        parsed_url = urlparse(url)
        filename = sanitize_filename(os.path.basename(parsed_url.path))

        # If no extension, add one from content-type
        if "." not in filename and "/" in content_type:
            ext = content_type.split("/")[-1]
            filename += f".{ext}"

        filepath = os.path.join(save_dir, filename)

        # Check for duplicates by hashing content
        content_hash = generate_hash(response.content)
        if seen_hashes is not None:
            if content_hash in seen_hashes:
                print(f"✗ Duplicate skipped: {filename}")
                return
            seen_hashes.add(content_hash)

        # Save image
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✓ Successfully fetched: {filename}")
        print(f"✓ Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Connection error for {url}: {e}")
    except Exception as e:
        print(f"✗ An error occurred with {url}: {e}")

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Allow multiple URLs (comma or space separated)
    urls = input("Please enter one or more image URLs (separated by space): ").split()

    if not urls:
        print("✗ No URLs provided.")
        return

    seen_hashes = set()
    for url in urls:
        fetch_and_save_image(url.strip(), seen_hashes=seen_hashes)

    print("\nConnection strengthened. Community enriched.")

if __name__ == "__main__":
    main()
