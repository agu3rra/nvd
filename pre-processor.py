# Preprocesses NVD data
import re
name_pattern = r'(nvdcve-1.1-){1}(\d){4}'

# Listing JSON files
from os import listdir
from os.path import isfile, join
path = join('data', 'extracted')
data_files = [f for f in listdir(path) if isfile(join(path, f))]
print('{} files identified'.format(len(data_files)))
for item in data_files:
    print(item)

import json

# use a stack to append data
full_list = []
total_cves = 0
for data_file in data_files:
    file_path = join(path, data_file)
    print('Processing {}'.format(file_path))
    with open(file_path, encoding='utf-8') as fh:
        contents = json.load(fh)
        contents = contents.get("CVE_Items", None)
        if contents is None:
            raise ValueError('CVE_Items not found in {}'.format(file_path))
        cve_count = len(contents)
        print('Found {} CVEs in {}'.format(cve_count, data_file))
        total_cves += cve_count
        full_list += contents

print('Total CVEs documented: {}'.format(total_cves))
print('Total CVEs documented: {}'.format(len(total_cves)))