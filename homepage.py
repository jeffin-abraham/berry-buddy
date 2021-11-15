import tkinter as tk                
from tkinter import Button, font  as tkfont
from tkinter.constants import N

class BerryApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, minsize=600, weight=1)
        container.grid_columnconfigure(0, minsize=1000, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, IdentifyPage, MapPage, CatalogPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

#space in StartPage (label and logo)
def space(self):
    space_label = tk.Label(self, height=5, bg='#e2c7d8')
    space_label.pack()

#space in StartPage (logo and btn)
def btnspace(self):
    space_label = tk.Label(self, height=2, bg='#e2c7d8')
    space_label.pack()
    
    
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#e2c7d8')
        self.controller = controller
        self.controller.title("BerryBuddy.exe")
        
        space(self)
        
        disclamer_label = tk.Label(self, bg='#0D0D0D', text="Disclamer: \n This application is not intended to supply toxicological advice to anyone. \n The creators of this application have referenced sources believed to be reliable in an effort to confirm the accuracy and completeness of the presented herein. \n However, none of the creators warrant that the information is in every respect accurate or complete, and \n they are nor responsible for errors or omissions or for any consequences from application of the information in this book. \n" \
                                             "Never eat any wild plant until you have positively identified the plant as edible. \n There is no substitute for the knowledge of a trained botanist or horticulturist for plant identification. \n In cases of accidental exposure or ingestion of toxic or poisonous berry varieties, contact a Poison Control Center (1-800-222-1222).")
        disclamer_label.pack()
        
        btnspace(self)
        
        logo_photo = tk.PhotoImage(file='berrylogo.gif')
        logo_photo_label = tk.Label(self,image=logo_photo, bg="#e2c7d8")
        logo_photo_label.pack()
        logo_photo_label.image = logo_photo
        
        btnspace(self)
        
        terms_label = tk.Label(self, text='Type "Agree" to get started', bg='#3d3d5c', fg='white')
        terms_label.pack(pady=10)

        my_term = tk.StringVar()
        term_entry_box = tk.Entry(self, textvariable=my_term, width=22)
        term_entry_box.focus_set()
        term_entry_box.pack(ipady=7)

        def check_password():
           if my_term.get() == 'Agree':
               my_term.set('')
               incorrect_term_label['text']=''
               controller.show_frame('PageOne')
           else:
               incorrect_term_label['text']='User has to Agree to move on.'
        
        getStarted_button = Button(self, text="Get Started!", command=check_password, highlightbackground='#e2c7d8', foreground="black", height=3)
        getStarted_button.pack()

        incorrect_term_label = tk.Label(self, text='', fg='white', bg='#95658B', anchor='n')
        incorrect_term_label.pack(fill='both',expand=True)
        
      

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#e2c7d8')
        self.controller = controller

        button_frame = tk.Frame(self, bg="#e2c7d8")
        button_frame.pack(fill='both')
        
        
        def identify():
            controller.show_frame('IdentifyPage')
        identify_button = tk.Button(button_frame, text='Identify', command=identify, highlightbackground="#e2c7d8", foreground="black")

            
        def map():
            controller.show_frame('MapPage')    
        map_button = tk.Button(button_frame, text='Map', command=map, highlightbackground="#e2c7d8", foreground="black")
            
        def catalog():
            controller.show_frame('CatalogPage')    
        catalog_button = tk.Button(button_frame, text='Catalog', command=catalog, highlightbackground="#e2c7d8", foreground="black")
        
        
        logo_photo = tk.PhotoImage(file='berrylogo.gif')
        logo_photo_label = tk.Label(button_frame,image=logo_photo, bg="#e2c7d8")
        logo_photo_label.grid(row=4, column=4, sticky=tk.W, padx=20, rowspan=2)
        logo_photo_label.image = logo_photo

        identify_button.grid(row=4, column=6, sticky=tk.N)
        map_button.grid(row=4, column=6, rowspan=2)
        catalog_button.grid(row=5, column=6, sticky=tk.S)

        button_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        


class IdentifyPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#e2c7d8")
        self.controller = controller
        
        
        label_frame = tk.Frame(self,bg="#95658B")
        label_frame.pack(fill='both',expand=True)
        
        #Put your code here with label_frame. Take test 1 out 
        test1 = tk.Label(
            label_frame, text="This is the identify page.")
        test1.grid(row=1, column=2, sticky=N)
        label_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)


        button_frame = tk.Frame(self, bg="#95658B")
        button_frame.pack(fill='both',expand=True)
        def back():
            controller.show_frame('PageOne')
        
        home_button = tk.Button(button_frame, text='Home', command=back, highlightbackground="#e2c7d8", foreground="black")
        
        button1 = Button(button_frame, text="Homepage", width=8,
                         highlightbackground="pink", foreground="black", command=back)
        home_button.grid(row=2, column=6, sticky=tk.S)
        button_frame.place(relx=1, rely=1, anchor=tk.SE)
        
class MapPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#e2c7d8")
        self.controller = controller
        
        label_frame = tk.Frame(self,bg="#95658B")
        label_frame.pack(fill='both',expand=True)
        
        #Put your code here with label_frame. Take test 1 out 
        test1 = tk.Label(
            label_frame, text="This is the Map page")
        test1.grid(row=1, column=2, sticky=N)
        label_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        button_frame = tk.Frame(self, bg="#95658B")
        button_frame.pack(fill='both',expand=True)
        def back():
            controller.show_frame('PageOne')
        
        home_button = tk.Button(button_frame, text='Home', command=back, highlightbackground="#e2c7d8", foreground="black")
        
        button1 = Button(button_frame, text="Homepage", width=8,
                         highlightbackground="pink", foreground="black", command=back)
        home_button.grid(row=2, column=6, sticky=tk.S)
        button_frame.place(relx=1, rely=1, anchor=tk.SE)
        
class CatalogPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#e2c7d8")
        self.controller = controller
  
        label_frame = tk.Frame(self,bg="#95658B")
        label_frame.pack(fill='both',expand=True)
        
        #Put your code here with label_frame. Take test 1 out 
        test1 = tk.Label(
            label_frame, text="This is the Catalog page")
        test1.grid(row=1, column=2, sticky=N)
        label_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        button_frame = tk.Frame(self, bg="#95658B")
        button_frame.pack(fill='both',expand=True)
        def back():
            controller.show_frame('PageOne')
        
        home_button = tk.Button(button_frame, text='Home', command=back, highlightbackground="#e2c7d8", foreground="black")
        
        button1 = Button(button_frame, text="Homepage", width=8,
                         highlightbackground="pink", foreground="black", command=back)
        home_button.grid(row=2, column=6, sticky=tk.S)
        button_frame.place(relx=1, rely=1, anchor=tk.SE)


if __name__ == "__main__":
    app = BerryApp()
    app.mainloop()