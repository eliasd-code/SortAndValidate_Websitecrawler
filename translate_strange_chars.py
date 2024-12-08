import csv
import unicodecsv

def ersetze_sonderzeichen(text):
    ersetzungen = {
        'Ã¼': 'ü',
        'Ã¤': 'ä',
        'Ã¶': 'ö',
        'ÃŸ': 'ß',
        'Ã–': 'Ö',
        'Ãœ': 'Ü',
        'Ã„': 'Ä',
        'Ã¨': 'è',
        'Ã©': 'é',
    }
    for ersetzung in ersetzungen:
        text = text.replace(ersetzung, ersetzungen[ersetzung])
    return text


eingabe_datei = 'clean_adr3.csv'
ausgabe_datei = 'clean_adr4.csv'

with open(eingabe_datei, 'rb') as eingabe, open(ausgabe_datei, 'wb') as ausgabe:
    csv_reader = unicodecsv.reader(eingabe, delimiter='\t', encoding='utf-8')

    csv_writer = unicodecsv.writer(ausgabe, delimiter='\t', encoding='utf-8')

    for row in csv_reader:
        bereinigte_row = [ersetze_sonderzeichen(cell) for cell in row]
        csv_writer.writerow(bereinigte_row)

print("Sonderzeichen wurden erfolgreich ersetzt. Die bereinigte Datei wurde als '{}' gespeichert.".format(ausgabe_datei))
