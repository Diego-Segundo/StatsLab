import tkinter as tk
from tkinter import ttk
import pandas as pd
from sodapy import Socrata
import numpy as np
import cleaning_data_project as cd
from scipy import stats
from matplotlib import pyplot as plt
import seaborn as sns
from PIL import ImageTk, Image


val_list = ("Bottle_Cost","Bottle_Selling_Price",
            "Bottle_Quantity_Sold",
            "Profit",
            "Total_Profit",
            "Bottle_Category_Name",
            "County",
            "Client_Store_Address",
            "Zipcode")

category = ("Bottle_Category_Name",
            "County",
            "Client_Store_Address",
            "Zipcode")

LARGE_FONT= ("Verdana", 38)

#Cretes a container class called MainWindow

class StatApp(tk.Tk):
#This method initializes the main app class
    def __init__(self, *args, **kwargs):
        
        #This initializes the inherited class when the program opens
        tk.Tk.__init__(self, *args, **kwargs)
        
        #Creates a container frame
        window = tk.Frame(self)
        
        #Gives the location of the main frame
        window.grid(row=0,column=1)
    

        
        #Determines how thick the columns & rows will be and the minimum size of the frame 
        window.rowconfigure(0, minsize = 800, weight=1)
        window.columnconfigure(1,minsize = 800, weight=1)
    

     
        #Creates a dictionary where all the pages go in
        self.frames = {}
        
        for F in (MainMenu,FirstPage, SecondPage):

            frame = F(window, self)
            self.frames[F] = frame
            '''self.frames = {
            StartPage: StartPage(container, self),
            frame = F(parent=container, controller=self)
        }'''
            
        #Gives the frame displayed a location
            frame.grid(row=0, column=1, sticky ="nsew")
            frame.config(bg="#47B5FF")
            frame.rowconfigure(1,  weight=1)
            frame.rowconfigure(2,  weight=1)
            
          
            
         


        
        #shows the page by running a user def
        self.show_frame(MainMenu)

        
        
#This user-def raise to called page to the front
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
        


class MainMenu(tk.Frame):
    
    def __init__(self, parent, window):
        tk.Frame.__init__(self,parent)
        self.str_val = tk.StringVar(window) #Use stringvar to monitor values in combobox
        self.iowa_data = cd.clean_data() #define the cleaned and extrated data
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TButton', background = 'red', foreground = 'white', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
        style.map('TButton', background=[('active','#47B5FF')])

        self.lbl_intro = tk.Label(self, text="Welcome to the Stat Lab", font=LARGE_FONT, fg="white")
        self.lbl_intro.pack(pady =40)
        self.lbl_intro.configure(bg='#47B5FF')
       

        self.frame = tk.Frame(self)
        self.frame.pack()
        self.frame.configure(bg='#47B5FF')

       

        self.path = "flask.jpeg"

        self.img = ImageTk.PhotoImage(Image.open(self.path))

        
        self.label = tk.Label(self.frame, image = self.img)
        self.label.pack()
        self.label.configure(bg='#47B5FF')

        # Create a Label Widget to display the text or Image
        

       

        self.widgets = tk.Frame(self)
        self.widgets.pack(pady = 10)
        self.widgets.configure(bg='#47B5FF')
        
        self.bnt_page= ttk.Button(self.widgets,text="First Page",width = 10, command=lambda: window.show_frame(FirstPage))
        self.bnt_page.pack(pady =5)
        self.bnt_page2 = ttk.Button(self.widgets,text="Second page",width = 10, command=lambda: window.show_frame(SecondPage))
        self.bnt_page2.pack(pady=5)
        self.bnt_MainMenu = ttk.Button(self.widgets,text="Main Menu",width = 10, command=lambda: window.show_frame(MainMenu))
        self.bnt_MainMenu.pack(pady =5)












 #Here we create a page called StartPage       
