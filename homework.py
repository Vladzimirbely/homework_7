import os
from zipfile import ZipFile
from openpyxl import load_workbook
import pathlib

resources_path = pathlib.Path(os.path.join(os.path.dirname(__file__), os.path.abspath('resources')))
tmp_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources/tmp')
archive_path = os.path.join(tmp_path, 'archive.zip')

def test_write_xlsx():
    with ZipFile(archive_path, 'r') as zf:
        archive = load_workbook(zf.open('Excel.xlsx'))
        default = load_workbook(os.path.join(resources_path, 'Excel.xlsx'))

        sheet_archive = archive.active
        sheet_default = default.active

        archive_value = []
        default_value = []

        for i in range(0, sheet_archive.max_row):
            for j in sheet_archive.iter_cols(1, sheet_archive.max_column):
                archive_value.append(j[i].value)

        for i in range(0, sheet_default.max_row):
            for j in sheet_default.iter_cols(1, sheet_default.max_column):
                default_value.append(j[i].value)

        assert archive_value == default_value
        assert default.sheetnames == archive.sheetnames
