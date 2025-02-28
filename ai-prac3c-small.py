VARIABLES = ["A", "B", "C", "D", "E", "F", "G"]
CONSTRAINTS = [("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), 
               ("B", "E"), ("C", "E"), ("C", "F"), ("D", "E"), 
               ("E", "F"), ("E", "G"), ("F", "G")]

def backtrack(assignment):
    if len(assignment) == len(VARIABLES):
        return assignment
    var=next(v for v in VARIABLES if v not in assignment)

    for value in["MONDAY","TUESDAY","WEDNESDAY"]:
        if all(assignment.get(x) != value for x, y in CONSTRAINTS if var == x or var == y):
            result= backtrack({**assignment, var: value})
            if result:return result
    return None


print(backtrack({}))