class FirstPage(tk.Frame):
        #This initializes the program with the 3 instances that are going to be used.The parent refers to the main class statapp. The window to the main frame named window. 
    def __init__(self, parent, window):
        tk.Frame.__init__(self,parent)#This initializes two intances from the inhertited class called tk.Frame
        self.str_val = tk.StringVar(window) #Use stringvar to monitor values in combobox
        self.iowa_data = cd.clean_data() #define the cleaned and extrated data
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TButton', background = 'red', foreground = 'white', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
        style.map('TButton', background=[('active','#47B5FF')])
        descriptive = tk.Frame(self)
        descriptive.grid(row=2, column=7,sticky ="nsew")
        descriptive.config(bg="#47B5FF")
        # This creates an original label for this page
        self.label1 = tk.Label(self, text="Welcome to the Descriptive Statistic Module", font=LARGE_FONT, fg="white")
        self.label1.grid(row=0, column=7,sticky ="nsew",pady=40)
        self.label1.configure(bg='#47B5FF')
        #This creates a button to change pages
        self.bnt_page= ttk.Button(self,text="Second page",width = 10, command=lambda: window.show_frame(SecondPage))
        self.bnt_page.grid(row=3,column = 0, padx=5)
        self.bnt_page2 = ttk.Button(self,text="Second page",width = 10, command=lambda: window.show_frame(SecondPage))
        self.bnt_page2.grid(row=3, column =8, padx=5)
        self.bnt_MainMenu = ttk.Button(self,text="Main Menu",width = 10, command=lambda: window.show_frame(MainMenu))
        self.bnt_MainMenu.grid(row=4, column =7, padx=5)
        #This creates the combobox
        self.combobox = ttk.Combobox(self, textvariable = self.str_val, values=val_list, state="readonly")
        self.combobox.grid(row=1, column=7, pady=50)
        self.combobox.current(1)
        #This creates an empty label for the descriptive stat answers
        self.lbl_mean = tk.Label(descriptive, bg= "#47B5FF", fg = "white",text = "")
        self.lbl_mean.grid(row = 5, column = 2,padx=10, pady=10)
        self.lbl_median =tk.Label(descriptive, bg= "#47B5FF",fg = "white",text ="")
        self.lbl_median.grid(row =5, column = 3,padx=10, pady=10)
        self.lbl_mode =tk.Label(descriptive,bg= "#47B5FF", fg = "white",text ="")
        self.lbl_mode.grid(row =5, column = 4,padx=10, pady=10)
        self.lbl_skew =tk.Label(descriptive,bg= "#47B5FF", fg = "white",text ="")
        self.lbl_skew.grid(row =5, column = 5,padx=10, pady=10)
        self.lbl_corr=tk.Label(descriptive,bg= "#47B5FF", fg = "white",text ="")
        self.lbl_corr.grid(row =5, column = 5,padx=10, pady=10)
        
        
        #Thia creates the buttons for statistic functionality
        self.bnt_mean = ttk.Button(descriptive,text="Mean",command=lambda:self.mean())
        self.bnt_mean.grid(row = 3, column = 2,padx=5)
        self.bnt_median = ttk.Button(descriptive, text ="Median", command=lambda:self.median())
        self.bnt_median.grid(row = 3, column = 3,padx=5)
        self.bnt_mode = ttk.Button(descriptive, text ="Mode", command=lambda:self.mode())
        self.bnt_mode.grid(row = 3, column = 4,padx=5)
        self.bnt_desc = ttk.Button(descriptive, text ="Describe", command=lambda:self.desc())
        self.bnt_desc.grid(row = 3, column = 6)
        self.bnt_corr = ttk.Button(descriptive,text = "Correlation Matrix", command=lambda:self.corr())
        self.bnt_corr.grid(row=3, column = 7, padx=5)
        self.bnt_corr = ttk.Button(descriptive,text = "Skew", command=lambda:self.skew())
        self.bnt_corr.grid(row=3, column = 5, padx=5)

        

    def mean(self):
        result = self.str_val
        save=result.get()
        try:
            if "zipcode" not in save:
                column_mean= round(self.iowa_data[save].mean(),0)
                self.lbl_mean.config(text= "Mean:" + str(column_mean))
            elif "zipcode" in save:
                column_mean = "can't find a zipcode's mean"
                self.lbl_mean.config(text=str(column_mean))
        except ValueError:
           column_mean="There is a string or incorrect data type in your column"
           self.lbl_mean.config(text=str(column_mean))
        except TypeError:
           column_mean="The column is not a number"
           self.lbl_mean.config(text=str(column_mean))
        except save=="zipcode":
            column_mean="Please choose another column"
            self.lbl_mean.config(text=str(column_mean))


    def median(self):
        result = self.str_val
        save=result.get()
        try:
            if "zipcode" not in save:
                column_mean= round(self.iowa_data[save].median(),0)
                self.lbl_median.config(text= "Median: " + str(column_mean))
            elif "zipcode" in save:
                column_mean = "can't find a zipcode's mean"
                self.lbl_median.config(text=str(column_mean))
        except ValueError:
           column_mean="There is a string or incorrect data type in your column"
           self.lbl_median.config(text=str(column_mean))
        except TypeError:
           column_mean="The column is not a number"
           self.lbl_median.config(text=str(column_mean))
        except save=="zipcode":
            column_mean="Please choose another column"
            self.lbl_median.config(text=str(column_mean))

    def mode(self):
      result = self.str_val.get()
      try:
          column_mean= round(self.iowa_data[result].mode(result),0)
          self.lbl_mode.config(text="Mode: " + str(column_mean))
      except TypeError:
          column_mean= self.iowa_data[result].mode(result)
          self.lbl_mode.config(text="Mode: " + str(column_mean))
     

    def desc(self):
      result = self.str_val.get()
      topw=tk.Toplevel()
     
      try:
            if "zipcode" not in result:
                column_mean= round(self.iowa_data[result].describe(),0)
                toplbl = tk.Label(topw, text=str(column_mean)).pack()
                
            elif "zipcode" in result:
                column_mean = "can't find a zipcode's mean"
                toplbl = tk.Label(topw, text = str(column_mean)).pack()

      except ValueError:
            column_mean="There is a string or incorrect data type in your column"
            toplbl = tk.Label(topw, text = str(column_mean)).pack()
      except TypeError:
            column_mean="The column is not a number"
            toplbl = tk.Label(topw, text = str(column_mean)).pack()
      except result=="zipcode":
            column_mean="Please choose another column"
            toplbl = tk.Label(topw, text = str(column_mean)).pack()


            
    def corr(self):
        topw = tk.Toplevel()
        dataset_corr = self.iowa_data.corr()
        toplbl = tk.Label(topw, text = dataset_corr).pack()
        
            
            

    def skew(self):
        result = self.str_val.get()
       
        try:
            if "zipcode" not in result:
                column_skew = round(self.iowa_data[result].skew(),0)
                self.lbl_skew.config(text = "Skew: " + str(column_skew))
                                  
            elif "zipcode" in result:
                column_skew = "can't find a zipcode's mean"
                self.lbl_skew.config(text = column_skew)

        except ValueError:
            column_skew="There is a string or incorrect data type in your column"
            self.lbl_skew.config(text = column_skew)
        except TypeError:
            column_skew="The column is not a number"
            self.lbl_skew.config(text = column_skew)
        except result=="zipcode":
            column_skew="Please choose another column"
            self.lbl_skew.config(text = column_skew)



    
            
      
        
        
        
        




                


