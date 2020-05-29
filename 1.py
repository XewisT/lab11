"""
а)Дано двійковий файл f, компоненти якого є цілими числами. Отримати в файлі g
всі компоненти файлу f, що діляться на 3 і не діляться на 5.
"""
def get_data():
    with open("f1.txt") as f:
        data = f.read()
    f.close()
    return data
data = get_data()
with open('f2.txt', 'w') as f:
    for i in data:
        try:
            if int(i) % 3 == 0 and int(i) % 5 != 0:
                f.write(i)
        except ValueError:
            del i
f.close()
