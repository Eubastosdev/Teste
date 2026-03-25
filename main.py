class Pessoa:
	def __init__(self,nome):
		self.nome = nome
		
	def comprimentar(self):
		print(f"Saudações,{self.nome}.")


p = Pessoa('Luiz')
p.comprimentar()