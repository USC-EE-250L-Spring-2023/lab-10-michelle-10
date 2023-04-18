# Lab 10
[Fork](https://docs.github.com/en/get-started/quickstart/fork-a-repo) this repo and clone it to your machine to get started!

## Team Members
- Michelle Arredondo
- Nayeli De Leon

## Lab Question Answers

Question 1: Under what circumstances do you think it will be worthwhile to offload one or both
of the processing tasks to your PC? And conversely, under what circumstances will it not be
worthwhile?

It is worthwhile to offload processes to your PC when the program requires a lot of power, energy, or computing resources. It is not worthwhile offloading if your program does not require a lot of power, energy, or computing resources. It could also be worthwhile offloading if you are working with sensitive or private data.

Question 2: Why do we need to join the thread here?

It is important to join the thread because it makes sure that the thread that was started easrlier has finished executing before the program moves on. 

Question 3: Are the processing functions executing in parallel or just concurrently? What is the difference?

Parallel processes are processes that run at the same but on different processors. Concurrent processes run simultaneously on the same processor or system. The processing functions in our program are executed in parallel because one process function is executed on the RPI and the other is offloaded and executed on the computer. If you are only using your computer with two terminals to test the code before running main.py on the RPI, then I think the processes would execute concurrently because they run simultaneously and on the same processor system. 
 	
source: chatGPT
 	
Question 4: What is the best offloading mode? Why do you think that is?

I think the best offloading mode was process2 because it had the shortest mean execution time. I think the offloading helped speed up how long it took process1 and process2 offloading modes to run process1() and process2() functions. But maybe process2 was faster because the function process2()requires more computing resources, so the program as a whole ran faster when function process2() was offloaded. 
	
Question 5: What is the worst offloading mode? Why do you think that is?

The worst offloading mode is 'both.' I think it takes the longest out of the three offloading modes because it's basically as though you were running the functions in main where it executes the first function and then the second function. This is supported by how the execution times for 'both' and 'none' were very similar. In other words, it takes the longest because offloading both doesn't actually let you run the functions simultaneously, so it seems to defeat the purpose of offloading.
	
Question 6: The processing functions in the example aren't very likely to be used in a real-world application. 
What kind of processing functions would be more likely to be used in a real-world application?
When would you want to offload these functions to a server?

An example of offloading could be with signal-image processing calculations. For instance, you could split time-domain data into two sections if you have a lot and then offload half of the data to calculate the fourier transform, and then calculate the other half in main.py. This could help speed up the execution time for large amounts of data. 
	
source: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwiRicLU2bL-AhXRJEQIHcLPBZkQFnoECBQQAQ&url=https%3A%2F%2Fwww.researchgate.net%2Ffigure%2FOffloading-process-strategy_tbl1_321048090&usg=AOvVaw0-T41dukzIn1wTMNMmK6m8
