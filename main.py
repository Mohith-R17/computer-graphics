import glfw
from OpenGL.GL import *
import random


def main():
    if not glfw.init():
        return

    window = glfw.create_window(800, 600, "OpenGL Window", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    last_change = 0
    r, g, b = 0, 0, 0

    while not glfw.window_should_close(window):
        current = glfw.get_time()

        if current - last_change >= 1:
            r = random.random()
            g = random.random()
            b = random.random()
            last_change = current

        glClearColor(r, g, b, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glfw.swap_buffers(window)
        glfw.poll_events()

    glfw.terminate()


    main()