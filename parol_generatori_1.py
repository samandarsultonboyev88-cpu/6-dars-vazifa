import random
import string

def parol_yarat(uzunlik):
    
    belgilar = string.ascii_letters + string.digits + string.punctuation
    
    parol = "".join(random.choice(belgilar) for _ in range(uzunlik))
    return parol

def parol_tekshir(parol):
   
    return len(parol) >= 8