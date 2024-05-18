import heapq

def min_cost_to_connect_cables(cables):
    # Створюємо мін-кучу з початкових довжин кабелів
    heapq.heapify(cables)
    print(cables)
    
    total_cost = 0
    
    # Поки у купі більше одного елементу
    while len(cables) > 1:
        # Виймаємо два найменші елементи
        first_min = heapq.heappop(cables)
        second_min = heapq.heappop(cables)
        
        # Вартість їх об'єднання
        cost = first_min + second_min
        
        # Додаємо вартість до загальної вартості
        total_cost += cost
        
        # Поміщаємо назад у купу новий кабель, який утворився після об'єднання
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print("Мінімальні витрати на з'єднання кабелів:", min_cost_to_connect_cables(cables))
