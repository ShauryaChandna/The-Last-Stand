#Start
import sys
import time
import random
lives=20
resources=[]
weapons=[]
inventory={'resources':resources,'weapons':weapons}
username=input("Enter username:  ")
completedtasks=[]
guesses=3
def health(h):
  if h<=0:
      print("You are out of health")
      print('GAME OVER')
      sys.exit()
  elif h>20:
      h = 20
      print('Health = ['+'|'*h + '-'*(20-h) + ']')
  else:
      print('Health = ['+'|'*h + '-'*(20-h) + ']')
def introscene():
  intro=['I woke up, sand in my eyes and mud everywhere else. I was',
'wearing nothing but a pair of pants. It looked like I was',
'on the beach of a deserted island. I had no energy and',
'the sun was shining bright. I got up and dusted myself',
'off and started looking around. There was no civilisation',
'for miles and miles that I hiked. After a few hours I did',
'see a person but he was covered in kevlar and had huge',
'automatic guns. I did not know whether to approach him or',
'not. I finally decided to take the risk and come through',
'the trees with my hands in the air so that he knew I was',
'not a threat, but as soon as I was about to come out of',
'the forest, the person was shot. There was someone else',
'out there, a girl who had a sniper and an smg in her',
'hand. As soon as she shot him, she ran over, took his',
'food, ammo and everything else which she found useful.',
'She then ran back to her shelter. That was the moment I',
'realised, I did not have a lot of options, 1, I could',
'live like a parasite, a leech and live off the food',
'others left behind, 2 I could man up and get over my fear',
'of blood and kill everyone who posed as a threat to me or',
'3 I could get off the island but I had no idea where I',
'was or what I was supposed to do.',
'After a few days, I had learnt the rules of the land. I',
'headed out early in the morning to do some scavenging for',
'resources not knowing what the future held for me, not',
'knowing if I would come back alive or not. I saw some',
'fruits a few hundred meters ahead of me. I jogged up to',
'them and bent over to pick them up and I was happy with',
'myself. It had been a long time since I had any food. As',
'soon as I picked them up and started putting them in my',
'bag, I felt a cold hard piece of metal against the back',
'of my head, it sent shivers down my spine. A shrill and',
'scary voice then said “Drop everything you have and put',
'your hands in the air”. The person told me to turn',
'around. I did as I was told.',
"I didn't know what to do so I..."]
  for i in intro:
    print(i)
  global lives
  a=input('''1. Try to escape
2. Obey their orders
3. Try to fight back

Enter 1/2/3


  '''
  )
  time.sleep(2)

  if a=='1':
    print('ZZZZZZZZZZ')
    time.sleep(1)
    print('You tried to run away but you were zapped from behind!')
    time.sleep(1)
    print('You lose 2 health and your fruits were taken away...')
    time.sleep(1)
    print('You see that he forgets to take his gun, and you pick it up')
    time.sleep(1)
    weapons.append('pistol')
    print('Inventory: ',inventory)
    time.sleep(1)
    lives-=2
    health(lives)
  elif a=='2':
    print('You turn around and see a man, seven feet tall with a gun pointed at your face')
    time.sleep(1)
    print('He takes your fruits and leaves without harming you')
    time.sleep(1)
    print('You see that he forgets to take his gun, and you pick it up')
    time.sleep(1)
    weapons.append('pistol')
    print('Inventory: ',inventory)
    time.sleep(1)
  elif a=='3':
    print('You turn around and see a man, seven feet tall with a gun pointed at your face')
    time.sleep(1)
    print('You smack the gun out of his hand and both of you lay a few punches on each other')
    time.sleep(1)
    print('He retreats and you pick up his gun')
    time.sleep(1)
    print('You lost 3 health')
    time.sleep(1)
    lives-=3
    health(lives)
    for i in range(4):
      resources.append('fruit')
    weapons.append('pistol')

    print('Inventory: ',inventory)
    time.sleep(1)

    print('Eating fruit regains 1 health')
    time.sleep(1)
    b=input('Do you wish to eat 3 fruits to restore your health?(y/n)')
    if b=='y':
      lives+=3
      health(lives)
      for i in range(3):
        resources.remove('fruit')
      print('Inventory: ',inventory)
  time.sleep(3)
  print('-'*20)

