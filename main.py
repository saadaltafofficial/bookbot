from stats import get_number_of_words, get_book_text, get_character_count,get_sorted_list 
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

file_path = sys.argv[1]

def sort_on(items):
    return items["num"]

def main():
	print("============ BOOKBOT ============")
	print("Analyzing book found at " + file_path + "...")
	print("----------- Word Count ----------")
	num_of_words = get_number_of_words(file_path)
	print(f"Found {num_of_words} total words")
	content = get_book_text(file_path) 
	dic_of_char = get_character_count(content)	
	print("----------- Character Count ----------")
	sorted_chars = get_sorted_list(dic_of_char)
	sorted_chars.sort(key=sort_on, reverse=True)
	for item in sorted_chars:
		print(f"{item['char']}: {item['num']}")
	print("============= END ===============")

if __name__ == "__main__":
	main()
