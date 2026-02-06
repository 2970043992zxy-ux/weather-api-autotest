# api_client.py
import requests
from config import BASE_URL, API_KEY, CITY_LOCATION, UNITS

def get_current_weather():
    '''获取当前的天气信息'''
    params = {
        'q': CITY_LOCATION,
        'appid': API_KEY,
        'units': UNITS
    }
    # 发送get请求
    response = requests.get(BASE_URL, params=params, timeout=10)
    # 将响应转换为JSON格式并返回
    return response

# 本地调试用，运行这个文件可以手动测试接口
if __name__ == '__main__':
    resp = get_current_weather()
    print(f'状态码: {resp.status_code}')
    print(f'响应内容: {resp.json()}')
