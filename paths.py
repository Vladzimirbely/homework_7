import os

resources_path = os.path.join(os.path.dirname(__file__), os.path.abspath('resources'))
tmp_path = os.path.join(os.path.dirname(__file__), os.path.abspath('resources/tmp'))
archive_path = os.path.join(tmp_path, 'archive.zip')

print(archive_path)