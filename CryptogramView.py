import Tkinter
import Cryptogram

LETTER_WIDTH = 13


class CryptogramView(object):
    def __init__(self, controller, parent):
        self._controller = controller
        self._parent = parent
        self._key_frame = Tkinter.Frame(parent)
        self._key_view = KeyView(self._key_frame, self._controller)
        self._grid_frame = Tkinter.Frame(parent)
        self._grid_view = GridView(self._grid_frame, self._controller)
        self._key_frame.grid(row=0, column=0)
        Tkinter.Label(parent, height=2).grid(row=1, column=0)
        self._grid_frame.grid(row=2, column=0)

    def set_crypto_string(self, crypto_string):
        self._grid_view.set_crypto_string(crypto_string)


class KeyView(object):
    def __init__(self, parent_frame, controller):
        self._parent_frame = parent_frame
        self._controller = controller
        for (index, letter) in enumerate(Cryptogram.ALPHABET):
            row = index / LETTER_WIDTH
            column = index % LETTER_WIDTH
            frame = Tkinter.Frame(self._parent_frame)
            letter_view = LetterView(frame, letter, self._controller)
            self._controller.register_letter(letter_view)
            frame.grid(row=row, column=column)


class GridView(object):
    def __init__(self, parent_frame, controller):
        self._parent_frame = parent_frame
        self._controller = controller

    def set_crypto_string(self, crypto_string):
        for (index, letter) in enumerate(crypto_string):  # TODO duplicated in KeyView init
            row = index / LETTER_WIDTH
            column = index % LETTER_WIDTH
            frame = Tkinter.Frame(self._parent_frame)
            LetterView(frame, letter, self._controller)
            frame.grid(row=row, column=column)


class LetterView(object):
    def __init__(self, parent_frame, crypto_letter, controller):
        self._parent_frame = parent_frame
        self._crypto_letter = crypto_letter
        self._is_alpha = crypto_letter in Cryptogram.ALPHABET
        if self._is_alpha:
            self._plaintext_letter = '?'
        else:
            self._plaintext_letter = ''
        self._controller = controller
        self._crypto_letter_label = Tkinter.Label(self._parent_frame, text=self._crypto_letter, width=4, relief=Tkinter.RAISED)
        self._crypto_letter_label.grid(row=0, column=0)
        self._plaintext_label = Tkinter.Label(self._parent_frame, text=self._plaintext_letter, bg='gray80', width=4, relief=Tkinter.SUNKEN)
        if self._is_alpha:
            self._controller.register_letter(self)
            self._plaintext_label.bind("<Button-1>", self._on_click)
        self._plaintext_label.grid(row=1, column=0)

    def _on_click(self, event):
        self._controller.handle_letter_click(self)

    def get_crypto_letter(self):
        return self._crypto_letter

    def set_plaintext_letter(self, letter):
        if self._is_alpha:
            self._plaintext_letter = letter
            self._plaintext_label.config(text=letter)

    def select(self):
        self._plaintext_label.config(bg='yellow')

    def deselect(self):
        self._plaintext_label.config(bg='gray80')
