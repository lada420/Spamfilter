#coding=utf8
import nilsimsa
from nilsimsa import Nilsimsa

POPC = [ord(x) for x in
    "\x00\x01\x01\x02\x01\x02\x02\x03\x01\x02\x02\x03\x02\x03\x03\x04"\
    "\x01\x02\x02\x03\x02\x03\x03\x04\x02\x03\x03\x04\x03\x04\x04\x05"\
    "\x01\x02\x02\x03\x02\x03\x03\x04\x02\x03\x03\x04\x03\x04\x04\x05"\
    "\x02\x03\x03\x04\x03\x04\x04\x05\x03\x04\x04\x05\x04\x05\x05\x06"\
    "\x01\x02\x02\x03\x02\x03\x03\x04\x02\x03\x03\x04\x03\x04\x04\x05"\
    "\x02\x03\x03\x04\x03\x04\x04\x05\x03\x04\x04\x05\x04\x05\x05\x06"\
    "\x02\x03\x03\x04\x03\x04\x04\x05\x03\x04\x04\x05\x04\x05\x05\x06"\
    "\x03\x04\x04\x05\x04\x05\x05\x06\x04\x05\x05\x06\x05\x06\x06\x07"\
    "\x01\x02\x02\x03\x02\x03\x03\x04\x02\x03\x03\x04\x03\x04\x04\x05"\
    "\x02\x03\x03\x04\x03\x04\x04\x05\x03\x04\x04\x05\x04\x05\x05\x06"\
    "\x02\x03\x03\x04\x03\x04\x04\x05\x03\x04\x04\x05\x04\x05\x05\x06"\
    "\x03\x04\x04\x05\x04\x05\x05\x06\x04\x05\x05\x06\x05\x06\x06\x07"\
    "\x02\x03\x03\x04\x03\x04\x04\x05\x03\x04\x04\x05\x04\x05\x05\x06"\
    "\x03\x04\x04\x05\x04\x05\x05\x06\x04\x05\x05\x06\x05\x06\x06\x07"\
    "\x03\x04\x04\x05\x04\x05\x05\x06\x04\x05\x05\x06\x05\x06\x06\x07"\
    "\x04\x05\x05\x06\x05\x06\x06\x07\x05\x06\x06\x07\x06\x07\x07\x08"]



def comp(dig1, dig2, threshold=None):
    bits = 0
    for i in range(0, 63, 2):
        bits += POPC[255 & int(dig1[i:i + 2], 16) ^ int(dig2[i:i + 2], 16)]
        if threshold is not None and bits > threshold: break
    return 128 - bits

spam_ex = ["Hey bob! Nice to meet you!", "Hey Jane! How is your day? Wanna relax a bit?", "Cute kittens are in danger! Donate 0.3 bitcoin to save them!"]
spamhexes = [str(spam_ex[0]).encode('hex'), str(spam_ex[1]).encode('hex'), str(spam_ex[2]).encode('hex')]
spamhashes = [str(Nilsimsa(spamhexes[0])).encode('hex'), str(Nilsimsa(spamhexes[1])).encode('hex'), str(Nilsimsa(spamhexes[2])).encode('hex')]
msges = []
score = 0
while 1:
    new_msg = str(raw_input())              #Пришло письмо
    new_msg_hex=str(new_msg.encode("hex"))  #Перевели его в хекс
    nilhash = Nilsimsa(new_msg_hex)         #Взяли хеш
    print nilhash
    nilhash_s = str(nilhash).encode('hex')  #Перевели хеш в хексы и строку
    for hash in range(len(spamhashes)):
        score = comp(nilhash_s, spamhashes[hash], threshold=110)
        if score >= 64:
            spam.append(new_msg)
            break
        msges.append(new_msg)