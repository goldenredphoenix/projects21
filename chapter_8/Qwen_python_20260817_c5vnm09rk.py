def get_list_timestamps_for_schedule(start_hour=8, start_minute=0, end_hour=13, end_minute=30, step_minutes=30):
    """
    Формирует список временных слотов в формате 'ЧЧ:ММ'
    
    Параметры:
    - start_hour, start_minute: начало (по умолчанию 08:00)
    - end_hour, end_minute: конец (по умолчанию 13:30)
    - step_minutes: шаг в минутах (по умолчанию 30)
    """
    result = []
    
    # Переводим всё в минуты от начала суток
    current_minutes = start_hour * 60 + start_minute
    end_minutes = end_hour * 60 + end_minute
    
    # Генерируем слоты
    while current_minutes <= end_minutes:
        # Считаем часы и минуты
        hours = current_minutes // 60
        minutes = current_minutes % 60
        
        # Формируем строку в формате 'ЧЧ:ММ' (с ведущими нулями)
        time_string = f"{hours:02d}:{minutes:02d}"
        result.append(time_string)
        
        # Переходим к следующему слоту
        current_minutes += step_minutes
    
    return result

# Пример использования
print(get_list_timestamps_for_schedule())
# Вывод: ['08:00', '08:30', '09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30']