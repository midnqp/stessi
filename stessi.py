#!/usr/bin/python3
import time, os, sys, subprocess

""" ACCEPTING AND CAPTURING IMAGES FROM TEXT """
os.system("python3 -m updog -d . -p 8080 &")

while True:
	listAll = subprocess.getoutput("ls | grep -E 'png|jpg|jpeg'").split()
	
	if len(listAll) > 0:	
		count = 0 
		for eachImage in listAll:
			count += 1
			os.system("rm -f output{0}.txt".format(count))
			os.system("tesseract {0} {1}".format(eachImage, "output"+str(count)))
			os.system("rm -f " + eachImage)
			print(eachImage)
		sys.stdout.write("\033[0;34mAll images are processed!\033[0;0m\n")

		""" CONVERTING TEXT TO SPEECH """
		from gtts import gTTS
		for i in range(1, count+1):
			eachOutputFile = open("output{0}.txt".format(i), "r").read()
			os.system("rm -f output{0}.mp3".format(i))
			gTTS(text=eachOutputFile, lang='en-us', slow=False).save("output{0}.mp3".format(i))
		sys.stdout.write("\033[0;34mAll audio are ready!\033[0;0m\n")

	time.sleep(1)
