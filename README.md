# Mars Rover Challenge
Google Mars Rover Technical Challenge

Full challenge spec can be found here: https://code.google.com/archive/p/marsrovertechchallenge/  

The main NASA class handles user input with friendly prompts. It contains the plateau size in case you want to expand the number of rovers present in the application.  

The Rover class takes the user's input, processes it and executes the Rover's movements. Because input is fairly strict, when input deviates from the expected / required, Exceptions are thrown. The headings set matches with the rules dict in move() and could potentially be expanded to include NE, SE, SW and NW as additional headings.  
Once a move has been performed, the Rover is checked to ensure it has not gone out of bounds within the plateau's coordinates. getposition() gets the final resting place of the Rover.  

## Usage
Run the program with `python rover.py`  
  
**Example input:**  
Enter the plateau's maximum coordinates in 'X Y' format  
`> 8 8`  
Enter the Rover's start coordinates and heading in 'X Y H' format:  
`> 1 2 E`  
Enter the Rover's instructions consisting of L, R and M in a string:  
`> MMLMRMMRRMML`  
**Final Output**  
`> 3 3 S`  

## Testing
Run all unit tests from the command line with `python test.py`  
`test_1()` tests the default Rover behaviour as per the brief  
`test_2()` runs an alternate Rover path   
`test_3()` tests Rover command and out of bounds exceptions  
`test_4()` tests Mars plateau input exceptions  
`test_5()` tests Rover start input exceptions  