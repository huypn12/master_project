from .model import Model

class Bees3(Model):
    def __init__(self):
        super().__init__()
        self.bscc_pfuncs = [
            lambda p: self.f_bscc_0(p),
            lambda p: self.f_bscc_1(p),
            lambda p: self.f_bscc_2(p),
            lambda p: self.f_bscc_3(p),
            lambda p: self.f_bscc_4(p),
            lambda p: self.f_bscc_5(p),
            lambda p: self.f_bscc_6(p),
            lambda p: self.f_bscc_7(p),
            lambda p: self.f_bscc_8(p),
            lambda p: self.f_bscc_9(p)
        ]

    def f_bscc_0(self, p):
        pass

    def f_bscc_1(self, p):
        pass

    def f_bscc_2(self, p):
        pass
    
    def f_bscc_3(self, p):
        pass
    
    def f_bscc_4(self, p):
        pass

    def get_bscc_pfuncs(self, ):
        return self.bscc_pfuncs

    def eval_bscc_pfuncs(self, p):
        return [f(p) for f in self.bscc_pfuncs]

