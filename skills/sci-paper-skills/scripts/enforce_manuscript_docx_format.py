#!/usr/bin/env python3
"""Enforce SCI manuscript DOCX formatting in OOXML.

The script is intentionally narrow: it standardizes line numbering,
font family, font size, text color, line spacing, and paragraph
alignment for a manuscript document without rewriting document content.
"""

from __future__ import annotations

import argparse
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
MC_NS = "http://schemas.openxmlformats.org/markup-compatibility/2006"

KNOWN_NAMESPACES = {
    "w": W_NS,
    "mc": MC_NS,
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "m": "http://schemas.openxmlformats.org/officeDocument/2006/math",
    "v": "urn:schemas-microsoft-com:vml",
    "wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing",
    "wp14": "http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing",
    "w10": "urn:schemas-microsoft-com:office:word",
    "w14": "http://schemas.microsoft.com/office/word/2010/wordml",
    "w15": "http://schemas.microsoft.com/office/word/2012/wordml",
    "w16": "http://schemas.microsoft.com/office/word/2018/wordml",
    "w16cid": "http://schemas.microsoft.com/office/word/2016/wordml/cid",
    "w16se": "http://schemas.microsoft.com/office/word/2015/wordml/symex",
    "sl": "http://schemas.openxmlformats.org/schemaLibrary/2006/main",
}

for prefix, namespace in KNOWN_NAMESPACES.items():
    ET.register_namespace(prefix, namespace)

FONT_ATTRS = ("ascii", "hAnsi", "eastAsia", "cs")
FONT_THEME_ATTRS = ("asciiTheme", "hAnsiTheme", "eastAsiaTheme", "cstheme", "csTheme")


def qn(local: str) -> str:
    return f"{{{W_NS}}}{local}"


def mcqn(local: str) -> str:
    return f"{{{MC_NS}}}{local}"


def wval(element: ET.Element, name: str = "val") -> str | None:
    return element.get(qn(name))


def set_wval(element: ET.Element, value: str, name: str = "val") -> None:
    element.set(qn(name), value)


PPR_ORDER = [
    "pStyle",
    "keepNext",
    "keepLines",
    "pageBreakBefore",
    "framePr",
    "widowControl",
    "numPr",
    "suppressLineNumbers",
    "pBdr",
    "shd",
    "tabs",
    "suppressAutoHyphens",
    "kinsoku",
    "wordWrap",
    "overflowPunct",
    "topLinePunct",
    "autoSpaceDE",
    "autoSpaceDN",
    "bidi",
    "adjustRightInd",
    "snapToGrid",
    "spacing",
    "ind",
    "contextualSpacing",
    "mirrorIndents",
    "suppressOverlap",
    "jc",
    "textDirection",
    "textAlignment",
    "textboxTightWrap",
    "outlineLvl",
    "divId",
    "cnfStyle",
    "rPr",
]

RPR_ORDER = [
    "rStyle",
    "rFonts",
    "b",
    "bCs",
    "i",
    "iCs",
    "caps",
    "smallCaps",
    "strike",
    "dstrike",
    "outline",
    "shadow",
    "emboss",
    "imprint",
    "noProof",
    "snapToGrid",
    "vanish",
    "webHidden",
    "color",
    "spacing",
    "w",
    "kern",
    "position",
    "sz",
    "szCs",
    "highlight",
    "u",
    "effect",
    "bdr",
    "shd",
    "fitText",
    "vertAlign",
    "rtl",
    "cs",
    "em",
    "lang",
    "eastAsianLayout",
    "specVanish",
    "oMath",
]

STYLE_ORDER = [
    "name",
    "aliases",
    "basedOn",
    "next",
    "link",
    "autoRedefine",
    "hidden",
    "uiPriority",
    "semiHidden",
    "unhideWhenUsed",
    "qFormat",
    "locked",
    "personal",
    "personalCompose",
    "personalReply",
    "rsid",
    "pPr",
    "rPr",
    "tblPr",
    "trPr",
    "tcPr",
    "tblStylePr",
]


