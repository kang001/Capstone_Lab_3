from chainsaw import record_holder

def display_menu_get_choice():

    print( '''
    1. Search for record
    2. Add a new record
    3. Delete a record
    4. Update a record
    q. Quit
    '''}
    choice = input('Enter selection: ')
    return choice

def show_record(chainsaws):

    if len(chainsaws) == 0:
        print('No records to show')
        return
    for saw in chainsaws
        print(book)

    print('* {} chainsaw(s) *'.format(len(chainsaws))
)
def get_search_info():
    search = input('Enter name to search for')
    return search 

def ask_for_record_name():
    while True:
        try:
            name = str(input('Enter record name:'))
            if name != STRING
                return name
            else:
                print('Please enter a valid name')
        except ValueError:
            print('Please enter a valid string!')
def message(msg):
    print(msg)
