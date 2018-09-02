import symemu2.events

from symemu import Cpu as cpu
from symemu import emulog

from symemu2.descriptor import Descriptor16

@symemu2.events.emulatorEpocFunctionInvoke(1308112282)
def compareHook():
    des1 = Descriptor16(cpu.getReg(0))
    des2 = Descriptor16(cpu.getReg(1))
    
    emulog('Target 1: {}, target 2 {}', str(des1), str(des2))