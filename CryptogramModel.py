import Cryptogram
import random

QUOTES = [
    "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG",
    "NOW IS THE TIME FOR ALL GOOD MEN TO COME TO THE AID OF THE PARTY",
    "FOURSCORE AND SEVEN YEARS AGO, OUR FATHERS BROUGHT FORTH ONTO THIS CONTINENT A NEW NATION",
    "I MUST NOT FEAR. FEAR IS THE MIND-KILLER. FEAR IS THE LITTLE-DEATH THAT BRINGS TOTAL OBLITERATION"
]


class CryptogramModel(object):
    def __init__(self, controller):
        self._controller = controller
        self._plaintext_string = self._select_plaintext_string()
        self._crypto_mapping = CryptogramMapping()
        self._crypto_string = self._crypto_mapping.encrypt(self._plaintext_string)

    def get_crypto_string(self):
        return self._crypto_string

    def _select_plaintext_string(self):
        return random.choice(QUOTES)


class CryptogramMapping(object):
    def __init__(self):
        self._mapping = self._generate_mapping()

    def encrypt(self, plaintext_string):
        crypto_string = ''
        for char in plaintext_string:
            if char in Cryptogram.ALPHABET:
                crypto_string += self._mapping[char]
            else:
                crypto_string += char
        return crypto_string

    def _generate_mapping(self):
        alphabet_copy = list(Cryptogram.ALPHABET)
        random.shuffle(alphabet_copy) # TODO need to prevent a mapping where a letter maps to itself
        return {plain: crypto for (plain, crypto) in zip(Cryptogram.ALPHABET, alphabet_copy)}