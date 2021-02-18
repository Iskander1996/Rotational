filename ="water.txt"
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

print(names_atoms)
print(x_coordinates_atoms)
print(y_coordinates_atoms)
print(z_coordinates_atoms)
