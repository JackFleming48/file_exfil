def connect_ftp():

    import os

    from dotenv import load_dotenv, dotenv_values
    from ftplib import FTP

    load_dotenv()

    hst = os.getenv("CONNECT_IP")
    usr = os.getenv("FTP_USER")
    psswd = os.getenv("FTP_PASS")

    ftp = FTP(host=hst)

    ftp.login(user=usr, passwd=psswd)
    ftp.set_pasv(False)

    print(ftp.getwelcome())
    print(ftp.pwd())
    return ftp

