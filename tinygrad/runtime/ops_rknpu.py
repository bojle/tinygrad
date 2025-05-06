import os
from tinygrad.device import Compiled, BufferSpec, Allocator

class RKNPUAllocator(Allocator):
    def __init__(self):
        super().__init__()
    def _alloc(self, size, options:BufferSpec):
        pass
    def _free(self, opaque, options:BufferSpec):
        pass
    def _copyin(self, dest, src:memoryview):
        pass
    def _copyout(self, dest:memoryview, src):
        pass
    def _transfer(self, dest, src, sz:int, src_dev, dest_dev):
        pass
    def _offset(self, buf, size:int, offset:int): 
        pass

class RKNPURenderer:
    pass

class RKNPUProgram:
    pass

class RKNPUDevice(Compiled):
    dev_name = "/dev/dri/card1"
    def __init__(self, device: str):
        print("RKNN Backend selected")
        super().__init__(device, RKNPUAllocator(), RKNPURenderer(), RKNPUProgram())
    def synchronize(self):
        pass
    #for opaque,sz,options in self.pending_copyin: self.allocator.free(opaque, sz, options)
    #self.pending_copyin.clear()

