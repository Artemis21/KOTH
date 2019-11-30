'''
Simple script to add this collection of scripts as a package to the python
installation's site-packages so that it will be added to sys.path.
'''
import os
import pathlib
import site


# Get the parent dir.
path = str(pathlib.Path(os.getcwd()).parent)
# Get the file name - koth.pth in site-packages.
file = os.path.join(site.USER_SITE, 'koth.pth')
with open(file, 'w') as f:
    # Write the path to the file.
    f.write(path)
