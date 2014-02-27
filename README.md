rsvp-reader
===========

Lightweight Rapid Serial Visual Presentation (RSVP) via Python TKInter. The reader and some of its features are motivated by the conversation at http://www.reddit.com/r/books/comments/1yvvam/software_that_speeds_up_your_reading_to_500_words/cfofjhi. Please submit issues and requests at https://github.com/ambevill/rsvp-reader/issues.


Installation
------------

- Linux: Download the zipped source code, e.g., https://github.com/ambevill/rsvp-reader/archive/master.zip. To run, open a terminal and call python on that directory: *python Downloads/rsvp-reader-master.zip*
- OS X: Same as Linux. See note on TCL compatibility below.
- Windows: Unlike Linux and OS X, Python is not included on Windows. Install Python 2 (http://python.org/download/) and then follow the Linux instructions. (Linux "terminal" = Windows "command prompt")


Note on TCL compatibility in OS X
---------------------------------

The native Python graphics toolkit (TKInter) relies on TCL. If the RSVP reader crashes on your Mac, it may be because of TCL compatibility issues. This is beyond the control of the rsvp-reader developers. Please see http://python.org/download/mac/tcltk/.

To check your Python version, run *python --version* in a terminal. To check your TCL version, run *echo "puts [info patchlevel]" | tclsh* in a terminal.


Settings and Modification
-------------------------

The rsvp-reader is intended for users with beginner-level Python skills. The basic user settings (words per minute, pause-length for punctuation) are listed in settings.py.

To access the source code, unzip the downloaded .zip file. To call the modified program, call python on the unzipped directory: *python Downloads/rsvp-reader-master*


Release Notes
-------------

Version 0.1: Initial version, including pauses (stops) for punctuation and skip-back buttons. Tested with:
- Ubuntu 13.10, Python 2.7.5+, TCL 8.5.13


Planned Improvements
--------------------

- Slowing words based on frequency of common use via Google Ngram data.
- An extra pane highlighting the read word in context.


License
-------

This code is provided under version 3 of the GNU General Public License.
