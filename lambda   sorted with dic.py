people=[
    {"name":"raj","age":"75","occuption":"adm"},
    {"name":"Arun","age":"10","occuption":"ssp"},
    {"name":"deepak","age":"15","occuption":"dm"},
    {"name":"gaurav","age":"55","occuption":"sdm"},
    {"name":"sonam","age":"25","occuption":"peon"},
    {"name":"tomar","age":"35","occuption":"asp"},
]

sort=sorted(people,key=lambda x:x ['age'])

print(sort)