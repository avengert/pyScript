# pyScript
Any Python reusable code used in my projects.

Features to add to a python script include:
  1) clear()    *** This works with python 2 & 3 ***
  2) pprint()   *** Allows a border to show up around printed text. This also has arguments ***
  3) pause()    *** Pauses the screen with a request to press ENTER, argument allows you to type custom text ***
  4) getOS()    *** Boolean that says TRUE if Windows FALSE if Linux
  5) getPyVer() *** Boolean True for python version 3+ FALSE for versions under 3


Use Case:
	pprint("TEST MESSAGE", "*", "32")
	pprint(<MESSAGE>, <STYLE>, <Length>)

	pause()
	pause("PAUSED FOR CONVENIENCE")
