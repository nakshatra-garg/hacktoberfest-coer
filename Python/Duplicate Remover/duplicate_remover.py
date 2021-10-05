from collections import OrderedDict

def duplicate_remover_using_set(input_list):
	'''
	Here we use the property of a Set that it can only contain unique elements.
	If we try adding same element to a Set, it simply ignores the extra additions.
	This function converts input_list into a Set, thus removing duplicates.
	Then it converts the newly formed Set back into a List and retrns it.
	'''
	return list(set(input_list))

def duplicate_remover_using_condition(input_list):
	'''
	Here firstly we create an empty list output_list to be returned as the result
	We iterate through the input_list, and add current element into output_list
	only if it doesn't exist in output_list beforehand. Hence the output_list only
	contains unique elements, which is finally returned as the result
	'''
	output_list = []
	for i in input_list:
		if i not in output_list:
			output_list.append(i)
	return output_list

def duplicate_remover_using_ordered_dict(input_list):
	'''
	Here we exploit the fact that keys of a Dictionary are unique. We use an
	Ordered dict(to maintain the input_list order), to create a dictionary
	from the input_list elements, thus eliminating duplicates in the process.
	We finally convert it back into a list and return it as the result.
	'''
	return list(OrderedDict.fromkeys(input_list)) 

if __name__ == "__main__":
	input_list = [ 1, 2, 1, 3, 3, 4, 1 ]
	print("Duplicate Remover using Set:")
	print("I/P:", input_list)
	print("O/P:", duplicate_remover_using_set(input_list))
	print("="*20)
	print("Duplicate Remover using Condition:")
	print("I/P:", input_list)
	print("O/P:", duplicate_remover_using_condition(input_list))
	print("="*20)
	print("Duplicate Remover using Ordered Dict:")
	print("I/P:", input_list)
	print("O/P:", duplicate_remover_using_ordered_dict(input_list))
