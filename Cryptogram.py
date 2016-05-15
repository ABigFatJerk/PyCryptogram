import Tkinter
import string
import CryptogramView
import CryptogramModel

ALPHABET = list(string.ascii_uppercase)


class Cryptogram(object):
    def __init__(self, parent):
        self._parent = parent
        self._letter_dict = {el: [] for el in ALPHABET}
        self._selected_letter = None
        self._view = CryptogramView.CryptogramView(self, self._parent)
        self._model = CryptogramModel.CryptogramModel(self)
        self._setup_new_game() # TODO would be separate call

    def _setup_new_game(self):
        self._view.set_crypto_string(self._model.generate_crypto_string())

    def register_letter(self, letter_view):
        self._letter_dict[letter_view.get_crypto_letter()].append(letter_view)

    def handle_letter_click(self, letter_view):
        if self._selected_letter is not None:
            for old_letter_view in self._letter_dict[self._selected_letter]:
                old_letter_view.deselect()
        self._selected_letter = letter_view.get_crypto_letter()
        for new_letter_view in self._letter_dict[self._selected_letter]:
            new_letter_view.select()

    def handle_key_press(self, event):
        if self._selected_letter is None:
            return
        key = event.char.upper()
        if key in ALPHABET:
            for selected_letter_view in self._letter_dict[self._selected_letter]:
                selected_letter_view.set_plaintext_letter(key)
        elif event.keysym == 'Delete':
            for selected_letter_view in self._letter_dict[self._selected_letter]:
                selected_letter_view.set_plaintext_letter('?')  # TODO very similar to above

if __name__ == '__main__':
    root = Tkinter.Tk()
    cryptogram = Cryptogram(root)
    root.mainloop()
