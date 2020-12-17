import wx
import guiperfumes
import db

# Implementing FrameFixacoes
class FrameFixacoes(guiperfumes.FrameFixacoes):
	def __init__( self, parent ):
		guiperfumes.FrameFixacoes.__init__( self, parent )

		self.atualizarGrid()
	# Handlers for FrameFixacoes events.
	def adicionarFixacao( self, event ):
		nome=self.txtNome.GetValue() #Recupera o conteúdo da caixa de texto
		db.inserirFixacao(nome) #Chama a função inserir fixacao do arquivo db.py
		#Exibe uma mensagem ao usuário confirmado o sucesso na inserção
		wx.MessageBox(message="Fixação Inserida com Sucesso",caption="SisPerfumes",style=wx.OK,parent=self)
		self.atualizarGrid()#Atualiza o grid com a relação de fixacoes
	def fecharFrame( self, event ):
		self.Show(False)

	def adicionarFixacao( self, event ):
		# TODO: Implement adicionarFixacao
		pass

	#Essa função é chamada quando o usuário edita o conteúdo de uma célula do meu grid
	def atualizarFixacao( self, event ):
		# TODO: Implement atualizarFixacao
		pass
		nome_fixacao=self.gridFixacoes.GetCellValue(event.GetRow(),event.GetCol()) #Recupera o nome da fixacao editado
		if (nome_fixacao): #Se o conteúdo não for vazio, faça
			id_fixacao=int(self.gridFixacoes.GetCellValue(event.GetRow(),0))#Pegue na linha editada, o conteúdo da primeira coluna
			db.atualizarFixacao(id_fixacao,nome_fixacao) #Chame a função para atualizar uma fixacao
			wx.MessageBox(message="Fixação Atualizada com Sucesso",caption="SysPerfumes",style=wx.OK,parent=self)
	def atualizarGrid(self):
		if (self.gridFixacoes.GetNumberRows()>0):
			self.gridFixacoes.DeleteRows(0,self.gridFixacoes.GetNumberRows()) #Limpa a tabela
		fixacoes=db.listarFixacoes() #Chama a função listar fixacoes, retornando a lista de fixacoes existentes
		for fixacao in fixacoes:
			self.gridFixacoes.AppendRows(1)#Adiciona uma linha em branco
			self.gridFixacoes.SetCellValue(self.gridFixacoes.GetNumberRows()-1,0,str(fixacao[0])) #adicione o id da fixacao
			self.gridFixacoes.SetCellValue(self.gridFIxacoes.GetNumberRows() - 1, 1, fixacao[1]) #adiciona o nome da fixacao
			self.gridFixacoes.SetReadOnly(self.gridFixacoes.GetNumberRows() - 1, 0, True) #Informa que a coluna 0(ID) é somente leitura