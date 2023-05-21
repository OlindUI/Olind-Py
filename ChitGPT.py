mport requests
import urllib.parse

api_url = "https://ybapi.cn/API/gpt.php?type=chit&msg="
user_input = input("Olind ")
question = urllib.parse.quote(user_input)
response = requests.get(api_url+question).json()
ai_answer = response["text"]
print(ai_answer)
