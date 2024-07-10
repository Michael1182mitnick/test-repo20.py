# sana all algorithm in python

def sana_all(input)
    if (input % 3 == 0) and (input % 5 == 0):
        return "SanaAll"
    if input % 3 == 0:
        return "Sana"
    if input % 5 == 0:
        return "All"
    return input 


print(sana_all(15))