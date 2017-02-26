## Runescape Eyes of Glouphrie Quest Calculator
Python GUI implementation to help players calculate the shapes they have in their inventory.    
Images taken from http://2007.runescape.wikia.com/  

## What should you do before running tool?
You should try to get as many shapes from Brimstail using drop trick.  
Another way is to try to exchange big shape values for smaller shapes.  
The idea is get a coverage of values so when you try the locks, you can be sure to get a solution.  

## How to run tool?  
#Windows: 
Access the files:  
build > exe.win32-2.7 > eyescalc.exe   
Run eyescalc.py
#Unix:   
Change directory to files  
Run command 'python eyescalc.py'   
There might be some dependencies that you'll have to install; possibly PIL and tkinter  


## Why did I make this?
Started playing OSRS again and came across this quest.    
I did this quest when I was younger, and when I was doing it again I had trouble trying to get the correct amount to   unlock the machine. So I decided I'd make a program to help me see if I have the solution in my inventory  

I also wanted to work with some Python GUI. This was my first time implementing with Tkinter  

## Type of Problem
The premise of this calculator involved adding shapes that held a numerical weight into a lock. The lock only opened itself with a certain weight.  
This is a variation of the subset sum problem.  

Our shapes that we hold in our inventory will be our array/list of numbers.  Our locks are the sum we are trying to find. 
Unlike the subset sum problem, we are restricted to a number of shapes allowed to open the lock.  
That is to say, if one lock has a limit of two shapes, we are lookng for a pair in the array that equals that lock weight  

## Compatability
Runs well with Linux environment  
Works with Windows environment using cx_Freeze  

## Screenshot
![alt tag](https://raw.githubusercontent.com/Fompei/eyes-of-glouphrie-calculator/master/linux_gui.png)  
![alt tag](https://raw.githubusercontent.com/Fompei/eyes-of-glouphrie-calculator/master/windows_gui.png)  