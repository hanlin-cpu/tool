def read_file():
    with open('table_ddl.txt', encoding="utf-8") as f:
        txt = f.readlines()
        handle_file(txt)


def handle_file(txt):
    tmp = '''| 参数 | 类型 | 注释 |
|:--- |: --- |:--- |
'''
    for t in txt:
        if t.strip().find('`') == 0:
            tmp += '|' + t.strip()[1:t.strip().find('`', 1)] + '|' + check_type(t.strip()) + '|' + check_comment(
                t.strip()) + '|' + '\r\n'
    print(tmp)


def check_type(string):
    if string.find('int(') != -1 or string.find('tinyint(') != -1:
        return '整型'
    elif string.find('float(') != -1 or string.find('double(') != -1 or string.find('decimal(') != -1:
        return '浮点'
    else:
        return '字符'


def check_comment(string):
    if len(string.split("COMMENT '")) == 2:
        return string.split("COMMENT '")[1]
    else:
        return 'x'


def make_markdown():
    pass


read_file()
