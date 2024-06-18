def find_route(start, route):
	current = start
	result = [start]
	distance = 0
	while current in route:
		next, distan = route[current]  
		distance += distan
		current = next
		result.append(current)

	return result, distance
			
routes = {
	"i": ("j", 4.0),
	"a": ("b", 3.4),
	"j": ("k", 6.0),
	"c": ("d", 5.6),
	"b": ("c", 4.0)
}

print(find_route("a", routes))
print(find_route("b", routes)) 
