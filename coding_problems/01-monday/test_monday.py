# pylint: skip-file

import pytest

from monday import kebabize


def test_basic_test_1():
    assert kebabize('myCamelCasedString') == 'my-camel-cased-string'


def test_basic_test_2():
    assert kebabize('myCamelHas3Humps') == 'my-camel-has-humps'


def test_basic_test_3():
    assert kebabize('SOS') == 's-o-s'


def test_basic_test_4():
    assert kebabize('42') == ''


def test_basic_test_5():
    assert kebabize('CodeWars') == 'code-wars'


@pytest.mark.parametrize("st,kebabcase",
                         [("JOlHSAllrhUXisu2szqd2k463r0OpS35FyRda2KyhyX", "j-ol-h-s-allrh-u-xisuszqdkr-op-s-fy-rda-kyhy-x"),
                          ("2agTNnToPe1SGUQwu5q", "ag-t-nn-to-pe-s-g-u-qwuq"),
                             ("UhEUbDZQafRJ23xZU9a2Jk3hV",
                              "uh-e-ub-d-z-qaf-r-jx-z-ua-jkh-v"),
                             ("6F61tiIUzS4RHxGSmdZTgvCHtYlXvh",
                              "fti-i-uz-s-r-hx-g-smd-z-tgv-c-ht-yl-xvh"),
                             ("2cA", "c-a"),
                             ("RDwFs", "r-dw-fs"),
                             ("CbqIDT6AWNL87RRz9SFyG",
                              "cbq-i-d-t-a-w-n-l-r-rz-s-fy-g"),
                             ("xyMVfpWcfg7BEBQ", "xy-m-vfp-wcfg-b-e-b-q"),
                             ("jpdY", "jpd-y"),
                             ("JiygFm3QohgSuFwZGGy5QNnn",
                              "jiyg-fm-qohg-su-fw-z-g-gy-q-nnn"),
                             ("I4Ea8fBbEPN3A6O6hQ3XzNNzI58oSfnIDHh4Cn08qxy",
                              "i-eaf-bb-e-p-n-a-oh-q-xz-n-nz-io-sfn-i-d-hh-cnqxy"),
                             ("XNmo77yf2M9NHNJyfKRISMJYyHHLRL",
                              "x-nmoyf-m-n-h-n-jyf-k-r-i-s-m-j-yy-h-h-l-r-l"),
                             ("7E5Rzbw", "e-rzbw"),
                             ("8gCwihTzgadcfvTu764VJ3TOqQdiuqX2Y",
                              "g-cwih-tzgadcfv-tu-v-j-t-oq-qdiuq-x-y"),
                             ("gbujY0G4zzjs1plUYrFiLMlNrHeotBuh",
                              "gbuj-y-gzzjspl-u-yr-fi-l-ml-nr-heot-buh"),
                             ("vRHFEuu4hSInUK3Hyw5uQilZnFcfMA6L0fj",
                              "v-r-h-f-euuh-s-in-u-k-hywu-qil-zn-fcf-m-a-lfj"),
                             ("QuDzqAYpr51Od61qP", "qu-dzq-a-ypr-odq-p"),
                             ("NE", "n-e"),
                             ("4l5Q687WCyjIk7fnL8BDMVTeE7w2VHYNt49HKrw1gY",
                              "l-q-w-cyj-ikfn-l-b-d-m-v-te-ew-v-h-y-nt-h-krwg-y"),
                             ("HqvA8crub4vYoZPJ9", "hqv-acrubv-yo-z-p-j"),
                             ("9tWsPlSTdz", "t-ws-pl-s-tdz"),
                             ("IaFcTRJjtfhmCtU9L8qEsKsNfbWRNkFRcmsehAaX8f",
                              "ia-fc-t-r-jjtfhm-ct-u-lq-es-ks-nfb-w-r-nk-f-rcmseh-aa-xf"),
                             ("hSTToFRZ", "h-s-t-to-f-r-z"),
                             ("5GR7uupV5qI4x", "g-ruup-vq-ix"),
                             ("X9rWDFgR6prKs9kcqKS", "xr-w-d-fg-rpr-kskcq-k-s"),
                             ("A1wppLZcNmTMKFCHFUm9l",
                              "awpp-l-zc-nm-t-m-k-f-c-h-f-uml"),
                             ("jPdKa21M7Z6AL7c5y", "j-pd-ka-m-z-a-lcy"),
                             ("Q35rO", "qr-o"),
                             ("SwujsmYk4D6WDqY9mFGIznl5Z1Aey6qpFuGFAC",
                              "swujsm-yk-d-w-dq-ym-f-g-iznl-z-aeyqp-fu-g-f-a-c"),
                             ("aykksE410T77EniQxXDFpQ9vUQS3bDnvsQz",
                              "aykks-e-t-eni-qx-x-d-fp-qv-u-q-sb-dnvs-qz"),
                             ("TKxBao6jc2hH3eik", "t-kx-baojch-heik"),
                             ("srMuDRfdJsOBYb7", "sr-mu-d-rfd-js-o-b-yb"),
                             ("lIruRddl6O9CWo7m", "l-iru-rddl-o-c-wom"),
                             ("m1sBK", "ms-b-k"),
                             ("f5U2ShONVPKqL3tJ6IvklwdPWcq98Zi9ekoSb7",
                              "f-u-sh-o-n-v-p-kq-lt-j-ivklwd-p-wcq-zieko-sb"),
                             ("9f6M80jP7dYRAWqKCCR8W",
                              "f-mj-pd-y-r-a-wq-k-c-c-r-w"),
                             ("iVWvFvAKmNWzjbwcb", "i-v-wv-fv-a-km-n-wzjbwcb"),
                             ("JEEPEtmQ7dFFHJIGzrE9znEptAw8Qxq6zDJxB0My",
                              "j-e-e-p-etm-qd-f-f-h-j-i-gzr-ezn-ept-aw-qxqz-d-jx-b-my"),
                             ("TyojSv9wK7OklIMJs1ztVNlIMObBzyFf",
                              "tyoj-svw-k-okl-i-m-jszt-v-nl-i-m-ob-bzy-ff"),
                             ("9", "")])
def test_random_test_cases(st, kebabcase):
    assert kebabize(st) == kebabcase
