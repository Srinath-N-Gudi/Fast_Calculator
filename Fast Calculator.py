from tkinter import *
import threading
class b:
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x200+500+250")
        self.root.title("Easy Calculator")
        self.enter = Entry(self.root, font = ("times new roman", 22, 'bold'), width=37)
        self.enter.place(x=75, y=50)
        self.answer = Label(self.root, text="",font = ("times new roman", 20, 'bold'))
        self.answer.pack(anchor='s')
        check = threading.Thread(target=self.check)
        check.start()
    def check(self):
        while True:
            value = self.enter.get()
            if value != "":
                try:
                    self.answer['text'] = eval(value)
                    self.root.update()
                except:
                    pass
root = Tk()
b(root)
root.mainloop()
