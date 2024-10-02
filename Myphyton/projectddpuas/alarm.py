import os
import requests
from pyrogram import Client, filters
from TikTokApi import TikTokApi
from urllib.parse import urlparse, parse_qs

from PyroUbot import *

# Perintah untuk mendownload video TikTok
@PY.UBOT("tiktok")
async def _(client, message):
    # Ambil URL dari pesan
    url = message.text.split(" ", 1)[1] if len(message.command) > 1 else None

    if not url:
        await message.reply("Silakan berikan URL TikTok.")
        return

    try:
        # Buat instance dari TikTokApi
        api = TikTokApi()

        # Ambil video menggunakan URL
        video = api.video(url=url)
        
        # Download video
        video_data = video.bytes()  # Mengambil data video dalam bytes
        video_path = "downloaded_video.mp4"  # Path untuk menyimpan video

        # Tulis video ke dalam file
        with open(video_path, "wb") as f:
            f.write(video_data)

        # Kirim video kembali ke chat Telegram
        await client.send_video(chat_id=message.chat.id, video=video_path)

        # Hapus file setelah dikirim
        os.remove(video_path)

    except Exception as e:
        await message.reply(f"Error: {str(e)}")

# Perintah untuk mendownload video Instagram
@PY.UBOT("instagram")
async def download_instagram(client, message):
    if len(message.command) < 2:
        await message.reply("Penggunaan: /instagram [link_instagram]")
        return

    link = message.command[1]
    try:
        # Mengambil halaman dari Instagram
        response = requests.get(link)
        if response.status_code == 200:
            # Harus menggunakan BeautifulSoup atau regex untuk mengambil URL video dari HTML
            from bs4 import BeautifulSoup
            
            soup = BeautifulSoup(response.content, "html.parser")
            video_tag = soup.find("video")  # Mencari tag video
            if video_tag and 'src' in video_tag.attrs:
                video_url = video_tag['src']
                await client.send_video(chat_id=message.chat.id, video=video_url)
            else:
                await message.reply("Tidak dapat menemukan video dari link yang diberikan.")
        else:
            await message.reply("Tidak dapat mengakses link yang diberikan.")
    except Exception as e:
        await message.reply(f"Error: {str(e)}")
