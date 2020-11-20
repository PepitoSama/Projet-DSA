import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
import csv

arrayRel = []

with open('csv/mails.csv') as csvFile:
    mailCSV = csv.reader(csvFile,delimiter=',')
    labelRow = next(mailCSV)
    
    for row in mailCSV: #On boucle sur chaque ligne
        if (row[0],row[1]) not in arrayRel: #On vérifie qu'on ne fait pas de duplications des relations
            arrayRel.append((row[0],row[1]))

G = nx.DiGraph()
G.add_edges_from(arrayRel)

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos,node_size=50)
nx.draw_networkx_edges(G,pos, edgelist=G.edges(),edge_color='black')
nx.draw_networkx_labels(G,pos)

plt.show()