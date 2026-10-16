import time
import os
import subprocess
import pyautogui
import pygetwindow as gw
import shutil




#shutil.rmtree(r"C:\Users\muhammet\AppData\Roaming\discord",ignore_errors = True)  WIP

#-------------------------------------------------------------------

os.startfile(r"C:\Users\muhammet\Desktop\Discord.lnk") #Programı Başlatıyor

#-------------------------------------------------------------------

time.sleep(26) #Programın yüklenmesi için 3 saniyelik bir zaman aralığı

#-------------------------------------------------------------------

screens = gw.getWindowsWithTitle("Discord") #Masaüstünedeki açık olan programlardan "Discord" isimli programı liste formatında buluyor birden fazla aynı program varsa listeye ekliyor

#-------------------------------------------------------------------

if screens: #Eğer listede eleman varsa

    screen = screens[0] #Listenin ilk elemanı yani istenen program

    if screen.isMinimized: #Program simge durumunda mı
        screen.restore() #Programı normal boyuta getirme

else:
    print("Program açılmadı") #Eğer program bulunamadıysa geri bildirim verir

#-------------------------------------------------------------------

screen.activate() #Seçilen programı en üste odak noktaya getirir

time.sleep(12)

pyautogui.write("karatassmuhammet18",interval=0.1)
pyautogui.hotkey("ctrl","alt","q")
pyautogui.write("gmail.com",interval=0.1)
time.sleep(0.8)
pyautogui.press("tab")
time.sleep(0.8)
pyautogui.write("1234567890Dominus_YT6",interval=0.1)
time.sleep(0.8)
pyautogui.press("tab")
time.sleep(0.8)
pyautogui.press("tab")
time.sleep(0.8)
pyautogui.press("space")

print("Bitti")
