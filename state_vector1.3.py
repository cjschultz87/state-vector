import card_system_v1_5 as cs

cards = [cs.card0, cs.card1, cs.card2, cs.card3, cs.card4, cs.card5, cs.card6]

playerDeck = [cs.card4,cs.card4,cs.card4,cs.card4,cs.card2,cs.card2,cs.card0,cs.card0]

firstAdversaryDeck = [cs.card3,cs.card3,cs.card3,cs.card3,cs.card2,cs.card2,cs.card0]

violetDeck = [cs.card4,cs.card4,cs.card4,cs.card4,cs.card4,cs.card2,cs.card2,cs.card2,cs.card0,cs.card0,cs.card0,cs.card5,cs.card5]

jackDeck = [cs.card5,cs.card5,cs.card5,cs.card5,cs.card3,cs.card3,cs.card3,cs.card3,cs.card3,cs.card0,cs.card0,cs.card0,cs.card0]

naomiDeck = [cs.card2,cs.card2,cs.card2,cs.card2,cs.card4,cs.card4,cs.card4,cs.card4,cs.card6,cs.card6,cs.card6,cs.card6,cs.card6]

leeDeck = [cs.card1,cs.card1,cs.card1,cs.card4,cs.card4,cs.card4,cs.card4,cs.card4,cs.card5,cs.card5]

randomAdversaryDeck = []

aDecks = [firstAdversaryDeck, violetDeck, jackDeck, naomiDeck, leeDeck, randomAdversaryDeck]



print"""
>Operator, welcome to State Vector: Instalment 1.0

>Your goal is to play your cards well, of which you have two in a hand each turn.
>The adversary also has two cards in their hand, in addition to their own deck.
>Make an inference and decide, which card will you attack with?
>Cards are rated with power and health respectively.
>The attacking card first deals damage to the defending card.
>Whatever difference is left is dealt to the adversary.
>Then the adversary's remaining card deals damage to yours, which defends.
>So the health of you and your adversary fluctuate as such.
>Victory is achieved by gaining more health than the adversary.
>Play stops once all cards are used from your deck or theirs.

>Would you like to proceed? 
yes\t(1) 
no\t(2) 
end\t(3)
"""

proceed = 0

condition0 = 0

condition1 = 0

condition2 = 0

endCondition = 0

proceed = input()
	
if not(proceed == 1):
	quit()
		
else:
	condition0 = 1
    

advesary = "null"		

while endCondition == 0:
	
	if condition0 == 1:
		proceed = 0
		
		adversaryDeck = aDecks[cs.dice(6)]

		if adversaryDeck == randomAdversaryDeck:
			sides = cs.dice(16)
	
			i = 0
	
			while i < sides:
				randomAdversaryDeck.append(cards[cs.dice(7)])
		
				p = 0
				while p < 1000:
					cs.dice(25)
					p += 1
			
			i += 1
	
		
		if adversaryDeck == firstAdversaryDeck: 
			print "\nFirst Adversary"
			adversary = "FIRST ADVERSARY"
		elif adversaryDeck == violetDeck:
			print "\nViolet"
			adversary = "VIOLET"
		elif adversaryDeck == jackDeck:
			print "\nJack"
			adversary = "JACK"
		elif adversaryDeck == naomiDeck:
			print "\nNaomi"
			adversary = "NAOMI"
		elif adversaryDeck == leeDeck:
			print "\nLee"
			adversary = "LEE"
		else:
			print "\nRandom Adversary"
			adversary = "RANDOM"
		
		cs.cards(playerDeck, adversaryDeck, adversary)
		

		while proceed == 0:
			proceed = input("End session? (1: yes, 2:no)")
			
			if proceed == 1:
				endCondition = 1
			
			else:
				endCondition = 0
				

print"""
>Would you like to proceed?
play story\t(1)
end session\t(2)
"""

proceed = 0

proceed = int(input())

if proceed == 2:
    quit()
    
sides = cs.dice(len(cards)-1)

playerDeck.append(cards[sides])
index = 0
while index < 5555555:
    index + index
    index += 1
sides = cs.dice(len(cards)-1)
playerDeck.append(cards[sides])

deckUpdateN = len(playerDeck)-1
	
