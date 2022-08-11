"""
        Try the tkinter filedialog to select a file
"""

from tkinter import filedialog as fd
filename = fd.askopenfilename(multiple=True)

if filename == '':
    print('No file was chosen')
else:
    print('Length of filename: ', len(filename), ' File chosen was:', filename)

#
#   Since we allow multiple filenames to be selected we need to parse filename
#   to move through them one at a time
#
