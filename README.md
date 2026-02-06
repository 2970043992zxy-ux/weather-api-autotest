# weather-api-autotest
# 天气API自动化测试项目

## 项目简介
这是一个用于学习和演示的**接口自动化测试**项目。使用 Python 对OpenWeatherMap的开放API进行自动化测试，涵盖了状态码验证、数据结构校验和业务逻辑验证。

## 技术栈
- **编程语言**: Python 3
- **测试框架**: pytest
- **HTTP请求库**: requests
- **测试报告**: Allure
- **版本控制**: Git

## 项目结构
weather_api_test/
├── api_client.py # 接口请求封装
├── config.py # 配置文件（需自行添加API Key）
├── test_weather_api.py # 测试用例
├── requirements.txt # 依赖库列表
└── README.md # 项目说明

## 如何运行
1. 克隆项目: `git clone https://github.com/2970043992zxy-ux/weather-api-autotest.git`
2. 安装依赖: `pip install -r requirements.txt`
3. 运行测试: `pytest test_weather_api.py -v --alluredir=./allure-results`
4. 查看报告: `allure serve ./allure-results`

## 测试用例设计
1. **基础功能测试**：验证接口可访问性、状态码和响应结构。
2. **业务逻辑测试**：验证关键数据字段（如温度）的合理性和格式。

## 项目目标
通过这个实战项目，我掌握了：
- 使用 Python requests 库进行接口测试
- 使用 pytest 框架组织测试用例
- 使用 Allure 生成专业测试报告
- 完整的自动化测试项目搭建流程
