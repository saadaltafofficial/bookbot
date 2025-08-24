
def get_book_text(path_of_file):
        file_contents = ""
        with open(path_of_file) as f:
                file_contents = f.read()
        return file_contents

def get_number_of_words(path_of_file):
        num_of_words = get_book_text(path_of_file).split()
        return len(num_of_words)

def get_character_count(content):
	freq = {}
	for char in content.lower():
		if char.isalpha():  # Only count alphabetic characters
			freq[char] = freq.get(char, 0) + 1
	return freq

def get_sorted_list(dict):
	sorted_list = []
	for item in dict:
		sorted_list.append({"char": item, "num": dict[item]})
	return sorted_list
	
