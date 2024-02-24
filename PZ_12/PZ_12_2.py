'''
    Составить генератор (yield), который преобразует
    все буквенные символы в строчные.
'''

def gen(text):
    for char in text:
        yield char.lower()

input_text = "Пайтон"
output_text = ''.join(gen(input_text))
print(output_text)





