def read_points_from_file(file_path):
    
   
    with open(file_path, 'r') as file:
        
        lines = file.readlines()

    # Initialize an empty list to store the points
    points = []

    # Iterate over each line
    for line in lines:
        # Split the line by comma to get x and y coordinates
        x, y = map(int, line.strip().split(','))
        
        points.append([x, y])

    return points


'''file_path = r'D:\fascinating-math\math\fourier\epicycles\output\cords.txt'  # Path to your file
points = read_points_from_file(file_path)
print(points)'''
