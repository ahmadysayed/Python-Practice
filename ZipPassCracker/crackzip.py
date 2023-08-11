#========== Author : Sayed Mujtaba Ahmady =================================
# Facebook Page : https://www.facebook.com/profile.php?id=100075938127515 +
# Instagram Page : https://www.instagram.com/_tech.box/                   +
# Youtube : https://www.youtube.com/@techbox8186                          +
# Github : https://github.com/ahmadysayed                                 + 
#==========================================================================
#Never forget to read the comments 

# ===========================================================================
# Usage:
#     For runnig this script you need to install python3

#     Don't forget to install the pyzipper module

#     pip install pyzipper

# For Runing the code:
#     you need to open your terminal or cmd in same folder as script and run
#     ==================================
#     +      python3 crackzip.py       + 
#     ==================================

#     Go throw the documentation to understand more
#     https://pypi.org/project/pyzipper/



import pyzipper

wordlist = "Your password dictionary file path"
file = "Your Zip or Rar file path"

fileobject = pyzipper.AESZipFile(file)

with open(wordlist, "rb") as wordlist:
    for word in wordlist:
        try:
            fileobject.pwd = word.strip()
            fileobject.read('d.py') #One of the content of the archive

        except:
            print("Tryping Password: ", word.decode().strip())
            continue
            
        else:
            print("Password Found: ", word.decode().strip())
            exit(0)
print("No Password Match, Please Try Another Wordlist")
    