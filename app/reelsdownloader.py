from InstagramReelDownloader import ReelDownload


def download_reels(reels_url, file_dir):
    return ReelDownload(reels_url, file_dir)


reels = "https://www.instagram.com/reel/DFFnMMQMuU9/?igsh=MWFyOHQxdDZwejlzYg=="

ReelDownload(reels)
