import symemu2.events
import symemu2.common

from ctypes import *

from symemu import Cpu as cpu
import symemu

# Please see epoc9.def as a reference of SID
# DoConnect takes CServer2 pointer as the first arg (this, r0), the second argument
# is a reference to RMessage2, so r1 should contains the pointer to needed message
#
# IPC Symbian sends connect message with the first IPC message to always be the version,
# which is a packed struct with the following structure
#
# uint8_t major; uint8_t minor; uint16_t build
#
# The hook is to answers the question if in EKA2L1, is there something that corrupted this 
# message, or it's just because of different structure ? Note that the RMessage2 structure
# is taken from Symbian Source, which is identical to Symbian^3

@symemu2.events.emulatorEpocFunctionInvoke(424139850)
def serverDoConnectHook():
    message2Ptr = cpu.getReg(1)
    handle = symemu.readDword(message2Ptr)
    func = symemu.readDword(message2Ptr + 4)
    verMajor = symemu.readByte(message2Ptr + 8)
    verMinor = symemu.readByte(message2Ptr + 9)
    verBuild = symemu.readWord(message2Ptr + 10)
    sessionPtr = symemu.readDword(message2Ptr + 24)
    flag = symemu.readDword(message2Ptr + 28)
    
    symemu.emulog('Func: {}, Version {}.{}({}), flag: {}', c_int(func), verMajor, verMinor, verBuild, flag)