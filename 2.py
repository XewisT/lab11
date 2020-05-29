"""
б) Дан текстовий файл f. Отримати файл g, утворений з файлу f заміною символів - цифр на поєднання букв, що позначають відповідну цифру (наприклад, '1' - 'один').
"""
def get_data():
    with open("fd.txt") as f:
        data = f.read()
    f.close()
    return data
data = get_data()
a = list(data)
with open('gd.txt', 'w') as f:
        if '1' in data:
            f.write('один ')
        if '2' in data:
            f.write('два ')
        if '3' in data:
            f.write('три ')
        if '4' in data:
            f.write('чотири ')
        if '5' in data:
            f.write('п`ять')
f.close()
