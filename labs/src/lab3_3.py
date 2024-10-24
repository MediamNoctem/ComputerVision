import numpy as np
from matplotlib import pyplot as plt


class Points:
    def __init__(self):
        self.points = []

    def add_point(self, r, c):
        self.points.append([r, c])

    def get_centroid(self):
        if len(self.points) == 0:
            return None, None

        r_sum = sum([p[0] for p in self.points])
        c_sum = sum([p[1] for p in self.points])
        centroid_r = r_sum / len(self.points)
        centroid_c = c_sum / len(self.points)

        return centroid_r, centroid_c

    def get_central_moments(self):
        """
        - mrr: Момент относительно оси r.
        - mcc: Момент относительно оси c.
        - mrc: Момент относительно r и c.
        """
        centroid_r, centroid_c = self.get_centroid()

        mrr = 0
        mcc = 0
        mrc = 0
        for r, c in self.points:
            mrr += (r - centroid_r) ** 2
            mcc += (c - centroid_c) ** 2
            mrc += (r - centroid_r) * (c - centroid_c)

        return {
            "mrr": mrr / len(self.points),
            "mcc": mcc / len(self.points),
            "mrc": mrc / len(self.points)
        }

    def get_bounding_box(self):
        if len(self.points) == 0:
            return None, None, None, None

        r_min = min([p[0] for p in self.points])
        r_max = max([p[0] for p in self.points])
        c_min = min([p[1] for p in self.points])
        c_max = max([p[1] for p in self.points])

        return r_min, r_max, c_min, c_max

    def get_principal_axes(self):
        """
        - angle: Угол поворота главной оси (в радианах).
        - mrr: Момент второго порядка относительно главной оси r.
        - mcc: Момент второго порядка относительно главной оси c.
        """
        moments = self.get_central_moments()

        angle = 0.5 * np.arctan2(2 * moments["mrc"], moments["mrr"] - moments["mcc"])

        mrr = moments["mrr"] * np.cos(angle) ** 2 + 2 * moments["mrc"] * np.sin(angle) * np.cos(angle) + moments[
            "mcc"] * np.sin(angle) ** 2
        mcc = moments["mrr"] * np.sin(angle) ** 2 - 2 * moments["mrc"] * np.sin(angle) * np.cos(angle) + moments[
            "mcc"] * np.cos(angle) ** 2

        return {
            "angle": angle,
            "mrr": mrr,
            "mcc": mcc
        }


points = Points()

points.add_point(1, 2)
points.add_point(3, 4)
points.add_point(5, 6)

print("Точки в формате [y, x]:")

for i in range(len(points.points)):
    print(points.points[i])

centroid_r, centroid_c = points.get_centroid()
print(f"Центр тяжести: ({centroid_r}, {centroid_c})")

moments = points.get_central_moments()
print("Центральные моменты второго порядка:")
for key, value in moments.items():
    print(f"{key}: {value}")

r_min, r_max, c_min, c_max = points.get_bounding_box()
print(f"Описывающий прямоугольник: (({r_max}, {c_min}), ({r_min}, {c_max}))")

axes = points.get_principal_axes()
print("Главные оси:")
print(f"Угол в градусах: {(axes['angle'] * 180) / 3.1415}")
print(f"Момент второго порядка относительно r: {axes['mrr']}")
print(f"Момент второго порядка относительно c: {axes['mcc']}")

x = [points.points[i][1] for i in range(len(points.points))]
y = [points.points[i][0] for i in range(len(points.points))]

if axes['angle'] < 90:
    x2 = c_max
    y2 = 0 + (x2 - 0) * np.tan(axes['angle'])
elif axes['angle'] > 90:
    y2 = r_max
    x2 = 0 + (y2 - 0) / np.tan(axes['angle'])
else:
    x2 = 0
    y2 = r_max

fig, ax = plt.subplots()
ax.set_xlim(0, c_max + 1)
ax.set_ylim(0, r_max + 1)
plt.plot(x, y, 'ro', label='Точки')
ax.plot([0, x2], [0, y2], 'black', linestyle='--', label='Главная ось')
rect = plt.Rectangle((c_min, r_max), c_max - c_min, r_min - r_max, fill=False, color='blue', label='Описывающий прямоугольник')
ax.add_patch(rect)
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()
