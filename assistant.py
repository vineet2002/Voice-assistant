import subprocess
from bs4 import BeautifulSoup
import pyaudio as py
import wolframalpha
import pyttsx3
from datetime import datetime
import json
import pywhatkit
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from urllib.request import urlopen
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !")

	else:
		speak("Good Evening Sir !")

	assname =("Jarvis 1 point o")
	speak("I am your Assistant")
	
	

def username():
	speak("What should i call you sir")
	uname = takeCommand()
	speak("Welcome ")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	
	speak("How can i Help you, Sir")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"
	
	return query
def NewsFromBBC():
     
    # BBC news api
    # following query parameters are used
    # source, sortBy and apiKey
    query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "6a6322e17d13451fb2f0f02217c01490"
    }
    main_url = " https://newsapi.org/v1/articles"
 
    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
 
    # getting all articles in a string article
    article = open_bbc_page["articles"]
 
    # empty list which will
    # contain all trending news
    results = []
     
    for ar in article:
        results.append(ar["title"])
         
    for i in range(len(results)):
         
        # printing all trending news
        print(i + 1, results[i])
 
    #to read the news out loud for us
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(results)
    
def sendEmail(to, content):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	
	# Enable low security in gmail
	server.login('19311a0599@sreenidhi.edu.in', '19311A0599')
	server.sendmail('19311A0599@sreenidhi.edu.in', to, content)
	server.close()
