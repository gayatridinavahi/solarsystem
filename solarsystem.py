import math
import time
from tkinter import *

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 1000

def main():
    root = Tk()
    canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()
    canvas.create_rectangle(0, 0, CANVAS_WIDTH, CANVAS_HEIGHT, fill="black")  # Set the canvas background color to black

    # Set up the sun
    sun_radius = 40
    sun_x, sun_y = CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2
    sun = canvas.create_oval(
        sun_x - sun_radius,
        sun_y - sun_radius,
        sun_x + sun_radius,
        sun_y + sun_radius,
        fill="yellow"
    )
    sun_label = canvas.create_text(sun_x, sun_y, text="Sun", fill="white", font="Arial 12 bold")

    # Set up the planets
    planet_radius = [10, 15, 18, 20, 25, 28, 30, 35]  # Radius of planets in pixels
    planet_distance = [100, 150, 200, 250, 300, 350, 400, 450]  # Distance from the sun in pixels
    planet_speed = [0.04, 0.03, 0.02, 0.015, 0.01, 0.008, 0.006, 0.004]  # Angular speed of planets in radians
    planet_colors = ["blue", "red", "green", "orange", "purple", "brown", "pink", "gray"]
    planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    planets = []
    planet_labels = []
    angles = [0] * len(planet_radius)  # Initial angles for each planet
    for i in range(len(planet_radius)):
        x = sun_x + planet_distance[i] * math.cos(angles[i])
        y = sun_y + planet_distance[i] * math.sin(angles[i])
        planet = canvas.create_oval(
            x - planet_radius[i],
            y - planet_radius[i],
            x + planet_radius[i],
            y + planet_radius[i],
            fill=planet_colors[i]
        )
        label = canvas.create_text(x, y, text=planet_names[i], fill="white", font="Arial 10 bold")
        planets.append(planet)
        planet_labels.append(label)

    # Animation loop
    while True:
        for i in range(len(planets)):
            angles[i] += planet_speed[i]  # Update angle for continuous motion
            x = sun_x + planet_distance[i] * math.cos(angles[i])
            y = sun_y + planet_distance[i] * math.sin(angles[i])
            dx = x - canvas.coords(planets[i])[0]
            dy = y - canvas.coords(planets[i])[1]
            canvas.move(planets[i], dx, dy)
            canvas.move(planet_labels[i], dx, dy)

        root.update()
        time.sleep(0.03)  # Delay between frames (in seconds)
    else:
        mainloop()

if __name__ == '__main__':
    main()
