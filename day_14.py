# Extra Challenge: Teacher’s Salary
# A school has asked you to write a program that will calculate
# teachers' salaries. The program should ask the user to enter the
# teacher’s name, the number of periods taught in a month,
# and the rate per period. The monthly salary is calculated by
# multiplying the number of periods by the monthly rate.
# The current monthly rate per period is $20. If a teacher has
# more than 100 periods in a month, everything above 100 is
# overtime. Overtime is $25 per period. For example, if a teacher
# has taught 105 periods, their monthly gross salary should be
# 2,125. Write a function called your_salary that calculates a
# teacher’s gross salary. The function should return the
# teacher’s name, periods taught, and gross salary. Here is
# how you should format your output:
# Teacher: John Kelly,
# Periods: 105
# Gross salary:2,125

class Teacher:
    
    def __init__(self, name, periods, rate = 20, ot_rate = 25):
        self.name = name
        self.periods = periods
        self.rate = rate
        self.ot_rate = ot_rate
        
        
    def salary(self):
        self.periods = int(input("Enter Total Periods: "))
        
        if self.periods > 100:
            ot_periods = self.periods - 100
            ot_amt = ot_periods * self.ot_rate
            gross_salary = ot_amt + (self.rate * self.periods)
            
        else:
            gross_salary = self.rate * self.periods
        
        
        print(f"Gross Salary: ${gross_salary}")

teacher_one = Teacher("George", 10)
teacher_one.salary()
