def direct_flights(graph, city_list):
    if len(city_list) == 0:
        return False, 0

    cost = 0
    graph_keys = graph.get_nodes()
    keys = dict()
    neighbors = dict()

    for item in graph_keys:
        neighbor_list = graph.get_neighbors(item)
        keys.update({f"{item.value}": item})
        neighbors.update({f"{item.value}": neighbor_list})

    if city_list[0] not in keys:
        return False, 0
    index = 0

    for place in city_list:
        index += 1
        current_neighbors = neighbors[place]
        for edge in current_neighbors:
            if index == len(city_list):
                break
            if edge.vertex.value == city_list[index]:
                cost += edge.weight
                break

    if cost > 0:
        return True, cost
    else:
        return False, 0


