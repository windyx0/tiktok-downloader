TikTok Downloader HD

A robust, Selenium-based library for downloading HD TikTok videos without watermarks using the SnapTik service.

Features

HD Quality: Uses advanced browser automation to trigger HD download buttons.

Bulk Download: Fetches video links from user profiles.

Resilient: Handles ads, popups, and connection timeouts.

Cookies Support: Allows using a Netscape cookie file for authenticated scraping.

Installation

Clone the repository or download the package.

Install dependencies:

pip install -r requirements.txt


Usage

Basic Example

from tiktok_downloader import TikTokDownloader

# Initialize
downloader = TikTokDownloader(
    download_dir="my_videos",
    cookies_path="cookies.txt",
    headless=False  # Set to True to run in background
)

# Download single video
url = "[https://www.tiktok.com/@user/video/1234567890](https://www.tiktok.com/@user/video/1234567890)"
downloader.download(url, filename_prefix="cool_video")

# Close driver
downloader.close()


Bulk Download from Channel

channel_url = "[https://www.tiktok.com/@realizeautomotive](https://www.tiktok.com/@realizeautomotive)"
links = downloader.get_user_videos(channel_url, limit=5)

for i, link in enumerate(links):
    downloader.download(link, filename_prefix=f"video_{i}")


Requirements

Python 3.6+

Google Chrome browser installed

cookies.txt (optional, but recommended for bulk scraping)

Disclaimer

This tool is for educational purposes only. Respect the copyright and terms of service of TikTok and SnapTik.