print"""
>Operator, you've earned more cards for
>completing the introductory session.
>Play them with appropriate discrection.

sys> player earned %s
sys> velocity = %i, health = %i
sys> physics = %i, magic = %i

sys> player earned %s
sys> velocity = %i, health = %id
sys> physics = %i, magic = %i


>Would you like to proceed?
yes\t(1)
end\t(2)

""" % (cs.cardDescription(playerDeck,deckUpdateN-1),cs.cardV(playerDeck,deckUpdateN-1),cs.cardHealth(playerDeck,deckUpdateN-1),cs.cardPhysics(playerDeck,deckUpdateN-1),cs.cardMagic(playerDeck,deckUpdateN-1),cs.cardDescription(playerDeck,deckUpdateN),cs.cardV(playerDeck,deckUpdateN),cs.cardHealth(playerDeck,deckUpdateN),cs.cardPhysics(playerDeck,deckUpdateN),cs.cardMagic(playerDeck,deckUpdateN))



proceed = 0

proceed = input()

if proceed == 2:
    quit()

print"""
The wind graces the walls of the Kira Hotel.
You look up at the glistening stars and the neon shades of the city skyscrapers.
They contrast against the architecture of the art deco chateau.
There's a certain tension in your body as you look into the lobby.

You stride into the hotel to the bouncing rhythm of a citypop bassline.
There's a string quartet playing in the background,
but from your perspective their playing is muted compared with the chiptune synths.

The walls have an elegantly carved hardwood panneling.
The designs are bold without being baroque.
You look around and see upholstered chairs neatly strewn across the room
-- a paradox in the heart of the city.

Violet> Pleased to make your acquaintance, my name is Violet.
"""

if adversaryDeck == violetDeck:
    print "Violet> You play your cards with interesting technique."
else:
    print "Violet> I watched your performance from the lobby."
    
print """
> Talk to Violet?
yes\t(1) 
no\t(2)
"""

proceed = input()

if not(proceed == 1):
    quit()
    
newCardVal = 0
    
print"""
Her blazer, with sleeves rolled up to elbow length, goes with her name;
The colour is a solid purple that contrasts against her white pencil skirt.

Violet> The magic of the cards is interwoven with the health of the person holding them. That means that you have to choose whether to use physics or magic carefully.

What do you mean?\t(1)
I realize as much.\t(2)
"""

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
    print """
Violet> There is a conservation of magic in the universe, so if you play a first card magically, the second card defends physically, and vice versa.
"""
    newCardVal += 1
    
elif playerInput == 2:
    print """
Violet> Good to see you're already familiar with the universal balance of magic and physics.
"""

bravo = 1

print """
Violet> Keep in mind that the physics of the cards varies somewhat from what you might expect. The normal understanding of force is about mass and acceleration, but the force of the cards is a component of physical work.

What do you mean?\t(1)
I realize that much.\t(2)
"""

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
    print """
Violet> The physical force of the cards is measured according to the total physical moment of distance and mass. The cards, through their balance of magic and physics have a certain displacement in space and time. Magical force is the quasi-circular integral of displacement in time according to a given magical radius.
"""
    newCardVal += 1

elif playerInput == 2:
    print """
Violet> Well, we don't need to go over things unnecessarily. I am just glad that you seem to have a firm understanding of these topics.
"""

bravo = 1

print """
Violet> Time in terms of magic isn't a dimension.

What do you mean?\t(1)
I realize as much.\t(2)
"""
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
    print """
Violet> With magic you have an orientation in time, but also occupy a given area that is determined by your mana's radius in the temporal plane. How you move through that plane with your cards determines the magical output. If you extend your radius to the extent of a super-circle your magical force increases geometrically.
"""

    newCardVal += 1

elif playerInput == 2:
    print """
Violet> I don't want to tell you what you already understand, so we can skip that topic.
"""

bravo = 1

print """
Violet> Magic in actuality can be quite simple, but is derived from a complex product.

What do you mean?\t(1)
I realize as much.\t(2)
"""
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
    print """
Violet> Because the magical difference is quasi-circular, the magic number is the integral of distance added to an imaginary component: the product of two pi and i. Two pi is the circumference of a unit circle, which is why magical force is the product of mana with the magical displacement actually to its own power. So the magnitude of the complex value is displacement squared minus the square of the product of two pi and i, plus the product of displacement two pi and i squared.
"""
    newCardVal += 1
