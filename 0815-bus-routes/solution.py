from math import inf
from typing import Dict, List, Set

class Solution:
	# since all edges are of length one, we can just use breadth first search
	def find_shortest_paths(self, n_vertices: int, edges: Dict[int, Set[int]], source: int) -> List[int]:
		shortest_paths = [0 if i == source else inf for i in range(n_vertices)]
		
		start_from = [source]
		next_start_from = []
		
		while len(start_from) > 0:
			for vertex in start_from:
				if vertex in edges:
					for neighbor in edges[vertex]:
						if shortest_paths[neighbor] == inf:
							shortest_paths[neighbor] = shortest_paths[vertex] + 1
							next_start_from.append(neighbor)
			start_from, next_start_from = next_start_from, start_from
			next_start_from.clear()
			
		return shortest_paths
	
	def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
		# special case: if we're already where we're going, then we don't
		# need to take a bus anywhere
		if source == target:
			return 0
		
		n_routes = len(routes)
		
		stops = {}
		for i, route in enumerate(routes):
			for stop in route:
				if stop in stops:
					stops[stop].append(i)
				else:
					stops[stop] = [i]
					
		# special case: if either where we are or where we're going is not
		# serviced by the bus system, then there's no possible route
		if source not in stops or target not in stops:
			return -1
		
		edges = {}
		for k, v in stops.items():
			for route1 in v:
				for route2 in v:
					if route1 != route2:
						if route1 in edges:
							edges[route1].add(route2)
						else:
							edges[route1] = {route2}
							
		min_n_buses = n_routes + 1
		
		for route1 in stops[source]:
			shortest_paths = self.find_shortest_paths(n_routes, edges, route1)
			for route2 in stops[target]:
				if shortest_paths[route2] < min_n_buses:
					min_n_buses = shortest_paths[route2]
					
		if min_n_buses < n_routes + 1:
			return min_n_buses + 1
		else:
			return -1
		
def main() -> None:
	test_cases = [
	[[[1,2,7],[3,6,7]], 1, 6],
	[[[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12],
	]
	
	solution = Solution();
	
	for inputs in test_cases:
		routes, source, target = inputs
		
		test = solution.numBusesToDestination(routes, source, target)
		
		print(test)
		
if __name__ == '__main__':
	main()
	