def mysteryroom():
  global lives
  print('You enter an empty room, and find a tiny safe in the corner')
  time.sleep(1)
  print('It reads, "Solve the given puzzle and use it as the code for the safe"')
  time.sleep(1)
  print('Find the next number in the series 2,6,15,31,56,?')
  time.sleep(1)
  print('For each wrong answer, you will lose 1 health, so answer carefully!')
  time.sleep(1)
  puzzle=int(input())
  if puzzle==92:
    print('That is correct!')
    print('You open the safe and find a gold key which you put in your bag')
    time.sleep(1)
    resources.append('key')
    print('Inventory:', inventory)
    print()
    print()
  else:
    print('That is incorrect, you lose 1 health')
    time.sleep(1)
    lives-=1
    if "fruit" in resources:
      fr=input('Would you like to eat fruit to restore your health?(y/n)')
      if fr=='y':
        lives+=1
        resources.remove('fruit')
    health(lives)
    repeat=input("Would you like to try the puzzle again?(y/n)")
    if repeat=='y':
      mysteryroom()
  print('-'*20)
  completedtasks.append("mysteryroom")


    
def skyscraper():
  global lives
  print('Lost and confused, you approach a 3000 foot high skyscraper')
  time.sleep(1)
  print("To enter, you must have access to the tower's key")
  time.sleep(1)
  print("-"*20)
  if 'key' not in resources:
    print('You must find the key first, and then enter the skyscraper')
    time.sleep(1)
  else:
    print('You enter the building and see an enemy with grenades in front of you.')
    time.sleep(1)
    if 'crossbow' in weapons:
      print('''Do you wish to use your crossbow or fists to fight, or run into the elevator?
  1. crossbow
  2. fists
  3. elevator

  1/2/3''')
      
      crossfist=input()
      if crossfist=='1':
        print('BOOM')
        time.sleep(1)
        print('You tried shooting at the enemy, but they launched their grenade at the same time')
        time.sleep(1)
        print('The arrow hit the grenade which then exploded')
        time.sleep(1)
        print('You managed to defeat the enemy, but you lost 10 bars of health as well')
        time.sleep(1)
        lives-=10
        health(lives)
      elif crossfist=='2':
        print("You get closer to the enemy, so they don't throw their explosive at you")
        time.sleep(1)
        print("You have a fistfight, where you come out on top!")
        time.sleep(1)
      elif crossfist=='3':
        print("You rush into the elevator but the enemy manages to throw a grenade into the elevator with you")
        time.sleep(1)
        print("You lose 15 health")
        time.sleep(1)
        lives-=15
        health(lives)
    elif 'pistol' in weapons:
      print('''Do you wish to use your gun or fists to fight, or run into the elevator?
  1. gun
  2. fists
  3. elevator

  1/2/3''')
      time.sleep(1)
      
      gunfist=input()
      if gunfist=='1':
        print('BOOM')
        time.sleep(1)
        print('You tried shooting at the enemy, but they launched their grenade at the same time')
        time.sleep(1)
        print('The bullet hit the grenade which then exploded')
        time.sleep(1)
        print('You managed to defeat the enemy, but you lost 10 bars of health as well')
        time.sleep(1)
        print('Since that was the last bullet in the gun, you decide to drop it')
        time.sleep(1)
        weapons.remove('pistol')
        lives-=10
        health(lives)
        print('Inventory: ', inventory)
      elif gunfist=='2':
        print("You get closer to the enemy, so they don't throw their explosive at you")
        time.sleep(1)
        print("You have a fistfight, where you come out on top!")
        time.sleep(1)
      elif gunfist=='3':
        print("You rush into the elevator but the enemy manages to throw a grenade into the elevator with you")
        time.sleep(1)
        print("You lose 15 health")
        time.sleep(1)
        lives-=15
        health(lives)
    else:
      print('''Do you wish to use your fists to fight, or run into the elevator?
  1. fists
  2. elevator

  1/2''')
      
      gunfist=input()

      if gunfist=='1':
        print("You get closer to the enemy, so they don't throw their explosive at you")
        time.sleep(1)
        print("You have a fistfight, where you come out on top!")
        time.sleep(1)
        grenade=input("Do you wish to pick up the grenades(y/n)")
        if grenade=='y':
          for i in range(3):
            weapons.append('grenade')
      elif gunfist=='2':
        print("You rush into the elevator but the enemy manages to throw a grenade into the elevator with you")
        time.sleep(1)
        print("You lose 15 health")
        time.sleep(1)
        lives-=15
        health(lives)
    print('You reach the top of the skyscraper and find a machine gun, a shield, a sword and a tablet')
    time.sleep(1)
    weapons.append('machine gun')
    weapons.append('sword')
    resources.append('shield')
    resources.append('tablet')
    completedtasks.append('skyscraper')
    print('-'*20)
    completion()

