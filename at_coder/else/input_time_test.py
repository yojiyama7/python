import sys
from sys import stdin
import os
import time

class OpeneeText:
	def __init__(self, text):
		self.text = text
	
	def readline(self):
		return self.text

	def on(self):
		sys.stdin = input_obj
	def off(self):
		sys.stdin = sys.__stdin__

# class OpeneeTexts:
# 	def __init__(self, texts, first_num=0):
# 		openee_text_obj = OpeneeText(texts[first_num])

RUN_COUNT = 10000
TEXT_LENGTH = 100

##################################
input_obj = OpeneeText("a"*TEXT_LENGTH)
input_obj.on()
#---------------------------------
start = time.time()

for i in range(RUN_COUNT):
	input()

input_time = time.time() - start
#---------------------------------
start = time.time()

for i in range(RUN_COUNT):
	sys.stdin.readline()

stdin_time = time.time() - start
#---------------------------------
input_obj.off()
##################################

print("             input(): {} sec".format(input_time))
print("sys.stdin.readline(): {} sec".format(stdin_time))
print("       input / stdin: {}".format(input_time / stdin_time))