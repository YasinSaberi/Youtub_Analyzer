# First, install the required library:
# pip install yt-dlp

import yt_dlp
import sys

def extract_playlist_titles(playlist_url, output_file='videos.txt'):
    """
    Extracts video titles from a YouTube playlist and saves them to a text file.
    
    Args:
    playlist_url (str): The URL of the YouTube playlist.
    output_file (str): The name of the output text file.
    """
    ydl_opts = {
        'extract_flat': True,  # Only extract info, no download
        'quiet': True,         # Suppress output
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(playlist_url, download=False)
            titles = []
            
            if 'entries' in info:
                for entry in info['entries']:
                    if entry and 'title' in entry:
                        titles.append(entry['title'])
            
            # Write titles to file
            with open(output_file, 'w', encoding='utf-8') as f:
                for title in titles:
                    f.write(title + '\n')
            
            print(f"Successfully saved {len(titles)} video titles to {output_file}")
            
        except Exception as e:
            print(f"Error: {e}")

# Usage:
if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Enter the YouTube playlist URL: ").strip()
    
    extract_playlist_titles(url)