def archer():
  global lives
  if 'pistol' not in weapons and 'shield' not in resources:
    print('You need either a pistol or a sword for this challenge')

  print('You see an expansive farm, and decide to enter it to get some food')
  time.sleep(1)
  print('THUNK')
  time.sleep(1)
  print('An arrow zips past you. You turn around and see an archer aiming at you from distance')
  time.sleep(1)
  if 'pistol' in weapons:
    print('You must fight the archer')
    time.sleep(1)
    print('You could either shoot from here or try to get closer and get a better angle on the archer')
    time.sleep(1)
    range=input('''
1. Shoot from current location
2. Get closer to the archer

1/2
''')
    if range=='1':
      print('You were able to hit the archer with a lucky shot')
      time.sleep(1)
      
    elif range=='2':
      print('The archer hit you once while you came closer to her')
      time.sleep(1)
      print("You lost 8 health")
      time.sleep(1)
      lives-=8
      health(lives)
      print('You got close enough to get a good shot on her, and managed to defeat her')
      time.sleep(1)

    print('Your pistol is out of ammo so you have to drop it')
    time.sleep(1)
    weapons.remove('pistol')
    crossbow=input('Would you like to pick up the crossbow?(y/n)')
    if crossbow=='y':
      weapons.append('crossbow')
    print('Inventory: ', inventory)
    time.sleep(1)

  elif 'shield' in resources:
    archery=input('''How would you like to protect yourself?
1. shield
2. machine gun

1/2

''')
    if archery=='1':
      print("You shield yourself from the archer's arrows as you get closer and closer to her")
      time.sleep(1)
      killarcher=input('''Now that you are next to the archer, you can also use your sword to kill her
      
1. machine gun
2. sword

1/2''')
      if killarcher=='1':
        print('While your machine gun was loading up, the archer managed to lay a few blows on you with her crossbow')
        time.sleep(1)
        print('You lost 7 health')
        time.sleep(1)
        print('After the machine gun loaded up, you were able to defeat the archer')
        time.sleep(1)
        lives-=7
        health(lives)
      elif killarcher=='2':
        print("You put your shield down, and swung the sword through the archer's chest")
        time.sleep(1)
      

    elif archery=='2':
      print('While you were loading up your machine gun, the archer shot a few arrows at you')
      time.sleep(1)
      numberarrows= random.randint(0,3)
      print('The archer hit you' , numberarrows, 'times')
      print('You lost', 4*numberarrows, 'health')
      lives-=4*numberarrows
      health(lives)
      print('You were finally able to hit the archer with your gun, and managed to defeat her')
      time.sleep(1)
    
    crossbow=input('Would you like to pick up the crossbow?(y/n)')
    if crossbow=='y':
      weapons.append('crossbow')
    print('Inventory: ', inventory)
    time.sleep(1)
    completedtasks.append('archer')
    print('-'*20)
    completion()
  

