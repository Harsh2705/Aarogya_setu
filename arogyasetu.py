from PIL import Image
img=Image.open('arogya1.jpg')
img.show()
from pydub import AudioSegment
from pydub.playback import play





print('**************************   I SAFE','WE SAFE','INDIA SAFE   *************************** ')


def bluetooth(list):
	list=['ON','OFF']
	return list

def location(list):
	list=['ON','OFF']
	return list

def your_status(list):
	list=['helpline_number','self_access']
	return list

def question1(list):
	list=['khasi','bhukar','sas lene mai dikkat','none of the above']
	return list

def question2(list):
	list=['sugar','heart_problem','kidney_issue','none of the above']
	return list

def question3(list):
	list=['yes','no']
	return list

def question4(list):
	list=['yes','no']
	return list






print("for bluetooth press b \n")
print("for location  press l \n")
print("press s \n")
print("press q1 \n")
print("press q2 \n")
print("press q3 \n")
print("press q4 \n")
while True:
	choice=input("kya karenge aap ")
	if choice=='b':
		print("kya aapka bluetooth on hai ya off hai",bluetooth(list))
		n=input("select--- ")
		if n=='OFF':
			print("sorry you on the bluetooth \n")
			break

		elif n=='ON':
			print("welcome","ab aap press l karke location on kare \n")


		else:
			print("invalid")

	elif choice=='l':
		print("kya aapka location on hai ya off hai",location(list))
		n=input("select---")
		if n=='OFF':
			print("sorry you on the location \n")
			break

		elif n=='ON':
			print("welcome","ab aap aarogya_setu mai enter kar chuke hai apna staus dekne ke liye press kre s  ")
			img=Image.open('corona.jpg')
			img.show()
			song=AudioSegment.from_mp3('teri.mp3')
			play(song)

		else:
			print("invlaid operation")

	elif choice=='s':
	    print(" ***************** WELCOME TO AAROGYA_SETU APP **************",your_status(list))	
	    img=Image.open('arogya2.jpg')
	    img.show()
	  
	    n=input("select what you do -----")
	    if n=='helpline_number':
	    	print("NUMBER IS ---- 1075 \n")

	    elif n=='self_access':
	    	print(" *********** PLEASE GIVE CORRECT ANSWER ***** \n")
	    	print(" ************ ACCURATE ANSWER HELP US *********** \n")
	    	print("FOR ANSWERING THE OUESTION1 YOU PRESS THE q1")
	    	print(" GOT IT --")


	    else:
	    	print("invalid")


	elif choice=='q1':
		song=AudioSegment.from_mp3('modig.mp3')
		play(song)
		print("1.kya aapko in sare lakshan mai se koi 1 lakshan hai -----",question1(list))
		n=input("select-----")
		if n=='none of the above':
			print("OK")
			print("GO TO THE NEXT QUESTION PRESS q2")

		elif n=='khasi':
			print("OK")
			print("AAPKO THODI HI DER MAI 1 AMBULANCE LENE AAYEGI \n")
			img=Image.open('sad.jpg')
			img.show()
			song=AudioSegment.from_mp3('zindgi.mp3')
			play(song)

		elif n=='bhukar':
			print("OK")
			print("AAPKO THODI HI DER MAI 1 AMBULANCE LENE AAYEGI \n")
			img=Image.open('sad.jpg')
			img.show()
			song=AudioSegment.from_mp3('zindgi.mp3')
			play(song)

		elif n=='sas lene mai dikkat':
			print("OK")
			print("AAPKO THODI HI DER MAI 1 AMBULANCE LENE AAYEGI \n")
			img=Image.open('sad.jpg')
			img.show()
			song=AudioSegment.from_mp3('zindgi.mp3')
			play(song)


		else:
			print("nothing")

	elif choice=='q2':
		song=AudioSegment.from_mp3('modig.mp3')
		play(song)

		print("2.kya aapko in rogo  mai se koi bhi rog hua hai -----",question2(list))
		n=input("select-----")
		if n=='none of the above':
			print("OK")
			print("GO TO THE NEXT QUESTION PRESS q3")

		elif n=='sugar':
			print("OK")
			print("AAPKO THODI HI DER MAI 1 AMBULANCE LENE AAYEGI \n")
			img=Image.open('sad.jpg')
			img.show()
			song=AudioSegment.from_mp3('zindgi.mp3')
			play(song)

		elif n=='heart_problem':
			print("OK")
			print("AAPKO THODI HI DER MAI 1 AMBULANCE LENE AAYEGI \n")
			img=Image.open('sad.jpg')
			img.show()
			song=AudioSegment.from_mp3('zindgi.mp3')
			play(song)

		elif n=='kidney_issue':
			print("OK")
			print("AAPKO THODI HI DER MAI 1 AMBULANCE LENE AAYEGI \n")
			img=Image.open('sad.jpg')
			img.show()
			song=AudioSegment.from_mp3('zindgi.mp3')
			play(song)


		else:
			print("nothing")

	elif choice=='q3':
		song=AudioSegment.from_mp3('modig.mp3')
		play(song)
		print("3.kya aapne pichele 28-40 dino mai se koi videsh yatra ki hai -----",question3(list))
		n=input("select-----")
		if n=='no':
			print("OK")
			print("GO TO THE NEXT QUESTION PRESS q4")

		else:
			print("AAPKO THODI HI DER MAI 1 AMBULANCE LENE AAYEGI \n")
			img=Image.open('sad.jpg')
			img.show()
			song=AudioSegment.from_mp3('zindgi.mp3')
			play(song)


	elif choice=='q4':
		song=AudioSegment.from_mp3('modig.mp3')
		play(song)
		print("4.kya aap kisi corona positive man se mile hai-----",question4(list))
		n=input("select-----")
		if n=='no':
			print("OK")
			print(" CONGRATULATIONS AAP SURKSHIT HAI","AAGAR AAPKO KOI BHI PROBLEM AATI HAI TO AAP HMARE HELPLINE NUMBER PE PHONE KRE \n")
			print("  ************ DHANYAWAD ***************** \n")
			img=Image.open('aakshay.jpg')
			img.show()
			song=AudioSegment.from_mp3('saala.mp3')
			play(song)
			break

		else:
		    print("AAPKO THODI HI DER MAI 1 AMBULANCE LENE AAYEGI \n")
		    