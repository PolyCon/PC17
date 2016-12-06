#FMF
fmf stands for form markup file
form markup borrows heavily from markup
The number of 
#
marks you put in a heading will determine the heading value (up to h6) of that line.
For a text input (or multiple text inputs) use t, :, and a list of the input names.
Ex. t:input1,input2
To write a list, the markup is similar to html, ul for unordered list, ol for ordered list, and then : and a string delimited list of list items
For radio buttons, use rb, the name of field the radio buttons effect and then the options.
Ex. rb:example,choice1,choice2,choice3.
Sub for submit button.