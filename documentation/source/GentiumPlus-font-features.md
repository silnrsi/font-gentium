---
title: Gentium Plus Font Features
fontversion: 5.960 beta2
---

Gentium Plus is an OpenType-enabled font family that supports the Latin, Cyrillic, and Greek scripts. It includes a number of optional features that may be useful or required for particular uses or languages. These OpenType features are primarily specified using four-letter tags (e.g. 'cv17'), although some applications may provide a direct way to control certain common features such as small caps. This document lists all the available features.

To learn how to access these features for web pages or in individual apps, please see [Using Font Features](Using-font-features.html).

This page uses web fonts (WOFF2) to demonstrate font features and should display correctly in all modern browsers. For a more concise example of how to use Gentium Plus as a web font see [Charis SIL Webfont Example](../web/CharisSIL-webfont-example.html). See [Using SIL Fonts on Web Pages: OpenType and Graphite feature support](http://scripts.sil.org/using_web_fonts#feat) for more information.

*If this document is not displaying correctly a PDF version is also provided.*

## Complete feature list

### Stylistic alternates

#### Small caps from lowercase

<span class='affects'>Affects: all lowercase letters with capital equivalents</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard   | <span class='gentium-dflt-R normal'>a ... z</span> (all letters with capital equivalents) | <span class='code'>smcp=0</span>
Small caps | <span class='gentium-smcp-R normal'>a ... z</span> (all letters with capital equivalents) | <span class='code'>smcp=1</span>

#### Small caps from capitals

<span class='affects'>Affects: all capitals</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard   | <span class='gentium-dflt-R normal'>A ... Z</span> (all capitals) | <span class='code'>c2sc=0</span>
Small caps | <span class='gentium-c2sc-R normal'>A ... Z</span> (all capitals) | <span class='code'>c2sc=1</span>

#### Literacy a and g

<span class='affects'>Affects: U+0061 U+00E0 U+00E1 U+00E2 U+00E3 U+00E4 U+00E5 U+0101 U+0103 U+0105 U+01CE U+01DF U+01E1 U+01FB U+0201 U+0203 U+0227 U+1E01 U+1E9A U+1EA1 U+1EA3 U+1EA5 U+1EA7 U+1EA9 U+1EAB U+1EAD U+1EAF U+1EB1 U+1EB3 U+1EB5 U+1EB7 U+2C65 U+2090 U+1D43 U+0363 U+0067 U+011D U+011F U+0121 U+0123 U+01E7 U+01F5 U+01E5 U+1E21 U+A7A1 U+1D4D</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard     | <span class='gentium-dflt-R normal'>a à á â ã ä å ā ă ą ǎ ǟ ǡ ǻ ȁ ȃ ȧ ḁ ẚ ạ ả ấ ầ ẩ ẫ ậ ắ ằ ẳ ẵ ặ ⱥ ₐ ᵃ ◌ͣ g ĝ ğ ġ ģ ǧ ǵ ǥ ḡ ꞡ ᵍ </span> | <span class='code'>ss01=0</span>
Single-story | <span class='gentium-ss01-R normal'>a à á â ã ä å ā ă ą ǎ ǟ ǡ ǻ ȁ ȃ ȧ ḁ ẚ ạ ả ấ ầ ẩ ẫ ậ ắ ằ ẳ ẵ ặ ⱥ ₐ ᵃ ◌ͣ g ĝ ğ ġ ģ ǧ ǵ ǥ ḡ ꞡ ᵍ </span> | <span class='code'>ss01=1</span>

#### Literacy a (only)

<span class='affects'>Affects: U+0061 U+00E0 U+00E1 U+00E2 U+00E3 U+00E4 U+00E5 U+0101 U+0103 U+0105 U+01CE U+01DF U+01E1 U+01FB U+0201 U+0203 U+0227 U+1E01 U+1E9A U+1EA1 U+1EA3 U+1EA5 U+1EA7 U+1EA9 U+1EAB U+1EAD U+1EAF U+1EB1 U+1EB3 U+1EB5 U+1EB7 U+2C65 U+2090 U+1D43 U+0363</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard     | <span class='gentium-dflt-R normal'>a à á â ã ä å ā ă ą ǎ ǟ ǡ ǻ ȁ ȃ ȧ ḁ ẚ ạ ả ấ ầ ẩ ẫ ậ ắ ằ ẳ ẵ ặ ⱥ ₐ ᵃ ◌ͣ </span> | <span class='code'>ss11=0</span>
Single-story | <span class='gentium-ss11-R normal'>a à á â ã ä å ā ă ą ǎ ǟ ǡ ǻ ȁ ȃ ȧ ḁ ẚ ạ ả ấ ầ ẩ ẫ ậ ắ ằ ẳ ẵ ặ ⱥ ₐ ᵃ ◌ͣ </span> | <span class='code'>ss11=1</span>

#### Literacy g (only)

<span class='affects'>Affects: U+0067 U+011D U+011F U+0121 U+0123 U+01E7 U+01F5 U+01E5 U+1E21 U+A7A1 U+1D4D</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard     | <span class='gentium-dflt-R normal'>g ĝ ğ ġ ģ ǧ ǵ ǥ ḡ ꞡ ᵍ </span> | <span class='code'>ss12=0</span>
Single-story | <span class='gentium-ss12-R normal'>g ĝ ğ ġ ģ ǧ ǵ ǥ ḡ ꞡ ᵍ </span> | <span class='code'>ss12=1</span>

#### Barred-bowl forms 

<span class='affects'>Affects: U+0111 U+0180 U+01E5</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard    | <span class='gentium-dflt-R normal'>đ ƀ ǥ</span> | <span class='code'>ss04=0</span>
Barred-bowl | <span class='gentium-ss04-R normal'>đ ƀ ǥ</span> | <span class='code'>ss04=1</span>

#### Slant italic specials

<span class='affects'>Affects: U+0061 U+00E3 U+00E0 U+00E1 U+00E2 U+00E4 U+00E5 U+0101 U+0103 U+01CE U+01DF U+01E1 U+01FB U+0201 U+0203 U+0227 U+1E01 U+1E9A U+1EA3 U+1EA5 U+1EA7 U+1EA9 U+1EAB U+1EAD U+1EAF U+1EB1 U+1EB3 U+1EB5 U+1EA1 U+1EB7 U+2C65 U+0250 U+00E6 U+0066 U+1E1F U+0069 U+00EC U+00ED U+00EE U+00EF U+0129 U+012B U+012D U+012F U+01D0 U+0209 U+020B U+1E2D U+1E2F U+1EC9 U+1ECB U+0131 U+006C U+013A U+1E37 U+1E39 U+1E3B U+1E3D U+0076 U+1E7D U+1E7F U+007A U+017A U+017C U+017E U+1E91 U+1E93 U+1E95 U+0493 U+04FB U+F327 U+A749 U+A75F U+2097</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='gentium-dflt-I normal'>a ã à á â ä å ā ă ǎ ǟ ǡ ǻ ȁ ȃ ȧ ḁ ẚ ả ấ ầ ẩ ẫ ậ ắ ằ ẳ ẵ ạ ặ ⱥ ɐ æ f ḟ i ì í î ï ĩ ī ĭ į ǐ ȉ ȋ ḭ ḯ ỉ ị ı l ĺ ḷ ḹ ḻ ḽ ꝉ ₗ v ṽ ṿ ꝟ z ź ż ž ẑ ẓ ẕ ғ ӻ  fi ffi</span> | <span class='code'>ss05=0</span>
Slanted  | <span class='gentium-ss05-I normal'>a ã à á â ä å ā ă ǎ ǟ ǡ ǻ ȁ ȃ ȧ ḁ ẚ ả ấ ầ ẩ ẫ ậ ắ ằ ẳ ẵ ạ ặ ⱥ ɐ æ f ḟ i ì í î ï ĩ ī ĭ į ǐ ȉ ȋ ḭ ḯ ỉ ị ı l ĺ ḷ ḹ ḻ ḽ ꝉ ₗ v ṽ ṿ ꝟ z ź ż ž ẑ ẓ ẕ ғ ӻ  fi ffi</span> | <span class='code'>ss05=1</span>

### Character alternates

#### B hook

<span class='affects'>Affects: U+0181</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard        | <span class='gentium-dflt-R normal'>Ɓ</span> | <span class='code'>cv13=0</span>
Lowercase-style | <span class='gentium-cv13-R normal'>Ɓ</span> | <span class='code'>cv13=1</span>

#### D hook

<span class='affects'>Affects: U+018A</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard        | <span class='gentium-dflt-R normal'>Ɗ</span> | <span class='code'>cv17=0</span>
Lowercase-style | <span class='gentium-cv17-R normal'>Ɗ</span> | <span class='code'>cv17=1</span>

#### H stroke

<span class='affects'>Affects: U+0126</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard        | <span class='gentium-dflt-R normal'>Ħ</span> | <span class='code'>cv28=0</span>
Vertical stroke | <span class='gentium-cv28-R normal'>Ħ</span> | <span class='code'>cv28=1</span>

#### J stroke hook

<span class='affects'>Affects: U+0284</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard  | <span class='gentium-dflt-R normal'>ʄ</span> | <span class='code'>cv37=0</span>
Top serif | <span class='gentium-cv37-R normal'>ʄ</span> | <span class='code'>cv37=1</span>

#### Eng

<span class='affects'>Affects: U+014A</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard                          | <span class='gentium-dflt-R normal'>Ŋ</span> | <span class='code'>cv43=0</span>
Lowercase style on baseline       | <span class='gentium-cv43-1-R normal'>Ŋ</span> | <span class='code'>cv43=1</span>
Uppercase style with descender    | <span class='gentium-cv43-2-R normal'>Ŋ</span> | <span class='code'>cv43=2</span>
Alt. lowercase style on baseline  | <span class='gentium-cv43-3-R normal'>Ŋ</span> | <span class='code'>cv43=3</span>

#### N left hook

<span class='affects'>Affects: U+019D</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard        | <span class='gentium-dflt-R normal'>Ɲ</span> | <span class='code'>cv44=0</span>
Lowercase-style | <span class='gentium-cv44-R normal'>Ɲ</span> | <span class='code'>cv44=1</span>

#### Open-O

<span class='affects'>Affects: U+0186 U+0254 U+1D10 U+1D53 U+1D97</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard  | <span class='gentium-dflt-R normal'>Ɔ ɔ ᴐ ᵓ ᶗ</span> | <span class='code'>cv46=0</span>
Top serif | <span class='gentium-cv46-R normal'>Ɔ ɔ ᴐ ᵓ ᶗ</span> | <span class='code'>cv46=1</span>

#### OU

<span class='affects'>Affects: U+0222 U+0223 U+1D3D U+1D15</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='gentium-dflt-R normal'>Ȣ ȣ ᴕ ᴽ</span> | <span class='code'>cv47=0</span>
Open     | <span class='gentium-cv47-R normal'>Ȣ ȣ ᴕ ᴽ</span> | <span class='code'>cv47=1</span>

#### p hook

<span class='affects'>Affects: U+01A5</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard   | <span class='gentium-dflt-R normal'>ƥ</span> | <span class='code'>cv49=0</span>
Right hook | <span class='gentium-cv49-R normal'>ƥ</span> | <span class='code'>cv49=1</span>

####  R tail

<span class='affects'>Affects: U+2C64</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard        | <span class='gentium-dflt-R normal'>Ɽ</span> | <span class='code'>cv55=0</span>
Lowercase-style | <span class='gentium-cv55-R normal'>Ɽ</span> | <span class='code'>cv55=1</span>

#### T hook

<span class='affects'>Affects: U+01AC</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard   | <span class='gentium-dflt-R normal'>Ƭ</span> | <span class='code'>cv57=0</span>
Right hook | <span class='gentium-cv57-R normal'>Ƭ</span> | <span class='code'>cv57=1</span>

#### V hook

<span class='affects'>Affects: U+01B2 U+028B U+1DB9</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard                | <span class='gentium-dflt-R normal'>Ʋ ʋ ᶹ</span> | <span class='code'>cv62=0</span>
Straight with low hook  | <span class='gentium-cv62-1-R normal'>Ʋ ʋ ᶹ</span> | <span class='code'>cv62=1</span>
Straight with high hook | <span class='gentium-cv62-2-R normal'>Ʋ ʋ ᶹ</span> | <span class='code'>cv62=2</span>

#### Y hook

<span class='affects'>Affects: U+01B3</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard  | <span class='gentium-dflt-R normal'>Ƴ</span> | <span class='code'>cv68=0</span>
Left hook | <span class='gentium-cv68-R normal'>Ƴ</span> | <span class='code'>cv68=1</span>

#### Ezh

<span class='affects'>Affects: U+01B7 U+04E0</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard       | <span class='gentium-dflt-R normal'>Ʒ Ӡ</span> | <span class='code'>cv20=0</span>
Reversed sigma | <span class='gentium-cv20-R normal'>Ʒ Ӡ</span> | <span class='code'>cv20=1</span>

#### ezh curl

<span class='affects'>Affects: U+0293</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard   | <span class='gentium-dflt-R normal'>ʓ</span> | <span class='code'>cv19=0</span>
Large bowl | <span class='gentium-cv19-R normal'>ʓ</span> | <span class='code'>cv19=1</span>

#### rams horn

<span class='affects'>Affects: U+0264</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard    | <span class='gentium-dflt-R normal'>ɤ</span> | <span class='code'>cv25=0</span>
Large bowl  | <span class='gentium-cv25-1-R normal'>ɤ</span> | <span class='code'>cv25=1</span>
Small gamma | <span class='gentium-cv25-2-R normal'>ɤ</span> | <span class='code'>cv25=2</span>

### Diacritic and symbol alternates

<!-- Not included because the feature is not working properly

#### Low-profile diacritics  [ss07]

<span class='affects'>Affects: U+0300 U+0301 U+0302 U+0303 U+0304 U+0307 U+0308 U+030C</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard    | <span class='gentium-dflt-R normal'>anything with ◌́◌̀◌̂◌̌◌̄◌̃◌̈◌̇ (áàâǎāãäȧ)</span> | <span class='code'>ss07=0</span>
Low-profile | <span class='gentium-ss07-R normal'>anything with ◌́◌̀◌̂◌̌◌̄◌̃◌̈◌̇ (áàâǎāãäȧ)</span> | <span class='code'>ss07=1</span>

-->

#### Vietnamese-style diacritics

<span class='affects'>Affects: U+1EA4 U+1EA5 U+1EA6 U+1EA7 U+1EA8 U+1EA9 U+1EAA U+1EAB U+1EAE U+1EAF U+1EB0 U+1EB1 U+1EB2 U+1EB3 U+1EB4 U+1EB5 U+1EBE U+1EBF U+1EC0 U+1EC1 U+1EC2 U+1EC3 U+1EC4 U+1EC5 U+1ED0 U+1ED1 U+1ED2 U+1ED3 U+1ED4 U+1ED5 U+1ED6 U+1ED7</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard         | <span class='gentium-dflt-R normal'>Ấấ Ầầ Ẩẩ Ẫẫ Ắắ Ằằ Ẳẳ Ẵẵ Ếế Ềề Ểể Ễễ Ốố Ồồ Ổổ Ỗỗ</span> | <span class='code'>cv75=0</span>
Vietnamese-style | <span class='gentium-cv75-R normal'>Ấấ Ầầ Ẩẩ Ẫẫ Ắắ Ằằ Ẳẳ Ẵẵ Ếế Ềề Ểể Ễễ Ốố Ồồ Ổổ Ỗỗ</span> | <span class='code'>cv75=1</span>

#### Kayan diacritics

<span class='affects'>Affects: U+0300 U+0301</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard     | <span class='gentium-dflt-R normal'>◌̀́</span> | <span class='code'>cv79=0</span>
Side by side | <span class='gentium-cv79-R normal'>◌̀́</span> | <span class='code'>cv79=1</span>

#### Ogonek

<span class='affects'>Affects: U+0328 U+0104 U+0105 U+0118 U+0119 U+012E U+012F U+0172 U+0173 U+01EA U+01EB U+01EC U+01ED</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='gentium-dflt-R normal'>anything with ◌̨ (Ąą Ęę Įį Ųų Ǫǫ Ǭǭ)</span> | <span class='code'>cv76=0</span>
Straight | <span class='gentium-cv76-R normal'>anything with ◌̨ (Ąą Ęę Įį Ųų Ǫǫ Ǭǭ)</span> | <span class='code'>cv76=1</span>

#### Caron

<span class='affects'>Affects: U+010F U+013D U+013E U+0165</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard     | <span class='gentium-dflt-R normal'>ď Ľ ľ ť</span> | <span class='code'>cv77=0</span>
Global-style | <span class='gentium-cv77-R normal'>ď Ľ ľ ť</span> | <span class='code'>cv77=1</span>

#### Modifier apostrophe

<span class='affects'>Affects: U+02BC U+A78B U+A78C</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='gentium-dflt-R normal'>ʼ Ꞌ ꞌ</span> | <span class='code'>cv70=0</span>
Large    | <span class='gentium-cv70-R normal'>ʼ Ꞌ ꞌ</span> | <span class='code'>cv70=1</span>

#### Modifier colon

<span class='affects'>Affects: U+A789</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='gentium-dflt-R normal'>꞉</span> | <span class='code'>cv71=0</span>
Expanded | <span class='gentium-cv71-R normal'>꞉</span> | <span class='code'>cv71=1</span>

#### Empty set

<span class='affects'>Affects: U+2205</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard   | <span class='gentium-dflt-R normal'>∅</span> | <span class='code'>cv98=0</span>
Zero-style | <span class='gentium-cv98-R normal'>∅</span> | <span class='code'>cv98=1</span>

### Cyrillic alternates

*There are also Cyrillic characters affected by the “Ezh” and “Small capitals” features. Some languages may also use the “Modifier apostrophe”.*

#### Cyrillic E

<span class='affects'>Affects: U+042D U+044D</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard        | <span class='gentium-dflt-R normal'>Э э</span> | <span class='code'>cv80=0</span>
Mongolian-style | <span class='gentium-cv80-R normal'>Э э</span> | <span class='code'>cv80=1</span>

#### Cyrillic shha

<span class='affects'>Affects: U+04BB</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard        | <span class='gentium-dflt-R normal'>һ</span> | <span class='code'>cv81=0</span>
Uppercase-style | <span class='gentium-cv81-R normal'>һ</span> | <span class='code'>cv81=1</span>

#### Cyrillic breve

<span class='affects'>Affects: U+0306</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard       | <span class='gentium-dflt-R normal'>anything with ◌̆ (Ә̆ә̆)</span> | <span class='code'>cv82=0</span>
Cyrillic-style | <span class='gentium-cv82-R normal'>anything with ◌̆ (Ә̆ә̆)</span> | <span class='code'>cv82=1</span>

#### Serbian Cyrillic alternates

*These alternate forms mainly affect italic styles. Unlike other features this is activated by tagging the span of text as being in the Serbian language.*

<span class='affects'>Affects: U+0431 U+0433 U+0434 U+043F U+0442</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='gentium-dflt-I normal'>б г д п т</span> | <span class='code'></span>
Serbian  | <span class='gentium-dflt-I normal' lang='sr'>б г д п т</span> | <span class='code'>lang='sr'</span>

### Greek alternates

#### Porsonic circumflex

<span class='affects'>Affects: U+0342 U+1F06 U+1F07 U+1F0E U+1F0F U+1F26 U+1F27 U+1F2E U+1F2F U+1F36 U+1F37 U+1F3E U+1F3F U+1F56 U+1F57 U+1F5F U+1F66 U+1F67 U+1F6E U+1F6F U+1F86 U+1F87 U+1F8E U+1F8F U+1F96 U+1F97 U+1F9E U+1F9F U+1FA6 U+1FA7 U+1FAE U+1FAF U+1FB6 U+1FB7 U+1FC0 U+1FC1 U+1FC6 U+1FC7 U+1FCF U+1FD6 U+1FD7 U+1FDF U+1FE6 U+1FE7 U+1FF6 U+1FF7</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard       | <span class='gentium-dflt-R normal'>◌͂ ◌῀ ◌῁  ◌῏  ◌῟  ἆ ἇ ᾆ ᾇ ᾶ ᾷ ἦ ἧ ᾖ ᾗ ῆ ῇ ἶ ἷ ῖ ῗ ὖ ὗ ῦ ῧ ὦ ὧ ᾦ ᾧ ῶ ῷ Ἆ Ἇ ᾎ ᾏ Ἦ Ἧ ᾞ ᾟ Ἶ Ἷ Ὗ Ὦ Ὧ ᾮ ᾯ</span> | <span class='code'>cv78=0</span>
Porsonic-style | <span class='gentium-cv78-R normal'>◌͂ ◌῀ ◌῁  ◌῏  ◌῟  ἆ ἇ ᾆ ᾇ ᾶ ᾷ ἦ ἧ ᾖ ᾗ ῆ ῇ ἶ ἷ ῖ ῗ ὖ ὗ ῦ ῧ ὦ ὧ ᾦ ᾧ ῶ ῷ Ἆ Ἇ ᾎ ᾏ Ἦ Ἧ ᾞ ᾟ Ἶ Ἷ Ὗ Ὦ Ὧ ᾮ ᾯ</span> | <span class='code'>cv78=1</span>

#### Capital adscript iota (prosgegrammeni)

<span class='affects'>Affects: U+1F88 U+1F89 U+1F8A U+1F8B U+1F8C U+1F8D U+1F8E U+1F8F U+1F98 U+1F99 U+1F9A U+1F9B U+1F9C U+1F9D U+1F9E U+1F9F U+1FA8 U+1FA9 U+1FAA U+1FAB U+1FAC U+1FAD U+1FAE U+1FAF U+1FBC U+1FCC U+1FFC</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard        | <span class='gentium-dflt-R normal'>ᾼ ᾈ ᾉ ᾊ ᾋ ᾌ ᾍ ᾎ ᾏ ῌ ᾘ ᾙ ᾚ ᾛ ᾜ ᾝ ᾞ ᾟ ῼ ᾨ ᾩ ᾪ ᾫ ᾬ ᾭ ᾮ ᾯ</span> | <span class='code'>cv83=0</span>
Subscript (ypogegrammeni) | <span class='gentium-cv83-R normal'>ᾼ ᾈ ᾉ ᾊ ᾋ ᾌ ᾍ ᾎ ᾏ ῌ ᾘ ᾙ ᾚ ᾛ ᾜ ᾝ ᾞ ᾟ ῼ ᾨ ᾩ ᾪ ᾫ ᾬ ᾭ ᾮ ᾯ</span> | <span class='code'>cv83=1</span>

#### beta

<span class='affects'>Affects: U+03B2 U+1D66 U+1D5D</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard    | <span class='gentium-dflt-R normal'>β ᵝ ᵦ</span> | <span class='code'>cv14=0</span>
With serifs | <span class='gentium-cv14-R normal'>β ᵝ ᵦ</span> | <span class='code'>cv14=1</span>

### Tone alternates

#### Chinantec tones

<span class='affects'>Affects: U+02CB U+02C8 U+02C9 U+02CA</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard        | <span class='gentium-dflt-R normal'>ˋ ˈ ˉ ˊ</span> | <span class='code'>cv90=0</span>
Chinantec-style | <span class='gentium-cv90-R normal'>ˋ ˈ ˉ ˊ</span> | <span class='code'>cv90=1</span>

#### Tone numbers

<span class='affects'>Affects: U+02E5 U+02E6 U+02E7 U+02E8 U+02E9 U+A712 U+A713 U+A714 U+A715 U+A716</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='gentium-dflt-R normal'>˥ ˦ ˧ ˨ ˩ ꜒ ꜓ ꜔ ꜕ ꜖</span> | <span class='code'>cv91=0</span>
Numbers  | <span class='gentium-cv91-R normal'>˥ ˦ ˧ ˨ ˩ ꜒ ꜓ ꜔ ꜕ ꜖</span> | <span class='code'>cv91=1</span>

<!-- Not currently working
#### Hide tone contour staves

<span class='affects'>Affects: U+02E5 U+02E6 U+02E7 U+02E8 U+02E9 U+A712 U+A713 U+A714 U+A715 U+A716</span>

Feature | Sample                      | Feature setting
------- | --------------------------- | -------
Standard | <span class='gentium-dflt-R normal'>˥ ˦ ˧ ˨ ˩ ꜒ ꜓ ꜔ ꜕ ꜖ (˩˦˥˧˨ ꜖꜓꜒꜔꜕)</span> | <span class='code'>cv92=0</span>
Numbers  | <span class='gentium-cv92-R normal'>˥ ˦ ˧ ˨ ˩ ꜒ ꜓ ꜔ ꜕ ꜖ (˩˦˥˧˨ ꜖꜓꜒꜔꜕)</span> | <span class='code'>cv92=1</span>
-->