
# Description of the pumps

These are some pictures of the pumps we will use in the project:

<img src="http://i.ebayimg.com/00/s/MTA2NlgxNjAw/z/KWsAAOSw5VFWOrZ6/$_57.JPG?set_id=880000500F" width="400" height="400" />
<img src="https://s-media-cache-ak0.pinimg.com/736x/14/05/25/14052577c84eba4bef773c84728b0461.jpg" width="300" height="300">
    
All of them are peristaltic pumps. According to the [Wikipedia](https://en.wikipedia.org/wiki/Peristaltic_pump): *"A peristaltic pump is a type of positive displacement pump used for pumping a variety of fluids. The fluid is contained within a flexible tube fitted inside a circular pump casing (though linear peristaltic pumps have been made). A rotor with a number of "rollers", "shoes", "wipers", or "lobes" attached to the external circumference of the rotor compresses the flexible tube. As the rotor turns, the part of the tube under compression is pinched closed (or "occludes") thus forcing the fluid to be pumped to move through the tube. Additionally, as the tube opens to its natural state after the passing of the cam ("restitution" or "resilience") fluid flow is induced to the pump."*

The following gifs illustrate the previous description:

![ppump](https://upload.wikimedia.org/wikipedia/commons/9/95/Peristaltic_pump.gif)
![ppump2](https://upload.wikimedia.org/wikipedia/commons/e/e1/Peristaltic_pump_LAMBDA_PRECIFLOW_-_pumping_mechanism.gif)

Based on the mechanism of peristaltic pumps, it is expected that the flow is proportional to the speed of the rotor. Our pumps work at a fixed speed and therefore we expect a constant flow. For operational purposes of our titrator we need to **calibrate** our pumps in order to know what is its flow. But before we go into that, we should first understand a bit more about how the pumps operate and how we can control it with a raspberry pi.

## Conecting our pumps to a Raspberry pi

A raspberry pi is a small device, and it operates at a relatively low power. This is actually one of the main advantages of these type of 'minicomputers' that allows to execute complex operations to assist other processes without spending too much energy. 

The raspberry pis that we will use can provide up to 5V to an external device. This is not enough to power up our pumps. Therefore, we will need an external power suply that can give enough power to the pumps to work. Still, we want to control the pumps using the raspberry. For this purpose we will make use of an electromagnetic device called **relay**, which works as an switch that allows you to control a high voltage electrical circuit (the pump) by opening and closing contacts in another low voltage circuit (the raspberry pi).

By using the relay we will turn on and off the pumps by sending signals from our raspberry pi. Before assembling the circuit we need to identify the different parts and the point contacts involved.

## Relay

Relays work as switches. The most basic ones involved a physical mechanism to open and close the circuit. The low power circuit is use to generate an electromagnetic field that attracts a moving component that closes the high-power circuit.

![relay](http://cdn4.explainthatstuff.com/how-relay-works2.gif)
![relay2](http://cdn4.explainthatstuff.com/how-a-relay-works.gif)

Devices as transistors can be also used as relays. We will be using the following card, that contain 4 relays. Each relay corresponds to one of the blue boxes:

![our relay](https://grobotronics.com/images/thumbnails/320/320/detailed/4/relay_module_4_channel.png)

Something very important about the relays is how they are connected. A single relay has three ports: the normal open (NO), normal closed (NC) and the common port (COM). The NC connects to a circuit that is ON by default. When the switch is activated, the connection from the common port is moved from the NC to the NO. Since for now we are interesting in only turning on and off the pumps, we will use only the NO and the COM ports.

![relay](http://pcbheaven.com/wikipages/images/howrelayswork_1268485820.jpg)
![relay2](http://pcbheaven.com/wikipages/images/howrelayswork_1268490625.gif)

This is the position of the ports in our relay:

![](../Images/relay.png)

## Raspberry Pi connections

For the connections fo the raspberry pi we will be using the General-purpose input/output (GPIO) pins. The behavior of these pins is controllable by the user at run time, which makes them convinient to send signals to the relay to turn on and off the pumps.

Identify the GPIO pins in the Raspberry Pie, they are designated as G.

![](../Images/pins.png)


## Diagram of the whole circuit

![](../Images/diagramPumps.png)

## Controlling the pumps from the Raspberry Pi

To give you and idea of the of how to control the pumps from the RP using python, we have prepared the test.py in the folder Pumps of this repository. The information regarding the specific connection and ports that must be used for the circuit above are also included in the documents of this folder. Check them out!

#  <i class="fa fa-exclamation-triangle" aria-hidden="true"></i> WARNING
# <i class="fa fa-exclamation-triangle" aria-hidden="true"></i> WARNUNG
# <i class="fa fa-exclamation-triangle" aria-hidden="true"></i> ADVERTENCIA
# READ THIS BEFORE YOU PROCEED

* Before connecting anything, double check your circuti, you might burn a circuit or cause an accident.

* If it is possible before connecting everything to a single power supply, test everything with a regular wall power source with smaller current. (It might not be possible with the steeper pumps).

* It is ok to build a with jumpers and alligators, after that use a permaboard or/and use a more permanent wired.

* Check frequently if the voltage and current is the adequate.

* Do not leave any open wire, use electic tape to cover it.

* Keep all the circuits an wiring far form liquids.

* If you are not sure about something, please ask.



```python

```
