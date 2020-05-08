import networkx as nx
import community
import matplotlib.pyplot as plt

# input: networkx graph
# output: generalized dict form of best partition using girvan_newman algorithm
def girvan_newman(G):
    partition_step = nx.algorithms.community.girvan_newman(G=G)
    best_partition = {}
    best_modularity = -1
    modularity_hist = []
    steps = []

    for step, comms in enumerate(partition_step):
        # transform to general form
        partition = {}
        for idx, comm in enumerate(comms):
            for node in comm:
                partition[node] = idx
        # calculate modularity using python-louvain
        modularity = community.modularity(partition, G)
        # for visualization
        steps.append(step)
        modularity_hist.append(modularity)
        # find best partion
        if modularity > best_modularity:
            best_modularity = modularity
            best_partition = partition
    
    # visualize girvan_newman steps in the aspect of modularity
    plt.plot(steps, modularity_hist)
    plt.xlabel('step')
    plt.ylabel('modularity')
    plt.show()

    return best_partition

# input: networkx graph
# output: generalized dict form of best partition using cnm algorithm
def cnm(G):
    comms = list(nx.algorithms.community.greedy_modularity_communities(G))
    partition = {}
    for idx, comm in enumerate(comms):
        for node in comm:
            partition[node] = idx
    return partition

# input: networkx graph
# output: generalized dict form of best partition using louvain algorithm
def louvain(G):
    partition = community.best_partition(G)
    return partition