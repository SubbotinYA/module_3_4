# Задача "Однокоренные":
# Напишите функцию single_root_words, которая принимает одно обязательное слово в параметр root_word,
# а далее неограниченную последовательность в параметр *other_words.
# Функция должна составить новый список same_words только из тех слов списка other_words, которые содержат root_word
# или наоборот root_word содержит одно из этих слов. После вернуть список same_words в качестве результата своей работы.
def single_root_words(root_word, *other_words):
    # Создаем пустой список, в который будем пополнять удовлетворяющими условиями
    same_words = []
    # сравнения всегда производятся после приведения к нижнему регистру
    root_word_lower = root_word.lower()
    for i in other_words:
        other_words_lower = i.lower()
        if root_word_lower in other_words_lower or other_words_lower in root_word_lower:
            same_words.append(i)

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
