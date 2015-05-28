# Summary

    dewinfont.py: .fon (NE) => .fd (Plaintext)
    show.py:      .fd => .png

# Character Map (Partial)

|   vgafix   |   8514fix  |
|------------|------------|
| ![vgafix]  | ![8514fix] |

|   vgafixe  |   vgafixg  |   vgafixr  |   vgafixt  |
|------------|------------|------------|------------|
| ![vgafixe] | ![vgafixg] | ![vgafixr] | ![vgafixt] |

|   cvgafix  |   hvgafix  |   jvgafix  |   svgafix  |
|------------|------------|------------|------------|
| ![cvgafix] | ![hvgafix] | ![jvgafix] | ![svgafix] |

|   vgaf874  |   vgaf1255  |   vgaf1256  |   vgaf1257  |
|------------|-------------|-------------|-------------|
| ![vgaf874] | ![vgaf1255] | ![vgaf1256] | ![vgaf1257] |

Q: What happened to cp1255 and cp1256 ?

[8514fix]: https://raw.githubusercontent.com/libmaru/Fixedsys/master/8514/8514fix.png
[vgafix]:  https://raw.githubusercontent.com/libmaru/Fixedsys/master/vga/vgafix.png
[vgafixe]: https://raw.githubusercontent.com/libmaru/Fixedsys/master/vga/vgafixe.png
[vgafixg]: https://raw.githubusercontent.com/libmaru/Fixedsys/master/vga/vgafixg.png
[vgafixr]: https://raw.githubusercontent.com/libmaru/Fixedsys/master/vga/vgafixr.png
[vgafixt]: https://raw.githubusercontent.com/libmaru/Fixedsys/master/vga/vgafixt.png
[cvgafix]: https://raw.githubusercontent.com/libmaru/Fixedsys/master/vga/cvgafix.png
[hvgafix]: https://raw.githubusercontent.com/libmaru/Fixedsys/master/vga/hvgafix.png
[jvgafix]: https://raw.githubusercontent.com/libmaru/Fixedsys/master/vga/jvgafix.png
[svgafix]: https://raw.githubusercontent.com/libmaru/Fixedsys/master/vga/svgafix.png
[vgaf874]: https://raw.githubusercontent.com/libmaru/Fixedsys/master/vga/vgaf874.png
[vgaf1255]: https://raw.githubusercontent.com/libmaru/Fixedsys/master/vga/vgaf1255.png
[vgaf1256]: https://raw.githubusercontent.com/libmaru/Fixedsys/master/vga/vgaf1256.png
[vgaf1257]: https://raw.githubusercontent.com/libmaru/Fixedsys/master/vga/vgaf1257.png


# Naming Convention

Suffix

    e   Central/Eastern European
    g   Greek
    r   Russian
    t   Turkish

Prefix

    c   Traditional Chinese (Big5)
    h   Korean (Hangul)
    j   Japanese (Shift-JIS)
    s   Simplified Chinese (GB2312)

Code Page

    874     Thai
    1255    Hebrew
    1256    Arabic
    1257    Baltic


# Note

FYI, eXeScope extracts more information than dewinfont.py

Take vgafix for example, eXeScope shows:

    Font No.1
      FontOrdinal: 31
      Version: 512
      Size: 4402
      Copyright: (c) Copyright Bitstream Inc. 1984. All rights reserved.
      Type: 0
      Points: 12
      VertRes: 96
      HorizRes: 96
      Ascent: 12
      InternalLeading: 3
      ExternalLeading: 0
      Italic: 0
      Underline: 0
      StrikeOut: 0
      Weight: 400
      CharSet: 0
      PixWidth: 8
      Pixheight: 15
      PitchAndFamily: 48
      AvgWidth: 8
      MaxWidth: 8
      FirstChar: 32
      LastChar: 255
      DefaultChar: 96
      BreakChar: 0
      WidthBytes: 225
      Device: 0, 
      Face: 4393, Fixedsys

While dewinfont.py shows:

    facename Fixedsys
    copyright (c) Copyright Bitstream Inc. 1984. All rights reserved.
    
    height 15
    ascent 12
    pointsize 12
    
    # italic no
    # underline no
    # strikeout no
    # weight 400
    
    # charset 0


# Copyright

8514fix, 85f874, 85f1257, c8514fix, h8514fix, s8514fix

    Copyright 1987, Microsoft Corporation

85f1255

    (C)Copyright Microsoft 1988-1995.  All rights reserved

85f1256

    (C) 1987 Microsoft Corp and (C) 1992 Glyph Systems, Inc.

8514fixe, 8517fixg, 8514fixr, 8514fixt, vgafixe, vgafixg, vgafixr, vgafixt

    (c) Copyright Microsoft Corp. 1987-95. All rights reserved.

j8514fix, jvgafix

    (c) Copyright Microsoft Corp. 1993. All rights reserved.

vgafix, vgaf874, cvgafix, hvgafix, svgafix

    (c) Copyright Bitstream Inc. 1984. All rights reserved.

vgaf1255

    (c) Copyright Bitstream Inc. 1984 and (c) Kivun 1991-1992

vgaf1256

    (C) 1992 Glyph Systems, Inc. and (C) 1984 Bitstream Inc.

vgaf1257

    (c) Copyright Microsoft Corporation 1985-95. All rights res

dewinfont

    dewinfont is copyright 2001 Simon Tatham. All rights reserved.

    Permission is hereby granted, free of charge, to any person
    obtaining a copy of this software and associated documentation files
    (the "Software"), to deal in the Software without restriction,
    including without limitation the rights to use, copy, modify, merge,
    publish, distribute, sublicense, and/or sell copies of the Software,
    and to permit persons to whom the Software is furnished to do so,
    subject to the following conditions:

    The above copyright notice and this permission notice shall be
    included in all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
    NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
    BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
    ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
    CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
