from os import urandom
from enum import Enum
from hashlib import blake2b
from _tweetnaclSquad import (crypto_box_beforenm, crypto_scalarmult_base, crypto_secretbox, crypto_secretbox_open)

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

    def __bytes__(self):
        return self._nonce

    def __len__(self):
        return len(self._nonce)

    def increment(self):
        self._nonce = (int.from_bytes(self._nonce, 'little') + 2).to_bytes(24, 'little') # using BOXBYTES is not needed, as we can just use 24

class PepperState(Enum):
    PEPPER_INVALID: int = -1
    PEPPER_AUTH: int = 0
    PEPPER_LOGIN: int = 1
    PEPPER_AUTHENTICATED: int = 2

class PepperEncrypter:
    class CryptographyError(Exception):
        def __init__(self, message):
            super().__init__(message)

    def __init__(self):
        self.state = PepperState.PEPPER_INVALID
        self.server_public_key = bytes.fromhex("439CF001F04AACD0E47A941C62FA73FC450769BD348BC71A9FEE3806D84C4D16")
        self.client_private_key = bytes(bytearray([0xFF, 0x45, 0x12, 0x7A, 0x9C, 0x23, 0x4B, 0x67, 0xA1, 0x2D, 0x3E, 0x56, 0x90, 0xAB, 0xC8, 0xD3, 0xE5, 0xF4, 0x6B, 0x72, 0x85, 0x19, 0x3A, 0x4F, 0x28, 0x63, 0x92, 0xBD, 0xFA, 0x34, 0x76, 0x08]))
        self.client_public_key = crypto_scalarmult_base(self.client_private_key)
        self.session_key = None
        self.decryptNonce = None
        self.encryptNonce = Nonce(urandom(24))
        self.shared_encryption_key = bytes(urandom(32))
        self.nonce = None
        self.s = None

    def decrypt(self, packet_id, payload):
        if packet_id == 10100:
            if self.state != PepperState.PEPPER_INVALID: raise self.CryptographyError(
                    "[PepperEncrypter::] Received ClientHelloMessage while not in PEPPER_INVALID state")
            self.state = PepperState.PEPPER_AUTH
            return payload

        elif packet_id == 10101:
            if self.state != PepperState.PEPPER_AUTH: raise self.CryptographyError(
                    "[PepperEncrypter::] Received LoginMessage while not in PEPPER_AUTH state")

            if payload[:32] != self.client_public_key:
                raise self.CryptographyError(
                    f"Client public key does not match! client public key: {self.client_public_key}, message (10101) key: {payload[:32]}")

            payload = payload[32:]
            self.nonce = Nonce(clientKey=self.client_public_key, serverKey=self.server_public_key)
            self.s = crypto_box_beforenm(self.server_public_key, self.client_private_key)
            decrypted = crypto_secretbox_open(payload, bytes(self.nonce), self.s)

            if decrypted[:24] != self.session_key:
                raise self.CryptographyError("LoginMessage SessionKey does not match with server key!")

            self.decryptNonce = Nonce(decrypted[24:48])  # decrypted nonce
            self.state = PepperState.PEPPER_LOGIN
            return decrypted[48:]

        else:
            if self.state != PepperState.PEPPER_AUTHENTICATED: raise self.CryptographyError("Session is not in PEPPER_AUTHENTICATED state!")
            self.decryptNonce.increment()
            return crypto_secretbox_open(payload, bytes(self.decryptNonce), self.shared_encryption_key)

    def encrypt(self, packetID, payload):
        match self.state:

            case PepperState.PEPPER_AUTH:
                if packetID == 20100:
                    self.session_key = payload[4:]
                    return payload

                elif packetID == 20103: return payload
                raise self.CryptographyError("Received packet with type other than 20100, 20103 while PepperState == AUTH")

            case PepperState.PEPPER_LOGIN:
                nonce = Nonce(self.decryptNonce, clientKey=self.client_public_key, serverKey=self.server_public_key)
                payload = bytes(self.encryptNonce) + self.shared_encryption_key + payload
                self.state = PepperState.PEPPER_AUTHENTICATED
                return crypto_secretbox(payload, bytes(nonce), self.s)

            case PepperState.PEPPER_AUTHENTICATED:
                self.encryptNonce.increment()
                return crypto_secretbox(payload, bytes(self.encryptNonce), self.shared_encryption_key)