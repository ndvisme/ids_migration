import csv


class FileHandler:

    def extract_data(self, path: str):
        if not path.endswith('.csv'):
            raise ValueError('Illegal input file type')
        pass

    def get_file(self, path: str):
        with open(path, mode='r') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
        return data
