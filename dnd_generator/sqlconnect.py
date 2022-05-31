import sqlite3
import data_import_functions as dif
import character_data as cd


conn = sqlite3.connect('dnd_db.sqlite3')
curs = conn.cursor()

def execute_query(curs, query):
    return curs.execute(query)

if __name__ == "__main__":
    execute_query(curs, dif.create_races_table)
    execute_query(curs, dif.create_classes_table)
    execute_query(curs, dif.create_ability_score_table)
    execute_query(curs, dif.create_skills_table)
    dif.populate_races_table(curs, conn)
    dif.populate_classes_table(curs, conn)
    dif.populate_ability_score_table(curs, conn)
    dif.populate_skills_table(curs, conn)
    conn.close()