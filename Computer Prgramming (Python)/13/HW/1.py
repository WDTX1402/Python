def print_btree(tree, dpt=0):
    if isinstance(tree,int):
        print("." * dpt + str(tree))
    else:
        print("." * dpt + str(tree[0]))
        if len(tree) >= 1:
            for child in tree[1]:
                print_btree(child,dpt + 1)

tree = [1,[[11, [111, 112]],[12, [121, [122, [1221, 1222]]]]]]

print_btree(tree)
