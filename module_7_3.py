class WordsFinder:
    def __init__(self, *files_names):
        self.files_names = files_names

    def get_all_words(self):
        all_words = {}
        for i in self.files_names:
            with open(i, "r", encoding='utf-8') as file:
                f = file.read().lower()
                for j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    f = f.replace(j, "")
                all_words[i] = f.split()
        return all_words

    def find(self, word):
        u = {}
        for name, words in self.get_all_words().items():
            u[name] = words.index(word.lower()) + 1
        return u

    def count(self, word):
        l = {}
        for name, words in self.get_all_words().items():
            count_name = words.count(word.lower())
            l[name] = count_name
        return l


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего