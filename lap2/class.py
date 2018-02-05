class person:
    def __init__(self,name, money, mood, healthRate):
        self.name=name
        self.mony=mony
        self.mood=mood
        self.healthRate=healthRate

    def sleep(self,hour):
             if(hour==7):
                 return "happy"
             if(hour<7):
                 return "tried"
             return "lazy"

    def eat(self,maels):
         if(maels==3):
             return "%100 health"
         if(maels<3):
             return "%75 health"
         return "%50 health"


    def buy(self,items):
        if(items==1):
            return "dicount 10 lE"

class employee:

        def __init__(self,id, car, email, salary,dict_to_work):
            self.id=id
            self.car=car
            self.email=email
            self.salary=salary
            self.dict_to_work=dict_to_work

        def work(self):
                if(hour==7):
                    return "happy"
                if(hour<7):
                    return "tried"
                return "lazy"
        def drive(self):
                print("my name is"+self.name);
        def refuse(self):
                print("my name is"+self.name);

 class office:
     def __init__(self,name, employee):
         self.name=name
         self.employee=employee
     def get_all_employees(self):
             print("my name is"+self.name);
     def get_employee(self):
             print("my name is"+self.name);
     def hire(self):
             print("my name is"+self.name);
     def fire(self):
             print("my name is"+self.name);
     def calculate_lateness(self):
             print("my name is"+self.name);
     def deduct(self):
             print("my name is"+self.name);
     def reward(self):
             print("my name is"+self.name);

class car:
     def __init__(self,name, fuelRate, velocity)):
         self.name=name
         self.fuelRate=fuelRate
         self.velocity=velocity
    def run(self):
            print("my name is"+self.name);
    def stop(self):
            print("my name is"+self.name);
