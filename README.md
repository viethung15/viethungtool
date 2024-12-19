import json
import requests,os,time
import socket
from time import strftime
from time import sleep
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import time
import sys
banner = """
\033[97m════════════════════════════════════════════════  
\033[1;31mTool By: \033[1;32mNGUYỄN BÙI VIỆT HƯNG 
\033[1;97m[\033[1;91m->\033[1;97m]\033[1;97mTelegram\033[1;31m  : \033[1;36mhttps://t.me/lkztool
\033[1;97m[\033[1;91m->\033[1;97m]\033[1;97m MB Bank\033[1;31m  : \033[1;36m178287
\033[1;97m[\033[1;91m->\033[1;97m]\033[1;97m Zalo\033[1;31m     : \033[1;36m0397251716
\033[1;97m[\033[1;91m->\033[1;97m]\033[1;97m Telegram\033[1;31m : \033[1;36mhttps://t.me/trumkimsa3
\033[97m════════════════════════════════════════════════
"""
os.system('cls' if os.name== 'nt' else 'clear')
for x in banner:
  print(x,end = "")
  sleep(0.001)
print("\033[1;31mTool Auto TikTok")   

    # Nhập auth
try:
  Authorization = open("Authorization.txt","x")
  t = open("token.txt","x")
except:
  pass
Authorization = open("Authorization.txt","r")
t = open("token.txt","r")
author = Authorization.read()
token = t.read()
if author == "":
  author = input("\033[1;97mNHẬP AUTHORIZATION : ")
  token = input("\033[1;31mNHẬP T : ")
  Authorization = open("Authorization.txt","w")
  t = open("token.txt","w")
  Authorization.write(author)
  t.write(token)
else:
  select = input("\033[1;97m║ Đăng\033[1;96m Nhập \033[1;95mTài \033[1;94mKhoản \033[1;93mHiện \033[1;92mCó\033[1;91m ( Enter Để Bỏ Qua ,Nhập AUTHORIZATION Tại Đây \033[1;97m║\033[1;91m Để Đổi )  \n\033[1;97m╚⟩⟩⟩ ")

  if select != "":
    author = select
    token = input("\033[1;36mNhập T : ")
    Authorization = open("Authorization.txt","w")
    t = open("token.txt","w")
    Authorization.write(author)
    t.write(token)
Authorization.close()
t.close()
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Content-Type': 'application/json;charset=utf-8',
    'Authorization': author,
    't': token,
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Referer': 'https://app.golike.net/account/manager/tiktok',
}


def chonacc():
  json_data = {}

  response = requests.get('https://gateway.golike.net/api/tiktok-account', headers=headers, json=json_data).json()
  return response
def nhannv(account_id):

  params = {
    'account_id': account_id,
    'data': 'null',
  }

  json_data = {}

  response = requests.get('https://gateway.golike.net/api/advertising/publishers/tiktok/jobs',params=params,headers=headers,json=json_data,).json()
  return response
def hoanthanh(ads_id,account_id):
  json_data = {
    'ads_id': ads_id,
    'account_id': account_id,
    'async': True,
    'data': None,
  }

  response = requests.post(
    'https://gateway.golike.net/api/advertising/publishers/tiktok/complete-jobs',
    headers=headers,
    json=json_data,
  ).json()
  return response
def baoloi(ads_id,object_id,account_id,loai):
  json_data1 = {
    'description': 'Tôi đã làm Job này rồi',
    'users_advertising_id': ads_id,
    'type': 'ads',
    'provider': 'tiktok',
    'fb_id': account_id,
    'error_type': 6,
  }

  response = requests.post('https://gateway.golike.net/api/report/send', headers=headers, json=json_data1).json()

  json_data = {
    'ads_id': ads_id,
    'object_id': object_id,
    'account_id': account_id,
    'type': loai,
  }

  response = requests.post(
    'https://gateway.golike.net/api/advertising/publishers/tiktok/skip-jobs',
    headers=headers,
    json=json_data,
  ).json()  
