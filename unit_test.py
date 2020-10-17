import pytest
import requests
import Main
from Constants import BASE


def test_prepare_routes():
    src, list_of_dst = "13.388860,52.517037", ["13.397634,52.529407","13.428555,52.523219"]
    expected_result = [{'destination': '13.397634,52.529407', 'duration': 251.5, 'distance': 1884.8}, {'destination': '13.428555,52.523219', 'duration': 394.2, 'distance': 3841.7}]
    result = Main.prepare_routes(src, list_of_dst)
    assert result == expected_result

def test_sort_route_list_by_duration():
    test_list = [{'destination': '13.428555,52.523219', 'duration': 394.2, 'distance': 3841.7}, {'destination': '13.397634,52.529407', 'duration': 251.5, 'distance': 1884.8}]
    expected_result = [{'destination': '13.397634,52.529407', 'duration': 251.5, 'distance': 1884.8}, {'destination': '13.428555,52.523219', 'duration': 394.2, 'distance': 3841.7}]
    
    Main.sort_route_list_by_duration(test_list)
    assert test_list == expected_result

def test_sort_repetitions():
    test_list = [{'destination': '13.428555,52.523219', 'duration': 394.2, 'distance': 3841.7}, {'destination': '13.397634,52.529407', 'duration': 394.2, 'distance': 1884.8}]
    expected_result = [{'destination': '13.397634,52.529407', 'duration': 394.2, 'distance': 1884.8}, {'destination': '13.428555,52.523219', 'duration': 394.2, 'distance': 3841.7}]
    
    Main.sort_repetitions(test_list)
    assert test_list == expected_result