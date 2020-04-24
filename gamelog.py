import symemu2.events
import symemu

def printStr(slot):
    strPointer = symemu.Cpu.getReg(slot)
    process = symemu.getCurrentProcess()
    
    format = ''
    
    while True:
        temp = process.readProcessMemory(strPointer, 1).decode('utf-8')
        
        if temp == '\0':
            break

        format += temp
        strPointer += 1
    
    symemu.emulog(format)

@symemu2.events.emulatorBreakpointInvoke('bounce', 0x65844, 0x2000C4D4)
def bounceLog():
    printStr(0)
    
@symemu2.events.emulatorBreakpointInvoke('CREEBIES_0x2002EC8B', 0xBC618, 0x2002EC8B)
def creebiesImmLog():
    printStr(1)
