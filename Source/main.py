
import requests
from bs4 import BeautifulSoup
# import json
import re
import time
import random
from xEncode_py import *
from base64_py import *
from md5_py import *
from sha1_py import *


# Website = "http://10.115.9.2/" 使用该地址也会跳转到下面的地址
# Website = "http://10.115.9.2/srun_portal_pc?ac_id=1&theme=basic"
Website = "http://10.115.9.2/cgi-bin/get_challenge" # 测试用
Website_portal = "http://10.115.9.2/cgi-bin/srun_portal"

User_Agent ={
    "User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    } 
account = "123456789"
origin_pwd = "987654321"
personal_ip = "10.115.194.33"

randnum = str(random.randint(1, 1234567890123456789012))


token = ""
hmd5 = ""
info = ""
checksum = ""
pwd = ""


# callback = "jQuery112407864382812073898_1694516091928"
# print(len(callback)) # 41

def post_sign_in_information(): # 推送登录信息
    
    
    get_token()
    print("获取的token：" + token + '\n')
    get_pwd()
    print("获取的pwd：" + pwd + '\n')
    get_info()
    print("获取的info：" + info + '\n')
    get_checksum()
    print("获取的checksum：" + checksum + '\n')

    params_portal = {
        "callback": "jQuery" + randnum + "_" + str(int(time.time()*1000)),
        # "callback": "jQuery193729712748856754747_1694580702794",
        "action": "login",
        "username": account,
        "password": pwd,
        "ac_id": "1",
        "ip": personal_ip,
        "chksum": checksum,
        "info": info,
        "n": "200",
        "type": "1",
        "os": "windows+10",
        "name": "windows",
        "double_stack": "0",
        "_": int(time.time()*1000)
        # "_": "1694580702794"
    }

    print(params_portal)
    res = requests.get(Website_portal,params=params_portal,headers=User_Agent)
    print(res.text)



def get_token():
    global token
    # 获取token

    params_challenge = {
    "callback": "jQuery" + randnum + "_" + str(int(time.time()*1000)),
    # "callback": "jQuery193729712748856754747_1694580702794",
    "username": account,
    "ip": personal_ip,
    "_": int(time.time()*1000)
    # "_": "1694580702794"
}

    content_origin = requests.get(Website,params=params_challenge,headers=User_Agent)
    if content_origin.status_code != 200:
        print("访问失败！查看网络连接情况！")
    # content_text = content_origin.json()
    content_text = content_origin.text
    token = re.search('"challenge":"(.*?)"', content_text).group(1)
    # content = BeautifulSoup(content_text,"html.parser")
    # print(type(content_text))    
    print(content_text)    
    # token = json.loads(content_text)["challenge"]
    # token = content_text["challenge"]
    # print(type(token))
    # print(token)
    


def get_pwd():
    # 进行密码的加密
    global pwd,hmd5
    hmd5 = get_md5(origin_pwd,token)
    pwd = "{MD5}" + hmd5


info_dict = {
    "username": account,
    "password": origin_pwd,
    "ip": personal_ip,
    "acid": "1",
    "enc_ver": "srun_bx1"
}


def get_info():

    # info_json = json.dumps(info_dict)
    # print(str(info_dict))
    # print(info_json)
    global info
    info_text = re.sub("'", '"', str(info_dict))
    info_text = re.sub(" ", '', info_text)

    # print(info_text)
    # print(token)

    # info_text = str(info_dict)
    print(info_text)    

    info = "{SRBX1}" + get_base64(get_xencode(info_text, token))
    
 


def get_checksum():
    global checksum
    chkstr = token + account
    chkstr += token + hmd5
    chkstr += token + "1"
    chkstr += token + personal_ip
    chkstr += token + "200"
    chkstr += token + "1"
    chkstr += token + info

    checksum = get_sha1(chkstr)
    


def check_network_status(): # 检测网络是否断联
    print()


def timer_30min(): # 30min定时器
    print()

post_sign_in_information()