import csv
import unicodecsv

def ist_gueltige_plz(plz):
    # Überprüfe, ob die PLZ eine Zahl mit genau fünf Stellen ist
    return plz.isdigit() and len(plz) == 5

eingabe_datei = 'clean_adr.csv'
ausgabe_datei = 'clean_adr_without_no_plz.csv'

with open(eingabe_datei, 'rb') as eingabe, open(ausgabe_datei, 'wb') as ausgabe:
    csv_reader = unicodecsv.reader(eingabe, delimiter=';', encoding='utf-8')
    csv_writer = unicodecsv.writer(ausgabe, delimiter=';', encoding='utf-8')

    for row in csv_reader:
        # Überprüfe, ob die PLZ gültig ist (nach dem dritten ";" in der Liste)
        if len(row) > 3 and ist_gueltige_plz(row[2]):
            csv_writer.writerow(row)

print("Zeilen ohne gültige PLZ wurden entfernt. Die bereinigte Datei wurde als '{}' gespeichert.".format(ausgabe_datei))