if __name__ == '__main__':
	clear = lambda: os.system('cls')
	
	# This Function will clean any
	# command before execution of this python file
	clear()
	wishMe()
	username()
	
	while True:
		
		query = takeCommand().lower()
		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("According to Wikipedia")
			print(results)
			speak(results)
		
		elif 'news' in query:
			NewsFromBBC()
		elif 'open youtube' in query:
			speak("Here you go to Youtube\n")
			webbrowser.open("youtube.com")

		elif 'open google' in query:
			speak("Here you go to Google\n")
			webbrowser.open("google.com")

		elif 'open stack overflow' in query:
			speak("Here you go to Stack Over flow.Happy coding")
			webbrowser.open("stackoverflow.com")

		#elif 'play music' in query or "play song" in query:
			#speak("Here you go with music")
			#p=vlc.MediaPlayer("C:\Users\vineetjoshi\Downloads\ACDC - Shoot To Thrill (Iron Man 2 Version).mp3")
			#p.play()
   			# music_dir = "G:\\Song"
			#music_dir = "D:\\music\\"
			#songs = os.listdir(music_dir)
			#print(songs)
			#random = os.startfile(os.path.join(music_dir, songs[0]))

		elif 'the time' in query:
			strTime = datetime.datetime.now()#.strftime("% H:% M:% S")
			speak(f"Sir, the time is {strTime}")

		

		elif 'email ' in query:
			try:
				speak("What should I say?")
				content = takeCommand()
				to = "19311a0593@sreenidhi.edu.in"
				sendEmail(to, content)
				speak("Email has been sent !")
			except Exception as e:
				print(e)
				speak("I am not able to send this email")

		elif 'send a mail' in query:
			try:
				speak("What should I say?")
				content = takeCommand()
				speak("whome should i send")
				to = input()
				sendEmail(to, content)
				speak("Email has been sent !")
			except Exception as e:
				print(e)
				speak("I am not able to send this email")

		elif 'how are you' in query:
			speak("I am fine, Thank you")
			speak("How are you, Sir")

		elif 'fine' in query or "good" in query:
			speak("It's good to know that your fine")

		elif "change my name to" in query:
			query = query.replace("change my name to", "")
			assname = query

		elif "change name" in query:
			speak("What would you like to call me, Sir ")
			assname = takeCommand()
			speak("Thanks for naming me")

		elif "what's your name" in query or "What is your name" in query:
			speak("My friends call me")
			speak(assname)
			print("My friends call me", assname)

		elif 'exit' in query:
			speak("Thanks for giving me your time")
			exit()

		elif "who made you" in query or "who created you" in query:
			speak("I have been created by Vineet.")
			
		elif 'joke' in query:
			speak(pyjokes.get_joke())
			
		elif "calculate" in query:
			
			app_id = "J6U9AT-TJUEGW8X78"
			client = wolframalpha.Client(app_id)
			indx = query.lower().split().index('calculate')
			query = query.split()[indx + 1:]
			res = client.query(' '.join(query))
			answer = next(res.results).text
			print("The answer is " + answer)
			speak("The answer is " + answer)

		elif 'search' in query or 'play' in query:
			
			query = query.replace("search", "")
			query = query.replace("play", "")		
			webbrowser.open(query)

		elif "who i am" in query:
			speak("If you talk then definitely your human.")

		elif "why you came to world" in query:
			speak("Thanks to vineet. further It's a secret")

		elif 'power point presentation' in query:
			speak("opening Power Point presentation")
			power = r"F:\\8 sem\\JARVIS Voice Recognition using Machine Learning.pptx"
			os.startfile(power)

		elif 'is love' in query:
			speak("It is 7th sense that destroy all other senses")

		elif "who are you" in query:
			speak("I am your virtual assistant created by vineet")

		elif 'reason for you' in query:
			speak("I was created as a Major project by Vineet ")

		elif 'change background' in query:
			ctypes.windll.user32.SystemParametersInfoW(20,
													0,
													"C://Users//vineetjoshi//Pictures//Screenshots//",
													0)
			speak("Background changed successfully")

		

		#elif 'news' in query:
			
		#	try:
		#		jsonObj = urlopen("https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey = 6a6322e17d13451fb2f0f02217c01490")
		#		data = json.load(jsonObj)
		#		i = 1
				
		#		speak('here are some top news from the times of india')
		#		print('''=============== TIMES OF INDIA ============'''+ '\n')
				
		#		for item in data['articles']:
					
		#			print(str(i) + '. ' + item['title'] + '\n')
		#			print(item['description'] + '\n')
		##			speak(str(i) + '. ' + item['title'] + '\n')
		#			i += 1
		#	except Exception as e:
				
		#		print(str(e))

		
		elif 'lock window' in query:
				speak("locking the device")
				ctypes.windll.user32.LockWorkStation()

		elif 'shutdown system' in query:
				speak("Hold On a Sec ! Your system is on its way to shut down")
				subprocess.call('shutdown / p /f')
				
		elif 'empty recycle bin' in query:
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
			speak("Recycle Bin Recycled")

		elif "don't listen" in query or "stop listening" in query:
			speak("for how much time you want to stop jarvis from listening commands")
			a = int(takeCommand())
			time.sleep(a)
			print(a)

		elif "where is" in query:
			query = query.replace("where is", "")
			location = query
			speak("User asked to Locate")
			speak(location)
			webbrowser.open("https://www.google.nl / maps / place/" + location + "")

		elif "camera" in query or "take a photo" in query:
			ec.capture(0, "Jarvis Camera ", "img.jpg")

		elif "restart" in query:
			subprocess.call(["shutdown", "/r"])
			
		elif "hibernate" in query or "sleep" in query:
			speak("Hibernating")
			subprocess.call("shutdown / h")

		elif "log off" in query or "sign out" in query:
			speak("Make sure all the application are closed before sign-out")
			time.sleep(5)
			subprocess.call(["shutdown", "/l"])

		elif "write a note" in query:
			speak("What should i write, sir")
			note = takeCommand()
			file = open('jarvis.txt', 'w')
			speak("Sir, Should i include date and time")
			snfm = takeCommand()
			if 'yes' in snfm or 'sure' in snfm:
				strTime = datetime.datetime.now().strftime("% H:% M:% S")
				file.write(strTime)
				file.write(" :- ")
				file.write(note)
			else:
				file.write(note)
		
		elif "show note" in query:
			speak("Showing Notes")
			file = open("jarvis.txt", "r")
			print(file.read())
			speak(file.read(6))

					
		# NPPR9-FWDCX-D2C8J-H872K-2YT43
		elif "jarvis" in query:
			
			wishMe()
			speak("Jarvis 1 point o in your service Mister")
			speak(assname)			

		elif "wikipedia" in query:
			webbrowser.open("wikipedia.com")

		elif "Good Morning" in query:
			speak("A warm" +query)
			speak("How are you Mister")
			speak(assname)
		elif "whatsapp message" in query:
			speak("please enter the number want to send message")
			number=(input('enter the phone number: '))
			speak("enter the message you want to send")
			message=input("enter the message: ")
			pywhatkit.sendwhatmsg(number,message,datetime.now().hour, datetime.now().minute+1)

		# most asked question from google Assistant
		elif "will you be my gf" in query or "will you be my bf" in query:
			speak("I'm not sure about, may be you should give me some time")

		elif "how are you" in query:
			speak("I'm fine, glad you me that")
		elif "weather" in query:
			headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
			def weather(city):
				city = city.replace(" ", "+")
				res = requests.get(
				f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
				print("Searching...\n")
				soup = BeautifulSoup(res.text, 'html.parser')
				location = soup.select('#wob_loc')[0].getText().strip()
				time = soup.select('#wob_dts')[0].getText().strip()
				info = soup.select('#wob_dc')[0].getText().strip()
				weather = soup.select('#wob_tm')[0].getText().strip()
				print(location)
				print(time)
				print(info)
				print(weather+"°C")
				city = input("Enter the Name of City -> ")
				city = city+" weather"
				weather(city)
				print("Have a Nice Day:)")

		elif "i love you" in query:
			speak("It's hard to understand")

		elif "what is" in query or "who is" in query:
			
			# Use the same API key
			# that we have generated earlier
			client = wolframalpha.Client("J6U9AT-TJUEGW8X78")
			res = client.query(query)
			
			try:
				print (next(res.results).text)
				speak (next(res.results).text)
			except StopIteration:
				print ("No results")

