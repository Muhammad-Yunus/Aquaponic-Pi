# Aquaponic-Pi

### Diagram block and Pin Mapping

##### One Wire Pin (4x DS18B20 Digital Temperature Sensor):
- Data -> GPIO13 RPI Zero 

##### Water Level Sensor
- WL Sensor A -> GPIO22 RPI Zero
- WL Sensor B -> GPIO27 RPI Zero

##### Selenoid Valve
- SV A -> GPIO19 RPI Zero
- SV B -> GPIO26 RPI Zero

##### TDS Probe to analog interface to PCF8591
- Left analog TDS -> A0
- Right analog TDS -> A1

![image](https://image.ibb.co/jv5RH7/Aquaponic_Hat.png)


### Content in this repo :
- Board Schematics (Cad Soft Eagle)
- Board Layout (Cad Soft Eagle)
- Python program :
    a. DS18B20
    b. PCF8591
    c. Selenoid Valve
    d. Water Level
    e. TDS 

##### Design And Developed By :
- [Legendre Technology](https://www.facebook.com/LegendreTechnology/)
- (Ziath & Robby) PRC Dept.of Physics Bogor Agricultural University 
