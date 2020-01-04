
import datetime
    
datetime_object = datetime.datetime.now()   
datetime_object = datetime_object.strftime("%d/%m/%Y, %H:%M:%S")

def save_journal_entry(entry):
    my_file = open("/Users/elliotstjernqvist/Dokument/Skola/Programmering_1/Python/excercises/my_journal.txt","a")#append mode 
    my_file.write(entry +  "\n") 
    my_file.close() 
    if __name__ == "__main__":
        print("Your entry system has started")

save_journal_entry("Today was a day, moms spaghetti" + " " + datetime_object )