def insert_index(parent: ET.Element, local_name: str, order: list[str]) -> int:
    target = order.index(local_name) if local_name in order else len(order)
    for index, child in enumerate(list(parent)):
        child_local = child.tag.split("}", 1)[-1]
        child_pos = order.index(child_local) if child_local in order else len(order)
        if child_pos > target:
            return index
    return len(parent)


def ensure_child(parent: ET.Element, local_name: str, order: list[str] | None = None) -> ET.Element:
    tag = qn(local_name)
    child = parent.find(tag)
    if child is not None:
        return child
    child = ET.Element(tag)
    if order:
        parent.insert(insert_index(parent, local_name, order), child)
    else:
        parent.append(child)
    return child


def sort_children(parent: ET.Element, order: list[str]) -> None:
    children = list(parent)
    indexed_children = list(enumerate(children))

    def sort_key(item: tuple[int, ET.Element]) -> tuple[int, int]:
        index, child = item
        child_local = child.tag.split("}", 1)[-1]
        child_pos = order.index(child_local) if child_local in order else len(order)
        return child_pos, index

    sorted_children = [child for _, child in sorted(indexed_children, key=sort_key)]
    if sorted_children != children:
        parent[:] = sorted_children


def root_start_tag_span(data: bytes) -> tuple[int, int]:
    search_from = 0
    declaration_end = data.find(b"?>")
    if declaration_end != -1:
        search_from = declaration_end + 2
    start = data.find(b"<", search_from)
    end = data.find(b">", start)
    return start, end


def serialize_xml(root: ET.Element) -> bytes:
    data = ET.tostring(root, encoding="utf-8", xml_declaration=True)
    ignorable = root.get(mcqn("Ignorable"))
    if not ignorable:
        return data

    start, end = root_start_tag_span(data)
    if start == -1 or end == -1:
        return data

    root_start = data[start:end]
    declarations = []
    for prefix in ignorable.split():
        namespace = KNOWN_NAMESPACES.get(prefix)
        declaration = f"xmlns:{prefix}=".encode("utf-8")
        if namespace and declaration not in root_start:
            declarations.append(f' xmlns:{prefix}="{namespace}"'.encode("utf-8"))

    if not declarations:
        return data
    return data[:end] + b"".join(declarations) + data[end:]


def ensure_ppr(paragraph: ET.Element) -> ET.Element:
    ppr = paragraph.find(qn("pPr"))
    if ppr is not None:
        return ppr
    ppr = ET.Element(qn("pPr"))
    paragraph.insert(0, ppr)
    return ppr


def ensure_rpr(run: ET.Element) -> ET.Element:
    rpr = run.find(qn("rPr"))
    if rpr is not None:
        return rpr
    rpr = ET.Element(qn("rPr"))
    run.insert(0, rpr)
    return rpr


def style_is_heading(style_id: str | None) -> bool:
    if not style_id:
        return False
    normalized = style_id.replace(" ", "").replace("-", "").lower()
    return normalized.startswith("heading") or normalized in {"title", "subtitle"}


def paragraph_style_id(paragraph: ET.Element) -> str | None:
    ppr = paragraph.find(qn("pPr"))
    if ppr is None:
        return None
    pstyle = ppr.find(qn("pStyle"))
    return wval(pstyle) if pstyle is not None else None


def apply_run_format(rpr: ET.Element, font_family: str, color: str, size_half_points: str) -> None:
    rfonts = ensure_child(rpr, "rFonts", RPR_ORDER)
    for attr in FONT_ATTRS:
        rfonts.set(qn(attr), font_family)
    for attr in FONT_THEME_ATTRS:
        rfonts.attrib.pop(qn(attr), None)

    color_el = ensure_child(rpr, "color", RPR_ORDER)
    set_wval(color_el, color)
    sz = ensure_child(rpr, "sz", RPR_ORDER)
    set_wval(sz, size_half_points)
    sz_cs = ensure_child(rpr, "szCs", RPR_ORDER)
    set_wval(sz_cs, size_half_points)


