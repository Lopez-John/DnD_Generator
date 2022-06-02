import items_data as id

def execute_query(curs, query):
    return curs.execute(query)

create_armor_types_table = '''
    CREATE TABLE IF NOT EXISTS armor_types(
        armor_type_id SERIAL NOT NULL PRIMARY KEY,
        armor_type VARCHAR(15) NOT NULL,
        armor_id VARCHAR(10) NOT NULL,
        don_time NUMERIC,
        doff_time NUMERIC
    );
'''
create_armor_table = '''
    CREATE TABLE IF NOT EXISTS armor(
        armor_id SERIAL NOT NULL PRIMARY KEY,
        armor VARCHAR(20) NOT NULL,
        cost NUMERIC NOT NULL,
        strength_needed NUMERIC,
        stealth NUMERIC,
        weight NUMERIC NOT NULL
    );
'''

create_tools_table = '''
    CREATE TABLE IF NOT EXISTS tools(
        tool_id SERIAL NOT NULL PRIMARY KEY,
        tool VARCHAR(25) NOT NULL,
        cost FLOAT
    )
'''