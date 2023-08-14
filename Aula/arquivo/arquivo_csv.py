class ArquivoCSV(object):

  def __init__(self, arquivo: str):
    self.arquivo = arquivo
    self.conteudo = self._extrair_conteudo()
    self.colunas = self._extrair_nome_colunas()

  def _extrair_conteudo(self) -> list:
    with open(file=self.arquivo, mode='r', encoding='utf8') as arquivo:
      return arquivo.readlines()

  def _extrair_nome_colunas(self) -> list:
    return self.conteudo[0].strip().split(sep=',')

  def extrair_coluna(self, indice_coluna: str) -> list:
    return list(map(lambda linha: linha.strip().split(",")[indice_coluna], self.conteudo))[1:]