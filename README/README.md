## ECHO V1 - Space vehicle CPU

#### <font color='#ff375f'> Overview of ECHO V1 </font>

- It is a 32-bit RISC-V CPU with a 32-bit wide data bus.
- It is designed to be very power efficient.
- It is designed to be used in a space vehicle, and as such
- It is also designed to be very simple, and as such.
- It is not a general purpose CPU.

### <font color='#ff375f'> Setting up the environment </font>
- Do it tomorrow
- Instruction 1
- Instruction 2
- Instruction n

### <font color='#ff375f'> Loading the CPU </font>
-  <u>Importing the required libraries</u>
   - I have used Pandas for reading CSV file and performing required operations.
   - And, Matplotlib for plotting the pie chart graphs for visualisation.

- <u>Importing the data</u>

  - I have used Pandas to read the CSV file and store it in a variable called 'dataSet'.

- <u>Data cleaning</u>

  - As my analysis was for number of students interested in a club and their mode of attendance.
  - My CSV file contained data of all the necessary information I needed. 
  - So, I stored interested students data in a variable called <b>'interestedIn'</b> and mode of attendance data in a variable called <b>'modeOfAttendance'</b>.]
  - The <b>interestedIn</b> and <b>modeOfAttendance</b> variables are of type Pandas dataFrame.

- <u>Data capture</u>
  - I have created 8 variables to store the count of students interested in a club and their mode of attendance.
  - I also created an empty temporary array called <b>'temporaryArray'</b> to store the data of interested students and mode of attendance.
  - I have used <b>for loop</b> to iterate through the modeOfAttendance dataFrame.
  - I have used <b>if-else</b> statements to check if the student is interested in attending online or offline.
  - Then, for every 'Online' value I appended the value '1' to the temporaryArray.
  - Later on I used the len() function to count the number of '1's in the temporaryArray and stored it in the variable <b>'online'</b>.
  - The remaining students were interested in attending offline classes.
  - This same logic I have used to count the number of students interested in each bootcamp.
  - I have used <b>for loop</b> to iterate through the interestedIn dataFrame.
  - I have used <b>if-else</b> statements to check if the student is interested in a particular bootcamp.
  - Then, for every 'True' value I appended the value '1' to the temporaryArray.
  - Later on I used the len() function to count the number of '1's in the temporaryArray and stored it in the variable <b>'bootcampName'</b>.
  - By this I have captured the data of number of students interested in a club and their mode of attendance.

- <u>Data visualization</u>
  - I have used <b>matplotlib</b> library to plot the pie chart graphs for visualisation.
  - I have used <b>plt.pie()</b> function to plot the pie chart.
  - I have used keyword argument called <b>labels</b> to set the labels. 

- <u>Conclusion</u>
  - By doing this analysis I have found that the number of students interested in attending online classes is more than the number of students interested in attending offline classes.



### <font color='#ff375f'>References and Contacts</font>
- [Pandas](https://pandas.pydata.org/)</font>
- [Matplotlib](https://matplotlib.org/)</font>
- [Jupyter Notebook](https://jupyter.org/)</font>
- [Python](https://www.python.org/)</font>

### <font color='#ff375f'> Author </font>
<font size='3'><b>AJAY S PATIL B.Tech Computer Science & Engineering at RV University</b> 
<br></font>
- [LinkedIn](https://www.linkedin.com/in/ajay-patil-b37042184/)
- [GitHub](https://github.com/ajayspatil7)
- [Twitter](https://twitter.com/s_patil_ajay)
- [Instagram](https://www.instagram.com/s_patil_ajay/)

