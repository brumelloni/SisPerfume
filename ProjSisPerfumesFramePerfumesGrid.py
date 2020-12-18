"""Subclass of FramePerfumesGrid, which is generated by wxFormBuilder."""

import guiperfumes
import FramePerfumesGrid

# Implementing FramePerfumesGrid
class ProjSisPerfumesFramePerfumesGrid( guiperfumes.FramePerfumesGrid ):
	def __init__( self, parent ):
		guiperfumes.FramePerfumesGrid.__init__( self, parent )

	# Handlers for FramePerfumesGrid events.
	def adicionarPerfume( self, event ):
		FramePerfumesGrid.FramePerfumes.adicionarPerfume(self, event)


	def salvarPerfume( self, event ):
		FramePerfumesGrid.FramePerfumes.salvarPerfume(self.gridPerfumes, event)

