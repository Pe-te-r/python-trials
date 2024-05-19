import rsa

public_key,private_key=rsa.newkeys(1024)

public_key_pem=public_key.save_pkcs1(format='PEM')
private_key_pem=private_key.save_pkcs1(format="PEM")


with open('public_key.pem', 'wb') as public_key_file:
    public_key_file.write(public_key_pem)


with open('private_key.pem', 'wb') as private_key_file:
    private_key_file.write(private_key_pem)

print("Private Key:")
print(private_key_pem.decode('utf-8'))

print("Public Key:")
print(public_key_pem.decode('utf-8'))


message='Hello world'

print(f'\n\n{message}')

encrypt=rsa.encrypt(message.encode(),public_key)
print(f'Encypted: {encrypt}')

decrypt=rsa.decrypt(encrypt,private_key).decode()
print(f'Decrypted: {decrypt}')

