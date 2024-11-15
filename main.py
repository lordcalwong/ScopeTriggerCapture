from ds1054z import DS1054Z
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np
import matplotlib.image as mpimg
ipaddr = '169.254.131.118'

scope = DS1054Z(ipaddr)
print("Connected to: ", scope.idn)
print("Currently displayed channels: ", str(scope.displayed_channels))

bmap_scope = scope.display_data
display(Image(bmap_scope))
scope.set_channel_scale(1, 0.5)

ds1054z save-data --filename samples_{ts}.txt

import pyvisa

from time import sleep
from q

rm = pyvisa.ResourceManager()
mp_dmm = rm.open_resource('ASRL/dev/ttyUSB0')

mp_dmm.baud_rate = 115200
print(mp_dmm.query("*IDN?"))
print(mp_dmm.query("MEAS?").strip())
