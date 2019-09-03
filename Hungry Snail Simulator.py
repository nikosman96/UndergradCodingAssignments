#SnailSimulator
import sys,time,random

#Slow typewriter effect
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

welcome_msg = 'Welcome to Snail Simulator 2017!'

snail = """
    .----.   @   @
   / .-"-.`.  \ /
   | | '\ \ \_/ )
 ,-\ `-.' /.'  /
'---`----'----'
"""

time.sleep(0.5)
print welcome_msg
time.sleep(1)

print ('')

print_slow('Initiating Artificial Snail Intelligence...')
time.sleep(0.5)

print ('')

print_slow('Gathering shell scripts...')
time.sleep(0.5)

print ('')

print_slow('Creating George Kemenes Interface...')
time.sleep(0.5)

print ('')

#for timer
import time

#first while loop
while True:

#question
	print_slow(snail)
	time.sleep(0.5)
	print ('Hello, my name is Snail.')
	time.sleep(2)
	print ('Who are you?')
#User interacts and answers with their name
	user_name = raw_input('Name: ')
	print ('')
#Bonus message for Laurence
	if user_name == 'Laurence' or user_name == 'laurence':
		time.sleep(0.5)
		print user_name,'?'
		time.sleep(2)
		print 'THE',user_name,'Pearl?'
		time.sleep(2)
		print 'The wonderful and brilliant herb enthusiast?'
		time.sleep(2)
		print 'It is such an honour to finally meet you.'
	else :
		time.sleep(0.5)
		print user_name, '?'
		time.sleep(2)
		print 'Yes... That sounds right.'
		time.sleep(2)
		print 'A highly evolved and intelligent organism like yourself deserves a name like '+user_name+'.'
	break
#so that snail only eats when it's hungry
fed = False
#second while loop
while not fed:
	time.sleep(2)
	print ('')
	print 'So', user_name,'what have you brought for me today?'
	food = raw_input('Food: ')
#only two possible answers which must not be case sensitive
# First option
	if food == 'Cabbage' or food == 'cabbage':
         fed = True
         start = time.time()
         print '\n'+'Mhmmmm... This heaven of green... The crunch!\nEating cabbagetakes me back to when I was a wee little snail and Grandma Aplysia would make us cabbage soup.'
# Second option
	elif food == 'Lettuce' or food == 'lettuce':
         fed = True
         start = time.time()
         print '\n'+'Mhmmmm... Simply exquisite...\nLettuce dig into this royal feast you have prepared for me ha ha ha.'

# Quick exit shortcut
	elif food == 'q':
  		break
# Anything else
	else :
 		print '\n'+'WHAT???? Get that AWAY from me.',user_name,'!!!! I thought I could trust you.'
	time.sleep(5)
# Third loop allowing time for digestion
while True:
    print '\n'+'Got anything else for me, ' +user_name+'?'
    food = raw_input('Enter Food or Type No to exit: ')
# Time.time function assigned to end
    end = time.time()
# Start assigned after each feeding so that the actual time passed can be calculated
    time_passed = end - start
# If less than 10 seconds pass the snail will not be hungry and will not eat
    if time_passed < 10:
        if food == 'Cabbage' or food == 'Lettuce' or food == 'cabbage' or food == 'lettuce':
            print '\n'+'Wow!',user_name,'... I just ate. Give me a few seconds to digest.'
        else:
            print '\n'+'WHAT???? Get that AWAY from me.',user_name,'!!!! I thought I could trust you.'
	time.sleep(5)

# If more than 10 seconds have passed the snail will eat
    elif time_passed >= 10:
        if food == 'Cabbage' or food == 'cabbage':
            start = time.time()
            print '\n'+'Mhmmmm... This heaven of green... The crunch!\nEating cabbage takes me back to when I was a wee little snail and Grandma Aplysia would make us cabbage soup.'
        elif food == 'Lettuce' or food == 'lettuce':
            start = time.time()
            print '\n'+'Mhmmmm... Simply exquisite...\nLettuce dig into this royal feast you have prepared for me ha ha ha.'
        else:
            print '\n'+'WHAT???? Get that AWAY from me.',user_name,'!!!! I thought I could trust you.'
	time.sleep(5)
end = time.time()
time_passed = end - start
