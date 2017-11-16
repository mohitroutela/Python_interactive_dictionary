import	json
from difflib import get_close_matches
data=json.load(open("data.json"))


def find_meaning(word):
	word=word.lower()
	if word in data:
		return data[word]
	elif len(get_close_matches(word,data.keys(),n=1,cutoff=0.7))>0:
		yn=input("did u mean this %s word? Enter Y if yes and N if no:  " %get_close_matches(word,data.keys(),n=2,cutoff=0.6)[0])
		if yn=="Y" or yn=="y":
			return data[get_close_matches(word,data.keys(),n=2,cutoff=0.6)[0]]
		elif yn=="N" or yn=="n":
			return "the word does not exist.pls double check it"
		else :
			return "we didn't get you"


	else:
		return "the word does not exist.pls double check it"





while True:
	word=input("enter the word you want to search/press q to exit\n")
	if word=="q":
		break
	else:
		output=find_meaning(word)
		if type(output)==list:
			for item in output:
				print(item)
		else:
			print(output)
		
