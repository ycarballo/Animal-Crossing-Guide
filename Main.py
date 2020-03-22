# Yanira Carballo
# March 21, 2020
# My Intergration Project- Animal Crossing Info Guide
# Intro to Animal Crossing


print('Welcome to the Animal Crossing Infomation Guide')
print('\n')
name = input (('Please enter your name: '))
print('\n')
print('Welcome' , name + '!')
print('\n')
print('You will be learning what Animal Crossing is and everything around it.')
print('\n')
print('At any moment you may enter "stop" to quit the guide when promted to type.')
print('\n')
start = input(('Enter "start" to begin: '))
print('\n')
if (start == 'start'):
    print("Let's get started then!")
    print('\n')
else:
    print('You have stopped the guide. You may now close the program. Have a great day!')
    exit()

    
# This was the introduction to the program. Next will be a short history of the game.

print('Animal Crossing is a simulation video game series created by Katsuya Eguchi and developed by Nintendo.')
print('\n')
print('The series is about your character going around making friends and doing activities.')
print('\n')
print('It is a cute, enjoyable, and stress relieving game which is why it has a huge fan base.')
print('\n')
print('The first game in the series was released on April 14, 2001 which was just called Animal Crossing.')
print('\n')
print('The games in this series are:')
print('\n')
game1 = ('Animal Crossing (2001)')
game2 = ('Animal Crossing: Wild World (2005)')
game3 = ('Animal Crossing: City Folk (2008)')
game4 = ('Animal Crossing: New Leaf (2012)')
game5 = ('Animal Crossing: Happy Home Designer (2015)')
game6 = ('Animal Crossing: Pocket Camp (2017)')
game7 = ('Animal Crossing: New Horizons (2020)')
games_in_series = [game1 , game2 , game3 , game4 , game5 , game6 , game7]
print(* games_in_series , sep = "\n")
print('\n')

# Next will be what you can do in the game.


print('There are many fun activities to do in the series.')
print('\n')
answer_to_fishing = (input('For example do you like to fish? (Enter yes or no): '))
if (answer_to_fishing == 'yes'):
    print('\n')
    print("That's great to hear becuase in Animal Crossing, fishing a a main activity you can do.")
    print('\n')
    print("There are plenty of fish species you can find and let's you know intesting facts about them.")
    print('\n')
    print('You can also donate them to a museum or sell them for currency!')
elif (answer_to_fishing == 'no'):
    print('\n')
    print("That's alright! There are still so many other activities you can do in the Animal Crossing World.")
    print('\n')
else:
    print('\n')
    print('You have stopped the guide. You may now close the program. Have a great day!')
    exit()
    
print('\n')
print('Along with fishing, you can also catch bugs, gather fruit, garden, and dig up fossils.')
print('\n')
print('Of course with everything you find, you can also donate it, sell it, or keep it to decorate your house anyway you want!')
print('\n')

# Next I will dicussing the villagers and what they can do.



print('One of the reasons why Animal Crossing is popular is because of its villagers.')
print('\n')
print('Villagers are animal charaters in the Animal Crossing world. They are not controlled by the players.')
print('\n')
print('They each have their own personalities, preferred style, and birthdays. They contribute a lot to the game.')
print('\n')
print("If one were to play the games, you'll find out that you'll like some villagers more than others.")
print('\n')
print('You can also interact with them. They give you cute nicknames and presents.')
print('\n')
print("For example if you accidentally hit them with a net, they'll say:")
print('\n')
saying = ('ow!')
x = 0
while (x <= 4):
    print(saying , end = ' ' )
    x = x + 1
print('\n')
print("Let's check out some villagers!")
print('\n')
dog = ('Goldie')
cat = ('Rosie')
bird = ('Midge')
elephant = ('Tia')
rabbit = ('Doc')

def stop():
    if (fav_animal == 'stop'):
       print('You have stopped the guide. You may now close the program. Have a great day!')
       exit()

fav_animal = (input('What is your most favorite animal from this list? (Dog, cat, bird, elephant, or rabbit): '))
print('\n')
if (fav_animal == 'dog'):
    print('A dog character is a villager named' , dog ,  'and her birthday is December 27 and she enjoys a more natural style.')
elif (fav_animal == 'cat'):
    print('A cat character is a villager named' , cat , 'and her birthday is Februay 27 and she is a peppy character.')
elif (fav_animal == 'bird'):
    print('A bird character is a villager named' , bird , 'and her birthday is March 12 and she likes both natural and cute styles')
elif (fav_animal == 'elephant'):
    print('An elephant chacater is a villager name' , elephant , 'and her birthday is November 18 and adores elegance and fancy items')
elif (fav_animal == 'rabbit'):
    print('A rabbit character is a villager named' , rabbit , 'and his birthday is June 9 and tends to be a bit lazy')
elif (fav_animal == 'stop'):
      stop ()

print('\n')
print('Now you should know a little more about my favorite game, Animal Crossing')





        
