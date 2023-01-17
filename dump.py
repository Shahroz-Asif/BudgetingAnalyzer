import math
import numpy
import pandas
import matplotlib.pyplot as plt

month_mappings = [ "JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC" ]

"""
SAME MONTHLY PATTERN: 1
DECREASING-STABLE MONTHLY PATTERN: 2, 4
DIFFICULT (STABILIZES): 3
"""

def generate_smoothened_points(points, degree):
    smoothened_points = []
    for i in range(len(points) - 1):
        prev_point = points[i - 1]
        curr_a_point = points[i]
        curr_b_point = points[(i + 1) % len(points)]
        next_point = points[(i + 2) % len(points)]

        
        point_range = numpy.array([prev_point, curr_a_point, (curr_a_point[0] + 1, curr_b_point[1]), (curr_a_point[0] + 2, next_point[1])])
        point_x = point_range[:,0]
        point_y = point_range[:,1]

        smoothing_eq = numpy.poly1d(numpy.polyfit(point_x, point_y, degree))
        smooth_x = numpy.linspace(curr_a_point[0], curr_b_point[0], 50)
        smooth_y = smoothing_eq(smooth_x)

        smooth_coord = [ ( smooth_x[i], smooth_y[i] ) for i in range(len(smooth_x)) ]
        smoothened_points.extend(smooth_coord)

    return smoothened_points

def create_graph(points, degree):
    x_points = points[:,0]
    y_points = points[:,1]

    poly_coeff = numpy.polyfit(x_points, y_points, degree)
    poly_func = numpy.poly1d(poly_coeff)

    x_new = numpy.linspace(x_points[0], x_points[-1] + 1, 50)
    y_new = poly_func(x_new)

    plt.plot(x_points, y_points, "o", x_new, y_new)
    plt.xlim([ x_points[0] - 1, x_points[-1] + 2 ])
    plt.show()

purchase_dataframe = pandas.read_csv("./Purchase.csv")
number_of_entries = purchase_dataframe.index[-1]
purchase_entries = purchase_dataframe.values[:-1]

selected_entries = [ purchase_entry for purchase_entry in purchase_entries if purchase_entry[2] not in [ 11, 28 ] ]

sorted_entries = [ [] for i in range(28) ]
for selected_entry in selected_entries:
    normalised_entry = [ selected_entry[0], month_mappings.index(selected_entry[1]) ]
    normalised_entry.extend(selected_entry[2:])
    sorted_entries[math.floor(selected_entry[2] - 1)].append(normalised_entry)

for sorted_entry in sorted_entries:
    required_data = [ [ entry_data[1] + (12 * (entry_data[0] % 2018)), entry_data[3] ] for entry_data in sorted_entry ]

    # 7, 19, 30, 42  #1 PEAK SHIFT: 2   
    create_graph(numpy.array(generate_smoothened_points(required_data, 7)), 7)

    # monthly_data = [ [] for i in range(12) ]
    # for data in required_data:
    #     month_index = data[0] % 12
    #     monthly_data[month_index].append([ (data[0] - month_index) // 12, data[1] ])
    
    # for month_data in monthly_data:
    #     print(month_data)

    # # If linear fit, extrapolate
    # # Non-linear fit


    # for month_data in monthly_data:
    #     create_graph(numpy.array(generate_smoothened_points(month_data, 1)), 1)
    #     create_graph(numpy.array(generate_smoothened_points(month_data, 7)), 7)

# print(len(first_product_entries), first_product_entries)


raise 
data_keys = [ key for key in purchase_dataframe.keys() ]

def count_entries():
    entry_count = [ 0 for i in range(28) ]
    for j in range(len(selected_entries)):
        purchase_entry = selected_entries[j]

        if purchase_entry[2] == math.nan:
            continue
        
        entry_count[math.floor(purchase_entry[2] - 1)] += 1

    for i in range(1, len(entry_count) + 1):
        print("Total ProductID " + str(i) + ": " + str(entry_count[i - 1]))

raise

categories = (
    "Water", "Diary", "Vegetables", "Fruits", "Grains", "Meat", "Beverages", "Snacks", "Electronics", "Hygiene"
)

# ID, Essentiality, Category
purchasable_types = (
    ("Water", 100, "Water")
)

# ID, Name, Quality, CostPerUnit, UnitType
purchasables = (
    (1, "Water", 100, 3.5, "litres")
)

