# Bank-Note-Authentication-
Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.

Achieved 99% accuracy by implementing RFRandom Forest Classifier :

It is an ensemble tree-based learning algorithm. The Random Forest Classifier is a set of decision trees from randomly selected subset of training set. It aggregates the votes from different decision trees to decide the final class of the test object.
Ensemble Algorithm :

Ensemble algorithms are those which combines more than one algorithms of same or different kind for classifying objects. For example, running prediction over Naive Bayes, SVM and Decision Tree and then taking vote for final consideration of class for test object.

Working of Random Forest Algorithm

We can understand the working of Random Forest algorithm with the help of following steps −

    Step 1 − First, start with the selection of random samples from a given dataset.

    Step 2 − Next, this algorithm will construct a decision tree for every sample. Then it will get the prediction result from every decision tree.

    Step 3 − In this step, voting will be performed for every predicted result.

    Step 4 − At last, select the most voted prediction result as the final prediction result.



Reference:https://medium.com/machine-learning-101/chapter-5-random-forest-classifier-56dc7425c3e1
          https://medium.com/machine-learning-101/chapter-5-random-forest-classifier-56dc7425c3e1
          https://www.tutorialspoint.com/machine_learning_with_python/machine_learning_with_python_classification_algorithms_random_forest.htm
