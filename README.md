# PROJECT TITLE
**Pore**

## Short Description
This project constructs a generative model based on local soft tissue behavior and structural feedback mechanisms, aiming to explore the generative logic of biological forms such as shell spirals, porous topologies and flexible folds within digital systems.

## Introduction 
My inspiration originates from the spiral growth patterns of shell-bearing organisms and the flexible structural characteristics of soft tissue. By integrating Python and TouchDesigner, construct a generative model based on local soft tissue behavior and structural feedback mechanisms., aiming to simulate directional spiral growth in shells, porous topologies in cavity-like biological structures, and dynamic folds in soft tissues.

The system experiments with three types of morphological generation mechanisms. First, using Python in combination with polar coordinate equations and the Archimedean spiral, 
it simulates the spiral growth trajectories of shells to explore structural patterns of axial expansion and scale increment. Then, TouchDesigner is employed to simulate the porous distribution and spatial connectivity of shell surfaces. 
Finally, the project models the folding and feedback behavior of soft-bodied surfaces, using local deformation and self-regulating mechanisms to reveal the adaptive capacity of flexible tissues in changing environments.

You need to supply three pieces of hardware to show this project:

### Display  
There are two possible display methods for this work:

* Projection onto a flat surface – A standard projector can be used to project the visuals onto a white wall or a white projection screen.
* Immersive three-panel installation – The visuals can also be presented within a three-sided projection 


### Computer 
The coding has been successfully run on the following models:

Apple M3 Max (16-inch, 2021)， 36GB unified memory，1TB SSD²，Mac OS Sonoma 14.8.3  

MacBook Pro 16” (Late 2019)Intel Core i7 / i9（9th Gen），36GB unified memory， 1TB SSD²  

maOS (Apple Silicon – MacBook Pro M1 to M4 series)  

The computer must be connected to the screen by an HDMI.

### Light

The audience should be placed in complete darkness to ensure the imagery is rendered with maximum clarity and contrast.
Any ambient or spill light should be eliminated from the exhibition space to preserve the intended perceptual experience.  

## Installation

There are two ways to present this work:

* Pre-rendered playback 
Use a pre-edited video recording of the piece for projection or display. Connect the video from the computer to the screen or projector via the HDMI  interface.

* Live generative version  
This project generates real-time visuals using Python and py5, and streams the output via NDI to TouchDesigner for display and control.

### Setup Instructions

* Step 1: Install Python and Configure the py5 Environment

  1. Download and install **Visual Studio Code**  https://code.visualstudio.com/
  2. Install **Python**(version 3.10 or above recommended)
  3. In Visual Studio Code, configure the **py5 environment**
     
      - Install the Python extension in VS Code    
   
      - Set up a virtual environment if required    
   
      - Install py5 and related dependencies  
   
* Step 2: Install TouchDesigner
  Download and install **TouchDesigner** from:  https://derivative.ca/

* Step 3: Install **NDI**
  Download from: https://ndi.video/  

* Step 4: Run the Python Script
  1. Open the project folder in **Visual Studio Code**
  2. Run the file: **pore.py**

* Step5: Display in TouchDesigner
	1.	Open TouchDesigner
	2.	Use an NDI In TOP to receive the video stream
	3.	Use a Switch TOP to switch between different visual inputs
	4.	Further visual control and composition can be performed within TouchDesigner

## Calibration 
* Sound synchronization
If the installation includes sound, confirm that there is no noticeable audio delay. The sound should respond to real-time events or visuals without lag.

* Visual display
Ensure that the projected or screen-displayed visuals appear correctly.  
Check for proper orientation (portrait or landscape), resolution (e.g. 1920×1080), and smooth frame playback.

* If using NDI, verify that the video stream is being received without latency or frame skipping.

## Text
Please put the following text next to the work:

Pore, by Wenxi Cao, 2026. This project constructs a generative model based on local soft tissue behavior and structural feedback mechanisms, aiming to explore the generative logic of biological forms such as shell spirals, porous topologies and flexible folds within digital systems.

If you are interested in collaborating, please contact: caowenxixi@126.com


## Requirements

### Tech Stack
- Python
- TouchDesigner 2022 or later
- NDI Tools

### Operating System
- macOS 11 or later
- Windows 10 / 11

### Python Libraries
- numpy
- ndi-python
- py5

## Screenshots

![Image 1](Image/1.png)
![Image 2](Image/2.png)
![Image 3](Image/3.png)
![Image 4](Image/4.png)

## Credits
* Author- Wenxi Cao（Cici Cao）

* References  
  Archimedean spiral-https://en.wikipedia.org/wiki/Archimedean_spiral?utm_source
  
  Daniel Berio-Ndi_numpy_image.py

## License
All rights reserved.

## Contact / Links
*GitHub repo link, website, demo URL.*
