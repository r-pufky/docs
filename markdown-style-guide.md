Markdown Documentation Style Guide
==================================
Covers the standard way to write documentation using markdown that is easily
consumable on both a command line and via a rendered page, with minimal
formatting / control interruptions.

1. [Markdown File Structure](#markdown-file-structure)
1. [Sections](#sections)
1. [Writing](#writing)
1. [Code/File/Commands](#code-file-commands)
1. [GUI Interactions](#gui-interactions)
1. [Windows Specific Instructions](#windows-specific-instructions)

Markdown File Structure
-----------------------
* Always save _unix_ endings.
* Always hard-wrap at _80 characters_. Exceptions:
  * Multi-line code blocks (**not** inline \`\` code blocks).
  * File listings in blocks.
  * URI's (used in the markdown link, not the link text itself).
  * Table contents.
  * TOC inline links.
  * Image links.
* Keep document focused. If sections get excessively long, cut section into a
  separate file and link.
* _README.md_ per directory level. This allows the directory to express context
  and github to render the file in the subdirectory.
* Sub-documents are _lower-with-dashes.md_.
* See [Github Flavored Markdown][j3] for markdown langauge definitions.

### Markdown callouts
Only for Style Guide. Use four backticks to create an non-interpreted pure text
code block for examples. This is effectively the same as a block, but allows for
the display of markdown control characters to be displayed on github. Follow up
the block with the actual interpreted markdown block to show the difference
between the two.

````
/example/file/path.txt `root:root 0750`
```text
some example text file listing
```
````

/example/file/path.txt `root:root 0750`
```text
some example text file listing
```

Sections
--------
* Content starts immediately after header, no vertical space.
* One vertical space before a new section.
* Title sections use `===` (equivalent to `#`) as a visual separator, matching
  to text length.
* Top-level sections use `---` (equivalent to `##`) as a visual separator,
  matching to text length.
* All other sections use `#` (### - ######).
* Table of Contents (TOC) must list all top-level sections; optionally 1-2
  levels of sub-sections. If more levels are required, the document probably
  needs a re-write. Title sections optional.

### Deprecated Documents
Used to keep documents for reference even though it is not actively deployed.

* Place a _deprecated_ line below the title header. Add a single vertical space
  between the _deprecated_ line and original content.
* Place a _deprecated_ line above the references. Place above the _template_
  link if the document is a templated document. Vertical spaces on both sides of
  the _deprecated_ line.
* If a _template_ line is present, no vertical spaces between _deprecated_ and
  _template_ lines.

Deprecated Line
* Deprecated in all caps, bold. No trailing period.
* If alternative link, add colon (`:`) then link reference with a period.
````
Example Title
=============
**DEPRECATED**: See [Alternative Reference][XX].

...

**DEPRECATED**: See [Alternative Reference][XX].

[XX]:
````

### Templated Documents
Documents using some standard template such as a service.

* _template_ link is inserted between _deprecated_ line and above references.
  Add one vertical space above and below the _template_ link.
* If a _deprevation_ line is present do not use vertical spaces between
  _deprecated_ and _template_ lines.

Template Line
* link to the template version at the bottom of the document.
* Separate the document using at sign (`@`) then the commit version.
* Specify the github commit version in the tag as well as the link.
````

[template.md@323434b2][XX]

...

[XX]: raw.gihub.com/master/323434b2/template.md
````

Writing
-------
* Be consistent.
* Active first-person short sentences are best.
* Continue a link-break sentence at the start of the next line. A space will be
  inserted automatically with github, and mentally on the CLI.
* Actions a user should enter or submit should be done inline or with block
  segments (\`\` or \`\`\`).
* References to other content not requiring a user action should be Italics.
  e.g. the program _bananas_ has method _jingles_.
* Bold should used sparringly and for criticla information. Do not overuse.
* Define Acronyms on first use and include a link if deemed necessary.
* Numbered lists should always be `1.`. This allows for easy modification of
  lists without the need to change pre-existing text.
* Numbered list imply a required order. Unnumbered do not. Use appropriately.
* Vertical spacing. Use _one vertical space_ between ideas in the same section
  as warranted. Follow [Sections][Ag] guidance for section spacing.

> :warning:  
> Remember, two trailings spaces indicate a hard line break. Anything less is
> intrepreted as a soft break.

### Sentences
1. Cap first letter.
1. Always periods. Even in lists. Exceptions:
   * `:` if following item is another list.
   * Checkbox lists, if they are using checkbox markdown `[ ]` `[x]`.
1. Acronyms always CAPPED.
1. Issued commands always block qouted '\`'; **not** capped starting sentence.
1. Sentences single spaced.

### Definitions
Used to define terminology for later usage.

1. Bold Acronym or word.
1. If Acronym, Follow immediatel with a colon (:) and the expanded word, Bolding
   letters used for the acronym.
1. Write the definition directory below in quotes.

````
**PIF**: **P**hysical **I**nter**f**ace.
> This defines the physical port of a piece of equipment. Also referred to as
> **Native Network**, **Parent VLAN**.
````

**PIF**: **P**hysical **I**nter**f**ace.
> This defines the physical port of a piece of equipment. Also referred to as
> **Native Network**, **Parent VLAN**.

### Emojis
Simplified emojis are allowed if they convey appropriate meaning within the
[emoji text][df]. Placed at the beginning of new thought sections or within
_quoted blocks_.

Current acceptable emoji's are:

| emoji             | code            | context                             |
|-------------------|-----------------|-------------------------------------|
| :warning:         | warning         | Consequences for actions.           |
| :question:        | question        | Unanswered questions/interactions.  |
| :star:            | star            | Callout.                            |
| :exclamation:     | exclamation     | User should be cautious.            |
| :skull:           | skull           | Bad / breaking results.             |
| :trollface:       | trollface       | Gotchas and general shittiness.     |
| :+1:              | +1              | Good idea.                          |
| :-1:              | -1              | Bad idea.                           |
| :thought_balloon: | thought_balloon | User should consider independently. |
| :floppy_disk:     | floppy_disk     | Save data.                          |
| :key:             | key             | Crypto/passwords/lock/unlock.       |
| :memo:            | memo            | User should take a note here.       |
| :no_entry_sign:   | no_entry_sign   | Do not proceed.                     |

### Callouts / Quotes
Inserts a vertical bar directing additional attention for third-person comments
on documentation itself.

* Emoji's allowed at the begining of block, see [allowed emojis][3g].
* One-line blocks with and without emojis are allowed.
* Additional formatting is allowed within the quote block.

````
> :warning:  
> This can be useful to callout specific context or warnings.
````

> :warning:  
> This can be useful to callout specific context or warnings.

````
> :key:  
> Generate your password with `gpg --gen-random -a 0 64`
````

> :key:  
> Generate your password with `gpg --gen-random -a 0 64`

````
```bash
echo 'hello world' > $TEST; export $TEST
```
> :memo:
> * Creates an environment variable _test_.
> * _test_ may be something else.
````

```bash
echo 'hello world' > $TEST; export $TEST
```
> :memo:
> * Creates an environment variable _test_.
> * _test_ may be something else.

### Emphasis
__Italics__: Always **underscores** `_italics_`.
* Allows for nested, distinguished formatting. `**bold _italics_ text**`.

**Bold**: Always **double asterisk** `**bold**`.
* Allows for nested, distinguished formatting. `**bold _italics_ text**`.

Strikethrough: **double tildes**. `~~strikethrough~~`.
* Allows for nested, distinguished formatting. `**bold ~~strikethrough~~**`.

### Tables
Tables are encased to present formatted data on both github and CLI.

* Full table formatting required.
* One space buffer on either side of data required.
* Pipes should be aligned.
* Line-breaking not enforced.

````
| test      | table  | example         |
|-----------|--------|-----------------|
| a         | b      | c               |
| it's      | good   | spacing         |
| long data | forces | table expansion |
````

| test      | table  | example         |
|-----------|--------|-----------------|
| a         | b      | c               |
| it's      | good   | spacing         |
| long data | forces | table expansion |

### Images
Always prefer written text to pictures. Pictures allowed for cases where it not
easily understandable, or is specifically a GUI element. Pictures generally tend
to get outdated quickly with UI updates and changes, leading to confusion
wherein text with the intent of the change will carry through these changes.
Pictures are also not so useful on the command line.

* One vertical separator above the image.
* Image stored locally within the repository itself.
* Image linked directly with no line breaks.
* Alternative text should be sufficient to understand the context of the image.
* Vertical separator below image optional dependent on usage.
* Text may be used in the alt text field to represent what is happening in the
  image. Separate with a vertical space.

````
![Example](example.png)
````

![Example](example.png)

````
![
+------+            +--------+
|      | +--------> |PIF ALL +---------->
|      |  untagged  |VIF 20  | untagged
+------+            +--------+
](example.png)
````

![
+------+            +--------+
|      | +--------> |PIF ALL +---------->
|      |  untagged  |VIF 20  | untagged
+------+            +--------+
](example.png)


### Linking
1. TOC links are inline. No line-wrapping.
1. All other links are reference text links at bottom of document, regardless of
   length or targets.

#### Reference Text
Optimized to handle modification post-creation.

1. use `[XX]` where XX is a unique two digit alpha-numeric hash ([1260][kl]
   possible links in a single doc).
1. Unused reference / context links:
   * Below reference text links.
   * One vertical space.
   * Format `[refXX]`.

Code/File/Commands
------------------
Content should be visually distinguished from the rest of the document for clear
interpretation of what is going on.

### Variables & User Data
Custom user data that should not be included in documentation, like passwords,
per user accounts, and other potentially sensitive information.

1. Use brackets `{}` with `CAPPED SPACES` to describe data to enter.
1. No backticks (\`) should be used, as this is not data the user should
   directly enter. The user needs to contextualize the notation _then_ enter
   data.

```
{VARIBLE DATA HERE}
```

Current acceptable abbreviations:

| Abbreviation | Word     |
|--------------|----------|
| PW           | Password |
| USER         | Username |

### All Blocks
A block is a strong callout for a single line, or a multi-line example. All
blocks have:
* One vertical space before start.
* Context helper in header block.
* Top-level indenting is stripped, so that characters start at X postiion 0 in
  the markdown document, maximizing space avaliable for content.
* One trailing vertical space at the end.
* Header text requires trailing colon(`:`) if it is a statement.

````
Some statement explaining context:
```text
some content

  starting with some additional space
multi-line
```
````

Some statement explaining context:
```text
some content

  starting with some additional space
multi-line
```

### Files
* Formatting per [all blocks style][sT].
* List file full path with octal permissions in inline block above.

````
/example/file/path.txt `root:root 0750`
```text
some example text file listing
```
````

/example/file/path.txt `root:root 0750`
```text
some example text file listing
```

````
`sudo crontab -e`
```bash
@reboot sleep 15; /sbin/sysctl -p
```
````

`sudo crontab -e`
```bash
@reboot sleep 15; /sbin/sysctl -p
```

#### Modifying File Lines
* If the purpose of the listing is to show lines to be modified, a single line
  may be shown to reflect those changes.
* Multiple lines changes in a file should be vertically separated with `...`.

````
/some/yaml/file.yaml `root:root 0750`
```yaml
one_line_change=XXXX
...
another_change=XXX
...
additional_change=YYY
```
````

/some/yaml/file.yaml `root:root 0750`
```yaml
one_line_change=XXXX
...
another_change=XXX
...
additional_change=YYY
```

### Commands
* Formatting per [all blocks style][sT].
* Context helper in header block for command shell type.
* Inline blocks are allowed.
* Never include user/permission elevation in command context (e.g. `sudo`),
  unless is functionally required (e.g. in a bash script). This adds to the
  length of the instruction without adding value. If the user should be
  operating in a different user context, call it out explicitly above or below
  the block.

````
```bash
ifconfig
```
````

```bash
ifconfig
```

````
```powershell
ipconfig
```
````

```powershell
ipconfig
```

### Code
* Formatting per [all blocks style][sT].
* Context helper in header block for language.
* inline blocks are allowed.

````
```python
def SomeMethod():
```
````

```python
def SomeMethod():
```

GUI Interactions
----------------
### Mouse
* Left-click action is an capped case inline code block. `Click`.
* Right-click action is an capped case inline code block. `Right Click`.

### Checkboxes
Use built in check/unchecked boxes with the GUI labels. No trailing peroids.

````
- [ ] option one
- [x] option two
````

- [ ] option one
- [x] option two

#### Indentation changes
Using checkboxes inline with numbered or unnumbered lists requires slight
adjustments for proper indentation during rendering. Indent one level more than
normal for checkboxes and sub-items in checkboxes for proper alignment.

```
* Internet (`eth3/SFP`)
    - [x] Static IP
        * Address: {YOUR PUBLIC IP} / {PUBLIC IP NETMASK}
        * Gateware: {YOUR ISP GATEWAY}
        * DNS: `1.1.1.1`
    - [ ] Internet connection is on VLAN
```

* Internet (`eth3/SFP`)
    - [x] Static IP
        * Address: {YOUR PUBLIC IP} / {PUBLIC IP NETMASK}
        * Gateware: {YOUR ISP GATEWAY}
        * DNS: `1.1.1.1`
    - [ ] Internet connection is on VLAN

### Section Headers
Use no `:` and indent the section like a standard list.

````
* Section Header 1
  * Data Key: `Data`
* Section Header 2
  - [x] Some Checkbox
````

* Section Header 1
  * Data Key: `Data`
* Section Header 2
  - [x] Some Checkbox

### Use Click/tab chains as a section header.
Any chain containing a click sequence or tabbed menu sequence to get to a GUI
window should be in it's own section, using backticks (\`) to denote user input.

````
#### `Dashboard > eth1 > Actions > Config`
* ...
````

#### `Dashboard > eth1 > Actions > Config`
* ...


Windows Specific Instructions
-----------------------------
* Windows key is `win`.
* Start menu is `start`.

### Group Policy Editor
* Always specify the shortcut key to launch group policy editor.
* List the full key using emoji shortcut with inline code block for the full
  path with a hard break.
* Add policy changes in _italics_ with the setting in another inline code block,
  with another hard line break.
* The last policy for a key does not need a hard line break.
* Separate keys with one veritical space.

````
`win + r > gpedit.msc`
> :key:: `Computer Configuration > Administrative Templates`  
> _Some awesome policy_ = `Enabled`

> :key:: ``Computer Configuration > Windows Components`  
> _Component policy A_ = `Enabled`  
> _Component policy B_ = `Disabled`
````

`win + r > gpedit.msc`
> :key:: `Computer Configuration > Administrative Templates`  
> _Some awesome policy_ = `Enabled`

> :key:: `Computer Configuration > Windows Components`  
> _Component policy A_ = `Enabled`  
> _Component policy B_ = `Disabled`

### Registry Editor
Running in an adminstrator context is required to modify system settings.

* Always specify the start menu and search keyword with privlege context in
  parens following.
* List the full key using emoji shortcut with inline code block for the full
  path.
* Add one vertical quote space separator. Table require a empty line above them
  to render correctly, even in a quote block.
* Add table containing Type, Name, Value for registry keys.
* Separate keys with one veritical space.

````
`start > regedit` (as admin)
> :key:: `HKEY_CLASSES_ROOT\CLSID\KEY`
>
> | Type  | Name  | Value |
> |-------|-------|-------|
> | DWORD | MyKey | 0     |

> :key:: `HKEY_CLASSES_ROOT\CLSID\OTHER\KEY`
>
> | Type  | Name     | Value |
> |-------|----------|-------|
> | DWORD | OtherKey | 0     |
````

`start > regedit` (as admin)
> :key:: `HKEY_CLASSES_ROOT\CLSID\KEY`
>
> | Type  | Name  | Value |
> |-------|-------|-------|
> | DWORD | MyKey | 0     |

> :key:: `HKEY_CLASSES_ROOT\CLSID\OTHER\KEY`
>
> | Type  | Name     | Value |
> |-------|----------|-------|
> | DWORD | OtherKey | 0     |

### Task Scheduler
* Always specify the shortcut key to launch group policy editor.
* List the full key using emoji shortcut with inline code block for the full
  path with a hard break.
* Add tasks changes in _italics_ with the setting in another inline code block,
  with another hard line break.
* The last policy for a key does not need a hard line break.
* Separate keys with one veritical space.

````
`start > Task Scheduler`
> :key:: `Task Scheduler Library > OneDrive Standalone Update Task v2`  
> `Right Click > Disabled`
````

`start > Task Scheduler`
> :key:: `Task Scheduler Library > OneDrive Standalone Update Task v2`  
> `Right Click > Disabled`

[Ag]: #sections
[df]: https://www.webfx.com/tools/emoji-cheat-sheet/
[3g]: #emojis
[sT]: #all-blocks
[j3]: https://github.github.com/gfm/
[kl]: https://math.stackexchange.com/questions/1331664/combinations-of-two-character-alphanumeric-how-many

[refjE]: https://help.github.com/categories/writing-on-github/
[refDD]: https://guides.github.com/features/mastering-markdown/
[refos]: https://daringfireball.net/projects/markdown/syntax#code