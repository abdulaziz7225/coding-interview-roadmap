from typing import List
from collections import deque, defaultdict


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        stop_to_buses = defaultdict(list)
        for bus_id, route in enumerate(routes):
            for bus_stop in route:
                stop_to_buses[bus_stop].append(bus_id)

        return self.bfs(routes, stop_to_buses, source, target)

    def bfs(self, routes: List[List[int]], stop_to_buses: dict, source: int, target: int) -> int:
        queue = deque()

        taken_buses = set()
        visited_stops = set()
        visited_stops.add(source)

        for bus_id in stop_to_buses[source]:
            queue.append(bus_id)
            taken_buses.add(bus_id)

        bus_count = 1

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                bus_id = queue.popleft()

                for bus_stop in routes[bus_id]:
                    if bus_stop == target:
                        return bus_count

                    if bus_stop in visited_stops:
                        continue

                    visited_stops.add(bus_stop)

                    for next_bus_id in stop_to_buses[bus_stop]:
                        if next_bus_id not in taken_buses:
                            queue.append(next_bus_id)
                            taken_buses.add(next_bus_id)

            bus_count += 1

        return -1

# n = total number of bus stops across all routes
# m = total number of unique bus stops in the graph
# b = total number of buses
# Time Complexity: O(n + m)
# Space Complexity: O(n)
