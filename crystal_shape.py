A = int(input("what is the angle of the crystal pattern: "))
Lx =  int(input("what is the x-axis length of the crystal pattern: "))
Ly = int(input("what is the y-angle length of the crystal pattern: "))

if A == 90:
   if Lx == Ly:
       print("square crystal")
   else:
       print("rectangle crystal")
elif A == 60 or A == 120:
    if Lx == Ly:
       print ("hexagonal crystal")
else:
    if A != 60 and A != 90 and A != 120:
      if Lx == Ly:
        print("rhombic crystal")
      else:
        print("parallelogram crystal")
