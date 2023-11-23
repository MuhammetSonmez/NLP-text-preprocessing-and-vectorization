import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import string

nltk.download('punkt')
nltk.download('stopwords')

def text_preprocessing(text):
    # transforming lowercase
    text = text.lower()
    
    # removing punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # removing digits
    text = ''.join([i for i in text if not i.isdigit()])
    
    # Tokenization
    tokens = word_tokenize(text)
    
    # Filtering stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]
    
    # Stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(word) for word in tokens]
    
    #Stemming is generally faster and may be sufficient in some cases
    #But from the perspective of grammatical accuracy and preserving meaning
    #Lemmatization is a more powerful option.
    #The choice of which method to use depends on the needs of your application and the characteristics of your text data.
    clean_text = ' '.join(tokens)

    return clean_text

sample_text = "This is the text preprocessing example with nltk. In this example include transforming to lowercase, removing punctuations, removing stop words and stemming."

cleaned_text = text_preprocessing(sample_text)

print("Before text preprocessing: ", sample_text)
print("After text preprocessing: ", cleaned_text)
