# -*- coding: utf-8 -*-
"""
@author:XuMing(xuming624@qq.com)
@description: 
"""
import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime
from dateutil import tz
from loguru import logger
pwd_path = os.path.abspath(os.path.dirname(__file__))
env_file = os.path.join(pwd_path, ".env")


def to_podcast(api_key, article_url="https://github.com/shibing624/AIDailyNews/blob/main/news/dailyNews.md"):
    audio_url = ""
    cover_url = ""

    # API URL
    url = "https://api.coze.cn/v1/workflow/run"

    # Headers including Authorization
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Request payload
    data = {
        "workflow_id": "7433057778338578447",
        "parameters": {
            "user_id": "12345",
            "article_url": article_url
        }
    }

    # Send POST request
    response = requests.post(url, headers=headers, json=data)

    # Check for HTTP errors
    if response.status_code == 200:
        try:
            # Parse the response JSON
            result = response.json()

            try:
                print("Request Successful!")
                data = result.get("data")
                print(f"Data: {data}")
                data_json = json.loads(data)

                # Extract and print relevant data
                audio_url = data_json.get("audio")
                cover_url = data_json.get("cover_url")
            except Exception as e:
                print(f"Error in Response: {result.get('msg')}, error: {e}")
        except ValueError as e:
            print(f"Error parsing JSON response: {e}")
    else:
        print(f"HTTP Error: {response.status_code}")
    return audio_url, cover_url


if __name__ == "__main__":
    if os.path.exists(env_file):
        load_dotenv(env_file, override=True)
        logger.info(f"env_file:{env_file}, {os.environ}")
    else:
        logger.warning(f"env_file not found:{env_file}")
    CZ_API_KEY = os.environ.get("CZ_API_KEY")
    news_url = "https://github.com/shibing624/AIDailyNews/blob/main/news/dailyNews.md"
    audio_url, cover_url = to_podcast(CZ_API_KEY, news_url)
    print(f"Audio URL: {audio_url}")
    print(f"Cover URL: {cover_url}")

    # 在原新闻md文件中添加音频和封面链接
    time_zone = tz.gettz("Asia/Shanghai")
    today_with_timezone = datetime.today().astimezone(time_zone)
    today_str = today_with_timezone.strftime("%Y-%m-%d")

    current_directory = os.path.dirname(os.path.abspath(__file__))
    # 获取当前项目的根目录
    news_folder = f"{current_directory}/news/"
    logger.info(f"news folder: {news_folder}")
    os.makedirs(news_folder, exist_ok=True)
    md_title = f"Daily News #{today_str}"
    audio_data = f"""
Podcast: [🎧 Listen]({audio_url})

[![Article Cover]({cover_url})]({audio_url})

"""

    md_path = os.path.join(news_folder, f"dailyNews_{today_str}.md")
    backup_md_path = os.path.join(news_folder, f"dailyNews.md")
    # 合并音频和封面链接到新闻md文件
    with open(md_path, "r") as fp:
        content = fp.read()
        c = content.split("## ", 1)[1]
        content = "## " + c
        with open(md_path, "w") as fp:
            fp.write(audio_data + content)
            logger.info(f"write to file: {md_path}")
        # copy file to backup_md_path file
        with open(backup_md_path, "w") as fp:
            fp.write(audio_data + content)
            logger.debug(f"write to file: {backup_md_path}")