def apply_paragraph_format(ppr: ET.Element, alignment: str, line_twips: str) -> None:
    spacing = ensure_child(ppr, "spacing", PPR_ORDER)
    spacing.set(qn("line"), line_twips)
    spacing.set(qn("lineRule"), "auto")
    jc = ensure_child(ppr, "jc", PPR_ORDER)
    set_wval(jc, alignment)


def apply_section_format(sect_pr: ET.Element, count_by: str, restart: str) -> None:
    ln_num = sect_pr.find(qn("lnNumType"))
    if ln_num is None:
        ln_num = ET.Element(qn("lnNumType"))
        insert_before = None
        for candidate in ("pgNumType", "cols", "formProt", "vAlign"):
            existing = sect_pr.find(qn(candidate))
            if existing is not None:
                insert_before = list(sect_pr).index(existing)
                break
        if insert_before is None:
            sect_pr.append(ln_num)
        else:
            sect_pr.insert(insert_before, ln_num)
    ln_num.set(qn("countBy"), count_by)
    ln_num.set(qn("restart"), restart)


def apply_settings_part(root: ET.Element) -> None:
    zoom = root.find(qn("zoom"))
    if zoom is not None and zoom.get(qn("percent")) is None:
        zoom.set(qn("percent"), "100")


def apply_styles(root: ET.Element, font_family: str, color: str, size_half_points: str, line_twips: str) -> None:
    doc_defaults = root.find(qn("docDefaults"))
    if doc_defaults is None:
        doc_defaults = ET.Element(qn("docDefaults"))
        root.insert(0, doc_defaults)

    rpr_default = ensure_child(doc_defaults, "rPrDefault")
    apply_run_format(ensure_child(rpr_default, "rPr"), font_family, color, size_half_points)

    ppr_default = ensure_child(doc_defaults, "pPrDefault")
    apply_paragraph_format(ensure_child(ppr_default, "pPr"), "both", line_twips)

    for style in root.findall(qn("style")):
        style_id = style.get(qn("styleId"))
        style_type = style.get(qn("type"))
        if style_type in {None, "paragraph", "character"}:
            apply_run_format(ensure_child(style, "rPr", STYLE_ORDER), font_family, color, size_half_points)
        if style_type in {None, "paragraph"}:
            alignment = "left" if style_is_heading(style_id) else "both"
            apply_paragraph_format(ensure_child(style, "pPr", STYLE_ORDER), alignment, line_twips)
        sort_children(style, STYLE_ORDER)

    # Built-in documents can carry nested run properties in table/list style
    # variants. Normalize those text properties without treating borders or
    # shading colors as manuscript text.
    for rpr in root.iter(qn("rPr")):
        apply_run_format(rpr, font_family, color, size_half_points)


def apply_document_part(root: ET.Element, font_family: str, color: str, size_half_points: str, line_twips: str, count_by: str, restart: str) -> None:
    for paragraph in root.iter(qn("p")):
        ppr = ensure_ppr(paragraph)
        alignment = "left" if style_is_heading(paragraph_style_id(paragraph)) else "both"
        apply_paragraph_format(ppr, alignment, line_twips)

    for run in root.iter(qn("r")):
        apply_run_format(ensure_rpr(run), font_family, color, size_half_points)

    for sect_pr in root.iter(qn("sectPr")):
        apply_section_format(sect_pr, count_by, restart)


def xml_targets(names: list[str]) -> list[str]:
    targets = []
    for name in names:
        if name == "word/styles.xml":
            targets.append(name)
        elif name == "word/document.xml":
            targets.append(name)
        elif name == "word/settings.xml":
            targets.append(name)
        elif name.startswith("word/header") and name.endswith(".xml"):
            targets.append(name)
        elif name.startswith("word/footer") and name.endswith(".xml"):
            targets.append(name)
        elif name in {"word/footnotes.xml", "word/endnotes.xml", "word/comments.xml"}:
            targets.append(name)
    return targets


