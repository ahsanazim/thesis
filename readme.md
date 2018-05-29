# *GARB: Gaze-Aware Reading-aid for the Browser* 

**How to run:**

For personal use really, anyone else will need an eye-tracker - specifically the `Tobii Eye Tracker 4C` for this to work:

- start up tobii eye tracking desktop app / make sure it's even working
- open up `tobii/Interactors/Interaction_Interactors_101` in IDE and run
	- terminal window should open, functions as console/app for this program
- double click `client/index.html` to run it
- browser should open up. If eye-tracker and server running correctly then reading-aid should be on for articles on for `2`,`3`,`5`, and off for `1`,`4`. You can change this by going in to the `CSS` code for each `article_.html` file anyway.

**file structure notes:**

- `tobii` (i.e. server) - main code containing our websocket server that uses the Tobii core SDK to constantly get gaze information. Sends this on to client

- `client` - frontend web app, websocket client. All the actual functionality - highlighting etc.

- `webgazer` - where I use the webcam-based WebGazer eye tracking library; directory contains the source file as well as a demo i've made where you can see it's accuracy while reading an article. Simply go to the directory and run `python -m SimpleHTTPServer 8000` then go to `http://localhost:8000/` in your browser and you can check it out. SECONDARY TECHNOLOGY; NOT IN USE ANYMORE


**Tobii SDK exploration:**

The server in `tobii` directory:
- Interactors
	- Interaction_Interactors_101
		- our C# server; all relevant functionality in `Program.cs` file.