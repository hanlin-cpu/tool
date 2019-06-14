import time

with open('poem.txt', encoding="utf-8") as f:
    txt = f.readlines()
f.close()

new_txt = ''
for t in txt:
    # if t.find('`') != -1:
    #     print(t.strip())
    print(t.find('`'))
    time.sleep(1)
