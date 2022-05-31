import character_data as cd

def execute_query(curs, query):
    return curs.execute(query)

create_races_table = '''
    CREATE TABLE IF NOT EXISTS races(
        'races_id' SERIAL NOT NULL PRIMARY KEY,
        'race' VARCHAR(15) NOT NULL,
        'racial_buff' VARCHAR(15) NOT NULL,
        'ability_score_increase' VARCHAR(5) NOT NULL
    );
    '''

def populate_races_table(curs, conn):
    for row in cd.races:
        insert_statement = f'''INSERT INTO races
                                VALUES ({row[0]},
                                '{row[1]}',
                                '{row[2]}',
                                '{row[3]}');'''
        execute_query(curs, insert_statement)
        conn.commit()

create_classes_table = '''
    CREATE TABLE IF NOT EXISTS class(
        'class_id' SERIAL NOT NULL PRIMARY KEY,
        'class' VARCHAR(15) NOT NULL,
        'primary_ability' VARCHAR(5) NOT NULL,
        'hit_dice' NUMERIC NOT NULL,
        'first_level_base' NUMERIC NOT NULL,
        'armor' VARCHAR(10)
    );
    '''

def populate_classes_table(curs, conn):
    for row in cd.classes:
        insert_statement = f'''INSERT INTO class
                            VALUES ({row[0]},
                            '{row[1]}',
                            '{row[2]}',
                            {row[3]},
                            {row[4]},
                            '{row[5]}');
        '''
        execute_query(curs, insert_statement)
        conn.commit()

create_ability_score_table = '''
    CREATE TABLE IF NOT EXISTS ability_scores(
        'ability_id' SERIAL NOT NULL PRIMARY KEY,
        'ability' VARCHAR(15) NOT NULL,
        'important_for' VARCHAR(25) NOT NULL,
        FOREIGN KEY (important_for)
        REFERENCES ability_score(ability_id)
    );
'''

def populate_ability_score_table(curs, conn):
    for row in cd.ability_score:
        insert_statement = f'''INSERT INTO ability_scores
                            VALUES({row[0]},
                                    '{row[1]}',
                                    '{row[2]}')
        '''
        execute_query(curs, insert_statement)
        conn.commit()

create_skills_table = '''
    CREATE TABLE IF NOT EXISTS skills(
        'skill_id' SERIAL NOT NULL PRIMARY KEY,
        'skill' VARCHAR(20),
        'ability_id' NUMERIC,
        FOREIGN KEY (ability_id)
        REFERENCES ability_score(ability_id)
    );

'''

def populate_skills_table(curs, conn):
    for row in cd.skills:
        insert_statement = f'''INSERT INTO skills
                                VALUES({row[0]},
                                        '{row[1]}',
                                        {row[2]})
        '''
        execute_query(curs, insert_statement)
        conn.commit()