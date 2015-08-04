# A bot to advertise MSAbroad
# Will go through /r/india as of now and whenever
# GRE, TOEFL, MS is mentioned it'll advertise the sub

import time
import praw
from collections import deque
import traceback
import datetime

def main():

	# Username, password and useragent
	USER = 'MSAbroadBot'
	PASS = 'imnoidiot5'
	USER_AGENT = 'Test Script by /u/kashre001'
	
	# Constants
	SLEEP_TIME = 30
	CACHE_SIZE = 200
	
	#Set up our cache and completed work set
	cache = deque(maxlen=CACHE_SIZE) # double-ended queue
	already_done = set()

	r = praw.Reddit(user_agent=USER_AGENT)
	r.login(USER, PASS, disable_warning=True)
	subreddit = r.get_subreddit('india')        
	#r.send_message('kashre001', 'Subject Line', 'You are awesome!')
	
	run = True
	while run:
		try:
			comments = subreddit.get_comments()
			#print('Looking at randia\n')
		
			#Check comments 
			for c in comments:				
				time.sleep(3)
				
				#Did we recently check it? If so fetch new comments
				if c.id in cache:
					break
				
				print c.body
				
				#Add this to our cache
				cache.append(c.id)
				
				#Check if we need to reply
				if check_comment(c.body):
					
					#Check if we already replied
					for reply in c.replies:
						if reply.author.name == USERNAME:
							already_done.add(c.id)
					
					if c.id not in already_done:						
						text = ''
						text = fetch_body(text)
						c.reply(text)
		
		except KeyboardInterrupt:
			run = False
		except Exception as e:
			now = datetime.datetime.now()
			print now.strftime("%m-%d-%Y %H:%M")
			print traceback.format_exc()
			print 'ERROR:', e
			print 'Going to sleep for 30 seconds...\n'
			time.sleep(SLEEP_TIME)
			continue


# If the comment has "GRE", "TOEFL", "IELTS" , "Masters" or "PhD"
# we need our bot to reply.						
def check_comment(text): 
	if ' gre ' in text.lower():
		return True
	if ' gre.' in text.lower():
		return True
	elif 'toefl' in text.lower():
		return True
	elif 'ielts' in text.lower():
		return True
	elif 'masters' in text.lower() :
		return True
	elif 'master\'s' in text.lower() :
		return True
	elif 'phd' in text.lower() :
		return True
	elif 'grad school' in text.lower() :
		return True
	elif 'graduate school' in text.lower() :
		return True
	elif 'higher education' in text.lower() :
		return True
	elif 'ms ' in text.lower() :
		return True	
	return False						


# Add a footer for the haters.	
def fetch_body(text):
	text += 'Hello there! Planning on doing a Master\'s abroad ? \n'
	text += 'Come join us at /r/MsAbroad! \n\n'
	text += 'We\'re here to help you out! :)\n'
	text += '------------------------------------------------------------------\n'
	text += 'I am just a BOT.\n\n'
	text += 'Please don\'t hate on me.\n\n'
	text += "PM /u/kashre001 if you have any issues ☜(⌒▽⌒)☞ \n\n"	
	return text
	
#call main function
main()	
	

