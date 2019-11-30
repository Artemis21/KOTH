import os
import pathlib
import site


path = str(pathlib.Path(os.getcwd()).parent)
file = os.path.join(site.USER_SITE, 'koth.pth')
with open(file, 'w') as f:
    f.write(path)
