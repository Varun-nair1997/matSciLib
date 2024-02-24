
# TODO: This file can import anything it needs to use and make all the calls in a 
# Sequence that you want it to make the calls.
# There is a function already here that will be availbile as an export from the module
from compliance_calculator import main_launch


def start_process(loading_data_file_path: str, unloading_data_file_path: str):
    return main_launch.start_process_main_launch(loading_data_file_path, unloading_data_file_path)
