from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    # Euclidian distance calculation
    # tile() will transform the shape of inX (shape=(1, 2) into inX (shape=(4, 2)))
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    # matrix.sum(axis=x) will sum all elements along the selected axis
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5
    # argsort() sorts indices([1.48, 1.4, 0.0, 0.1]) --> ([3, 2, 0, 1])
    # so it calculates at which indices the numbers need to be so every right element is bigger then the left element
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        # calculates which label belongs to the i th neighbor
        # the smaller the i index so closer the neighbor
        voteIlabel = labels[sortedDistIndicies[i]]
        # counts how often a label occurs
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount

def file2matrix(filename):
    love_dictionary = {'largeDoses': 3, 'smallDoses': 2, 'didntLike': 1}
    fr = open(filename)
    arrayOfLines = fr.readlines()
    numberOfLines = len(arrayOfLines)
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayOfLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        if listFromLine[-1].isdigit():
            classLabelVector.append(int(listFromLine[-1]))
        else:
            classLabelVector.append(love_dictionary.get(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector

def plotDatingMatrixIceCreamVsVideoGames(datingDataMat, datingLables):
    fig = plt.figure()
    fig.suptitle('Ice Cream vs Video Games', fontsize=20)
    ax = fig.add_subplot(111)
    ax.set_ylabel('Liters of Ice Cream Consumed Per Week', fontsize=14)
    ax.set_xlabel('Percentage of Time Spent Playing Video Games', fontsize=14)
    ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15.0*array(datingLables), array(datingLables))
    plt.show()

def plotDatingMatrixVideoGamesVsFlyierMiles(datingDataMat, datingLables):
    fig = plt.figure()
    fig.suptitle('Ice Cream vs Video Games', fontsize=20)
    ax = fig.add_subplot(111)
    ax.set_ylabel('Percentage of Time Spent Playing Video Games', fontsize=14)
    ax.set_xlabel('Frequent Flyier Miles Earned per Year', fontsize=14)
    ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1], 15.0*array(datingLables), array(datingLables))
    ax.legend()
    print array(datingLables)
    plt.show()

group, labels = createDataSet()
print classify0([0, 0], group, labels, 3)
datingDataMat, datingLables = file2matrix('datingTestSet.txt')
print datingDataMat
print len(datingLables)
#plotDatingMatrixIceCreamVsVideoGames(datingDataMat, datingLables)
plotDatingMatrixVideoGamesVsFlyierMiles(datingDataMat, datingLables)