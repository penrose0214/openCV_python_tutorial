import time         #cant be changed(바꿀 필요 없음)
import board        
import busio        #library for raspberry-pi connection (literally meaning bus)
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt

i2c = busio.I2C(board.SCL, board.SDA, frequency=400000) # setup I2C
mlx = adafruit_mlx90640.MLX90640(i2c) # begin MLX90640 with I2C comm
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_8_HZ # set refresh rate
mlx_shape = (24,32)

# setup the figure for plotting
plt.ion() # enables interactive plotting
fig,ax = plt.subplots(figsize=(12,7))
therm1 = ax.imshow(np.zeros(mlx_shape),vmin=0,vmax=60) #start plot with zeros
'''changed colorbar -> scalarbar'''
cbar = fig.colorbar(therm1) # setup colorbar for temps                   
cbar.set_label('Temperature [$^{\circ}$C]',fontsize=14) # colorbar label

frame = np.zeros((24*32)) # setup array for storing all 768 temperatures
t_array = []
while True:
    t1 = time.monotonic()
    try:
        mlx.getFrame(frame) # read MLX temperatures into frame var
        data_array = (np.reshape(frame,mlx_shape)) # reshape to 24x32 --> can change the shape into any N X M matrix
        therm1.set_data(np.fliplr(data_array)) # flip left to right
        therm1.set_clim(vmin=np.min(data_array),vmax=np.max(data_array)) # set bounds
        #src_HighTempObj(therm1)
        '''on_mappbale_changed -> update_normal'''
        cbar.update_normal(therm1) # update colorbar range
        plt.pause(0.001) # required
        fig.savefig('mlx90640_test_fliplr.png',dpi=300,facecolor='#FCFCFC',bbox_inches='tight') # comment out to speed up
        t_array.append(time.monotonic()-t1)
        print('Sample Rate: {0:2.1f}fps'.format(len(t_array)/np.sum(t_array)))
    except ValueError:
        continue # if error, just read again
    
'''
    src_red_pixel(therm1)
    
    
    '''
    
    #드론말고 여러대의 라즈베리파이 