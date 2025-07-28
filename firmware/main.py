from kmk.kmk_keyboard import KMKKeyboard
from kmk.modules.layers import Layers
from kmk.scanners.keypad import MatrixScanner
from kmk.scanners.analog import AnalogScanner
from kmk.keys import KC

import board
import busio
from adafruit_mcp230xx.mcp23017 import MCP23017

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

# --- Setup I2C and MCP23017 ---
i2c = busio.I2C(scl=board.D10, sda=board.D16)  # GPIO10=SCL, GPIO16=SDA
mcp = MCP23017(i2c, address=0x20)  # A0, A1, A2 grounded -> 0x20

# --- MCP23017 Pins ---
mcp_rows = [
    mcp.get_pin(5),   # GPA5 = ROW3
    mcp.get_pin(1 + 8),  # GPB1 = ROW4
    mcp.get_pin(6),   # GPA6 = ROW5
]

mcp_cols = [
    mcp.get_pin(4),   # GPA4 = COL1
    mcp.get_pin(3),   # GPA3 = COL2
    mcp.get_pin(2),   # GPA2 = COL3
    mcp.get_pin(1),   # GPA1 = COL4
    mcp.get_pin(0),   # GPA0 = COL5
    mcp.get_pin(2 + 8),   # GPB2 = COL9
    mcp.get_pin(3 + 8),   # GPB3 = COL10
    mcp.get_pin(4 + 8),   # GPB4 = COL11
    mcp.get_pin(5 + 8),   # GPB5 = COL12
    mcp.get_pin(6 + 8),   # GPB6 = COL13
    mcp.get_pin(7 + 8),   # GPB7 = COL14
    mcp.get_pin(0 + 8),   # GPB0 = COL15
    mcp.get_pin(7),   # GPA7 = COL16
]

# Set direction for MCP pins
for pin in mcp_rows:
    pin.switch_to_input(pull=None)
for pin in mcp_cols:
    pin.switch_to_output(value=True)

# --- Nice!Nano Direct Pins ---
direct_rows = [
    board.D20,  # GPIO20 = ROW1
    board.D19,  # GPIO19 = ROW2
]

direct_cols = [
    board.D14,  # GPIO14 = COL6
    board.D15,  # GPIO15 = COL7
    board.D18,  # GPIO18 = COL8
]

# --- Combine into a single matrix ---
# Order: COL1–COL16, ROW1–ROW5

keyboard.matrix = MatrixScanner(
    cols=mcp_cols + direct_cols,  # COL1–COL16 (MCP) + COL6–COL8 (Direct)
    rows=direct_rows + mcp_rows,  # ROW1–ROW5 (2 Direct + 3 MCP)
    columns_to_anodes=True
)

# --- KEYMAP (Example Only!) ---
keyboard.keymap = [
    [  # row x column layout: 5 rows × 16 columns
        KC.ESC, KC._1, KC._2, KC._3, KC._4, KC._5, KC._6, KC._7, KC._8, KC._9, KC._0, KC.MINS, KC.EQL, KC.BSPC, KC.NO, KC.NO,
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.NO, KC.NO,
        KC.CAPS, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.NO, KC.ENT, KC.NO, KC.NO,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.NO, KC.NO, KC.NO, KC.NO, KC.RSFT,
        KC.LCTL, KC.LGUI, KC.LALT, KC.SPC, KC.SPC, KC.RALT, KC.RGUI, KC.APP, KC.LEFT, KC.DOWN, KC.UP, KC.RGHT, KC.NO, KC.NO, KC.NO, KC.RCTL,
    ]
]

if __name__ == '__main__':
    keyboard.go()
