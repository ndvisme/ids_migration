import csv

DATA_STRUCTURE_ERR = "Expected two columns: [old_id] [new_id]"
ILLEGAL_FILE_TYPE = "Illegal input file type"


class FileHandler:

    def validate_file_type(self, path: str):
        if not path.endswith('.csv'):
            raise ValueError(ILLEGAL_FILE_TYPE)

    def validate_file_structure(self, path: str):
        raw = self.get_file(path)

        if raw[0][0] != 'old_id' or raw[0][1] != 'new_id':
            raise ValueError(DATA_STRUCTURE_ERR)

    def get_file(self, path: str):
        self.validate_file_type(path)

        with open(path, mode='r') as file:
            reader = csv.reader(file)
            data = [row for row in reader]

        return data

    def extract_data(self, path: str) -> list['OldToNewId']:
        raw = self.get_file(path)
        old_to_new_ids = []

        self.validate_file_structure(path)

        for row in raw[1:]:
            old_to_new_ids.append(
                OldToNewId(old=row[0], new=row[1])
            )

        return old_to_new_ids


class OldToNewId:
    def __init__(self, old: str, new: str):
        self.old = old
        self.new = new
