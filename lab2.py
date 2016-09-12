import random
import graphspace_utils
import json_utils



def erdos_renyi(n,m):
    """
    generates a graph (returned as a list of nodes and a list of edges) using the Erdos Renyi model.
    """
    V = []
    E = []
    E_set = set()
    for i in range(n):           #create nodes
        V.append(str(i))

    i = 0 
    while i < m:
        u = random.choice(V)
        v = random.choice(V)
        if u == v:
            pass
        elif frozenset([u,v]) in E_set:     #skips any already added edges or edges that go to self
            pass
        else:
            E_set.add(frozenset([u,v]))
            i += 1

    for item in E_set:             #turns all the sets into lists and then appends them to E
        E.append(set_to_ls(item))
    
    return V, E


def set_to_ls(s):
    ls = []
    for item in s:
        ls.append(item)
    return ls













def main():
    for i in range(5):
        print(i, random.random())

    testList = ['A','B','C','D','E']
    for i in range(5):
        print(i,random.choice(testList))

    testV, testE = erdos_renyi(25,100)
    print(len(testV))
    print(len(testE))

    data = json_utils.make_json_data(nodes,edges,None,None,'Lab 2: Graph 2.2','Desc.',['Tag'])
    json_utils.write_json(data,'lab2.json')
    graphspace_utils.postGraph('lab2graph2-2','lab2.json','franzni@reed.edu','bio331')



if __name__ == '__main__':
    main()
