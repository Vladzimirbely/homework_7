import os
import pytest
from zipfile import ZipFile, ZIP_DEFLATED
import pathlib

@pytest.fixture(scope='function', autouse=True)
def create_zip():
    resources_path = pathlib.Path(os.path.join(os.path.dirname(__file__), os.path.abspath('resources')))
    tmp_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources/tmp')
    archive_path = os.path.join(tmp_path, 'archive.zip')

    if not os.path.exists(tmp_path):
        os.mkdir(tmp_path)

    with ZipFile(archive_path, 'w', ZIP_DEFLATED) as zf:
        for file in resources_path.iterdir():
            zf.write(file, arcname=file.name)

    yield

    os.remove(archive_path)
    os.remove(tmp_path)