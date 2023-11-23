# NLP text preprocessing and vectorization
Hi, this project is a guide repository containing guides and examples related to the text preprocessing and vectorization. Its purpose is to proviade clear explanations of first step to NLP(Natural Language Processing) for beginners and offer pratical examples for developers.

## Contents
This guide repo includes guides and examples covering various topics related to text preprocessing and vectorization:

# 1. Cleanning:<br>
   -Convert all text to lowercase to ensure uniformity and prevent the model from treating the same word in different cases as different.
   # Example:
   ```python
   mystr = "Hello, it's my example sentence!"
   mystr = mystr.lower()
   print(mystr)
   ```
   -Eliminate unnecessary punctuation marks, as they often do not contribute much to the meaning and can add noise to the data.
   # Example(recommended method):
   ```python
    import re
    mystr = re.sub(r'[^\w\s]', '', mystr)  # removing punctuation
    print(mystr)
   ```
   # or:
   ```python
   import string
   mystr = "Hello, it's my example sentence!"
   translator = str.maketrans("", "", string.punctuation)
   mystr = mystr.translate(translator)
   print(mystr)
   ```
# 2. Tokenization:<br>
   -To tokenize means to break down text into small pieces or 'tokens.' A token typically represents a word, but depending on the tokenization strategy, it could also be a letter of a word, an n-gram, or even a sentence.
   -The primary purpose of tokenization is to divide the text into smaller and manageable units, allowing for further analysis or modeling. The goal is to break the text into meaningful components that can be processed effectively.
   # Example(recommended method):
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('wordnet')
      
   mystr = nltk.word_tokenize(mystr)
   print(mystr)
   ```
   # or:
   ```python
   tokenized_str = mystr.split()
   print(tokenized_str)
   ```
   # Warning:
<h4>
The split() function and nltk.word_tokenize() function essentially perform the same task: breaking down a piece of text into its constituent words. However, there are some differences between these two approaches, and the choice of which function to use may vary depending on the situation. Here are some key distinctions:
<br>
Natural Language Processing Functionality: The nltk.word_tokenize() function supports a broader range of functionality in natural language processing applications. Specifically, it can utilize grammatical information to ensure accurate parsing of sentences and words. In contrast, the split() function merely performs the function of separating based on spaces.
<br>
Punctuation Processing: The nltk.word_tokenize() function employs a more advanced logic for separating punctuation marks from words. For instance, the "word_tokenize" function applies various grammatical rules to accurately separate words combined with punctuation marks.
<br>
Handling Stop Words: The nltk.word_tokenize() function has the capability to address "stop words," commonly disregarded words that often carry little meaning and are typically ignored during analysis.
<br>
Extensive Linguistic Resources: The nltk library encompasses a comprehensive linguistic resource, including various natural language processing tools such as grammatical analysis and stemming. Therefore, using nltk can provide additional tools and features for your natural language processing applications.
<br>
However, in some cases, simply splitting a text based on spaces may be sufficient, and in such situations, the split() function can be used. Your decision depends on the specific requirements of your application and your particular needs.
</h6>
# 3. Stemming:<br>
# 4. Lemmatization:<br>

   
