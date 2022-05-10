import json, requests, random , keyboard, time, os
os.system("title GuildInviter by Yumix_ =)")
global nicknames
nicknames = []

settings = [
    50, # matches count
    "Сюды ваш токен", #/api dev vimeworld token
    0.85, # kd /g i (seconds)
    5, #minimum player level
] 
'''
# Такой код сеттингсов в билде: 
# KD установлен на 1, т.к. 0.85 бывает багается, а в int() можно запихнуть ток целые числа.
settings = [
    int(input("Введите количество матчей для парсинга: ")), # matches count
    input("Введите ключ разработчика: (Без него, увы, никак): "), #/api dev vimeworld token
    1, # kd /g i (seconds)
    int(input("Введите минимальный уровень игрока: ")), #minimum player level
] 
'''
print("Количество матчей: " + str(settings[0]))
print("Ключ разработчика: " + settings[1][:-5] + '*'*5)
print('Задержка при вводе команды "/g i" (в секундах): ' + str(settings[2]))
print("Минимальный лвл игрока: " + str(settings[3]))
req = requests.get("https://api.vimeworld.com/match/latest?token=" + settings[1] +"&count=" + str(settings[0])).json()
print("Начинаем парсинг! ")
for j in range(len(req)): 
    match_id = req[j]["id"]
    match_info = requests.get("https://api.vimeworld.com/match/" + match_id + "?token=" + settings[1]).json()
    print("Начал парсить матч #" + match_id + " [" + match_info["game"]  + "]")
    try: 
        b = 0
        for i in range(len(match_info["players"])): 
            player_id = match_info["players"][i]["id"]
            if requests.get("https://api.vimeworld.com/user/" + str(player_id) + "?token=" + settings[1]).json()[0]["level"]  > settings[3]  and not (requests.get("https://api.vimeworld.com/user/" + str(player_id) + "?token=" + settings[1]).json()[0]["username"] in nicknames):  

                try: 
                    guild_name = requests.get("https://api.vimeworld.com/user/" + str(player_id) + "/stats?token=" + settings[1]).json()["user"]["guild"]["name"]
                except: 
                    b+=1
                    nicknameById = requests.get("https://api.vimeworld.com/user/" + str(player_id) + "?token=" + settings[1]).json()[0]["username"]
                    nicknames.append(nicknameById)
        print("Запарсил матч #" + match_id + " [" + match_info["game"] + "] (По счету " + str(j+1) +"/" + str(settings[0]) + ")")
        print("В матче " + match_id + "я нашел " + str(b) + " игрока(-ов)")
    except Exception as e:     
        print("что-то пошло не так во время парсинга матча #" + match_id)
        print(e)
        break
if not nicknames: 
    print("Я не нашел ни одного игрока по заданным параметрам :(")
    os.system("pause")
    exit()
print("Игроки: ")
print(', '.join(map(str,nicknames)))
#print("(Массив Python): ")
#print(nicknames)
for i in range(len(nicknames)): 
    time.sleep(settings[2])
    keyboard.press_and_release("t");time.sleep(0.1)
    keyboard.write("/g i " + nicknames[i])
    keyboard.press_and_release("enter")
