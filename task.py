import heapq


def min_cost_to_connect_cables(cable_lengths):
    if len(cable_lengths) <= 1:
        return 0

    # Мінімальна купа з довжин кабелів
    heapq.heapify(cable_lengths)

    total_cost = 0

    while len(cable_lengths) > 1:

        # Витягаємо два найкоротші кабелі
        first_shortest = heapq.heappop(cable_lengths)
        second_shortest = heapq.heappop(cable_lengths)

        # З'єднуємо найкоротші кабелі
        cost = first_shortest + second_shortest
        total_cost += cost

        # Додаємо об'єднаний кабель назад у купу
        heapq.heappush(cable_lengths, cost)

    return total_cost


# Тест
cable_lengths = [8, 4, 6, 13, 2]
print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cable_lengths))
