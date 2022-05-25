from asyncio.windows_events import NULL


armor_types = [
        [1, 'Light Armor', (1,2,3), 1, 1],
        [2, 'Medium Armor',(4,5,6,7,8), 5, 1],
        [3, 'Heavy Armor', (9,10,11,12), 10, 5],
        [4, 'Shield', 13, NULL, NULL]
]
armor = [
        [1, 'Padded', 5, NULL, 1, 8],
        [2, 'Leather', 10, NULL, 0, 10],
        [3, 'Studded Leather', 45, NULL, 0, 13],
        [4, 'Hide', 10, NULL, 0, 12],
        [5, 'Chain Shirt', 50, NULL, 0, 20],
        [6, 'Scale Mail', 50, NULL, 1, 45],
        [7, 'Breast Plate', 400, NULL, 0, 20],
        [8, 'Half Plate', 750, NULL, 1, 40],
        [9, 'Ring Mail', 30, NULL, 1, 40],
        [10, 'Chain Mail', 75, 13, 1, 55],
        [11, 'Splint', 200, 15, 1, 60],
        [12, 'Plate', 1500, 15, 1, 65],
        [13, 'Shield', 10, NULL, NULL, 6]
]

tools = [
        [1, 'Alchemist Supplies', 10.0, 8.0],
        [2, 'Brewer Supplies', 20.0, 9.0],
        [3, 'Calligrapher Supplies', 10.0, 5.0],
        [4, 'Cartographer Tools', 8.0, 6.0],
        [5, 'Cobbler Tools', 5.0, 5.0],
        [6, 'Cook Utensils', 1.0, 8.0],
        [7, 'Glassblower Tools', 30.0, 5.0],
        [8, 'Jewler Tools', 25.0, 2.0],
        [9, 'Leatherworker Tools', 5.0, 5.0],
        [10, 'Mason Tools', 10.0, 8.0],
        [11, 'Painter Tools', 10.0, 5.0],
        [12, 'Potter Tools', 10.0, 3.0],
        [13, 'Smith Tools', 20.0, 8.0],
        [14, 'Tinker Tools', 50.0, 10.0],
        [15, 'Weaver Tools', 1.0, 5.0],
        [16, 'Woodcarver Tools', 1.0, 5.0],
        [17, 'Disguise Kit', 25.0, 3.0],
        [18, 'Forgery Kit', 15.0, 5.0],
        [19, 'Dice Set', 0.1, 0.0],
        [20, 'Dragonchess set', 1.0, 0.5],
        [21, 'Playing Card Set', 5.0, 0.0],
        [22, 'Three-Dragon Ante Set', 1, 0.0],
        [23, 'Herbalism Kit', 5.0, 3.0],
        [24, 'Bagpipes', 30.0, 6.0],
        [25, 'Drum', 6.0, 3.0],
        [26, 'Dulcimer', 25.0, 10.0],
        [27, 'Flute', 2.0, 1.0],
        [28, 'Lute', 35.0, 2.0],
        [29, 'Lyre', 30.0, 2.0],
        [30, 'Horn', 3.0, 2.0],
        [31, 'Pan Flute', 12.0, 2.0],
        [32, 'Shawm', 2.0, 1.0],
        [33, 'Viol', 30.0, 1.0],
        [34, 'Navigator Tools', 25.0, 2.0],
        [35, 'Poisoner Tools', 50.0, 2.0],
        [36, 'Thieves Tools', 25.0, 1.0]
]

artisan_tools = [
                [1, 1],
                [2, 2], 
                [3, 3],
                [4, 4],
                [5, 5],
                [6, 6],
                [7, 7],
                [8, 8],
                [9, 9],
                [10, 10],
                [11, 11], 
                [12, 12],
                [13, 13],
                [14, 14],
                [15, 15],
                [16, 16]
]

gaming_set = [
        [1, 19],
        [2, 20],
        [3, 21],
        [4, 22]
]

musical_instruments = [
        [1, 24],
        [2, 25],
        [3, 26],
        [4, 27],
        [5, 28],
        [6, 29],
        [7, 30],
        [8, 31],
        [9, 32],
        [10, 33]
]
dice = [
    [1, 'd4'],
    [2, 'd6'],
    [3, 'd8'],
    [4, 'd10'],
    [5, 'd12'],
    [6, 'd20'],
    [7, 'd10 tens']
]
damage_type = [
    [1, 'Bludgeoning'],
    [2, 'Piercing'],
    [3, 'Slashing'],
]

