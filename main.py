text = input('Введите текст: ')
text = text.lower()
punctuation = ['.', ',', '!', '?', '-', ':', ';'] #deleting punctuation from the text
for i in punctuation:
    text = text.replace(i, '')
words = text.split()
long = words[0]
for i in words:
    if len(i) > len(long):
        long = i
short = words[0]
for i in words:
    if len(i) < len(short):
        short = i
num = {}
for i in words:
    num[i] = words.count(i)
print('Количество разных слов: ', len(set(words)))
print('Самое длинное слово: ', long)
print('Самое короткое слово: ', short)
print('Частота символов: ', num)
