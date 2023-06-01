#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random


def main():
    hexa2chara = {
    '0000': 'f',
    '0001': 'g',
    '0010': 'h',
    '0011': 'i',
    '0100': 'j',
    '0101': 'k',
    '0110': 'l',
    '0111': 'm',
    '1000': 'n',
    '1001': 'o',
    '1010': 'p',
    '1011': 'q',
    '1100': 'r',
    '1101': 's',
    '1110': 't',
    '1111': 'u'
    }

    chara2hexa = {x:y for y,x in hexa2chara.items()}
    XOR_values = list((bin(0x0000801000004000))[2:].zfill(64))
    XOR_values = [int(x) for x in XOR_values]
    bin_plain_texts = []

    def binp():
        for i in range(2500):
            temp = np.random.choice(['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u'],size=(1,16),replace = True)[0]
            bin_input=[]
            for i in temp:
                bin_input.extend([int(a) for a in chara2hexa[i]])

            bin_plain_texts.append(bin_input)
            bin_plain_texts.append(list(np.bitwise_xor(bin_input,XOR_values)))
    binp()

    plaintexts = []

    def plain():
        for i in range(len(bin_plain_texts)):
            s = ""
            for j in range(0,64,4):

                s+=hexa2chara[''.join([str(a) for a in bin_plain_texts[i][j:j+4]])]

            plaintexts+=[s]
    plain()
    
    file = open("plain1.txt","w")
    for plaintext in plaintexts:
        file.write(plaintext+"\n")
    file.close()

    XOR_values = list((bin(0x0000080100100000))[2:].zfill(64))
    XOR_values = [int(x) for x in XOR_values]
    bin_plain_texts = []
    for i in range(2500):
        temp = np.random.choice(['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u'],size=(1,16),replace = True)[0]
        bin_input=[]
        for i in temp:
            bin_input.extend([int(a) for a in chara2hexa[i]])

        bin_plain_texts.append(bin_input)
        bin_plain_texts.append(list(np.bitwise_xor(bin_input,XOR_values)))

    plaintexts = []

    for i in range(len(bin_plain_texts)):
        s = ""
        for j in range(0,64,4):

            s+=hexa2chara[''.join([str(a) for a in bin_plain_texts[i][j:j+4]])]
        plaintexts+=[s]

    file = open("plain2.txt","w")
    for plaintext in plaintexts:
        file.write(plaintext+"\n")
    file.close()

main()
