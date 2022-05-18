from asyncio.windows_events import NULL


races = [
        [1, 'Dwarf', 3, 2],
        [2, 'Elf', 2, 2],
        [3, 'Halfling', 2, 2],
        [4,'Human', (1,2,3,4,5,6), 1],
        [5, 'Dragonborn', (1,6), (2,1)],
        [6, 'Gnome', 4, 2],
        [7, 'Half-Elf', 6, 2],
        [8, 'Half-Orc', (1, 3), (2,1)],
        [9, 'Tiefling', (4, 6), (1, 2)]
        ]

classes = [
        [1, 'Barbarian', 1, '1d12', (12, 3), ], 
        [2, 'Bard', 6, ], 
        [3, 'Cleric', 5],
        [4, 'Druid', 5],
        [5, 'Fighter', (1, 2)],
        [6, 'Monk', (2, 5)],
        [7, 'Paladin', (1, 6)],
        [8, 'Ranger', (2, 5)],
        [9, 'Rogue',2],
        [10, 'Sorcerer', 6],
        [11, 'Warlock', 6],
        [12, 'Wizard', 4]
        ]

ability_score = [
        [1, 'Strength', (1, 5, 7)],
        [2, 'Dexterity', (6, 8, 9)],
        [3, 'Consitution', (1,2,3,4,5,6,7,8,9,10,11,12)],
        [4, 'Intelligence',12],
        [5, 'Wisdom', (3, 4)],
        [6, 'Charisma', (2, 10, 11)]
        ]

skills = [
        [1, 'Acrobatics', 2],
        [2, 'Animal Handling' 5],
        [3, 'Arcana', 4],
        [4, 'Deception', 6],
        [5, 'History', 4],
        [6, 'Insight', 5],
        [7, 'Intimidation', 6],
        [8, 'Investigation', 4],
        [9, 'Medicine', 5],
        [10, 'Nature', 4],
        [11, 'Perception', 5],
        [12, 'Performance', 6],
        [13, 'Persuasion', 6],
        [14, 'Religion', 4],
        [15, 'Slight of Hand', 2],
        [16, 'Stealth', 2],
        [17, 'Survival', 5]
]
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

tools = []