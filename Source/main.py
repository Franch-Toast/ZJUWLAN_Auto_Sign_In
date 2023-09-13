
import requests
# from bs4 import BeautifulSoup
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
Website_challenge = "http://10.115.9.2/cgi-bin/get_challenge" # 用于获取token
Website_portal = "http://10.115.9.2/cgi-bin/srun_portal" # 用于登录

User_Agent ={
    "User_Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
    } 


randnum = str(random.randint(1, 1234567890123456789012))


# callback = "jQuery112407864382812073898_1694516091928"
# print(len(callback)) # 41

def post_sign_in_information(): # 推送登录信息
    
    
    get_token()
    print("获取的token： " + token + '\n')
    get_pwd()
    print("加密后的的pwd： " + pwd + '\n')
    get_info()
    print("加密后的info： " + info + '\n')
    get_checksum()
    print("加密后的checksum： " + checksum + '\n')

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

    # print(params_portal)
    res = requests.get(Website_portal,params=params_portal,headers=User_Agent)
    res = res.text
    print("登录响应： " + res + "\n")

    

    if re.search('"error":"(.*?)"', res).group(1) == "ok":
        suc_msg = re.search('"suc_msg":"(.*?)"', res).group(1)
        if suc_msg == "ip_already_online_error":
            print("【 登陆失败！已经处于登录状态中。】\n")
        elif suc_msg == "login_ok":
            print("【 登陆成功！】\n")
    elif re.search('"error_msg":"(.*?)"', res).group(1) == "E2531: User not found.":
        print("【 登陆失败！输入的账号不存在。】\n")
    elif re.search('"error_msg":"(.*?)"', res).group(1) == "E2901: (Third party 1)bind_user2: ldap_bind error":
        print("【 登陆失败！输入的账号或密码错误。】\n")

    print("********************************\n\n")



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

    content_origin = requests.get(Website_challenge,params=params_challenge,headers=User_Agent)
    if content_origin.status_code != 200:
        print("访问失败！查看网络连接情况！")
    # content_text = content_origin.json()
    content_text = content_origin.text
    token = re.search('"challenge":"(.*?)"', content_text).group(1)
    # content = BeautifulSoup(content_text,"html.parser")
    # print(type(content_text))    
    # print(content_text)    
    # token = json.loads(content_text)["challenge"]
    # token = content_text["challenge"]
    # print(type(token))
    


def get_pwd():
    # 进行密码的加密
    global pwd,hmd5
    hmd5 = get_md5(origin_pwd,token)
    pwd = "{MD5}" + hmd5





def get_info():

    info_dict = {
    "username": account,
    "password": origin_pwd,
    "ip": personal_ip,
    "acid": "1",
    "enc_ver": "srun_bx1"
}

    # info_json = json.dumps(info_dict)
    # print(str(info_dict))
    # print(info_json)
    global info
    info_text = re.sub("'", '"', str(info_dict))
    info_text = re.sub(" ", '', info_text)

    # print(info_text)
    # print(token)

    # info_text = str(info_dict)
    # print(info_text)    

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


if __name__ == '__main__':

    global account,origin_pwd,personal_ip

    cycle_time = 1800 # 30min
    while(1):
        cycle_time = int(input("请输入定时检测的时间（秒），建议时间在 1 天内："))
        if cycle_time <= 0 or cycle_time > 86400:
            print("输入的时间不合适，请重新输入。")
        else:
            break
    
    account = input("请输入账号（学号）：")
    origin_pwd = input("请输入密码：")
    personal_ip = input("请输入本机ip：")

    while(1):
        print("**********开始尝试登录**********\n")

        post_sign_in_information()

        time.sleep(cycle_time)
