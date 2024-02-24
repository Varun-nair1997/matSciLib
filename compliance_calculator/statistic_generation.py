
import numpy as np
def statistic_generation(data):
    """
    This function will calculate all the stats such as pmax, pmin, deltaP, and the adjusted ranges for slope calculation. The shortend dataframes are not included because it is not always needed. This is designed for the load column.
    :param data: x, y pair in 2 columns called 'Load (kN)' and 'COD(mm). must be dataframe must have same column names
    :return: Dictionary containing the max, min, delta, lower limit and upper limit with reasonable key names
    """
    pmax_load = np.max(data['Load (kN)'])
    pmin_load = np.min(data['Load (kN)'])
    load_range = pmax_load-pmin_load
    scaled_load_lower_range = 0.95*pmax_load - 0.25*load_range # parametrize that 0.25??
    scaled_load_upper_range = 0.95*pmax_load
    return {'Pmax':pmax_load, 'Pmin':pmin_load, 'deltaP':load_range, 'lower_lim':scaled_load_lower_range,'upper_lim':scaled_load_upper_range}