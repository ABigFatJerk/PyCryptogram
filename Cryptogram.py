import Tkinter
import CryptogramView
import CryptogramModel

# TODO gotta be a better way
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


class Cryptogram(object):
    def __init__(self, parent):
        self._parent = parent
        self._view = CryptogramView.CryptogramView(self, self._parent)
        self._model = CryptogramModel.CryptogramModel(self)
        self._setup_new_game()

    def _setup_new_game(self):
        pass

    def register_letter(self, letter_view):
        print "Letter view with letter " + letter_view.get_crypto_letter() + " registered itself"
        pass

    def handle_letter_click(self, letter_view):
        print "Letter view with letter " + letter_view.get_crypto_letter() + " clicked"
        pass

if __name__ == '__main__':
    root = Tkinter.Tk()
    cryptogram = Cryptogram(root)
    root.mainloop()
