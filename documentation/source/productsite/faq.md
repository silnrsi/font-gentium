
Many questions can be answered by consulting the following FAQ pages. Here are a few sample questions answered in each FAQ:

- [SIL fonts in general](https://software.sil.org/fonts/faq)
    - *How can I type...?*
    - *How can I use font features?*
    - *Will you add support for character...?*
    - *Will you add support for script...?*
    - *WIll you help me...?*

- [SIL’s Latin, Cyrillic, and Greek fonts](https://software.sil.org/lcgfonts/faq).
    - *How can I type IPA symbols?*
    - *How do I use both a single-story and double-story 'a' in italic?*
    - *Why don’t my diacritics position properly?*
    - *Why is the line spacing so much looser than other fonts?*
    - *I’ve updated my font to the latest version and some letters have become black boxes with white letters - why?*

- [The SIL Open Font License (OFL-FAQ)](https://openfontlicense.org/ofl-faq)
    - *Can I use this font for...?*
    - *Can I modify the font and then include it in...*
    - *If I use the font on a web page do I have to include an acknowledgement?*
    - The full OFL-FAQ.txt is also included in the font package.

Here are a few of the most frequently asked questions specifically regarding Gentium:

#### *How do you pronounce Gentium?*

The preferred pronunciation is with a soft G as in ‘general’, not a hard one as in ‘gold’: JEN-tee-oom.

#### *Why did you change the font family name from Gentium Plus to only Gentium?*

The version 7 reduction of default line spacing and addition of kerning would have caused most documents that used Gentium Plus to reflow. This would have caused significant pain for users who wanted to use the new version but also had large collections of existing documents that would reflow. Changing the name to only Gentium allows both old and new font families to be installed at the same time and eases the transition to the new version.

#### *Is Gentium Plus better than Gentium?*

No—the current Gentium has more weights, features, and character support than the old Gentium Plus. Yes—this is confusing now but is better for the future.

#### *Why did you stop producing Compact versions?*

Improvements to both these fonts and industry font technology has reduced the need for *Compact* versions. The reduced default line spacing in v7 is close to that of the *Compact* versions. This enables many users of *Compact* variants to switch to using the standard fonts, and allows documents to be shared without requiring special fonts. If tight or loose line spacing is needed the best solution is to use the standard fonts and explicitly set the line spacing in your application. If the application does not allow user-specified line spacing the [v6.2 Compact fonts remain available](https://software.sil.org/lcgfonts/download/). Please also contact the app developer to request that they give users better control over line spacing.

#### *Where are the Literacy versions?*

We have not prepared ‘pre-tuned’ *Literacy* versions of the version 7 fonts. The standard fonts include the literacy forms, which can be turned on in many applications and on web pages using OpenType stylistic sets (`ss01`, `ss11`, `ss12`) — see [Using Font Features](https://software.sil.org/fonts/features) and [Using SIL Fonts on Web Pages](https://software.sil.org/fonts/webfonts). If your application does not allow you to control these features the [v6.2 Literacy fonts remain available](https://software.sil.org/lcgfonts/download/). Please also contact the app developer to request that they give users access to OpenType stylistic sets.

#### *Is there a guide to the many versions of Gentium and its variants?*

Yes! See the [Versions](versions) page.

#### *Why does my application not show the Bold weight in font menus and dialogs?*

Some applications will list all the weights but leave out Bold. To access the Bold you need to choose Regular and turn on Bold using the application’s UI controls such as a “B” button. See our [Font Help Guide on Axis-Based Font Families](https://software.sil.org/fonts/axis-based-fonts/) for more information.

#### *Why do I sometimes get a fake Bold?*

If you choose a weight other than Regular (such as Medium), and then use application controls to turn on Bold, some applications will make a “fake” Bold rather than use one of the real ones in the font (Bold, ExtraBold). This is because only Regular has an associated Bold counterpart. This is a technical limitation with some apps and OSes. If you are using a weight other than Regular for text and want to make a word or phrase stand out, you will need to select the text and apply one of the heavier weights manually. See our [Font Help Guide on Axis-Based Font Families](https://software.sil.org/fonts/axis-based-fonts/) for more information.

#### *Where is the heavier-weight Book family?*

Gentium Book is an alternate font family that is slightly heavier overall. Gentium Book Regular is the same weight as Gentium Medium. This family is no longer included in the main Gentium package—it is available as a [separate download package](https://software.sil.org/gentium/download/). 

#### *What was GentiumAlt?*

It was a version of the font with redesigned diacritics (flatter ones) to make it more suitable for use with stacking diacritics. It is no longer supported or needed, but is included in the very early versions of Gentium. See the [Previous Versions archive](https://software.sil.org/gentium/download/previous-versions/).

#### *Where are the Basic fonts (Gentium Basic, Gentium Book Basic)?*

These font families were based on the original Gentium design, but with limited character set support. They are no longer supported or needed. Gentium includes support for all the characters and styles supported by the Basic fonts. The fonts remain available from the [Previous Versions archive](https://software.sil.org/gentium/download/previous-versions/).

#### *Why are the Basic fonts no longer supported? I need them because the font files are smaller in size than the full Gentium.*

Font size is less of a concern than when the Basic fonts were introduced in 2008. New compression technologies have also reduced the size of the fonts, particularly for web use. For example, Gentium Basic Regular (TrueType) was 264K. The current Gentium Regular (WOFF2)—which contains six times the glyphs—is only 347K. If you still feel that font size is a significant concern please [contact us](https://software.sil.org/gentium/about/contact/). We may be able to point you to techniques that can reduce the size impact even further depending on your particular situation.

#### *Do you plan to add sans-serif font to go with Gentium?*

There is a definite need for a sans-serif font that shares some of Gentium’s strengths—high readability, economy of space, etc. It would also be great if that font also harmonized well with Gentium. We don’t currently have any plans for a companion face, although one of our other projects—[Andika](https://software.sil.org/andika/)—may be useful. Andika is a sans-serif font designed specifically for use in literacy programs around the world, and is available from our web site.

#### *Will you be extending Gentium to cover other scripts, and Hebrew in particular?*

It is unlikely that we would do this as our focus remains the Latin, Greek, and Cyrillic scripts. We might welcome contributed expansions to other scripts that are potentially compatible with the general Gentium design, such as Armenian. If you are interested in making such a contribution please see the [Developer page](developer) or [contact us](https://software.sil.org/gentium/about/contact/).
