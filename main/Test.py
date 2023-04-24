# 导入所需的库和模块
import random
from datetime import datetime
import logging
import sys

# 设置日志记录器
logging.basicConfig(filename='olind_py.log', level=logging.DEBUG)

# 猜数字游戏方法
def guess_number():
    logging.info('猜数字游戏正在运行')
    answer = random.randint(1, 100)
    count = 0
    while True:
        count += 1
        try:
            guess = int(input('在此键入一个1~100之间的整数：'))
        except ValueError:
            print('参数不可用。请输入整数')
            logging.error('参数不可用，请输入整数')
            continue
        if guess < answer:
            print('您您猜小了')
        elif guess > answer:
            print('猜大了')
        else:
            print('恭喜你，猜对了！你一共猜了%d次' % count)
            logging.info('猜数字游戏已结束运行')
            break

# 定义猜谜语游戏方法
def guess_riddle():
    logging.info('猜谜语游戏正在运行')
    riddles = {'什么东西有头无身，有眼无眉，有耳无嘴？': '针', '什么东西一说它就不见了？': '沉默'}
    riddle = random.choice(list(riddles.keys()))
    answer = riddles[riddle]
    print(riddle)
    count = 0
    while True:
        count += 1
        guess = input('请键入你的答案：')
        if guess == answer:
            print('恭喜你，猜对了！你一共猜了%d次' % count)
            logging.info('猜谜语游戏已结束运行')
            break
        else:
            print('猜错了，请再试试')

# 定义获取天气方法
def get_weather(api_key, city):
    logging.info('获取天气信息正在运行')
    try:
        from pyowm import OWM
    except ImportError:
        print('pyowm库未安装，请先安装该库')
        logging.error('pyowm库未安装')
        return
    owm = OWM(api_key)
    mgr = owm.weather_manager()
    try:
        observation = mgr.weather_at_place(city)
    except Exception as e:
        print('出现了一点错误:( 这是错误信息：%s' % e)
        logging.error('获取天气信息失败，错误信息为：%s' % e)
        return
    weather = observation.weather
    status = weather.detailed_status
    temp = weather.temperature('celsius')['temp']
    print('当前%s的天气状况为：%s，气温为%.1f℃' % (city, status, temp))
    logging.info('获取天气信息已结束运行')

# 定义获取今日日历事件方法
def get_today_events(calendar_id, api_key):
    logging.info('获取今日日历事件正在运行')
    try:
        from google.oauth2 import service_account
        from googleapiclient.discovery import build
        from datetime import date, time, datetime, timedelta
    except ImportError:
        print('缺少必要的Python库，请先安装google-auth和google-api-python-client库')
        logging.error('缺少必要的Python库')
        return
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    SERVICE_ACCOUNT_FILE = 'credentials.json'
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    try:
        service = build('calendar', 'v3', credentials=credentials)
        now = datetime.utcnow().isoformat() + 'Z'
        events_result = service.events().list(calendarId=calendar_id, timeMin=now, maxResults=10, singleEvents=True, orderBy='startTime').execute()
        events = events_result.get('items', [])
    except Exception as e:
        print('出现了一点错误:( 错误信息为：%s' % e)
        logging.error('获取信息失败:( 错误信息为：%s' % e)
        return
    if not events:
        print('今天没有任何日历事件')
    else:
        print('今天的日历事件有：')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            start_time = datetime.fromisoformat(start)
            print('%s - %s' % (start_time.strftime('%H:%M'), event['summary']))
    logging.info('获取今日日历事件已结束运行')

# 定义获取当前时间方法
def get_current_time():
    logging.info('正在获取当前时间')
    now = datetime.now()
    print('当前时间为：%s' % now.strftime('%Y-%m-%d %H:%M:%S'))
    logging.info('结束运行完成')

# 定义主程序
def main():
    # 设置API密钥和城市
    api_key = '292x19o1'
    city = 'Beijing'
    # 设置Google日历API密钥和日历ID
    calendar_id = '2918'
    api_key_gcal = '29s129x'

    while True:
        # 获取用户输入
        query = input('你好，我是OlindPy，请问需要帮助什么...：')
        # 处理用户输入
        if query == '猜数字':
            guess_number()
        elif query == '猜谜语':
            guess_riddle()
        elif query == '天气':
            get_weather(api_key, city)
        elif query == '日历事件':
            get_today_events(calendar_id, api_key_gcal)
        elif query == '当前时间':
            get_current_time()
        elif query == '退出':
            print('再见！')
            logging.info('程序已退出')
            sys.exit()
        else:
            print('你的输入有误，请重新输入')

if __name__ == '__main__':
    main()
