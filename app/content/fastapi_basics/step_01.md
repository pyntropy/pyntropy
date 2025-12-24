## Блок кода

```python
def factorial(n: int) -> int:
    """Вычисляет факториал числа"""
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

# Пример использования
result = factorial(5)
Тест   `print(f"Факториал 5 равен {result}")`

<definition>
Этот тег используется для выделения определений, важных заметок или пояснений в тексте.
</definition>