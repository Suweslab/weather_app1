import pytest
from weather import get_weather, format_weather

def test_getwether():
    data = get_weather("Sydney")
    assert data['city'] == "Sydney"
    assert data['temperature'] == 25
    assert data['condition'] == "Sunny"

def test_fortmat_weather():
    data = get_weather("Sydney")
    result = format_weather(data)
    assert result == "The weather in Sydney is 25 with Sunny conditions."