import time

############################################

pi = 3.1415926535897932384626433
 
############################################

def sqrt(a):
    strA = ""
    
    if type(a) == int:
        if not(len(str(a)) % 2 == 0):
            strA += "0"
    elif type(a) == float:
        index = 0
        
        while index < len(str(a)):
            if str(a)[index] == ".":
                if not((index-1) % 2 == 1):
                    strA += "0"
                break
            index += 1
                
    aN = len(strA)
                    
    

    index = len(strA)
    
  
    while index < aN + len(str(a)):
        if str(a)[index-aN] == ".":
            pass
        else:
            strA += str(a)[index-aN]
        index += 1
    
    if type(a) == float:
        index = 0
        
        while index < len(str(a)):
            if str(a)[index] == ".":
                aN = len(strA) / 2 - 1
            index += 1
    
    index = 0
    
    while index < 50 - (len(str(a)) - aN):
        strA += "0"
        index += 1
        
    rVal = ""
    
    index = 1
    
    val_0 = ""
    val_1 = "0"
    val_2 = 0
    
    while index < len(strA) * 2:
    
    
        if index > 1:
            val_0 = str(int(val_0) - val_2)
    
        val_0 += strA[index-1:index+1]
        
        index_1 = 0
        
        while int(val_1 + str(index_1)) * index_1 <= int(val_0):
            index_1 += 1
        
        #while (int(val_1) * 10 + index_1) * index_1 < int(val_0):
         #   index_1 += 1
        
        index_1 -= 1
        
        rVal += str(index_1)[len(str(index_1)) - 1]
        
        val_2 = int(val_1 + str(index_1)) * index_1
        
        val_1 = str(2*int(rVal))
        
        index += 2
    
    index = 0
    
    rValPrime = ""
    
    while index < len(strA):
        if index == aN:
            rValPrime += "."
        rValPrime += rVal[index]
        index += 1
    
    return float(rValPrime)
    
    
###########################################

def atan(a):
    rVal = 0
    
    if a <= 1:
        index = 0
    
        while index < 50:
            rVal += float(pow(-1,index) * pow(a,2*index + 1))/float(2*index + 1)
            index += 1
    else:
        rVal = 9
        rVal = 7 + ((16*pow(a,2))/rVal)
        rVal = 5 + ((9*pow(a,2))/rVal)
        rVal = 3 + ((4*pow(a,2))/rVal)
        rVal = 1 + ((pow(a,2))/rVal)
        rVal = a / rVal
    
    return rVal
    
###########################################

def dice(sides):
	
	digits = []
	
	index = 0
	
	while index < len(str(sides)):
		seed = str(int(time.clock()*1000000))
		digits.append(int(str(seed)[len(seed)-1]))
		index += 1
		
	index = 0
	
	rVal = 0
	
	while index < len(digits):
		rVal += int(digits[index] * pow(10,len(digits) - (1+index)))
		index += 1

	rVal = int(rVal % sides)

	try:
		return rVal
	except:
		return -1
		
###########################################

def factorialm(a):
    rVal = 1
    
    index = 0
    
    while index <= a:
        rVal *= rVal
        if index == 2:
            rVal += 1
        index += 1
        
    return rVal
    
def factorial(a):
    rVal = 1
    
    index = 0
    
    while index <= a:
        rVal *= index
        if index == 1:
            rVal += 1
        index += 1
        
    return rVal

###########################################

def pforce(M, bravo_1, bravo_0, v):

	n = 1000
	
	i_1 = (pow(n,2) + n)/2
	i_2 = (2*pow(n,3) + 3*pow(n,2) + n)/6
	
	alpha = [0,0,0,0,0,0,0,0,0,0]

	alpha[0] = pow(bravo_0,2)*pow(bravo_1,2)
	alpha[1] = 2 * pow(bravo_0,3) * bravo_1
	alpha[2] = 3 * pow(bravo_0,2) * bravo_1 * i_1
	alpha[3] = bravo_0*pow(bravo_1,2) * i_1
	alpha[4] = pow(bravo_1,2) * i_2
	alpha[5] = pow(bravo_0,4)
	alpha[6] = 2 * pow(bravo_0,3) * i_1
	alpha[7] = pow(bravo_0,2) * bravo_1 * i_1
	alpha[8] = bravo_0 * bravo_1 * i_2
	alpha[9] = pow(bravo_0,2) * i_2

	sierra_1 = alpha[0] - alpha[1] - alpha[2] + alpha[3] + alpha[4] + alpha[5] + alpha[6] -alpha[7] - alpha[8] - alpha[9]
	
	F = ((float(v)/float(10)) * sierra_1 * (bravo_1 - bravo_0))/pow(n,3)
			
	F = F * M
	
	return F

