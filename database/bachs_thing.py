
from pyrosm import OSM
from pyrosm import get_data
import osmnx as ox
import matplotlib.pyplot as plt
import networkx as nx
import shapely.geometry
import random

def GetPath(source, target, G):
    s = list(zip(*source.geometry.centroid.xy))[0]
    e = list(zip(*target.geometry.centroid.xy))[0]
    source_node = ox.nearest_nodes(G, s[0], s[1])
    target_node = ox.nearest_nodes(G, e[0], e[1])
    route = nx.shortest_path(G, source_node, target_node, weight="length")
    return route

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #fp = get_data("test_pbf")
# Initialize the OSM parser object

    #bounding_box = OSM("Helsinki.osm.pbf").get_boundaries(name="Helsinki")

    #print(bounding_box['geometry'].values[0])
    osm = OSM("Helsinki.osm.pbf", [24.92, 60.14, 25.2, 60.24])

    walkNodes, walkEdges = osm.get_network("walking", nodes=True)
    building = osm.get_buildings()

    fig, ax = plt.subplots(figsize=(12, 12))

    walkEdges.plot(color="blue", figsize=(12, 12), lw=1, alpha=0.5, ax = ax)

    #simulate travel
    n = 50
    droprate = 0.01

    shops = []
    buildings = []
    if building is not None:
        for i in building.iterrows():
            if i[1]["shop"] is not None:
                shops.append(i[1])
            buildings.append(i[1])

    G = osm.to_graph(walkNodes, walkEdges, graph_type="networkx")

    print("Start simulation")
    for i in range(n):
        #incompleteRoad = walkEdges.copy()
        #droplist = [random.randint(0, len(incompleteRoad) - 1) for i in range(int(len(walkEdges) * droprate))]
        #droplist = list(set(droplist))
        #for n in droplist:
        #    incompleteRoad = incompleteRoad.drop(labels=n, axis=0)

        path = GetPath(shops[random.randint(0, len(shops) - 1)], buildings[random.randint(0, len(buildings) - 1)], G)
        cordPathx = [G.nodes[i]['x'] for i in path]
        cordPathy = [G.nodes[i]['y'] for i in path]

        ax.plot(cordPathx, cordPathy, color="red", lw=5, alpha = min(2 / n, 1))
        print("done" + str(i))

    #if building is not None:
    #    for i in building.iterrows():
    #        if i[1]["shop"] is not None:
                #print(i.geometry)

    #    print(road)
    #building.plot(ax = ax)

    plt.show()

