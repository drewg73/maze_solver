from graphics import Window
from maze import Maze

def main():
    win = Window((100 + 50 * 10), (100 + 50 * 10))
    m1 = Maze(50, 50, 10, 10, 50, 50, win, 10093409)
    m1.solve()
    win.wait_for_close()

if __name__ == "__main__":
    main()
