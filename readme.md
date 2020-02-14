# GameWiki

> A small python personal wiki using markdown, designed for speed and simplicity, especially during tabeltop rpg sessions.

## Development Requirements

* Python 3
* PyQT 5
* `pip install markdown`
* `pip install html2markdown`
* `pip install pyinstaller`
* build: `pyinstaller app.py`
  * Have to move `resources` & `.ui` file to `dist` after package

## Docs & notes

* https://doc.qt.io/qt-5/qtextedit.html#reimplemented-protected-functions
  * Specifically the mouse events section
* Possibly switch to qPlainTextEdit for speed and lack of default commands?
* Implement markdown blocks as commands?
* reimplement tokenizer to keep md markup, hide and show on entry, like typora?

## Algorithm for markdown parsing

* 3-phase approach: completely split parsing into 3 separate functions *that define discrete spaces*
  * Container Parser
    * Parses line for *container* style markup *only*
    * Creates a visible container on screen, like a box
  * Block Parser
    * Parses line to find its *block* type
    * Restyles block as needed
      * Possibly changes block type or replaces it
      * Possibly restyles it via css
  * Inline Parser
    * 