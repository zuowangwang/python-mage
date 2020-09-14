# -*- comding:utf-8   -*-
#121集

class Document:
    def __init__(self, content):
        self.content = content

    def print(self):
        raise NotImplementedError

class Word(Document): pass

def printable(cls):
    def _print(self):
        print('{} : {}'.format(type(self).__name__, self.content))
    cls.print = _print
    return cls

@printable
class printableWord(Word):pass


pw = printableWord('test word1')
pw.print()
print('\n')

class PrintableMinxin:
    def print(self):
        print('{} : {}'.format(type(self).__name__, self.content))


class superPrintableMinxin(PrintableMinxin):
    def print(self):
        print('~~~~~~~~~~~~')
        super().print()
        print('~~~~~~~~~~~~')



class Printablepdfminxin(PrintableMinxin, Word):pass

pdfm = Printablepdfminxin('tsest minxin')
print(pdfm.__class__.mro())
pdfm.print()
print('\n')



class Printablepdfminxin(superPrintableMinxin, Word):pass

pdfm = Printablepdfminxin('tsest123123 m123inxin')
print(pdfm.__class__.mro())
pdfm.print()















