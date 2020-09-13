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















