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

   -Stop word removing:<br>
   -Remove common stopwords (e.g., "and," "the," "is") that do not carry significant meaning and may only add noise to the data.
   # Example(recommended method):
   ```python
   language = "english"
   stop_words = nltk.corpus.stopwords.words(language)
   custom_stopwords = ['test'] #adding custom stop word
   stop_words.extend(custom_stopwords)
   wordsFiltered = []
   for word in mystr:
      if word not in stop_words:
         wordsFiltered.append(word)
   print([word for word in wordsFiltered])
   print(mystr)
   ```
   # Or:
   ```python
   custom_stopwords = ['the', 'your', 'customized', 'stopwords', 'list']
   # filtered word list
   wordsFiltered = [word for word in words if word not in custom_stopwords]
   print(wordsFiltered)
   ```

# 3. Stemming:<br>
   -Stemming is the process of reducing words to their base or root form, often by removing suffixes. The goal is to map related words to the same root, reducing them to a common base form. This can be beneficial in scenarios where variations of a word carry similar meanings, and treating them as the same token can simplify text analysis.

<h3>For example:</h3>
<table>
   <tr>
      <td>"running"</td>
      <td>→</td>
      <td>"run"</td>
   </tr>
   <tr>
      <td>"flies"</td>
      <td>→</td>
      <td>"fli"</td>
   </tr>
   <tr>
      <td>"happily"</td>
      <td>→</td>
      <td>"happi"</td>
   </tr>
</table>

   -By applying stemming, variations of words are collapsed into a common form, which can help in tasks such as text mining, information retrieval, and search engines. Stemming does not always result in a real word, but it aims to capture the core meaning of a word.

   # Algorithmic Approaches to Stemming:

   -There are different algorithms for stemming, and each has its own rules and heuristics. Some common stemming algorithms include:<br>
<ol>
   <li>Porter Stemmer: Developed by Martin Porter, it's one of the oldest and widely used stemming algorithms. It applies a series of rules to reduce words to their base form.
   # Example:
         
   ```python
   stemmer = nltk.stem.PorterStemmer()
   for word in mystr:
      print(stemmer.stem(word))
   ```

   </li>
   <li>
   Snowball Stemmer: Also known as the Porter2 stemmer, it is an extension of the Porter stemmer and provides support for multiple languages.
   # Example:
         
   ```python
   stemmer = nltk.stem.SnowballStemmer()
   for word in mystr:
      print(stemmer.stem(word))
   ```
   </li>
   <li>
Lancaster Stemmer: This is an aggressive stemming algorithm that often produces shorter stems compared to the Porter stemmer.
   # Example:
         
   ```python
   stemmer = nltk.stem.LancasterStemmer()
   for word in mystr:
      print(stemmer.stem(word))
   ```
   </li>
</ol>
-Considerations and Limitations: While stemming is a valuable tool, it's important to note some considerations and limitations:
<ol>
   <li>
Over-stemming: Aggressive stemming may lead to over-stemming, where different words are incorrectly reduced to the same stem.
   </li>
   <li>
Under-stemming: On the other hand, under-stemming may occur when related words are not reduced to the same stem.
   </li>
   <li>
Loss of Information: Since stemming involves removing suffixes, there is a potential loss of information, and the resulting stems may not always be meaningful words.
   </li>
</ol>
   -Despite these considerations, stemming is a widely used technique in text preprocessing for its simplicity and effectiveness in reducing the dimensionality of text data while retaining semantic meaning.

# 4. Lemmatization:<br>

## Combine the all informations (text preprocessing)
      
      ```python
      import re
      import nltk
      from nltk.corpus import stopwords
      from nltk.stem import PorterStemmer, WordNetLemmatizer
      #nltk.download('stopwords')
      
      #cleaning
      mystr = "Hello, it's my example sentence!"
      mystr = mystr.lower()
      print(mystr)
      
      mystr = re.sub(r'[^\w\s]', '', mystr)#removing punctuation
      print(mystr)
      
      #tokenization
      nltk.download('punkt')
      nltk.download('wordnet')
      
      mystr = nltk.word_tokenize(mystr)
      print(mystr)
      
      #stop words removing
      language = "english"
      stop_words = stopwords.words(language)
      custom_stopwords = ['test'] #adding custom stop word
      stop_words.extend(custom_stopwords)
      wordsFiltered = []
      for word in mystr:
          if word not in stop_words:
              wordsFiltered.append(word)
      
      #print([word for word in wordsFiltered])
      
      print(mystr)
      
      #print(stop_words)
      
      #stemming
      """
      stemmer = PorterStemmer()
      for word in mystr:
          print(stemmer.stem(word))
      """
      #Lemmatization
      
      lemmatizer= WordNetLemmatizer()
      for word in mystr:
          print(lemmatizer.lemmatize(word))
      
      
      data = ['Title'][0:10]
      lemmatizer = WordNetLemmatizer()
      for index, row in data.iterrows():
          filter_sentence = []
          sentence = row['Title']
          sentence = re.sub(r'\w\s', '', sentence)#cleaning
          words = nltk.word_tokenize(sentence)#tokenization
          words = [w for w in words if not w in stop_words] #stopwords removal
          for word in words:
              filter_sentence.append(lemmatizer.lemmatize(word))
          print(filter_sentence)
          data.ix[index, 'Title'] = filter_sentence   
      ```

<h1>Always remember :</h1> 
Tokens : is every word in a sentence
Word: Token which is not stopword 
Stopword: Unwanted words ( should be removed but not all words . Words like not, ok should be avoided )
