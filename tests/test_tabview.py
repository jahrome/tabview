#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tabview.tabview as t


def test_tabview_encoding():
    """Test that correct encoding is returned for a latin-1 and a utf-8 encoded
    file.

    """
    r = t.detect_encoding('sample/test_latin-1.csv')
    assert(r == 'latin-1')
    r = t.detect_encoding('sample/unicode-example-utf8.txt')
    assert(r == 'utf-8')


def test_tabview_file():
    """Test that data processed from two files matches the data below

    """
    res1 = [["Origin (English)", "Name (English)",
             "Origin (Native)", "Name (Native)"],
            ["Australia", "Nicole Kidman", "Australia", "Nicole Kidman"]]
    res2 = ["ALP", "B34130005", "Ladies' 7 oz. ComfortSoft® Cotton "
            "Piqué Polo - WHITE - L",
            "100% ComfortSoft&#174; cotton; Welt-knit collar; Tag-free neck "
            "label; High-stitch density for superior embellishment platform; "
            "Ash is 99% cotton, 1% polyester; Light Steel is 90% cotton, "
            "10% polyester; Hemmed sleeves; Sideseamed for a feminine fit; "
            "Narrow, feminine, clean-finished placket with four "
            "dyed-to-match buttons; ", "8.96", "7.51", "5.78", "035", "L",
            "28", "5", "WHITE", "FFFFFF", "00", ".58",
            "http://www.alphabroder.com",
            "/images/alp/prodDetail/035_00_p.jpg",
            "/images/alp/prodGallery/035_00_g.jpg", "17.92", "035",
            "00766369145683", "100", "no", "Hanes", "6", "36", "1007", "no",
            "/images/alp/prodDetail/035_00_p.jpg",
            "/images/alp/backDetail/035_bk_00_p.jpg",
            "/images/alp/sideDetail/035_sd_00_p.jpg"]
    res = t.process_file('sample/unicode-example-utf8.txt')[0:2]
    assert(res == res1)
    res = t.process_file('sample/test_latin-1.csv')[-1]
    assert(res == res2)
