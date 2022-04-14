import json


class PositionalIndex:
    def __init__(self):
        self.__dictionary = {}
        self.__data = {}

    def __load_data(self, data_url):
        print("loading data ...")
        with open(data_url, 'r') as f:
            self.__data = json.load(f)

    def __dictionary_construction(self):
        print("dictionary construction ...")
        print('|', end='')
        for idx in range(len(self.__data)):
            for word_idx in range(len(self.__data[f'{idx}']['content'])):
                word = self.__data[f'{idx}']['content'][word_idx]
                if word in self.__dictionary:
                    if idx in self.__dictionary[word]['postings']:
                        self.__dictionary[word]['postings'][idx]['positions'].append(word_idx)
                        self.__dictionary[word]['postings'][idx]['count'] += 1
                    else:
                        self.__dictionary[word]['postings'][idx] = {'positions': [word_idx], 'count': 1}

                    self.__dictionary[word]["count"] += 1
                else:
                    self.__dictionary[word] = {'count': 1, 'postings': {}}
                    self.__dictionary[word]['postings'][idx] = {'positions': [word_idx], 'count': 1}

            if idx % 200 == 0:
                print('=', end='')
        print('|')

        self.__dictionary = dict(sorted(self.__dictionary.items()))

    def __save_dictionary(self, new_dictionary_url):
        print('saving dictionary ...')
        with open(new_dictionary_url, 'w') as f:
            f.write(json.dumps(self.__dictionary))

    def create(self, data_url, new_dictionary_url):
        self.__load_data(data_url)
        self.__dictionary_construction()
        self.__save_dictionary(new_dictionary_url)


if __name__ == '__main__':
    # positionalIndex = PositionalIndex()
    # positionalIndex.create('../data/main_data.json', '../data/dictionary.json')
    pass
