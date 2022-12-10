import sys
import threading
import time
import os
import random
from playsound import playsound
from threading import Thread
import multiprocessing

# Получение текущего времени
def get_current_time() -> str:
    t = time.localtime()
    now_time = time.strftime("%H:%M:%S", t)
    return now_time


# Получение времени от пользователя на которое нужно установить будильник
def get_alarm_time() -> str:
    alarm_time = input("Введите время на которое хотите поставить будильник в формате 'HH:MM:SS' :-> ")
    return alarm_time


# Получение всех звуков которые лежат в папке \sounds
def get_alarm_sounds() -> list:
    sounds = []
    for root, dirs, files in os.walk("sounds"):
        for filename in files:
            sounds.append(filename)
    return sounds


# Получение выбора звука от пользователя
def set_alarm_sound(sounds: list) -> str:
    t = 1
    for sound in sounds:
        print(f'{t}:{sound}')
        t += 1
    choise_sound = input('Выберите звук для будильника из представленного списка: -> ')
    return sounds[int(choise_sound) - 1]


# Проигрывание звука, который установил пользователь
def play_alarm_sound(sound_name: str) -> None:
    playsound(f"sounds/{sound_name}", block=False)


# Угадай число чтобы остановить будильник
def math_to_stop(p) -> None:
    random_number = random.choice(range(1, 100, 1))
    while True:
        input_choise = input("Введи число: ->")
        if input_choise == str(random_number):
            p.terminate()
            break
        elif int(input_choise) < random_number:
            print("Загаданное число больше!!!")
        elif int(input_choise) > random_number:
            print('Загаданное число меньше!!!')
        else:
            print("Введи число меньше 100!!!")


# Логика будильника
def alarm_logic() -> None:
    alarm_time = get_alarm_time()
    choise_sound = set_alarm_sound(get_alarm_sounds())
    while alarm_time != get_current_time():
        time.sleep(0.5)
    p = multiprocessing.Process(target=play_alarm_sound(choise_sound))
    p.start()
    math_to_stop(p)
