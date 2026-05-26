class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []


    def add_review(self, review):
        self.reviews.append(review)
        print("Review added successfully")


    def count_reviews(self):
        return len(self.reviews)


    def display_reviews(self):

        print("\nBook Title :", self.title)
        print("Author :", self.author)

        print("\nReviews:")

        if len(self.reviews) == 0:
            print("No reviews available")

        else:
            for review in self.reviews:
                print("-", review)



book1 = Book("Python Basics", "John Smith")

book1.add_review("Excellent book for beginners")
book1.add_review("Easy to understand")
book1.add_review("Very informative")


book1.display_reviews()

print("\nTotal Reviews =", book1.count_reviews())