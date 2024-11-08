
from antlr4 import *

class CPP14ParserBase(Parser):
    @staticmethod
    def parser():
        from .cppParser import cppParser
        return cppParser

    def IsPureSpecifierAllowed(self) -> bool:
        try:
            x = self._ctx  # memberDeclarator
            c = x.getChild(0).getChild(0)
            c2 = c.getChild(0)
            p = c2.getChild(1)
            if p is None:
                return False
            yo = isinstance(p, self.parser().ParametersAndQualifiersContext)
            return yo
        except:
            pass
        return False