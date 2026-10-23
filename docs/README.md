# 📐 Документация к библиотеке geometric_lib

> **Общее описание решения**
> Библиотека `geometric_lib` представляет собой скрипты для вычесления площадей  и периметров фигур.

---

## ⚙️ Описание функций с примерами вызова

### 🔵 Модуль `circle.py`

*   **`area(r)`**: Возвращает площадь круга радиусом `r`.
*   **`perimeter(r)`**: Возвращает длину окружности радиусом `r`.

```python
import circle

print(circle.area(5))       # Результат: 78.53981633974483
print(circle.perimeter(5))  # Результат: 31.41592653589793
```

### 🟩 Модуль `rectangle.py`

*   **`area(a, b)`**: Возвращает площадь прямоугольника со сторонами `a` и `b`.
*   **`perimeter(a, b)`**: Возвращает периметр прямоугольника со сторонами `a` и `b`.

```python
import rectangle

print(rectangle.area(4, 5))      # Результат: 20
print(rectangle.perimeter(4, 5)) # Результат: 18
```

### 🔲 Модуль `square.py`

*   **`area(a)`**: Возвращает площадь квадрата со стороной `a`.
*   **`perimeter(a)`**: Возвращает периметр квадрата со стороной `a`.

```python
import square

print(square.area(5))      # Результат: 25
print(square.perimeter(5)) # Результат: 20
```

### 🔺 Модуль `triangle.py`

*   **`area(a, h)`**: Возвращает площадь треугольника со стороной `a` и высотой `h`.
*   **`perimeter(a, b, c)`**: Возвращает периметр треугольника со сторонами `a`, `b` и `c`.

```python
import triangle

print(triangle.area(4, 5))         # Результат: 10.0
print(triangle.perimeter(3, 4, 5)) # Результат: 12
```

---

## 📜 История изменения проекта

В таблице ниже представлены хеши коммитов и их описания (кроме последней записи):

| Hash коммита | Описание изменений |
| :--- | :--- |
| `1d9917` | add dock for code |
| `7be7a0` | lalala |
| `d4d911` | fix the error in rectangle.py |
| `f93997` | create file rectangle.py |
| `cf5b2f` | create file rectangle.py |
| `d078c8d`| L-03: Docs added |
| `8ba9aeb`| L-03: Circle and square added |
