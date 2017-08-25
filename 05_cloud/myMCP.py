import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

def getLux(LUX_MCP):
  return mcp.read_adc(LUX_ADC, gain=1)

def getLuxString(LUX_MCP):
    return 'Light = ' + str(getLux(LUX_MCP))
