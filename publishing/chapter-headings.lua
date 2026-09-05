local chapter_pattern = "^Kapitel%s+(%d+)%s*:%s*(.+)$"

local function latex_escape(text)
  local replacements = {
    ["\\"] = "\\textbackslash{}", ["{"] = "\\{", ["}"] = "\\}",
    ["#"] = "\\#", ["$"] = "\\$", ["%"] = "\\%", ["&"] = "\\&",
    ["_"] = "\\_", ["^"] = "\\textasciicircum{}", ["~"] = "\\textasciitilde{}",
  }
  return (text:gsub(".", function(char)
    return replacements[char] or char
  end))
end

function Header(el)
  if el.level ~= 1 then
    return nil
  end

  local text = pandoc.utils.stringify(el.content)

  -- Inledningen ska börja på ny sida i PDF efter innehållsförteckningen.
  if text == "Inledning" and FORMAT:match("latex") then
    return pandoc.RawBlock("latex", "\\clearpage\n\\section{Inledning}")
  end

  local number, title = text:match(chapter_pattern)
  if not number then
    return nil
  end

  -- PDF: enradig TOC-post men två centrerade rader i själva kapitlet.
  if FORMAT:match("latex") then
    local short = latex_escape("Kapitel " .. number .. ": " .. title)
    local visible_title = latex_escape(title)
    local command = table.concat({
      "\\clearpage",
      "\\section[" .. short .. "]{",
      "{\\normalfont\\large Kapitel " .. number .. "}\\\\[0.35em]",
      "{\\Huge\\bfseries " .. visible_title .. "}",
      "}"
    }, "\n")
    return pandoc.RawBlock("latex", command)
  end

  -- EPUB: behåll en semantisk H1-rad för navigationen. CSS visar den som
  -- två rader i boktexten utan att navigationstiteln bryts.
  local content = {
    pandoc.Span({pandoc.Str("Kapitel " .. number)}, pandoc.Attr("", {"chapter-number"})),
    pandoc.Space(),
    pandoc.Span({pandoc.Str(title)}, pandoc.Attr("", {"chapter-title"}))
  }
  local classes = el.classes
  classes:insert("chapter-heading")
  return pandoc.Header(1, content, pandoc.Attr(el.identifier, classes, el.attributes))
end
