# Оператор "with"
import string

class WordsFinder():

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    for p in punctuation:
                            line = line.replace(p, '')
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        results = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                results[name] = words.index(word.lower()) + 1
            else:
                results[name] = -1
        return results

    def count(self, word):
        results = {}
        for name, words in self.get_all_words().items():
            results[name] = words.count(word.lower())
        return results

finder2 = WordsFinder('test_file.txt', 'test_file2.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
print(finder2.find('captaiN')) # 2 слово по счёту
print(finder2.count('caPTaiN')) # 10 слов caPTain в тексте всего