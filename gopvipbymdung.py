# -*- coding: utf-8 -*-
den='\x1b[1;90m'
luc='\x1b[1;32m'
trang='\x1b[1;37m'
red='\x1b[1;31m'
vang='\x1b[1;33m'
tim='\x1b[1;35m'
lamd='\x1b[1;34m'
lam='\x1b[1;36m'
purple='\x1b[35m'
hong='\x1b[95m'
blue = '\x1b[1;34m'
green = '\x1b[1;32m'

import os
import sys
import subprocess

REQUIRED_MODULES = {
    "requests": "requests",
    "pystyle": "pystyle",
    "colorama": "colorama",
    "bs4": "beautifulsoup4",
    "selenium": "selenium",
    "mechanize": "mechanize",
    "webdriver_manager": "webdriver-manager",
    "paho.mqtt": "paho-mqtt",
    "pyfiglet": "pyfiglet",
    "psutil": "psutil",
    "termcolor": "termcolor",
    "httpx": "httpx",
    "zlapi": "zlapi",
    "gtts": "gtts",
}

missing = []

for module, package in REQUIRED_MODULES.items():
    try:
        __import__(module)
    except ImportError:
        missing.append(package)

if missing:
    print("[*] Đang cài đặt thư viện:", ", ".join(missing))
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "--upgrade"] + missing
    )
    print("[✓] Cài đặt hoàn tất!")

import requests
import json
import pyfiglet
from datetime import datetime
from time import sleep, strftime
from sys import platform

from pystyle import (
    Add,
    Center,
    Anime,
    Colors,
    Colorate,
    Write,
    System
)

