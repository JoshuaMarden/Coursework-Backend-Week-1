# pylint: skip-file

import pytest

from tuesday import length_of_last_word


def test_basic_test_1():
    assert length_of_last_word("Hello World") == 5


def test_basic_test_2():
    assert length_of_last_word("   fly me   to   the moon  ") == 4


def test_basic_test_3():
    assert length_of_last_word("luffy is still joyboy") == 6


@pytest.mark.parametrize("s,word_length",
                         [("ySZlK vvJzzRBwxDrRv  XZ", 2),
                          ("KJ  dIMDVWhhDAS Tj vMPy", 4),
                             ("AWfVS tjT", 3),
                             ("GzJ s z xo  QD pScwgKQmPyoXWZaPsuNIdci", 23),
                             ("X GmRFkaVBPt snPcRfoyhaxnV P Grwg g", 1),
                             ("U L  qLHKEeNDcKndBtSvH rHRU   crtgd", 5),
                             ("Ys ", 2),
                             (" rAOFiyUOB ENYpJwWwty mS HdNrMECvC", 9),
                             (" E  U ZLrtekjTTsGsH W ", 1),
                             (" E ODcR  AbOVzRvC EnxVPptzcXdd", 12),
                             ("IarCIvBJ  RJtdxfAEMNaZO g", 1),
                             ("Fl XwHgSme jD wCywPp mJxL", 4),
                             ("NTyGHNPJ pbcPjkbRDg aTcI uNOA rYHkRv TO G mv", 2),
                             ("hqldmxvNr  YIEu QKJsE  qaOQ", 4),
                             ("uI", 2),
                             ("gPOBqwtrCHrAOB uJ mQp     ahKT zik", 3),
                             (" PZ B WK soBNDArhI  NNFPVVdewuXi ysLZZBk  ovx", 3),
                             ("  ZpbAgXzk gQJ I B wA EgYw  Nhz  duH", 3),
                             ("A TcBhEQlolPw", 11),
                             ("HKMzL ", 5),
                             ("  zyEAqRI   ie", 2),
                             ("w uyM RJBqW b myF JIrrBLP", 7),
                             ("VArtvORJwV bR", 2),
                             ("m HGNNEaHS  JV", 2),
                             ("M", 1),
                             ("nPDS zRROw Uzgr  ygjECtI Td toFV zI  Wz oPKb ", 4),
                             ("uXr XKv c IDhe  J FPQ f AhgnT YvHs", 4),
                             (" S L IsJJ", 4),
                             ("Lz ZR rKTBV iM   nK  zxxiBloBbqliEh Ixl ", 3),
                             ("Sm OTiDUNt", 7),
                             ("h rZdI lKexUyAbcRQEd s zcNkOjL", 7),
                             ("WtMkAYD  zyth ZdrclqaF BGc ", 3),
                             ("zVNKy  N", 1),
                             ("mVOhsmsVOjQo", 12),
                             (" Bg TTE", 3),
                             ("G zng", 3),
                             ("czJskXXBYlNkSgXS h  e bHFW ugOOZ", 5),
                             ("C", 1),
                             ("  IIYwg", 5),
                             ("jbGPFwJt L cl jHddlHrKY ", 9)])
def test_random_test_cases(s, word_length):
    assert length_of_last_word(s) == word_length
