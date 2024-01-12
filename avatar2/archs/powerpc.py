from capstone import *
from keystone.keystone_const import *
from unicorn import *
from unicorn.mips_const import *
from .architecture import Architecture
import avatar2

from avatar2.installer.config import QEMU, PANDA, OPENOCD, GDB_MULTI

#CS_ARCH_PPC', 'KS_ARCH_PPC', 'KS_MODE_PPC32', 'KS_MODE_PPC64', 'UC_ARCH_PPC', 'UC_MODE_PPC32', 'UC_MODE_PPC64'

class PPC32(Architecture):

    qemu_name = 'ppc'
    gdb_name = 'powerpc:common'
    endian = 'big'

    get_qemu_executable = Architecture.resolve(QEMU)
    get_panda_executable = Architecture.resolve(PANDA)
    get_gdb_executable  = Architecture.resolve(GDB_MULTI)
    get_oocd_executable = Architecture.resolve(OPENOCD)


    registers = {
        'r0':0, 'r1':1, 'r2':2, 'r3':3, 'r4':4, 'r5':5, 'r6':6, 'r7':7, 'r8':8, 
        'r9':9, 'r10':10, 'r11':11, 'r12':12, 'r13':13, 'r14':14, 'r15':15, 
        'r16':16, 'r17':17, 'r18':18, 'r19':19, 'r20':20, 'r21':21, 'r22':22, 
        'r23':23, 'r24':24, 'r25':25, 'r26':26, 'r27':27, 'r28':28, 'r29':29, 
        'r30':30, 'r31':31,
        'sp':1,
        'pc':64,
        'msr':65,
        'cr': 66,
        'lr': 67,
        'ctr': 68,
        'xer': 69

    }

    unicorn_registers = {}

    pc_name = 'pc'
    sr_name = 'msr'

    capstone_arch = CS_ARCH_PPC
    keystone_arch = KS_ARCH_PPC
    capstone_mode = CS_MODE_BIG_ENDIAN

    unicorn_arch = UC_ARCH_PPC
    unicorn_mode = UC_MODE_PPC32



class PPC_MPC8544DS(PPC32):

    
    qemu_name = 'ppc'
    gdb_name = 'powerpc:MPC8XX'

