import tkinter as tk

def submit():
	print ("SUBMIT")
	lists.append(slide1.get())
	listm.append(slide2.get())
	listl.append(slide3.get())

	print(lists)
	print(listm)
	print(listl)
lists = []
listm = []
listl = []


root = tk.Tk()
root.title("GUI Slider")

lab1 = tk.Label(root, text = "Eating Tacker")
lab1.grid(row = 0, column = 0, columnspan = 2)
labS = tk.Label(root, text = "Small")
labS.grid(row = 2, column = 0, columnspan = 2)
slide1 = tk.Scale(root, from_=0, to=10, resolution=1, orient=tk.HORIZONTAL)
slide1.grid(row = 3, column = 0, columnspan = 2)

labM = tk.Label(root, text = "Medium")
labM.grid(row = 4, column = 0, columnspan = 2)
slide2 = tk.Scale(root, from_=0, to=10, resolution=1, orient=tk.HORIZONTAL)
slide2.grid(row = 5, column = 0, columnspan = 2)

labL = tk.Label(root, text = "Large")
labL.grid(row = 6, column = 0, columnspan = 2)
slide3 = tk.Scale(root, from_=0, to=10, resolution=1, orient=tk.HORIZONTAL)
slide3.grid(row = 7, column = 0, columnspan = 2)


btn1 = tk.Button(root, text="Submit",command = submit)
btn1.grid(row = 8, column = 0, columnspan = 2)

#create text area down belwo for display

text1 = tk.Text(root, height = 7, width = 30, background = "grey")
text1.grid(row = 10, column = 0, columnspan = 2)
text1.config(state="normal")
text1.insert(tk.INSERT,"Food you ate today: \n")
text1.insert(tk.INSERT,"Improvments to your diet: ")

root.mainloop() 