def zombies():
  global lives
  print('While exploring the map, you sense a garbage like smell')
  time.sleep(1)
  print('Zombies start surrounding you from all corners')
  time.sleep(1)
  if 'pistol' in weapons:
    zombiefight=input(''' How will you escape the zombies?
1. Try to run away from them
2. Shoot them with your pistol

1/2

'''
)
    if zombiefight=='1':
      zombiecount=random.randint(0,5)
      print('While running away', zombiecount,'zombies got a hold of you')
      time.sleep(1)
      print('You lost',zombiecount*2,'health')
      time.sleep(1)
      lives-=zombiecount*2
      health(lives)
    elif zombiecount=='2':
      print('You could not shoot all the zombies quick enough, and they managed to hurt you')
      time.sleep(1)
      print('You lost 4 health')
      time.sleep(1)
      lives-=4
      health(lives)
      weapons.remove('pistol')
  else:
    if 'machine gun' in weapons and 'crossbow' in weapons:
      zombiefight=zombiefight=input(''' How will you escape the zombies?
1. Try to run away from them
2. Shoot them with your crossbow
3. Shoot them with your minigun

1/2/3

'''

      )
      if zombiefight=='1':
        zombiecount=random.randint(0,5)
        print('While running away', zombiecount,'zombies got a hold of you')
        time.sleep(1)
        print('You lost',zombiecount*2,'health')
        time.sleep(1)
        lives-=zombiecount*2
        health(lives)
      elif zombiefight=='2':
        print('You could not shoot all the zombies quick enough, and they managed to hurt you')
        time.sleep(1)
        print('You lost 6 health')
        time.sleep(1)
        lives-=6
        health(lives)
      elif zombiefight=='3':
        print('You chose the best option, and defeated the zombies')
        time.sleep(1)
        print('You gain 3 health')
        time.sleep(1)
        lives+=3
        if lives>20:
          lives=20
        health(lives)
    elif 'crossbow' in weapons:
      zombiefight=zombiefight=input(''' How will you escape the zombies?
1. Try to run away from them
2. Shoot them with your crossbow

1/2

'''

      )
      if zombiefight=='1':
        zombiecount=random.randint(0,5)
        print('While running away', zombiecount,'zombies got a hold of you')
        time.sleep(1)
        print('You lost',zombiecount*2,'health')
        time.sleep(1)
        lives-=zombiecount*2
        health(lives)
      elif zombiefight=='2':
        print('You could not shoot all the zombies quick enough, and they managed to hurt you')
        time.sleep(1)
        print('You lost 6 health')
        time.sleep(1)
        lives-=6
        health(lives)


    elif 'machine gun' in weapons:
      zombiefight=zombiefight=input(''' How will you escape the zombies?
1. Try to run away from them
2. Shoot them with your minigun

1/2

'''

      )
      if zombiefight=='1':
        zombiecount=random.randint(0,5)
        print('While running away', zombiecount,'zombies got a hold of you')
        time.sleep(1)
        print('You lost',zombiecount*2,'health')
        time.sleep(1)
        lives-=zombiecount*2
        health(lives)

      elif zombiefight=='2':
        print('You chose the best option, and defeated the zombies')
        time.sleep(1)
        print('You gain 3 health')
        time.sleep(1)
        lives+=3
        if lives>20:
          lives=20
        health(lives)
  completedtasks.append('zombies')
  print('-'*20)
  completion()

def completion():
  if 'zombies' in completedtasks and 'archer' in completedtasks and 'skyscraper' in completedtasks:
    robot()

def robot():
  global guesses
  print('You wake up in the middle of a huge ship')
  time.sleep(1)
  print('A mechanical sound plays from a speaker, "You have reached the final stage. Bring your A game, or prepare to die"')
  time.sleep(1)
  print('You have been tested in the toughest of physical conditions, but this challenge is all about your brain')
  time.sleep(1)
  print('A giant robot appears, and displays a message')
  time.sleep(1)
  final= int(input('''
______________________________________________________________________________________________
|                                     Solve the Puzzle                                        |
|Gunman         716                                                                           |
|Mysteryroom    13211                                                                         |
|Skyscraper     19310                                                                         |
|Archer         146                                                                           |
|Zombies        2657                                                                          |
|Robot          ?                                                                             |
|_____________________________________________________________________________________________|

'''
#The first one or two characters of the code is the position of the first letter of the word in the english alphabet. 
#The next character is the serial number of the word in the puzzle
#The last one or two characters is the number of letters in the word
  ))
  if final==1865:
    print('The floor disappears, you fall... slowly')
    time.sleep(3)
    print("Reaching closer to land, you start thinking that you're finally out of lives, and this is how you die")
    time.sleep(2)
    print("There is a loud THUD")
    time.sleep(1)
    print("But somehow you are still alive")
    time.sleep(1)
    print("You look around, and see banners and posters of you all around")
    time.sleep(1)
    print("It seems you had got the right answer, and with that, saved humanity")
    time.sleep(1)
    print("GAME OVER")
  else:
    guesses-=1
    print('INCORRECT')
    time.sleep(1)
    print('You have', guesses, 'guesses left')
    if guesses==0:
      print('YOU LOSE')
      sys.exit()
    robot() 