elif playerInput == 2:
    print """
Violet> We don't need to get into the details.
"""

bravo = 1

print """
Violet> Magical force reacts to fortitude.

What do you mean?\t(1)
I realize as much.\t(2)
"""
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
    print """
Violet> Your physical fortitude is how you defend against magic and vice versa. Keep in mind that whenever you go on the offensive, if your adversary, whoever they are, has more fortitude than you have force, they gain in the difference.
"""
    newCardVal += 1
    
elif playerInput == 2:
    print """
Violet> Unneccessary descriptions only take up time.
"""

bravo = 1

if newCardVal > 1:
    print """
Violet> I had an interesting time talking with you.
"""

if newCardVal > 2:
    print """
Violet> We discussed a good number of topics. That makes me feel sure of things.
"""

if newCardVal > 3:
    print """
Violet> A studious mind such as yours deserves another card.
"""
    
sides = cs.dice(len(cards)-1)

playerDeck.append(cards[sides])
index = 0
while index < 5555555:
    index + index
    index += 1
sides = cs.dice(len(cards)-1)
playerDeck.append(cards[sides])

deckUpdateN = len(playerDeck)-1
	
print"""
>Operator, you've earned more cards.
>Play them with appropriate discrection.

sys> player earned %s
sys> velocity = %i, health = %i
sys> physics = %i, magic = %i

sys> player earned %s
sys> velocity = %i, health = %id
sys> physics = %i, magic = %i
""" % (cs.cardDescription(playerDeck,deckUpdateN-1),cs.cardV(playerDeck,deckUpdateN-1),cs.cardHealth(playerDeck,deckUpdateN-1),cs.cardPhysics(playerDeck,deckUpdateN-1),cs.cardMagic(playerDeck,deckUpdateN-1),cs.cardDescription(playerDeck,deckUpdateN),cs.cardV(playerDeck,deckUpdateN),cs.cardHealth(playerDeck,deckUpdateN),cs.cardPhysics(playerDeck,deckUpdateN),cs.cardMagic(playerDeck,deckUpdateN))

print """
Violet> Would you like to play a round?

yes\t(1)
no\t(2)
"""

while bravo == 1:
    try:
        playerInput = input()
        int(playerInput)
        if (playerInput == 1 or playerInput == 2) == True:
            bravo = 0
        else:
            bravo = 1
            
        if playerInput == 2:
            bravo = 0
        
        elif playerInput == 1:
            round = cs.cards(playerDeck,violetDeck,"VIOLET")
    
            if round == 1:
                print """
Violet> You played your cards well.
"""

                sides = cs.dice(len(cards)-1)

                playerDeck.append(cards[sides])
                index = 0
                while index < 5555555:
                    index + index
                    index += 1
                sides = cs.dice(len(cards)-1)
                playerDeck.append(cards[sides])

                deckUpdateN = len(playerDeck)-1
	
                print"""
>Operator, you've earned more cards.
>Play them with appropriate discrection.

sys> player earned %s
sys> velocity = %i, health = %i
sys> physics = %i, magic = %i


sys> player earned %s
sys> velocity = %i, health = %id
sys> physics = %i, magic = %i
""" % (cs.cardDescription(playerDeck,deckUpdateN-1),cs.cardV(playerDeck,deckUpdateN-1),cs.cardHealth(playerDeck,deckUpdateN-1),cs.cardPhysics(playerDeck,deckUpdateN-1),cs.cardMagic(playerDeck,deckUpdateN-1),cs.cardDescription(playerDeck,deckUpdateN),cs.cardV(playerDeck,deckUpdateN),cs.cardHealth(playerDeck,deckUpdateN),cs.cardPhysics(playerDeck,deckUpdateN),cs.cardMagic(playerDeck,deckUpdateN))

                print """
Violet> Would you like to play another round?

yes\t(1)
no\t(2)
"""
                try:
                    playerInput = input()
            
                    if playerInput == 1:
                        bravo = 1
                    else:
                        bravo = 2
            
                except:
                    bravo = 1
    
            elif round == 2:
                print """
Violet> You didn't do that well, but I can't tell if it was how you played or just bad luck.
"""
            else:
                print """
Violet> A status quo is quite difficult to achieve. Let's enjoy this moment.
"""
            
    except:
        bravo = 1

