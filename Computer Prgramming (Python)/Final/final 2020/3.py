def find_distance(node, routes):
	if node not in routes:
		return 0
	else:
		destination, distance = routes[node]
		return distance + find_distance(destination, routes)

routes = {
	
	"i": ("j", 4.0),
	"a": ("b", 3.4),
	"j": ("k", 6.0),
	"c": ("d", 5.6),
	"b": ("c", 4.0)
}
print(f"{find_distance('a', routes)}")