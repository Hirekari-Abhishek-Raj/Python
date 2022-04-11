class Movie:
	def __init__(self,length_in_minutes,num_characters,language):
		self.length_in_minutes=length_in_minutes
		self.num_characters=num_characters
		self.language=language
	def printMovie(self):
		print("This is a",self.language,"movie with",self.num_characters ,"characters and is", self.length_in_minutes ,"minutes long.")
language=str(input())		
characters=int(input())
minutes=int(input())
M1=Movie(minutes,characters,language)
M1.printMovie()