playermap = []
def islandgen():
  global gamemap
  gamemap = [["~", "~", "~", "~", "~", "~", "~", "~",], ["~", "~", "~", "~", "~", "~", "~", "~",], ["~", "~", "~", "~", "~", "~", "~", "~",], ["~", "~", "~", "~", "~", "~", "~", "~",], ["~", "~", "~", "~", "~", "~", "~", "~",], ["~", "~", "~", "~", "~", "~", "~", "~",], ["~", "~", "~", "~", "~", "~", "~", "~",], ["~", "~", "~", "~", "~", "~", "~", "~",], ["~", "~", "~", "~", "~", "~", "~", "~",], ["~", "~", "~", "~", "~", "~", "~", "~",], ["~", "~", "~", "~", "~", "~", "~", "~",], ["~", "~", "~", "~", "~", "~", "~", "~",], ["~", "~", "~", "~", "~", "~", "~", "~",], ["~", "~", "~", "~", "~", "~", "~", "~",], ["~", "~", "~", "~", "~", "~", "~", "~",], ["~", "~", "~", "~", "~", "~", "~", "~",]]
  x = 4
  y = 8
  gamemap[12][5] = "∆"
  cont = 1
  storycount = 0
  global playermap

  #specifically 10 spaces are covered out of the original 25(not including the starting space at gamemap[0][0])
  for i in range(96):
    #we basically create a machine that "explores" the dungeon and creates the layout as it goes
    dire = []
    d = {"left": 1, "right": 1, "up": 1, "down": 1}

    #here we decide what are the possible ways for the machine to go; it will not cross the boundaries of the area and it will not retrace its steps
    if y == 0 or gamemap[y-1][x] == "ø":
      d["up"] = 0
    if y == 15 or gamemap[y+1][x] == "ø":
      d["down"] = 0
    if x == 0 or gamemap[y][x-1] == "ø":
      d["left"] = 0
    if x == 7 or gamemap[y][x+1] == "ø":
      d["right"] = 0
    for i in d:
      if d[i] == 1:
        dire.append(i)
    try:
      #we use the try statement here because there is a small chance that the machine backs itself into a corner and has no available spaces, which would cause the randint to have a range of (0,0) which throws an error
      picker = random.randint(0, len(dire)-1)
    except:
      count = 0
      for i in range(len(gamemap)-1):
        for j in range(len(gamemap[i])-1):
          if gamemap[i][j] == "ø":
            count += 1
      if count < 64:
        islandgen()
        return
        break
      else:
        for i in range(len(gamemap)-1):
          for j in range(len(gamemap[i])-1):
            if gamemap[i][j] == "~":
              x = j
              y = i
              
    if len(dire) == 0:
      for i in range(len(gamemap)-1):
          for j in range(len(gamemap[i])-1):
            if gamemap[i][j] == "~":
              x = j
              y = i
      continue

    #heer we decide the coordinates the machine moves to using the direection obtained by the picker 
    if dire[picker] == "up":
      y -= 1
    elif dire[picker] == "down":
      y += 1
    elif dire[picker] == "right":
      x += 1
    elif dire[picker] == "left":
      x -= 1
    gamemap[y][x] = "ø"
 
  for i in gamemap:
    print(i)
  print()
  #since we don't want the player to know the hidden events, we provide them with a copy of the gamemap that only tells them their path
  for i in gamemap:
    k = i[:]
    playermap.append(k[:])


  #here we decide on event spaces; ¥ is a treasure space(10% chance of spawning) and ¢ is an enemy space(20% chance of spawning)
  for i in range(len(gamemap)):
    for j in range(len(gamemap[i])):
      if gamemap[i][j] == "ø":
        d10 = random.randint(1, 10)
        if d10 == 2:
          gamemap[i][j] = "¥"
        elif d10 == 4 or d10 == 6:
          gamemap[i][j] = "¢"
        elif d10 <= 10 and storycount <= 3:
          gamemap[i][j] = "π"
          storycount += 1
    gamemap[12][5] = "Δ"


