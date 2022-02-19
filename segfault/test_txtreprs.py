from __future__ import annotations

def test_ND_empty_repr_double(named_hist):

    h = (
        named_hist.new.Reg(10, -1, 1, name="x", label="y")
        .StrCat([], name="a", label="b")
        .Double()
    )
    assert "name='x'" in repr(h)
    assert "label='y'" in repr(h)
    assert "name='a'" in repr(h)
    assert "label='b'" in repr(h)

def test_ND_empty_repr_weight(named_hist):

    h = (
        named_hist.new.Reg(10, -1, 1, name="x", label="y")
        .StrCat([], name="a", label="b")
        .Weight()
    )
    assert "name='x'" in repr(h)
    assert "label='y'" in repr(h)
    assert "name='a'" in repr(h)
    assert "label='b'" in repr(h)