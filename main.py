from machine import Pin, SPI
import time
import json
import matrix_fonts
from max7219_matrix import max7219_matrix

def load_anims(file_name):
  data={}
  try:
    with open(file_name) as infile:
      data=json.load(infile)
  except Exception as err:
      print('Oops problem loading JSON! ')
      print (err)
  return data

eyes_anims = load_anims('eyes_ani.json')
mouth_anims = load_anims('mouth_ani.json')

eyes = max7219_matrix(SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3)), Pin(1, Pin.OUT, True))
mouth = max7219_matrix(SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(10), mosi=Pin(11)), Pin(9, Pin.OUT, True), 4)

def anim_runner(anim,font):
    for i in anim:
        if "l" in i and "r" in i:
                eyes.show_char([font[i["l"]],font[i["r"]]])
        if "m1" in i and "m2" and "m3" in i and "m4" in i:
                mouth.show_char([font[i["m1"]],font[i["m2"]],font[i["m3"]],font[i["m4"]]])
        if "bl" in i:
           eyes.set_brightness(i["bl"])
        if "ml" in i:
           mouth.set_brightness(i["ml"])
        time.sleep(i["d"])
               
def convert_text_to_bytes(font,message='hello'):
    message_bytes=[]
    for char_pos in range(len(message)):
      message_bytes.append(font[message[char_pos]])
    return message_bytes

def scroll_message(matrix, font, message):
    reverse = True
    message_bytes = convert_text_to_bytes(font,message)
    matrix.set_brightness(10)
    matrix.scroll_data(message_bytes,reverse)

def demo():
    eyes.show_char([matrix_fonts.eyes['ghost1'], matrix_fonts.eyes['ghost1']])
    scroll_message(mouth,matrix_fonts.textFont1,'Happy Halloween')
    time.sleep(1)
    scroll_message(eyes, matrix_fonts.textFont1, 'Spooky')
    anim_runner(eyes_anims['stareAndBlink'],matrix_fonts.eyes)
    anim_runner(eyes_anims['growEyes'],matrix_fonts.eyes)
    anim_runner(eyes_anims['roll'],matrix_fonts.eyes)
    anim_runner(eyes_anims['downLeftABit'],matrix_fonts.eyes)
    anim_runner(eyes_anims['stareAndBlink'],matrix_fonts.eyes)
    anim_runner(eyes_anims['downRightABit'],matrix_fonts.eyes)
    anim_runner(eyes_anims['stareAndBlink'],matrix_fonts.eyes)
    scroll_message(eyes, matrix_fonts.textFont1, ' Trick or Treat ')
    scroll_message(mouth, matrix_fonts.textFont1, 'HA HA HA')
    anim_runner(mouth_anims['pacman'],matrix_fonts.shapes)
    anim_runner(eyes_anims['stareAndBlink'],matrix_fonts.eyes)
    anim_runner(eyes_anims['stareAndBlink'],matrix_fonts.eyes)
    anim_runner(eyes_anims['growEyes'],matrix_fonts.eyes)
    anim_runner(eyes_anims['roll'],matrix_fonts.eyes)
    anim_runner(eyes_anims['ghosts1'],matrix_fonts.eyes)
    anim_runner(eyes_anims['stareAndBlink'],matrix_fonts.eyes)
    anim_runner(eyes_anims['winkLeft'],matrix_fonts.eyes)
    anim_runner(eyes_anims['winkRight'],matrix_fonts.eyes)
    anim_runner(eyes_anims['stareAndBlink'],matrix_fonts.eyes)

counter=1        
while True:
    demo()
    counter+=1

    



