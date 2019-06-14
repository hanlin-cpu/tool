from tkinter import *


class App:
    def __init__(self, master):
        frame = Frame(master)  # container
        frame.pack()
        self.quitButton = Text()
        self.quitButton.pack()

        self.hiButton = Button(frame, text='Say Hi', command=self.read_file)
        self.hiButton.pack()

    def hello(self):
        print('hello tkinter')

    def read_file(self):
        with open(self.quitButton.get(0.0, "end"), encoding="utf-8") as f:
            txt = f.readlines()
            self.handle_file(txt)

    def handle_file(self, txt):
        tmp = '''| 参数 | 类型 | 注释 |
|:--- |: --- |:--- |
'''
        for t in txt:
            if t.strip().find('`') == 0:
                tmp += '|' + t.strip()[1:t.strip().find('`', 1)] + '|' + self.check_type(
                    t.strip()) + '|' + self.check_comment(
                    t.strip()) + '|' + '\r\n'
        print(tmp, end='')

    def check_type(self, string):
        if string.find('int(') != -1 or string.find('tinyint(') != -1:
            return '整型'
        elif string.find('float(') != -1 or string.find('double(') != -1 or string.find('decimal(') != -1:
            return '浮点'
        else:
            return '字符'

    def check_comment(self, string):
        if len(string.split("COMMENT '")) == 2:
           // return string.split("COMMENT '")[1]
        else:
          //  return 'x'


root = Tk()

app = App(root)

root.mainloop()
