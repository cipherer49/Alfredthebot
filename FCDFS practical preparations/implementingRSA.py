import rsa
def generate_keys():
    (pubkey, privkey) = rsa.newkeys(1024)
    with open('keys/pubkey.pem', 'wb') as f:
        f.write(pubkey.save_pkcs1('PEM'))
    with open('keys/privkey.pem', 'wb') as f:
        f.write(privkey.save_pkcs1('PEM'))

def load_keys():
    with open('keys/pubkey.pem', 'rb') as f:
        pubkey = rsa.PublicKey.load_pkcs1(f.read())
    with open('keys/privkey.pem', 'rb') as f:
        privkey = rsa.PrivateKey.load_pkcs1(f.read())

    return pubkey, privkey

def encrypt(msg, key):
    return rsa.encrypt(msg.encode('ascii'), key)

def decrypt(ciphertext, key):
    try:
        return rsa.decrypt(ciphertext, key).decode('ascii')
    except:
        return False
def sign_sha1(msg, key):
    return rsa.sign(msg.encode('ascii'),key, 'SHA-1')

def verify_sha1(msg, signature,key):
    try:
        return rsa.verify(msg.encode('ascii'), signature, key) == 'SHA-1'
    except:
        return False

generate_keys()
pubkey, privkey = load_keys()

message = input('Enter a message:')
ciphertext = encrypt(message, pubkey)

signature = sign_sha1(message, privkey)

plaintext = decrypt(ciphertext, privkey)

print(f'Cipher text:{ciphertext}')
print(f'Signature:{signature}')

if plaintext:
    print(f'Plain text:{plaintext}')
else:
    print('Could not decrypt  the message.')

if verify_sha1(plaintext, signature, pubkey):
    print('Signature verified')
else:
    print('could not verify the message')
