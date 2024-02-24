import matplotlib.pyplot as plt
from compliance_calculator.compliance import compliance_of_open_crack_calculation
import numpy as np

def plot_unload(data):
    """
    This IS SPECIFICALLY for unload, it should not be used for the load data.

    This function can be considered the main function for the purely unloading data set.

    :param data: UNLOADING data, x, y pair in 2 columns called 'Load (kN)' and 'COD(mm). must be dataframe must have same column names
    :return: N/A plots curve and line of best fit. alre prints Compliance of open-crack configuration
    """
    plot_data = compliance_of_open_crack_calculation(data)
    regression_data = plot_data['regression_object']
    selected_rows = plot_data['subset_data']

    plt.scatter(data['Load (kN)'], data['COD(mm)'], label='Selected Data') # need new name for plot
    plt.plot(selected_rows['Load (kN)'], regression_data['intercept'] + regression_data['slope'] * selected_rows['Load (kN)'], color='red', label='Regression Line')
    print('Compliance of open-crack configuration', regression_data['slope'])
    plt.xlabel('Load (kN)')
    plt.ylabel('COD(mm)')
    plt.legend()
    plt.show()

def plot_subsets_with_regression(dictionary_of_dicts):
    """
    This generates a plot of each segment along with its regression line
    :param dictionary_of_dicts: dictionary of dicts defined in the convert_to_dict_of_dicts function's documentation
    :return: N/A generates a plot
    """
    # sns.set(style="whitegrid")
    fig, ax = plt.subplots()

    # Iterate over the dictionary of dictionaries
    for key, value in dictionary_of_dicts.items():
        subset_data = value['data']
        regression_output = value['C'+key[1:]]

        # Create a scatter plot for the subset data
        ax.scatter(subset_data['Load (kN)'], subset_data['COD(mm)'], label=f'Subset {key}', alpha=0.7)

        # Plot the regression line
        x_range = np.linspace(subset_data['Load (kN)'].min(), subset_data['Load (kN)'].max(), 100)
        y_range = regression_output['intercept'] + regression_output['slope'] * x_range
        ax.plot(x_range, y_range, label=f'Regression Line (C{key[1:]}), slope={regression_output["slope"]:.2f}', color='red')

        # Set labels and legend
        ax.set_xlabel('Load (kN)')
        ax.set_ylabel('COD (mm)')
        ax.set_title('Subsets with Regression Line')
        # ax.legend()


        # Show the plot for each subset
        # plt.figure(1)
    fig.show()
    return(True)

def plot_mean_vs_slope(dictionary_of_dicts):
    """
    plots the final plot between Mean load (y-axis) vs Compliance offset (x-Axis).
    :param dictionary_of_dicts: dictionary of dicts defined in the convert_to_dict_of_dicts function's documentation
    :return: N/A plots curve of Mean load (y-axis) vs Compliance offset (x-Axis)
    """
    slopeList = []
    meanList = []

    # Iterate over the dictionary of dictionaries
    for key, value in dictionary_of_dicts.items():
        slope_data = value['compliance_offset']
        mean_data = value['mean' + key]
        slopeList.append(slope_data)
        meanList.append(mean_data)

    plt.plot(slopeList,meanList)

# Get the Line2D object from the plot
    line = plt.gca().get_lines()[0]

    # Get the data points of the line
    line_x, line_y = line.get_data()
    xy_pairs = list(zip(line_x, line_y))

    # Find the index of the target x value in the line's x values

    # Extract the corresponding y value
    plt.show()
    return xy_pairs

