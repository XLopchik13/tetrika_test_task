import pytest
from unittest.mock import patch, MagicMock
from solution import get_animals_count_by_letter


@pytest.fixture
def mock_pages():
    html_page_1 = """
    <div id="mw-pages">
        <div class="mw-category-group">
            <ul>
                <li><a href="/wiki/Антилопа">Антилопа</a></li>
                <li><a href="/wiki/Бегемот">Бегемот</a></li>
                <li><a href="/wiki/Белка">Белка</a></li>
            </ul>
        </div>
    </div>
    <a href="/next">Следующая страница</a>
    """

    html_page_2 = """
    <div id="mw-pages">
        <div class="mw-category-group">
            <ul></ul>
        </div>
    </div>
    """

    response_1 = MagicMock()
    response_1.status_code = 200
    response_1.text = html_page_1

    response_2 = MagicMock()
    response_2.status_code = 200
    response_2.text = html_page_2

    return [response_1, response_2]


@patch("solution.requests.get")
def test_get_animals_count_by_letter(mock_get, mock_pages):
    mock_get.side_effect = mock_pages

    result = get_animals_count_by_letter()

    assert result["А"] == 1
    assert result["Б"] == 2
    assert "В" not in result
