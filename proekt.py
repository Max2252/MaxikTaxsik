import random
import time


# a  = [2,4,6,7,8]

# print( random.choices(a, weights=[0.2, 0.2, 0.2,0.2, 0.2], k = 10))

# import random

# a = random.choice([random.randint(1,200),"21312","dqwasdsa",random.randint(1,200)])
# print(a)
a = {
    "██╗░░██╗███████╗" : "",
    "██║░░██║██╔════╝" : "",
    "███████║█████╗░░" : "",
    "██╔══██║██╔══╝░░" : "",
    "██║░░██║███████╗" : "",
    "╚═╝░░╚═╝╚══════╝" : "",

    "██╗░░░██╗███╗░░██╗██████╗░███████╗██████╗░████████╗░█████╗░██╗░░░░░███████╗" : "",
    "██║░░░██║████╗░██║██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔══██╗██║░░░░░██╔════╝" : "",
    "██║░░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝░░░██║░░░███████║██║░░░░░█████╗░░" : "",
    "██║░░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗░░░██║░░░██╔══██║██║░░░░░██╔══╝░░" : "",
    "╚██████╔╝██║░╚███║██████╔╝███████╗██║░░██║░░░██║░░░██║░░██║███████╗███████╗" : "",
    "░╚═════╝░╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝" : "",}

bosse = random.choice(["Босс Смертных","Челик","Häpuchi","你的死！","Гарри Поттер"])

hpboss = random.randint(75,200)

hpplayr = 100


damagekastet = random.randint(1,74)

items = {"Яблоко": " - Востанавливает вам 20 HP", "Кастеты": " - Нанести Урон","Enchanted golden apple(Яблоко 2)": " - +100 hp"}

energyplayr = 100

energybos = 100


def smert(damagekastet):
    if damagekastet <= 10:
        print("Вы позекотали ему пятки")
        time.sleep(1)
        print(f"Вы нанесли урона {damagekastet}")
    elif damagekastet <= 50 and damagekastet != 10:
        print("Вы побили бедного боса до потери сознания")
        time.sleep(1)
        print(f"Вы нанесли урона {damagekastet}")
    elif damagekastet > 50:
        print("По моему он перестал дышать...")
        
        time.sleep(1)
        print(f"Вы нанесли урона {damagekastet}")



for key in a:
    print(key)
a = input("Нажмите Enter для старта")
while True:
    if a == "":
        break
    else:
        print(a)
    a = input("Нажмите Enter для старта")
while True:
    damageplayre = [0,10,20,30,40,50]
    damageplayr = random.choice(damageplayre)
    damagebosse = [0,10,20,30,40,50]
    damageboss = random.choice(damagebosse)
    enersys = random.randint(10,50)
    enersyse = random.randint(10,50)
    energysp = random.randint(10,50)
    energyb = random.randint(10,50)
    print("_______________________________________________________________")
    print(f"Ваш враг:{bosse}")
    print(f"Его здоровье:{hpboss}")
    print()
    print()
    print(f"Ваша энергия:{energyplayr}")
    print(f"Ваше здоровье:{hpplayr} ")
    print("[ИНВЕНТАРЬ]   [ВОСТАНОВИТЬ ЭНЕРГИЮ]   [АТАКА]")
    print()
    print("1 - Инвентарь;2 - Востановить энергию;3 - Удар")
    xod = int(input("Выберите категорию: "))
    print("_______________________________________________________________")
    if energybos <= energyb:
        print("Враг усталь...🌚")
        energybos += enersyse
    if xod == 1:
        print("Ваш инвентарь: ",items)
        deystvie = input("Ваш действия(Для выхода напишите назад): ").lower()
        print("Напишите предмет")
        print("_______________________________________________________________")
        if deystvie == "яблоко" and "Яблоко" in items:
            print("Вы съeли яблоко")
            time.sleep(1)
            hpplayr += 20
            del items["Яблоко"]
        if deystvie == "кастеты" and "Кастеты" in items:
            smert(damagekastet)
            hpboss -= damagekastet
            time.sleep(1)
            del items["Кастеты"]
        if deystvie == "яблоко 2" and "Enchanted golden apple(Яблоко 2)" in items:
            print("Вы съeли Enchanted golden apple")
            time.sleep(1)
            hpplayr += 100
            del items["Enchanted golden apple(Яблоко 2)"]
        if deystvie == "назад":
            print()
    if xod == 2:
        print(f"Вы востановили энергию:{energysp} энергии")
        energyplayr += enersys
        time.sleep(1)
        if energybos <= energyb:
            print("Враг усталь...🌚")
            energybos += enersyse
            time.sleep(1)
        else:
            print(f"Враг наносит вам {damageboss} урона")
            hpplayr -= damageboss
            time.sleep(1)
    elif xod == 3:
        if energyplayr >= energysp:
            print(f"Вы наносите {damageplayr} урона")
            energyplayr -= energysp
            hpboss -= damageplayr
            time.sleep(1)
        else:
            print("Недостаточно энергии".upper())
            time.sleep(1)
            print("1 - Инвентарь;2 - Востановить энергию;3 - Удар")
            xod = int(input("Выберите категорию: "))
        if energybos >= energyb and hpboss > 0:
            print(f"Враг наносит вам {damageboss} урона")
            hpplayr -= damageboss
            time.sleep(1)
        else:
            print("Враг усталь...🌚")
            energybos += enersyse
            time.sleep(1)
    if hpboss <= 0:
        print("_______________________________________________________________")
        print("Бос повержен!")
        time.sleep(3)
        print("ВЫ ПРОШЛИ ЭТУ СУПЕР, ПУПЕР, МУПЕР НАВАРОЧЕННУЮ ИГРУ ИЗ ФИКАЛИЯ И ДРУГОЙ ДРЕБЕДЕНЕ!!!")
        time.sleep(10)
        print("Вот ваше ничего 😁🌚")
        print("_______________________________________________________________")
        break
    if hpplayr <= 0:
        print("Вы проиграли...")
        break