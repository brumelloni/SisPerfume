# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class FramePrincipal
###########################################################################

class FramePrincipal ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Sistema de Gestão de Perfumes", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.MAXIMIZE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.menuMarcas = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Marcas", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.menuMarcas )

		self.menuEssencias = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Essencias", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.menuEssencias )

		self.menuFixacoes = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Fixações", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.menuFixacoes )

		self.menuVolume = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Volumes", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.menuVolume )

		self.m_menubar1.Append( self.m_menu1, u"Cadastros Básicos" )

		self.m_menu2 = wx.Menu()
		self.menuPerfumes = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Perfume", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.menuPerfumes )

		self.menuPerfumesEssencia = wx.MenuItem( self.m_menu2, wx.ID_ANY, u"Essencia", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu2.Append( self.menuPerfumesEssencia )

		self.m_menubar1.Append( self.m_menu2, u"Perfumes" )

		self.m_menu3 = wx.Menu()
		self.menuSobre = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Sobre", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.menuSobre )

		self.menuSair = wx.MenuItem( self.m_menu3, wx.ID_ANY, u"Sair", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu3.Append( self.menuSair )

		self.m_menubar1.Append( self.m_menu3, u"Ajuda" )

		self.SetMenuBar( self.m_menubar1 )


		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_MENU, self.abrirMarcas, id = self.menuMarcas.GetId() )
		self.Bind( wx.EVT_MENU, self.abrirEssencias, id = self.menuEssencias.GetId() )
		self.Bind( wx.EVT_MENU, self.abrirFixacoes, id = self.menuFixacoes.GetId() )
		self.Bind( wx.EVT_MENU, self.abrirVolumes, id = self.menuVolume.GetId() )
		self.Bind( wx.EVT_MENU, self.abrirPerfumes, id = self.menuPerfumes.GetId() )
		self.Bind( wx.EVT_MENU, self.abrirPerfumesEssencia, id = self.menuPerfumesEssencia.GetId() )
		self.Bind( wx.EVT_MENU, self.abrirSobre, id = self.menuSobre.GetId() )
		self.Bind( wx.EVT_MENU, self.abrirSair, id = self.menuSair.GetId() )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def abrirMarcas( self, event ):
		event.Skip()

	def abrirEssencias( self, event ):
		event.Skip()

	def abrirFixacoes( self, event ):
		event.Skip()

	def abrirVolumes( self, event ):
		event.Skip()

	def abrirPerfumes( self, event ):
		event.Skip()

	def abrirPerfumesEssencia( self, event ):
		event.Skip()

	def abrirSobre( self, event ):
		event.Skip()

	def abrirSair( self, event ):
		event.Skip()


###########################################################################
## Class FrameMarcas
###########################################################################

class FrameMarcas ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Marcas", pos = wx.DefaultPosition, size = wx.Size( 471,263 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Descrição:", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer5.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.txtNome = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.txtNome, 1, wx.ALL|wx.EXPAND, 5 )

		self.btnAdicionar = wx.Button( self, wx.ID_ANY, u"Adicionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.btnAdicionar, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer5, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.gridMarcas = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gridMarcas.CreateGrid( 0, 2 )
		self.gridMarcas.EnableEditing( True )
		self.gridMarcas.EnableGridLines( True )
		self.gridMarcas.EnableDragGridSize( False )
		self.gridMarcas.SetMargins( 0, 0 )

		# Columns
		self.gridMarcas.SetColSize( 0, 30 )
		self.gridMarcas.SetColSize( 1, 300 )
		self.gridMarcas.EnableDragColMove( False )
		self.gridMarcas.EnableDragColSize( True )
		self.gridMarcas.SetColLabelSize( 30 )
		self.gridMarcas.SetColLabelValue( 0, u"ID" )
		self.gridMarcas.SetColLabelValue( 1, u"Nome" )
		self.gridMarcas.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridMarcas.EnableDragRowSize( True )
		self.gridMarcas.SetRowLabelSize( 80 )
		self.gridMarcas.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gridMarcas.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer6.Add( self.gridMarcas, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.fecharFrame )
		self.btnAdicionar.Bind( wx.EVT_BUTTON, self.adicionarMarca )
		self.gridMarcas.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.atualizarMarca )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def fecharFrame( self, event ):
		event.Skip()

	def adicionarMarca( self, event ):
		event.Skip()

	def atualizarMarca( self, event ):
		event.Skip()


