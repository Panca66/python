from tema2_nr_par import nr_par

def test_simple():
    assert nr_par(18)
    assert nr_par(19) == False
