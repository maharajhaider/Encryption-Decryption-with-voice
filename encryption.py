import pyttsx3

class encryption:
    def __init__(self, otext, keyword, number,p,q):
        self.otext = otext
        self.keyword = keyword
        self.number=number
        self.p=p
        self.q=q

    def caesar(self,otext,number):
         import string
         import collections
         upper= collections.deque(string.ascii_uppercase)
         lower= collections.deque(string.ascii_lowercase)

         upper.rotate(number)
         lower.rotate(number)

         upper = ''.join(list(upper))
         lower = ''.join(list(lower))
         print (otext.translate(str.maketrans(string.ascii_uppercase, upper)).translate(str.maketrans(string.ascii_lowercase, lower)))


    def vigenerecipher(self, otext, keyword):

        key = keyword
        kl = list(keyword)
        text = "".join(otext.split())

        if len(text) != len(keyword):
            for i in range(len(text) - len(keyword)):
                key = key + kl[i]
                kl.append(kl[i])

        cipheredtext = ""
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                   "t", "u", "v",
                   "w", "x", "y", "z"]

        for i in range(len(text)):
            cipher = 0
            ltpos = 0
            lkpos = 0
            if text[i].isalpha() == True:
                if text[i].islower() == True:
                    for j in range(len(letters)):
                        if text[i] == letters[j]:
                            ltpos = j
                        if key[i] == letters[j]:
                            lkpos = j
                    cipher = ltpos + lkpos
                    cipher = cipher % 26
                    cipheredtext = cipheredtext + letters[cipher]
                elif text[i].isupper() == True:
                    for q in range(len(letters)):
                        letters[q] = letters[q].upper()
                    for j in range(len(letters)):
                        if text[i] == letters[j]:
                            ltpos = j
                        if key[i] == letters[j]:
                            lkpos = j
                    cipher = ltpos + lkpos
                    cipher = cipher % 26
                    cipheredtext = cipheredtext + letters[cipher]
            else:
                cipheredtext = cipheredtext + text[i]
        for i in range(len(otext)):
            if otext[i] == " ":
                cipheredtext = cipheredtext[:i] + " " + cipheredtext[i:]

        print(cipheredtext)


    def RSA(self,otext,p,q):

        from decimal import Decimal

        n = p * q
        u = (p - 1) * (q - 1)

        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)

        for j in range(2, u):
            if gcd(j, u) == 1:
                break

        for i in range(1, 10):
            x = 1 + i * u
            if x % j == 0:
                d = int(x / j)
                break

        for i in otext:
            c = Decimal(0)
            Z = ord(i)
            c = pow(Z, j)
            ce = c % n
            if Z <98:
                print(chr(ce + 64),end="")
            else:           
                print(chr(ce + 64),end="")


f1 = encryption("ATTACK AT DAWN", 'LEMON',5,6,3)
f1.vigenerecipher("ATTACKATDAWN", "LEMON")
f1.caesar("ATTACKATDAWN",5)
f1.RSA("ATTACKATDAWN",6,3)

speaker=pyttsx3.init()
speaker.say(f1.otext)
speaker.runAndWait()
