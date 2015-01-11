# -*- coding: utf-8 -*-

import pytest
import tabview.tabview as t


res1 = ["Yugoslavia (Latin)", "Djordje Balasevic", "Jugoslavija",
        "Đorđe Balašević"]
res2 = ["ALP", "B34130005", "Ladies' 7 oz. ComfortSoft® Cotton "
        "Piqué Polo - WHITE - L",
        "100% ComfortSoft&#174; cotton; Welt-knit collar; "
        "Tag-free neck label; High-stitch density for superior "
        "embellishment platform; "
        "Ash is 99% cotton, 1% polyester; Light Steel is "
        "90% cotton, 10% polyester; Hemmed sleeves; "
        "Sideseamed for a feminine fit; "
        "Narrow, feminine, clean-finished placket with four "
        "dyed-to-match buttons; ",
        "8.96", "7.51", "5.78", "035", "L",
        "28", "5", "WHITE", "FFFFFF", "00", ".58",
        "http://www.alphabroder.com",
        "/images/alp/prodDetail/035_00_p.jpg",
        "/images/alp/prodGallery/035_00_g.jpg", 17.92, "035",
        "00766369145683", "100", "no", "Hanes", "6",
        "36", "1007", "no", "/images/alp/prodDetail/035_00_p.jpg",
        "/images/alp/backDetail/035_bk_00_p.jpg",
        "/images/alp/sideDetail/035_sd_00_p.jpg"]


@pytest.fixture(params=[('sample/unicode-example-utf8.txt', 'utf-8', res1),
                        ('sample/test_latin-1.csv', 'latin-1', res2)])
def data(request):
    with open(request.param[0], 'rb') as f:
            return f.readlines(), request.param[1], request.param[2]


def test_tabview_encoding(data):
    """Test that correct encoding is returned for a latin-1 and a utf-8 encoded
    file.

    """
    d, enc, _ = data
    r = t.detect_encoding(d)
    assert(r == enc)


def test_tabview_file(data):
    """Test that data processed from two files matches the data below

    """
    d, _, sample_data = data
    code = 'utf-8'  # Per top line of file
    res = t.process_data(d)
    # Check that process_file returns a list of lists
    assert type(res) == list and type(res[0]) == list
    # Have to decode res1 and res2 from utf-8 so they can be compared to
    # the results from the file, which are unicode (py2) or string (py3)
    for j, i in enumerate(sample_data):
        try:
            i = i.decode(code)
        except AttributeError:
            i = str(i)
        assert i == res[-1][j]