def mapcheck():
  global playermap
  for i in playermap:
    print(i)

def playerdirection():
  global xcoord, ycoord, newx, newy, direection
  y = ycoord
  x = xcoord
  dire = []
  d = {"left": 1, "right": 1, "up": 1, "down": 1}
  if y == 0 or playermap[y-1][x] == "~":
      d["up"] = 0
  if y == 15 or playermap[y+1][x] == "~":
      d["down"] = 0
      print("nope")
  if x == 7 or playermap[y][x+1] == "~":
      d["right"] = 0
  if x == 0 or playermap[y][x-1] == "~":
      d["left"] = 0
  for i in d:
      if d[i] == 1:
          dire.append(i)
  for i in range(len(dire)):
      print(str(i+1)+":",dire[i])
    
  choosedire = int(input("Pick a direction(Enter the number)"))-1
  if dire[choosedire] == "up":
      newy = ycoord-1
  if dire[choosedire] == "down":
      newy = ycoord+1
  if dire[choosedire] == "left":
      newx = xcoord-1
  if dire[choosedire] == "right":
      newx = xcoord+1

  playermap[ycoord][xcoord] = "□"
          
def playermovement():
  global xcoord, ycoord, newx, newy, completedtasks, resources, gamemap
  global up, down, left, right
  try:
    xcoord = newx
    ycoord = newy
  except:
    xcoord = 5
    ycoord = 12
    newx, newy = 5, 12
  playerdirection()

  if gamemap[newy][newx] == "¥":
      print("you found some fruit!")
      resources.append("fruit")
  elif gamemap[newy][newx] == "¢":
      battle()
  elif gamemap[newy][newx] == "π":
      if 'mysteryroom' not in completedtasks:
          mysteryroom()
      elif 'skyscraper' not in completedtasks:
          skyscraper()
      else:
          z = random.randint(0,1)
          if z == 0:
              zombies()
          elif z == 1:
              archer()
  playermap[newy][newx] = "Δ"
      
def battle():
  x = random.randint(1,99)
  if x < 34:
    encounter1()
  elif x < 67:
    encounter2()
  elif x < 100:
    encounter3()
  
def encounter1():
  enemyhealth = 5
  global lives, resources
  print("-"*30)
  print("You see a gunman! He attacks!"), print("-"*30)
  print('''        ___ 
     __|___|__ 
      ('o_o') 
      _\~-~/_    ______. 
     //\__/\ \ ~(_]---' 
    / )O  O( .\/_) 
    \ \    / \_/ 
    )/_|  |_\ 
   // /(\/)\ \ 
   /_/      \_\ 
  (_||      ||_) 
    \| |__| |/ 
     | |  | | 
     | |  | | 
     |_|  |_| 
     /_\  /_\ ''')
  while enemyhealth > 0:
    print("-"*30)
    print("HP:", enemyhealth)
    print("1: Use pistol", "    ", "2: Run", "    ", "3: Heal")
    action = int(input("What do you want to do?(1/2/3)"))
    print()
    if action == 1:
      damage = random.randint(1,5)
      enemyhealth -= damage
      print("-"*30)
      print("Bang!"), print("You shot the gunman!"), print("You dealt", damage, "damage!"), print()
      time.sleep(1)

    elif action == 2:
        print("He shoots you as you run! You take 2 damage")
        lives -=2
        health(lives)
        print("-"*30)
        time.sleep(1)
        return
    
    elif action == 3:
      print("-"*30)
      if "fruit" in resources:
          lives+=1
          resources.remove('fruit')
          health(lives)
          print("you ate a fruit")
      else:
          print("You have no fruit left!")

    if enemyhealth <= 0:
      break

    time.sleep(1)
    print("-"*30)
    print(), print("The gunman fires!"), print("BANG!"), print()

    
    x = random.randint(0,1)
    if x == 0:
        lives -= random.randint(1,5)
        health(lives)
    else:
        print("-"*30)
        print("The attack missed!"), print()
        time.sleep(1)
    
  print("-"*30)
  print("You deafeated the gunman!"), print("You were healed by 25% of your Max Health"), print()
  time.sleep(1)
  lives += 5
  health(lives)
  time.sleep(1)

