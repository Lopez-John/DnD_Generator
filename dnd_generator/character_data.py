
from asyncio.windows_events import NULL


races = [
        [1, 'Dwarf', '3', '2'],
        [2, 'Elf', '2', '2'],
        [3, 'Halfling', '2', '2'],
        [4,'Human', '1,2,3,4,5,6', '1'],
        [5, 'Dragonborn', '1,6', '2,1'],
        [6, 'Gnome', '4', '2'],
        [7, 'Half-Elf', '6', '2'],
        [8, 'Half-Orc', '1, 3', '2,1'],
        [9, 'Tiefling', '4, 6', '1,2']
        ]

classes = [
        [1, 'Barbarian', '1', 5, 12, '1,2,4'], 
        [2, 'Bard', '6', 3, 8, '1'], 
        [3, 'Cleric', '5', 3, 8, '1,2,4'],
        [4, 'Druid', '5', 3, 8, '1,2,4'],
        [5, 'Fighter', '1,2', 4, 10, '1,2,3,4'],
        [6, 'Monk', '2,5', 3, 8, 'NULL'],
        [7, 'Paladin', '1,6', 4, 10, '1,2,3,4'],
        [8, 'Ranger', '2,5', 4, 10, '1,2,4'],
        [9, 'Rogue', '2', 3, 8, '1'],
        [10, 'Sorcerer', '6', 2, 6, 'NULL'],
        [11, 'Warlock', '6', 3, 8, '1'],
        [12, 'Wizard', '4', 2, 6,  'NULL']
        ]

ability_score = [
        [1, 'Strength', '1,5,7'],
        [2, 'Dexterity', '6,8,9'],
        [3, 'Consitution', '1,2,3,4,5,6,7,8,9,10,11,12'],
        [4, 'Intelligence','12'],
        [5, 'Wisdom', '3,4'],
        [6, 'Charisma', '2,10,11']
        ]

skills = [
        [1, 'Acrobatics', 2],
        [2, 'Animal Handling', 5],
        [3, 'Arcana', 4],
        [4, 'Athletics', 1],
        [5, 'Deception', 6],
        [6, 'History', 4],
        [7, 'Insight', 5],
        [8, 'Intimidation', 6],
        [9, 'Investigation', 4],
        [10, 'Medicine', 5],
        [11, 'Nature', 4],
        [12, 'Perception', 5],
        [13, 'Performance', 6],
        [14, 'Persuasion', 6],
        [15, 'Religion', 4],
        [16, 'Slight of Hand', 2],
        [17, 'Stealth', 2],
        [18, 'Survival', 5]
]