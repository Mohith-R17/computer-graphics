import glfw
from OpenGL.GL import *


WIDTH = 800
HEIGHT = 600


def draw_pixel(x, y):
    glBegin(GL_POINTS)
    glVertex2i(x, y)
    glEnd()


def plot_circle_points(xc, yc, x, y):
    points = [
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
        (xc + y, yc + x),
        (xc - y, yc + x),
        (xc + y, yc - x),
        (xc - y, yc - x)
    ]

    for px, py in points:
        draw_pixel(px, py)


def midpoint_circle(xc, yc, r):

    x = 0
    y = r

    p = 1 - r

    while x <= y:

        plot_circle_points(xc, yc, x, y)

        if p < 0:
            p = p + 2 * x + 3
        else:
            p = p + 2 * (x - y) + 5
            y -= 1

        x += 1


def main():

    if not glfw.init():
        print("Failed to initialize GLFW")
        return

    window = glfw.create_window(
        WIDTH,
        HEIGHT,
        "Midpoint Circle Drawing Algorithm",
        None,
        None
    )

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glOrtho(
        0,
        WIDTH,
        0,
        HEIGHT,
        -1,
        1
    )

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glPointSize(3)

    while not glfw.window_should_close(window):

        glClearColor(0, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT)

        glColor3f(0, 1, 0)

        midpoint_circle(400, 300, 150)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()