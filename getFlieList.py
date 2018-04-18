# -*- coding: utf-8 -*-
#!/usr/bin/python3

"""
2018.04.13
"""

def GetFileList(FindPath,FlagStr=[]): 
    import os 
    FileList=[] 
    FileNames=os.listdir(FindPath) 
    if (len(FileNames)>0): 
        for fn in FileNames: 
            if (len(FlagStr)>0): 
                if (FlagStr in fn): 
                    fullfilename = os.path.join(FindPath,fn) 
                    FileList.append(fullfilename)

            else: 
                fullfilename=os.path.join(FindPath,fn) 
                FileList.append(fullfilename) 
    if (len(FileList)>0): 
        FileList.sort() 
    return FileList

if __name__ == "__main__" :
    path = "/home/hyx/Pictures"
    print(GetFileList(path,"jpg"))
    