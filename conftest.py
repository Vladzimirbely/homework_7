import os
import shutil
import pytest
from zipfile import ZipFile

files_path = os.path.join('tmp')
archive_path = os.path.join('resources')
archive = os.path.join(archive_path, 'archive.zip')

@pytest.fixture(scope='session', autouse=True)
def create_zip():
    if not os.path.exists(archive_path):
        os.mkdir(archive_path)

    with ZipFile(archive, 'w') as zf:
        for file in os.listdir(files_path):
            full_file_path = os.path.join(files_path, file)
            zf.write(full_file_path, os.path.basename(full_file_path))

    yield
    shutil.rmtree(archive_path)
