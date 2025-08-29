print("Insert the paper thickness (milimeters)")
print("Example: 1; 20; 50000")
question = input("Insert your number: ")
def paper_thickness_calculator():
    times_folded = 0
    paper_thickness = int(question)
    fold_it = "y"
    while fold_it == "y" or fold_it == "Y" or fold_it == " " or fold_it == "":
        paper_thickness = paper_thickness * 2
        times_folded += 1
        print(f"Your paper is now {paper_thickness} mm thick")
        fold_it = input("want to continue? [y/n]: ")
    paper_thickness_mm = paper_thickness
    paper_thickness_cm = paper_thickness_mm // 10
    paper_thickness_m = paper_thickness_cm // 100
    paper_thickness_km = paper_thickness_m // 1000
    paper_thickness_miles = paper_thickness_km // 1.609
    paper_thickness_ly = paper_thickness_km // 9461000000000
    print(f"Your paper is officially {paper_thickness_mm} mm thick and where folded {times_folded} times!")
    print(f"{paper_thickness_cm} cm")
    print(f"{paper_thickness_m} m")
    print(f"{paper_thickness_km} km")
    print(f"{paper_thickness_miles} miles")
    print(f"{paper_thickness_ly} ly")
paper_thickness_calculator()
