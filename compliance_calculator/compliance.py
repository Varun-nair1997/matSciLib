
from scipy.stats import linregress
from compliance_calculator.statistic_generation import statistic_generation

def compliance_of_open_crack_calculation(data):
    """
    This function calculates the compliance of open crack calculation. It does this by calculating a linear fit to a reduced data set of load data. It also saves this as a global variable called Co that is used in other places of this program (in the class it is a class variable and is also accesible globally throughout the class
    :param data: x, y pair in 2 columns called 'Load (kN)' and 'COD(mm). must be dataframe must have same column names
    :return: Dictionary containing the information needed to plot the regression line and the subset of points used to generate the line
    """
    stats = statistic_generation(data)
    data_edges = [stats['lower_lim'], stats['upper_lim']]
    selected_rows = data[(data['Load (kN)'] >= data_edges[0]) & (data['Load (kN)'] <= data_edges[1])]
    slope, intercept, r_value, p_value, std_err = linregress(selected_rows['Load (kN)'], selected_rows['COD(mm)'])
    regression_object = {'slope':slope, 'intercept':intercept,'r_value':r_value, 'p_value':p_value, 'std_err':std_err}
    return {'regression_object':regression_object, 'subset_data':selected_rows}

def find_first_intersection(vertical_line_x, curve_points):
    for i in range(len(curve_points) - 1):
        x1, y1 = curve_points[i]
        x2, y2 = curve_points[i + 1]

        # Check if the segment is vertical
        if x1 == x2:
            # Check if the vertical line intersects this segment
            if vertical_line_x == x1:
                return vertical_line_x, min(y1, y2)

        # Check if the segment intersects the vertical line
        elif (x1 < vertical_line_x < x2) or (x2 < vertical_line_x < x1):
            m = (y2 - y1) / (x2 - x1)
            y_intersect = m * (vertical_line_x - x1) + y1
            return vertical_line_x, y_intersect