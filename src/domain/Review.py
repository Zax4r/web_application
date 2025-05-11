from dataclasses import dataclass

@dataclass
class Review:
    author: str
    text: str
    
    
class ReviewHandler:
    
    def __init__(self):
        self.reviews = []
    
    def add(self,author,text):
        self.reviews.append(Review(author,text))
        
    def list_reviews(self):
        return self.reviews
    
    def remove(self,index):
        self.reviews.pop(index)