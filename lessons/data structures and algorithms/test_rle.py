from itertools import chain, repeat
import hypothesis.strategies as st
from hypothesis import given

iterables = st.one_of(st.tuples(st.integers(1, 10)),
                      st.lists(st.integers(0, 10)),
                      st.text().map(iter))


@given(iterables)
def test_rle(it):
    def encode_decode(rle):
        return chain.from_iterable(repeat(item, count) for item, count in rle(it))

    expected = list(it)
    assert list(encode_decode(it)) == expected