chontktiktok = chonacc()  
def dsacc():
  if(chontktiktok["status"]!=200):
    print("\033[1;34mAuthorization hoặc T sai hãy nhập lại!!!")
    quit()

  for i in range(len(chontktiktok["data"])):
    print(f'\033[1;97m•[✩]➭\033[1;36m [{i+1}] \033[1;91m=> \033[1;97mTên Tài Khoản┊\033[1;32m㊪ :\033[1;93m {chontktiktok["data"][i]["nickname"]}  ')
   
dsacc() 
while True:
  try:
    luachon = int(input("\033[1;35m\033[1;97m║ Chọn \033[1;96mTài \033[1;95mKhoản \033[1;94mĐể \033[1;93mChạy \n\033[1;97m╚⟩⟩⟩ "))
    while luachon > len((chontktiktok)["data"]):
      luachon = int(input("\033[1;32mAcc Này Không Có Trong Danh Sách , Hãy Nhập Lại : "))
    account_id = chontktiktok["data"][luachon - 1]["id"]
    break  
  except:
    print("\033[1;35mSai Định Dạng !!!") 
while True:
  try:
    delay = int(input("\033[1;97m║ Nhập\033[1;91m Delay \n\033[1;97m╚⟩⟩⟩ "))
    break
  except:
    print("\033[1;31mSai Định Dạng !!!")
while True:
  try: 
    doiacc = int(input("\033[1;97m║ \033[1;99mNhận\033[1;91m Tiền\033[1;96m Thất\033[1;95m Bại\033[1;94m Bao\033[1;93m Nhiu\033[1;92m Lần\033[1;91m Thì\033[1;96m Dừng\033[1;93m \n\033[1;97m╚⟩⟩⟩ "))
    break
  except:
    print("\033[1;31mNhập Vào 1 Số!!!")    
os.system('cls' if os.name== 'nt' else 'clear')    
dem = 0
tong = 0
checkdoiacc = 0
dsaccloi = []
accloi = ""
os.system('cls' if os.name== 'nt' else 'clear')

for x in banner:
  print(x,end = "")
  sleep(0.001)
