# NLP text preprocessing and vectorization
Hi, this project is a guide repository containing guides and examples related to the text preprocessing and vectorization. Its purpose is to proviade clear explanations of first step to NLP(Natural Language Processing) for beginners and offer pratical examples for developers.

## Contents
This guide repo includes guides and examples covering various topics related to text preprocessing and vectorization:

1. Cleanning:<br>
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
