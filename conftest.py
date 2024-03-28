import shutil
import pytest
from zipfile import ZipFile, ZIP_DEFLATED
from paths import *
import pathlib

@pytest.fixture(scope='function', autouse=True)
def create_zip():
    if not os.path.exists(tmp_path):
        os.mkdir(tmp_path)

    with ZipFile(archive_path, 'w', ZIP_DEFLATED) as zf:
        for file in pathlib.Path(resources_path).iterdir():
            zf.write(file, arcname=file.name)

    yield
    shutil.rmtree(tmp_path)
