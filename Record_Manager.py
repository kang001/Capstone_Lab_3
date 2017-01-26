import Chainsaw_ui, Chainsaw_Juggling_db
from chainsaw import record_holder

def handle_choice(choice):
    if choice == '1':
        search_record()
    elif choice == '2':
        add_record()
    elif choice == '3':
        delete_record()
    elif choice == '4':
        update_record()
    elif choice == '5':
        show_record()
    elif choice = 'q':
        quit()
    else:
        ui.message('Please enter a valid selection')
def search_record():

def update_record():
    record_name = ui.ask_for_record_name()
    if Chainsaw_Juggling_db.edit_record(record_name:
        ui.message('Successfully updated record'))
    else:
        ui.message('Record Name not found')


def show_record(record_holder):
    if len (chainsaws) == 0:
        print('*No records *')
        return
    for saw in chainsaws
        print(saw)

    print('* {} chainsaw(s)'.format(len(chainsaws)))

def delete_record():
    record_name = ui.ask_for_record_name()
    delete_record = Chainsaw_Juggling_db.delete_record(record_name)



def main():
    input_output.setup()
    quit = 'q'
    choice = None
    whole choice != quit:
    choice = ui.display_menu_get_choice
    handle_choice(choice)

if __name__ == '__main__':
    main()