banners = f"""⠀⠀⠀⠀⢨⠊⠀⢀⢀⠀⠀⠀⠈⠺⡵⡱⠀⠀⠀⢠⠃⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⢰⡁⠉⠊⠙⢎⣆⠀⠀⠀⠀⢩⢀⠜⠀⠀⠀
⠀⠀⠀⢠⠃⠀⠀⢸⢸⡀⠀⠀⠀⠀⠘⢷⡡⠀⠀⠎⠀⢰⣧⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⠈⣐⢤⣀⣀⢙⠦⠀⠀⠀⠀⡇⠀⠀⠀⠀
⠀⠀⢀⠃⠀⠀⠀⡌⢸⠃⠀⠀⠀⢀⠀⠀⠑⢧⡸⠀⢀⣿⢻⡀⠀⠀⣻⠀⠀⠀⠀⠀⣠⡴⠛⠉⠀⠀⠀⠑⢝⣦⠀⠀⠀⢰⠠⠁⠀⠀
⠀⠀⠌⠀⠀⠀⡘⣖⣄⢃⠀⠀⠀⠈⢦⡀⠀⡜⡇⠀⣼⠃⠈⢷⣶⢿⠟⠀⠀⠀⢠⠞⠁⠀⣀⠄⠂⣶⣶⣦⠆⠋⠓⠀⢀⣀⡇⠀⠀⠀
⠡⡀⡇⠀⢰⣧⢱⠊⠘⡈⠄⠀⠀⡀⠘⣿⢦⣡⢡⢰⡇⢀⠤⠊⡡⠃⠀⠀⢀⡴⠁⢀⠔⠊⠀⠀⢠⣿⠟⠁⠀⢀⠀⢀⠾⣤⣀⠀⠀⡠
⡀⠱⡇⠀⡆⢃⠀⠀⠀⠃⠀⠀⠀⣧⣀⣹⡄⠙⡾⡏⠀⡌⣠⡾⠁⠀⠀⣠⠊⢠⠔⠁⠀⠀⠀⠀⣸⡏⠀⠀⠀⢨⣪⡄⢻⣥⠫⡳⢊⣴
⠀⠀⢡⢠⠀⢸⡆⠀⣀⠀⠀⠀⠀⠈⣛⢛⣁⣀⠘⣧⣀⢱⡿⠀⠀⢀⡔⢁⢔⠕⠉⠐⣄⣠⠤⠶⠛⠁⢀⣀⠀⠀⠉⠁⠈⠷⣞⠔⡕⣿
⢄⡀⠘⢸⠀⣘⠇⠀⠀⠀⠀⠀⠀⠀⠀⠉⠐⠤⡑⢎⡉⢨⠁⠀⣠⢏⠔⠁⠘⣤⠴⢊⣡⣤⠴⠖⠒⠻⠧⣐⠓⠀⠀⠀⠀⠈⠀⡜⠀⠇
⠤⡈⠑⠇⠡⣻⢠⠊⠉⠉⠉⠑⠒⠤⣀⠀⠀⠀⠈⣾⣄⢘⣫⣜⠮⢿⣆⡴⢊⢥⡪⠛⠉⠀⠀⠀⠀⢀⠄⠂⠁⠀⠀⠀⠀⠀⠀⢧⡀⠈
⠁⠈⠑⠼⣀⣁⣇⠀⣴⡉⠉⠉⠀⠒⡢⠌⣐⡂⠶⣘⢾⡾⠿⢅⠀⣠⣶⡿⠓⠁⢠⠖⣦⡄⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢎⢳
⠀⠀⠀⠀⠉⣇⣿⢜⠙⢷⡄⠀⠀⠀⣄⣠⠼⢶⡛⣡⢴⠀⢀⠛⠱⡀⠀⠀⠀⠀⢀⠎⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡋⠮⡈
⠀⠀⢀⣖⠂⢽⡈⠀⠈⠑⠻⡦⠖⢋⣁⡴⠴⠊⣉⡠⢻⡖⠪⢄⡀⢈⠆⠀⠀⢠⠊⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠤⡵⢤⣃
⠀⠀⠸⢠⡯⣖⢵⡀⠀⠀⣠⣤⠮⠋⠁⠀⠀⠀⠀⠀⠸⣌⢆⢱⡾⠃⢀⠠⠔⠁⣀⢸⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⡸⠚⡸⠈⠁
⠤⢀⣀⢇⢡⠸⡗⢔⡄⠸⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⡩⠔⢉⡠⠔⠂⠉⢀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢁⠎⢀⡠⠔
⠀⠀⠀⠘⡌⢦⡃⣎⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠠⡟⠠⡐⣋⠤⠀⣀⠤⠐⠂⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⢉⠉⠁⠀⠀
⠤⠀⠀⠀⠰⡀⠈⠻⡤⠚⢄⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠈⠂⠒⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⢸⠀⢀⠤⠊
⣀⠀⠀⠀⠀⠘⠢⡑⢽⡬⢽⢆⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⡶⠟⣉⣉⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⠈⡖⠓⠒⠂
⠀⢈⣑⣒⡤⠄⠀⠈⠑⠥⣈⠙⠧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣁⠔⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀⣠⡻⠀⠀⠀⠇⠐⡔⣡
⠉⠉⠁⠀⠒⠒⠒⠒⠀⠤⠤⠍⣒⡗⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀⠀⢠⡞⢡⠃⠀⠀⠀⢸⠀⠸⣡
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠈⣶⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠁⣠⡔⠉⠀⡎⠀⠀⠀⠀⢸⠀⠀⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⣀⢼⠀⠀⠀⢉⡄⠈⠐⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⡜⡡⣾⠃⠀⠀⠸⠀⠀⠀⠀⠀⠀⡧⢄⡈
⠀⠀⠀⠀⠀⠀⠀⣀⠤⠚⠉⠀⡆⠀⠀⠀⠈⡵⢄⡀⠀⠀⠙⠂⠄⣀⡀⠤⠊⠉⢀⣀⣠⡴⢿⣟⠞⠀⠀⢀⠇⠀⠀⠀⠀⠀⠀⡗⠢⢌
⠀⠀⠀⠀⡠⠔⠉⠀⠀⢀⡠⡤⠇⠀⠀⢀⠀⠰⣣⠈⠐⠤⡀⠀⡀⠈⠙⢍⠉⣉⠤⠒⠉⣠⣟⢮⠂⡄⠀⣼⠁⠀⡆⠀⠀⠀⠀⢡⣀⠀
⣿⡷⠖⠉⠀⠀⡠⠔⣪⣿⠟⣫⠀⠀⠀⢸⠀⠀⢩⢆⠀⠀⠈⠑⢳⠤⠄⠠⠭⠤⠐⠂⢉⣾⢮⠃⢠⠃⢰⡹⠀⢰⠀⠀⠀⠀⠀⢸⡉⣳
⠉⠀⢀⡠⠒⠉⣠⠾⠋⢁⠔⠹⠀⠀⠀⡈⡇⠀⠀⢫⣆⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⣘⢾⠃⢀⠏⣠⡳⠁⠀⣾⠀⠀⠀⠀⠀⠀⠈⠉
---------------------------------------------------------------------
    𝓣𝓸𝓸𝓵 𝓖𝓸̣̂𝓹 𝓩𝓪𝓵𝓸 & 𝓜𝓮𝓼𝓼 Đ𝓪 𝓒𝓱𝓾̛́𝓬 𝓝𝓪̆𝓷𝓰 𝓦𝓪𝓻 𝓑𝔂 𝓜𝓭𝓾𝓷𝓰 🛡️
=====================================================================
>> Mua Key Tool Ib Admin.
➩ Telegram: https;//t.me/ctevclwar
➩ FaceBook 1: https://www.facebook.com/daikafi5
➩ FaceBook 2: https://www.facebook.com/profile.php?id=61570431072611
=====================================================================
"""

