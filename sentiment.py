import pandas as pd
import pythainlp
from pythainlp.corpus.common import thai_stopwords
from pythainlp import word_tokenize
from wordcloud import WordCloud, STOPWORDS
import matplotlib as plt

column_names=["text"]
# Add header row while reading a CSV file
df = pd.read_csv('/content/test.csv', names=column_names)
df2=df['text'].str.split(pat="\t",expand=True)
dftext=pd.DataFrame(df2)
dftext=dftext.iloc[:,0:2]
dftext[1].value_counts().plot.bar()


thai_stopwords = list(thai_stopwords())
thai_stopwords

def text_process(text):
    final = "".join(u for u in text if u not in ("?", ".", ";", ":", "!", '"', "ๆ", "ฯ"))
    final = word_tokenize(final)
    final = " ".join(word for word in final)
    final = " ".join(word for word in final.split()
                     if word.lower not in thai_stopwords)
    return final

dftext['text_tokens'] = dftext[0].apply(text_process)

df_pos = dftext[dftext[1] == 'pos']
pos_word_all = " ".join(text for text in df_pos['text_tokens'])