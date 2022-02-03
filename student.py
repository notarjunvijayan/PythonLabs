class student:
    #Student class

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

    
    def showdata(self):
        print("Name: {}".format(self.name))
        print("Roll No: {} \n\n".format(self.rollno))

st1 = student("Arjun", 15)
st2 = student("Anoop", 16)
student.showdata(st1)
student.showdata(st2)