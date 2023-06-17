import thingspeak
import time
import adafruit_dht 
import board
channel_id = 1896125 # put here the ID of the channel you created before
write_key = 'PO1LRE1T9GIY8OR3' # update the "WRITE KEY"
import os
import subprocess

multi_run=subprocess.run(["killall","libgpiod_pulsein"])#code to debug error "unable to set line 25 to input", can run the code multiple times

dhtDevice_in = adafruit_dht.DHT11(board.D25)

def measure(channel):
    try:
        temperature_in = dhtDevice_in.temperature
        humidity_in = dhtDevice_in.humidity   
        if humidity_in is not None and temperature_in is not None:
            print('Temperature_IN = {0:0.1f}*C Humidity_IN = {1:0.1f}%'.format(temperature_in, humidity_in))
        else:
            print('Did not receive any reading from sensor. Please check!')
         
        response_in= channel.update({'field1': temperature_in, 'field2': humidity_in}) 
    except:
       
        time.sleep(5)
        measure(channel)

if __name__ == '__main__':
    try:
        while 1:
            channel = thingspeak.Channel(id=channel_id, api_key=write_key)
            measure(channel)
            time.sleep(5)

    except KeyboardInterrupt:
        kill()
