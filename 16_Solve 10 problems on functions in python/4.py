import math;

def circle_stats(radius):
    area =  math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    # return area, circumference
    return {"area": area, "circumference": circumference}


# a, c = circle_stats(5)
# print(f"The area: {a} and the circumference: {c} of circle with radius: ", 5)

data = circle_stats(5)
print(f"The area: {round(data["area"], 3)} and the circumference: {round(data["circumference"], 4)} of circle with radius: ", 5)