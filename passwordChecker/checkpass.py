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
#     After Successfully python installation by defualt 
#     it will come install 3 following module but if you
#     face to error try to run the following commands

#     pip install requests
#     pip install hashlib
#     pip install os-sys

# For Runing the code:
#     you need to open your terminal or cmd in same folder as script and run
#     ==================================
#     python3 checkpass.py yourpassword +   <= change the text to password that you want to check
#     ==================================

#     In terminal you will see if your password ever hacked or not



import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res

def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # Check password if it exists in API response
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was fount {count} times... you should probably change your password!')
        else:
            print(f'{password} wat NOT found. Carry on!')
    return 'done!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))