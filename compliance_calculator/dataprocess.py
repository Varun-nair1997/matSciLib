from compliance_calculator.statistic_generation import statistic_generation
from scipy.stats import linregress


def break_data_into_subsets(curve_df):
    """
    This function breaks a data set down by a fraction dicated by the delta P value the formula for reduction is:

    LOWER LIMIT: current max in the data frame - 10% of delta P
    UPPER LIMIT: current maximum after removing the last window

    :param curve_df: x, y pair in 2 columns called 'Load (kN)' and 'COD(mm). must be dataframe must have same column names
    :return: Dictionary of smaller dataframes keyed to the appropriate symbols from the literature
    """
    # TODO: redo boundaries need overlap on subset boundaries refer dox
    # TODO: mean of n-1th subset is Pmin for nth subset (arithmetic mean of subset)

    sorted_df = curve_df.sort_values(by='Load (kN)', ascending=True)

    print(sorted_df.columns)

    stats = statistic_generation(curve_df)
    constant = stats['deltaP']

    threshold = 0.95 * sorted_df['Load (kN)'].max()
    sorted_df = sorted_df[sorted_df <= threshold]

    # Initialize the DataFrame to store subsets

    subsets_dict = {}

    # Iterate over the data to create subsets
    while not sorted_df.empty:
        Pmin = sorted_df.iloc[0]['Load (kN)']
        # Calculate the edges of the subset
        lower_bound = Pmin
        upper_bound = Pmin + (0.1 * constant)

        # I want this logic to work till global 0.95Pmax. It means I want my subsets from data less than 95% of maximum load.

        # Filter data points within the specified range
        subset = sorted_df[(sorted_df['Load (kN)'] >= lower_bound) & (sorted_df['Load (kN)'] <= upper_bound)]

        # Remove the subset from the sorted_df, data more than mean load of previous segment
        sorted_df = sorted_df[sorted_df['Load (kN)'] > subset['Load (kN)'].mean()]

        # Add the subset to the DataFrame
        key = f'P{len(subsets_dict) + 1}'
        subsets_dict[key] = subset

        # print(f'P{len(subsets_df) + 1})')
        print(lower_bound)
        print(upper_bound)
    return subsets_dict