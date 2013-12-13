# -*- coding: utf-8 -*-
from __future__ import absolute_import
import lxml.html
from webstruct import WebAnnotatorLoader

HTML = b"""
<html><head>
<meta http-equiv="content-type" content="text/html; charset=windows-1252"></head><body onbeforeunload=""><p><span style="" wa-subtypes="" wa-id="8" wa-type="ORG" class="WebAnnotator_ORG">Scrapin</span><span style="" wa-subtypes="" wa-id="8" wa-type="ORG" class="WebAnnotator_ORG">ghub</span> has an <b>office</b> in <span style="" wa-subtypes="" wa-id="9" wa-type="CITY" class="WebAnnotator_CITY">Montevideo</span></p>
</body><wa-color id="WA-color-0" bg="#33CCFF" fg="#000000" class="WebAnnotator_ORG" type="ORG"></wa-color><wa-color id="WA-color-1" bg="#FF0000" fg="#000000" class="WebAnnotator_PER" type="PER"></wa-color><wa-color id="WA-color-2" bg="#33FF33" fg="#000000" class="WebAnnotator_FUNC" type="FUNC"></wa-color><wa-color id="WA-color-3" bg="#CC66CC" fg="#000000" class="WebAnnotator_TEL" type="TEL"></wa-color><wa-color id="WA-color-4" bg="#FF9900" fg="#000000" class="WebAnnotator_FAX" type="FAX"></wa-color><wa-color id="WA-color-5" bg="#99FFFF" fg="#000000" class="WebAnnotator_EMAIL" type="EMAIL"></wa-color><wa-color id="WA-color-6" bg="#FF6666" fg="#000000" class="WebAnnotator_HOURS" type="HOURS"></wa-color><wa-color id="WA-color-7" bg="#66FF99" fg="#000000" class="WebAnnotator_SUBJ" type="SUBJ"></wa-color><wa-color id="WA-color-8" bg="#3333FF" fg="#FFFFFF" class="WebAnnotator_STREET" type="STREET"></wa-color><wa-color id="WA-color-9" bg="#660000" fg="#FFFFFF" class="WebAnnotator_CITY" type="CITY"></wa-color><wa-color id="WA-color-10" bg="#006600" fg="#FFFFFF" class="WebAnnotator_STATE" type="STATE"></wa-color><wa-color id="WA-color-11" bg="#663366" fg="#FFFFFF" class="WebAnnotator_ZIPCODE" type="ZIPCODE"></wa-color><wa-color id="WA-color-12" bg="#993300" fg="#FFFFFF" class="WebAnnotator_COUNTRY" type="COUNTRY"></wa-color></html>
"""

def test_wa_loader():
    ld = WebAnnotatorLoader()
    tree = ld.loadbytes(HTML)
    res = lxml.html.tostring(tree)
    assert "<p> __START_ORG__ Scrapinghub __END_ORG__  has an <b>office</b> in  __START_CITY__ Montevideo __END_CITY__ </p>" in res
    assert "wa-" not in res, res
    assert "WA-" not in res, res
