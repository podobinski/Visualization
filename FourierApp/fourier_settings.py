__author__ = 'benjamin'

import numpy as np


# all imports have to be done using absolute imports -> that's a bug of bokeh which is know and will be fixed.
def import_bokeh(relative_path):
    import imp
    import os
    app_root_dir = os.path.dirname(os.path.realpath(__file__))
    return imp.load_source('', app_root_dir + '/' + relative_path)


# import local modules
ff = import_bokeh('fourier_functions.py')

# general settings
# plotting
x_min=-3*np.pi
x_max=3*np.pi
y_min=-2.5
y_max=2.5
resolution=500

#function input
function_input_msg = "Choose 'my own function' for entering a function here!"
function_input_init = "sin(x) * Heaviside( (-1)^ceil(x/pi*2) )"

#fourierseries
timeinterval_start = -np.pi
timeinterval_end = +np.pi
timeinterval_length = timeinterval_end-timeinterval_start

#different functions available
function_library = [ff.hat,ff.step,ff.saw,ff.parser]
function_names = ["Hat", "Step", "Saw","my own function"]

# settings for controls
# control function type
function_init = 1

# control degree
degree_min=0
degree_max=20
degree_step=1
degree_init=5


