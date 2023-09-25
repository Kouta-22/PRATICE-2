
from mrjob.job import MRJob
import re
palavra_ragex = re.compile(r'[\w]+')
class QuantidadePalavra(MRJob):
    def mapper(self, _,linha):
        for p in palavra_ragex.findall(linha):
            yield p.lower(),  1
    
    def reducer(self, p, qtd):
        yield p,sum(qtd)
if __name__ == '__main__':
    QuantidadePalavra.run()

