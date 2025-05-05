# Using CSC HPC environment efficiently 19.-21.9.2023 

###### tags: `puhti` `mahti` `allas`

> This is the collaborative "notebook" for the "Using CSC HPC environment efficiently" course organised in September 2023 by CSC -IT center for Science. 
> [Prerequisite course page in eLena platform](https://e-learn.csc.fi/course/view.php?id=75)
> [Course page in eLena platform](https://e-learn.csc.fi/course/view.php?id=76)
> [Collection of slides and material](https://csc-training.github.io/csc-env-eff/)
> [Zoom-link for sessions](https://cscfi.zoom.us/j/69786868477?pwd=cWhHTFpjakhFMUFWUnc1VE8vTVRqUT09)
> [Zoom-link for SUPPORT SESSIONS / weekly user meetings](https://cscfi.zoom.us/j/65059161807)

:::danger
:calendar: The latest updates on the **course schedule** can be found in here.
:interrobang: This is also the place to ask questions about the workshop content! We use the Zoom chat only for posting links, reporting Zoom problems and such.
:::

:::info
:bulb: **Hint:** HackMD is great for sharing information in this kind of courses, as the code formatting is nice & easy with [MarkDown](https://www.markdownguide.org/basic-syntax/)! Just add 3 ticks (``` ` ```) for the``` code blocks ```.  
Otherwise, it's like a Google doc: it allows simultaneous editing. There's a section for practice down there ⬇️
:::

[ToC]

## How we work

### Zoom instructions
<details>
    
- Link to the zoom room was sent to you via e-mail
- Please arrive 5-10 minutes before to test your microphone setup.
- Use your **full name** (Firstname Lastname)!
![](https://i.imgur.com/TAHEHVt.png)

- During the course, please remember to always mute your microphone when you are not speaking.
- Please use a headset in order to avoid echo (a simple phone headset is just fine).
- You can find all the controls (mic, video, chat, screen sharing) at the bottom of the Zoom window (when you bring your mouse there).
- You can use the chat box for questions and comments, but please make sure you reply to "all panelists and participants" instead of just "all panelists", which is often the default.
- If you have a spoken question/comment, please use the "raise hand" button: we will then give the floor (and microphone rights) to you.
- Note: for questions and answers about the course topics, we will be using this living document
- Break-out rooms: More info:https://support.zoom.us/hc/en-us/articles/115005769646-Participating-in-Breakout-Rooms#collapseWeb Breakout rooms are smaller sessions that are split off from the main Zoom meeting. They are completely isolated in terms of audio and video. The host will need to invite you to join the breakout room, after which you can click "Join" in the notification pop-up. Mouse over the number of people in the breakout room to reveal the "Join" button. ![](https://i.imgur.com/wRJ2gqp.png)



- In Zoom, there are couple of buttons: First row emojis can be used to express your feelings :) They will disappear automatically after a while. Second row icons are used to indicate whether you are done with the practicals (green symbol), still need some time to work with the practicals (red symbol), or wish us to slow down or speed up, or whether you are having coffee. These you need to turn off yourself. To indicate that you have a question, you can use the "raise hand" button.
![](https://siili.rahtiapp.fi/uploads/85ebdf02-05d2-4b51-81d0-c14458f299e5.png)
</details>

### Code of conduct
<details>
    
We strive to follow the [Code of Conduct developed by The Carpentries organisation](https://docs.carpentries.org/topic_folders/policies/code-of-conduct.html) to foster a welcoming environment for everyone. In short:
- Use welcoming and inclusive language
- Be respectful of different viewpoints and experiences
- Gracefully accept constructive criticism
- Focus on what is best for the community
- Show courtesy and respect towards other community members
</details>details>

## 📅 Agenda

### Prerequisite / support session 13.9.
14:00-15:00 Join the pre-course support session, which is also part of [CSC's weekly user meetings](https://cscfi.zoom.us/j/65059161807)

### Day 1: Tuesday 19.9.


 
 
| Time  | Content |
|-------|---------|
| 8:45  | Login, check connections work, test microphone |
| 9:00  | Welcome, course practical info, learning targets,  ice-breaker, feedback/expectations (10 min) |
| 9:10  | **Topic 1: Prerequisites & Connecting** (15 min) |
| 9:25  | **Topic 2: Introduction to HPC Environment** (20 min) |
| 9:45  | _Break_ (10 min)|
| 9:55 | **Topic 3: Disk Systems** (15 min) |
| 10:10 | **Intro to breakout rooms & hosts, joining the breakout rooms, accessing materials**  | 
| 10:10 | **Topic 3: Hands on 3.1** (<20 min) |
| 10:30 | **Topic 4: Module System & preinstalled software** (15 min)|
| 10:45 | **Topic 4: Hands on 4.1** (10 min)|
| 10:55 | _Break_ (10 min) |
| 11:05 | **Topic 5: Batch queue system and interactive use**  (20 min)|
| 11:25 | **Topic 5: Hands on 5.1** (30 min) |
| 11:55 | Recap + preparations for the next day (5 min) |
| 12:00 | Finish |




### Day 2: Wednesday 20.9.
    
    
| Time  | Content |
|-------|---------|
| 8:45  | Channel open, "morning coffee" |
| 9:00  | Re-cap, feedback/expectations + some Qs from HedgeDoc (5 min) |
| 9:05  | **Topic 6: Understanding resource usage** (20 min)|
| 9:25  | **Topic 6: Hands on 6.1** (30 min) | 
| 9:55 | _Break_ (10 min)|
| 10:05 | **Topic 7:  Allas, where to keep your data and current issues**  (25 min)|
| 10:30 | **Topic 7:** Hands on 7.1 (30 min) |
| 11:00 | _Break_ (10 min) |
| 11:10 | **Topic 8: Installing applications** (15min) |
| 11:25 | **Topic 8: Hands on 8.4 and 8.1** (25min) |
| 11:50 | Recap + preparations for next day (10 min)|
| 12:00 | Finish |
| 14:00 | Bonus: Join the weekly user meeting https://cscfi.zoom.us/j/65059161807  |



 
### Day 3: Thursday 21.9.


    
    
 | Time  | Content |
|-------|---------|
| 8:45  | Channel open, "morning coffee" |
| 9:00  | Re-cap, feedback/expectations + some Qs from HedgeDoc (5 min) |
| 9:05  | **Topic 9: Containers & Apptainer** (20 min)|
| 9:25  | **Topic 9: Hands on 9.2** (35 min) | 
| 10:00  | _Break_ (10 min)|
| 10:10 | **Topic 10: How to speed up jobs** (20min)|
| 10:30 | **Topic 10: Hands on** (40min)  **NOTE:** use the `--reservation=computing-environment-sept` in your batch script!|
| 11:10 | _Break_ (10 min)|
| 11:20 | Topic themed breakout rooms + ask anything on all previous topics (25 min) |
| 11:45 | Recap + feedback + open questions + cleaning up files from course project (15 min) |
| 12:00 | Finish |   
    



---



## ☃️ ICE BREAKER (HackMD -practice)

### Ice breakers
Let's learn how to use this HedgeDoc document by answering an ice breaker question! 


    
**Q1: What from this workshop are you going to use in the near future?**

**Answers:**

* Hopefully batchjobs (+6)
* Already working lots with slurm, but will soon need to figure out which settings (runtime, tasks, etc) are most efficient (+4) 
* CSC computational services in general (+4)
* Learning the services in CSC (+1)
* managing resources efficiently (+4)
* Getting better at submitting efficient batch jobs (+3)
* Getting more comfortable with linux interface, especially in Puhti
* Learn to calculate better the resources I need for my batch job. Not so much trial and error (+3)
* How to use puhti, install program and run it (+2)
* Install specific programs (+1)
* Really just how to efficently use CSC services to transfer and store data.
* Efficient use of batch job submission, particularly using GPU's for Gromacs based MD simulations in puhti, mahti and Lumi.

### Q2: What topics would you like to still discuss (in topic themed break out rooms)? 

* Can I figure out from lots of statistics from my runs if my code runs into a bottle neck (e.g., more cores do not speed up the runs anymore) ?
* Maybe discuss about other services e.g. Rahti.
* parallel computing ? how to write your script, not the launch script but the python or perl or what ever language running. Some really simple example would be create
* Spark jobs?
* Sensitive data- ePouta
* Tykky module and its usage with Docker

## 📝 Q & A

Your questions are answered here. We will answer them, and this document will store the answers for you for later use! :rocket: 

:::info
Scroll :arrow_down: to the bottom of the page to submit a question 
:::



- [x] **I have difficulty pasting my questions into HackMD (here). Do you have some instructions on how to write here?**

    - A: HackMD can look a bit differend depending on the view you are in. Can you see the three icons on top left corner, next to HackMD text? There’s pencil, this side-by-side symbol, and an eye (see below for a screenshot). In eye view, you can’t edit, you are just viewing. The other two reveal the markdown (MD) version of the page, which you can edit. I find it easiest to edit with the side-by-side view, but it can be a bit slow sometimes. First time opening the page, the small Edit (pencil) button might be on right next to the table of contents. Please note that it might make things faster if you **switch to view only mode when not editing**!

:::info
The small pencil icon for entering edit mode for the first time. You might need to scroll all the way up to see it.
![The icon corresponding to the edit link with title "Edit this note"](https://siili.rahtiapp.fi/uploads/f24239cd-3c6b-46f6-a61f-4f08c4d96415.png)
:::

:::info
The bigger HedgeDoc toolbar for switching between modes later on.
![The toolbar from which the different modes can be accessed. You can also switch between edit and view mode using hotkeys ctrl-alt-v and ctrl-alt-e respectively](https://siili.rahtiapp.fi/uploads/3bb6bbfd-f73b-4933-bd18-7d46dd7f45fc.png)
:::

:::info
:bulb: **Hint:** You can also apply styling from the toolbar at the top :arrow_upper_left: of the editing area.![](https://i.imgur.com/Cnle9f9.png)
:::


  


## ✏️ Add your questions here

Please type your questions ON THE BOTTOM OF THIS SECTION. We will answer them, and organise the document topically.

 
- [x] **Q0: Have I clicked the edit mode on?**
    - A: Probably not yet.. ↖️


- [x] **Q1: Slides available after the course?** 
    - A: They sure are! You will also have the access to this HedgeDoc document (save the link). 
        - The slides and tutorials are available here: https://csc-training.github.io/csc-env-eff/
        - Access to e-lena (and the quizzes there) may discontinue.
    - We encourage you to share and use the material also in your own courses. The material is in git, and we welcome all feedback and edit suggestions (pull requests)!

- [x] **Q2: Has the Zoom meeting already started? I'm just gettin "The meeting has not started" -note.** 
    - A: Make sure you have the full Zoom link when connecting! It's long and contains the password :)

- [x] **Q3: Should we be able to access the slides in e-elena? I can only see the first slide.**
    - A: Try navigating with the arrow keys :)

  
- [x] **Q4: So many credendials... Which ones do I need and where?!?**
    - A: You need 
        - **CSC credentials** to Puhti/Mahti
        - **Haka OR Virtu credentials** (=your university/institution credentials) to my.csc.fi
        - **Haka credentials** (=your university/institution credentials) to [eLena platform](https://e-learn.csc.fi/course/view.php?id=71) 
        - contact us if you don't have HAKA/Virtu in use

- [x] **Q5: I have forgotten my CSC username and password**
    - A: In my.csc.fi you can check your CSC username. If you have forgotten your CSC password, check this link: https://docs.csc.fi/accounts/how-to-change-password/ -Note that it takes some time for the password to update to Puhti, if you need to change that :)

- [x] **Q6: Depending on the place you say to obtain acces to Puhti and Allas or Puhti and Mahti, should we have all three of them (just in case)?**
    - A: On the course there is one tutorial in which you can try moving data from Puhti to Mahti. It is an optional task so you don't necessarily need Mahti.

- [ ] **Q7: Can FileZilla, WinSCP or Putty be used to transfer files directly to Allas from my local machine?**
    - I think you can access Allas from your browser, at least to download objects, but not sure if you can upload anything 
    - I think you cannot upload files to Allas via any of those listed file transferring tools, you can use/acces the Allas from https://sd-connect.csc.fi


- [x] **Q8: Can I use VSCode remote explorer to connect to Puhti ?** 
    - A: I have not tried it myself, but should be possible
    - A: See here: https://docs.csc.fi/support/tutorials/remote-dev/

- [x] **Q9: Am I right with the assumption about BU: if I apply for too much memory, the set memory gets billed? But with runtime/CPU usage just the used one gets billed?**
    - A: Yes. This is correct. You can think of it this way: what has been allocated for you, i.e. what is not available for others, is billed. The memory is allocated for you _for the duration of the job_ and not available for others and is billed. If the job ends before the time you specified in the batch script, the resources are freed and they are again available for others --> not billed.

- [x] **Q10: Does using SSH for Puhti mean you can access files directly from your own computer or do you still need to store the data you want to use in Allas/csc services?**
    - A: SSH for Puhti means here "just" a terminal connection. You'll get the command line and you can access files etc. The File browser is separate.
    - **I didn't quite understand. If I use SHH from my work laptop, so I'm accesing Puhti through terminal, am I then able to for example do DNA sequence aligment on FASTQ files on my local disk or do these files need to be stored in CSC for me to be able process them with Puhti?**
    - A: Yes, you need to copy the files to CSC to be able to use the Puhti software and computing capacity. With ePouta, the situation might be different, but it's not covered here.

- [x] **Q11: I have problems when connecting through ssh to Puhti with the foot terminal emulator. When running commands such as "clear" I get an error message saying that "foot" is an unknown terminal type. Thanks in advance!** 
    - A: This is probably slightly more complicated issue that would require more information. Probably this application is not compatible with Puhti. Maybe you could try using the Puhti web interface for the duration of the course?
    - Me again: thanks for the answer! Indeed the web interface works great and I can also use a different terminal emulator. I managed to solve my problem by copying the cofiguration files (`/usr/share/terminfo/f/foot*`) of my emulator to Puhti (`~/.terminfo/f/`).

- [x] **Q12: How can I download the material from Git?. It saves only as html.**
    - A: Do you refer to the course slides? These can be viewed in the browser as pages (navigate with arrow keys).
    - I mean if I want to download the slides to use them in my own courses. So far I can only view them in the browser.
    - A: Yes, since they are html files, you can only view them using a browser. Html files can be converted to PDF using e.g. chromium browser if needed.
    - Q: Thank you. It does save as PDF but you need to do that slide by slide (tedious). Are you aware of an alternative batch solution?

- [x] **Q13: If I want to install a tiny software (e.g., home-made script or .exe), what should I do?**
    - A: This depends a lot. If it is just e.g. a Python script, you can copy it to the supercomputer and try to run it using some of the Python modules available (or install a Python environment of your own). With .exe file (executables/binaries), it should support Linux operating system. If this is the case and the application is just a serial (or threaded) application, you can try to run it directly. Otherwise you should probably recompile the application to ensure that it performs well. See https://docs.csc.fi/computing/installing/ for more info.

- [x] **Q14: What should I exepct to see after enabling the Remote graphics option -X when connecting with ssh? (I am using Xterminal on windows)**
    - A: `-X` option will enable to forward graphics from the supercomputer to your local display. So you should not expect to see anything after ssh, but if you try opening e.g. a picture with `eog` it should work. If not using the `-X` option you would get an error like `cannot open display`



- [x] **Q15: Do you intend to add GPU optimized tensorflow-federated libraries in the future? I am currently using one installed myself.**
   - A: Normal [Tensorflow we already have](https://docs.csc.fi/apps/tensorflow/) (GPU optimized of course). We don't have TensorFlow Federated yet, although I suspect it can be easily added on top of the normal module by a user with a command: `pip install --user tensorflow-federated`. If you think it should be included in the CSC-provided module, you can send an email request to servicedesk@csc.fi.


- [x] **Q16: What is the best approach to keep track of the directories & objects stored in Allas and Puhti? I have experience backing up files in Allas before scratch purge, but it is quite complicated to keep track which file is backed up and which is not. What I am doing is to delete the entire directory which I have backed up in Allas and download the same object back to refresh the 180 days timer (mainly to keep the dependent path viable).**
    - A: There are many ways to organize your files and to keep track of what is / should be backed up and what is disposable, and you might need to do some experimenting and soul-searching to find the solution that works the best for you, but some options could be e.g.
        1. Mentally define some specific directories (say, `data`, `plots`, `scripts` and whatnot) as important, regularly back those up and commit to making sure that no important data is stored outside those directories
        1. Back up "everything" (e.g. your home directory and the project's scratch directory) but exclude some specific directories (like `tmp` or `testing` or `wip`) that you use for storing temporary files
        1. The first option, but all the important directories are contained within one directory for easy backing up (so you have one directory, e.g. `backed_up`, that contains `data`, `plots` etc)

- [x] **Q17: Is there somewhere examples and/or instruction to use the $LOCAL_SCRATCH, i have never seen this in the csc-instructions ?**
    - A: Yes, see for example here: https://docs.csc.fi/computing/running/creating-job-scripts-puhti/#local-storage
- I would need more instructions than just the one line code to be added to the job submission script, not very good if you're not advanced user
   - A: Please check this for description and relation to other storage options: https://docs.csc.fi/computing/disk/#compute-nodes-with-local-ssd-nvme-disks Do you have a specific question, e.g. what do you want to achieve? 
   - A: The ML guide has one example script: https://docs.csc.fi/support/tutorials/ml-data/#fast-local-drive-puhti-and-mahti-only

- [x] **Q18: how do you see the disk usage in ALLAS**
  - A: Our lecture/tutorial on ALLAS will come later in this course. For now, one easiest way to find ALLAS disk usage is to check on our pouta web page (HORIZON interface). First, login at www.pouta.csc.fi with your CSC account and then select a project under which you have uploaded some files to allas before. On the left hand side panel, select 'Object store' and  then 'Container' tab. You can then see different objects (within containers) you have created. If you click an object, you can then see the disk space used by the object. 

  - *a-info* command on Puhti/Mahti gives you a overview of disk space used for data objects in different buckets. Unfortunately, there is no way to check the amount of diskspace left in your ALLAS quota

- [x] **Q19: my permission was denied when trying to copy files to Mahti. I tried using my csc password, what could be wrong?**
  - A: Mahti service might not have been activated for the project you are using. You can check in MyCSC web portal.
  - - Ahh yes that makes sense. Thanks!


- [x] **Q20: Hmm I tried to run command `$echo $TMPDIR` and it outputs blank, so nothing. Is this normal ?** 
  - A: On login nodes, one should be able to see something like the following: /local_scratch/$USER.   
  - okay so there is some kind of problem, since I assume that using ssh and normally logging in to Puhti will use login node? 
  - A: yes. If you login using ssh, you will end up in login nodes 
  - What should I do to this problem ?
  - A: Problem was solved in breakout room
  - great !

- [x] **Q21 : How do I estimate time and resources that I will use when using the [billing calculator](https://research.csc.fi/billing-units)? Is it a matter of experience to know how much different jobs will take or are there examples somewhere?** 
    - A:  Time and resources are very much depend on your job. So your experience with your job can only help you. If you have jobs that take quite long time and heavy resources, you can start with small datasets and then extrapolate the resources accordingly to bigger datasets.  BUs are also computed for data storage. You can use BU calculator to get some estimates for storing data.
    - So if I have never run a job in Puhti, or in general, before, how can I estimate GPU/time etc?
    - That is challenging to get any realistic estimates without actually running your job.
    - A: As the first estimate, you could use the same time it takes for your calculation on your own computer (or whatever you are using now). The benefit of HPC is, that you can throw more resources at the same problem - either as a truly parallel job (openMP, MPI) or running many at the same time (farming). In practice, you'll learn to make better estimates with experience and if you didn't apply enough initially, you can always apply more later.

- [x] **Q22: For the completion of the course (i.e. getting the course certificate): Do I need to click also on all the ressources in the learning platform or just make the quizzes? Because the progress bar seems to depend on the resource clicking as well?**
    - The progress bar function has been acting up lately :(  Quizzes + the feedback should be enough to get the certificate. 

- [x] **Q23: How do I actually use the [billing unit calculator](https://research.csc.fi/billing-units)? The example in the quiz features GPUs as well and how do I account for those? And the billing unit calculator does not seem to combine memory and task/CPU calculation? But the quiz question only want one result?**

     - A: In the BU calculator you can add multiple jobs into a single estimate. The calculator is also a way to look at the relative BU cost of different resources (or you can look at the BU formula from Docs CSC: https://docs.csc.fi/computing/hpc-billing/ ). i.e. How significant is the CPU or Memory based billing unit cost, _if_ the job is using GPUs? Note also, that with BUs we try to encourage researchers to use the resources efficiently: reserve what you need but not more.

- [x] **Q24: Where should conda package containers be installed if we would like everyone on a project to be able to use them?**
     - A: In */projappl/<project>/*  directory. You will learn more about it later in the course
     
- [x] **Q25: I have created several buckets in Allas that each contain many files. Is it possible to compress these into a single .zip within Allas? Or what would be the best way to do this?**
     - A:  ALLAS objects are immutable  and can't be modified within ALLAS.  You have to bring the data out of ALLAS, zip it outside and upload it again. Some tools like a-put can archive (using tar) before uploading. a-put command also has compression option with ```-c```flag. More info here: https://docs.csc.fi/data/Allas/using_allas/a_commands/#a-put-uploads-data-to-allas
     
- [x] **Q26: For the first running of the task, how to approximate how much resources needed?**
     - A: Feel free to test with small resources just to see how far you can succeed with your job. It is a good idea to understand your programme/software/tool before using it. You can for example check if your program supports multiple threads/cores, needs huge/low memory or supports GPUs or not etc. These resource requirement also changes based on the amount of input data. Sometimes you have to tune your resources based on wall-clock time permissible on the partition you are using in supercomputing environment. Yes. this is a bit of exploration process in the beginning especially if you are handling complex software

- [x] **Q27: Just out of curiosity, how is the billing unit calculated in relation to the actual cost of the resources used?**
     - A: You can check the actual costs in relation to BUs in my.csc (https://my.csc.fi/billing-unit-calculator). Please note that BUs are just CSC's way of finding how much resources are being used and these resources are free-of-charge for open science research.

- [ ] **Q28: Regarding the resource usage, it would be very helpful to have a step by step guide / example how to do the calculation, testing and finally running the job. It is hard to account for all possible scenarios, but some guidelines, examples ?** 
     - A: Thanks for the feedback!

- [x] **Q29: Can I individually allocate the RAM for each core of the job?**
     - A: In SBATCH directives of your batch script you can use ```--mem-per-cpu= ```flag.  Try ```sbatch --help ```for more help.

- [x] **Q30: Simple thing, how do I open the slides in the course info page, I can see the tab, the hyperlink is working, but the slide inside is only with the first covering page**
     - A: Try navigating with the arrow keys (left and right)! :)
     - Ahh ok, sorry, didn't check the arrow keys haha

- [x] **Q31: Is this course linked to university credit system? If so, what should we do to receive the credits?**
     - A: Not directly, but you can get a course certificate, which recommends 0.5 credits. You can then take this certificate to your faculty, and they will (usually) then mark you the credits. To get the certificate, you need to complete all the quizzes in e-lena AND give the course feedback. After these steps, you should be able to download the course certificate in e-Lena.

- [x] **Q32: How do I know if I have to use collated parallel IO method or when running the simulation "normally" is sufficient? The software I use is openfoam.** 
     - A: Collated method should be used specially when number of your output/results files is large. If your mesh is large, which normally implies lot or sub domains, lot of time (or iteration) steps, and all data, including lot variables, is written on disk, then, handling writing in those numerous output files become hard for Lustre file system, which is used on CSC's servers. It is good question of where is the limit when collated method should be used. if the number of sub domains (= processes) with non-collated method become larger than 120, I would use collated method - I don't see reason why not. Feel free to contact me, so we can discuss more about your case. Esko Järvinen, CSC, esko.jarvinen@csc.fi
    
- [x] **Q33: Off-topic question: Any tips for keeping track of different versions of the models?**
     - A: If you are referring to machine learning models, take a look at [MLflow](https://www.mlflow.org/). We also have a guide on how to use MLflow on Puhti: https://docs.csc.fi/support/tutorials/ml-workflows/ 
    - Thank you for the link! Actually, my models are simpler fluid dynamics simulations but I test e.g. different meshes and then try to compare the results to see if they have any differences. Maybe github is suitable for this kind of version control?
    - **(not an instructor)**: Hi, I do work on the same topic using `OpenFOAM` and I rely heavily in `git` for version control of models. As long as your code uses text based files as input it works very well. Just be careful with the amount of information you're uploading. For example, I avoid uploading any results.
    - Tip: Code Refinery offers some training and tips related to version control, they have one course ongoing at the moment, and you can hop on-board :) https://coderefinery.org
        - **(same not instructor)**: is this course only online? A: Yep, I think so! Code Refinery has this pretty effective & nice "whole world is invited" approach to their knowledge sharing <3. Thanks!! I'll be there :-)
    - Thank you for the tips!
    

    
    
    
---
**:arrow_up: Write your questions above this line :arrow_up:**

---


**Testing area:** Here you can test how to use HackMD :)
test *test* **test**
(?) 
*test by H

Testing - A

Hello world

Test

testi

:)


---





## Useful links 
- [Elements of Super computing](https://edukamu.fi/elements-of-supercomputing) online course
- [Training links](https://docs.csc.fi/support/training-material/#training-materials-and-sources-from-csc-and-partners) by us and our friends
- [Weekly research user meetings](https://ssl.eventilla.com/usersupportcoffee) (come and ask anything!)
- [Data management self-learning course](https://e-learn.csc.fi/course/view.php?id=63)
- [Practical Deep Learing course](https://ssl.eventilla.com/event/8aPek)
- [Sensitive Data (SD) services webpage](https://research.csc.fi/sensitive-data)
- [Sensitive Data (SD) services user guide](https://docs.csc.fi/data/sensitive-data/)