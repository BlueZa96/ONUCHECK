def merge_onu_data_and_stats(data_list, stats_list):
    # Создаем словари с нормализованными ключами
    data_dict = {
        entry["IntfName"].lower(): entry
        for entry in data_list if "IntfName" in entry
    }
    stats_dict = {
        stat["IntfName"].lower(): stat
        for stat in stats_list if "IntfName" in stat
    }

    # Собираем все возможные поля
    data_fields = set()
    for entry in data_list:
        data_fields.update(entry.keys())

    stats_fields = set()
    for stat in stats_list:
        stats_fields.update(stat.keys())

    data_fields.discard("IntfName")
    stats_fields.discard("IntfName")

    all_intfs = set(data_dict.keys()) | set(stats_dict.keys())

    merged = []
    for intf in all_intfs:
        data_entry = data_dict.get(intf, {})
        stats_entry = stats_dict.get(intf, {})

        original_intf = data_entry.get("IntfName") or stats_entry.get("IntfName") or intf

        merged_entry = {"IntfName": original_intf}

        # Добавляем все поля из data
        for field in data_fields:
            merged_entry[field] = data_entry.get(field)

        # Добавляем все поля из stats
        for field in stats_fields:
            merged_entry[field] = stats_entry.get(field)

        # Фильтрация: если все значения (кроме IntfName) пустые или "--" — пропускаем
        non_empty_values = [
            v for k, v in merged_entry.items()
            if k != "IntfName" and v not in (None, "", "--")
        ]
        if non_empty_values:
            merged.append(merged_entry)

    return merged
