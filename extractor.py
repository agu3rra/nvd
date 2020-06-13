# Listing all files for extraction
from os import listdir
from os.path import isfile, join
raw_path = join('data', 'raw')
zipped_files = [f for f in listdir(raw_path) if isfile(join(raw_path, f))]
print('{} files identified'.format(len(zipped_files)))

# extract them all
extract_path = join('data', 'extracted')
from zipfile import ZipFile
for zip_file in zipped_files:
    print('Extracting contents of {}'.format(zip_file))
    with ZipFile(join(raw_path, zip_file), 'r') as zip_ref:
        zip_ref.extractall(extract_path)