weapon_properties = [
    [1, 'Light'],
    [2, 'Finesse'],
    [3, 'Thrown(range 20/60)'],
    [4, 'Thrown(range 30/120)'],
    [5, 'Two-Handed'],
    [6, 'Heavy'],
    [7, 'Reach'],
    [8, 'Special'],
    [9, 'Versatile (1d10)'],
    [10, 'Versatile(1d8)'],
    [11, 'Ammunition (range 80/320)'],
    [12, 'Ammunition (range 20/120)'],
    [13, 'Ammunition (range 25/100)'],
    [14, 'Ammunition (range 100/400'],
    [15, 'Ammunition (range 150/600)'],
    [16, 'Loading'],
    [17, 'Ammunition (range 30/120)'],
    [18, 'Throw(range 5/15)']
]

weapons = [
    [1, 'Club', 0.1, 1, 1, 1, 2.0, 1],
    [2, 'Dagger', 2.0, 1, 1, 2, 1.0, (2, 1, 3)],
    [3, 'Greatclub', 0.2, 1, 3, 1, 10.0, 5],
    [4, 'Handaxe', 5.0, 1, 2, 3, 2.0, (1, 3)],
    [5, 'Javelin', 5.0, 1, 2, 2, 2.0, 4],
    [6, 'Light Hammer', 2.0, 1, 1, 2.0, (1, 3)],
    [7, 'Mace', 5.0, 1, 1, 2.0, NULL],
    [8, 'Quarterstaff', 0.2, 1, 2, 4.0, 10],
    [9, 'Sickle', 1, 1, 1, 3, 2.0, 1],
    [10, 'Spear', 1, 1, 2, 2, 3.0, (3, 10)],
    [11, 'Crossbow, light', 25, 1, 3, 2, 5.0, (11, 15, 5)],
    [12, 'Dart', .01, 1, 1, 2, .25, (2, 3)],
    [13, 'Shortbow', 25, 1, 2, 2, 2, (11, 5)],
    [14, 'Sling', .1, 1, 1, 1, NULL, 17],
    [15, 'Battleaxe', 10, 1, 3, 3, 4, 9],
    [16, 'Flail', 10, 1, 3, 1, 1, NULL],
    [17, 'Glaive', 20, 1, 4, 3, 6, (6, 7, 5)],
    [18, 'Greataxe', 30, 1, 4, 3, 6, (6, 5)],
    [19, 'Greatsword', 50, 2, 2, 2, 6, (6,5)],
    [20, 'Halbard', 20, 1, 4, 3, 6, (7, 7, 5)],
    [21, 'Lance', 20, 1, 5, 3, 6, (7, 8)],
    [22, 'Longsword', 15, 1, 3, 3, 3, 9],
    [23, 'Maul', 10, 2, 2, 1, 10, (6, 5)],
    [24, 'Morningstar', 15, 1, 3, 2, 4, NULL],
    [25, 'Pike', 5, 1, 4, 2, 18, (6, 7, 5)],
    [26, 'Rapier', 25, 1, 3, 2, 2, 2],
    [27, 'Scimitar', 25, 1, 2, 3, 3, (2, 1)],
    [28, 'Shortsword', 10, 1, 2, 2, 2, (2, 1)],
    [29, 'Trident', 5, 1, 2, 2, 4, (3, 10)],
    [30, 'War Pick', 5, 1, 3, 2, 2, NULL],
    [31, 'Warhammer', 15, 1, 3, 1, 2, 9],
    [32, 'Whip', 2, 1, 1, 3, 3, (2, 7)],
    [33, 'Blowgun', 10, 1, NULL, 2, 1, (13, 16)],
    [34, 'Crossbow, hand', 75, 1, 2, 2, 3, (17, 1, 16)],
    [35, 'Crossbow, heavy', 50, 1, 4, 2, 18, (14, 6, 5)],
    [36, 'Longbow', 50, 1, 3, 2, 2, (15, 6, 5)],
    [37, 'Net', 1, NULL, NULL, NULL, 3, (8, 18)]
]

weapon_types = [
        [1, 'Simple Melee Weapons'],
        [2, 'Simple Ranged Weapons'],
        [3, 'Martial Melee Weapons'],
        [4, 'Martial Ranged Weapons']
]