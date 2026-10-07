import logging
import sys
import math

log_format = "%(asctime)s | [%(levelname)-7s] | %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

logging.basicConfig(
    level=logging.DEBUG,
    format=log_format,
    datefmt=date_format,
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("logs/file_txt.log", encoding="utf-8")
    ]
)


def get_triangle_type(a, b, c):

    if a + b <= c or a + c <= b or b + c <= a:
        return "не треугольник"

    # Проверка типа
    if a == b == c:
        return "равносторонний"
    elif a == b or b == c or a == c:
        return "равнобедренный"
    else:
        return "разносторонний"


def calculate_vertices(a, b, c):

    max_side = max(a, b, c)
    scale = 90.0 / max_side

    A = a * scale
    B = b * scale
    C = c * scale

    x1, y1 = 5, 95

    x2, y2 = int(x1 + A), int(y1)

    cos_angle = (A ** 2 + B ** 2 - C ** 2) / (2 * A * B)
    cos_angle = max(-1.0, min(1.0, cos_angle))

    x3 = x1 + B * cos_angle
    y3 = y1 - B * math.sqrt(1 - cos_angle ** 2)

    return [(int(x1), int(y1)), (int(x2), int(y2)), (int(x3), int(y3))]


def process_input(line1, line2, line3):

    try:
        a = float(line1)
        b = float(line2)
        c = float(line3)
    except (ValueError, TypeError):
        logging.warning("Нечисловые входные данные")
        return "", [(-2, -2), (-2, -2), (-2, -2)]

    if a <= 0 or b <= 0 or c <= 0:
        logging.warning("Отрицательные или нулевые значения")
        return "", [(-1, -1), (-1, -1), (-1, -1)]

    triangle_type = get_triangle_type(a, b, c)
    logging.info(f"Тип треугольника: {triangle_type}")

    if triangle_type == "не треугольник":
        return triangle_type, [(-1, -1), (-1, -1), (-1, -1)]

    vertices = calculate_vertices(a, b, c)
    logging.info(f"Координаты вершин: {vertices}")
    return triangle_type, vertices


def main():
    logging.info("Приложение запущено")
    line1 = input("Введите сторону A: ")
    line2 = input("Введите сторону B: ")
    line3 = input("Введите сторону C: ")

    triangle_type, vertices = process_input(line1, line2, line3)

    print("\n--- Результат ---")
    print(f"Тип треугольника: {triangle_type}")
    print(f"Координаты вершин: {vertices}")


if __name__ == "__main__":
    main()