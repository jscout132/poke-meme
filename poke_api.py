from random import randint
import requests, json
item_id = 150
url = 'https://pokeapi.co/api/v2/item/'

poke_url_1 = requests.get(url+str(item_id))


from random import randint

mem_list = []
for i in range(0,8):
    rand_num = randint(1,100)
    mem_list.insert(randint(0,len(mem_list)),rand_num)
    mem_list.insert(randint(0,len(mem_list)),rand_num)


item_list = []

for i in mem_list:
    poke_url = requests.get(url+str(i))
    item_list.append(poke_url.json()['name'])

# url_list = []
# for i in mem_list:
#     url_list.append(f'')
#print(max(poke_url_1.json()))

# poke_dict_1 = {
#     'poke_name_1': poke_url_1.json()['forms'][0]['name'],
#     'poke_picture_1': poke_url_1.json()['sprites']['front_shiny'],
#     'types_1': poke_url_1.json()['types'][0]['type']['name']
# }

# make a 4 x 4 grid
# future options to add greater sizes like easy medium hard
# pull 8 random numbers
# and then append those numbers on at random locations again

# make an empty dictionary
# loop through the mem_list numbers
# update the url each time and add to the dictionary the different values
# pass the full dictionary

# maybe some control for number range so it's not just a bunch of similar items