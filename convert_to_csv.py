import csv


with open('unzipped_files/TNVED1.TXT', 'rt', encoding='cp866') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(';') for line in stripped if line)
    with open('converted_to_csv/TNVED1.csv', 'w', encoding='ANSI') as out_file:
        writer = csv.writer(out_file)
        writer.writerows(lines)


with open('unzipped_files/TNVED2.Txt', 'rt', encoding='cp866') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(';') for line in stripped if line)
    with open('converted_to_csv/TNVED2.csv', 'w', encoding='ANSI') as out_file:
       writer = csv.writer(out_file)
       writer.writerows(lines)
       

with open('unzipped_files/TNVED3.Txt', 'rt', encoding='cp866') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(';') for line in stripped if line)
    with open('converted_to_csv/TNVED3.csv', 'w', encoding='ANSI') as out_file:
       writer = csv.writer(out_file)
       writer.writerows(lines)
       

with open('unzipped_files/TNVED4.Txt', 'rt', encoding='cp866') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(';') for line in stripped if line)
    with open('converted_to_csv/TNVED4.csv', 'w', encoding='ANSI') as out_file:
       writer = csv.writer(out_file)
       writer.writerows(lines)
