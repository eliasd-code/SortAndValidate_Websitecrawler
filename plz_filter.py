import csv
import unicodecsv

# Liste der erlaubten PLZ-Präfixe
erlaubte_plz_prefixe = ['68', '69', '70', '71', '72', '75', '76', '77', '78', '79']

eingabe_datei = 'clean_adr5.csv'
ausgabe_datei = 'clean_adr6.csv'


def ist_erlaubte_plz(plz):
    # Überprüfe, ob die ersten beiden Ziffern der PLZ in der erlaubten Liste sind
    return plz[:2] in erlaubte_plz_prefixe

with open(eingabe_datei, 'rb') as eingabe, open(ausgabe_datei, 'wb') as ausgabe:
    csv_reader = unicodecsv.reader(eingabe, delimiter=';', encoding='utf-8')
    csv_writer = unicodecsv.writer(ausgabe, delimiter=';', encoding='utf-8')

    for row in csv_reader:
        # Überprüfe, ob die PLZ erlaubt ist (nach dem dritten ";" in der Liste)
        if len(row) > 2 and ist_erlaubte_plz(row[2]):
            csv_writer.writerow(row)

print("Zeilen mit nicht erlaubten PLZ wurden entfernt. Die gefilterte Datei wurde als '{}' gespeichert.".format(ausgabe_datei))
