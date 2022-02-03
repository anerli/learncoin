'''
Wrappers for cryptographic primitives to abstract away their specific implementations,
which you may not normally want since it obscures the security of these mechanisms,
but it does otherwise make the code more clear.
'''
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey

def secure_hash(data: bytes) -> bytes:
    digest = hashes.Hash(hashes.SHA256())
    digest.update(data)
    return digest.finalize()

PrivateKey = Ed25519PrivateKey
PublicKey = Ed25519PublicKey