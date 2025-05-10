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
        raw = self.get_file(path)
        old_to_new_ids = []

        for row in raw[1:]:
            old_to_new_ids.append(
                OldToNewId(old=row[0], new=row[1])
            )

        return old_to_new_ids


class OldToNewId:
    def __init__(self, old: str, new: str):
        self.old = old
        self.new = new
