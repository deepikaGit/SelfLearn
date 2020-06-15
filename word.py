"""
This is how we use a docString works
"""
import sys
from urllib.request import urlopen

def fetch_words(url):
	#story = urlopen('http://sixty-north.com/c/t.txt')
	url = 'http://sixty-north.com/c/t.txt'
	story = urlopen(url)
	story_words=[]
	for line in story:
		line_words = line.decode('utf-8').split()
		for word in line_words:
			story_words.append(word)
	story.close()   
	return story_words
	
	for word in story_words:
		print(word)

def print_items(items):
	for item in items:
		print(item)
		
def main():
	url = 'test'
	words = fetch_words(url)
	print_items(words)
	
if __name__ == "__main__":
	main()
	#main(sys.argv[1])
	#print(__name__)