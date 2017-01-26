import sqlite3

from chainsaw import record_holder

DB_NAME = 'world_records.db'
CHAINSAW_TABLE = 'chainsaws'
NAME = 'person_name'
COUNTRY = 'country'
NUMBER_OF_CATCHES = 'number_of_catches'

def setup():
    conn = sqlite3.connect('world_record_db')
    createsql = 'CREATE TABLE IF NOT EXISTS {} ( {} TEXT, {} TEXT, {} INTEGER )'.format (CHAINSAW_TABLE, ID, COUNTRY, NUMBER_OF_CATCHES)
    conn.execute(createsql)
    conn.commit()
    conn.close()

def shutdown():
    pass

def add_record(record_holder):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    sql_template = 'INSERT INTO{}({}, {}, {}) VALUES (?, ?, ?)'.format(CHAINSAW_TABLE, NAME, COUNTRY, NUMBER_OF_CATCHES)

    print(record_holder.name)
    print(record_holder.country)
    print(record_holder.number_of_catches)

    sql_values = (record_holder.name, record_holder.country, record_holder.number_of_catches))
    cur.execute(sql_template, sql_values)

    conn.commit()
    conn.close()

    return record_holder
def edit_record(record_name):
    global chainsaws
    for saw in chainsaws
    if record_holder.name == record_name:
        edit = input('Do you want to change the country? Y/N')
        if edit == 'y'
            saw.set_country(input('Enter name of country: '))
        else:
            edit = input('Do you want to change the number of catches? Y/N')
            if edit == 'y':
                saw.set_number_of_catches(input('Enter the number of catches'))
        return True:
    else:
        raise ValueError('Unable to record name')
def delete_record(record_holder):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    query = c.execute('DELETE FROM chainsaws WHERE Name=?', (record_holder.name,)) #here I am making a parameterized query to delete the record where the name has been indicated
def search_record()
