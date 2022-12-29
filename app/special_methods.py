
class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('Movie object created')
    
    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration
    
    def __del__(self):
        print('movie deleted')

m = Movie('movie1','director1',60)
print(str(m))
print(len(m))

del m
print(m)