import pygame
import pygame_gui
from quantum.helpers import InputTextBox
from quantum import Particle, WaveFunction
import scipy as sci
import numpy as np
import pylab

h = sci.constants.h
h_bar = sci.constants.hbar

pygame.init()


def flux(x):
    return


def main():
    # setup
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1600, 900))
    running = True

    V_of_x_input = InputTextBox(75, 20, 140, 32, "V(x)")
    V_0_input = InputTextBox(75, 57, 140, 32, "V_0")
    a_input = InputTextBox(75, 94, 140, 32, "a")

    input_boxes = [V_of_x_input, V_0_input, a_input]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            for box in input_boxes:
                box.handle_event(event)
                # handle held key in case of backspace etc

            # animte circle here

        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        V_0 = V_0_input.text
        a = a_input.text

        pygame.draw.circle(screen, "blue", (700, 700), 25)

        pygame.draw.rect(screen, "red", (20, 670, 500, 200), border_radius=2)
        pygame.draw.rect(screen, "red", (1080, 670, 500, 200), border_radius=2)

        pygame.draw.lines(screen, "white", True, points=[(20, 870), (1580, 870)])
        pygame.draw.line(screen, "white", (1580, 870), (1570, 880))
        pygame.draw.line(screen, "white", (1580, 870), (1570, 860))

        pygame.draw.line(screen, "white", (20, 870), (30, 880))
        pygame.draw.line(screen, "white", (20, 870), (30, 860))

        pygame.draw.lines(screen, "white", True, points=[(800, 900), (800, 500)])
        pygame.draw.line(screen, "white", (800, 500), (790, 510))
        pygame.draw.line(screen, "white", (800, 500), (810, 510))



        pygame.display.flip()
        # fps limit
        clock.tick(60)


if __name__ == "__main__":
    #main()
    pygame.quit()
