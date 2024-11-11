
class Teacher:
    def description(self):
        print("I am a Teacher. I educate students.")


class Author:
    def description(self):
        print("I am an Author. I write books.")


class TutorAuthor(Teacher, Author):
    def description(self):
        
        super().description() 
        Author.description(self)  


tutor_author = TutorAuthor()


tutor_author.description()
