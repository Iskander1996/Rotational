filename ="co2.txt"

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

for i in range(2):
    if names_atoms[i] == "C":
        names_atoms[i] = 12.011
    else:
        names_atoms[i] = 14.007

#for atom in range(len(names_atoms)):
   #xc[atom] = (names_atoms[atom]*x_coordinates_atoms[atom]/names_atoms[atom])
#print(xc_
summ = 0
for i in range(2):
    summ += names_atoms[i]

xc_1 = 0
for k in range(2):
    xc_1 += names_atoms[k]* x_coordinates_atoms[k]
    xc = xc_1/summ

yc_1 = 0
for k in range(2):
    yc_1 += names_atoms[k]* y_coordinates_atoms[k]
    yc = yc_1/summ

zc_1 = 0
for k in range(2):
    zc_1 += names_atoms[k]* z_coordinates_atoms[k]
    zc = zc_1/summ

#Moment of Inertia
Ix = 0
for l in range(2):
    Ix +=  names_atoms[l]*(x_coordinates_atoms[l] - xc)**2
Iy = 0
for l in range(2):
    Iy +=  names_atoms[l]*(y_coordinates_atoms[l] - yc)**2
Iz = 0
for l in range(2):
    Iz +=  names_atoms[l]*(z_coordinates_atoms[l] - zc)**2

#Rotational cnstants

C = 16.6 / Iz
print(names_atoms)
print("Molecular weight= ", summ)
print("center of mass in x coord = ", xc)
print("center of mass in y coord = ", yc)
print("center of mass in z coord = ", zc)
print("Ix = ", Ix)
print("Iy = ", Iy)
print("Iz = ", Iz)

print("C = ", C)

print(x_coordinates_atoms)
print(y_coordinates_atoms)
print(z_coordinates_atoms)
