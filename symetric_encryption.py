from cryptography.fernet import Fernet
import sys 


def get_key():
    return Fernet.generate_key()

def encrypt(message,key):
    fernet=Fernet(key)

    return fernet.encrypt(message.encode())


def decrypt(cipher,key):
    fernet=Fernet(key)

    return fernet.decrypt(cipher).decode()



def main():
    print("Encrypting and decrypt simple messages on the terminal: ")
    
    print("\n Type exit to quit.")

    key=get_key()

    while True:
        message=input('\n\nmessage: ')
        if message.lower()=='exit':
            sys.exit()

        cipher=encrypt(message,key)
        
        print(f'Encrypted: {cipher}')

        print(f'Decrypted: {decrypt(cipher,key)}')
    
if __name__=='__main__':
    main()

