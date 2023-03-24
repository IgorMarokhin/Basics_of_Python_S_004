'''
Задача No27. Решение в группах
Пользователь вводит текст (строка). Словом считается последовательность непробельных символов идущих подряд,
слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.

Input: She sells sea shells on the sea shore. The shells that she sells are sea shells. I'm sure.
So if she sells sea shells on the sea shore. I'm sure that the shells are sea shore shells.

Output: 13
'''
string = "She sells sea shells on the sea shore.\n" \
         "The shells that she sells are sea shells. I'm sure.\n" \
         "So if she sells sea shells on the sea shore.\n" \
         "I'm sure that the shells are sea shore shells."

def word_counter(string: str):
    result = {i for i in string
                        .lower()
                        .replace(".", " ")
                        .split()}
    print(result)
    return f"В тексте содержится {len(result)} различных слов"

print(word_counter(string))