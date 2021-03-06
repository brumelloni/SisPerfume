"""Subclass of FrameFixacoes, which is generated by wxFormBuilder."""

import guiperfumes
import FrameFixacoes

# Implementing FrameFixacoes
class ProjSisPerfumesFrameFixacoes( guiperfumes.FrameFixacoes ):
	def __init__( self, parent ):
		guiperfumes.FrameFixacoes.__init__( self, parent )

	# Handlers for FrameFixacoes events.
	def adicionarFixacao( self, event ):
		FrameFixacoes.FrameFixacoes.adicionarFixacao(self.txtNome, event)

	def atualizarFixacao( self, event ):
		FrameFixacoes.FrameFixacoes.atualizarFixacao(self.txtNome, event)


