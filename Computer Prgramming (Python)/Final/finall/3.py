def find_distance(str, rte):
    if str not in rte:
        return 0
    else:
        next , distance  = rte[str]
        return distance + find_distance(next,rte)

routes = {
	"i": ("j", 4.0),
	"a": ("b", 3.4),
	"j": ("k", 6.0),
	"c": ("d", 5.6),
	"b": ("c", 4.0)
}
print(f"{find_distance('a', routes)}")