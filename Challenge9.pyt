import csv
movies = [
    ["Title", "Director", "Year"],
    ["Inception", "Christopher Nolan", 2010],
    ["Avengers", "Joss Whedon", 2012],
    ["The Matrix", "Lana Wachowski", 1999]
]
file_path = "C:/Users/User/Desktop/output.csv"
try:
     with open(file_path,"w") as file:
      writer = csv.writer(file)
      for movie in movies:
       writer.writerow(movie)
except:
  print("Something went wrong")