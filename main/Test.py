import random
import pyowm
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, time, timedelta

    def __init__(self):
        self.name = "Olind-Py"
        self.guesses = 0
        self.riddles = [
            {
                "question": "什么东西一看就会让你觉得很饿？",
                "answer": "菜单"
            },
            {
                "question": "什么东西有头有尾，中间却什么都没有？",
                "answer": "硬币"
            },
            {
                "question": "什么东西越吃越饿？",
                "answer": "火锅"
            }
        ]

  def run(self):
        self.greet()
        while True:
            command = input("请输入命令（猜谜语/菜单/退出）：")
            if command == "猜谜语":
                self.guess_riddle()
            elif command == "菜单":
                self.chat()
            elif command == "退出":
                print(f"你和我一共猜了{self.guesses}个谜语。")
                break
            else:
                print(f"{self.name}：我不太明白你的意思")
                
    def guess_riddle(self):
        riddle = random.choice(self.riddles)
        print(riddle["question"])
        answer = input("请输入答案：")
        if answer == riddle["answer"]:
            print("恭喜你，你的答案正确的")
        else:
            print(f"很遗憾，答案是{riddle['answer']}。")
        self.guesses += 1
        
def guess_number():
    number = random.randint(1, 100)
    guess = 0
    while guess != number:
        guess = int(input("从1-100选择一个数字以猜测"))
        if guess < number:
            print("你所键入的数字太小了，请重试")
        elif guess > number:
            print("你所键入的数字太大了，请重试")
    print("恭喜你猜对了！")

def get_weather(city):
    owm = pyowm.OWM('0x129cy2') # APIkey
    observation = owm.weather_at_place(city)
    weather = observation.get_weather()
    temperature = weather.get_temperature('celsius')['temp']
    status = weather.get_detailed_status()
    print(f"{city}当前的天气情况是{status}，当前温度为{temperature}摄氏度。")

def get_today_events():
    scopes = ['https://www.googleapis.com/auth/calendar.readonly']
    service_account_file = 'Olind/test'  # Service Account路径
    credentials = service_account.Credentials.from_service_account_file(service_account_file, scopes=scopes)
    service = build('calendar', 'v3', credentials=credentials)
    today = datetime.utcnow().date()
    start_of_today = datetime.combine(today, time.min).isoformat() + 'Z'
    end_of_today = datetime.combine(today, time.max).isoformat() + 'Z'
    events_result = service.events().list(calendarId='primary', timeMin=start_of_today, timeMax=end_of_today, singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        print('今天没有任何日历事件。')
    else:
        print('今天的日历事件如下：')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            start_time = datetime.fromisoformat(start).strftime('%H:%M')
            print(f"{start_time} - {event['summary']}")

def get_current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"当前时间为{current_time}。")

print("您好，我是OlindPy，一款由Olind新开发的bot，请问您需要什么帮助？")

while True:
    command = input("请输入您的问题：")
    if "猜数字" in command:
        guess_number()
    elif "天气" in command:
        city = input("请输入您要查询的城市：")
        get_weather(city)
    elif "日历" in command:
        get_today_events()
    elif "时间" in command:
        get_current_time()
    elif "时间" in command:
        get_current_time()
    elif "谜语" in command:
        self.guess_riddle()
    elif "再见" in command:
        print("再见，希望下次遇到你")
        break
    else:
        print("很抱歉，你的问题我无法回答，请重试...")
