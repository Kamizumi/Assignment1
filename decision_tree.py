#-------------------------------------------------------------------------
# AUTHOR: Timothy Tsang
# FILENAME: Assignment1
# SPECIFICATION: Creates a decision tree for the given csv file
# FOR: CS 4210- Assignment #1
# TIME SPENT: Years Jk the math part took like 3 hours, everything else was p chill
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
#--> add your Python code here
# X =
for row in db:
    X.append([
        1 if row[0] == "Young" else 2 if row[0] == "Prepresbyopic" else 3,
        1 if row[1] == "Myope" else 2,
        1 if row[2] == "No" else 2,
        1 if row[3] == "Reduced" else 2
    ])



#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2
#--> add your Python code here
# Y =
for row in db:
    Y.append(1 if row[4] == "Yes" else 2)

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()
