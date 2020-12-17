import wx
import guiperfumes
import db

# Implementing FrameEssencias
class FrameEssencias(guiperfumes.FrameEssencias):
	def __init__( self, parent ):
		guiperfumes.FrameEssencias.__init__( self, parent )

		self.atualizarGrid()
	# Handlers for FrameEssencias events.
	def adicionarEssencia( self, event ):
		nome=self.txtNome.GetValue() #Recupera o conteúdo da caixa de texto
		db.inserirEssencia(nome) #Chama a função inserir essencia do arquivo db.py
		#Exibe uma mensagem ao usuário confirmado o sucesso na inserção
		wx.MessageBox(message="Volume Inserido com Sucesso",caption="SisPerfumes",style=wx.OK,parent=self)
		self.atualizarGrid()#Atualiza o grid com a relação de essencias
	def fecharFrame( self, event ):
		self.Show(False)

	def adicionarEssencia( self, event ):
		# TODO: Implement adicionarEssencia
		pass

	#Essa função é chamada quando o usuário edita o conteúdo de uma célula do meu grid
	def atualizarEssencia( self, event ):
		# TODO: Implement atualizarEssencia
		pass
		nome_essencia=self.gridEssencias.GetCellValue(event.GetRow(),event.GetCol()) #Recupera o nome da essencia editado
		if (nome_essencia): #Se o conteúdo não for vazio, faça
			id_essencia=int(self.gridEssencias.GetCellValue(event.GetRow(),0))#Pegue na linha editada, o conteúdo da primeira coluna
			db.atualizarEssencia(id_essencia,nome_essencia) #Chame a função para atualizar uma essencia
			wx.MessageBox(message="Essencia Atualizada com Sucesso",caption="SysPerfumes",style=wx.OK,parent=self)
	def atualizarGrid(self):
		if (self.gridEssencias.GetNumberRows()>0):
			self.gridEssencias.DeleteRows(0,self.gridEssenciasGetNumberRows()) #Limpa a tabela
		essencias=db.listarEssencias() #Chama a função listar essencias, retornando a lista de essencias existentes
		for essencia in enssencias:
			self.gridEssencias.AppendRows(1)#Adiciona uma linha em branco
			self.gridEssencias.SetCellValue(self.gridEssencias.GetNumberRows()-1,0,str(essencia[0])) #adicione o id da essencia
			self.gridEssencias.SetCellValue(self.gridEssencias.GetNumberRows() - 1, 1, essencia[1]) #adiciona o nome da essencia
			self.gridEssencias.SetReadOnly(self.gridEssencias.GetNumberRows() - 1, 0, True) #Informa que a coluna 0(ID) é somente leitura