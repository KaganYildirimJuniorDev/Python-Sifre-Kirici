import keyboard
import time
import string
from itertools import product

print("Lütfen şifre kutusuna tıkla. 5 saniye içinde başlıyor...")
time.sleep(5)

chars = string.ascii_lowercase

for length in range(1, 4):
    for combo in product(chars, repeat=length):
        guess = ''.join(combo)

        keyboard.write(guess)
        keyboard.send("enter")

        print(f"Denendi: {guess}")
        time.sleep(0.05)
