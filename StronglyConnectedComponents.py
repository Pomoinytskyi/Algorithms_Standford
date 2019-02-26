import random
import sys
from collections import Counter
from datetime import datetime

# nodesCount = 8
nodesCount = 875714
topologicalOrder = []
graph = {}
results = []


class Node:
    def __init__(self, index=0):

        self.Id = index
        self.Next = []
        self.IsVisited = False
        self.Order = -1
        self.Previous = []

    def __str__(self):
        next = ''.join(str(e.Id) + ', ' for e in self.Next)
        return "{} - {}".format(self.Id, next)


def DFS():
    print("DFS")
    ordering = 1
    source = None
    stack = []
    dic = {}
    for index in range(nodesCount, 0, -1):
        node = graph[index]
        if (node.IsVisited):
            continue
        counter = 0
        source = node

        stack.append(node)
        dic[node.Id] = node

        while(len(stack) > 0):
            item = stack[-1]

            if(item.IsVisited == True):
                item.Order = ordering
                ordering = ordering + 1
                counter = counter + 1

                dic.pop(item.Id)
                a = stack.pop()

            else:
                item.IsVisited = True
                for next in item.Next:
                    if(next.IsVisited == False):
                        if (next not in dic):
                            stack.append(next)
                            dic[next.Id] = next
                        else:
                            print("e")

        # print("Item {}, count {}".format(source.Index, counter))
        results.append(counter)


def PrintGraph():
    print("---------------")
    for node in graph.values():
        print(node)


def PrintOrder():
    print("==========")
    for i, node in graph.items():
        print("{} - {}".format(node.Id, node.Order))


def ReverseAndReset():
    global graph
    print("Reverse graph")
    for index, node in graph.items():
        node.IsVisited = False
    for node in graph.values():
        a = node.Next
        node.Next = node.Previous
        node.Previous = a


def OrderGraph():
    global graph

    tempGraph = {}
    for node in graph.values():
        tempGraph[node.Order] = node
        node.Order = -1
        node.IsVisited = False
    graph = tempGraph


def Main():
    print("============== Calculate Strongly Connected Components ==================")

    print("Create nodes")

    for i in range(1, nodesCount+1):
        graph[i] = Node(i)

    print("loading edges")
    s = "lastLine"
    # fileName = "./TestData/SccTest.txt"
    fileName = "./TestData/StronglyConnectedComponents.txt"
    with open(fileName, "r") as infile:
        for line in infile:
            s = line
            line = list(map(int, line.split()))
            graph.get(line[0]).Next.append(graph.get(line[1]))
            graph.get(line[1]).Previous.append(graph.get(line[0]))

    print("Loaded")

    ReverseAndReset()
    # PrintGraph()
    DFS()
    OrderGraph()
    ReverseAndReset()
    global results
    results = []
    DFS()
    results.sort()
    res = results[-3:]
    for r in res:
        print("{}".format(r))
    # ReverseAndReset()
    # DFS()
    # PrintGraph()

    # PrintGraph()


if __name__ == "__main__":
    Main()
