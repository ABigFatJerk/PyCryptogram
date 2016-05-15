class CryptogramModel(object):
    def __init__(self, controller):
        self._controller = controller
        self._plaintext_string = self._select_plaintext_string()
        self._crypto_mapping = CryptogramMapping()
        self._crypto_string = self._crypto_mapping.encrypt(self._plaintext_string);

    def get_crypto_string(self):
        return self._crypto_string

    def _select_plaintext_string(self):
        return "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"


class CryptogramMapping(object):
    def __init__(self):
        pass

    def encrypt(self, plaintext_string):
        return plaintext_string