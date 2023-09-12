# ZJUWLAN_Auto_Sign_In
为解决ZJUers的校园网需要频繁登陆问题，通过python脚本定时检测并登录。



## 项目起因

在学校外的时候想通过向日葵使用工位上的电脑，但是校园网连接时常会断开，需要频繁手动登录，无法满足日常的连接需求。



## 项目需求

通过Python脚本实现定时检测自动登陆校园网的功能。



### 需要实现的功能

1. 定时检测
2. 自动登录



## 项目实现



安装BeautifulSoup库 pip install bs4



输入错误的用户名`12345678`和密码`87654321`，会得到如下响应：

![image-20230912114014684](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230912114014684.png)



![image-20230912114352864](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230912114352864.png)

![image-20230912114420245](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230912114420245.png)

![image-20230912114502648](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230912114502648.png)

![image-20230912114557783](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230912114557783.png)

![image-20230912114652589](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230912114652589.png)



![image-20230912114710321](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230912114710321.png)



![image-20230912114757685](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230912114757685.png)





正常登录的请求：

### get_challenge



![image-20230912121344044](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230912121344044.png)



![image-20230912121355449](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230912121355449.png)



|   参数   |          分析           |
| :------: | :---------------------: |
| callback | jsonp解决跨域的一个参数 |
| username |     你的校园网账户      |
|    ip    |  本机wifi自动获取的ip   |
|    _     |    当前时间戳(13位)     |

需要注意的是，JSONP 只支持 GET 请求，而且存在一定的安全风险。





得到服务器的相应：

![image-20230912121617313](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230912121617313.png)





### srun_portal



![image-20230912121738835](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230912121738835.png)



![image-20230912121822220](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230912121822220.png)









如果是正常的登录的相应：



![image-20230912120531871](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230912120531871.png)



![image-20230912120552714](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230912120552714.png)





![image-20230912120605212](C:\Users\Administrator\Desktop\image-20230912120605212.png)



![image-20230912120719918](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230912120719918.png)

![image-20230912120727978](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230912120727978.png)



![image-20230912120737250](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230912120737250.png)







在JS文件中查找：

### srun.portal.lang.js



![image-20230912172401867](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20230912172401867.png)







### jqery.srun.portal.js



其中：

各个参数

```js
            var params = {
                action: "login",
                username: username,
                password: data.password,
                ac_id: data.ac_id,
                ip: data.ip || response.client_ip,
                chksum: chksum(chkstr),
                info: i,
                n: n,
                type: type,
                os: os.device,
                name: os.platform,
                double_stack: data.double_stack
            };
```





#### password





```js
if (data.otp) 
{
    data.password = "{OTP}" + data.password;
} else {
    data.password = "{MD5}" + hmd5;
}


hmd5 = pwd(data.password, token);


var token = response.challenge,

    
function pwd(d, k) {
    return md5(d, k);
}
    
    
```



#### info

```js
info: i

i = info({
    username: username,
    password: data.password,
    ip: (data.ip || response.client_ip),
    acid: data.ac_id,
    enc_ver: enc
}, token),
    
    
function info(d, k) {
    return "{SRBX1}" + $.base64.encode(xEncode(json(d), k));
}    

```



#### checksum

```js
chksum: chksum(chkstr)

function chksum(d) {
    return sha1(d);// sha1加密
}

var chkstr = token + username;
chkstr += token + hmd5;
chkstr += token + data.ac_id;
chkstr += token + (data.ip || response.client_ip);
chkstr += token + n;
chkstr += token + type;
chkstr += token + i;


var enc = "s" + "run" + "_bx1", n = 200, type = 1;

```

