print("Favourite Actors List:")
print("--------- ------ -----")
print("1. Superstar Rajinikanth \n2. Thalapathy Vijay \n3. Little Superstar Simbu\n4. Nadipui Arakan SJ Suriya")
actor = input("Enter Your Favourite Actor in this List: ")
if actor == "Superstar Rajinikanth":
    print("You choosed RAJINIKANTH as a favourite actor\n Total Films acted: 168\n Total blockbuster hits: 80\n floped flims: 88")
elif actor == "Thalapathy Vijay":
    print("You choosed VIJAY as a favourite actor\n Total Films acted: 67\n Total blockbuster hits: 50\n floped flims: 17")
elif actor == "Little Superstar Simbu":
    print("You choosed SIMBU as a favourite actor\n Total Films acted: 45\n Total blockbuster hits: 32\n floped flims: 13")
elif actor == "Nadipu Arakan SJ Surya":
    print("You choosed SJ SURYA as a favourite actor\n Total Films acted: 42\n Total blockbuster hits: 35\n floped flims: 7")
else:
    print("Please Select only the following actor list")
