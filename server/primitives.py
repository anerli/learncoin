'''
Wrappers for cryptographic primitives to abstract away their specific implementations,
which you may not normally want since it obscures the security of these mechanisms,
but it does otherwise make the code more clear.
'''
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, BestAvailableEncryption, NoEncryption

def secure_hash(data: bytes) -> bytes:
    digest = hashes.Hash(hashes.SHA256())
    digest.update(data)
    return digest.finalize()

PrivateKey = Ed25519PrivateKey
PublicKey = Ed25519PublicKey

# def generate_private_key() -> PrivateKey:
#     return PrivateKey.generate()

def serialize_private_key(key: PrivateKey) -> bytes:
    return key.private_bytes(
        encoding=Encoding.Raw,
        format=PrivateFormat.Raw,
        encryption_algorithm=NoEncryption()#BestAvailableEncryption(b'asd')
    )

def deserialize_private_key(key_bytes: bytes) -> PrivateKey:
    return PrivateKey.from_private_bytes(key_bytes)

# ! needs testing
def serialize_public_key(key: PublicKey) -> bytes:
    return key.public_bytes(
        encoding=Encoding.Raw,
        format=PrivateFormat.Raw,
        encryption_algorithm=NoEncryption()#BestAvailableEncryption(b'asd')
    )

# ! needs testing
def deserialize_public_key(key_bytes: bytes) -> PublicKey:
    return PublicKey.from_public_bytes(key_bytes)

if __name__ == '__main__':
    key = PrivateKey.generate()
    #print('pubkey:', key.public_key().public_bytes().hex())
    print('privkey:', key)

    key_bytes = serialize_private_key(key)

    print(key_bytes.hex())

    #key = PrivateKey.from_private_bytes(key_bytes)
    key = deserialize_private_key(key_bytes)

    print(key)