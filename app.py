from urllib import response
import requests

def check_baidu():
    "访问百度， 检查返回状态码"
    response = requests.get("https://www.baidu.com/12345")
    return response.status_code



