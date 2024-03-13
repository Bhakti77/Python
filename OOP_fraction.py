class fraction:

    def __init__(self,numerator,denomenator):
        self.num = numerator
        self.den = denomenator
        print(numerator,denomenator)

    def __str__(self):
       return "{}/{}".format(self.num,self.den)
    
    #we created dunder method with our logic
    def __add__(self,other):
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num,temp_den)
    
    def __sub__(self,other):
        temp_num = self.num * other.den - other.num * self.den
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num,temp_den)
    
    def __sub__(self,other):
        temp_num = self.num * other.num 
        temp_den = self.den * other.den
        return "{}/{}".format(temp_num,temp_den)
    
    def __truediv__(self,other):
        temp_num = self.num * other.den 
        temp_den = self.den * other.num
        return "{}/{}".format(temp_num,temp_den)
    
obj1 = fraction(2,3)
obj2 = fraction(4,5)
print(obj1+obj2)
print(obj1-obj2)
print(obj1*obj2)

