import sys
import community
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mpcolors



def get_graph(data,image):
    G=nx.Graph()
    L2 = []
    max_modularity = -1
    communities = []
    for line in open(data):
        line1 = line.split(' ')
        L1 = []
        for i in line1:
            i1 = i.replace("\n","")
            L1.append(int(i1))
            L2.append(int(i1))
        G.add_edge(*L1)
    nodes = list(set(L2))
    H = G.copy()
    g = G
    for i in range(len(nodes)-1):
        print nodes
        dict_betweenness = nx.edge_betweenness_centrality(g, k=None, normalized=True, weight=None, seed=None)
        print dict_betweenness
        max_betweenness = max(dict_betweenness.items(),key = lambda x:x[1])[0]
        print max_betweenness
        g.remove_edge(*max_betweenness)
        connected_subgraphs = nx.connected_components(g)
        a = 0
        connected_subgraphs_dict = {}
        for ii in connected_subgraphs:
            connected_subgraphs_dict[a] = ii
            a = a + 1
            print ii
#        connected_subgraphs_list=connected_subgraphs.neighbors()
#        print connected_subgraphs_list
        print "000"
        print connected_subgraphs_dict
        number_of_community = 0
        community_dict = {}
        for key in connected_subgraphs_dict:
            print key
#            number_of_community = number_of_community + 1
            for iiii in connected_subgraphs_dict[key]:
                #print number_of_community
                community_dict[iiii] = number_of_community
            number_of_community = number_of_community + 1
            print community_dict
        print "888"
        modularity = community.modularity(community_dict,G)
        if modularity > max_modularity:
            max_modularity = modularity
            print max_modularity
            print 666
            communities = list(connected_subgraphs_dict.items())
            connected_subgraphs_dict_final = community_dict
    print communities
    print 777
    communities_list = []
    for community_ in communities:
        c = list(community_[1])
        print sorted(c)
        print 999
        communities_list.append(c)
    print communities_list
    values = [connected_subgraphs_dict_final.get(node) for node in H.nodes()]
#    pos = nx.spring_layout(G)
#    colors = mpcolors.cnames.values()
    nx.draw_spring(H, cmap = plt.get_cmap('jet'), node_color = values, node_size=300,with_labels=True)
#    nx.draw_networkx(G,nodelist= communities_list,alpha=0.2)
#    ec = nx.draw_networkx(G, pos, node_color = colors, alpha=0.2)
#    nc = nx.draw_networkx_nodes(G, pos, nodelist=nodes, node_color=colors, with_labels=True,node_size=100, cmap=plt.cm.jet)
    plt.savefig(image)



if __name__ == '__main__':
    inputdata = sys.argv[1]
    inputdata1 = sys.argv[2]
    get_graph(inputdata,inputdata1)
