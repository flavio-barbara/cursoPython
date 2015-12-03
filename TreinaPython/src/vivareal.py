#!/bin/python

import sys

def  mystery( letter):
    for palin in letter:
        i = 0
        op = 0
        while i <= len(palin)-i-1:
            op += abs(ord(palin[i]) - ord(palin[-i-1]))
            i += 1
        print(op)


_letter_cnt = 0
_letter_cnt = int(raw_input())
_letter_i=0
_letter = []
while _letter_i < _letter_cnt:
    _letter_item = raw_input()
    print('leu')
    _letter.append(_letter_item)
    _letter_i+=1
print('end')
    

mystery(_letter);