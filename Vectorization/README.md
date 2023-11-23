<h1>Vectorization</h1>

# Bag of Words<br>
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
    
# Tf-idf Vectorizer<br>
-tf: How frequently a term occurs in a document<br>
TF(t) = (Number of items term t appears in a document)/(Total number of terms in the document)<br>
## Example: <br>
1- "Data science plays a crucial role in extracting insights from large datasets."<br>
TF("data") = 1/12<br>
TF("science") = 1/12<br>
TF("plays") = 1/12<br>
TF("crucial") = 1/12<br>
TF("role") = 1/12<br>
TF("extracting") = 1/12<br>
TF("insights") = 1/12<br>
TF("from") = 1/12<br>
TF("large") = 1/12<br>
TF("datasets") = 1/12<br>
<br>
-idf: the weight of rare words. The words that occur rarerly in the corpus have a high IDF score.<br>
IDF(t) = log(Total number of documents)/(Number of documents with term t in it)<br>
## Example:<br>
1-  "Machine learning algorithms can analyze vast amounts of data."<br>
2-  "The application of artificial intelligence is growing rapidly."<br>
3- "data scientists use statistical methods to draw meaningful insights."<br>
IDF(Machine) = log 3/1<br>
IDF(data) = log 3/2<br>
...<br>
## Tf-idf = Tf * idf<br>
# Example:

```python
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer()
doc1 = "data scientists use statistical methods to draw meaningful insights."
doc2 = "machine learning algorithms can analyze vast amounts of data."
result = tfidf.fit_transform([doc1, doc2])
print(len(tfidf.vocabulary_))
```
    output:17
```python
print(tfidf.vocabulary_)
```
    output: {'data': 4, 'scientists': 12, 'use': 15, 'statistical': 13, 'methods': 10, 'to': 14, 'draw': 5, 'meaningful': 9, 'insights': 6, 'machine': 8, 'learning': 7, 'algorithms': 0, 'can': 3, 'analyze': 2, 'vast': 16, 'amounts': 1, 'of': 11}
```python
print(result)
```
    output:
    (0, 6)	0.3428712594108198
    (0, 9)	0.3428712594108198
    (0, 5)	0.3428712594108198
    (0, 14)	0.3428712594108198
    (0, 10)	0.3428712594108198
    (0, 13)	0.3428712594108198
    (0, 15)	0.3428712594108198
    (0, 12)	0.3428712594108198
    (0, 4)	0.24395572500006343
    (1, 11)	0.3428712594108198
    (1, 1)	0.3428712594108198
    (1, 16)	0.3428712594108198
    (1, 2)	0.3428712594108198
    (1, 3)	0.3428712594108198
    (1, 0)	0.3428712594108198
    (1, 7)	0.3428712594108198
    (1, 8)	0.3428712594108198
    (1, 4)	0.24395572500006343
    
```python
feature_names = tfidf.get_feature_names_out()
for col in result.nonzero()[1]:
  print(feature_names[col]
         ,"  -  "
         ,result[0, col])
```
    output: 
    insights   -   0.3428712594108198
    meaningful   -   0.3428712594108198
    draw   -   0.3428712594108198
    to   -   0.3428712594108198
    methods   -   0.3428712594108198
    statistical   -   0.3428712594108198
    use   -   0.3428712594108198
    scientists   -   0.3428712594108198
    data   -   0.24395572500006343
    of   -   0.0
    amounts   -   0.0
    vast   -   0.0
    analyze   -   0.0
    can   -   0.0
    algorithms   -   0.0
    learning   -   0.0
    machine   -   0.0
    data   -   0.24395572500006343

# Word2vec<br>





