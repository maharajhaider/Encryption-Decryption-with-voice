import pyttsx3
import string
import collections
class decryption:
    def __init__(self,oentext,keyword1,rotate_str,rotation_number):
        self.oentext=oentext
        self.key=keyword1
        self.rotate_str=rotate_str
        self.rotation_number=rotation_number
    


    def caesar(self,rotate_str, rotation_number):

         upper= collections.deque(string.ascii_uppercase)
         lower= collections.deque(string.ascii_lowercase)

         upper.rotate(rotation_number)
         lower.rotate(rotation_number)

         upper = ''.join(list(upper))
         lower = ''.join(list(lower))

         return rotate_str.translate(str.maketrans(string.ascii_uppercase, upper)).translate(str.maketrans(string.ascii_lowercase, lower))





        
    def vigeneredecipher(self,oentext,keyword1):
         key = keyword1
         kl = list(keyword1)
         entext="".join(oentext.split())

         if len(entext) != len(keyword1):
             for i in range(len(entext) - len(keyword1)):
                 key = key + kl[i]
                 kl.append(kl[i])
         decipher = ""
         letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
               "u", "v",
               "w", "x", "y", "z"]
         for i in range(len(entext)):
             num = 0
             ltpos = 0
             lkpos = 0
             if entext[i].isalpha() == True:
                 if entext[i].islower() == True:
                     for j in range(len(letters)):
                         if entext[i] == letters[j]:
                             ltpos = j
                         if key[i] == letters[j]:
                             lkpos = j
                     num = int(ltpos - lkpos)
                     num = num % 26
                     decipher = decipher + letters[num]
                 elif entext.isupper()==True:
                     for q in range(len(letters)):
                         letters[q] = letters[q].upper()
                     for j in range(len(letters)):
                         if entext[i] == letters[j]:
                             ltpos = j
                         if key[i] == letters[j]:
                             lkpos = j
                     num = int(ltpos - lkpos)
                     num= num % 26
                     decipher = decipher + letters[num]
             else:
                 decipher=decipher+decipher[i]

         for i in range(len(oentext)):
             if oentext[i]==" ":
                 decipher=decipher[:i]+" "+decipher[i:]

         return(decipher)
myobject=decryption("IHSQIRIHCQCU","IOZQGH","EXXEGOEXSRGI",4)
print(myobject.vigeneredecipher("IHSQIRIHCQCU","IOZQGH"))
print(myobject.caesar("EXXEGOEXSRGI",4))
speaker=pyttsx3.init()
speaker.say(myobject.vigeneredecipher("IHSQIR IH CQCU","IOZQGH"))
speaker.runAndWait()
speaker.say(myobject.caesar("EXXEGO EX SRGI",4))
speaker.runAndWait()