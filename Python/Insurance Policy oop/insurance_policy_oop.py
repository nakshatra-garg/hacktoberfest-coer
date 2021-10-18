#Creating Insurance POLicy's Class
class insurance:
    def __init__(self, name, age, years):
        self.name = name
        self.age = age
        self.years = years

#Creating child class for the type of insurance
class health_insurance(insurance):
    def __init__(self, name, age, years):
        super().__init__(name, age, years)
    #Function to check if person is eligible for the insurance of this type
    def eligibility(self):
        if self.age >= 50:
            print("Applicant is not eligible for this policy.")

        else:
            print("Applicant have to pay {} per year for applying health insurance policy for {} years.".format(
                15000 // self.years, self.years))

#Creating child class for the type of insurance
class vehicle_insurance(insurance):
    def __init__(self, name, age, years, driving_license):
        super().__init__(name, age, years)
        self.driving_license = driving_license

    # Function to check if person is eligible for the insurance of this type
    def eligible(self):
        if self.driving_license == "yes":
            print("Applicant have to pay {} per year for applying vehicle insurance policy for {} years.".format(
                5000 // self.years, self.years))
        else:
            print("Applicant is not eligible for this policy")

#person's Details through input
name = input("Applicant's name : ")
age = int(input("Applicant's age : "))
years = int(input("how long applicant intend to continue his/her policy ? "))
Ptype = [health_insurance, vehicle_insurance]

#Asking user what insurance he/she wants to apply
Pselect = Ptype[int(input(    "What policy do applicant want to apply for ? \n 0: Health insurance \n 1: car insurance \n Type policy number : "))]

#Applying if else conditions to run the code with respect to the person's choice
if Pselect == Ptype[1]:
    drivingLicense = input("Do applicant have driving licence and the vehicle registered. \n Yes/No. ")
    ins = Pselect(name, age, years, drivingLicense)
    ins.eligible()
else:
    ins = Pselect(name, age, years)
    ins.eligibility()

