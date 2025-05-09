import tempfile
import os
from app.file_handler import File_Handler

def test_find_file():

    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as temp_csv:
        temp_csv.write(b"old_id,new_id\nOLD1,NEW1\nOLD2,NEW2")
        temp_csv_path = temp_csv.name

    try:
        file_handler = File_Handler()
        data = file_handler.get_file(path=temp_csv_path)

        assert data is not None
    finally:
        os.remove(temp_csv_path)
