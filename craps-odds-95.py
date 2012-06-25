#!/usr/bin/python -tt

import random
maxbet = 5

def dicer():
	dice1 = 0
	dice2 = 0
	while (dice1 == 0 or dice2 == 0): 
		dice1 = random.randint(0,6)
		dice2 = random.randint(0,6)
	return (dice1 + dice2)

def lineroll(roll):
	lineresult = 0
	linemoney = 0
	while (lineresult != roll):		
		lineresult = dicer()
		#print "lineresult", lineresult 
		
		if lineresult == 7:  # you loose 
			linemoney = linemoney + 0
			print "     you loose rolled a ", lineresult
			return linemoney

		elif lineresult == roll:            # you win 
			linemoney = linemoney + 25 
			print "     winner winner you rolled the point"
			return linemoney
	
		elif lineresult == 6 and roll == 8:
			linemoney = linemoney + 12 
			print "     winner 12 ", lineresult

		elif lineresult == 8 and roll == 6: 
			linemoney = linemoney + 12 
			print "      winner 12 ", lineresult

		elif lineresult == 5 and roll == 6: 
			linemoney = linemoney + 12 
			print "      winner 12 ", lineresult

		elif lineresult == 9 and roll == 8: 
			linemoney = linemoney + 12 
			print "      winner 12 ", lineresult


		else:				    # its some other number continue 
			linemoney = linemoney + 0			

def game():
	mypot = 100
	gohome = maxbet * 2 
	while (mypot > maxbet):
		# insert while here
		pointoutcome = 0
		passroll = dicer()

		if mypot <= gohome:
			return mypot
	
		if passroll == 7 or passroll == 11:
			mypot = mypot + maxbet	
			print "->you win first roll!", passroll
			#print "Money is", mypot
		elif passroll == 2 or passroll == 3 or passroll == 12:
			mypot = mypot - maxbet
			print "->you loose!", passroll
			#print "Money is", mypot
		else:
			print "->Setting Point to", passroll
			
			if passroll == 6 or passroll == 8: # make bet on 6 or 8
				mypot = mypot - 12 
								
			passbet = maxbet * 2 # win the pass bet
			mypot = mypot - maxbet

			lineResult = lineroll(passroll) # run the line bets

			if lineResult == 0:
				mypot = mypot - passbet
			else:
				pointoutcome = lineResult + passbet
			#print "line outcome ", lineResult

		mypot = mypot + pointoutcome
		print "				-->My pot is ", mypot	
		
		if mypot >= 200:
			return mypot
		
		if mypot <= gohome:
			return mypot

def main():
	losses = 0
	wins = 0
	games = 1000
	while (games != 0):
		winloose = game()
		
		if winloose >= 200:
			wins = wins + 1
		else:
			losses = losses + 1
		games = games - 1

	print "wins were ", wins
	print "losses  were ", losses

	



if __name__ == '__main__':
  main()
