"""Convert a solution Markdown file to Word with native (OMML) equations.

Usage: python3 build_docx.py <solution.md>

Styles and page setup come from templates/reference.docx. Paragraphs in an
"Answer Box" custom-style block get a border so text answers are boxed like
the \\boxed{} equation answers.
"""
import sys
from pathlib import Path

import docx
import pypandoc
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

HERE = Path(__file__).resolve().parent


def box_paragraph(p):
    ppr = p._p.get_or_add_pPr()
    bdr = OxmlElement("w:pBdr")
    for side in ("top", "left", "bottom", "right"):
        e = OxmlElement(f"w:{side}")
        e.set(qn("w:val"), "single")
        e.set(qn("w:sz"), "8")
        e.set(qn("w:space"), "4")
        e.set(qn("w:color"), "000000")
        bdr.append(e)
    ppr.append(bdr)


def main(md):
    md = Path(md).resolve()
    out = md.with_suffix(".docx")
    pypandoc.convert_file(
        str(md), "docx", outputfile=str(out),
        extra_args=[f"--reference-doc={HERE / 'templates' / 'reference.docx'}",
                    f"--resource-path={md.parent}"],
    )
    d = docx.Document(str(out))
    for p in d.paragraphs:
        if p.style.name == "Answer Box":
            box_paragraph(p)
    d.save(str(out))
    print(out)


if __name__ == "__main__":
    main(sys.argv[1])
