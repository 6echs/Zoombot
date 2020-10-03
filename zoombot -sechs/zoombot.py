#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import sys
import pynput
import time
import schedule
import pyautogui

ZOOM_PATH = "C:\\Users\\Uzman\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"

# Buraya x değişkenlerinin yerine derslerin passcodelarını yaz

SIFRELER = {
    "kimyapass": "123456",
    "biyolojipass": "xxxxxx",
    "fizikpass": "xxxxxx",
    "edebiyatpass": "xxxxxx",
    "mat1pass": "xxxxxx",
    "mat2pass": "xxxxxx"
    
}

# Buraya meeting id'leri yaz

BULUSMALAR = {
    "kimya": "123 456 7890",
    "biyoloji": "xxx xxx xxxx",
    "fizik": "xxx xxx xxxx",
    "edebiyat": "xxx xxx xxxx",
    "mat1": "xxx xxx xxxx",
    "mat2": "xxx xxx xxxx"
}
def start_zoom(path):
    subprocess.Popen([ZOOM_PATH], shell=False, stdin=None, stdout=None, stderr=None, close_fds=True)

def close_zoom():
    subprocess.Popen(["taskkill", "/f", "/im", "Zoom.exe"], shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
    time.sleep(1)

def join_meeting(meeting_id, sifre_id, meeting_min=60, width=300, height=400):
    print("* Eski Zoom kapatılıyor.")
    close_zoom()
    time.sleep(3)
    print("* Yeni Zoom açılıyor.")
    start_zoom(ZOOM_PATH)
    time.sleep(3)   
    
    # Join a Meeting
    time.sleep(3)
    print("* Buluşmaya katıl butonuna tıklanıyor.")
    join_btn = pyautogui.locateCenterOnScreen('join_buton.png')
    pyautogui.moveTo(join_btn)
    pyautogui.click()
    time.sleep(3)
    
    # Meeting ID
    print("* ID giriliyor.")
    pyautogui.write(meeting_id)
    # Join
    join2_btn = pyautogui.locateCenterOnScreen('join2_btn.png')
    pyautogui.moveTo(join2_btn)
    pyautogui.click()
    time.sleep(5)
    
    # Passcode
    print("* Passcode yazılıyor.")
    pyautogui.write(sifre_id)
    pyautogui.press('enter')
    time.sleep(2)
    print("* Buluşmaya katılınıyor.")
    
    timer = 0
    while (timer != meeting_min):
        time.sleep(15)
        time.sleep(15)
        time.sleep(15)
        time.sleep(15)
        timer = timer + 1
    
    print ("* Buluşma bitti.")
    close_zoom()
    
def enter_class(ders,sifre):
    meeting_id = BULUSMALAR[ders]
    sifre_id = SIFRELER[sifre]
    try:
        join_meeting(meeting_id, sifre_id, meeting_min=39)
    except e:
        print(e)
        enter_class(ders,sifre)
        
# Tırnak içine alınmış dersleri ve saatleri kendi programına göre ayarlayabilirsin, aynı zamanda şifre kısmını da değişmeyi unutma.

def set_schedules():
    print("* Tarihler ayarlandı!")
    schedule.every().monday.at("08:00").do(enter_class, ders="kimya", sifre="kimyapass" )
    schedule.every().monday.at("08:55").do(enter_class, ders="kimya", sifre="kimyapass")
    schedule.every().monday.at("09:45").do(enter_class, ders="mat1", sifre="mat1pass")
    schedule.every().monday.at("10:35").do(enter_class, ders="biyoloji", sifre="biyolojipass")
    schedule.every().monday.at("11:25").do(enter_class, ders="fizik", sifre="fizikpass")
    
    schedule.every().tuesday.at("08:00").do(enter_class, ders="mat2", sifre="mat2pass")
    schedule.every().tuesday.at("08:55").do(enter_class, ders="mat2", sifre="mat2pass")
    schedule.every().tuesday.at("09:45").do(enter_class, ders="fizik", sifre="fizikpass")
    schedule.every().tuesday.at("10:35").do(enter_class, ders="fizik", sifre="fizikpass")
    schedule.every().tuesday.at("11:25").do(enter_class, ders="fizik", sifre="fizikpass")
    
    schedule.every().wednesday.at("08:00").do(enter_class, ders="mat2", sifre="mat2pass")
    schedule.every().wednesday.at("08:55").do(enter_class, ders="mat2", sifre="mat2pass")
    schedule.every().wednesday.at("09:45").do(enter_class, ders="edebiyat", sifre="edebiyatpass")
    schedule.every().wednesday.at("10:35").do(enter_class, ders="mat1", sifre="mat1pass")
    schedule.every().wednesday.at("11:25").do(enter_class, ders="biyoloji", sifre="biyolojipass")
    
    schedule.every().thursday.at("08:00").do(enter_class, ders="mat2", sifre="mat2pass")
    schedule.every().thursday.at("08:55").do(enter_class, ders="mat2", sifre="mat2pass")
    schedule.every().thursday.at("09:45").do(enter_class, ders="kimya", sifre="kimyapass")
    schedule.every().thursday.at("10:35").do(enter_class, ders="mat1", sifre="mat1pass")
    schedule.every().thursday.at("11:25").do(enter_class, ders="biyoloji", sifre="biyolojipass")
    
    schedule.every().friday.at("08:00").do(enter_class, ders="edebiyat", sifre="edebiyatpass")
    schedule.every().friday.at("08:55").do(enter_class, ders="kimya", sifre="kimyapass")
    schedule.every().friday.at("09:45").do(enter_class, ders="biyoloji", sifre="biyolojipass")
    schedule.every().friday.at("10:35").do(enter_class, ders="biyoloji", sifre="biyolojipass")
    schedule.every().friday.at("11:25").do(enter_class, ders="mat2", sifre="mat2pass")
    
    print("* Sınıf bekleniyor.")

if __name__ == "__main__":
    set_schedules()
    while True:
        schedule.run_pending()
        time.sleep(1)
