class A:
    def __init__(s,t,u,v):
        s.t = u
        s.u=v
        s.v=t
    def b(selveste):
        print (selveste.u)
a1 = A(1,2,3)
a1.b()

class B(A):
    def __init__(s,t:int=0,u:int=0,v:float = 0.0,w:bool = True):
        super().__init__(t,u,v)
        s.w = (w**2)**0.5
    def b(me_myself_and_i):
        print(me_myself_and_i.w)
b1 = B(1,2,3,4)
b1.b()
