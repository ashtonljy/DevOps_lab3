import price_info as price

def test_total_cost_shopping():
    expected = 46.75
    result = price.total_cost_shopping()
    assert(result == expected)