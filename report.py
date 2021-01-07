def CStudent
           age = 0
           marks = []
           name = ""
           total = 0
           
           def __init__ (self, name, age, marks):
              self.name   = name
              self.age    = age
              self.marks  = marks
              self.total = self.marks[0] + self.marks[1] + self.marks[2] + self.marks[3] + self.marks[4]
           
           #This function PrintMarks_Mapping is not used in this program and it explains how to use mapping in print statements
           def PrintMarks_Mapping(self):
              print "%(name)-12s" %{"name" : self.name }, 
              print "%(age)-4d" %{"age" : self.age },
              print "%(mark)-4d" %{"mark" : self.marks[0] },
              print "%(mark)-4d" %{"mark" : self.marks[1] },
              print "%(mark)-4d" %{"mark" : self.marks[2] },
              print "%(mark)-4d" %{"mark" : self.marks[3] },
              print "%(mark)-4d" %{"mark" : self.marks[4] },
              print "%(total)-4d" %{"total" : self.total }
              
           def PrintMarks(self):
              print "%-12s" %self.name, 
              print "%-4d" %self.age,
              print "%-4d %-4d %-4d %-4d %-4d" %(self.marks[0],self.marks[1],self.marks[2],self.marks[3],self.marks[4] ),
              print "%-4d" %self.total
        
        print "Enter Number of Students: ",
        maxstudents = 0
        maxstudents = input()
        i = 0
        studentlist = []
        #import random as r
        
        for i in range(0, maxstudents):
           marks = []
           
           name = raw_input("Enter Student Name: ")
           
           print "Enter Age: ", 
           age = input()
           print "Enter Mark for Subject1: ",
           marks.append(input())
           print "Enter Mark for Subject2: ",
           marks.append(input())
           print "Enter Mark for Subject3: ",
           marks.append(input())
           print "Enter Mark for Subject4: ",
           marks.append(input())
           print "Enter Mark for Subject5: ",
           marks.append(input())
           
           #age = r.randint(16,19)
           #for j in range(0, 5):
           #   marks.append(r.randint(30,99))
           
           s = CStudent(name, age, marks)
           studentlist.append(s)
        
        print "\n"
        print "Name         Age Sub1 Sub2 Sub3 Sub4 Sub5 Total" 
        for i in range(0, len(studentlist)):
           studentlist[i].PrintMarks()