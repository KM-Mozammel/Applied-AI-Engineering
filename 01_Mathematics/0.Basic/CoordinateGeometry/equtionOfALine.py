# Equation of a Line - Line through two points:
    
p1 = (0, 0)
p2 = (3, 4)

def line_equation(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m*x1
    return m, b

m, b = line_equation(p1, p2)
print(f"Line equation: y = {m}x + {b}")
