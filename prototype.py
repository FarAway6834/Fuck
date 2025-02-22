class limit_bit:#수요자가너무병신이라잠시동안병신으로만들어놓겠음
    __slots__ = ('__sbj', '__bit', '__max')
    def __init__(self, *target, bit):
        try: assert len(target)==1
        except:
            raise AttibutrError('limit_bit has only 1 potional arguemnts and only 1 keyworld argument `bit`')
        2pb = 2**bit
        self.__2pb = 2pb
        self.__max = 2pb-1
        self.__sbj = target[0]
        self.__bit = bit
    
    __invert__ = lambda self : self.__max - self
    
    def __and__(self, x):
        #대충 index바로제서 하는걸로 구성할것.
        #or도, xor도
        return ...
    
    def __lshift__(self, x):
        return (2**x)*self - self.__2pb*(x//(2**(self.__bit-x)))
    
    __rshift__ = lambda self, x : self // (2 ** x)
    
    #잠깐만씨발내가왜이런병신같고개쉬운프로젝트가지고지랄햐여하는데