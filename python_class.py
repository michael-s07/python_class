
class Patient:
  def __init__(self, name, age,sex, bmi, num_of_children,smoker):
    self.name = name
    self.age = age
    # add more parameters here
    self.sex= sex
    self.bmi=bmi
    self.num_of_children=num_of_children
    self.smoker=smoker
#Adding Functionality with Methods
  def estimated_insurance_cost(self):
    estimated_cost = 250 * self.age - 128 * self.sex + 370 * self.bmi + 425 * self.num_of_children + 24000 * self.smoker - 12500
    return print("{}'s estimated insurance costs is {} dollars.".format(self.name,estimated_cost))
    #Update age
  def update_age(self,new_age):
    self.age=new_age
    return print("{} is now {} years old".format(self.name,self.age))

    #Update Number of Children
  def update_num_of_children(self,new_num_of_children):
    self.num_of_children = new_num_of_children
    if self.num_of_children ==1:
      return print("{} has {} child.".format(self.name,self.num_of_children))
    else:
      return print("{} has {} children.".format(self.name,self.num_of_children))
      
#Update BMI
  def update_bmi(self, new_bmi):
    self.bmi=new_bmi
    return print("{} is now {} in BMI".format(self.name,self.bmi))

#Update smoker status
  def update_smoker(self, new_smoker):
    self.smoker=new_smoker
    if self.smoker==0:
      return print("{} is NOT a Smoker".format(self.name))
    else:
      return print("{} is a smoker".format(self.name))


      #Storing Data
  def patient_profile(self):
    patient_information={"Name":self.name, "Age":self.age, "Sex":self.sex, "BMI":self.bmi, "Number_of_Children":self.num_of_children, "Smoker":self.smoker}
    return patient_information


patient1 = Patient("John Doe", 25, 1, 22.2, 0, 0)
print(patient1.name)
patient1.estimated_insurance_cost()
patient1.update_age(33)
patient1.estimated_insurance_cost()
patient1.update_num_of_children(1)
patient1.estimated_insurance_cost()
print(patient1.patient_profile())


    