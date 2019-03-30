# Find-Shortest-Path-Using-GREEDY-Algorithm

Full code : [Code](/Shortest_path_Greedy.py)

Find Shortest Path With Greedy Algorithm

![Graph](/picture_graph.png)

Greedy Algorithms
Greedy algorithm is an algorithmic paradigm that follows the problem solving heuristic of making the locally optimal choice at each stage with the intent of finding a global optimum. In many problems, a greedy strategy does not usually produce an optimal solution, but nonetheless a greedy heuristic may yield locally optimal solutions that approximate a globally optimal solution in a reasonable amount of time. 
(source: https://en.wikipedia.org/wiki/Greedy_algorithm)

Problem : 
 
1.	Atsugi
2.	Sakai
3.	Tokyo
4.	Saitama
5.	Sendai
6.	Fukuyama
7.	Kashiwa
8.	Akihabara
9.	Nagasaki
10.	Yokohama
11.	Hiroshima
12.	Kyoto
13.	Osaka
14.	Matsuyama
15.	Funabashi
16.	Chiba
17.	Nara
18.	Nagano
19.	Kumamoto
20.	Fuji

Once upon a time, Yudhis and Tyo want to take a vacation in Osaka City, but they are from different cities, Yudhis from Tokyo, and Tyo from Fuji, They want to meet quickly because they both have missed each other, so make a program to help them find the fastest route so they can meet fast.


Step: 
•	We use the heap-queue library to store heuristic values and are sorted from small to large.
•	The first step, we save the graph in the form of an adjacency list, which is by storing neighboring nodes with how much cost or distance needed to go to the neighboring node into the list.
 
•	The second step, we store the heuristics values, that is straight line distance between from origin city to destination city.
 
•	Then we make a greedy function with parameter origin city and destination city, to compare the heuristic values of each neighbor to the destination city, then we sum up and print the costs every time we move to a neighboring city and the function is complete if it has arrived at the destination city.

 
•	Last, we make a function that prints the route from the city of origin to the city of destination.
•	Then we can test the program
 
•	And The results is..
