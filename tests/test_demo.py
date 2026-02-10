from app import check_baidu

def test_baidu_status():
    # 断言返回的状态码是200
    assert check_baidu() == 200