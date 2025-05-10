
from app.file_handler import OldToNewId
from app.db import update_app_instances


def test_update_app_instance(mocker):
    mock_conn = mocker.patch("psycopg2.connect")
    mock_cursor = mock_conn.return_value.cursor.return_value

    old_to_new_id = [OldToNewId(old="oldId", new="newId")]
    update_app_instances(old_to_new_id)

    mock_conn.assert_called_once_with(dbname='sightd', user='postgres', password='password', host='localhost', port=5432)
