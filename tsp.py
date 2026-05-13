def tsp_nearest_neighbor(distance_matrix):
    n = len(distance_matrix)
    visited = [False] * n

    path = []
    total_cost = 0

    current_city = 0
    path.append(current_city)
    visited[current_city] = True

    for _ in range(n - 1):
        nearest_city = None
        min_distance = float('inf')

        for city in range(n):
            if not visited[city] and distance_matrix[current_city][city] < min_distance:
                min_distance = distance_matrix[current_city][city]
                nearest_city = city

        path.append(nearest_city)
        visited[nearest_city] = True
        total_cost += min_distance
        current_city = nearest_city

    total_cost += distance_matrix[current_city][0]
    path.append(0)

    return path, total_cost




n = int(input("Enter number of cities: "))

distance_matrix = []

print("Enter the distance matrix row by row:")

for i in range(n):
    row = list(map(int, input().split()))
    distance_matrix.append(row)

path, cost = tsp_nearest_neighbor(distance_matrix)

print("Shortest Path:", path)
print("Total Cost:", cost)


#https://github.com/SnehaGogawale/WADpractical.git