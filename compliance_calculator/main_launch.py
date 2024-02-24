# TODO: This file can import anything it needs to use and make all the calls in a 
# Sequence that you want it to make the calls.
# There is a function already here that will be availbile as an export from the module
# See __init__.py to understand how its going to be availible and how to modify it

import pandas as pd
from compliance_calculator import compliance
from compliance_calculator import plotting
from compliance_calculator import dataprocess
from scipy.stats import linregress
import matplotlib.pyplot as plt


def start_process_main_launch(loading_data_file_path: str, unloading_data_file_path: str):

    loading = pd.read_csv(loading_data_file_path)
    unloading = pd.read_csv(unloading_data_file_path)

    Co = compliance.compliance_of_open_crack_calculation(loading)['regression_object']['slope']
    plotting.plot_unload(unloading)

    def convert_to_dict_of_dicts(input_dict):
        """
        This generates the main data structure for this project

        {Pi:
            {raw data:pd.df,
            regression data:
                {slope: float,
                intercept: float,
                r_value: float,
                p_value: float,
                std_err:float},
            compliance offset: float,
            meanP: float}}

        :param input_dict: a nested dictionary of key value pairs that connects a segment name to the segment
        :return: the above drawn out dictionary
        """
        result_dict_of_dicts = {}

        # Iterate over the input dictionary
        for key, df in input_dict.items():
            # Calculate 'C' using linregress
            slope, intercept, r_value, p_value, std_err = linregress(df['Load (kN)'], df['COD(mm)'])
            compliance_offset = (Co - slope) * 100 / slope
            meanP = df['Load (kN)'].mean()

            # Create a dictionary for the current subset
            subset_dict = {'data': df, 'C' + key[1:]: {'slope': slope, 'intercept': intercept, 'r_value': r_value,
                                                       'p_value': p_value, 'std_err': std_err},
                           'compliance_offset': compliance_offset, 'mean' + key: meanP}

            # Add the subset dictionary to the result dictionary
            result_dict_of_dicts[key] = subset_dict

        return result_dict_of_dicts

    data_dict = dataprocess.break_data_into_subsets(loading)
    dict_of_dicts = convert_to_dict_of_dicts(data_dict)

    subPlots = plotting.plot_subsets_with_regression(dict_of_dicts)
    plt.savefig('plots_of_subsets.png')
    plt.clf()
    if subPlots:
        print(subPlots)
    xy_pairs = plotting.plot_mean_vs_slope(dict_of_dicts)
    two_percent = compliance.find_first_intersection(2,xy_pairs)

    final_result = {}
    final_result["Co"] = Co
    final_result["two_percent"] = two_percent
    print(final_result)
    return final_result


if __name__ == '__main__':
    loading = input('please enter loading curve file path: ')
    unloading = input('please enter unloading curve file path: ')
    start_process_main_launch(loading, unloading)