# ID, PurchasableID, AmountOfUnits, PurchaseMonth, PurchaseYear
purchases = (
    (1, 1, 20, 0, 2021),
    (1, 1, 22, 1, 2021),
    (1, 1, 30, 2, 2021),
    (1, 1, 45, 3, 2021),
    (1, 1, 57, 4, 2021),
    (1, 1, 65, 5, 2021),
    (1, 1, 64, 6, 2021),
    (1, 1, 60, 7, 2021),
    (1, 1, 46, 8, 2021),
    (1, 1, 35, 9, 2021),
    (1, 1, 25, 10, 2021),
    (1, 1, 20, 11, 2021),
    (1, 2, 5, 0, 2021),
    (1, 2, 5, 1, 2021),
    (1, 2, 6, 2, 2021),
    (1, 2, 8, 3, 2021),
    (1, 2, 6, 4, 2021),
    (1, 2, 6, 5, 2021),
    (1, 2, 6, 6, 2021),
    (1, 2, 6, 7, 2021),
    (1, 2, 5, 8, 2021),
    (1, 2, 5, 9, 2021),
    (1, 2, 5, 10, 2021),
    (1, 2, 4, 11, 2021)
    # (1, 2, 5, 0, 2022),
    # (1, 2, 6, 1, 2022),
    # (1, 2, 8, 2, 2022),
    # (1, 2, 6, 3, 2022),
    # (1, 2, 6, 4, 2022),
    # (1, 2, 6, 5, 2022),
    # (1, 2, 6, 6, 2022),
    # (1, 2, 5, 7, 2022),
    # (1, 2, 5, 8, 2022),
    # (1, 2, 5, 9, 2022),
    # (1, 2, 4, 10, 2022),
    # (1, 2, 4, 11, 2022),
)

water_points = [ ( purchase[3] + (purchase[4] % 2021), purchase[2] ) for purchase in purchases if purchase[1] == 1 ]
oil_points = [ ( purchase[3] + (12 * (purchase[4] % 2021)), purchase[2] ) for purchase in purchases if purchase[1] == 2 ]
# oil_points_precise = numpy.array([
#     (0.0, 4),
#     (0.2, 4.1),
#     (0.4, 4.2),
#     (0.6, 4.4),
#     (0.8, 4.8),
#     (1.0, 5.4),
#     (1.2, 6.5),
#     (1.4, 7.2),
#     (1.6, 7.6),
#     (1.8, 7.9),
#     (2.0, 8),
#     (2.2, 8.2),
#     (2.4, 8.3),
#     (2.6, 8.2),
#     (2.8, 8),
#     (3.0, 5),
#     (3.2, 5),
#     (3.4, 5),
#     (3.6, 5),
#     (3.8, 5),
#     (4.0, 4),
#     (4.2, 4),
#     (4.4, 4),
#     (4.6, 4),
#     (4.8, 4)
# ])

# filled_oil_points = [ oil_points[0] ]

# for i in range(len(oil_points) - 1):
#     diff = oil_points[i + 1][0] - oil_points[i][0]

def generate_smoothened_points(points):
    smoothened_points = []
    for i in range(len(points) - 1):
        prev_point = points[i - 1]
        curr_a_point = points[i]
        curr_b_point = points[(i + 1) % len(points)]
        next_point = points[(i + 2) % len(points)]

        print(i, prev_point, curr_a_point, curr_b_point, next_point)
        
        point_range = numpy.array([prev_point, curr_a_point, (curr_a_point[0] + 1, curr_b_point[1]), (curr_a_point[0] + 2, next_point[1])])
        print(point_range)
        point_x = point_range[:,0]
        point_y = point_range[:,1]

        smoothing_eq = numpy.poly1d(numpy.polyfit(point_x, point_y, 6))
        smooth_x = numpy.linspace(curr_a_point[0], curr_b_point[0], 50)
        smooth_y = smoothing_eq(smooth_x)

        smooth_coord = [ ( smooth_x[i], smooth_y[i] ) for i in range(len(smooth_x)) ]
        smoothened_points.extend(smooth_coord)

    return smoothened_points

def create_graph(points):
    print(points)
    x_points = points[:,0]
    y_points = points[:,1]

    poly_coeff = numpy.polyfit(x_points, y_points, 6)
    poly_func = numpy.poly1d(poly_coeff)

    x_new = numpy.linspace(x_points[0], x_points[-1], 50)
    y_new = poly_func(x_new)

    plt.plot(x_points, y_points, "o", x_new, y_new)
    plt.xlim([ x_points[0] - 1, x_points[-1] + 1 ])
    plt.show()

generate_smoothened_points(water_points)
# ori_x = numpy.array([0, 1, 2, 3])
# ori_y = numpy.array([5, 6, 8, 6])