def encounter2():
  enemyhealth = 7
  global lives, resources
  print("-"*30)
  print("You see a bomber! He throws a stick of dynamite at you!"), print("-"*30)
  print('''
                _-*
        _------'
      _/
     / /
    / /
   / /
  / /
 / /
(_)
''')
  while enemyhealth > 0:
    print("-"*30)
    print("HP:", enemyhealth)
    print("1: Use pistol", "    ", "2: Run", "    ", "3: Heal")
    action = int(input("What do you want to do?(1/2/3)"))
    print()
    if action == 1:
      damage = random.randint(1,5)
      enemyhealth -= damage
      print("-"*30)
      print("Bang!"), print("You shot the bomber!"), print("You dealt", damage, "damage!"), print()
      time.sleep(1)

    elif action == 2:
        print("An explosion hits you as you run! You take 3 damage")
        lives -=2
        health(lives)
        print("-"*30)
        time.sleep(1)
        return
    
    elif action == 3:
      print("-"*30)
      if "fruit" in resources:
          lives+=1
          resources.remove('fruit')
          health(lives)
          print("you ate a fruit")
      else:
          print("You have no fruit left!")

    if enemyhealth <= 0:
      break

    time.sleep(1)
    print("-"*30)
    print(), print("The bomber throws a bomb!"), print("BANG!"), print()

    
    x = random.randint(0,1)
    if x == 0:
        lives -= random.randint(3,6)
        health(lives)
    else:
        print("-"*30)
        print("The bomb missed!"), print()
        time.sleep(1)
    
  print("-"*30)
  print("You deafeated the bomber!"), print("You were healed by 25% of your Max Health"), print()
  time.sleep(1)
  lives += 5
  health(lives)
  time.sleep(1)

def encounter3():
  enemyhealth = 3
  global lives, resources
  print("-"*30)
  print("You see a archer! They fire an arrow!"), print("-"*30)
  print('''
       /\ 
      /__\_{) 
     |--<<)__\ 
      \  /  ( 
       \/   ) 
           /| 
           \ \ 
           ~ ~ ''')
  while enemyhealth > 0:
    print("-"*30)
    print("HP:", enemyhealth)
    print("1: Use pistol", "    ", "2: Run", "    ", "3: Heal")
    action = int(input("What do you want to do?(1/2/3)"))
    print()
    if action == 1:
      damage = random.randint(1,5)
      enemyhealth -= damage
      print("-"*30)
      print("Bang!"), print("You shot the archer!"), print("You dealt", damage, "damage!"), print()
      time.sleep(1)

    elif action == 2:
        print("He shoots you as you run! You take 2 damage")
        lives -=2
        health(lives)
        print("-"*30)
        time.sleep(1)
        return
    
    elif action == 3:
      print("-"*30)
      if "fruit" in resources:
          lives+=1
          resources.remove('fruit')
          health(lives)
          print("you ate a fruit")
      else:
          print("You have no fruit left!")

    if enemyhealth <= 0:
      break

    time.sleep(1)
    print("-"*30)
    print(), print("The archer fires!"), print("FWOOSH!"), print()

    
    x = random.randint(0,1)
    if x == 0:
        lives -= random.randint(3,7)
        health(lives)
    else:
        print("-"*30)
        print("The arrow missed!"), print()
        time.sleep(1)
    
  print("-"*30)
  print("You deafeated the archer!"), print("You were healed by 25% of your Max Health"), print()
  time.sleep(1)
  lives += 5
  health(lives)
  time.sleep(1)

#Actual game is run here
print("WELCOME TO")
print(''' _               _     _____ _                  _ 
| |             | |   /  ___| |                | | 
| |     __ _ ___| |_  \ `--.| |_ __ _ _ __   __| | 
| |    / _` / __| __|  `--. \ __/ _` | '_ \ / _` | 
| |___| (_| \__ \ |_  /\__/ / || (_| | | | | (_| | 
\_____/\__,_|___/\__| \____/ \__\__,_|_| |_|\__,_| ''')
maininput = input("Press any key to continue")

forever = 1
introscene()
islandgen()

while forever == 1:
    playermovement()
    mapcheck()
