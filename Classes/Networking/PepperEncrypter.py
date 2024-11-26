from os import urandom
from hashlib import blake2b
from Classes.Cryptography.Cryptography import (
    crypto_box_curve25519xsalsa20poly1305_tweet_beforenm,
    crypto_scalarmult_curve25519_tweet_base,
    crypto_secretbox_xsalsa20poly1305_tweet,
    crypto_secretbox_xsalsa20poly1305_tweet_open
)


class Nonce:
    def __init__(self, nonce=None, clientKey=None, serverKey=None):
        if not clientKey:
            if nonce:
                self._nonce = nonce
            else:
                self._nonce = urandom(24)
        else:
            b2 = blake2b(digest_size=24)
            if nonce:
                b2.update(bytes(nonce))
            b2.update(bytes(clientKey))
            b2.update(serverKey)
            self._nonce = b2.digest()

    def __bytes__(self) -> bytes:
        return self._nonce

    def __len__(self) -> int:
        return len(self._nonce)

    def increment(self):
        self._nonce = (int.from_bytes(self._nonce, 'little') + 2).to_bytes(24, 'little')


class PepperEncrypter:
    ENCRYPTION_OVERHEAD = 16

    def __init__(self):
        self.authenticated = False
        self.server_public_key = bytes.fromhex("439CF001F04AACD0E47A941C62FA73FC450769BD348BC71A9FEE3806D84C4D16")
        self.client_private_key = bytearray([0xFF, 0x45, 0x12, 0x7A, 0x9C, 0x23, 0x4B, 0x67, 0xA1, 0x2D, 0x3E, 0x56, 0x90, 0xAB, 0xC8, 0xD3, 0xE5, 0xF4, 0x6B, 0x72, 0x85, 0x19, 0x3A, 0x4F, 0x28, 0x63, 0x92, 0xBD, 0xFA, 0x34, 0x76, 0x08])
        self.client_public_key = bytearray(32)
        self.session_key = None
        self.shared_key = None
        self.decryptNonce = None
        self.encryptNonce = Nonce(urandom(24))
        self.shared_encryption_key = bytes(urandom(32))
        self.nonce = None
        self.s = bytearray(32)

    def decrypt(self, packet_id: int, payload):
        if packet_id == 10100:
            return payload

        elif packet_id == 10101:  # LoginMessage payload starts with 32 bytes, being the client public key
            crypto_scalarmult_curve25519_tweet_base(self.client_public_key, self.client_private_key)

            if payload[:32] != self.client_public_key:
                print("[Crypto Error]: Client public key not matching!")
                return None

            payload = payload[32:]
            self.nonce = Nonce(clientKey=self.client_public_key, serverKey=self.server_public_key)
            crypto_box_curve25519xsalsa20poly1305_tweet_beforenm(self.s, self.server_public_key,
                                                                 self.client_private_key)
            payload = bytearray(self.ENCRYPTION_OVERHEAD) + bytearray(payload)
            decrypted = bytearray(len(payload))

            crypto_secretbox_xsalsa20poly1305_tweet_open(decrypted, payload, len(payload), bytes(self.nonce), self.s)
            decrypted = decrypted[32:]

            if decrypted[:24] != self.session_key:
                print("[Crypto Error] Session key not matching!")
                return None

            # session_key = decrypted[0:24]
            decrypted = decrypted[24:]
            self.decryptNonce = Nonce(bytes(decrypted[:24]))  # decrypted nonce
            self.authenticated = True
            return decrypted[24:]
        elif self.decryptNonce is None:
            return payload
        else:
            if not self.authenticated: return
            self.decryptNonce.increment()
            payload = bytearray(self.ENCRYPTION_OVERHEAD) + bytearray(payload)
            decrypted = bytearray(len(payload))
            crypto_secretbox_xsalsa20poly1305_tweet_open(decrypted, payload, len(payload), bytes(self.decryptNonce),
                                                         self.shared_encryption_key)
            return decrypted[32:]

    def encrypt(self, packetID: int, payload):
        if packetID == 20100:
            self.session_key = payload[4:]
            return payload

        elif packetID == 20103: return payload

        elif packetID in [29125, 20103]:
            nonce = Nonce(bytes(self.decryptNonce), clientKey=self.client_public_key,
                              serverKey=self.server_public_key)
            payload = bytes(self.encryptNonce) + self.shared_encryption_key + payload
            payload = bytearray(32) + bytearray(payload)
            encrypted = bytearray(len(payload))
            crypto_secretbox_xsalsa20poly1305_tweet(encrypted, payload, len(payload), bytes(nonce), self.s)
            return encrypted[self.ENCRYPTION_OVERHEAD:]
        else:
            self.encryptNonce.increment()
            payload = bytearray(32) + bytearray(payload)
            encrypted = bytearray(len(payload))
            crypto_secretbox_xsalsa20poly1305_tweet(encrypted, payload, len(payload), bytes(self.encryptNonce),
                                                        self.shared_encryption_key)
            return encrypted[self.ENCRYPTION_OVERHEAD:]