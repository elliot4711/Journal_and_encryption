
from excercise_24 import save_journal_entry

def show_menu():
    ans = input("Would you like to add a new journal entry, view your latest yournal entry, or quit the program? " )
    if ans == "new":
        ans = input("What would you like to enter into your journal? ")
        save_journal_entry(ans)
    if ans == "view":
        f = open('my_journal.txt', 'r')
        file_contents = f.read()
        print(file_contents)
        f.close
    else:
        quit

show_menu()

