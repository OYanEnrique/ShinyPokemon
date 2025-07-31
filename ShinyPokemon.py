#Daycare Simulator
#import time
from time import sleep
from random import randint
from random import choice

shiny= False
judge= 'Ok stats'
starter_pokemon=['rowlet','popplio','litten','pikachu','eevee', 'bulbasaur', 'charmander', 'squirtle', 'cyndaquil', 'totodile', 'chikorita', 'torchic', 'mudkip', 'treecko', 'piplup', 'turtwig', 'chimchar', 'snivy', 'tepig', 'oshawott', 'chespin', 'fennekin', 'froakie', 'grookey', 'scorbunny', 'sobble', 'fuecoco', 'sprigatito', 'quaxly']

nature=['Hardy', 'Lonely', 'Adamant', 'Naughty', 'Brave', 'Bold', 'Docile', 'Impish', 'Lax', 'Relaxed', 'Modest', 'Mild', 'Bashful', 'Rash', 'Quiet', 'Calm', 'Gentle', 'Careful', 'Quirky', 'Sassy', 'Timid', 'Hasty', 'Jolly', 'Naive', 'Serious']
#player_choice=input('Choose between rowlet, popplio, litten, pikachu or eevee!\n').lower()
print("="*50)
print('The Daycare Couple gave you a Pokémon Egg!')
print("="*50)
sleep(2)
print('\nYou received an Egg!\n')
sleep(2)

player_choice=choice(starter_pokemon).title()

pokemon_nature=choice(nature).title()

tsv=randint(1,512)
psv=randint(1,512)
#print(f'Your Trainer Shiny Value is {tsv}!\n')
#print(f'Your Pokémon Shiny Value is {psv}!\n')

atk_iv=randint(0,31)
def_iv=randint(0,31)
speed_iv=randint(0,31)
spatk_iv=randint(0,31)
spdef_iv=randint(0,31)

ball=['pokeball', 'greatball', 'ultraball', 'safariball', 'levelball', 'lureball', 'moonball', 'friendball', 'loveball', 'heavyball', 'fastball', 'sportball', 'premierball', 'repeatball', 'timerball', 'nestball', 'netball', 'diveball', 'luxuryball', 'healball', 'quickball', 'duskball', 'dreamball', 'beastball']

caught_ball=choice(ball)

sleep(2)
print('Your Egg is hatching!!!\n')
sleep(2)
print(f'A {player_choice} hatched from the Egg!\n')

if tsv==psv:
	shiny=True
	print(f'🌟 \033[93m Your {player_choice.title()} is a Shiny Pokémon! \033[0m 🌟\n')
else:
	print(f'Your {player_choice.title()} is not a Shiny Pokémon!\n')
	
print(f'Your {player_choice.title()} have {atk_iv} Atk IVs, {spatk_iv} Sp. Atk IVs, {def_iv} Def IVs, {spdef_iv} Sp. Def IVs and {speed_iv} Speed IVs!\n')

print(f'{pokemon_nature} Nature!\n')

print("="*50)
print('Pokémon Judge')
print("="*50)
sleep(2)
print(f'\nJudging your {player_choice}!\n')
sleep(2)
if atk_iv + spatk_iv + def_iv +spdef_iv +speed_iv <= 90:
	judge='Ok stats'
	print(f'Your {player_choice.title()} have OK stats!\n')
elif atk_iv + spatk_iv + def_iv +spdef_iv +speed_iv >=91 and atk_iv + spatk_iv + def_iv +spdef_iv +speed_iv <= 120:
	judge='Good stats'
	print(f'Your {player_choice.title()} have Good stats!\n')
elif atk_iv + spatk_iv + def_iv +spdef_iv +speed_iv >=121 and atk_iv + spatk_iv + def_iv +spdef_iv +speed_iv <= 150:
	judge='Great stats'
	print(f'Your {player_choice.title()} have Great stats!\n')
elif atk_iv + spatk_iv + def_iv +spdef_iv +speed_iv >=151 and atk_iv + spatk_iv + def_iv +spdef_iv +speed_iv <= 186:
	judge='Amazing Stats'
	print(f'Your {player_choice.title()} have Amazing Stats!\n')

print(f'Caught in a {caught_ball.title()}!\n')
print(f'TSV: {tsv}, PSV: {psv}\n')

with open("PokemonGenerator.txt", "a") as savefile:
	savefile.write("\n")
	savefile.write("\n")
	savefile.write("="*50)
	savefile.write('\nPokémon hatched!\n')
	savefile.write(f'\nPokémon: {player_choice}')
	savefile.write(f'\nNature: {pokemon_nature}')
	savefile.write(f'\nShiny: {shiny}')
	savefile.write(f'\nCaught in a {caught_ball.title()}')
	savefile.write(f'\nAtk IV: {atk_iv}, Sp. Atk IV: {spatk_iv}, Def: {def_iv}, Sp. Def {spdef_iv}, Speed: {speed_iv}\n')
	savefile.write(f'{judge}\n')
	savefile.write(f'\nTSV: {tsv}, PSV: {psv}')
	savefile.write("\n")
	savefile.write("="*50)
	