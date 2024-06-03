# pylint: skip-file

import pytest

from wednesday import is_valid


def test_basic_test_1():
    assert is_valid("()") == True


def test_basic_test_2():
    assert is_valid("()[]{}") == True


def test_basic_test_3():
    assert is_valid("(]") == False


@pytest.mark.parametrize("s,validity",
                         [(")(", False),
                          ("))}[(", False),
                             ("{{(())}}", True),
                             ("{[[]]}", True),
                             ("}}}([]](", False),
                             ("[([{}[]])]", True),
                             ("}{}", False),
                             ("(){[}]", False),
                             ("{[}]", False),
                             ("[][][][][]", True),
                             ("}]({]]", False),
                             ("[[[]]]", True),
                             ("}{}]}[(]", False),
                             ("[(())]{}", True),
                             ("}(]({[({", False),
                             (")(", False),
                             ("}[]]]}", False),
                             ("()", True),
                             ("{}[[]]", True),
                             ("}", False),
                             ("{}", True),
                             ("}[}](", False),
                             ("{{}]{){{", False),
                             ("[]{}[]", True),
                             ("[]{}", True),
                             ("[]([])", True),
                             ("[)}[()[", False),
                             ("]])][", False),
                             ("(", False),
                             ("(]()})()", False),
                             ("(({}))", True),
                             ("))]})}", False),
                             ("[{)(]]", False),
                             ("({{[[]]}})[]", True),
                             ("()}[{(", False),
                             ("{((}{(((", False),
                             (")}}{[", False),
                             ("([{([([])])}])", True),
                             ("][)()})", False),
                             ("}[[]}{", False),
                             ("[[((", False)])
def test_random_test_cases(s, validity):
    assert is_valid(s) == validity
