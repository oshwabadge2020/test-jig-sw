import displayio
import adafruit_miniqr
import board
import pulseio
from digitalio import DigitalInOut, Direction, Pull
#backlight = DigitalInOut(board.TFT_BACKLIGHT)
#backlight.direction = Direction.OUTPUT
#backlight.value = False

pwm = pulseio.PWMOut(board.TFT_BACKLIGHT)
pwm.duty_cycle = 65535-16000

display = board.DISPLAY

def bitmap_qr(matrix):
	"""The QR code bitmap."""
	border_pixels = 2
	bitmap = displayio.Bitmap(matrix.width + 2 * border_pixels,matrix.height + 2 * border_pixels, 2)
	for y in range(matrix.height):
		for x in range(matrix.width):
			if matrix[x, y]:
				bitmap[x + border_pixels, y + border_pixels] = 1
			else:
				bitmap[x + border_pixels, y + border_pixels] = 0
	return bitmap

print('Hello World!')
qr = adafruit_miniqr.QRCode()
qr.add_data(b'aaaaa')
qr.make()

palette = displayio.Palette(2)
palette[1] = 0x000000
palette[0] = 0xffffff

bitmap = bitmap_qr(qr.matrix)
tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
tile_grid.flip_y=True
# Create a Group to hold the TileGrid
group = displayio.Group(scale=9, x=0, y=0)
group.append(tile_grid)
display.show(group)
while True:
	pass
