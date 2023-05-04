from tech_news.analyzer.reading_plan import ReadingPlanService  # noqa: F401, E261, E501
from unittest.mock import MagicMock
import pytest

mock_news = [
    {
        "title": "new 1",
        "reading_time": 1,
    },
    {
        "title": "new 2",
        "reading_time": 100,
    },
    {
        "title": "new 3",
        "reading_time": 5,
    }
]


def test_reading_plan_group_news():
    ReadingPlanService._db_news_proxy = MagicMock(return_value=mock_news)
    result = ReadingPlanService.group_news_for_available_time(10)

    assert len(result['readable']) == 1
    assert len(result['unreadable']) == 1
    assert len(result["readable"][0]['chosen_news']) == 2
    assert result["readable"][0]['unfilled_time'] == 4

    with pytest.raises(ValueError):
        ReadingPlanService.group_news_for_available_time(-1)
