class NameAge:
  def __init__(self,name,age,**kwargs):
    super().__init__(**kwargs)
    self.student_name = name
    self.student_age = age
    
class ID:
  def __init__(self,studentID,**kwargs):
    super().__init__(**kwargs)
    self.student_ID = studentID
    
class Averages:
  def __init__(self,scores,**kwargs):
    super().__init__(**kwargs)
    self.scores = scores
    summation = sum(self.scores)
    self.average = summation/len(self.scores)
    
class output(NameAge,ID,Averages):
  def __init__(self,**kwargs):
    super().__init__(**kwargs)
  def student_data(self):
    print(f"STUDENT NAME : {self.student_name}")
    print(f"STUDENT AGE : {self.student_age}")
    print(f"STUDENT ID : {self.student_ID}")
    print(f"AVERAGES : {self.average}")

student = output(
    name="Alice",
    age=18,
    studentID="STU-009",
    scores=[88, 90, 92]
)

student.student_data()
