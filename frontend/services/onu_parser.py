from ..utils.onu_regex import match_onu_line_by_regex_template, is_start_of_onu_entry

def split_onu_entries(raw_text):
    """Разделяет сырые строки в структурированные записи ONU"""
    entries = []
    buffer = ""

    for line in raw_text.strip().splitlines():
        line = line.strip()
        if is_start_of_onu_entry(line):
            if buffer:
                entries.append(buffer.strip())
            buffer = line
        else:
            buffer += " " + line

    if buffer:
        entries.append(buffer.strip())

    return entries


def parse_onu_entries(entries, regex_template):
    """Парсит список строковых записей в структурированные объекты"""
    result = []
    for entry in entries:
        parsed = parse_onu_line(entry, regex_template)
        if parsed:
            result.append(parsed)
        #else: print("NO MATCH FOR ENTRY:", repr(entry))  # отладка
    return result


def parse_onu_line(line, regex_template):
    """Преобразует строку ONU в словарь"""
    if not line:
        return None

    match = match_onu_line_by_regex_template(line, regex_template)
    return match.groupdict() if match else None


