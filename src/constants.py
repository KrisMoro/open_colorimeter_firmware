import board
import collections
import adafruit_tsl2591

__version__ = '0.1.0'

CALIBRATIONS_FILE = 'calibrations.json'
CONFIGURATION_FILE = 'configuration.json'
SPLASHSCREEN_BMP = 'assets/splashscreen.bmp'

LOOP_DT = 0.1
BLANK_DT = 0.05
DEBOUNCE_DT = 0.6 
NUM_BLANK_SAMPLES = 50 
BATTERY_AIN_PIN = board.A6

BUTTON_LEFT = 7  # LEFT button
BUTTON_UP = 6  # UP button
BUTTON_DOWN = 5  # DOWN button
BUTTON_RIGHT = 4  # RIGHT button
BUTTON_MENU = 3  # SELECT button
BUTTON_BLANK = 2  # START button
BUTTON_ITIME = 1  # button A
BUTTON_GAIN = 0  # button B

BUTTON = { 
        'none'  : 0b00000000,
        'left'  : 0b10000000,
        'up'    : 0b01000000,
        'down'  : 0b00100000, 
        'right' : 0b00010000,
        'menu'  : 0b00001000, 
        'blank' : 0b00000100, 
        'itime' : 0b00000010,
        'gain'  : 0b00000001,
        }

COLOR_TO_RGB = collections.OrderedDict([ 
    ('black'  , 0x000000), 
    ('gray'   , 0x818181), 
    ('red'    , 0xff0000), 
    ('green'  , 0x00ff00),
    ('blue'   , 0x0000ff),
    ('white'  , 0xffffff), 
    ('orange' , 0xffb447),
    ])

LIGHT_SOURCE  = collections.OrderedDict([
        ('red', board.D10),
        ('green', board.D11),
        ('blue', board.D12)
]) 

NEOPIXEL_COLORS = collections.OrderedDict([
        ('all'  , (255,255,255)),
        ('red'  , (255,0,0)),
        ('green', (0,255,0)),
        ('blue' , (0,0,255))
])

STR_TO_GAIN = collections.OrderedDict([
        ('low'  , adafruit_tsl2591.GAIN_LOW ),
        ('med'  , adafruit_tsl2591.GAIN_MED ),
        ('high' , adafruit_tsl2591.GAIN_HIGH),
        ('max'  , adafruit_tsl2591.GAIN_MAX ),
        ])
GAIN_TO_STR = {v:k for k,v in STR_TO_GAIN.items()}

STR_TO_INTEGRATION_TIME = collections.OrderedDict([
        ('100ms', adafruit_tsl2591.INTEGRATIONTIME_100MS),
        ('200ms', adafruit_tsl2591.INTEGRATIONTIME_200MS),
        ('300ms', adafruit_tsl2591.INTEGRATIONTIME_300MS),
        ('400ms', adafruit_tsl2591.INTEGRATIONTIME_400MS),
        ('500ms', adafruit_tsl2591.INTEGRATIONTIME_500MS),
        ('600ms', adafruit_tsl2591.INTEGRATIONTIME_600MS),
        ])
INTEGRATION_TIME_TO_STR = {v:k for k,v in STR_TO_INTEGRATION_TIME.items()}
