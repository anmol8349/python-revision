

class point:
    def __init__(self,x,y):
        self.x_cod= x
        self.y_cod= y
        
    def __str__(self):
        return "<{},{}>".format(self.x_cod,self.y_cod)
    
    
    def distance(self,other):
        return ((self.x_cod - other.x_cod) **2 + (self.y_cod-other.y_cod)**2)**0.5
    
    
    def distance_from_origin(self):
        return self.distance(point(0,0))
    
    
    


class Line:
    
    def __init__(self ,A,B,C):
        self.A =A
        self.B=B
        self.C=C
        
    def __str__(self):
        return '{}x+{}y+{} = 0'.format(self.A,self.B,self.C)
    
    def point_on_line(line,point):
        if line.A*point.x_cod + line.B*point.y_cod +line.C ==0:
            print( "lies on line")
        
        else:
            print( "does not lie on line ")
    
    
    
    
    
    def shortest(line,point):
        return abs(line.A*point.x_cod +line.B*point.y_cod+line.C)/(line.A**2+line.B**2)**0.5
        
    
    
    
# ------------------------------------------------------------------------------------------------------
    
    
    
p1 = point(0,0)
p2 = point(1,2)
print(p1)
print(p2)


y = p1.distance(p2)

z=p2.distance_from_origin()
print(z)



l1 = Line(1,5,0)

p3 = point(0,1)
l1.point_on_line(p3)
short=l1.shortest(p3)
# print (l1)
print(short)