print("\033[1;31mTool Auto TikTok")
while True:
  if checkdoiacc == doiacc:
    dsaccloi.append(chontktiktok["data"][luachon - 1]["nickname"])
    print(f"\033[1;36mCác Acc Tiktok {dsaccloi} Có Vẻ Gặp Vấn Đề Nên Đổi Acc Chạy Đê ")
    dsacc()
    while True:
      try:
        luachon = int(input("\033[1;35m\033[1;97m║ Chọn \033[1;96mTài \033[1;95mKhoản \033[1;94mĐể \033[1;93mChạy \n\033[1;97m╚⟩⟩⟩  "))
        while luachon > len((chontktiktok)["data"]):
          luachon = int(input("\033[1;32mAcc Này Không Có Trong Danh Sách, Hãy Nhập Lại : "))
        account_id = chontktiktok["data"][luachon - 1]["id"]
        checkdoiacc = 0
        break  
      except:
        print("\033[1;35mSai Định Dạng !!!")

     
  print(f'\033[1;97mĐang \033[1;96mLấy \033[1;95mNhiệm \033[1;91mVụ\033[1;93m Follow',end="\r")    
  while True:
    try:  
      nhanjob = nhannv(account_id)
      break
    except:
      pass
  if(nhanjob["status"] == 200):
    ads_id = nhanjob["data"]["id"]
    link = nhanjob["data"]["link"]
    object_id = nhanjob["data"]["object_id"]
    if(nhanjob["data"]["type"] != "follow"):
      baoloi(ads_id,object_id,account_id,nhanjob["data"]["type"])
      continue
    os.system(f"termux-open-url {link}")
    for remaining_time in range(delay, -1, -1):
            colors = [
                "\033[1;37mL\033[1;36mK\033[1;35mZ \033[1;32mT\033[1;31mO\033[1;34mO\033[1;33mL\033[1;31m\033[1;32m",
                "\033[1;34mL\033[1;31mK\033[1;37mZ \033[1;36mT\033[1;32mO\033[1;35mO\033[1;37mL\033[1;31m\033[1;32m",
                "\033[1;31mL\033[1;37mK\033[1;36mZ \033[1;33mT\033[1;35mO\033[1;32mO\033[1;34mL\033[1;31m\033[1;32m",
                "\033[1;32mL\033[1;33mK\033[1;34mZ \033[1;35mT\033[1;36mO\033[1;37mO\033[1;36mL\033[1;31m\033[1;32m",
                "\033[1;37mL\033[1;34mK\033[1;35mZ \033[1;36mT\033[1;32mO\033[1;33mO\033[1;31mL\033[1;31m\033[1;32m",
                "\033[1;34mL\033[1;33mK\033[1;37mZ \033[1;35mT\033[1;31mO\033[1;36mO\033[1;36mL\033[1;31m\033[1;32m",
                "\033[1;36mL\033[1;35mK\033[1;31mZ \033[1;34mT\033[1;37mO\033[1;35mO\033[1;32mL\033[1;31m\033[1;32m",
            ]
            for color in colors:
                print(f"\r{color}|{remaining_time}| \033[1;31m", end="")
                time.sleep(0.12)
                        
                        
    print("\r                          \r", end="") 
    print("\033[1;35mĐang Nhận Tiền         ",end = "\r")
    attempts = 0
    max_attempts = 2

    # Vòng lặp thử lại tối đa max_attempts lần
    while attempts < max_attempts:
        try:
            nhantien = hoanthanh(ads_id, account_id)
            if nhantien["status"] == 200:
                # Nếu hoàn thành thành công, cập nhật thông tin và thoát vòng lặp
                dem += 1
                tien = nhantien["data"]["prices"]
                tong += tien

                # Lấy thời gian hiện tại
                local_time = time.localtime()
                hour = local_time.tm_hour
                minute = local_time.tm_min
                second = local_time.tm_sec

                # Định dạng giờ, phút, giây
                h = f"{hour:02d}"
                m = f"{minute:02d}"
                s = f"{second:02d}"

                # Tạo chuỗi thông báo
                chuoi = (
                    f"\033[1;31m\033[1;36m{dem}\033[1;31m\033[1;97m | "
                    f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m | "
                    f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                    f"\033[1;31m{nhantien['data']['type']}\033[1;31m\033[1;32m\033[1;32m\033[1;97m |"
                    f"\033[1;32m Ẩn ID\033[1;97m | \033[1;97m \033[1;32m+{tien} \033[1;97m| "
                    f"\033[1;33m{tong}"
                )

                # Xóa dòng trước đó và in thông báo mới
                print(" " * 60, end="\r")  # Xóa dòng cũ
                print(chuoi)    
                checkdoiacc = 0
                break  # Thoát vòng lặp nếu thành công
            else:
                # In toàn bộ response để kiểm tra lý do
                # print(f"Thử lại lần {attempts + 1}.")
                if attempts == 0:
                    for countdown in range(3, -1, -1):
                        print(f"Vui lòng chờ {countdown} giây để hoàn thành job lần thứ 2", end="\r")
                        time.sleep(1)
                    print(" " * 50, end="\r")  # Xóa dòng đếm ngược sau khi hoàn thành

            attempts += 1

        except Exception as e:
            print(f"Đã xảy ra lỗi: {str(e)}. Thử lại lần {attempts + 1}.")
            attempts += 1
            time.sleep(1)  # Thử lại sau 1 giây

    # Nếu hoàn thành thất bại sau 2 lần thử, bỏ qua job và in thông báo
    if attempts == max_attempts:
        print("\033[1;31mBỏ Qua Nhiệm Vụ", end="\r")
        # Xóa dòng thông báo lỗi cũ
        time.sleep(1)

    # Xử lý trường hợp không hoàn thành
    if nhantien["status"] != 200:
        while True:
            try:
                baoloi(ads_id, object_id, account_id, nhanjob["data"]["type"])
                print(" " * 60, end="\r")  # Xóa dòng thông báo lỗi cũ
                print("\033[1;31mBỏ Qua Nhiệm Vụ", end="\r")
                time.sleep(1)
                checkdoiacc += 1
                break
            except Exception as e:
                print(f"Lỗi khi xử lý thông báo lỗi: {str(e)}")
                time.sleep(1)  # Thử lại sau 1 giây
