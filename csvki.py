import csv

lista = [1, 'Python', 'tomek']
mydict = [{'branch': 'COE', 'cgpa': '9.0',
           'name': 'Nikhil', 'year': '2'},
          {'branch': 'COE', 'cgpa': '9.1',
           'name': 'Sanchit', 'year': '2'},
          {'branch': 'IT', 'cgpa': '9.3',
           'name': 'Aditya', 'year': '2'},
          {'branch': 'SE', 'cgpa': '9.5',
           'name': 'Sagar', 'year': '1'},
          {'branch': 'MCE', 'cgpa': '7.8',
           'name': 'Prateek', 'year': '3'},
          {'branch': 'EP', 'cgpa': '9.1',
           'name': 'Sahil', 'year': '2'}]

fields = ['branch', 'cgpa', 'name', 'year']

with open('dane_csv22.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(mydict)

# with open('dane_csv.csv', 'w', newline='') as file:
#     writer = csv.writer(file, delimiter=',', dialect='excel')
#     writer.writerow(['id', 'jezyk', 'osoba'])
#     writer.writerow(lista)
#     writer.writerow([2, 'Java', 'piotr'])
#     writer.writerows([[3, 'Java', 'piotr'], [4, 'Java', 'piotr'], [5, 'Java', 'piotr'], [7, 'Java', 'piotr']])

# print(csv.list_dialects())
#
# with open("SampleCSVFile_119kb.csv", 'r') as file:
#     csv_file = csv.DictReader(file)
#     for r in csv_file:
#         print(dict(r))
#         print(dict(r).get('1'))
#
# with open("SampleCSVFile_119kb.csv", 'r') as file:
#     csv_file = csv.reader(file)
#     plik = list(csv_file)
#     for r in csv_file:
#         print(list(r))
#
# print(plik[0][1])
