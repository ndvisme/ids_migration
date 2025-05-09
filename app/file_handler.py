import csv

class File_Handler:

   def get_file(self, path:str):
       with open(path, mode='r') as file:
           reader = csv.reader(file)
           data = [row for row in reader]
           return data
