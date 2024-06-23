# pi_timekeeper
Simple timekeeping with a Raspberry Pi


The program is based on a small Python application, which is intended to time the individual heats in a competition.
The current time is shown on an HDMI display on the Raspi.

Features:

through remote control
- Start measurement
- Stop measurement
- Reset measurement

through the light barrier
- Stop measurement

The light barrier and the buttons on the remote control are connected via an I2C board.

https://sequentmicrosystems.com/collections/all-io-cards/products/eight-hv-digital-inputs-for-raspberry-pi

The corresponding Pyhton library is required.

https://github.com/SequentMicrosystems/8inputs-rpi/tree/main/python
