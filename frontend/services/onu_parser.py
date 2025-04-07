from ..utils.onu_regex import match_onu_line_by_regex_template, is_start_of_onu_entry

def split_onu_entries(raw_text):
    """Разделяет сырые строки в структурированные записи ONU"""
    entries = []
    prev_line = ""
    waiting_for_check = False  #Флаг, указывает закончена ли строка, или она еще продолжится.

    lines = raw_text.strip().splitlines()

    for line in lines:
        if is_start_of_onu_entry(line):
            if waiting_for_check:
                entries.append(prev_line) #Целая строка после проверки предедущей

            prev_line = line
            waiting_for_check = True
        else:
            prev_line += line
            entries.append(prev_line) #Соедененная строка если предедущая была повреждена
            prev_line = ""
            waiting_for_check = False

    if waiting_for_check and prev_line:
        entries.append(prev_line) #Последняя строка если она оказалась целой

    return entries


def parse_onu_entries(entries, regex_template):
    """Парсит список строковых записей в структурированные объекты"""
    result = []
    for entry in entries:
        parsed = parse_onu_line(entry, regex_template)
        if parsed:
            result.append(parsed)
    return result


def parse_onu_line(line, regex_template):
    """Преобразует строку ONU в словарь"""
    if not line:
        return None

    match = match_onu_line_by_regex_template(line, regex_template)
    return match.groupdict() if match else None


