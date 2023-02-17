import numpy as np
import operator

def createDataSet():
  group = np.array(
    [
      [1,101],
      [5,89],
      [108,5],
      [115,8]
    ]
  )
  labels = ['爱情片','爱情片','动作片','动作片']
  return group, labels

def classify0(inX, dataSet, labels, k):
  dataSize = dataSet.shape[0]
  diffMat = np.tile(inX, (dataSize, 1)) - dataSet
  sqDiffMat = diffMat**2
  sqDistances = sqDiffMat.sum(axis=1)
  distances = sqDistances**0.5
  sortDistances = distances.argsort()

  classCount = {}
  for i in range(k):
    label = labels[sortDistances[i]]
    classCount[label] = classCount.get(label, 0) + 1
  
  sortClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
  return sortClassCount[0][0]

if __name__ == '__main__':
  group, labels = createDataSet()

  # tmpgp = np.array(
  #   [
  #     [0,101],
  #     [0,89],
  #     [108,0],
  #     [115,0]
  #   ]
  # )
  # print(group)
  # print(group.sum(axis=1).argsort())

  test = [10, 20]
  print(classify0(test, group, labels, 3))
