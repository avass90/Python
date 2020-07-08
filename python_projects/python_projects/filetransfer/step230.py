import tkinter
from tkinter import *
from tkinter import filedialog
import glob
import os
import datetime
import shutil

class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(600,250))
        self.master.title('Check files')
        

        self.btnbrowse1 = Button(self.master, text="Source Directory", width=15, height=1,command=self.sourcepath)
        self.btnbrowse1.grid(row=3,column=0,padx=(30,0),pady=(70,0), sticky=NE)

        self.btnbrowse2 = Button(self.master, text="Destination Directory", width=15, height=1,command=self.destinationpath)
        self.btnbrowse2.grid(row=4,column=0,padx=(30,0),pady=(20,0), sticky=NE)

        self.btncheck = Button(self.master, text="Copy Files", width=15, height=2, command=self.fileTransfer)
        self.btncheck.grid(row=5,column=0,padx=(30,0),pady=(20,0), sticky=NE)

        self.btnclose = Button(self.master, text="Close Program...", width=15, height=2)
        self.btnclose.grid(row=5,column=2,padx=(30,0),pady=(20,0), sticky=E)


        self.txt1= Entry(self.master, font=("Helvetica", 16),fg='black')
        self.txt1.grid(row=3,column=1,padx=(20,0),pady=(70,0), columnspan=2)


        self.txt2= Entry(self.master, font=("Helvetica", 16),fg='black')
        self.txt2.grid(row=4,column=1,padx=(20,0),pady=(20,0), columnspan=2)

    def sourcepath(self):
        file1 = filedialog.askdirectory()
        if self.txt1 != None:
            self.txt1.delete(0, END)
            self.txt1.insert(0, file1)
        else:
            pass

    def destinationpath(self):
        file1 = filedialog.askdirectory()
        if self.txt2 != None:
            self.txt2.delete(0, END)
            self.txt2.insert(0, file1)
        else:
            pass

######################################################################

    def fileTransfer(self):
        def GetFileList(path, type):
            '''
            Return a list of filename matching the given path and file type
            '''
            return glob.glob(path + "*" + type)

        originPath = self.txt1.get()+"/"
        destinationPath = self.txt2.get()+"/"
        fileType = ".txt"

    # Create list of text filenames in Origin folder
        fileList = GetFileList(originPath, fileType)
        


        for file in fileList:
            # Get last modified date and today's date
            modifyDate = datetime.datetime.fromtimestamp(os.path.getmtime(file))
            todaysDate = datetime.datetime.today()
                
            filePathList = file.split("\\") # Create a list from the filepath
            filename = filePathList[-1] # The last element is a the filename
                
            # If modified within last 24 hours, then copy to destination folder
            modifyDateLimit = modifyDate + datetime.timedelta(days=1)

            # If the file was edited less then 24 hours ago then copy it
            if modifyDateLimit > todaysDate:
                shutil.copy2(file, destinationPath + filename)

   


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
