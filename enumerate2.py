x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here

for  label, corr_x, corr_y, coor_z in zip(labels,x_coord,y_coord,z_coord):
    points.append("{}: {}, {}, {}".format(label,corr_x, corr_y, coor_z))

for point in points:
    print(point)
print("-------------------------")
#------------------------------------#
#creating dictionary of zip
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names,cast_heights))
print(cast)
print("___________________________")

#----------------------------------#

#zip to transpose data from a 4-by-3 matrix to a 3-by-4 matrix.
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)
print("--------------------------")
#----------------------------------#

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i, character in enumerate(cast):
    cast[i] = character + " " + str(heights[i])

print(cast)