class SecondPage(tk.Frame):
    
    #This line starts the second page
    def __init__(self, parent,window):
        tk.Frame.__init__(self,parent)
        self.str_val = tk.StringVar(window)
        self.str_val2 = tk.StringVar(window)
        self.iowa_data = cd.clean_data()
        #Here we create a new frame where all the button and label will sit on
        self.inferential = tk.Frame(self)
        self.inferential.grid(row=2, column = 7, sticky = "nsew", pady=100)
        self.inferential.config(bg="#47B5FF")
        

        
        self.combobox1 = tk.Frame(self)
        self.combobox1.place(x=473,y=290)
        self.combobox1.config(bg="#47B5FF")

        

        #These lines of code include the labels for the page and answers
        self.lbl1 = tk.Label(self, text="Welcome to the Inferential Statistics Module", font=LARGE_FONT)
        self.lbl1.grid(row=0, column=7, pady=40)
        self.lbl1.configure(bg="#47B5FF", fg ="white")
        self.lbldist = tk.Label(self.inferential, text="", fg = "white")
        self.lbldist.grid(row= 4, column = 2)
        self.lbldist.configure(bg="#47B5FF")
        self.lblbar = tk.Label(self.inferential, text="", fg = "white")
        self.lblbar.grid(row= 4, column = 3)
        self.lblbar.configure(bg="#47B5FF")
        self.lblheatmap = tk.Label(self.inferential, text ="", fg = "white")
        self.lblheatmap.grid(row = 4, column = 4)
        self.lblheatmap.configure(bg = "#47B5FF")
        self.lblscat = tk.Label(self.inferential, text="", fg = "white")
        self.lblscat.grid(row= 4, column = 5)
        self.lblscat.config(bg="#47B5FF")
        self.lblregplot = tk.Label(self.inferential, text="", fg ="white")
        self.lblregplot.grid(row = 4, column = 6)
        self.lblregplot.configure(bg = "#47B5FF")
        
        
        
        self.bnt1 = ttk.Button(self,text="First Page", width = 10,command=lambda: window.show_frame(FirstPage))
        self.bnt1.grid(row=3,column=8, padx = 5)
        self.bnt2 = ttk.Button(self,text="First Page",width = 10, command=lambda: window.show_frame(FirstPage))
        self.bnt2.grid(row=3,column=0, padx =5)
        self.bnt_MainMenu = ttk.Button(self,text="Main Menu",width = 10, command=lambda: window.show_frame(MainMenu))
        self.bnt_MainMenu.grid(row=4, column =7, padx=5)

        #Here we add a combobox with the dataframe columns
        self.combobox = ttk.Combobox(self.combobox1, textvariable = self.str_val, values=val_list, state="readonly")
        self.combobox.grid(row=1, column = 6)
        self.combobox.current(1)
        
        #This line creates a second combobox 
        self.combobox = ttk.Combobox(self.combobox1, textvariable = self.str_val2, values=val_list, state="readonly")
        self.combobox.grid(row=1, column = 7, padx = 10)
        self.combobox.current(1)

        #These line screate various buttons for the user to interact and preform inferential analysis
        self.bnt_mean = ttk.Button(self.inferential,text="Distribution",command=lambda:self.distribution())
        self.bnt_mean.grid(row = 3, column = 2,padx=5)
        self.bnt_median = ttk.Button(self.inferential, text ="Bar Graph", command=lambda:self.BarGraph())
        self.bnt_median.grid(row = 3, column = 3,padx=5)
        self.bnt_mode = ttk.Button(self.inferential, text ="Heat Map", command=lambda:self.heatmap())
        self.bnt_mode.grid(row = 3, column = 4,padx=5)
        self.bnt_corr = ttk.Button(self.inferential,text = "Scatter Plot", command=lambda:self.scatter())
        self.bnt_corr.grid(row=3, column = 5, padx=5)
        self.bnt_desc = ttk.Button(self.inferential, text ="Regression Plot", command=lambda:self.regplot())
        self.bnt_desc.grid(row = 3, column = 6)
        self.bnt_corr = ttk.Button(self.inferential,text = "GridFace (not working)", command=lambda:self.corr())
        self.bnt_corr.grid(row=3, column = 7, padx=5)

    def distribution(self):
        column = self.str_val.get()  
        

        try:
            if  column not in category:
                fig = plt.figure()
                plt.hist(round(self.iowa_data[column], 0))
                plt.xlabel(column)
                plt.ylabel("Frequency")
                plt.show()
                plt.clf()
            elif column in catogory:
                content = "Do not use distribution with zipcode"
                self.lbldist.configure(text = str(content))
                
                
            
        except:
            content = "Only use numeric columns"
            self.lbldist.configure(text = str(content))


    
    


    def BarGraph(self):
        column = self.str_val.get()
       
        
    
      
        
        try:
            if column not in category:
                    fig = plt.figure
                    ax = sns.countplot(x=column, data = round(self.iowa_data, 0))
                    sns.set(font_scale = 2)
                    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
                    plt.title(f"Scatter plot of {column}")
                    plt.show()
                    plt.clf()
            elif column in  category:
                    fig = plt.figure
                    ax = sns.countplot(x=column, data = self.iowa_data)
                    sns.set(font_scale = 2)
                    ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
                    plt.title(f"Scatter plot of {column}")
                    plt.show()
                    plt.clf()
     
        except:
            content = "Only use numeric columns"
            self.lblbar.configure(text = str(content))


    def scatter(self):
        column1 = self.str_val.get() 
        column2 = self.str_val2.get()
        
        try:
            if column1 not in category and column2 not in category:
                fig = plt.figure()
                column1_series = round(self.iowa_data[column1], 0)
                column2_series = round(self.iowa_data[column2],0)
                ax=plt.plot(column1_series,column2_series, marker =".", linestyle = "none")
                plt.title(f"Scatter plot of {column1} and {column2}")
                plt.xlabel(column1)
                plt.ylabel(column2)
                plt.show()
                plt.clf()

            elif column1 in category and column2 in category:
                content = "Do not use categorical variables"
                self.lblscat.config(text= str(content))
                


            
        except:
            content = "Only use numeric columns"
            self.lblscat.configure(text = str(content))



    def heatmap(self):
        column1 = self.str_val.get() 
        column2 = self.str_val2.get()
        
        try:
            if column1 not in category and column2 not in category:
                heatmap_freq = pd.crosstab(round(self.iowa_data[column1],0),\
                           round(self.iowa_data[column2], 0) )
                ax = sns.heatmap(heatmap_freq, annot = True, fmt = "d", cmap = "YlOrRd")
                fig = plt.figure()
                plt.title(f"Scatter plot of {column1} and {column2}")
                plt.show()
                plt.clf()
            elif column1 in category or column2 in category:
                heatmap_freq = pd.crosstab(self.iowa_data[column1],\
                           self.iowa_data[column2] )
                ax = sns.heatmap(heatmap_freq, annot = True, fmt = "d", cmap = "YlOrRd")
                fig = plt.figure()
                plt.title(f"Scatter plot of {column1} and {column2}")
                plt.show()
                plt.clf()
     
        except:
            content = "Only use numeric columns"
            self.lblheatmap.configure(text = str(content))
            

    def regplot(self):
        column1 = self.str_val.get() 
        column2 = self.str_val2.get()
        
        try:
            if column1 not in category and column2 not in category:
                ax = sns.regplot(x = round(self.iowa_data[column1],0), y = round(self.iowa_data[column2],0))
                plt.title(f"Scatter plot of {column1} and {column2}")
                plt.show()
                plt.clf()
            elif column1 in category and column2 in category:
                content = "Only numeric columns for linear regressions"
                self.lblregplot.config(text= str(content))

            
        except:
            content = "Only use numeric columns"
            self.lblregplot.configure(text = str(content))


    
                
               
        

        




app = StatApp()
app.title("StatLab")
app.configure(bg="#47B5FF")
app.rowconfigure(0, minsize = 800, weight=1)
app.columnconfigure(1, minsize = 800, weight=1)
app.columnconfigure(7, minsize = 10, weight=1)
app.mainloop()
