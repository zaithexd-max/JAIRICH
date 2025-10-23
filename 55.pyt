class Book:
  def __init__(self,title,author,num_pages):
    self.title = title
    self.author = author
    self.num_pages = num_pages
  def __str__(self):#Edit the return of the class
    return f"{self.title} by {self.author}"
  def __eq__(self,other):#Equal
    return self.title == other.title and self.author == other.author
  def __lt__(self,other):#Less than
    return self.num_pages < other.num_pages
  def __gt__(self,other): #Greather Than
    return self.num_pages > other.num_pages
  def __add__(self,other): #Add
    return f"{self.num_pages + other.num_pages} pages"
  def __contains__(self,keyword): #Find if certain thing contain other thing
    return keyword in self.title or keyword in self.author
  def __getitem__(self,key): #check if index is match
    if key == "title":
      return self.title
    elif key == "author":
      return self.author
  

book1 = Book("The Hobbit","J.R.R Tolkien",310)
book2 = Book("Harry Potter","J.K. Rowling",223)
print(book1)
print(book1 == book2)
print(book2 < book1)
print(book2 > book1)
print(book2 + book1)
print("Harry" in book2)
print(book1['title'])