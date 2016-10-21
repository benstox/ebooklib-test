#!/usr/bin/env python3

from ebooklib import epub

book = epub.EpubBook()

# set metadata
book.set_identifier('id123456')
book.set_title('The Tale of Gamelyn')
book.set_language('en')

book.add_author('Stephen Knight', file_as='Knight, Stephen', role='ed')
book.add_author('Thomas H Ohlgren', file_as='Ohlgren, Thomas H', role='ed')

# create chapter
c1 = epub.EpubHtml(title='Introduction', file_name='introduction.xhtml', lang='en')
c1.content = u"""
    <h1>Introduction</h1>
    <p>The Tale of Gamelyn survives in twenty-five early manuscripts, yet this is not a sign that it was popular. The poem was added to one version of The Canterbury Tales (known as the cd group of manuscripts) where it follows the unfinished Cook's Tale, often with a spurious link to make it his second tale. The cd connection with Gamelyn began very early (Manly and Rickert, 1940, II, 170-72), and it may have been generated at a stage when Chaucer himself had included Gamelyn among his papers, with the intention of rewriting it for a suitable character. Nevertheless, there is, as Laura Hibberd stated (1924, p. 156), no sign that Chaucer's own hand was involved in the transmission of the text.</p>
"""
c2 = epub.EpubHtml(title='Text', file_name='text.xhtml', lang='en')
c2.content = u"""
    <h1>Text</h1>
    <h2>Fitt 1</h2>
    <p>Lithes and listneth     and harkeneth aright,</p>
    <p>And ye shul here     of a doughty knyght;</p>
    <p>Sire John of Boundes     was his name,</p>
    <p>He coude of norture     and of mochel game.</p>
"""


# add chapter
book.add_item(c1)
book.add_item(c2)

# define Table Of Contents
book.toc = (
    epub.Link('introduction.xhtml', 'Introduction', 'introduction'),
    (epub.Section('The Tale of Gamelyn'), (c1, )),
    epub.Link('text.xhtml', 'Text', 'text'),
    (epub.Section('The Tale of Gamelyn'), (c2, )))

# add default NCX and Nav file
book.add_item(epub.EpubNcx())
book.add_item(epub.EpubNav())

# define CSS style
style = 'BODY {color: white;}'
nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)

# add CSS file
book.add_item(nav_css)

# basic spine
book.spine = ['nav', c1]

# write to the file
epub.write_epub('test.epub', book, {})
