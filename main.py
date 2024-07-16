from graphics import *

def main():
	win = Window(800, 600)
	red_line = Line(Point(50, 50), Point(100, 50))
	blue_line = Line(Point(100, 50), Point(100, 200))
	win.draw_line(red_line, "red")
	win.draw_line(blue_line, "blue")
	win.wait_for_close()

if __name__ == "__main__":
	main()