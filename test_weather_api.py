# test_weather_api.py
import pytest
import allure
from api_client import get_current_weather

@allure.feature('天气API测试')
class TestWeatherAPI:

    @allure.story('基础功能测试')
    @allure.title('验证获取当前天气接口返回状态码为200')
    def test_status_code_is_200(self):
        response = get_current_weather()
        assert response.status_code == 200, f'预期状态码为200, 实际得到{response.status_code}'
    
    @allure.story('基础功能测试')  # 这里缩进要与第一个测试用例对齐
    @allure.title('验证返回数据包含必要的字段')
    def test_response_has_required_fields(self):
        response = get_current_weather()
        data = response.json()

        # OpenWeatherMap的字段结构
        assert 'main' in data, "响应中缺少 'main' 字段"
        assert 'weather' in data, "响应中缺少 'weather' 字段"

        main_data = data['main']
        required_fields = ['temp', 'feels_like', 'humidity']
        for field in required_fields:
            assert field in main_data, f"main对象中缺少 '{field}' 字段"
        
        # 检查weather数组
        assert len(data['weather']) > 0, 'weather数组为空'
        weather_data = data['weather'][0]
        assert 'description' in weather_data, "weather缺少description字段"
    
    @allure.story('业务逻辑测试')  # 这里也要对齐
    @allure.title('验证温度数据格式正确')
    def test_temperature_format(self):
        response = get_current_weather()
        data = response.json()
        temp = data['main']['temp']

        # 将温度值转换成浮点数进行检查
        temp_float = float(temp)
        assert -50 <= temp_float <= 50, f"温度值{temp}不在合理范围(-50~50)内"