w = int(input())
h = int(input())

def BMI(w,h):
    BMI = w / ((h/100)**2)
    return BMI

print(BMI(w,h))
