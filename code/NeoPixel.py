
import time


import board


import digitalio


import neopixel_write


pixels = digitalio.DigitalInOut(board.GP13)
pixels.direction = digitalio.Direction.OUTPUT


num_pixels = 12


frame_buffer = bytearray(3*num_pixels)



while True:

    # generate the next frame based on the real-time clock value
    now = time.monotonic_ns() / 1000
    
    # generate a temporal color sequence with each component out of phase
    red = int((now//11000) % 256)
    grn = int((now//33000) % 256)
    blu = int((now//55000) % 256)

    # print(f"{red}, {grn}, {blu}")

    # update the entire frame buffer including an additional position-dependent term
    # to create spatial variation
    for p in range(num_pixels):
        frame_buffer[3*p]   = (grn + 12*p) % 256
        frame_buffer[3*p+1] = (red + 12*p) % 256
        frame_buffer[3*p+2] = (blu + 12*p) % 256

    # transfer the new frame to the NeoPixel LED strand
    neopixel_write.neopixel_write(pixels, frame_buffer)

