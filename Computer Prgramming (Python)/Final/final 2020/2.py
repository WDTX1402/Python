def find_route(str,rte):
    result = [str]
    current = str
    distance = 0
    while current in rte:
        next , distan = rte[current]
        distance += distan
        current = next
        result.append(current)

    return result , distance


routes = {
	
	"i": ("j", 4.0),
	"a": ("b", 3.4),
	"j": ("k", 6.0),
	"c": ("d", 5.6),
	"b": ("c", 4.0)
}
print(f"{find_route('a', routes)}")