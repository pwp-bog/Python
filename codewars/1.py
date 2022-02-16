def to_camel_case(text: str) -> str:
	array = ""
	text = text.replace("-", " ")
	text = text.replace("_", " ")
	array = text.split()
	index = []

	new_array = ""
	for i in range(len(array)):
		if array[i] == " ":
			index.append(i + 1)
		else:
			new_array += array[i]

	print(index)

	return new_array


print(to_camel_case("Camel-text_lol"))
