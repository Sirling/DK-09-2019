from cryptography.fernet import Fernet
key = b'7rXp-DncbBjrWlzhDxM5EPX0O5sdTnd2KNFmB_npXVU='
cipher_suite = Fernet(key)
with open('c:\Work\Projects\DK-09-2019\mysqltip.bin', 'rb') as file_object:
    for line in file_object:
        encryptedpwd = line
uncipher_text = (cipher_suite.decrypt(encryptedpwd))
password = bytes(uncipher_text).decode("utf-8") #convert to string
