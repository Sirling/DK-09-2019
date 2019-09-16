from cryptography.fernet import Fernet
#  шифрование пароля с использованием ключа
key = b'FJ_8mpFZFzvX8iKOUMhdCjQTBv7cyrGmAkuYyskNzMY='
cipher_suite = Fernet(key)
# считывание из файла с зашифрованным паролем
with open('c:\\Work\\Projects\\DK-09-2019\\mysqltip.bin', 'rb') as file_object:
    for line in file_object:
        encryptedpwd = line
# дешифровка пароля
uncipher_text = (cipher_suite.decrypt(encryptedpwd))
# конвертация в стринг
password = bytes(uncipher_text).decode("utf-8")
