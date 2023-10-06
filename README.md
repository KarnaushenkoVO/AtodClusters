# Atod clusters
This is solution for the challenge from technical part evaluation for robotics course.

You can find original description of the task in the file _task_desciprion.pdf_ in the repository.

# Files
- _atod_clusters.py_ - file with the solution
- _tests.py_ - tests suit for the solution
- _task_description.pdf_ - original task description in PDF format
- _README.md_ - documentation


# How to run?
To execute code you need to run atod_clusters.py and enter input values line by line.

Command to run:
_python3 atod_clusters.py_

No any additional requirements except Python.
See how it should look like on the screenshot below:

![Screenshot](how_to_run.png)


**Input parameters**:
The first row contains two integers separated by a space: N and M — the number of stars in the sky and
the number of magical connections drawn, respectively. The subsequent M rows contain two integers each:
Ai, Bi — representing the star number Invoker identified and the star number Puck pointed out.

**Output**:
1. The integer K — representing the total number of Atod Clusters formed.
2. The subsequent K rows should list the number of connections each Atod Cluster has, in non-descending
order.


Tested using python3.7 and python3.10.


# Tests
You can find tests suit in tests.py file. Just execute this file using python 
and it will show if anything is wrong.  You can try to break the code.

Command to run:
_python3 tests.py_

# How to read the code?
In the end of the _atod_clusters.py_ file you may find execution entry point.
This if statement is responsible for input parsing 
(using utility _parse_two_numbers_ from the top of the file) and delegating further execution to
_find_atod_clusters_ function which contains all the logic.
You can also find helpful docstring for statements which can be unclear.
