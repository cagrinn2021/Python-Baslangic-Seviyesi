##
ID={"Name":"Cagri","Surname":"Esen","Age":"26","Place_Of_Birt":"Gop"}

print(ID["Name"])
print(ID["Surname"])
print(ID["Age"])
print(ID["Place_Of_Birt"])

ID["Name"]="Cagla" # only the right side changes
print(ID["Name"])
print(ID)

#adding
ID["ID"]=12345678900
print(ID)

#in innn
users={"Cagri":{
    "Tc ":3131313,
    "Place_birt":"Ankara",
    "Age":26
},"Cagla":{
    "Tc":12312312313,
         "place birt":"gop",
                      "Age":31
}
}
print(users["Cagla"].get("Age"))
