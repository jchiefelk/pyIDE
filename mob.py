# UI
# Imort modules
import os,sys
from gi.repository import Gtk, Vte,Pango,PangoCairo
from gi.repository import GLib, Gdk
from gi.repository import GObject
from gi.repository import GtkSource
# Graphical User Interface
# Classes - Core M.O.B Functions
StatusBar = Gtk.Statusbar()
source = GtkSource.View()
buffer = source.get_buffer()
terminal = Vte.Terminal()
textview = Gtk.TextView()
entry = Gtk.Entry()
menu = Gtk.MenuBar()
filemenu = Gtk.Menu()
scrolledwindow1 = Gtk.ScrolledWindow()
vpaned = Gtk.VPaned()
grid = Gtk.Grid()
#Syntax Highlighting
buffersource = GtkSource.Buffer()
language = GtkSource.Language()
# buffersource.set_language(language)
buffersource.set_highlight_syntax(True)
# style = GtkSource.StyleScheme()
# style.get_style(classic)
# buffersource.set_style_scheme(style)
# Starting Window
class MainWindow(Gtk.Window):
    file_tag = ""
    # Open File function
    def open_file(menuitem, user_param):
        chooser = Gtk.FileChooserDialog(title="Open a file",action=Gtk.FileChooserAction.OPEN, buttons=(Gtk.STOCK_CANCEL,Gtk.ResponseType.CANCEL,Gtk.STOCK_OPEN,Gtk.ResponseType.OK))
        chooser.set_default_response(Gtk.ResponseType.OK)
        filter = Gtk.FileFilter()
        filter2 = Gtk.FileFilter()
        filter2.set_name("All Files")
        filter2.add_pattern("*.*")
        chooser.add_filter(filter2)
        response = chooser.run()
        if response == Gtk.ResponseType.OK:
            filename = chooser.get_filename()
            global file_tag
            file_tag = filename
            textbuffer = source.get_buffer()
            print "Opened File: " + filename
            StatusBar.push(0,"Opened File: " + filename)
            index = filename.replace("\\","/").rfind("/") + 1
            file = open(filename, "r")
            text = file.read()
            textbuffer.set_text(text)
            file.close()
            chooser.destroy()
        elif response == Gtk.ResponseType.CANCEL:
            chooser.destroy()
            chooser.destroy()
    def save_file(menuitem,user_param):
            textbuffer = source.get_buffer()
            StatusBar.push(0,"Saved File: " + file_tag)
            index = file_tag.replace("\\","/").rfind("/") + 1
            text = textbuffer.get_text(textbuffer.get_start_iter() , textbuffer.get_end_iter(),False)
            file = open(file_tag, "w+")
            file.write(text)
            file.close()

    def save_file_as(menuitem,user_param):
        chooser = Gtk.FileChooserDialog(title="Save file",action=Gtk.FileChooserAction.SAVE, buttons=(Gtk.STOCK_CANCEL,Gtk.ResponseType.CANCEL,Gtk.STOCK_SAVE,Gtk.ResponseType.OK))
        chooser.set_default_response(Gtk.ResponseType.OK)
        filter2 = Gtk.FileFilter()
        filter2.set_name("All Files")
        filter2.add_pattern("*.*")
        chooser.add_filter(filter2)
        response = chooser.run()
        if response == Gtk.ResponseType.OK:
            filename = chooser.get_filename()
            textbuffer = source.get_buffer()
            print "Saved File: " + filename
            StatusBar.push(0,"Saved File: " + filename)
            index = filename.replace("\\","/").rfind("/") + 1
            text = textbuffer.get_text(textbuffer.get_start_iter() , textbuffer.get_end_iter(),False)
            file = open(filename, "w")
            file.write(text)
            file.close()
            chooser.destroy()
        elif response == Gtk.ResponseType.CANCEL:
            chooser.destroy()
            chooser.destroy()

	# "Automatic" code generation
	# LaTeX sum-to-for loop converter
    def entry_go(self,widget):
	input = entry.get_text()
	command= input+"\n"
	
	# Instructions for a C Project
	if input[5] =="C" and input[6]=="$":
		print('Fuck a Job and Check Im in the M.O.B with Respect')
		index = input[20]
		start = input[22]
		end = input[26]
		# Declare loop variable
		var = 'int'+' '+index+';'+'\n'
		# loop indice
		textbuffer = source.get_buffer()
		textbuffer.insert_at_cursor(var)
		C_output = 'for('+index+'='+start+';'+index+'<='+end+';'+index+'++)'
		textbuffer.insert_at_cursor(C_output)
		# Add brackets for C code
		textbuffer.insert_at_cursor('{')
		# Add newline when encounter whitespace
		#Loop Contents
		loop_list=input[28:len(input)]
		func_start = 0
		func_end = 0
		start = [ ] 
		end = [ ]
		for x in range(0,len(input)-28):
			if loop_list[x]== ' ' and loop_list[x+1] !=' ':
				func_start = x+1
				start.append(func_start)
			if loop_list[x]!= ' ' and (x+1)==len(loop_list) or loop_list[x+1] ==' ':
				func_end = x+1
				end.append(func_end)
				
		x = 0
		for x in range(0,len(start)): 
			textbuffer.insert_at_cursor('\n')
			loop_contents = str(loop_list[start[x]:end[x]])+';'
			textbuffer.insert_at_cursor(loop_contents)
			
		textbuffer.insert_at_cursor('\n')
		textbuffer.insert_at_cursor('}')
		entry.set_text(' ')
		entry.set_text('FIGA:')

	if input[5] == 'p' or input[5] == 'P' and input[6]=='y' and input[7]=='t' and input[11]=='$':	
		index = input[25]
		start = input[27]
		end = input[31]
		python_output = 'for'+' '+index+' ' +'in'+' '+'range'+'('+start+','+end+'):'
		textbuffer = source.get_buffer()
		textbuffer.insert_at_cursor(python_output)
		
	
	

    def function1(self,widget):
	scrolledwindow1.remove(source)
	scrolledwindow1.add(source)
	file_tag = ''
	textbuffer = source.get_buffer()
	textbuffer.set_text('')
	
    
    def __init__(self):
        Gtk.Window.__init__(self)
        # Window title and Icon
        self.set_title("M.O.B")
        # Vertical Box
        self.box = Gtk.VBox(homogeneous=False, spacing=0)
        self.add(self.box)
        # Menu
        filem = Gtk.MenuItem("File")
        #Popup Menu
        terminal.menu = Gtk.Menu()
        menu_item = Gtk.ImageMenuItem.new_from_stock("gtk-copy", None)
        menu_item.connect_after("activate", lambda w: self.copy_clipboard())
        terminal.menu.add(menu_item)
        # Import
        imenu = Gtk.Menu()
        importm = Gtk.MenuItem("Functions")
        importm.set_submenu(imenu)
        ifunction1 = Gtk.MenuItem("New Source")
        imenu.append(ifunction1)
	# function Signals
	ifunction1.connect("activate",self.function1)
	#Signals for other menu items
        openm = Gtk.MenuItem("Open")
        savem = Gtk.MenuItem("Save")
        saveasm = Gtk.MenuItem("Save As")
        exit = Gtk.MenuItem("Exit")
        openm.connect("activate",self.open_file)
        saveasm.connect("activate",self.save_file_as)
        savem.connect("activate",self.save_file)
        exit.connect("activate", Gtk.main_quit)
        filemenu.append(importm)
        filemenu.append(openm)
        filemenu.append(savem)
        filemenu.append(saveasm)
        filemenu.append(exit)
        filem.set_submenu(filemenu)
        menu.append(filem)
        # Source View
	source.new_with_buffer(buffersource)
        source.set_show_line_numbers(True)
        source.set_show_line_marks(True)
        source.set_highlight_current_line(True)
        # source.modify_bg(Gtk.StateType.NORMAL, Gdk.color_parse("silver"))
        # source.modify_fg(Gtk.StateType.NORMAL, Gdk.color_parse("black"))
	source.modify_font(Pango.FontDescription('monospace 12'))
        # Terminal settings
        terminal.set_scroll_on_output(True)
        terminal.set_scroll_on_keystroke(True)
        #terminal.set_visible(True)
        terminal.set_scrollback_lines(-1)
        terminal.set_font_from_string("monospace 12")
        terminal.set_color_background(Gdk.color_parse("black"))
        terminal.set_color_foreground(Gdk.color_parse("silver"))
        terminal.set_cursor_blink_mode(True)
	terminal.connect("child-exited", lambda w: gtk.main_quit())
	terminal.set_encoding("UTF-8")
        terminal.fork_command_full(Vte.PtyFlags.DEFAULT,os.environ['HOME'],["/bin/bash"],[],GLib.SpawnFlags.DO_NOT_REAP_CHILD,None,None,)
        # set Terminal PATH
	command= "PATH=/usr/local/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/usr/texbin"+'\n'
	length = len(command)
        terminal.feed_child(command, length)  	
	command = 'PYTHONPATH='+'\n'
	length = len(command)
	terminal.feed_child(command,length)	
	command = 'reset'+'\n'
	length = len(command)
	terminal.feed_child(command,length)
	# Text Entry Boxt
	entry.set_text('FIGA:')
	entry.connect("activate",self.entry_go)
        # Scrolled Text Window
        scrolledwindow1.set_hexpand(True)
        scrolledwindow1.set_vexpand(True)
        scrolledwindow1.set_border_width(10)
	scrolledwindow1.add(source)
        # Vertical Pane
 	vpaned.add1(scrolledwindow1)
        vpaned.add2(terminal)
        # Pack everything in vertical box
 	self.box.pack_start(menu, False, False, 0)
        self.box.pack_start(entry, False, False, 0)
	self.box.pack_start(vpaned, True, True, 0)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()



#Starting Window
window = MainWindow()
Gtk.main()

