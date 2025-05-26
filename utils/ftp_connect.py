import os

from dotenv import load_dotenv, dotenv_values
from ftplib import FTP

load_dotenv()

hst = os.getenv("CONNECT_IP")
usr = os.getenv("FTP_USER")
psswd = os.getenv("FTP_PASS")

def connect_ftp(hst, usr, psswd):

    ftp = FTP(host=hst)

    ftp.login(user=usr, passwd=psswd)

    print(ftp.getwelcome())
    print(ftp.pwd())

connect_ftp(hst, usr, psswd)