def enforce_docx(input_path: Path, output_path: Path, font_family: str, color: str, size_half_points: str, line_twips: str, count_by: str, restart: str) -> None:
    with zipfile.ZipFile(input_path, "r") as zin:
        infos = zin.infolist()
        xml_names = set(xml_targets([info.filename for info in infos]))
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as tmp:
            tmp_path = Path(tmp.name)
        try:
            with zipfile.ZipFile(tmp_path, "w", compression=zipfile.ZIP_DEFLATED) as zout:
                for info in infos:
                    data = zin.read(info.filename)
                    if info.filename in xml_names:
                        root = ET.fromstring(data)
                        if info.filename == "word/styles.xml":
                            apply_styles(root, font_family, color, size_half_points, line_twips)
                        elif info.filename == "word/settings.xml":
                            apply_settings_part(root)
                        else:
                            apply_document_part(root, font_family, color, size_half_points, line_twips, count_by, restart)
                        data = serialize_xml(root)
                    zout.writestr(info, data)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            if input_path.resolve() == output_path.resolve():
                shutil.move(str(tmp_path), str(output_path))
            else:
                shutil.copyfile(tmp_path, output_path)
        finally:
            tmp_path.unlink(missing_ok=True)


def font_family_errors(rpr: ET.Element | None, font_family: str, context: str) -> list[str]:
    if rpr is None:
        return [f"{context}: run properties are missing"]
    rfonts = rpr.find(qn("rFonts"))
    if rfonts is None:
        return [f"{context}: run font family is not {font_family}"]

    errors = []
    for attr in FONT_ATTRS:
        if rfonts.get(qn(attr)) != font_family:
            errors.append(f"{context}: run font {attr} is not {font_family}")
    for attr in FONT_THEME_ATTRS:
        if rfonts.get(qn(attr)) is not None:
            errors.append(f"{context}: run font theme {attr} should be removed in favor of {font_family}")
    return errors


def style_order_errors(style: ET.Element, context: str) -> list[str]:
    seen_positions = []
    for child in list(style):
        child_local = child.tag.split("}", 1)[-1]
        if child_local in STYLE_ORDER:
            seen_positions.append((STYLE_ORDER.index(child_local), child_local))

    errors = []
    for previous, current in zip(seen_positions, seen_positions[1:]):
        if current[0] < previous[0]:
            style_id = style.get(qn("styleId")) or "unknown"
            errors.append(
                f"{context}: style {style_id} child order has {current[1]} after {previous[1]}"
            )
            break
    return errors


def ignorable_namespace_errors(raw_xml: bytes, root: ET.Element, context: str) -> list[str]:
    ignorable = root.get(mcqn("Ignorable"))
    if not ignorable:
        return []

    start, end = root_start_tag_span(raw_xml)
    if start == -1 or end == -1:
        return [f"{context}: could not inspect root namespace declarations"]
    root_start = raw_xml[start:end]

    errors = []
    for prefix in ignorable.split():
        if f"xmlns:{prefix}=".encode("utf-8") not in root_start:
            errors.append(f"{context}: namespace '{prefix}' in Ignorable but not declared")
    return errors


def settings_errors(root: ET.Element, context: str) -> list[str]:
    zoom = root.find(qn("zoom"))
    if zoom is not None and zoom.get(qn("percent")) is None:
        return [f"{context}: zoom is missing w:percent"]
    return []


