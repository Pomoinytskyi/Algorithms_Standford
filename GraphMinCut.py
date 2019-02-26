import random
import sys
from collections import Counter
from datetime import datetime


class Node:
    Counter = 1000

    def __str__(self):
        s = "[ " + str(self.Index) + " ] - " + \
            ",".join([str(item.Index) for item in self.Next])
        return s

    def __init__(self, index=None):
        if(index == None):
            Node.Counter += 1
            index = Node.Counter

        self.Index = index
        self.Next = []

    def Add(self, neighbour, noDuplicates=None):
        if noDuplicates == None:
            noDup = False
        else:
            noDup = noDuplicates

        if(noDup and neighbour.Index in [item.Index for item in self.Next]):
            return
        self.Next.append(neighbour)

    def Remove(self, neighbour):
        self.Next = [x for x in self.Next if x.Index != neighbour.Index]

    def GetRandomNeighbour(self):
        node = random.choice(self.Next)
        return node

    def CreatePairNode(self, neighbour):
        result = Node()

        for node1 in self.Next:
            node1.Remove(self)

            if node1.Index != neighbour.Index:
                result.Add(node1)
                node1.Add(result)

        for node2 in neighbour.Next:
            node2.Remove(neighbour)
            if (node2.Index != self.Index):
                result.Add(node2)
                node2.Add(result)
        return result


def Cut(graph):
    keyA = random.choice(list(graph.keys()))
    nodeA = graph.get(keyA)
    nodeB = nodeA.GetRandomNeighbour()

    pairedNode = nodeA.CreatePairNode(nodeB)

    del graph[nodeA.Index]
    del graph[nodeB.Index]
    graph[pairedNode.Index] = pairedNode


def GetNode(index: int, graph):
    item = graph.get(index)
    if item == None:
        item = Node(index)
        graph[item.Index] = item
    return item


def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor


def Main():

    #print("============== Graph Min Cut ==================")
    file = open("./TestData/Graph.txt", "r")
    graph = {}
    for line in file:
        line = list(map(int, line.split()))

        node = GetNode(line[0], graph)
        graph[node.Index] = node

        for nextIndex in line[1:]:
            neighbour = GetNode(nextIndex, graph)
            node.Add(neighbour, True)
            neighbour.Add(node, True)

    random.seed(datetime.now())
    while(len(graph) > 2):
        Cut(graph)

    result = len(next(iter(graph.values())).Next)
    return result


if __name__ == "__main__":

    minValue = 10000
    for i in range(10):
        print("iteration {}".format(i))
        res = Main()
        if res < minValue:
            minValue = res

        print("Min value {}".format(minValue))

    print(res)
