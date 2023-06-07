import string
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

class Comparison:
    def comparison(text1,text2):
        #Stop Word kaldır
        text1 = text1.lower()
        text2 = text2.lower()
        text1 = text1.split()
        text2 = text2.split()
        without_stop_word = []
        for word in text1:
            if word not in stop_words:
                without_stop_word.append(word)
        text1 = without_stop_word
        without_stop_word = []
        for word in text2:
            if word not in stop_words:
                without_stop_word.append(word)
        text2 = without_stop_word

        #Noktalama işaretlerini kaldır
        text1 = ' '.join([str(elem) for elem in text1])
        text2 = ' '.join([str(elem) for elem in text2])
        textnull = ""
        for i in text1:
            if i not in string.punctuation:
                textnull += i
        text1 = textnull
        textnull = ""
        for i in text2:
            if i not in string.punctuation:
                textnull += i
        text2 = textnull

        text1_re = text1
        text2_re = text2
        #Benzerlik Oranını Hesapla
        text1 = text1.split()
        text2 = text2.split()

        maxlen = max(len(text1), len(text2))
        benzer = 0
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    benzer += 1
                    break

        benzer_oran = (benzer * 100) / maxlen
        return benzer_oran,text1_re,text2_re