function Header (el)
  return pandoc.Header(el.level, el.content)
end
