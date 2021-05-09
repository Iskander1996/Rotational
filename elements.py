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

