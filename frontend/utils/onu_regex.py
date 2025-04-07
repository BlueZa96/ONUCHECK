import re

def match_onu_line_by_regex_template(line, regex_template):
    """Ищет совпадение строки с шаблоном ONU"""
    return regex_template.match(line.strip())

def is_start_of_onu_entry(line):
    """Определяет, начинается ли строка с новой записи ONU (регистр игнорируется)"""
    return re.match(r'^GPON\d+', line.strip(), re.IGNORECASE) is not None