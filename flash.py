from machine import Pin, I2C, PWM
import time
import ssd1306

I2C_SDA = 0
I2C_SCL = 1
LED_PIN = 25
BUZZER_PIN = 15

i2c = I2C(0,  scl=Pin(I2C_SCL), sda=Pin(I2C_SDA))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
led = Pin(LED_PIN, Pin.OUT)
buzzer = PWM(Pin(BUZZER_PIN)) if BUZZER_PIN is not None else None

MORSE = {
    'A': '.-','B':'-...','C':'-.-.','D':'-..','E':'.',
    'F':'..-.','G':'--.','H':'....','I':'..','J':'.---',
    'K':'-.-','L':'.-..','M':'--','N':'-.','O':'---',
    'P':'.--.','Q':'--.-','R':'.-.','S':'...','T':'-',
    'U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--',
    'Z':'--..',
    '1':'.----','2':'..---','3':'...--','4':'....-','5':'.....',
    '6':'-....','7':'--...','8':'---..','9':'----.','0':'-----',
    ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.','-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': '/'
}

DOT = 0.12

def tone_on():
    led.on()
    if buzzer:
        buzzer.freq(2000)
        buzzer.duty_u16(20000)

def tone_off():
    led.off()
    if buzzer:
        buzzer.duty_u16(0)

def send_symbol(sym):
    if sym == '.':
        tone_on(); time.sleep(DOT); tone_off(); time.sleep(DOT)
    elif sym == '-':
        tone_on(); time.sleep(3 * DOT); tone_off(); time.sleep(DOT)

def send_char(ch):
    code = MORSE.get(ch.upper(), '')
    if code == '/'
        time.sleep(7 * DOT)
        return
    for s in code:
    time.sleep(2*DOT)

def send_text(text):
    oled.fill(0)
    oled.text('Transmitting:', 0, 0)
    oled.text(text[:16], 0, 12)
    oled.show()
    for ch in text:
        send_char(ch)

def show_idle():
    oled.fill(0)
    oled.text('PiMorse', 0, 0)
    oled.text('Enter text over REPL', 0, 20)
    oled.text('Then call text', 0, 40)
    oled.show()

show_idle()
