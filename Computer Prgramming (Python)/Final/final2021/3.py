def count_operands_in_expr(expr):
	if not isinstance(expr, tuple):
		return 1

	else:
		left, _, right = expr
		return count_operands_in_expr(left) + count_operands_in_expr(right)


print(count_operands_in_expr((3, '**', 4)))  
print(count_operands_in_expr(((((2, '+', 4), '/', 3), '*', 2), '+', (3, '**', 4)))) 
