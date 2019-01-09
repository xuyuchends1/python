import os
ui_files=[]

def getUIFiles():
    dir = os.getcwd()
    for root, dirs, files in os.walk(dir):
        for name in files:
            extension=os.path.splitext(name)[1]
            if extension=='.ui':
                ui_files.append(os.path.join(root,name))

def transPYFiles(file):
    return os.path.splitext(file)[0]+".py"

def runCMD():
    if len(ui_files):
        for file in ui_files:
            py_file=transPYFiles(file)
            cmd="C:\Anaconda3\python.exe -m PyQt5.uic.pyuic -o {} {}".format(py_file,file)
            os.system(cmd)

getUIFiles()
runCMD()