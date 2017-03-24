#usfocuses
##NLP Analysis of the Congressional records and the Presidential Speeches

###Business Understanding

The Congressional records and the Presidential Speeches contain a large amount of information regarding the past major events of United States.   The massiveness of data makes it difficult to look up for relevant information of certain topics at certain periods that we are interested in and identify the historical trends of specific topics over the past years.  With the methods of web scraping, TF-IDF(term frequency–inverse document frequency), and search algorithm,  it is possible to find out the most relevant important words for a given topic or keywords. It would be convenient for historians to find the relevant information regarding certain topics of certain periods and for teachers to teach the history class. The main goal of this project is to address the questions proposed above.



###Data Understanding
The Congressional Record that is published daily when the congress is in session is the official record of the proceedings and debates of the United States congress.

###Data preparation
TF-IDF, Bag of words, and parts of Speeches tagging are some techniques for text precessing.

###Modeling TBD
Multinomial classification models such as multinomialNB, Logistic Regression and Random Forest are applied.

###Evaluation TBD
One way to identify the accuracy of the model would be to check the trends of topics over time since the trend of a certain topic is known in the history.
For multinomial classification problem, plotting the confusion matrix is a good method to find out how well the model performs on classifying different labels.

####Deployment TBD
