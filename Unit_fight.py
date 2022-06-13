dummy_class = {
'name' : 'dummy class',
'health' : 1,
'melee_damage' : 1,
'pierce_damage' : 1,
'range' : 1,
'rof' : 1,
'melee_armour' : 1,
'pierce_armour' : 1,
'armour_classes' : [],
'bonus_damage' : {},
'los' : 1
}

pikeman = {
                'name' : 'pikeman',
                'health' : 55,
                'melee_damage' : 4,
                'pierce_damage' : 0,
                'range' : 0,
                'rof' : 3.05,
                'melee_armour' : 0,
                'pierce_armour' : 0,
                'armour_classes' : ['infantry', 'spearman'],
                'bonus_damage' : {'cavalry' : 22, 'camel' : 18},
                'los' : 4
}

camel_rider = {'name' : 'camel rider',
               'health' : 100, 
               'melee_damage' : 6, 
               'pierce_damage' : 'n/a', 
               'range' : 0, 
               'rof' : 2.03, 
               'melee_armour' : 0, 
               'pierce_armour' : 0, 
               'armour_classes' : ['camel'], 
               'bonus_damage' : {'cavalry' : 9, 'camel' : 5}, 
               'los' : 4  
               }
knight = {'name' : 'knight',
          'health' : 100, 
          'melee_damage' : 10, 
          'pierce_damage' : 'n/a', 
          'range' : 0, 'rof' : 1.83, 
          'melee_armour' : 2, 
          'pierce_armour' : 2, 
          'armour_classes' : ['cavalry'], 
          'bonus_damage' : {}, 
          'los' : 4  
         }

elite_magyar_huszar_FU = {
                        'name' : 'elite magyar huszar',
                        'health' : 105,
                        'melee_damage' : 14,
                        'pierce_damage' : 0,
                        'range' : 0,
                        'rof' : 1.83,
                        'melee_armour' : 3,
                        'pierce_armour' : 6,
                        'armour_classes' : ['cavalry', 'unique unit'],
                        'bonus_damage' : {'siege weapon' : 8, 'ram' : 2},
                        'los' : 6
                        }

two_handed_swordsman_FU = {
                'name' : 'two handed swordsman',
                'health' : 60,
                'melee_damage' : 16,
                'pierce_damage' : 0,
                'range' : 0,
                'rof' : 2.03,
                'melee_armour' : 4,
                'pierce_armour' : 5,
                'armour_classes' : ['infantry'],
                'bonus_damage' : {'eagle warrior' : 8},
                'los' : 5
}



def ttk(unit_1, unit_2):
    #how long it takes for unit 2 to kill unit 1
    hits = 0
    results = {}
    current_health = unit_1['health']
    while current_health > 0:
        hits += 1
        if unit_2['melee_damage'] != 'n/a':
            if unit_2['melee_damage'] > unit_1['melee_armour']:
                current_health = current_health + unit_1['melee_armour'] - unit_2['melee_damage'] - bonus(unit_1,unit_2)
            else:
                current_health = current_health - 1 -bonus(unit_1,unit_2)
        if unit_2['pierce_damage'] != 'n/a':
            if unit_2['pierce_damage'] > unit_1['pierce_armour']:
                current_health = current_health + unit_1['pierce_armour'] - unit_2['pierce_damage'] - bonus(unit_1,unit_2)
            else:
                current_health = current_health - 1 - bonus(unit_1,unit_2)
    time_to_kill = (hits - 1) * unit_2['rof']
    # Assumes both units attack at same time, time starts when first hit is registered.
    # results = {'time to kill' : time_to_kill}
    return time_to_kill

def bonus(unit_1, unit_2):
    #bonus damage done by unit 2 to unit 1
    damage = 0
    for i in unit_1['armour_classes']:
        if i in unit_2['bonus_damage'].keys():
            damage += unit_2['bonus_damage'][i]
    return damage

def health_remaining(unit_1, unit_2):
    # not used, incorporated code into fight function
    if ttk(unit_1, unit_2) > ttk(unit_2, unit_1):
        return unit_1['health'] - (((ttk(unit_2, unit_1) - (ttk(unit_2, unit_1) % unit_2['rof']))/unit_2['rof']) * (unit_2['melee_damage'] + bonus(unit_1,unit_2)))
    elif ttk(unit_2, unit_1) > ttk(unit_1, unit_2):
        return unit_2['health'] - (((ttk(unit_1, unit_2) - (ttk(unit_1, unit_2) % unit_1['rof']))/unit_1['rof']) * (unit_1['melee_damage'] + bonus(unit_2,unit_1)))


print(ttk(knight, camel_rider))
        
# print(ttk(knight, pikeman))

# print(ttk(camel_rider, pikeman))

# print(ttk())

# print(health_remaining(pikeman,camel_rider))

def fight(unit_1, unit_2):
    if ttk(unit_1, unit_2) > ttk(unit_2, unit_1):
        health1 = unit_1['health'] - ((((ttk(unit_2, unit_1) - (ttk(unit_2, unit_1) % unit_2['rof']))/unit_2['rof']) + 1) * (unit_2['melee_damage'] + bonus(unit_1,unit_2) - unit_1['melee_armour']))
        print(unit_1['name'] + ' is victorious, with ' + str(health1) + ' health remaining' )
    elif ttk(unit_2, unit_1) > ttk(unit_1, unit_2):
        health2 = unit_2['health'] - (((ttk(unit_1, unit_2) - (ttk(unit_1, unit_2) % unit_1['rof']))/unit_1['rof'] + 1) * (unit_1['melee_damage'] + bonus(unit_2,unit_1) - unit_2['melee_armour']))
        print(unit_2['name'] + ' is victorious, with ' + str(health2) + ' health remaining')
    else:
        print('Draw')

fight(knight, camel_rider)

