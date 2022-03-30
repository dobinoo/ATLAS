#This is the input part of ATLAS
#The part of ATLAS that take care of input
#Here the voice input is compared with specific sequences and it should forward the input to the right part of program

import time                         #import for time use
import logging                      #import for future debug

logging_level = logging.DEBUG       #setting up logging level
#logging.basicConfig(filename = "debug/input.log", encoding = "utf-8", level = logging_level, format = "%(asctime)s %(message)s")     #logging config


#main wordlist for specific protocols############################################################################################################################
main_word_list = {"shut down" : ["shut down", "shutdown", "switch off", "turn off", "go to sleep", "good night", "goodbye", "good bye"],
				"wiki def" : ["tell me about", "who is", "what is", "define", "definition of", "who are", "what are", "short explanation"],
				"wiki summary" : ["tell me more", "continue", "go on", "tell me about"],
				"thanks" : ["thanks", "thank you"],
				"time" : ["what time is it", "what time it is", "the time"],
				"abusive" : ['dumb', 'suck', 'idiot', 'fuck', 'retard', 'asshole', 'fucker'],
				"no response" : ['wow', 'whoa', 'cool', 'okay', 'good', 'yes', 'wonderful', 'great', 'terrific', 'nice', 'oh', 'awesome', 'sounds good', 'fine', 'no problem', 'ok'],
				"how are you" : ['how are you', 'whats up', 'what\'s up', 'what is up', 'how do you feel', 'how are you feeling'],
				"hello" : ["hello", "hi", "high", 'good morning', 'good afternoon', 'good day', 'morning', 'ola'],
				"are you there" : ['are you on', 'you on', 'can you hear me', 'you there', 'are you there', 'are you listening', 'are you up'],
				"introduction" : ['introduce yourself', 'ATLAS', 'yourself'],
				"add to script" : ['add to script']}
#main wordlist for specific protocols############################################################################################################################


#Main function to call in core program to parse voice
def voice_input(voice_sentence):
	logging.debug("Voice_input function with this sentence: " + voice_sentence + "\n")
	voice_output = "You are asking wrong question\n"
	logging.info("Setting default voice_output: " + voice_output + "\n")

	parsed_sentence = sentence_parse(voice_sentence)
	keys_list = []

	#For every word in sentence search key words in dictionary
	for word in parsed_sentence:
		key = dictionary_search(word)
		if key != "":
			logging.debug("Printed key found in dictionary: " + key)
			keys_list.append(key)
			print (keys_list)
		else:
			logging.info("No key found or key is empty")
	#print(keys_list)

	# if voice_sentence == "ATLAS":
	# 	voice_output = "Another Technical Love of an Anonymous Stranger"
	# 	logging.debug("Returning voice_output: " + voice_output + "\n")

	return voice_output

#Function to parse sentence_parse
def sentence_parse(sentence):
	parsed_sentence = sentence.split()
	return parsed_sentence

#Function to search inside dictionaries
def dictionary_search(phrase):
	logging.debug("Entered function with this phrase:" + phrase + "\n")
	logging.info("Default key_name = '' ")
	key_name = ""

	#search function
	for key, value in main_word_list.items():
		for word in value:
			if word == phrase:
				key_name = key
				logging.debug("Found key:" + key_name)
				#print(key)

	return key_name

#dont forget to input wikipedia
#wikipedia protocol to get summary from wikipedia
def get_wiki_summary(string):
	logging.debug("Entered Atlas_input.py -> get_wiki_summary with: " + string)
	try:
		data = wikipedia.summary(string).lower()
		data = data.replace("i.e.", "i,e,").replace("e.g.", "e,g,").replace("jr.", "jr,").replace("sr.", "sr,").replace("lit.", "lit,")

		summary = ''
		data = data.split("\n")[0]

		for i, sentence in enumerate(data.split(".")[1:-1]):
			if i == 0:
				sentence = re.sub(r'\(.*\)', "", sentence)
			summary += sentence + "."

	except:
		summary = "I'm not sure what you mean. Could you be more specific?"
		logging.error("Problem within Altas_input.py -> get_wiki_summary")

	return(summary)

#dont forget to input wikipedia
#wikipedia protocol to get summary from wikipedia
def get_wiki_def(string):
	logging.debug("Entered Atlas_input.py -> get_wiki_def with: " + string)
	try:
		data = wikipedia.summary(string).lower()
		data = data.replace("i.e.", "i,e,").replace("e.g.", "e,g,").replace("jr.", "jr,").replace("sr.", "sr,").replace("lit.", "lit,")

		definition = data.split(".")[0]+"."
		definition = re.sub(r'\(.*\)', "", definition)

	except:
		definition = "I'm not sure what you mean. Could you be more specific?"
		logging.error("Problem within Altas_input.py -> get_wiki_def")

	return(definition)
