import os
import main_def
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
function_utils = os.path.join(MAIN_DIR,"Ongoing/Complete_Function.py")
time_utils = os.path.join(MAIN_DIR,"timer.py")
# exec(open(time_utils).read())
# exec(open(function_utils).read())


def print_param():
    return None