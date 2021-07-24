import os
import time
import backend
import platform
import datetime

class bc:
    G = '\033[92m' #GREEN
    Y = '\033[93m' #YELLOW
    R = '\033[91m' #RED
    A = '\033[0m' #RESET COLOR


def CONTACT_PROGRAM_ENTIRE_PROGRAM():

    if os.path.isfile("log_status.txt") == True:
        pass
    else:
        with open("log_status.txt", 'w') as file:
            file.write("on")

    try:
        filelogs1 = open("log_status.txt", "r")
        logs = filelogs1.read()
        filelogs1.close()
    except Exception as e:
        print(f'{bc.R}\nError has occurred: {e}{bc.A}')
    
    if os.path.isfile("log.txt") == True:
        pass
    else:
        file = open("log.txt", "w")
        file.write(f'\n{datetime.datetime.now()} - Log File Created')
        if logs == "on":
            file.write(f'\nLogging is enabled')
        else:
            file.write(f'\nLogging is disabled')
        file.close()
    

    def CLEAR_L():
        clear = "clear"
        if platform.system() == 'Windows':
            clear = "cls"
        os.system(clear)
        print(f'{datetime.datetime.now()} - Cleared Screen')

        if logs == "on":
            file = open("log.txt", "a+")
            file.write(f'\n{datetime.datetime.now()} - Cleared Screen')
            file.close()
        else:
            pass

    def CLEAR_NL():
        clear = "clear"
        if platform.system() == 'Windows':
            clear = "cls"
        os.system(clear)


    # WORD LIST AREA --------------------

    # new
    new_wl = ["new", "newcontact", "new contact", "create", "add", "addnew", "add new", "create new"]
    # view
    view_wl = ["view", "list", "show", "showall", "show all", "list all", "listall", "viewall", "view all"]
    # delete
    del_wl = ["delete", "del", "remove", "erase"]
    # search
    search_wl = ["search", "find", "lookup"]
    # cls
    cls_wl = ["clear", "cls", "clearconsole", "clear console"]
    # switch log on
    logson_wl = ["logon", "log on", "enable log", "logenable", "log enable", "onlog", "logon"]
    # switch log off
    logsoff_wl = ["logoff", "log off", "disable log", "logdisable", "log disable", "offlog", "logoff"]
    # save to file - txt
    save_file_wl = ["save to file", "make file", "save", "file", "text", "make text", "create", "output", "save all", "saveall", "txt"]
    # save to file - csv
    csv_file_wl = ["csv", "comma separated values", "comma separated value", "spreadsheet"]
    # help
    help_wl = ["help", "how", "how to", "support"]

    # PROGRAM STARTS HERE ---------------

    backend.connect()

    main_choice = input(f'\n+ What to do?: ')

    if logs == "on":
        file = open("log.txt", "a")
        file.write(f'\n{datetime.datetime.now()} - Entered command: {main_choice}')
        file.close()
    else:
        pass
    
    if main_choice.lower() in new_wl:
        CLEAR_NL()
        # namei = "hirusha"
        # numberi = "0710758322"
        try:
            namei = input(f'{bc.Y}+ Name: {bc.A}')
            numberi = input(f'{bc.Y}+ Number: {bc.A}')
            backend.insert(namei.lower(), numberi.lower())
            print(f'\n{bc.G}+ Added: {namei.lower()} - {numberi.lower()} to the database{bc.A}')

            if logs == "on":
                file = open("log.txt", "a")
                file.write(f'\n{datetime.datetime.now()} - Added: {namei.lower()} - {numberi.lower()} to the database')
                file.close()
            else:
                pass

        except Exception as e:
            print(f'{bc.R}\nError has occurred: {e}{bc.A}')
    
    elif main_choice.lower() in view_wl:
        CLEAR_NL()
        fc = backend.view()
        for i in fc:
            print(f'{i[0]} -- {i[1]} -- {i[2]}')

        if logs == "on":
            file = open("log.txt", "a")
            file.write(f'\n{datetime.datetime.now()} - Listed all contacts')
            file.close()
        else:
            pass
    
    elif main_choice.lower() in save_file_wl:
        CLEAR_NL()
        fc = backend.view()

        fileout = open("saved_text.txt", "w+")
        for i in fc:
            fileout.write(f'\n{i[0]} -- {i[1]} -- {i[2]}')
        fileout.close()

        if logs == "on":
            file = open("log.txt", "a")
            file.write(f'\n{datetime.datetime.now()} - Saved all contacts to a text file')
            file.close()
        else:
            pass
    
    elif main_choice.lower() in csv_file_wl:
        CLEAR_NL()
        fc = backend.view()

        fileout = open("saved_csv.csv", "w+")
        fileout.write(f'ID,Name,Number')
        for i in fc:
            fileout.write(f'\n{i[0]},{i[1]},{i[2]}')
        fileout.close()

        if logs == "on":
            file = open("log.txt", "a")
            file.write(f'\n{datetime.datetime.now()} - Saved all contacts to a csv file')
            file.close()
        else:
            pass

    elif main_choice.lower() in del_wl:
        CLEAR_NL()
        try:
            print(r"""
             _____       _      _       
             |  __ \     | |    | |      
             | |  | | ___| | ___| |_ ___ 
             | |  | |/ _ \ |/ _ \ __/ _ \
             | |__| |  __/ |  __/ |_  __/
             |_____/ \___|_|\___|\__\___|

Use command 'view' to show all the Names, Numbers and ID""")

            idfi = input(f"\n{bc.Y}+ Enter the ID: {bc.A}")
            backend.delete(idfi)
            print(f'{bc.Y}+ Successfully deleted the contact with ID: {idfi}{bc.A}')

            if logs == "on":
                file = open("log.txt", "a")
                file.write(f'\n{datetime.datetime.now()} - Deleted the contact with ID: {idfi}')
                file.close()
            else:
                pass
        except Exception as e:
            print(f'{bc.R}\nError has occurred: {e}{bc.A}')
    
    elif main_choice.lower() in search_wl:
        CLEAR_NL()
        namefi = input(f"{bc.Y}+ Name: {bc.A}")
        numberfi = input(f"{bc.Y}+ Number: {bc.A}")

        result = backend.search(name=namefi.lower(), number=numberfi)
        if result == []:
            print(f'{bc.R}\nNo results found!{bc.A}')
            log_finds = "No results found"
        else:
            for i in result:
                print(f'\nID: {i[0]}\nName: {i[1]}\nNumber: {i[2]}')
            log_finds = "Found results"


        if logs == "on":
            file = open("log.txt", "a")
            file.write(f'\n{datetime.datetime.now()} - Searched for {namefi.lower()} - {numberfi} --- {log_finds}')
            file.close()
        else:
            pass
    
    elif main_choice.lower() in cls_wl:
        CLEAR_L()
    
    elif main_choice.lower() in logsoff_wl:
        try:
            filelogs2 = open("log_status.txt", "w")
            filelogs2.write("off")
            filelogs2.close()
            print(f'+ Disabled Logging!')

            if logs == "on":
                file = open("log.txt", "a")
                file.write(f'\n{datetime.datetime.now()} - Disabled Logging')
                file.close()
            else:
                pass

        except Exception as e:
            print(f'{bc.R}\nError has occurred: {e}{bc.A}')
    
    elif main_choice.lower() in logson_wl:
        try:
            filelogs2 = open("log_status.txt", "w")
            filelogs2.write("on")
            filelogs2.close()
            print(f'+ Enabled Logging!')

            if logs == "on":
                file = open("log.txt", "a")
                file.write(f'\n{datetime.datetime.now()} - Enabled Logging')
                file.close()
            else:
                pass

        except Exception as e:
            print(f'{bc.R}\nError has occurred: {e}{bc.A}')
        
    elif main_choice.lower() in help_wl:
        try:
            print(f'''{bc.Y}
new --> Create a new contact
view --> Show all the saved contacts
delete --> Delete contact with ID
find --> Search for a contact 
( with name and number, hit enter if you dont know )
logon --> Enable Logging (you can do this manually too)
logogg --> Disable Logging (you can do this manually too)
save --> Save the contacts to a text file in a readable format
help --> show this!
{bc.A}''')
            if logs == "on":
                file = open("log.txt", "a")
                file.write(f'\n{datetime.datetime.now()} - Showing Help')
                file.close()
            else:
                pass
        except Exception as e:
            print(f'{bc.R}\nError has occurred: {e}{bc.A}')

    else:
        print(f"{bc.R}- Command not found!{bc.A}")
        time.sleep(2)
        CLEAR_NL()
        CONTACT_PROGRAM_ENTIRE_PROGRAM()


if __name__ == '__main__':
    try:
        try:
            filelogs1 = open("log_status.txt", "r")
            logs = filelogs1.read()
            filelogs1.close()
        except Exception as e:
            print(f'{bc.R}\nError has occurred: {e}{bc.A}')

        if logs == "on":
            file = open("log.txt", "a")
            file.write(f'\n{datetime.datetime.now()} - Opened the program!')
            file.close()
        else:
            pass
        while True:
            CONTACT_PROGRAM_ENTIRE_PROGRAM()
    except Exception as e:
        print(f'An Error has occured: {e}')
    finally:
        try:
            filelogs1 = open("log_status.txt", "r")
            logs = filelogs1.read()
            filelogs1.close()
        except Exception as e:
            print(f'{bc.R}\nError has occurred: {e}{bc.A}')

        if logs == "on":
            file = open("log.txt", "a")
            file.write(f'\n{datetime.datetime.now()} - Program Closed')
            file.close()
        else:
            pass













