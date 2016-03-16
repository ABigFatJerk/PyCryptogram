import Tkinter
import Cryptogram

LETTER_WIDTH = 13
BASE_COLOR = 'gray80'
SELECTED_COLOR = 'yellow'


class CryptogramView(object):
    def __init__(self, controller, parent):
        self._controller = controller
        self._parent = parent
        self._parent.bind_all('<Any-KeyPress>', self.on_keypress)
        
        self._key_frame = Tkinter.Frame(parent)
        self._key_grid = LetterGrid(self._key_frame, self._controller)
        self._key_grid.set_letters(Cryptogram.ALPHABET)
        self._puzzle_frame = Tkinter.Frame(parent)
        self._puzzle_grid = LetterGrid(self._puzzle_frame, self._controller)

        self._key_frame.grid(row=0, column=0)
        Tkinter.Label(parent, height=2).grid(row=1, column=0)
        self._puzzle_frame.grid(row=2, column=0)

    def on_keypress(self, event):
        self._controller.handle_key_press(event)

    def set_crypto_string(self, crypto_string):
        self._puzzle_grid.set_letters(crypto_string)


class LetterGrid(object):
    def __init__(self, parent_frame, controller):
        self._parent_frame = parent_frame
        self._controller = controller

    def set_letters(self, letters):
        for (index, letter) in enumerate(letters):
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
        self._plaintext_label = Tkinter.Label(self._parent_frame, text=self._plaintext_letter, bg=BASE_COLOR, width=4, relief=Tkinter.SUNKEN)
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
        self._plaintext_label.config(bg=SELECTED_COLOR)

    def deselect(self):
        self._plaintext_label.config(bg=BASE_COLOR)
