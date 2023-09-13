# ZJUWLAN_Auto_Sign_In
本项目为解决ZJUers的校园网（**ZJUWLAN**）需要频繁登陆问题，通过python脚本定时检测并登录。

项目基于工院学生，其他校区的同学需要根据自身情况进行修改，在[使用方法](#脚本使用方法)中提到修改内容。



## 项目起因

​		在学校外的时候经常有需求想通过向日葵远程连接工位上的电脑，但是**校园网在长时间无动作时或长时间休眠后常会断开登录**导致需要频繁手动输入账号密码重新进入登录状态，然而赶回工位手动连接并不现实，**无法实现稳定的日常的远程控制及文件传输需求**。

![](https://github.com/Franch-Toast/ZJUWLAN_Auto_Sign_In/blob/main/pic/1.png)

## 项目需求

​		分析**ZJUWLAN**登录过程，通过Python脚本实现定时检测登陆状态、自动登陆校园网的功能，保证电脑能够保持网络连接，即使断开连接也能在较短的时间内恢复连接。



### 需要实现的功能

1. 定时检测
2. 自动登录



## 项目实现

### 项目文件分析

```
|-- ZJUWLAN_Auto_Sign_In
    |-- README.md
    |-- Source
    |   |-- base64_py.py				# base64加密方式
    |   |-- main.py      				
    |   |-- md5_py.py					# md5加密方式
    |   |-- sha1_py.py					# sha1加密方式	
    |   |-- xEncode_py.py				# xEncode加密方式
    |   |-- js_for_save
    |       |-- jqery.srun.portal.js    # 记录登录过程的JS文件，从服务器响应文件中保留存档
    |       |-- all.min.js    			# 记录加密方法的JS文件，从服务器响应文件中保留存档
    |       |-- srun.portal.lang.js     # 记录错误信息的的JS文件，从服务器响应文件中保留存档
    |-- pic
```



### 脚本使用方法

该脚本使用的均为内置库，电脑中需有 python3 运行环境。

#### 检查并修改登录URL

在`main.py`中检查所在位置的网络连接请求URL，网络位置为工院我的工位时URL为：

```python
# Website = "http://10.115.9.2/" # 使用自己网络连接的请求URL
Website_info = "http://10.115.9.2/cgi-bin/rad_user_info" # 用于读取当前登录的信息
Website_challenge = "http://10.115.9.2/cgi-bin/get_challenge" # 用于获取token
Website_portal = "http://10.115.9.2/cgi-bin/srun_portal" # 用于登录
```

根据自己所在位置的URL更改文件中的内容，仅需要更改上面所有的 IP 即可。

![](https://github.com/Franch-Toast/ZJUWLAN_Auto_Sign_In/blob/main/pic/2.png)

#### 运行脚本

在 IDE 中或在 windows 自带的命令行工具中运行脚本：`python {文件所在路径\}main.py`

根据提示输入：

1. 定时检测的时间，以秒作为单位。示例中输入的是 1800 s （30min），即每30min检测一次登陆状态；
2. 登录账号；
3. 登录密码。

![](https://github.com/Franch-Toast/ZJUWLAN_Auto_Sign_In/blob/main/pic/3.png)



脚本即刻开始按设定的时间周期运行，并在运行过程中输出检测结果与登录结果：

- 检测到登陆掉线
- 当前登录状态良好
- 登陆失败！已经处于登录状态中
- 登陆成功！
- 登陆失败！输入的账号不存在。
- 登陆失败！输入的账号或密码错误。

目前仅添加了以上几个常见的错误信息。



### 使用结果示例

首先电脑处于未登陆状态后运行脚本，这里作为演示，周期时间设置为 5 s。

#### 成功登录

![](https://github.com/Franch-Toast/ZJUWLAN_Auto_Sign_In/blob/main/pic/4.png)

#### 登陆账号或密码错误

![](https://github.com/Franch-Toast/ZJUWLAN_Auto_Sign_In/blob/main/pic/5.png)

#### 登陆账号不存在

![](https://github.com/Franch-Toast/ZJUWLAN_Auto_Sign_In/blob/main/pic/6.png)




