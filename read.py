filename ="formal.txt"

#atomic_mass={"H":1.008, "O":15.999}
def main():
    xyz = open(filename)
    names_atoms = []
    x_coordinates_atoms = []
    y_coordinates_atoms = []
    z_coordinates_atoms = []
    
    for line in xyz:
        atoms, x, y, z = line.split()
        names_atoms.append(atoms)
        x_coordinates_atoms.append(float(x))
        y_coordinates_atoms.append(float(y))
        z_coordinates_atoms.append(float(z))
   
    xyz.close
    Rotational(names_atoms,               
                x_coordinates_atoms,
               y_coordinates_atoms, 
               z_coordinates_atoms)

def check_input(names_atoms,               
                x_coordinates_atoms,
               y_coordinates_atoms, 
               z_coordinates_atoms):
    """
    checking input data: needs atoms names and their x, y ,z coordinates
    """
    if(len(names_atoms)==len(x_coordinates_atoms) and len(names_atoms)==len(y_coordinates_atoms) and len(names_atoms) == len (z_coordinates_atoms)):
        print("format of data(number of atoms, coordinates) is suitable for calculations")
    else:
        print("formate of data not correct, calculated results might be wrong")
    print("check", names_atoms)
#Coordantes center of mass
def put_masses(names_atoms):

    print(names_atoms)
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

    print(names_atoms)
    
    

def moment(names_atoms,
                x_coordinates_atoms,
                y_coordinates_atoms,
                z_coordinates_atoms):
    
    Ixx = 0
    for l in range(len(names_atoms)):
        Ixx +=  names_atoms[l]*(y_coordinates_atoms[l]**2 + z_coordinates_atoms[l]**2)
    Iyy = 0
    for m in range(len(names_atoms)):
        Iyy +=  names_atoms[m]*(x_coordinates_atoms[m]**2 + z_coordinates_atoms[m]**2)
    Izz = 0
    for l in range(len(names_atoms)):
        Izz +=  names_atoms[l]*(x_coordinates_atoms[l]**2 + y_coordinates_atoms[l]**2)
    Ixy = 0
    for l in range(len(names_atoms)):
        Ixy +=  -names_atoms[l]*(y_coordinates_atoms[l]*x_coordinates_atoms[l])
    Ixz = 0
    for l in range(len(names_atoms)):
        Ixz +=  -names_atoms[l]*(x_coordinates_atoms[l]*z_coordinates_atoms[l])
    Iyz = 0
    for l in range(len(names_atoms)):
        Iyz +=  -names_atoms[l]*(y_coordinates_atoms[l]*z_coordinates_atoms[l])
    print("A=", 16.3/ Ixx )
    print("B=", 16.3/ Iyy )
    print("C=", 16.3/ Izz)
    
    
def Rotational(names_atoms,               
                x_coordinates_atoms,
               y_coordinates_atoms, 
               z_coordinates_atoms):
   
    check_input(names_atoms,               
                x_coordinates_atoms,
               y_coordinates_atoms, 
               z_coordinates_atoms)
    put_masses(names_atoms)
    moment(names_atoms,
                x_coordinates_atoms,
                y_coordinates_atoms,
                z_coordinates_atoms)

if __name__ == "__main__":
    main()