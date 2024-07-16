from tkinter import Tk, BOTH, Canvas

class Window():
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.__root = Tk()
		self.__root.title("Maze Solver")
		self.canvas = Canvas(self.__root, {"bg": "white"})
		self.canvas.pack(fill=BOTH, width=self.width, height=self.height, expand=1)
		self.is_running = False
		self.__root.protocol("WM_DELETE_WINDOW", self.close)

	def redraw(self):
		self.root.update_idletasks()
		self.root.update()

	def wait_for_close(self):
		self.is_running = True
		while self.is_running:
			self.redraw()	
	
	def close(self):
		self.is_running = False

