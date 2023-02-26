def arb():
	odd1 = float(input('Input 1st Odd: '))
	odd2 = float(input('\nINPUT 2nd Odd: '))
	consider = ((1/odd1) + (1/odd2))*100
	if consider >= 100:
		print('\nNot an Arbitrage bet, You will make a loss!')
	else:
		print('\nGreat you found an Arb bet!')
		amount = int(input('\nINPUT AMOUNT: '))
		def oddA(odd1,odd2,amount):
			return round(((odd1/(odd1+odd2))*amount),2)
		def oddB(odd1,odd2,amount):
			return round(((odd2/(odd2+odd1))*amount),2) 
		stake1 = oddA(odd1,odd2,amount)
		stake2 = oddB(odd1,odd2,amount)
		w,w2= round((stake2 * odd1),2), round((stake1 * odd2),2) 
		p,p2 = round(abs(amount - w),2), round(abs(amount - w2),2)
	print('\nODD :- {}\n Stake : {}\n Winnings : {}\n Profit : {}\n\nODD :- {}\n Stake : {}\n Winnings : {}\n Profit : {}\n'.
	format(odd1,stake2,w,p,odd2,stake1,w2,p2))
	def restart():
		l = input('Type `restart` to restart calculator or `exit` to quit: ').lower()
		if l == 'restart':
			arb()
		elif l == 'exit':
			exit
		else:
			print('\nIncorrect command, Try again\n')
			restart()
	restart()
arb()



