<h1>Vectorization</h1>

## bag of words
# Representing words by their frequencies

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









