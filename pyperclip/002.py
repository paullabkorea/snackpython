import time
import pyperclip

복사된값 = pyperclip.paste()
data = [int(value) for value in 복사된값.split('\r\n') if value]
print(복사된값)