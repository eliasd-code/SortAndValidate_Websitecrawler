# Elias Dafkov  15.02.2022

import os
import datetime
import getpass
os.system('clear')

# Sehr wichtige farben
class bcolors:
    RESET = '\033[0m' #RESET COLOR
    GREEN = '\033[92m' #GREEN
    YELLOW = '\033[93m' #YELLOW
    RED = '\033[91m' #RED
    CYAN = '\033[96m'

# Exakte Duplikate Sortieren CODE 1
def sortDuplicate():

    print()
    print('### '+bcolors.CYAN+'Exakte Duplikate Sortieren'+bcolors.RESET+' ###')

    sortedSet = set()

    while True:
        print('Gebe die zu Sortierende Datei ein')
        fileToSort = input('>> ')
        if os.path.exists(fileToSort) == False:
            print(bcolors.RED+'[!] Datei wurde nicht gefunden: '+bcolors.RESET+''+fileToSort)
            print()
            continue
        print(bcolors.GREEN+'[+] Datei wurde gefunden: '+bcolors.RESET+''+fileToSort)

        print('Gebe den Namen der output Datei ein')
        fileOutputSorted = input('>> ')
        if os.path.exists(fileOutputSorted):
            print(bcolors.RED+'[!] Achtung!')
            print('[i] Die Datei: '+bcolors.RESET+''+fileOutputSorted+''+bcolors.RED+' Existiert bereits in deinem Verzeichnis!')
            print('[!] Alle Daten werden überschrieben!'+bcolors.RESET)
            print('Fortfahren ? y/n')
            x = input('>> ')
            if x != 'y':
                exit()
        break

    print()
    print('Beginne..')
    print("Öffne "+fileToSort+" ..")
    print()
    now = datetime.datetime.now()
    startTime= now.strftime('%d.%m.%Y %H:%M Uhr')

    # Datei öffnen und set hinzufügen
    with open(fileToSort, 'r', encoding='utf-8') as infile:
        for element in infile:
            sortedSet.add(element)

    infile.close()
    infile = False
    element = False

    print(bcolors.GREEN+'[+] Daten wurden Sortiert.'+bcolors.RESET)
    print('[i] Schreibe Daten in "'+fileOutputSorted+'" ..')
    with open(fileOutputSorted, 'w', encoding='utf-8') as infile:
        for element in sortedSet:
            infile.write(element)
    print(bcolors.GREEN+'[+] Daten wurden geschrieben'+bcolors.RESET)
    print()
    print("[i] Start time: "+startTime)
    now = datetime.datetime.now()
    print("[i] End time: "+now.strftime('%d.%m.%Y %H:%M Uhr'))
    print("[i] Datas saved in -> "+bcolors.YELLOW+''+fileOutputSorted+''+bcolors.RESET)
    print(bcolors.GREEN+"[+] finished"+bcolors.RESET)

# Datei nach PLZ Sortieren CODE 3
def sortAfterPLZ():

    print()
    print('### '+bcolors.CYAN+'Datei nach PLZ Sortieren'+bcolors.RESET+' ###')

    while True:
        print('Gebe die zu Sortierende Datei ein')
        fileToSort = input('>> ')
        if os.path.exists(fileToSort) == False:
            print(bcolors.RED+'Datei wurde nicht gefunden: '+bcolors.RESET+''+fileToSort)
            print()
            continue
        print(bcolors.GREEN+'Zu sortierende Datei wurde wurde gefunden: '+bcolors.RESET+''+fileToSort)
        print()

        print('Gebe die PLZ Word list ein')
        plzWordList = input('>> ')
        if os.path.exists(plzWordList) == False:
            print(bcolors.RED+'Datei wurde nicht gefunden: '+bcolors.RESET+''+plzWordList)
            print()
            continue
        print(bcolors.GREEN+'PLZ Wordlist wurde gefunden: '+bcolors.RESET+''+plzWordList)
        print()

        print('Gebe den Namen der output Datei ein')
        fileOutputSorted = input('>> ')
        if os.path.exists(fileOutputSorted):
            print(bcolors.RED+'[!] Achtung!')
            print('[i] Die Datei: '+bcolors.RESET+''+fileOutputSorted+''+bcolors.RED+' Existiert bereits in deinem Verzeichnis!')
            print('[!] Alle Daten werden überschrieben!'+bcolors.RESET)
            print('Fortfahren ? y/n')
            x = input('>> ')
            if x != 'y':
                exit()
        break

    print()
    print('Beginne..')
    print("Öffne Dateien ..")
    print()
    now = datetime.datetime.now()
    startTime= now.strftime('%d.%m.%Y %H:%M Uhr')

    plzList = []
    # Datei öffnen und set hinzufügen
    print('Schreibe PLZ in Liste')
    with open(plzWordList, 'r', encoding='utf-8') as infile:
        for element in infile:
            element = element.strip('\n')
            plzList.append(element)
    infile.close()
    infile = False
    element = False


    writeInOutput = open(fileOutputSorted,'w')
    # open output File !!! open(fileFromUser,'w')
    with open(fileToSort, 'r', encoding='utf-8') as infile:
        for element in infile:
            for plz in plzList:
                if element.find(';'+plz+';') != -1:
                    writeInOutput.write(element)
                    break

    writeInOutput.close()

    print(bcolors.GREEN+'[+] Daten wurden geschrieben'+bcolors.RESET)
    print()
    print("[i] Start time: "+startTime)
    now = datetime.datetime.now()
    print("[i] End time: "+now.strftime('%d.%m.%Y %H:%M Uhr'))
    print("[i] Datas saved in -> "+bcolors.YELLOW+''+fileOutputSorted+''+bcolors.RESET)
    print(bcolors.GREEN+"[+] finished"+bcolors.RESET)

