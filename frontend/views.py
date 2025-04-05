# views.py
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings

from .services.onu_parser import split_onu_entries, parse_onu_entries
from .utils.merge_lists import merge_onu_data_and_stats
from .utils.api_caller import onu_api_call_get
from .regex_templates import ONU_DATA_LINE_REGEX, ONU_STATS_LINE_REGEX


def index(request):
    return render(request, 'index.html')

def get_onu_data_and_stat(request):
    try:
        raw_data = onu_api_call_get(settings.ONU_DATA_URL).text
        raw_stats = onu_api_call_get(settings.ONU_STATS_URL).text

        data_entries = split_onu_entries(raw_data)
        stats_entries = split_onu_entries(raw_stats)

        parsed_data = parse_onu_entries(data_entries, ONU_DATA_LINE_REGEX)
        parsed_stats = parse_onu_entries(stats_entries, ONU_STATS_LINE_REGEX)

        merged_result = merge_onu_data_and_stats(parsed_data, parsed_stats)
        return JsonResponse(merged_result, safe=False)
    except Exception as e:
        return JsonResponse({"error": str(e)})
