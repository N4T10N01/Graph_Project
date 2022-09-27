

def PathListGenerator():

    dict={}
    print("""------------------------------------------------------------------------------------------------------------""")
    print("This function helps develop the dictionary necessary for graphUpdator, but is unnecessary to directly use it")
    print("The format of the dictionary needed for graphUpdator that will be generated here is as follows:")
    print("{nodePath: str, edgePath: str, nodeID: str, edgeNodeLabel1: str, edgeNodeLabel2: str}")
    print("Optional Arguments: {weightLabels: list[str], uniqueValues: list[str], additionalPaths: dict[str : str] }")
    print("Please check UndirectedGraph documentation to obtain further information. ")
    print("\n")
    print("Generation shall now begin...")

    dict['nodePath']=input("Enter path to csv containing nodes for graph\n")
    dict['edgePath']=input("Enter path to csv containing edges for graph\n")
    dict['nodeID']=input("Enter label for row/column containing values that can uniquely identify nodes\n")
    dict['edgeNodeLabel1']=input("Enter label for row/column containing values for one end of an edge\n")
    dict['edgeNodeLabel2']=input("Enter label for row/column containing values for the other end of an edge\n")

    print("Necessary values are done. Proceeding to optional arguments.")
    print("If you wish to skip over an argument, enter \"s\" ")

    inp=input("Enter label(s) for row/column containing values for edge weights, separated by commas but no spaces\n")
    dict['weightLabel']=None if inp =="s" else inp.split(',')
    inp=input("Enter label(s) for row/column containing values unique to edges, separated by commas but no spaces\n")
    dict['uniqueValues']=[] if inp =="s" else inp.split(',')

    dict['additionalPaths']={}
    print("Enter title of csv and corresponding paths for additional features of the graph in the following format:")
    inp=input("title/path, title/path, ...:\n")

    if inp is not 's':
        for pair in [tuple.split('/') for tuple in inp.split(', ')]: 
            print(pair) 
            dict['additionalPaths'][pair[0]]=pair[1]
    
    print("Dictionary has been generated, now returning")
    print("""------------------------------------------------------------------------------------------------------------""")
    return dict
    
        
    



    








    






a=PathListGenerator()
print(a)
