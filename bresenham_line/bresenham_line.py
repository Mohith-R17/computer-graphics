import glfw
from OpenGL.GL import *

WIDTH, HEIGHT = 800, 600


def draw_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()


def bresenham_line(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    err = dx - dy

    while True:
        draw_pixel(x1, y1)

        if x1 == x2 and y1 == y2:
            break

        e2 = 2 * err

        if e2 > -dy:
            err -= dy
            x1 += sx

        if e2 < dx:
            err += dx
            y1 += sy


def main():
    if not glfw.init():
        return

    window = glfw.create_window(WIDTH, HEIGHT, "Bresenham Line", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WIDTH, 0, HEIGHT, -1, 1)

    glPointSize(3)

    while not glfw.window_should_close(window):
        glClearColor(0, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT)

        glColor3f(1, 0, 0)

        bresenham_line(100, 100, 700, 500)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()