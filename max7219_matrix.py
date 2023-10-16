import time

class max7219_matrix:
    
    _NOOP = const(0)
    _DIGIT0 = const(1)
    _DECODEMODE = const(9)
    _INTENSITY = const(10)
    _SCANLIMIT = const(11)
    _SHUTDOWN = const(12)
    _DISPLAYTEST = const(15)
    _BLANK_PANEL_DATA = [0,0,0,0,0,0,0,0]
    
    
    def __init__(self, spi, cs, panels=2):
        self.spi = spi
        self.cs = cs
        self.number_panels = panels
        self.setup()
        
        
    def setup(self):
        self.write(_SHUTDOWN,0)
        self.write(_DISPLAYTEST,0)
        self.write(_SCANLIMIT,7)
        self.write(_DECODEMODE,0)
        self.write(_SHUTDOWN,1)

    def write(self, command, data):
        self.cs.value(0)
        for m in range(self.number_panels):
            self.spi.write(bytearray([command, data]))
        self.cs.value(1)

    def show_char(self, panelData):
        panelRange = range(len(panelData))
        for i in range(8):
            self.cs.value(0)            
            for panelIdx in panelRange:
                self.spi.write(bytearray([i+1, panelData[panelIdx][i]]))
            self.cs.value(1)

    def clear_panels(self):
        data = []
        for i in range(self.number_panels):
            data.append(self._BLANK_PANEL_DATA)
        self.show_char(data)

    def rotate(self, data, reverse=False):
        if reverse:
            return data.append(data.pop(0))
        return data.insert(0,data.pop())

    def scroll_data(self, panelData, reverse=False, delay=0.5):
        startIdx = 0
        if reverse:
            startIdx = self.number_panels -1
        self.clear_panels()
        data = [self._BLANK_PANEL_DATA] * self.number_panels
        for char in panelData:
            data[startIdx] = char
            self.show_char(data)
            self.rotate(data, reverse)
            time.sleep(delay)
        for i in range(self.number_panels):
            data[startIdx] = self._BLANK_PANEL_DATA
            self.show_char(data)
            self.rotate(data, reverse)
            time.sleep(delay)
        
    def set_brightness(self, brightness):
        self.write(_INTENSITY, brightness)
                

