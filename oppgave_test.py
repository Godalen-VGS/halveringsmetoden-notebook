import math

import pytest

from notebook_loader import last_notebook

oppgave = last_notebook("oppgave")


@pytest.mark.parametrize("f,a,b,fasit", [
    (lambda x: x**2 - 2, 0, 2, math.sqrt(2)),
    (lambda x: x**2 - 2, -2, 0, -math.sqrt(2)),
    (lambda x: x**3 - x - 2, 1, 2, 1.5213797068045676),
    (lambda x: math.cos(x) - x, 0, 1, 0.7390851332151607),
    (lambda x: 3*x - 6, 0, 5, 2.0),
    (lambda x: x - 1, 1, 3, 1.0),
], ids=["sqrt2", "minus_sqrt2", "kubisk", "cos", "lineaer", "nullpunkt_i_endepunkt"])
def test_finner_nullpunkt(f, a, b, fasit):
    svar = oppgave.halvering(f, a, b)
    assert svar is not None
    assert abs(svar - fasit) <= 1e-6


def test_ingen_fortegnsskifte_gir_none():
    # Sjekker også et vanlig tilfelle, så en tom funksjon som alltid gir None ikke får poeng
    assert oppgave.halvering(lambda x: x**2 - 2, 0, 2) is not None
    assert oppgave.halvering(lambda x: x**2 + 1, -1, 1) is None


def test_toleranse_brukes():
    svar = oppgave.halvering(lambda x: x**2 - 2, 0, 2, toleranse=1e-10)
    assert abs(svar - math.sqrt(2)) <= 1e-10
