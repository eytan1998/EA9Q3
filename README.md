# # Economic algorithms exercise 9 Eitan Ankri

### question 3
![q3](https://github.com/eytan1998/EA9/blob/master/Q3.png)

#### find if given budget and preferences are decomposition
we follow this algorithm we learn at lesson
![algo](https://github.com/eytan1998/EA5/blob/master/How.png)

shortly we make graph with s(start), t(tail), and person as nodes and subjects as nodes.

make edges from s to each person with capacity of C/n because this is the budget we gave for each person. 

make edges from person to subject with capacity C\n like above

make edges from subject to t with capacity of d because this the budget for each subject