def sortLightAdresses():
    print()
    print('### '+bcolors.CYAN+'Leichte Adress Duplikate Sortieren'+bcolors.RESET+' ###')

    sortedSet = set()

    while True:
        print('Gebe die zu Sortierende Datei ein')
        fileToSort = input('>> ')
        if os.path.exists(fileToSort) == False:
            print(bcolors.RED+'[!] Datei wurde nicht gefunden: '+bcolors.RESET+''+fileToSort)
            print()
            continue
        print(bcolors.GREEN+'[+] Datei wurde gefunden: '+bcolors.RESET+''+fileToSort)

        print('Gebe den Namen der output Datei ein')
        fileOutputSorted = input('>> ')
        if os.path.exists(fileOutputSorted):
            print(bcolors.RED+'[!] Achtung!')
            print('[i] Die Datei: '+bcolors.RESET+''+fileOutputSorted+''+bcolors.RED+' Existiert bereits in deinem Verzeichnis!')
            print('[!] Alle Daten werden überschrieben!'+bcolors.RESET)
            print('Fortfahren ? y/n')
            x = input('>> ')
            if x != 'y':
                exit()
        break

    print()
    print('Beginne..')
    print("Öffne "+fileToSort+" ..")
    print()
    now = datetime.datetime.now()
    startTime= now.strftime('%d.%m.%Y %H:%M Uhr')

    # Datei öffnen und set hinzufügen
    with open(fileToSort, 'r', encoding='utf-8') as infile:
        for element in infile:
            sortedSet.add(element)

    infile.close()
    infile = False
    element = False

    print(bcolors.GREEN+'[+] Daten wurden Sortiert.'+bcolors.RESET)
    print('[i] Schreibe Daten in "'+fileOutputSorted+'" ..')
    with open(fileOutputSorted, 'w', encoding='utf-8') as infile:
        for element in sortedSet:
            infile.write(element)
    print(bcolors.GREEN+'[+] Daten wurden geschrieben'+bcolors.RESET)
    print()
    print("[i] Start time: "+startTime)
    now = datetime.datetime.now()
    print("[i] End time: "+now.strftime('%d.%m.%Y %H:%M Uhr'))
    print("[i] Datas saved in -> "+bcolors.YELLOW+''+fileOutputSorted+''+bcolors.RESET)
    print(bcolors.GREEN+"[+] finished"+bcolors.RESET)

# Menü
print('Adressen Sortieren...')
while True:
    print()
    print('Hier die Karte '+bcolors.CYAN+getpass.getuser()+bcolors.RESET+'..')
    print('--------------------------'+bcolors.YELLOW+'Speißekarte'+bcolors.RESET+'--------------------------')
    print(bcolors.CYAN+'Wähle eine von den Folgenden Speißen'+bcolors.RESET)
    print('0 = Exit')
    print('1 = Exakte Duplikate Sortieren')
    print('2 = Leichte Adress Duplikate Sortieren (Nur .CSV)')
    print('3 = Datei nach PLZ Sortieren (Nur .CSV + PLZ Liste)')
    print('---------------------------------------------------------------')
    userInput = input('>> ')
    if userInput == '0':
        print(bcolors.RED+'Exit'+bcolors.RESET+'..')
        break
    elif userInput == '1':
        os.system('clear')
        sortDuplicate()
    elif userInput == '2':
        os.system('clear')
        sortLightAdresses()
    elif userInput == '3':
        os.system('clear')
        sortAfterPLZ()
