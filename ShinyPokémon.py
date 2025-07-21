#Daycare Simulator
#import time
from time import sleep
from random import randint
from random import choice

starter_pokemon=['rowlet','popplio','litten','pikachu','eevee', 'bulbasaur', 'charmander', 'squirtle', 'cyndaquil', 'totodile', 'chikorita', 'torchic', 'mudkip', 'treecko', 'piplup', 'turtwig', 'chimchar', 'snivy', 'tepig', 'oshawott', 'chespin', 'fennekin', 'froakie', 'grookey', 'scorbunny', 'sobble', 'fuecoco', 'sprigatito', 'quaxly']

#player_choice=input('Choose between rowlet, popplio, litten, pikachu or eevee!\n').lower()
print('The Daycare Couple gave you a Pokémon Egg!\n')
sleep(5)
print('You received an Egg!\n')
sleep(5)

player_choice=choice(starter_pokemon).title()

tsv=randint(1,512)
psv=randint(1,512)
#print(f'Your Trainer Shiny Value is {tsv}!\n')
#print(f'Your Pokémon Shiny Value is {psv}!\n')

atk_iv=randint(0,15)
def_iv=randint(0,15)
speed_iv=randint(0,15)

ball=['pokeball', 'greatball', 'ultraball', 'safariball', 'levelball', 'lureball', 'moonball', 'friendball', 'loveball', 'heavyball', 'fastball', 'sportball', 'premierball', 'repeatball', 'timerball', 'nestball', 'netball', 'diveball', 'luxuryball', 'healball', 'quickball', 'duskball', 'dreamball', 'beastball']

sleep(5)
print('Your Egg is hatching!!!\n')
sleep(5)
print(f'A {player_choice} hatched from the Egg!\n')

if tsv==psv:
	print(f'🌟 \033[93m Your {player_choice.title()} is a Shiny Pokémon! \033[0m 🌟\n')
else:
	print(f'Your {player_choice.title()} is not a Shiny Pokémon!\n')
	
print(f'Your {player_choice.title()} have {atk_iv} Atk IVs, {def_iv} Def IVs and {speed_iv} Speed IVs!\n')
print(f'Caught in a {choice(ball).title()}!\n')