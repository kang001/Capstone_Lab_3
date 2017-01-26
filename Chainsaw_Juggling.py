import sqlite3

try:
    db = sqlite3.connect('world_record_db.db')
    cur = db.cursor()
    cur.execute('create table Chainsaw_Juggling (record text, country text, number_of_catches int )')
    table_name1 = 'Chainsaw_Juggling'
    new_field = 'Record Holder'
    field_type = 'STRING'

    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()

except sqlite3.Error as e:
