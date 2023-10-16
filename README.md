# MAX7219 Pico Jack-o'-lantern
#### this project was inspired by this gurgleapps [project](https://gurgleapps.com/learn/projects/8x8-led-matrix-halloween-jack-o-lantern-pumpkin-project-with-a-pico)

## Setup
* Install [micropython](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html) onto your pi pico
* Wire the pins of the pi pico so that pins SPI0csn (pin2), SPI0sck (pin4), SPI0tx  (pin5) are wired, Ground (pin38), and vcc(Pin40) to the left eye (MAX7219 single board in ports) and the left eye (out ports) is wired to the right eye (in ports).  Here is the pi [pico diagram](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html) for reference.
* Wire the pins of the pi pico so that pins SPI1csn (pin12), SPI1sck (pin14), SPI1tx  (pin15) are wired, Ground (pin38), and vcc(Pin40) to the mouth (MAX7219 four in 1 display).  Here is the pi [pico diagram](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html) for reference.
* Use either [thonny](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/2), [ampy](https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy), or [vscode](https://www.hackster.io/shilleh/how-to-use-vscode-with-raspberry-pi-pico-w-and-micropython-de88d6) to install the python and json files in this project on your pi pico.
* Carve eyes and a mouth into your pumpkin and mount the eyes and mouth.

## Materials used
* 1 [pi pico](https://www.raspberrypi.com/products/raspberry-pi-pico/)
* 2 [single board](https://www.amazon.com/ACEIRMC-MAX7219-Display-Single-Chip-Control/dp/B08VHX2KC4/ref=sr_1_10?crid=73PDNS1ZPPNM&keywords=max7219&qid=1697389881&sprefix=max7219%2Caps%2C84&sr=8-10) MAX7219 (eyes)
* 1 [four in 1 display](https://www.amazon.com/HiLetgo-MAX7219-Arduino-Microcontroller-Display/dp/B07FFV537V/ref=sr_1_1_sspa?crid=73PDNS1ZPPNM&keywords=max7219&qid=1697389818&sprefix=max7219%2Caps%2C84&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1) MAX7219 (mouth)
* 1 [carvable foam pumpkin](https://www.target.com/p/13-34-carvable-faux-halloween-pumpkin-orange-hyde-38-eek-boutique-8482/-/A-84064494?ref=tgt_adv_xsp&AFID=google&fndsrc=tgtao&DFA=71700000012510724&CPNG=PLA_Seasonal%2BShopping%7CSeasonal_Ecomm_Home&adgroup=Online+Test&LID=700000001170770pgs&LNM=PRODUCT_GROUP&network=g&device=c&location=9022830&targetid=aud-1957922309919:pla-2177501878715&ds_rl=1246978&ds_rl=1247068&gclid=Cj0KCQjwm66pBhDQARIsALIR2zBCfE2mTGVFw3BKAnD6QUHfkpq8SoGByFyV9vUbamdE8Pn4EW8rmDQaAoFzEALw_wcB&gclsrc=aw.ds)
* various small parts (wires, solder or solderless breadboard, etc)
* To create your own custom images you can use this [tool](https://gurgleapps.com/tools/matrix).
