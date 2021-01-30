If you use hc-06. There is no need to connect any resistor. You can connect it directly to the ramps1.4.

http://www.ebay.com/itm/3Mbps-Mini-USB-Bluetooth-V4-0-Dongle-Dual-Mode-Wireless-Adapter-Device-20M-/131608011429?hash=item1ea472e2a5:g:f6YAAOSwdzVXiei-

Power on arduino with ramps1.4 and hc-06
Right click on your desktop bluetooth icon. And click add device. Select hc-06. The default password when asked is 1234. And the default baurate is 9600.

If you didn't change the baurate then on the software select 9600 to connect.

If your desktop do not have bluetooth. Import to buy buletooth 4.0 as 2.0 has issue. You can buy here http://www.ebay.com/itm/Mini-Bluetooth-4-0-USB-2-0-CSR4-0-Dongle-Adapter-For-Win-8-7-XP-Laptop-PC-Catchy-/331642902784?hash=item4d37751900:g:xAIAAOSw~gRV5Dyd

You can use joystick to control the robotic arm wirelessly.

If you can't get bluetooth to work. Program your hc-06
use no line ending at arduino monitor. And type below command in sequence: This will change device name to RoboticArm. Password 1828.Baurate 57600.


AT
AT+BAUD7
AT+NAMERoboticArm
AT+PIN1828


Baurate setting is below.
1 set to 1200bps
2 set to 2400bps 
3 set to 4800bps 
4 set to 9600bps (Default) 
5 set to 19200bps 
6 set to 38400bps 
7 set to 57600bps 
8 set to 115200bps

Tutorial: http://www.instructables.com/id/AT-command-mode-of-HC-05-Bluetooth-module/

