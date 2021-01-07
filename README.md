Dependency packages for Unix-like systems:
- python3, ffmpeg, libleptonica-dev, liblept5, tesseract-ocr*

(*a large compiled tesseract-ocr binary is included in: ./tesseract/bin/)

Dependency modules for Python3 (using PIP):
- updog (GUI)
- gtts



Installing/Using:
GUI: 
- `./stessi.py`
- From a browser, access `localhost:8080`. Upload image files, and get 
	text & audio outputs.

CLI (not yet): 
- `python3 stessi.py [directory containing images to input]`



Extending language support:
- add .traineddata files in ./tesseract/share/tessdata/, 
	like: ben.traineddata



Support the Little Plans Ahead:
1. Friendly & Cordial GUI: Multi-language directories 
like - ben, eng, etc. You upload in them.
	- Remains hidden stessi.py by: ".stessi.py". Sudd-
	  enly one directory appears named 'text'. As gTTS
		makes audio, appears suddenly the 'audio' directory.
	- Somehow support multi-user in GUI. How's that poss-
		ible? 
2. Make CLI.
  - args: fileNames, lang
  - echo `file $fileName`; #if image fileTypes, proceed.