###########################################################################
## Class FrameFixacoes
###########################################################################

class FrameFixacoes ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Fixações", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Descrição:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer8.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.txtNome = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.txtNome, 1, wx.ALL, 5 )

		self.btnAdicionar = wx.Button( self, wx.ID_ANY, u"Adicionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.btnAdicionar, 0, wx.ALL, 5 )


		bSizer7.Add( bSizer8, 0, wx.EXPAND, 5 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		self.gridFixacoes = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gridFixacoes.CreateGrid( 0, 2 )
		self.gridFixacoes.EnableEditing( True )
		self.gridFixacoes.EnableGridLines( True )
		self.gridFixacoes.EnableDragGridSize( False )
		self.gridFixacoes.SetMargins( 0, 0 )

		# Columns
		self.gridFixacoes.SetColSize( 0, 30 )
		self.gridFixacoes.SetColSize( 1, 300 )
		self.gridFixacoes.EnableDragColMove( False )
		self.gridFixacoes.EnableDragColSize( True )
		self.gridFixacoes.SetColLabelSize( 30 )
		self.gridFixacoes.SetColLabelValue( 0, u"ID" )
		self.gridFixacoes.SetColLabelValue( 1, u"Nome" )
		self.gridFixacoes.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridFixacoes.EnableDragRowSize( True )
		self.gridFixacoes.SetRowLabelSize( 80 )
		self.gridFixacoes.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gridFixacoes.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer10.Add( self.gridFixacoes, 0, wx.ALL, 5 )


		bSizer7.Add( bSizer10, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnAdicionar.Bind( wx.EVT_BUTTON, self.adicionarFixacao )
		self.gridFixacoes.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.atualizarFixacao )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def adicionarFixacao( self, event ):
		event.Skip()

	def atualizarFixacao( self, event ):
		event.Skip()


###########################################################################
## Class FrameVolumes
###########################################################################

class FrameVolumes ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Volumes", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Descrição:", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer5.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.txtNome = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.txtNome, 1, wx.ALL|wx.EXPAND, 5 )

		self.btnAdicionar = wx.Button( self, wx.ID_ANY, u"Adicionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.btnAdicionar, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer5, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.gridVolume = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gridVolume.CreateGrid( 0, 2 )
		self.gridVolume.EnableEditing( True )
		self.gridVolume.EnableGridLines( True )
		self.gridVolume.EnableDragGridSize( False )
		self.gridVolume.SetMargins( 0, 0 )

		# Columns
		self.gridVolume.SetColSize( 0, 30 )
		self.gridVolume.SetColSize( 1, 300 )
		self.gridVolume.EnableDragColMove( False )
		self.gridVolume.EnableDragColSize( True )
		self.gridVolume.SetColLabelSize( 30 )
		self.gridVolume.SetColLabelValue( 0, u"ID" )
		self.gridVolume.SetColLabelValue( 1, u"Nome" )
		self.gridVolume.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridVolume.EnableDragRowSize( True )
		self.gridVolume.SetRowLabelSize( 80 )
		self.gridVolume.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gridVolume.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer6.Add( self.gridVolume, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnAdicionar.Bind( wx.EVT_BUTTON, self.adicionarVolume )
		self.gridVolume.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.atualizarMarca )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def adicionarVolume( self, event ):
		event.Skip()

	def atualizarMarca( self, event ):
		event.Skip()


###########################################################################
## Class FrameEssencias
###########################################################################

class FrameEssencias ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Essencias", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Descrição:", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )

		bSizer5.Add( self.m_staticText2, 0, wx.ALL, 5 )

		self.txtNome = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.txtNome, 1, wx.ALL|wx.EXPAND, 5 )

		self.btnAdicionar = wx.Button( self, wx.ID_ANY, u"Adicionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.btnAdicionar, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer5, 0, wx.ALL|wx.EXPAND, 5 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.gridEssencias = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gridEssencias.CreateGrid( 0, 2 )
		self.gridEssencias.EnableEditing( True )
		self.gridEssencias.EnableGridLines( True )
		self.gridEssencias.EnableDragGridSize( False )
		self.gridEssencias.SetMargins( 0, 0 )

		# Columns
		self.gridEssencias.SetColSize( 0, 30 )
		self.gridEssencias.SetColSize( 1, 300 )
		self.gridEssencias.EnableDragColMove( False )
		self.gridEssencias.EnableDragColSize( True )
		self.gridEssencias.SetColLabelSize( 30 )
		self.gridEssencias.SetColLabelValue( 0, u"ID" )
		self.gridEssencias.SetColLabelValue( 1, u"Nome" )
		self.gridEssencias.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridEssencias.EnableDragRowSize( True )
		self.gridEssencias.SetRowLabelSize( 80 )
		self.gridEssencias.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gridEssencias.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer6.Add( self.gridEssencias, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnAdicionar.Bind( wx.EVT_BUTTON, self.adicionarEssencia )
		self.gridEssencias.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.atualizarMarca )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def adicionarEssencia( self, event ):
		event.Skip()

	def atualizarMarca( self, event ):
		event.Skip()


###########################################################################
## Class FramePerfumesGrid
###########################################################################

class FramePerfumesGrid ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Perfumes", pos = wx.DefaultPosition, size = wx.Size( 1100,272 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		bSizer23 = wx.BoxSizer( wx.VERTICAL )

		self.gridPerfumes = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.gridPerfumes.CreateGrid( 0, 6 )
		self.gridPerfumes.EnableEditing( True )
		self.gridPerfumes.EnableGridLines( True )
		self.gridPerfumes.EnableDragGridSize( False )
		self.gridPerfumes.SetMargins( 0, 0 )

		# Columns
		self.gridPerfumes.SetColSize( 0, 30 )
		self.gridPerfumes.SetColSize( 1, 200 )
		self.gridPerfumes.SetColSize( 2, 100 )
		self.gridPerfumes.SetColSize( 3, 200 )
		self.gridPerfumes.SetColSize( 4, 200 )
		self.gridPerfumes.SetColSize( 5, 200 )
		self.gridPerfumes.EnableDragColMove( False )
		self.gridPerfumes.EnableDragColSize( True )
		self.gridPerfumes.SetColLabelSize( 30 )
		self.gridPerfumes.SetColLabelValue( 0, u"ID" )
		self.gridPerfumes.SetColLabelValue( 1, u"Nome" )
		self.gridPerfumes.SetColLabelValue( 2, u"Quantidade" )
		self.gridPerfumes.SetColLabelValue( 3, u"Volume" )
		self.gridPerfumes.SetColLabelValue( 4, u"Marca" )
		self.gridPerfumes.SetColLabelValue( 5, u"Fixação" )
		self.gridPerfumes.SetColLabelValue( 6, wx.EmptyString )
		self.gridPerfumes.SetColLabelValue( 7, wx.EmptyString )
		self.gridPerfumes.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.gridPerfumes.EnableDragRowSize( True )
		self.gridPerfumes.SetRowLabelSize( 80 )
		self.gridPerfumes.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.gridPerfumes.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer23.Add( self.gridPerfumes, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer22.Add( bSizer23, 1, wx.EXPAND, 5 )

		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

		self.btnAdicionar = wx.Button( self, wx.ID_ANY, u"Adicionar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.btnAdicionar, 1, wx.ALL, 5 )

		self.btnSalvar = wx.Button( self, wx.ID_ANY, u"Salvar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.btnSalvar, 1, wx.ALL, 5 )


		bSizer22.Add( bSizer24, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer22 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btnAdicionar.Bind( wx.EVT_BUTTON, self.adicionarPerfume )
		self.btnSalvar.Bind( wx.EVT_BUTTON, self.salvarPerfume )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def adicionarPerfume( self, event ):
		event.Skip()

	def salvarPerfume( self, event ):
		event.Skip()


