
import requests
from bs4 import BeautifulSoup
from xEncode_py import *
from base64_py import *
from md5_py import *
from sha1_py import *


# Website = "http://10.115.9.2/" 使用该地址也会跳转到下面的地址
# Website = "http://10.115.9.2/srun_portal_pc?ac_id=1&theme=basic"
Website = "http://10.115.9.2/cgi-bin/get_challenge" # 测试用

User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"

account = "789456123"
pwd = "123456789"
personal_ip = "10.115.xxx.xx"


params_challenge = {
    "callback": "jQuery112407864382812073898_1694516091928",
    "username": account,
    "ip": personal_ip,
    "_": "1694516091930"
}


def post_sign_in_information(): # 推送登录信息

    content_origin = requests.get(Website,params=params_challenge)
    if content_origin.status_code != 200:
        print("访问失败！查看网络连接情况！")
    content_text = content_origin.text

    content = BeautifulSoup(content_text,"html.parser")

    # content_title = content.title.text
    print(content)


def check_network_status(): # 检测网络是否断联
    print()


def timer_30min(): # 30min定时器
    print()

post_sign_in_information()