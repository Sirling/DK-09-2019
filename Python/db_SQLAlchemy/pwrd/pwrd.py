from cryptography.fernet import Fernet
#  шифрование пароля с использованием ключа
key = b'rYUav-sYOJWL4-jiCsLYogp-Wsa1u3OU3r-i1e-0x64='
cipher_suite = Fernet(key)
# считывание из файла с зашифрованным паролем
with open('C:\Work\Projects\DK-09-2019\Python\mysqltip.bin', 'rb') as file_object:
    for line in file_object:
        encryptedpwd = line
# дешифровка пароля
uncipher_text = (cipher_suite.decrypt(encryptedpwd))
# конвертация в стринг
password = bytes(uncipher_text).decode("utf-8")
