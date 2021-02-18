filename ="formal.txt"

#atomic_mass={"H":1.008, "O":15.999}

names_atoms = []
x_coordinates_atoms = []
y_coordinates_atoms = []
z_coordinates_atoms = []
total = 0
xyz = open(filename)

for line in xyz:
   atoms, x, y, z = line.split()
   names_atoms.append(atoms)
   x_coordinates_atoms.append(float(x))
   y_coordinates_atoms.append(float(y))
   z_coordinates_atoms.append(float(z))

xyz.close
if(len(names_atoms)==len(x_coordinates_atoms) and len(names_atoms)==len(y_coordinates_atoms) and len(names_atoms) == len (z_coordinates_atoms)):
    print("format of data(number of atoms, coordinates) is suitable for calculations")
else:
    print("formate of data not correct, calculated results might be wrong")
#Coordantes center of mass

for i in range(len(names_atoms)):
    if names_atoms[i] == "H":
        names_atoms[i] = 1.008
    elif names_atoms[i] == "C":
        names_atoms[i]=12.001
    elif names_atoms[i] == "N":
        names_atoms[i]= 14.007
    elif names_atoms[i] == "O":
        names_atoms[i] = 15.998
    else:
        print("Not reconized atom ", names_atoms)
        break
        

#for atom in range(len(names_atoms)):
   #xc[atom] = (names_atoms[atom]*x_coordinates_atoms[atom]/names_atoms[atom])
#print(xc_
   
summ = 0
for i in range(len(names_atoms)):
    summ += names_atoms[i]

xc_1 = 0
for k in range(len(names_atoms)):
    xc_1 += names_atoms[k]* x_coordinates_atoms[k]
    xc = xc_1/summ

yc_1 = 0
for k in range(len(names_atoms)):
    yc_1 += names_atoms[k]* y_coordinates_atoms[k]
    yc = yc_1/summ

zc_1 = 0
for k in range(len(names_atoms)):
    zc_1 += names_atoms[k]* z_coordinates_atoms[k]
    zc = zc_1/summ

#Moment of Inertia
Ixx = 0
for l in range(len(names_atoms)):
    Ixx +=  names_atoms[l]*(y_coordinates_atoms[l]**2 + z_coordinates_atoms[l]**2)
Iyy = 0
for m in range(len(names_atoms)):
    Iyy +=  names_atoms[m]*(x_coordinates_atoms[m]**2 + z_coordinates_atoms[m]**2)
Izz = 0
for l in range(len(names_atoms)):
    Izz +=  names_atoms[l]*(x_coordinates_atoms[l]**2 + y_coordinates_atoms[l]**2)

#Moment of Inertia
Ixy = 0
for l in range(len(names_atoms)):
    Ixy +=  -names_atoms[l]*(y_coordinates_atoms[l]*x_coordinates_atoms[l])
Ixz = 0
for l in range(len(names_atoms)):
    Ixz +=  -names_atoms[l]*(x_coordinates_atoms[l]*z_coordinates_atoms[l])
Iyz = 0
for l in range(len(names_atoms)):
    Iyz +=  -names_atoms[l]*(y_coordinates_atoms[l]*z_coordinates_atoms[l])
#Rotational cnstants
A = 16.6 / Ixx
B = 16.6 / Iyy
C = 16.6 / Izz

print(names_atoms)
print("Molecular weight= ", summ)
print("center of mass in x coord = ", xc)
print("center of mass in y coord = ", yc)
print("center of mass in z coord = ", zc)
print("Ix = ", Ixx)
print("Iy = ", Iyy)
print("Iz = ", Izz)
print("Ixy = ", Ixy)
print("Ixz = ", Ixz)
print("Iyz = ", Iyz)
print("A = ", A)
print("B = ", B)
print("C= ", C)
print(x_coordinates_atoms)
print(y_coordinates_atoms)
print(z_coordinates_atoms)
