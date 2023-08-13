import datetime

입력 = input("입력: ")

if "howru" in 입력:
    print("imgood")
elif "month" in 입력:
    now = datetime.datetime.now()
    print(f"Today is {now.month}")
elif "day" in 입력:
    now = datetime.datetime.now()
    print(f"Today is {now.day}")
else:
    print(입력)