# Thesis - *eye tracking for improving online reading* 

**general overview:** [link to thesis proposal](insert link)

**recent updates** see [issues](https://github.com/ahsanazim/thesis/issues)

**file structure notes:**

- `tobii` (i.e. server) - main code containing our websocket server that uses the Tobii core SDK to constantly get gaze information. Sends this on to client

- `client` - frontend web app, websocket client. Currently allows you to start server and then receive stream of gaze information from server. Right now this is displayed to dev tools console.

- `webgazer` - where I use the webcam-based WebGazer eye tracking library; directory contains the source file as well as a demo i've made where you can see it's accuracy while reading an article. Simply go to the directory and run `python -m SimpleHTTPServer 8000` then go to `http://localhost:8000/` in your browser and you can check it out. SECONDARY TECHNOLOGY; NOT IN USE ANYMORE


**Tobii SDK exploration:**

Code in `tobii` directory ordered by functionality. All runs and works
- Interactors
	- Interaction_Interactors_101
		- BEFORE: simply tells if you're looking at the screen or not (i.e. 'HEY THERE' vs 'GOODBYE')
		- NOW: for now contains the beginnings of the websocket server, this will probably be moved somewhere else later if need be
	- Interaction_Interactors_102
- States
	- Interaction_States_101
	- Interaction_States_102
- Streamms
	- Interaction_Streams_101
	- Interaction_Streams_102