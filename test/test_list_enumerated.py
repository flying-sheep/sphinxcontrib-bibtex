"""
    test_list_enumerated
    ~~~~~~~~~~~~~~~~~~~~

    Test the ``:list: enumerated`` option.
"""

import pytest
import re


@pytest.mark.sphinx('html', testroot='list_enumerated')
def test_list_enumerated(app, warning):
    app.builder.build_all()
    assert not warning.getvalue()
    output = (app.outdir / "index.html").read_text()
    assert re.search(
        '<ol .*start="1".*>'
        '.*<li.*Akkerdju.*</li>'
        '.*<li.*Bro.*</li>'
        '.*<li.*Chap.*</li>'
        '.*<li.*Dude.*</li>'
        '.*</ol>'
        '.*<ol .*start="5".*>'
        '.*<li.*Eminence.*</li>'
        '.*<li.*Frater.*</li>'
        '.*<li.*Giggles.*</li>'
        '.*<li.*Handy.*</li>'
        '.*</ol>'
        '.*<ol .*start="23".*>'
        '.*<li.*Iedereen.*</li>'
        '.*<li.*Joke.*</li>'
        '.*<li.*Klopgeest.*</li>'
        '.*<li.*Laterfanter.*</li>'
        '.*</ol>',
        output, re.DOTALL)
