import csv


class FileHandler:
    def get_file(self, path: str):
        with open(path, mode='r') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
        return data