def pforce_1(M, bravo_0, bravo_1, v):

    m = pow(sqrt(v) + (bravo_1 - bravo_0),2)
    
    m *= M

    return m

def mforce(M, bravo_0, bravo_1, v, n):

    i_1 = (pow(n,2) + n) / 2
    i_2 = (2*pow(n,3) + 3*pow(n,2) + n)/6
    
    delta = bravo_1 - bravo_0
    
    m = 0
    m_1 = 0
    
    alpha_0 = 1.0
    alpha_1 = v
    
    index = 0
    
    while index < n:
            
        if index == 1:
            alpha_0 = float((pow(sqrt(v) + delta,2)/float(bravo_0)) - float(v)) / float(delta)
            
            alpha_1 = delta * alpha_0
            
        if index > 1:
            alpha_1 = (pow(delta,index) * alpha_0) / factorial(index)
            
            alpha_0 /= float(bravo_0)
            
            #print alpha_1
            
        m += alpha_1
    
        index += 1
        
    index = 0
    
    alpha_0 = 1.0
    alpha_1 = v
    
    while index < n:
        if index == 1:
            alpha_0 = float((pow(sqrt(v) + delta,2)/float(bravo_0)) - float(v)) / float(delta)
            
            alpha_1 = delta * alpha_0
            
        if index > 1:
            alpha_1 = (pow(delta,index) * alpha_0) / factorialm(index)
            
            alpha_0 /= float(bravo_0)
            
        m_1 += alpha_1
        
        index += 1
        
    m = (m+m_1)/2
            
    
    #m *= 0.9742483472
    
    #m_2 = m*m
    
    #m = m_2 + float(m)/pi - float(1)/pow(2*pi*i_1,2)
    #m = (m_2 - 4*2*pi*i_2 + 4*m*pi*i_2)
    
    #m *= float(1)/float(pow(10,4))
    
    #m *= M
    
    return m
		
###########################################


def mx(array):

	i0 = 0
	i1 = 1
	
	arrayVal = array[i0]
	
	while i1 < len(array):
		
		if arrayVal < array[i1]:
			arrayVal = array[i1]
		
		i0 += 1
		i1 += 1
		
	return arrayVal
    
def mn(array):

	i0 = 0
	i1 = 1
	
	arrayVal = array[i0]
	
	while i1 < len(array):
		
		if arrayVal > array[i1]:
			arrayVal = array[i1]
		
		i0 += 1
		i1 += 1
		
	return arrayVal
	
	
###########################################

def cardIndex(deck):
	
	roll = dice(len(deck))
						
	return roll

###########################################


def cardV(array, seed):
	
	return array[seed].velocity
	
def cardHealth(array, seed):

	return array[seed].health
	
def cardPhysics(array, seed):
	
	return array[seed].physics
	
def cardMagic(array, seed):

	return array[seed].magic
	
def cardDescription(array, seed):

	return array[seed].description

###########################################

		
class card0:
	velocity = 15
	health = 2
	physics = 4
	magic = 2
	description = "orion"
	
class card1:
	velocity = 17
	health = 3
	physics = 2
	magic = 4
	description = "capricorn"
	
class card2:
	velocity = 0
	health = 7
	physics = 5
	magic = 5
	description = "firewall"
	
class card3:
	velocity = 11
	health = 1
	physics = 7
	magic = 1
	description = "rigel"
	
class card4:
	velocity = 12
	health = 1
	physics = 7
	magic = 7
	description = "artemis"
	
class card5:
	velocity = 15
	health = 5
	physics = 9
	magic = 5
	description = "leo"
	
class card6:
	velocity = 19
	health = 2
	physics = 5
	magic = 9
	description = "pegasus"
	
###########################################

class adversary:
	mass = 1
	magic = 1
	
class operator:
	mass = 1
	magic = 1

###########################################


adversaryDeck = [card0, card0, card0, card2, card2, card3, card3, card3, card5, card5, card6]

playerDeck = [card0, card0, card5, card5, card5, card5, card4, card4, card4, card3, card4]


###########################################

