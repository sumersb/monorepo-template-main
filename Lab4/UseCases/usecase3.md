**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 3

<hr>

**Use Case**: Spacebar fills the canvas with the last color

**Primary Actor**: User

**Goal in Context**: Want to change the background of the canvas by using a spacebar or clear canvas

**Preconditions**: The program must be running the user must have already used a color (or default white) and then press spacebar, if nothing has been done then nothing will happen

**Trigger**: User pressing spacebar
  
**Scenario**: Scenario 1 : user selects a color and presses the spacebar to fill the entire canvas with said color
 
**Exceptions**:  The program becomes unresponsive and the the process is unable to load


**Priority**: High-Priority

**When available**: on release

**Channel to actor**: The primary actor communicates through I/O devices. Specifically keyboard The system is responsible for clearing the canvas with the last used color and should respond within 0.2 second of any keyboard event. The user is responsible for all other input.

**Secondary Actor**: N/A
**Channels to Secondary Actors**: N/A

**Open Issues**: If a user accidentally selects the spacebar and clears the canvas then they should have a way to reset the operation, like an undo button

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
