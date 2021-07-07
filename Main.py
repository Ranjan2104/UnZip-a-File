# Amresh Ranjan

import zipfile as z

target = 'demo.zip'

print('Starting to Unzip the File!')

root = z.ZipFile(target)

root.extractall('new')
root.close()

print('\nFile is Succesfully Unzipped!')
