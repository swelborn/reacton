import reactivex.subject

import react_ipywidgets as react
import react_ipywidgets.rx as iprx

from . import ipywidgets as w
from . import logging  # noqa: F401


def test_basic():
    source = reactivex.subject.BehaviorSubject("a")

    @react.component
    def Test():
        label = iprx.use_observable_state(source, "b")
        return w.Button(description=label)

    box = react.make(Test())
    assert box.children[0].description == "a"
    source.on_next("Hi")
    assert box.children[0].description == "Hi"
    source.on_next("Py")
    assert box.children[0].description == "Py"
