from  tkinter import filedialog
from tkinter.filedialog import askopenfile
import os

def upload_file():
    f_types = [('rk file',['*.txt','*.xlsx'])]
    filename = filedialog.askopenfile(filetypes=f_types)
    r=os.path.basename(filename).split('/')[-1]
    print(r)




upload_file()