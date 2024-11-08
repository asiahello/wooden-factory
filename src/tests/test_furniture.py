from src.furniture import Cabinet

def test_hotty_cabinet():
    cabinet = Cabinet(width=1000, height=2000, type="hotty")
    assert len(cabinet.elements) == 17  # 5 horizontal, 12 vertical
    assert cabinet.total_weight() > 0

def test_vetty_cabinet():
    cabinet = Cabinet(width=1000, height=2000, type="vetty")
    assert len(cabinet.elements) == 13  # 10 horizontal, 3 vertical
    assert cabinet.total_weight() > 0