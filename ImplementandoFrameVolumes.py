import wx
import guiperfumes
import db

# Implementing FrameVolumes
class FrameVolumes(guiperfumes.FrameVolumes):
	def __init__( self, parent ):
		guiperfumes.FrameVolumes.__init__( self, parent )

		self.atualizarGrid()
	# Handlers for FrameVolumes events.
	def adicionarVolume( self, event ):
		nome=self.txtNome.GetValue() #Recupera o conteúdo da caixa de texto
		db.inserirVolume(nome) #Chama a função inserir volume do arquivo db.py
		#Exibe uma mensagem ao usuário confirmado o sucesso na inserção
		wx.MessageBox(message="Volume Inserido com Sucesso",caption="SisPerfumes",style=wx.OK,parent=self)
		self.atualizarGrid()#Atualiza o grid com a relação de volumes
	def fecharFrame( self, event ):
		self.Show(False)

	def adicionarVolume( self, event ):
		# TODO: Implement adicionarVolume
		pass

	#Essa função é chamada quando o usuário edita o conteúdo de uma célula do meu grid
	def atualizarVolume( self, event ):
		# TODO: Implement atualizarVolume
		pass
		nome_volume=self.gridVolume.GetCellValue(event.GetRow(),event.GetCol()) #Recupera o nome do volume editado
		if (nome_volume): #Se o conteúdo não for vazio, faça
			id_volume=int(self.gridVolume.GetCellValue(event.GetRow(),0))#Pegue na linha editada, o conteúdo da primeira coluna
			db.atualizarVolumes(id_volume,nome_volume) #Chame a função para atualizar um volume
			wx.MessageBox(message="Volume Atualizado com Sucesso",caption="SysPerfumes",style=wx.OK,parent=self)
	def atualizarGrid(self):
		if (self.gridVolume.GetNumberRows()>0):
			self.gridVolume.DeleteRows(0,self.gridVolume.GetNumberRows()) #Limpa a tabela
		volumes=db.listarVolumes() #Chama a função listar volumes, retornando a lista de volumes existentes
		for volume in volumes:
			self.gridVolume.AppendRows(1)#Adiciona uma linha em branco
			self.gridVolume.SetCellValue(self.gridVolume.GetNumberRows()-1,0,str(volume[0])) #adicione o id do volume
			self.gridVolume.SetCellValue(self.gridVolume.GetNumberRows() - 1, 1, volume[1]) #adiciona o nome do volume
			self.gridVolume.SetReadOnly(self.gridVolume.GetNumberRows() - 1, 0, True) #Informa que a coluna 0(ID) é somente leitura