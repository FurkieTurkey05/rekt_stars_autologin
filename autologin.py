import pyautogui
import pyperclip
import time
import cryptocode
import uuid    
uuuid=str(uuid.UUID(int=uuid.getnode()))
open("keys.txt","a").close
try:
    cryptkey=cryptocode.decrypt(open("crypt.txt","r",encoding="utf-8").read(),uuuid)
    if cryptkey == False:
        print("[device not recognized, + for add device login key]")
        cryptkey=input("enter key for decrption\n>>>")
    print("[device recognized]")
except:
    print("[+ for add device login key]")
    cryptkey=input("enter key for decrption\n>>>")
    if cryptkey == "+":
        hwdecrypt=input("enter key for this device\n>>>")
        try:
            open("crypt.txt","w",encoding="utf-8").write(cryptocode.encrypt(hwdecrypt,uuuid))
        except FileNotFoundError:
            open("crypt.txt","a",encoding="utf-8").write(cryptocode.encrypt(hwdecrypt,uuuid))

while True:
    keyslist=open("keys.txt","r",encoding="utf-8").read().split("\n")
    n=0
    has_available_login=False
    for x in keyslist:
        if keyslist.index(x) % 2 == 0 and x != "":
            n=n+1
            print(str(n)+"- "+x)
            has_available_login=True
    if has_available_login==False:
        print("0- no recoded login available")
    x = input("[select login type]\n[q to exit, + to record login]\n>>>")
    if x == "q":
        break
    if x == "+":
        new_name=input("enter name for new login\n>")
        available=False
        while available == False:
            try:
                isinlist=keyslist.index(new_name)
                new_name=input("this login name was taken!!!\nenter name for new login\n>>>")
            except:
                available=True
        new_pass=input("enter password for new login\n>")
        new_pass=cryptocode.encrypt(new_pass,cryptkey)
        open("keys.txt","a",encoding="utf-8").write(f"{new_name}\n{new_pass}\n")  
        print("success")
    else:
        try:
            index=int(keyslist.index(x)+1)
        except ValueError:
            index=int(int(x)*2)-1
        if cryptocode.decrypt(keyslist[index],cryptkey)!=False:
            pyperclip.copy(cryptocode.decrypt(keyslist[index],cryptkey))
            pyautogui.hotkey("alt","tab")
            time.sleep(.2)
            pyautogui.hotkey("ctrl","v")
            pyautogui.press("enter")
        else:
            print("incorrect key for decrption")
            cryptkey=input("enter key for decrption\n>>>")
#rektstars autologin#