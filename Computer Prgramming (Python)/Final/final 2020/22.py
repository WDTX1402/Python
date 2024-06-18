def find_route(str, rte):
    start = str
    for k,v in rte.items():
        for k2,v2 in v.items():
            if

routes = {
	"i": ("j", 4.0),
	"a": ("b", 3.4),
	"j": ("k", 6.0),
	"c": ("d", 5.6),
	"b": ("c", 4.0)
}

print(find_route("a", routes))  
print(find_route("b", routes)) 
