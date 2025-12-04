import numpy as np
import matplotlib.pyplot as plt

A1 = np.array([[-1.023, -0.612], [1.184, -0.756]])
b1 = np.array([4.675, 32.544])

A2 = np.array([[0.886, 1.280], [0.068, -0.728]])
b2 = np.array([40.318, 47.451])

A3 = np.array([[-0.546, 0.100], [1.180, -0.724]])
b3 = np.array([-46.077, -64.406])

maps = [(A1, b1), (A2, b2), (A3, b3)]

def generate_attractor(n_points=500_000, discard=5000):
    x = np.zeros(2)
    points = []

    for i in range(n_points + discard):
        A, b = maps[np.random.randint(0, 3)]
        x = A @ x + b
        if i >= discard:
            # снимаем жёсткий фильтр, просто добавляем точки
            points.append(x.copy())

    points = np.array(points)
    if points.ndim != 2:
        raise ValueError("Массив points пустой или имеет неверную форму")
    return points

points = generate_attractor()

# центрирование и масштабирование
points -= points.mean(axis=0)
points *= 0.01

plt.figure(figsize=(10,10))
plt.scatter(points[:,0], points[:,1], s=0.1, color='black', marker='.')
plt.axis('equal')
plt.axis('off')
plt.show()
