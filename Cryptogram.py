import Tkinter
import CryptogramView
import CryptogramModel


class Cryptogram(object):
    def __init__(self, parent):
        self._parent = parent
        self._view = CryptogramView.CryptogramView(self, self._parent)
        self._model = CryptogramModel.CryptogramModel(self)


if __name__ == '__main__':
    root = Tkinter.Tk()
    cryptogram = Cryptogram(root)
    root.mainloop()