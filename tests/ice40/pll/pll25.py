from magma import wire, compile, EndCircuit
from loam.boards.icestick import IceStick
from mantle.lattice.ice40.PLL import SB_PLL

icestick = IceStick()
icestick.Clock.on()
icestick.PMOD0[0].rename('O').output().on()

main = icestick.main()

pll = SB_PLL(25000000, 12000000)

wire( main.CLK, pll.I )
wire( pll.O, main.O )

EndCircuit()
