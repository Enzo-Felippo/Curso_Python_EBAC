class ArquivoTXT(object):

  def __init__(self, arquivo: str):
    self.arquivo = arquivo
    self.conteudo = self._extrair_conteudo()

  def _extrair_conteudo(self):
    with open(file=self.arquivo, mode='r', encoding='utf8') as arquivo:
      return arquivo.readlines()

  def extrair_linha(self, numero_linha: int):
    return self.conteudo[numero_linha]