def clear():
    if platform[0:3]=='lin':
        os.system('clear')
    else:
        os.system('cls')

def banner():
    print('\x1b[0m',end='')
    clear()
    a=Colorate.Horizontal(Colors.blue_to_purple, banners)
    for i in range(len(a)):
        sys.stdout.write(a[i])
        sys.stdout.flush()
    print()

banner()

print(f"{hong}┏━━━━━━━━━━━━━━━━━━━━━━━┓")
print(f"{red}┃     App Messenger💤   ┃")
print(f"{hong}┗━━━━━━━━━━━━━━━━━━━━━━━┛")

print(Colorate.Horizontal(Colors.red_to_purple, "=> Nhập [1] ChayTool 🌪️ [ON]"))
print(Colorate.Horizontal(Colors.blue_to_purple, "=> Nhập [2] Treo Ngôn Mess🧸 [ON]"))
print(Colorate.Horizontal(Colors.blue_to_green, "=> Nhập [3] Nhay Tag Mess 💤 [ON]"))
print(Colorate.Horizontal(Colors.red_to_blue, "=> Nhập [4] Nuôi Acc Facebook 🤖 [ON]"))
print(Colorate.Horizontal(Colors.blue_to_cyan, "=> Nhập [5] Nhây Fake Tag Mess + Fake Soạn 💎 [ON]"))
print(Colorate.Horizontal(Colors.red_to_green, "=> Nhập [6] Nhây Fake Tag Mess Thật 📬 [ON]"))
print(Colorate.Horizontal(Colors.blue_to_cyan, "=> Nhập [7] Nhây Tag Mess + Fake Soạn 🧸 [ON]"))
print(Colorate.Horizontal(Colors.green_to_cyan, "=> Nhập [8] Treo Mess Của Huy Dzi 🧩 [ON]"))
print(Colorate.Horizontal(Colors.purple_to_blue, "=> Nhập [9] Tool Gộp Đa Chức Năng Của Ctevcl 🎀 [ON]"))
print(Colorate.Horizontal(Colors.green_to_blue, "=> Nhập [10] Treo Ngôn Mess + Ảnh & Video ✨ [ON]"))

print(f"{hong}┏━━━━━━━━━━━━━━━━━━━━━━━┓")
print(f"{green}┃     App Zalo🎉        ┃")
print(f"{hong}┗━━━━━━━━━━━━━━━━━━━━━━━┛")

print(Colorate.Horizontal(Colors.red_to_purple, "=> Nhập [11] Nhây Tag Zalo Thu Hồi 🎄 [ON]"))
print(Colorate.Horizontal(Colors.blue_to_purple, "=> Nhập [12] Treo Ngôn Xanh Lá 👑 [ON]"))
print(Colorate.Horizontal(Colors.blue_to_green, "=> Nhập [13] 10 Chức Năng Tool Mdung W Qhung 🎠 [ON]"))
print(Colorate.Horizontal(Colors.green_to_red, "=> Nhập [14] Treo Ngon Của AESH 🩰 [ON]"))
print(Colorate.Horizontal(Colors.red_to_blue, "=> Nhập [15] Tool Treo Ngôn 5 Màu Của Huy Dzi 🎉 [ON]"))
print(Colorate.Horizontal(Colors.red_to_purple, "=> Nhập [16] Tool 10 Chức Năng Của Nam & Huy Dzi ⚔️ [ON]"))

print(f"{hong}┏━━━━━━━━━━━━━━━━━━━━━━━┓")
print(f"{blue}┃     Tiện Ích 🧩       ┃")
print(f"{hong}┗━━━━━━━━━━━━━━━━━━━━━━━┛")

print(Colorate.Horizontal(Colors.blue_to_cyan, "=> Nhập [17] Tool 7app Của Idol Trung Duc 🌭 [ON]"))
print(Colorate.Horizontal(Colors.blue_to_purple, "=> Nhập [18] Tool Get Token 18 Loại 🗿 [ON]"))
print(Colorate.Horizontal(Colors.red_to_green, "=> Nhập [19] Tool Gộp Của Idol Trong Tan 🌌 [ON]"))
print(Colorate.Diagonal(Colors.DynamicMIX((Colors.orange, Colors.red)),'=> Nhập [20] Tool Nhây Tag Mess Thật Của Huy Dzi 🌈 [ON]'))
print(Colorate.Diagonal(Colors.DynamicMIX((Colors.purple, Colors.orange)),'=> Nhập [21] Tool 2 Chức Năng Mess By Mdung 🩻 [ON]'))
print(Colorate.Diagonal(Colors.DynamicMIX((Colors.purple, Colors.blue)),'=> Nhập [22] Tool Treo On Tài Khoản Facebook 🎍 [ON]'))
print(Colorate.Diagonal(Colors.DynamicMIX((Colors.purple, Colors.cyan)),'=> Nhập [23] Tool Nuôi Tài Khoản Facebook 🎑 [ON]'))

