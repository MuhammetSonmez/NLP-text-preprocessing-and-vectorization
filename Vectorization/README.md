<h1>Vectorization</h1>

# bag of words<br>
-Bag of Words (BoW) is a common technique used in natural language processing (NLP) and text analysis to represent textual data. The basic idea behind BoW is to convert a piece of text into a numerical vector by counting the frequency of each word in the text and representing it as a vector of word counts.
## Representing words by their frequencies

<ol>
    <li>
        # Sentence 1: This hot dog is tasty -> hot, dog, tasty
    </li>
    <li>
        # Sentence 2: This dog is so cute -> dog, cute
    </li>
    <li>
        # Sentence 3: The food is felicious -> food, delicious
    </li>
    <li>
        # Sentence 3: The food is weird -> food, weird
    </li>
</ol>
<table>
    <tr>
        <th>
            Sentence
        </th>
        <th>
            weird
        </th>
        <th>
            hot
        </th>
        <th>
            dog
        </th>
        <th>
            tasty
        </th>
        <th>
            cute
        </th>
        <th>
            delicious
        </th>
        <th>
            food
        </th>
    </tr>
    <tr>
        <td>1</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <td>2</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
    </tr>
    <tr>
        <td>3</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>4</td>
        <td>1</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>0</td>
        <td>1</td>
    </tr>

</table>
# Example
    
```python
from sklearn.feature_extraction.text import CountVectorizer
string = ["This is an example of bag of words."]
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(string)
print(vectorizer.get_feature_names_out())
print(x.toarray())
```
    
```python
words_and_vectors = [(list(x.toarray())[0][i],vectorizer.get_feature_names_out()[i])
for i in range(len(list(x.toarray()[0])))]

for i in words_and_vectors:
  print(i)
    
```
    







