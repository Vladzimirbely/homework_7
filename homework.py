from zipfile import ZipFile
from pypdf import PdfReader
from openpyxl.reader.excel import load_workbook
from paths import *

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

def test_write_pdf():
    archive = PdfReader('resources/Pdf.pdf')
    default = PdfReader(os.path.join(resources_path, 'Pdf.pdf'))
    assert len(default.pages) == len(archive.pages)
    assert default.pages[0].extract_text() == archive.pages[0].extract_text()
