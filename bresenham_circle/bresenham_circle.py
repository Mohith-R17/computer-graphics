import glfw
from OpenGL.GL import *

WIDTH, HEIGHT = 800, 600


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
        (xc - y, yc - x),
    ]

    for px, py in points:
        draw_pixel(px, py)


def bresenham_circle(xc, yc, r):
    x = 0
    y = r
    d = 3 - 2 * r

    while x <= y:
        plot_circle_points(xc, yc, x, y)

        if d < 0:
            d = d + 4 * x + 6
        else:
            d = d + 4 * (x - y) + 10
            y -= 1

        x += 1


def main():
    if not glfw.init():
        return

    window = glfw.create_window(WIDTH, HEIGHT, "Bresenham Circle", None, None)

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

        glColor3f(0, 1, 0)

        bresenham_circle(400, 300, 150)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()