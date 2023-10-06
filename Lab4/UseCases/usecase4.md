**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 4

<hr>

**Use Case**: left-clicks (i.e. on the pressed event, not released) a pixel color will change wherever the mouse is located. This should allow me to drag and draw over the canvas like a pencil on a piece of paper.

**Primary Actor**: User

**Goal in Context**: When the user left clicks or left clicks and drags, all the pixels the mouse is on or drags over shall change to the color selected 
**Preconditions**: The program is running and stable, the mouse is on top of the canvas

**Trigger**: The mouse is on top of the canvas and then the left click button is pressed (can then be held and mouse be dragged)
  
**Scenario**: Scenario 1 : The user wants to change the color of an individual pixel so they left-click and the color of that pixel changes to the color selected
              Scenario 2 : The user wants to change the color of a group of pixels so they left-click and drag the mouse and all the pixels that the mouse  hovered over while clicked change to the color selected
**Exceptions**: The user accidentally changes the color of a bunch of pixels, we could implement an undo button to undo the most recent change
**Priority**: High-Priority

**When available**: On release

**Channel to actor**: The primary actor communicates through I/O devices. Specifically the mouse. The system is responsible for changing the color of pixels the mouse is over when clicked or when clicked and dragged, and should respond within 0.1 seconds of any mouse event. The user is responsible for all other input.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A
**Open Issues**: The user accidentally changes the color of a bunch of pixels, we could implement an undo button to undo the most recent change so we must have a feature allowing for undo 

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
