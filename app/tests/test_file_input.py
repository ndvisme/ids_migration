import tempfile
import pytest
import os
from typing import List
from app.file_handler import (
    DATA_STRUCTURE_ERR,
    ILLEGAL_FILE_TYPE,
    FileHandler,
    OldToNewId
)


def test_find_file():
    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as temp_csv:
        temp_csv.write(b"old_id,new_id\nOLD1,NEW1\nOLD2,NEW2")
        temp_csv_path = temp_csv.name
    try:
        file_handler = FileHandler()
        data = file_handler.get_file(path=temp_csv_path)

        assert data is not None
    finally:
        os.remove(temp_csv_path)


def test_file_type():
    file_name = 'test.txt'
    file_handler = FileHandler()

    with pytest.raises(ValueError) as exc_info:
        file_handler.extract_data(path=file_name)

    assert str(exc_info.value) == ILLEGAL_FILE_TYPE


def test_file_colums():
    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as temp_csv:
        temp_csv.write(b"old_ids,new_ids\nOLD1,NEW1\nOLD2,NEW2")
        csv_path = temp_csv.name

    handler = FileHandler()
    with pytest.raises(ValueError) as exc_info:
        handler.extract_data(csv_path)

    assert str(exc_info.value) == DATA_STRUCTURE_ERR


def test_extract_data():
    with tempfile.NamedTemporaryFile(delete=False, suffix='.csv') as temp_csv:
        temp_csv.write(b"old_id,new_id\nOLD1,NEW1\nOLD2,NEW2")
        csv_path = temp_csv.name
    try:
        handler = FileHandler()
        oldToNewIds: List['OldToNewId'] = handler.extract_data(path=csv_path)

        assert oldToNewIds[0].old == 'OLD1'
        assert oldToNewIds[0].new == 'NEW1'

        assert oldToNewIds[1].old == 'OLD2'
        assert oldToNewIds[1].new == 'NEW2'

    finally:
        os.remove(csv_path)
