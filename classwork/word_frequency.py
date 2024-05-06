import string

def process_file(filename):
    word_hist = dict()
    fin = open(filename, encoding='utf8')
    for line in fin:
        process_line(line, word_hist)
    return word_hist

def process_line(line, word_hist):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        word_hist[word] = word_hist.get(word, 0) + 1

def total_words(word_hist):
    return len(word_hist)

def word_occur (word_hist):
    return sum(word_hist.values())

def most_common(word_hist):
    t = []
    for key, value in word_hist():
        t.append((value, key))

    t.sort()
    t.reverse()
    return t

def main():
   word_hist = process_file('pg1513.txt')
   print(f'Total numbers of words: {total_words(word_hist):,}')
   print(f'Total word occurences: {word_occur(word_hist):,}')

if __name__ == '__main__':
    main()