import csv


class FileHandler:

    def validate_file_type(self, path: str):
        if not path.endswith('.csv'):
            raise ValueError('Illegal input file type')

    def get_file(self, path: str):
        self.validate_file_type(path)

        with open(path, mode='r') as file:
            reader = csv.reader(file)
            data = [row for row in reader]

        return data

    def extract_data(self, path: str) -> list['OldToNewId']:
        raw_data = self.get_file(path)

        extracted_data = [OldToNewId(old=row[0], new=row[1]) for row in raw_data[1:] if len(row) >= 2]

        return extracted_data


class OldToNewId:
    def __init__(self, old: str, new: str):
        self.old = old
        self.new = new
