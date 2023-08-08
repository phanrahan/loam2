from magma import *
from ..spartan import Spartan
from ..gpio import GPIO, Pin
from ..clock import Clock
from .usart import USART

class Spartan6(Spartan):
    family = 'spartan6'

    def __init__(self, name, board, speed):
        super(Spartan6,self).__init__(name, board, speed)
        self.clock = Clock(self)
        self.USART = USART
        
    def TQG144(self):
        self.package = 'TQG144'
        
        GPIO(self, "P144")
        GPIO(self, "P143")
        GPIO(self, "P142")
        GPIO(self, "P141")
        GPIO(self, "P140")
        GPIO(self, "P139")
        GPIO(self, "P138")
        GPIO(self, "P137")
        GPIO(self, "P134")
        GPIO(self, "P133")
        GPIO(self, "P132")
        GPIO(self, "P131")
        GPIO(self, "P127")
        GPIO(self, "P126")
        GPIO(self, "P124")
        GPIO(self, "P123")
        GPIO(self, "P121")
        GPIO(self, "P120")
        GPIO(self, "P119")
        GPIO(self, "P118")
        GPIO(self, "P117")
        GPIO(self, "P116")
        GPIO(self, "P115")
        GPIO(self, "P114")
        GPIO(self, "P112")
        GPIO(self, "P111")
        Pin(self, "P109")
        Pin(self, "P110")
        Pin(self, "P107")
        Pin(self, "P106")
        GPIO(self, "P105")
        GPIO(self, "P104")
        GPIO(self, "P102")
        GPIO(self, "P101")
        GPIO(self, "P100")
        GPIO(self, "P99")
        GPIO(self, "P98")
        GPIO(self, "P97")
        GPIO(self, "P95")
        GPIO(self, "P94")
        GPIO(self, "P93")
        GPIO(self, "P92")
        GPIO(self, "P88")
        GPIO(self, "P87")
        GPIO(self, "P85")
        GPIO(self, "P84")
        GPIO(self, "P83")
        GPIO(self, "P82")
        GPIO(self, "P81")
        GPIO(self, "P80")
        GPIO(self, "P79")
        GPIO(self, "P78")
        GPIO(self, "P75")
        GPIO(self, "P74")
        Pin(self, "P73")
        Pin(self, "P72")
        Pin(self, "P71")
        GPIO(self, "P70")
        GPIO(self, "P69")
        GPIO(self, "P67")
        GPIO(self, "P66")
        GPIO(self, "P65")
        GPIO(self, "P64")
        GPIO(self, "P62")
        GPIO(self, "P61")
        GPIO(self, "P60")
        GPIO(self, "P59")
        GPIO(self, "P58")
        GPIO(self, "P57")
        GPIO(self, "P56")
        GPIO(self, "P55")
        GPIO(self, "P51")
        GPIO(self, "P50")
        GPIO(self, "P48")
        GPIO(self, "P47")
        GPIO(self, "P46")
        GPIO(self, "P45")
        GPIO(self, "P44")
        GPIO(self, "P43")
        GPIO(self, "P41")
        GPIO(self, "P40")
        GPIO(self, "P39")
        GPIO(self, "P38")
        Pin(self, "P37")
        GPIO(self, "P35")
        GPIO(self, "P34")
        GPIO(self, "P33")
        GPIO(self, "P32")
        GPIO(self, "P30")
        GPIO(self, "P29")
        GPIO(self, "P27")
        GPIO(self, "P26")
        GPIO(self, "P24")
        GPIO(self, "P23")
        GPIO(self, "P22")
        GPIO(self, "P21")
        GPIO(self, "P17")
        GPIO(self, "P16")
        GPIO(self, "P15")
        GPIO(self, "P14")
        GPIO(self, "P12")
        GPIO(self, "P11")
        GPIO(self, "P10")
        GPIO(self, "P9")
        GPIO(self, "P8")
        GPIO(self, "P7")
        GPIO(self, "P6")
        GPIO(self, "P5")
        GPIO(self, "P2")
        GPIO(self, "P1")
        Pin(self, "P108")
        Pin(self, "P113")
        Pin(self, "P13")
        Pin(self, "P130")
        Pin(self, "P136")
        Pin(self, "P25")
        Pin(self, "P3")
        Pin(self, "P49")
        Pin(self, "P54")
        Pin(self, "P68")
        Pin(self, "P77")
        Pin(self, "P91")
        Pin(self, "P96")
        Pin(self, "P129")
        Pin(self, "P20")
        Pin(self, "P36")
        Pin(self, "P53")
        Pin(self, "P90")
        Pin(self, "P128")
        Pin(self, "P19")
        Pin(self, "P28")
        Pin(self, "P52")
        Pin(self, "P89")
        Pin(self, "P122")
        Pin(self, "P125")
        Pin(self, "P135")
        Pin(self, "P103")
        Pin(self, "P76")
        Pin(self, "P86")
        Pin(self, "P42")
        Pin(self, "P63")
        Pin(self, "P18")
        Pin(self, "P31")
        Pin(self, "P4")

    def FTG256(self):
        self.package = 'FTG256'

        GPIO(self, "C4")
        GPIO(self, "A4")
        GPIO(self, "B5")
        GPIO(self, "A5")
        GPIO(self, "D5")
        GPIO(self, "C5")
        GPIO(self, "B6")
        GPIO(self, "A6")
        GPIO(self, "F7")
        GPIO(self, "E6")
        GPIO(self, "C7")
        GPIO(self, "A7")
        GPIO(self, "D6")
        GPIO(self, "C6")
        GPIO(self, "B8")
        GPIO(self, "A8")
        GPIO(self, "C9")
        GPIO(self, "A9")
        GPIO(self, "B10")
        GPIO(self, "A10")
        GPIO(self, "E7")
        GPIO(self, "E8")
        GPIO(self, "E10")
        GPIO(self, "C10")
        GPIO(self, "D8")
        GPIO(self, "C8")
        GPIO(self, "C11")
        GPIO(self, "A11")
        GPIO(self, "F9")
        GPIO(self, "D9")
        GPIO(self, "B12")
        GPIO(self, "A12")
        GPIO(self, "C13")
        GPIO(self, "A13")
        GPIO(self, "F10")
        GPIO(self, "E11")
        GPIO(self, "B14")
        GPIO(self, "A14")
        GPIO(self, "D11")
        GPIO(self, "D12")
        Pin(self, "C14")
        Pin(self, "C12")
        Pin(self, "A15")
        Pin(self, "E14")
        GPIO(self, "E13")
        GPIO(self, "E12")
        GPIO(self, "B15")
        GPIO(self, "B16")
        GPIO(self, "F12")
        GPIO(self, "G11")
        GPIO(self, "D14")
        GPIO(self, "D16")
        GPIO(self, "F13")
        GPIO(self, "F14")
        GPIO(self, "C15")
        GPIO(self, "C16")
        GPIO(self, "E15")
        GPIO(self, "E16")
        GPIO(self, "F15")
        GPIO(self, "F16")
        GPIO(self, "G14")
        GPIO(self, "G16")
        GPIO(self, "H15")
        GPIO(self, "H16")
        GPIO(self, "G12")
        GPIO(self, "H11")
        GPIO(self, "H13")
        GPIO(self, "H14")
        GPIO(self, "J11")
        GPIO(self, "J12")
        GPIO(self, "J13")
        GPIO(self, "K14")
        GPIO(self, "K12")
        GPIO(self, "K11")
        GPIO(self, "J14")
        GPIO(self, "J16")
        GPIO(self, "K15")
        GPIO(self, "K16")
        GPIO(self, "N14")
        GPIO(self, "N16")
        GPIO(self, "M15")
        GPIO(self, "M16")
        GPIO(self, "L14")
        GPIO(self, "L16")
        GPIO(self, "P15")
        GPIO(self, "P16")
        GPIO(self, "R15")
        GPIO(self, "R16")
        GPIO(self, "R14")
        GPIO(self, "T15")
        GPIO(self, "T14")
        GPIO(self, "T13")
        GPIO(self, "R12")
        GPIO(self, "T12")
        GPIO(self, "L12")
        GPIO(self, "L13")
        GPIO(self, "M13")
        GPIO(self, "M14")
        Pin(self, "P14")
        Pin(self, "L11")
        Pin(self, "P13")
        GPIO(self, "R11")
        GPIO(self, "T11")
        GPIO(self, "M12")
        GPIO(self, "M11")
        GPIO(self, "P10")
        GPIO(self, "T10")
        GPIO(self, "N12")
        GPIO(self, "P12")
        GPIO(self, "N11")
        GPIO(self, "P11")
        GPIO(self, "N9")
        GPIO(self, "P9")
        GPIO(self, "R9")
        GPIO(self, "T9")
        GPIO(self, "L10")
        GPIO(self, "M10")
        GPIO(self, "M9")
        GPIO(self, "N8")
        GPIO(self, "P8")
        GPIO(self, "T8")
        GPIO(self, "P7")
        GPIO(self, "M7")
        GPIO(self, "R7")
        GPIO(self, "T7")
        GPIO(self, "P6")
        GPIO(self, "T6")
        GPIO(self, "R5")
        GPIO(self, "T5")
        GPIO(self, "N5")
        GPIO(self, "P5")
        GPIO(self, "L8")
        GPIO(self, "L7")
        GPIO(self, "P4")
        GPIO(self, "T4")
        GPIO(self, "M6")
        GPIO(self, "N6")
        GPIO(self, "R3")
        GPIO(self, "T3")
        Pin(self, "T2")
        GPIO(self, "M4")
        GPIO(self, "M3")
        GPIO(self, "M5")
        GPIO(self, "N4")
        GPIO(self, "R2")
        GPIO(self, "R1")
        GPIO(self, "P2")
        GPIO(self, "P1")
        GPIO(self, "N3")
        GPIO(self, "N1")
        GPIO(self, "M2")
        GPIO(self, "M1")
        GPIO(self, "L3")
        GPIO(self, "L1")
        GPIO(self, "K2")
        GPIO(self, "K1")
        GPIO(self, "J3")
        GPIO(self, "J1")
        GPIO(self, "H2")
        GPIO(self, "H1")
        GPIO(self, "G3")
        GPIO(self, "G1")
        GPIO(self, "F2")
        GPIO(self, "F1")
        GPIO(self, "K3")
        GPIO(self, "J4")
        GPIO(self, "J6")
        GPIO(self, "H5")
        GPIO(self, "H4")
        GPIO(self, "H3")
        GPIO(self, "L4")
        GPIO(self, "L5")
        GPIO(self, "E2")
        GPIO(self, "E1")
        GPIO(self, "K5")
        GPIO(self, "K6")
        GPIO(self, "C3")
        GPIO(self, "C2")
        GPIO(self, "D3")
        GPIO(self, "D1")
        GPIO(self, "C1")
        GPIO(self, "B1")
        GPIO(self, "G6")
        GPIO(self, "G5")
        GPIO(self, "B2")
        GPIO(self, "A2")
        GPIO(self, "F4")
        GPIO(self, "F3")
        GPIO(self, "E4")
        GPIO(self, "E3")
        GPIO(self, "F6")
        GPIO(self, "F5")
        GPIO(self, "B3")
        GPIO(self, "A3")
        Pin(self, "A1")
        Pin(self, "A16")
        Pin(self, "B11")
        Pin(self, "B7")
        Pin(self, "D13")
        Pin(self, "D4")
        Pin(self, "E9")
        Pin(self, "G15")
        Pin(self, "G2")
        Pin(self, "G8")
        Pin(self, "H12")
        Pin(self, "H7")
        Pin(self, "H9")
        Pin(self, "J5")
        Pin(self, "J8")
        Pin(self, "K7")
        Pin(self, "K9")
        Pin(self, "L15")
        Pin(self, "L2")
        Pin(self, "M8")
        Pin(self, "N13")
        Pin(self, "P3")
        Pin(self, "R10")
        Pin(self, "R6")
        Pin(self, "T1")
        Pin(self, "T16")
        Pin(self, "E5")
        Pin(self, "F11")
        Pin(self, "F8")
        Pin(self, "G10")
        Pin(self, "H6")
        Pin(self, "J10")
        Pin(self, "L6")
        Pin(self, "L9")
        Pin(self, "G7")
        Pin(self, "G9")
        Pin(self, "H10")
        Pin(self, "H8")
        Pin(self, "J7")
        Pin(self, "J9")
        Pin(self, "K10")
        Pin(self, "K8")
        Pin(self, "B13")
        Pin(self, "B4")
        Pin(self, "B9")
        Pin(self, "D10")
        Pin(self, "D7")
        Pin(self, "D15")
        Pin(self, "G13")
        Pin(self, "J15")
        Pin(self, "K13")
        Pin(self, "N15")
        Pin(self, "R13")
        Pin(self, "N10")
        Pin(self, "N7")
        Pin(self, "R4")
        Pin(self, "R8")
        Pin(self, "D2")
        Pin(self, "G4")
        Pin(self, "J2")
        Pin(self, "K4")
        Pin(self, "N2")
        

class XC6SLX9(Spartan6):
    part = 'xc6slx9'

    def __init__(self, name='', board=None, package='tqg144',speed='2'):
        assert package in ['tqg144', 'ftg256']
        Spartan6.__init__(self, name, board, speed)
        if   package == 'tqg144':
            self.TQG144()
        elif package == 'ftg256':
            self.FTG256()

if __name__ == "__main__":
    fpga = XC6SLX9()