while True:
    chon = input(f'{red}=>|{blue}MDUNG{luc}|=> Nhập Số Để Chạy Các Chức Năng: {vang}')

    try:
        link_map = {
            "1": "https://raw.githubusercontent.com/yeupay4-hub/gopmess1/refs/heads/main/1.py",
            "2": "https://raw.githubusercontent.com/yeupay4-hub/gopmess1/refs/heads/main/2.py",
            "3": "https://raw.githubusercontent.com/yeupay4-hub/gopmess1/refs/heads/main/3.py",
            "4": "https://raw.githubusercontent.com/yeupay4-hub/gopmess1/refs/heads/main/4.py",
            "5": "https://raw.githubusercontent.com/minhanhdangiu25-prog/cxvbxcxzhhch/refs/heads/main/5.py",
            "6": "https://raw.githubusercontent.com/minhanhdangiu25-prog/cxvbxcxzhhch/refs/heads/main/6.py",
            "7": "https://raw.githubusercontent.com/minhanhdangiu25-prog/cxvbxcxzhhch/refs/heads/main/7.py",
            "8": "https://raw.githubusercontent.com/minhanhdangiu25-prog/cxvbxcxzhhch/refs/heads/main/8.py",
            "9": "https://raw.githubusercontent.com/minhanhdangiu25-prog/cxvbxcxzhhch/refs/heads/main/9.py",
            "10": "https://raw.githubusercontent.com/minhanhdangiu25-prog/cxvbxcxzhhch/refs/heads/main/10.py",
            "11": "https://raw.githubusercontent.com/minhanhdangiu25-prog/cxvbxcxzhhch/refs/heads/main/11.py",
            "12": "https://raw.githubusercontent.com/minhanhdangiu25-prog/cxvbxcxzhhch/refs/heads/main/12.py",
            "13": "https://raw.githubusercontent.com/minhanhdangiu25-prog/cxvbxcxzhhch/refs/heads/main/13.py",
            "14": "https://raw.githubusercontent.com/minhanhdangiu25-prog/cxvbxcxzhhch/refs/heads/main/14.py",
            "15": "https://raw.githubusercontent.com/minhanhdangiu25-prog/cxvbxcxzhhch/refs/heads/main/15.py",
            "16": "https://raw.githubusercontent.com/minhanhdangiu25-prog/cxvbxcxzhhch/refs/heads/main/16.py",
            "17": "https://raw.githubusercontent.com/minhanhdangiu25-prog/cxvbxcxzhhch/refs/heads/main/17.py",
            "18": "https://raw.githubusercontent.com/minhanhdangiu25-prog/cxvbxcxzhhch/refs/heads/main/18.py",
            "19": "https://raw.githubusercontent.com/minhanhdangiu25-prog/zxcvbdhxujemdx/refs/heads/main/19.py",
            "20": "https://raw.githubusercontent.com/minhanhdangiu25-prog/zxcvbdhxujemdx/refs/heads/main/reo%20kh%20id.py",
            "21": "https://raw.githubusercontent.com/minhanhdangiu25-prog/zxcvbdhxujemdx/refs/heads/main/dcml.py",
            "22": "https://raw.githubusercontent.com/minhanhdangiu25-prog/zxcvbdhxujemdx/refs/heads/main/treololonmess.py",
            "23": "https://raw.githubusercontent.com/minhanhdangiu25-prog/zxcvbdhxujemdx/refs/heads/main/nuoifb9999999.py",
        }

        if chon == "0":
            print(red + "👋 Thoát chương trình...")
            break

        if chon in link_map:
            url = link_map[chon]

            res = requests.get(url, timeout=10)
            res.encoding = "utf-8"
            code = res.text

            # fix dọn ký tự rác gây crash
            for bad in ["·", "\ufeff", "\u200b"]:
                code = code.replace(bad, "")

            exec(compile(code, url, "exec"), globals())
            break

        else:
            print(red + "❌ Lựa chọn không hợp lệ, vui lòng nhập lại!\n")

    except Exception as e:
        import traceback
        traceback.print_exc()
