import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    # Словник для підрахунку кількостей сум
    sum_counts = {i: 0 for i in range(2, 13)}
    # Імітація кидків кубиків
    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        sum_counts[total] += 1

    return sum_counts


def calculate_probabilities(sum_counts, num_rolls):
    probabilities = {sum_value: (
        count / num_rolls) * 100 for sum_value, count in sum_counts.items()}

    return probabilities


def printing_tables(table1, table2):
    print("|Сума|", "Імовірність1|", "Імовірність2|")
    for key, value in table2.items():
        print(f"|  {key}|     {table1[key]}%|      {value:.2f}%|")


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs)
    plt.xlabel('Суми (2-12)')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність сум при кидках двох кубиків')
    plt.xticks(sums)
    plt.ylim(0, max(probs) + 0.05)  # Невелике відступлення зверху
    plt.grid(axis='y')
    plt.show()


# аналітичні розрахунки
analitic_calculation = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78,

}

# Кількість кидків
num_rolls = 100000

# Виконати симуляцію
sum_counts = simulate_dice_rolls(num_rolls)

# Обчислити ймовірності
probabilities = calculate_probabilities(sum_counts, num_rolls)

# Раздракувати обидві таблиці
printing_tables(analitic_calculation, probabilities)

# Побудувати графік
plot_probabilities(probabilities)
