import re
import time
from tiktok_downloader import TikTokDownloader

def main():
    # --- CONFIG ---
    DOWNLOAD_DIR = "tiktok_downloads"
    COOKIE_FILE = "cookies.txt"
    
    print("--- TikTok HD Downloader Client ---")
    
    channel = input("Target Channel URL: ").strip()
    if not channel:
        channel = "https://www.tiktok.com/@realizeautomotive"
        
    try:
        limit = int(input("Video Limit (Default 10): ") or 10)
    except ValueError:
        limit = 10

    # Init Library
    dl = TikTokDownloader(download_dir=DOWNLOAD_DIR, cookies_path=COOKIE_FILE)

    try:
        # 1. Fetch Links
        links = dl.get_user_videos(channel, limit)
        print(f"[*] Found {len(links)} videos.")

        # 2. Download Loop
        success_count = 0
        
        for i, link in enumerate(links):
            # Extract ID from URL
            vid_id = re.findall(r'/video/(\d+)', link)
            vid_id = vid_id[0] if vid_id else f"video_{i}"
            
            if dl.download(link, filename_prefix=vid_id):
                success_count += 1
            
            # Short pause to be polite
            time.sleep(0.3)

    except KeyboardInterrupt:
        print("\n[!] Interrupted by user.")
    finally:
        dl.close()
        print(f"\n=== Finished: {success_count} downloaded ===")

if __name__ == "__main__":
    main()