def collect_check_errors(docx_path: Path, font_family: str, color: str, size_half_points: str, line_twips: str, count_by: str, restart: str) -> list[str]:
    errors: list[str] = []
    with zipfile.ZipFile(docx_path, "r") as zf:
        for name in xml_targets(zf.namelist()):
            raw_xml = zf.read(name)
            root = ET.fromstring(raw_xml)
            errors.extend(ignorable_namespace_errors(raw_xml, root, name))
            if name == "word/settings.xml":
                errors.extend(settings_errors(root, name))
            elif name != "word/styles.xml":
                sect_prs = list(root.iter(qn("sectPr")))
                if name == "word/document.xml" and not sect_prs:
                    errors.append(f"{name}: no section properties found for line numbering")
                for sect_pr in sect_prs:
                    ln_num = sect_pr.find(qn("lnNumType"))
                    if ln_num is None or ln_num.get(qn("countBy")) != count_by or ln_num.get(qn("restart")) != restart:
                        errors.append(f"{name}: section line numbering is not countBy={count_by}, restart={restart}")
                for paragraph in root.iter(qn("p")):
                    ppr = paragraph.find(qn("pPr"))
                    expected_jc = "left" if style_is_heading(paragraph_style_id(paragraph)) else "both"
                    spacing = ppr.find(qn("spacing")) if ppr is not None else None
                    jc = ppr.find(qn("jc")) if ppr is not None else None
                    if spacing is None or spacing.get(qn("line")) != line_twips or spacing.get(qn("lineRule")) != "auto":
                        errors.append(f"{name}: paragraph line spacing is not {line_twips}/auto")
                    if jc is None or wval(jc) != expected_jc:
                        errors.append(f"{name}: paragraph alignment is not {expected_jc}")
                for run in root.iter(qn("r")):
                    rpr = run.find(qn("rPr"))
                    errors.extend(font_family_errors(rpr, font_family, name))
                    color_el = rpr.find(qn("color")) if rpr is not None else None
                    sz = rpr.find(qn("sz")) if rpr is not None else None
                    sz_cs = rpr.find(qn("szCs")) if rpr is not None else None
                    if color_el is None or wval(color_el) != color:
                        errors.append(f"{name}: run color is not {color}")
                    if sz is None or wval(sz) != size_half_points or sz_cs is None or wval(sz_cs) != size_half_points:
                        errors.append(f"{name}: run size is not {size_half_points} half-points")
            else:
                for style in root.findall(qn("style")):
                    errors.extend(style_order_errors(style, name))
                for rpr in root.iter(qn("rPr")):
                    errors.extend(font_family_errors(rpr, font_family, name))
                    color_el = rpr.find(qn("color"))
                    sz = rpr.find(qn("sz"))
                    sz_cs = rpr.find(qn("szCs"))
                    if color_el is not None and (wval(color_el) or "").upper() != color:
                        errors.append(f"{name}: run style color is not {color}")
                    if sz is not None and wval(sz) != size_half_points:
                        errors.append(f"{name}: run style size {wval(sz)}, expected {size_half_points}")
                    if sz_cs is not None and wval(sz_cs) != size_half_points:
                        errors.append(f"{name}: complex-script run style size {wval(sz_cs)}, expected {size_half_points}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Enforce or check SCI manuscript DOCX formatting.")
    parser.add_argument("input_docx", type=Path)
    parser.add_argument("output_docx", type=Path, nargs="?", help="Output DOCX. Omit with --check.")
    parser.add_argument("--check", action="store_true", help="Check formatting without writing.")
    parser.add_argument("--font-family", default="Times New Roman", help="Font family for all manuscript text.")
    parser.add_argument("--color", default="000000", help="OOXML text color, default black.")
    parser.add_argument("--size-pt", type=float, default=12.0, help="Font size in points.")
    parser.add_argument("--line-spacing", type=float, default=1.5, help="Line spacing multiplier.")
    parser.add_argument("--line-count-by", default="1", help="Line number interval.")
    parser.add_argument("--line-restart", default="continuous", choices=["continuous", "newPage", "newSection"])
    args = parser.parse_args()

    if not args.input_docx.exists():
        parser.error(f"input DOCX not found: {args.input_docx}")
    if not args.check and args.output_docx is None:
        parser.error("output_docx is required unless --check is used")

    color = args.color.upper()
    size_half_points = str(int(round(args.size_pt * 2)))
    line_twips = str(int(round(240 * args.line_spacing)))

    if args.check:
        errors = collect_check_errors(args.input_docx, args.font_family, color, size_half_points, line_twips, args.line_count_by, args.line_restart)
        if errors:
            for error in errors[:50]:
                print(error, file=sys.stderr)
            if len(errors) > 50:
                print(f"... {len(errors) - 50} additional issue(s)", file=sys.stderr)
            return 1
        print("DOCX manuscript formatting check passed.")
        return 0

    assert args.output_docx is not None
    enforce_docx(args.input_docx, args.output_docx, args.font_family, color, size_half_points, line_twips, args.line_count_by, args.line_restart)
    print(f"Wrote formatted DOCX: {args.output_docx}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
