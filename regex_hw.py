import re
names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]

list2 = ["Ani 132 fddfs","Bryer churco","shriya Iyer","Vedanth $%#Sinha","barcelona","454frt htrg","Valid Name","Smriti Sthyha"]

def validate_names(names):
    #pattern = re.compile(r"^[A-Z](\w+){2,}")
    
    pattern = re.compile(r"^[A-Z][a-z]*\s+(?=[A-Z][a-z]*)(?:[A-Z][a-z]*\s*)*$")
    #pattern = re.compile(r"([A-Z][a-z]+) ([A-z]*)?\s?([A-Z][a-z]+)")
    for user_name in names:
        if re.match(pattern,user_name): 
            print(user_name)
        else:
            print("Invalid name")

validate_names(names)
