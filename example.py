print "Moofinder has been launched \n Importing libraries..."
try:
    import gi
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk #imports Gtk library
    print "Gtk library has been imported"
except:
    print "unable to import Gtk library. (needs to be installed)"
try:
    import math
    print "math.pi library has been imported"
except:
    print ("math.pi library is missing")
    sys.exit

class Buglump:
    
    def on_window1_destroy(self, object, data = None): #quit with X
        print "quit with cancel"
        Gtk.main_quit()

    def on_gtk_quit_activate(self, menuitem, data = None): #quit with file >> quit
        print "quit with menu"
        Gtk.main_quit()
        
    def on_gtk_about_activate(self, menuitem, data = None): #about page
        print "help about selected"
        self.response = self.aboutdialog.run() #opens window with .run() method
        self.aboutdialog.hide() #waits for Close button, .hide() will close the box

    def on_push_status_activate(self, menuitem, data = None):
        self.status_count += 1
        self.statusbar.push(self.context_id, "Message number %s" %str(self.status_count))

    def on_pop_status_activate(self, menuitem, data = None):
        self.status_count -= 1
        self.statusbar.pop(self.context_id)

    def on_clear_status_activate(self, menuitem, data = None):
        while (self.status_count > 0):
            self.statusbar.pop(self.context_id)
            self.status_count -= 1

    def on_sfm_button_clicked(self, menuitem, data = None):
        self.entry1 = self.builder.get_object("entry1")
        self.entry2 = self.builder.get_object("entry2")
        self.result1 = self.builder.get_object("result1")

        self.sfm = float(self.entry1.get_text()) #gets and converts values to floats
        self.diameter = float(self.entry2.get_text())
        #calculates result, converts to int to round, converts to a string to display text
        self.rpm = str(int(self.sfm * ((12/math.pi)/self.diameter)))

        print "RPM calculated"

        self.result1.set_text(self.rpm)
        

    def __init__(self):
        self.gladefile = "example2.glade" #filename
        self.builder = Gtk.Builder()
        self.builder.add_from_file(self.gladefile)

        self.builder.connect_signals(self) #connect signals to defs above

        self.window = self.builder.get_object("window1") #gets window1 object
        self.aboutdialog = self.builder.get_object("aboutdialog") #gets aboutdialog window
        self.statusbar = self.builder.get_object("statusbar1") #gets statusbar
        self.context_id = self.statusbar.get_context_id("status") #gets context id
        self.window.show() #shows window1 and everything in it

        self.status_count = 0 #initializes variable 'status_count', sets to 0

if __name__ == "__main__":
    main = Buglump() # name of the class
    Gtk.main() # to run
