from tkinter import Tk, Button
from tkinter.ttk import Progressbar

class WordPressDownloader(Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('WordPress Downloader')
        self.geometry("300x50")
        self.resizable(False,False)

        self.progressbar = Progressbar(self)
        self.progressbar.pack(fill='x', padx=10)

        self.button = Button(self, text='Download')
        self.button.pack(padx=10, pady=3, anchor='e')


if __name__ == '__main__':
    app = WordPressDownloader()
    app2 = WordPressDownloader()
    app.mainloop()
    app2.mainloop()
