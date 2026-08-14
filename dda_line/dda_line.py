import glfw
from OpenGL.GL import *

WIDTH = 800
HEIGHT = 600


def draw_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2i(round(x), round(y))
    glEnd()


def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    x_increment = dx / steps
    y_increment = dy / steps

    x = x1
    y = y1

    for _ in range(steps + 1):
        draw_pixel(x, y)

        x += x_increment
        y += y_increment


def main():
    if not glfw.init():
        print("Failed to initialize GLFW")
        return

    window = glfw.create_window(
        WIDTH,
        HEIGHT,
        "DDA Line Drawing Algorithm",
        None,
        None
    )

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, WIDTH, 0, HEIGHT, -1, 1)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glPointSize(3)

    while not glfw.window_should_close(window):

        glClearColor(0, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT)

        glColor3f(0, 1, 0)

        dda_line(100, 100, 700, 500)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()