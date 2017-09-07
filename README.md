# machine_learning_by_example



#Machine Learning:
-	Machine learning is a sub field of artificial intelligence.
-	By definition its the "computers the ability to learn without being explicitly programmed"
-	Machine learning explores the study and construction of algorithms that can learn from and make predictions on data without being explicitly programmed.
-	Machine Learning is all about learning form examples and experience rather than writing manual rules
-	One program that can solve many problems without being rewritten.
-   You write a lot of manual rules to solve the problem, in machine learning you let the algorithm decide for you from examples.

###Training data and Testing data:
-	In machine learning train your algorithm in a different dataset and test it with a different dataset.
-	Save 10% of your data as test_dataset and train the algorithm with the remaining 90% of the data and finally test the accuracy of the algorithm with the 10% of data.

###Classifier:
-	A classifier (eg. decision tree) is a function, it takes data(features) as input and assigns label to it as output
-	The technique to automatically write the classifier is called **Supervised learning**

#Supervise Learning
o	Creating a classifier by finding patterns in examples
o	First we will collect the training data(examples of the problem we want to solve)

##Supervised Classifications:
-	You have a bunch of examples and your know which is the rite one

####In machine leaning we will input features and try to get labels out of it.
Example:
- Identifying the songs based on Features 
    - in this use case are
        - Intensity of the song
        - Tempo of the song
        - Genre
        - Gender of the voice
- Based of the above input(Features) the brain decides between 2 things
    - Like
    - Don’t Like

##Decision surface:
Its the line separates one class from another class whether it can generalize to never before seen data point.

##Bayse Rule:

In probability theory and statistics, Bayes’ theorem (alternatively Bayes’ law or Bayes' rule) describes the probability of an event, based on prior knowledge of conditions that might be related to the event. For example, if cancer is related to age, then, using Bayes’ theorem, a person’s age can be used to more accurately assess the probability that they have cancer, compared to the assessment of the probability of cancer made without knowledge of the person's age.

####Examples

Suppose a drug test is 99% sensitive and 99% specific. That is, the test will produce 99% true positive results for drug users and 99% true negative results for non-drug users. Suppose that 0.5% of people are users of the drug. What is the probability that a randomly selected individual with a positive test is a user?


Despite the apparent accuracy of the test, if an individual tests positive, it is more likely that they do not use the drug than that they do. This surprising result arises because the number of non-users is very large compared to the number of users; thus the number of false positives outweighs the number of true positives. To use concrete numbers, if 1000 individuals are tested, there are expected to be 995 non-users and 5 users. From the 995 non-users, 0.01 × 995 ≃ 10 false positives are expected. From the 5 users, 0.99 × 5 ≈ 5 true positives are expected. Out of 15 positive results, only 5, about 33%, are genuine. This illustrates the importance of base rates, and how the formation of policy can be egregiously misguided if base rates are neglected.[15]
The importance of specificity in this example can be seen by calculating that even if sensitivity is raised to 100% and specificity remains at 99% then the probability of the person being a drug user only rises from 33.2% to 33.4%, but if the sensitivity is held at 99% and the specificity is increased to 99.5% then probability of the person being a drug user rises to about 49.9%.