def cards(playerDeck, adversaryDeck, adversary):
	
	
	i = 1
	
	adversaryHealth = 9999
	
	playerHealth = 9999
	
	adversaryLen = len(adversaryDeck)
	playerLen = len(playerDeck)
	if len(playerDeck) > 9:
		while len(playerDeck) > 9:
			playerDeck.pop(dice(len(playerDeck)-1))
	
	i0 = 0
	
	i1 = 0
	
	aDeck = []
	
	pDeck = []
	
	while i0 < len(adversaryDeck):
		aDeck.append(adversaryDeck[i0])
		
		i0 += 1
	
	while i1 < len(playerDeck):
		pDeck.append(playerDeck[i1])
		
		i1 += 1
	
	
	while i < len(pDeck) and i < len(aDeck):
	
		operatorDamage = 0
		
		adversaryDamage = 0
			
		adversaryIndex0 = cardIndex(aDeck)
		
		a = 0
		while a < 1000:
			dice(25) - dice(25)
			a += 1
			
		adversaryIndex1 = cardIndex(aDeck)
		
		ap0 = cardV(aDeck, adversaryIndex0)
		
		ap1 = cardV(aDeck, adversaryIndex1)
		
		ah0 = cardHealth(aDeck, adversaryIndex0)
		
		ah1 = cardHealth(aDeck, adversaryIndex1)
		
		aphy0 = cardPhysics(aDeck, adversaryIndex0)
		
		aphy1 = cardPhysics(aDeck, adversaryIndex1)
		
		amag0 = cardMagic(aDeck, adversaryIndex0)
		
		amag1 = cardMagic(aDeck, adversaryIndex1)
		
		ad0 = cardDescription(aDeck, adversaryIndex0)
		
		ad1 = cardDescription(aDeck, adversaryIndex1)
		
		A = [[ap0, ap1], [ah0, ah1], [ad0, ad1], [aphy0,aphy1],[amag0,amag1]]
		
		aT_0 = 1+dice(4)
		aT_1 = 5 + dice(10)
        
		cT_0 = 1+dice(9)
		cT_1 = 1+dice(9)
		
		print "\n####################################################################################"
		
		print "%s TIME FRAME = [%i %i]" % (adversary,aT_0,aT_1)
		
		print "%s CARDS:\t%s (v%i,h%i|phy%i,magic%i)\t%s (v%i,h%i|phy%i,magic%i)" % (adversary,ad0,ap0,ah0,aphy0,amag0,ad1,ap1,ah1,aphy1,amag1)
		print ""
		print "%s COORDINATES: %i,%i" % (adversary,cT_0,cT_1)
		print ""
		print "%s HEALTH: %i" % (adversary,adversaryHealth)
		print "OPERATOR HEALTH: %i" % playerHealth
		print ""
		
		
		bool = 1
		
		oD = []
		
		index = 0
		
		print "operator deck:"
		
		while index < len(pDeck):
			oD.append("(" + str(index + 1) + ") " + cardDescription(pDeck, index) + " (" + str(cardV(pDeck, index)) + "," + str(cardHealth(pDeck, index)) + "|" + str(cardPhysics(pDeck, index)) + "," + str(cardMagic(pDeck, index)) + ")")
			
			print oD[index]
			
			index += 1
			

		print ""
		print "choose first card"
		
		playerIndex0 = 0
		playerIndex1 = 1
		
		while bool == 1:
			playerIndex0 = input() - 1
			
			try:
				int(playerIndex0)
			except:
				bool = 1
			else:
				bool = 0

				
		print "choose second card"
		
		bool = 1
        
		while bool == 1:
			try:
				playerIndex1 = input() - 1
				int(playerIndex1)
				bool = 0
			except:
				bool = 1
        
		opAngle = 0
                
        
        
		
		pp0 = cardV(pDeck, playerIndex0)
		
		pp1 = cardV(pDeck, playerIndex1)
		
		ph0 = cardHealth(pDeck, playerIndex0)
		
		ph1 = cardHealth(pDeck, playerIndex1)
		
		pphy0 = cardPhysics(pDeck, playerIndex0)
		
		pphy1 = cardPhysics(pDeck, playerIndex1)
		
		pmag0 = cardMagic(pDeck, playerIndex0)
		
		pmag1 = cardMagic(pDeck, playerIndex1)
		
		pd0 = cardDescription(pDeck, playerIndex0)
		
		pd1 = cardDescription(pDeck, playerIndex1)
		
		P = [[pp0, pp1], [ph0, ph1], [pd0, pd1], [pphy0,pphy1],[pmag0,pmag1]]
		
		T_0 = 1+dice(4)
		T_1 = 5 + dice(10)
		
		

		print "TIME FRAME = [%i %i]" % (T_0,T_1)
		print "OPERATOR CARDS:\t%s (v%i,h%i|phy%i,magic%i)\t%s (v%i,h%i|phy%i,magic%i)" % (pd0,pp0,ph0,pphy0,pmag0,pd1,pp1,ph1,pphy1,pmag1)
		
		adChoice0 = 0
		adChoice1 = 0
		cardChoice = 0
		
		print ""
		print "New Timeframe? yes(1) no(2)"
		
		bool = 1
        
		while bool == 1:
			try:
				playerInput = input()
				int(playerInput)
				if (playerInput == 1 or playerInput == 2) == True:
					bool = 0
				else:
					bool = 1
			except:
				bool = 1
		
		if playerInput == 1:
			T_0 = 1+dice(4)
			T_1 = 5 + dice(10)
			
			if T_1 < T_0:
				q = T_0
				T_1 = T_0
				T_0 = q
			
			print "New Timeframe = [%i %i]" % (T_0,T_1)
		else:
			print "Timeframe Static"
		
		if (aT_1 - aT_0) / (T_1 - T_0) == 0:
			aT_0 = 1+dice(4)
			aT_1 = 5 + dice(10)
			print "New %s Timeframe = [%i %i]" % (adversary,aT_0,aT_1)
		else:
			print "%s Timeframe Static" % adversary
            
            		bool = 1
        
		print ""
		print "operator angle (rad):"
        
		bool = 1
        
		while bool == 1:
			try:
				opAngle = input()
				float(playerInput)
				bool = 0
			except:
				bool = 1
        
		
		print ""
		print "which card will you draw first? "
		
		while cardChoice == 0:
			playerInput = input()
		
			for descriptions in P[2]:
				cardChoice += 1
			
				if descriptions == playerInput - 1:
					break
				
		PM = 0
		
		while PM == 0:
			print "physical (1) or magical (2)?"
		
			bravo = 1
        
			while bravo == 1:
				try:
					playerInput = input()
					int(playerInput)
					if (playerInput == 1 or playerInput == 2) == True:
						bravo = 0
					else:
						bravo = 1
				except:
					bravo = 1
			
			if playerInput == 1:
			
				PM = 1
				
			elif playerInput == 2:
				
				PM = 2
		
		i1 = 1
        
		adChoice0 = 0
		adChoice1 = 0
        
		adC = [adChoice0,adChoice1]
        
		adChoiceM = 0
		adChoiceP = 0
        
		aSeed = 0
        
		if mx(A[1]) == A[1][1]:
			aSeed = 1
        
		aMVal = mforce(A[4][aSeed], aT_0,aT_1, A[0][aSeed])
		aVFal = mforce(A[4][aSeed], aT_0,aT_1, A[1][aSeed])
		aPVal = pforce(A[3][aSeed], aT_0,aT_1, A[0][aSeed])
		aPFVal = pforce(A[3][aSeed], aT_0,aT_1, A[1][aSeed])
        
		aV = [aMVal,aPVal]
		aVF = [aVFal,aPFVal]
        
		if aMVal > aPVal:
			adChoiceM += float(10)
		else:
			adChoiceP += float(10)
        
		pSeed0 = 0
        
		if mx(P[1]) == 1:
			pSeed0 = 1
        
		playerPVal0 = pforce(P[3][pSeed0], T_0,T_1, P[1][pSeed0])
        
		playerMVal0 = mforce(P[4][pSeed0], T_0,T_1, P[1][pSeed0])
        
		pMV0 = [playerPVal0,playerMVal0]
        
		if mx(aV) == aMVal:
			if mx(aV) - mx(pMV0) < 0:
				
				adChoiceP += float(10)
			
			elif mx(aV) - mx(pMV0) > 0:
				
				adChoiceM += float(10)
			if mx(aV) - mx(pMV0) > 10:
				
				adChoiceM += float(10)
                
		elif mx(aV) == aPVal:
			if mx(aV) - mx(pMV0) < 0:
				adChoiceM += float(10)
			elif mx(aV) - mx(pMV0) > 0:
				adChoiceM += float(10)
			if mx(aV) - mx(pMV0) > 10:
				adChoiceP += float(10)    

		pSeed1 = 0
        
		if mx(P[1]) == 1:
			pSeed1 = 1
        
		playerPVal1 = pforce(P[3][pSeed1], T_0,T_1, P[0][pSeed1])
        
		playerMVal1 = mforce(P[4][pSeed1], T_0,T_1, P[0][pSeed1])
        
		pMV1 = [playerPVal1,playerMVal1]
        
		if playerPVal1 - mx(aVF) < 0:
			if mx(aVF) == aVFal:
				adChoiceP -= 10
            
		if playerMVal1 - mx(aVF) < 0:
			if mx(aVF) == aVFal:
				adChoiceM -= 10
                
		if adChoiceP > adChoiceM:
			AM = 0
			print "%s played physical" % adversary
			if mx(pMV0) - mx(aVF) < 0:
				adC[(aSeed - 1)%2] += 10
			else:
				adC[aSeed] += 10
            
		elif adChoiceM > adChoiceP:
			AM = 1
			print "%s played magic" % adversary
			if mx(pMV0) - mx(aVF) < 0:
				adC[(aSeed - 1)%2] += 10
			else:
				adC[aSeed] += 10
            
		elif adChoiceP == adChoiceM:
			AM = dice(2)        
			adChoice = dice(2)
            
		adChoice0 *= float(dice(2))/float(2)
		adChoice1 *= float(dice(2))/float(2)
		adChoice = 0
        
		if adChoice0 > adChoice1:
			adChoice = 0
		elif adChoice1 > adChoice0:
			adChoice = 1
		elif adChoice0 == adChoice1:
			adChoice = dice(2)
            

			
		operatorDamage = 1
		opFort = 1
		adversaryDamage = 1
		aFort = 1
        
		if PM == 1: 
			operatorDamage = pforce(P[3][cardChoice - 1], T_0,T_1, P[0][cardChoice - 1])
			opFort = mforce(P[3][cardChoice%2],T_0,T_1,P[1][cardChoice%2])
		elif PM == 2:
			operatorDamage = mforce(P[4][cardChoice - 1], T_0,T_1, P[0][cardChoice - 1])
			opFort = pforce(P[4][cardChoice%2],T_0,T_1,P[1][cardChoice%2])
        
		if AM == 0:
			adversaryDamage = pforce(A[3][adChoice], aT_0,aT_1, A[0][adChoice])
			aFort = mforce(A[3][(adChoice+1)%2],aT_0,aT_1,A[1][(adChoice+1)%2])
		if AM == 1:
			adversaryDamage = mforce(A[4][adChoice], aT_0,aT_1, A[0][adChoice])
			aFort = pforce(A[4][(adChoice+1)%2],aT_0,aT_1,A[1][(adChoice+1)%2])
            
		if operatorDamage > 9999:
			operatorDamage = 9999
		if opFort > 9999:
			opFort = 9999
		if adversaryDamage > 9999:
			adversaryDamage = 9999;
		if aFort > 9999:
			aFort = 9999
    
		ratio = float(opAngle) / float(atan(float(cT_0)/float(cT_1)))
        
		if ratio == 1:
			pass
		else:
			if ratio > 1:
				ratio = float(1) / ratio
			elif ratio < 1:
				pass
        
		print "angular scale: " + str(ratio)
        
		if ratio > 0.666 and ratio < 0.667:
			print "evil is no good"
		if (ratio > 0.777 and ratio < 0.778) or (ratio > 0.999 and ratio < 1):
			print "perfect"
        
		operatorDamage *= ratio
        
		print "operator played %s first" % P[2][cardChoice - 1]
		
		print "operator damage: %i" % operatorDamage
        
		aFort *= ratio
		
		print "%s fortitude: %i" % (adversary,aFort)
        
		operatorDamage -= aFort
        
		if operatorDamage < 0 and PM == 1:
			operatorDamage = 0
		
		adversaryDamage *= ratio
        
		print "%s played %s first" % (adversary,A[2][adChoice])
		
		print "%s damage: %i" % (adversary,adversaryDamage)
        
		opFort *= ratio
        
		print "operator fortitude: %i" % opFort
        
		adversaryDamage -= opFort
        
		if adversaryDamage < 0 and AM == 0:
			adversaryDamage = 0
        
		playerHealth -= adversaryDamage
        
		adversaryHealth -= operatorDamage
		
		if adversaryHealth <= 0 or playerHealth <= 0:
			i = adversaryLen + 1
			
		if playerIndex0 < playerIndex1:
			pDeck.pop(playerIndex0)
			pDeck.pop(playerIndex1 - 1)
			
		else:
			pDeck.pop(playerIndex1)
			pDeck.pop(playerIndex0 - 1)
			
		
		if adversaryIndex0 < adversaryIndex1:
			aDeck.pop(adversaryIndex0)
			aDeck.pop(adversaryIndex1 - 1)
			
		else:
			aDeck.pop(adversaryIndex1)
			aDeck.pop(adversaryIndex0 - 1)
			
		
		
		print "you have %i cards" % len(pDeck)
		print "%s has %i cards" % (adversary,len(aDeck))
        
        
	
	health_condition = 0

	if playerHealth > adversaryHealth:
		print "\nVICTORY"
		health_condition = 1
		
	elif playerHealth < adversaryHealth:
		print "\nANNIHILIATION"
		health_condition = 2
        
	else:
		print "\nSTATUS QUO"
		health_condition = 3
        
	return health_condition
