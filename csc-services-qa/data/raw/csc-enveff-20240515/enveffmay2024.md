# Using CSC HPC environment efficiently, Part 2: Next steps  15.-16.5.2024 

###### tags: `puhti` `mahti` `allas`

:::warning
Link to this document: https://hackmd.io/@CSCBioMaria/Bk00RUSdp
:::

> This is the collaborative "notebook" for the "Using CSC HPC environment efficiently" "advanced" course organised in May 2024 by CSC -IT center for Science. 
> [Prerequisite course page in eLena platform](https://e-learn.csc.fi/course/view.php?id=75)
> [Course page in eLena platform](https://e-learn.csc.fi/course/view.php?id=76)
> [Collection of slides and material](https://csc-training.github.io/csc-env-eff/)
> [Zoom-link for COURSE sessions](https://cscfi.zoom.us/j/66502128121?pwd=MnVWcGNMT0p1Mlp6SzJZbzNVeVFGUT09)
> [Zoom-link for SUPPORT sessions / weekly user meetings](https://cscfi.zoom.us/j/65059161807)

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

### Prerequisite / support session 8.5.
14:00-15:00 Join the pre-course support session, which is also part of [CSC's weekly user meetings](https://cscfi.zoom.us/j/65059161807)

### Day 1: Wednesday 15.5.
 
 
| Time  | Content |
|-------|---------|
| 8:45  | Login, check connections work, test microphone |
| 9:00  | Welcome, course practical info, learning targets,  ice-breaker, feedback/expectations (15 min) |
| 9:15  | **Topic 8: Working efficiently with data** (25 min) |
| 9:40  |**Intro to breakout rooms & hosts, joining the breakout rooms, accessing materials** (5 min)|
| 9:45  | **Topic 8: Hands on 8.1** (25 min)|
| 10:10  | _Break_ (10 min)|
| 10:20 | **Going through the hands-on(s) together** (10 min)|
| 10:30 | **Topic 9: Installing applications** (20 min) |
| 10:50 | **Topic 9: Hands on 9.1 and 9.2** (15 min)|
| 11:05 | _Break_ (10 min) |
| 11:15 | **Topic 9: Hands on 9.1 and 9.2 continued** (15 min)|
| 11:40 | **Going through the hands-on(s) together** (15 min)|
| 11:55 | Recap + preparations for the next day (5 min) |
| 12:00 | Finish |
| 14:00 | Bonus: Join the weekly user meeting https://cscfi.zoom.us/j/65059161807  |



### Day 2: Thursday 16.5.
    
    
| Time  | Content |
|-------|---------|
| 8:45  | Channel open, "morning coffee" |
| 9:00  | Re-cap, feedback/expectations + some Qs from HedgeDoc (5 min) |
| 9:05  | **Topic 10: Containers & Apptainer** (25 min)|
| 9:30  | **Topic 10: Hands on 10.1** (30 min) | 
| 10:05 | _Break_ (10 min)|
| 10:15 | **Going through the hands-on(s) together** (15 min)|
| 10:30 | **Topic 11:  How to speed up jobs**  (30 min)|
| 11:00 | _Break_ (10 min) |
| 11:10 | **Topic 11:** Hands ons 11.1 (35 min) |
| 11:40 | **Going through the hands-on(s) together** (15 min)|
| 11:55 | Recap (5 min)|
| 12:00 | Finish |


---



## ☃️ ICE BREAKER (HackMD -practice)

### Ice breakers
Let's learn how to use this HackMD document by answering an ice breaker question! 


    
**Q1: What topic of this course are you most excited about?**

**Answers:**

* type here 
* How to speed up jobs! 
* installing my own software on puhti
* How to efficiently handle large datasets +2
* How to speed up jobs
* Learning some basic apptainer syntax
* Containers
* Installing software
* How to handle large data
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
The bigger HedgeDoc/HackMD toolbar for switching between modes later on.
![The toolbar from which the different modes can be accessed. You can also switch between edit and view mode using hotkeys ctrl-alt-v and ctrl-alt-e respectively](https://hackmd.io/_uploads/HJyCrkgj6.png)
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

- [x] **Q7: Do you record the sessions?**  
    - A: No. However, the lecture videos, slides and hands-ons are available in the [github page](https://csc-training.github.io/csc-env-eff/), and all the material + the quizzes etc can be accessed in [eLena platform](https://e-learn.csc.fi/course/view.php?id=76), so this course works well as self-study also!  


- [x] **Q8: What counts as heavy I/O? Opening 10/100/1000 files?**
    - A: We will get back to this topic tomorrow when talking about workflows and speeding up jobs. But as a rule of thumb, pay attention when opening 1000s of files and you should **not** work with 10 000s-100 000s on Lustre. Working with 10-100 files is not a problem usually.

- [x] **Q9: What counts as a "small file"? Does the file format matter?**
    - A: It is hard to give an exact number, but small files typically refers to kB order of magnitude. File format does not really matter.

- [x] **Q10: Do the small files cause issues if they're idle, or are they only an issue if they're constantly being accessed?**
    - A: They can also cause issues even if they are idle. Especially having a lot of files in a single directory is not recommended. Having some kind of hierarchy is better (or even better, tar and compress the files).

- [x] **Q11: Why would we use the allas-conf -k instead of establisheing an S3 connection?** 
    - A: As you would probably have realised that S3 connection is persistent, this may have security concerns. Swift connection is more secure as you refresh for every 8 hours.
    - A: in addition to the above, using S3 protocol is OK if you use it all the time, but if you have uploaded the data using Swfit protocol, then you should also download it with Swift protocol.

- [x] **Q12: What should I do if there is data in our scratch from a previous user that I cannot delete?**
    - A: You should send a ticket to <servicedesk@csc.fi>. Our admins can edit the permissions.

- [x] **Q13: What do I do with data in scratch that we work with for more than 6 months?**
     - A: Unfortunately, cleaning process will be in force on Puhti and is bit incovenient if you are in the middle of some analysis. As mentioned in the lecture, if you have lot of data, please move them to allas during cleaning process. To ease this process, CSC has provided some easy-to-use utility commands like lcleaner (https://docs.csc.fi/support/tutorials/clean-up-data/#using-lcleaner-to-check-which-files-will-be-automatically-removed). If the data is small enough and is mixed with program/config files, you might use /projappl space (which is more dedicated for storing compilied programs/packages/installation stuff). /projappl space will not be cleaned. 
     

- [x] **Q14: So you need to do allas-conf -k only once or again each time you login with ssh? And again if you change the project you work on?**
     - A: Once you logout from supercomputing environement, the env variable that stores your password will be unset.  
     - **Q: Did I get it right, if I execute batch-script and before the run starts my laptop for example loses internet connection hence the ssh connection breaks, the batch job wont have the allas access?**
     - A: Once you submit your batch script (which has already access to your allas credentials), that is fine. Your loosing connection to supercomputer later from laptop will not affect the already running batch job.  
     - Q: already running batch job = batch job in que / actually running?
     - yes. to be precise, it is enough that you have submitted the job to the cluster.
     - great, thanks
     - you are welcome !

- [x] **Q15: Is $LOCAL_SCRATCH the NVMe?**
     - A: Yes, that's correct.
     - **Q: If we reserve NVMe does the code run only there? What if we don't reserve enough and it runs out? How can we know what space we need, just the amount of storage of the files we want to process?**
     - You have to reserve NVMe disk space in your batch script and move your data to the local disk area (i.e., NVMe disk area) and compute there. Once you finish your heavy I/O computation there, you have to move all your results back to parallel file system area (i.e., scratch). In short, you have to intentionally do the computation on NVMe and it does not happen there just because we reserve NVMe disk space. Yes. if we dont have enough space in NVMe, your batch job fails. It is difficult to know exact amount of NVMe space needed beforehand. It depends on your application input data and resulting data from your analysis. You can request bit more disk space than you need to be on  safe side. 

- [x] **Q16: NVME billing is pretty expensive, why is it billed so heavily in BUs?**
     - A: NVMe is a scarce resource on CSC supercomputers, that's why it is more expensive than regular disk space. A little bit like GPU-resources.
     - A: You can check NVMe availability per node type in https://docs.csc.fi/computing/systems-puhti/

- [x] **Q17: What are binaries?**
     - A: They are programs that you can run. Like a command. Some programming languages are intepreted, so you can just run the code itself. However, many codes need to be first compiled into a program (a binary, a.k.a. executable).
     - **Q: By programming langauges, do you refer to the language that the progrom was written in?**
     - A: Yes. For example, C code needs to be compiled into a binary while Python code can be run as is. 

- [x] **Q18: Why should we compile software in $TEMPDIR first and then move it to projappl? Can't we do it in projappl directly? Do we also need to install a software there and then move it to projappl, or can we install it to projappl directly?**
     - A: Because compilation usually creates a lot of I/O load. So moving that away from Lustre to the login node NVMe is recommended - it will make the compilation faster and does not cause lags in Lustre for others.
     - If the software is very simple and small, you could do compilation directly in /projappl as well.
     - No need to *install* in $TMPDIR, just *compile* it there, and then there are usually options you can give the build tools that install the software to /projappl when you run e.g. `make install`. See the tutorials for more details about this. E.g. `./configure --prefix=/projappl/...` and `-DCMAKE_INSTALL_PREFIX=/projappl/...`

- [x] **Q19: I installed the development version of a R-package from github. It's a newer version than that available in CRAN and already installed in Puhti. How do I get the development version to work in Puhti? I have got this working on my own laptop, but not in Puhti.**
     - A: Did you check the tutorial? https://csc-training.github.io/csc-env-eff/hands-on/installing/installing_hands-on_r.html
     - A: if there are some errors, seeing those messages would helpful.

- [x] **Q20: Is it possible to create a container that would be under the project, not under a specific user? I would wish that all project users have similar access to it.**
     - A: Sure! Just move it to a shared directory under your project's /projappl
     - A: Access permissions can be edited with `chmod` commands. E.g., to give all project members execute permissions for the container, try `chmod g+x my_container.sif`
     - Thank you!

- [x] **Q21: Should bin be lib able to find the libhello.so? I think there's a mistake in using CMake exercise**
     - A: Yes, sorry about that!
     - A: If you reload the page, this should now be fixed.

- [x] **Q22: If we're queuing for a  batch job, is there a way to estimate how much we would wait or our position in the queue?**
     - A: Yes, you can add option `--start` in you `squeue` command (e.g. `squeue --me --start`) to see an estimate of when the job will start running. However, this is only a rough estimate and it may change depending on what jobs are submitted later on that may have a higher priority.

- [x] **Q23: What are the login nodes available on puhti, i couldn't find a list of them or how to access a certain node in the docs.csc website about the disk areas or elsewhere. I'm currently on node 12 for example**

     - A: They are `puhti-login11`, `puhti-login12`, `puhti-login14` and `puhti-login15` (https://docs.csc.fi/support/wn/comp-new/#new-login-nodes-on-puhti-9112022). You can for example go to specific login node on Puhti by specifying the login node information as : *ssh username@puhti-loginxx.csc.fi* (xx-> 11,12,14,15) 

- [x] **Q24: What is a container engine and what does it do?**
     - A: It is a piece of software that is used to build and run containers
     - Q: If a container was built using a different engine than Apptainer that CSC uses, do we need to use this apptainer build command, or is it for something else? I'm not sure I understand the function of this command. 
     - You can think of container engine as some management system for containers: it can for exmaple spins up, cancel your containers when needed.  It is container specific. Docker container engine just manages docker containers on host system and not for other containers.  
     - A: However, it is easy to convert Docker containers to Apptainer containers. It is often just a single command, see e.g. https://csc-training.github.io/csc-env-eff/hands-on/singularity/singularity-tutorial_how_to_get_containers.html
     - Q: What do you mean by "spin up, cancel your containers when needed"?
    
- [x] **Q25: Do we need to bind a directory every time we run the software, or is this something that can be setup permamnently for a container?**
     - A: It depends. You need to bind or mount a host file system when you are trying to write something permanently on disk. Just for running some command, you don't need to bind  a file sytem.  Host system always needs to be mounted during runtime.
     - Q: How could we bind it permanently? For example, to have the software always be able to acces my files when i use it to submit batch jobs.
     - There seems to be some misunderstanding here. Once you mount a host folder under container, it will be there as long as container is running. So one does not need to do anything. But for some reason, if container dies, one needs to bind them again.
     - Instead of using --bind you can set APPTAINER_BIND variable. Syntax is the same as for --bind `export APPTAINER_BIND="dir1,dir2:/input`. This may make the command more readable if you have complex bind.
    
- [x] **Q26: Could you please confirm if Tykky environments are only suitable for python/conda packages?**
     - A: Yes, you can also install other than Python/Conda stuff with tykky. `conda-containerize update` command allows you to run any installation commands (e.g. clone repo from GitHub and install something). `wrap-container` command can also be used to generate wrapper scripts for an existing container. See https://docs.csc.fi/computing/containers/tykky/#modifying-a-conda-installation and https://docs.csc.fi/computing/containers/tykky/#container-based-installations

- [x] **Q27: What output should we expect from step 2 under 'using the `apptainer wrapper` script' section in the second tutorial? It doesn't return anything for me and im not sure i understand what the second command does.**
     - A:  *Apptainer_wrapper* command binds many host directories(``` /projappl, /scratch,$HOME... ```) by  default. So if your env variable, `$`SCRATCH refers to some directory under your project (e.g., ``` /scratch/project_xxx/$USER```), you should be able to see all the content inside of the host folder (i.e.,/scratch/project_xxx/$USER)
    - Can you try directly using actual path (instead of as env variable) like in the command: ```apptainer_wrapper exec ls /your/scratch/path ``` ?
    
- [x] **Q28: When in sinteractive and we're running a container, are we able to submit batch jobs for more processing power**
     - A: Yes. You can submit batch jobs from interactive nodes.
    
- [x] **Q29: If I start an array job with four arrays, the output file will only show the billing unit consumption of one array (~1/4 of the total). Is there a way to see the BU consumption of the whole array job?**
     - A: Did you use seff command to find the BUs? By default, seff gives information on the first array job. You can also try `seff <jobid>_1, seff <jobid>_2, seff <jobid>_3 ...`   You can also try using *sacct*  command for more details on job at a time  (`sacct -o jobname,jobid,reqmem,maxrss,timelimit,elapsed,state -j <slurmjobid>`) 

- [x] **Q30: Do many large files also pose a problem?**
     - A: For large files, parallel file system is still better.  The real problem is with metadata handling. For the given data, if you supply in many small files, file system has to do many file I/O operations as comapared to the operations needed in hanlding teh same data in few bigger files. 
     - Q: What if our data was a several thousand large files? Does the same thing apply? 
     - Yes. Metadata operations will be increased accordingly.There are some better optimisation methods like *file striping* can be done on parallel file system to mitigate the issues. The issue is also not just the size of files, but also how many operation you are eventually doing with that big files. if you are accessing bigger files several times as part of cmputation, this is different thing than the accesing the file once during the computation.  Other things like accessing some data randomly from some part of  files do matter.
    
- [x] **Q31: Sorry about the long question, I'd just like to confirm that I understand it correctly, does using NVMe solve the problem with the many small files? (where it's just used to store the intermediate data during processing? because in that case then the software still has to access the same amount of large files so I'm a bit confused. Or are we supposed to move the data into the NVMe beforehand?)  And that would be in terms of the data we're running. And then when it comes to the software, if it has a lot of files in and of-itself, we need to use it in a container. These two things are ways to go around the 'large number of file' problem but for two separate scenarios?**
     - A: The idea when using NVMe would be for example this: 1) you have a tar-package containing a lot of small files you need to process. You do not want to do it on Lustre, because it would be inefficient. 2) Instead, you copy the package containing the files to NVMe and only then decompress it (so that you at no point have a lot of files on Lustre). 3) On the NVMe, you process the data. 4) When you're done, you package the results and move them back to /scratch.
     - A: This could be done either in an interactive session or in a batch job. But yes, the important thing is that you need to *move* the data first to NVMe, and then also remember to move it back (because the NVMe is cleaned automatically immediately when the job ends).
     - A container is another way to mitigate the large file number, since a container is just 1 file from the file system point of view.
     - **Q: Would this still be practical if we have really large files? the packing and unpacking, would it perhaps take a couple of hours for some amount of TB in data?**
    
- [x] **Q32: srun: fatal: SLURM_MEM_PER_CPU, SLURM_MEM_PER_GPU, and SLURM_MEM_PER_NODE are mutually exclusive.!, I get this error in the first exercise for speeding up jobs, Performing a simple scaling test. Did I typo something?**
     - A: Probably. Did you launch the job from an interactive session? You should be on the login node, otherwise there may be some issues.
     - Q: Thanks that was the issue, I was in a interactive session.

- [x] **Q33: Do jobs submitted with HyperQueue inherit $PATH from the session where they are launched? In other words, I have snakemake and other software in a container that I created with Tykky. I want to tell snakemake to submit jobs with HyperQueue. Will these jobs see the software that is inside the container? PS: I could also have the container as an apptainer image made from a docker image, it this would work somehow instead of the wrapper scripts from Tykky.**
     - A: Did you check our tutorial here: https://docs.csc.fi/support/tutorials/snakemake-puhti/ ? 
     - We also have a dedicated tutorial, combing Hyperqueue and singularity container image in snakemake workflow here: https://csc-training.github.io/csc-env-eff/hands-on/throughput/snakemake-ht.html
     - A: I have not, will take a look, thank you! I had tried before with snakemake+SLURM and it didn't work so I found another sub-optimal alternative. It seems that HQ should work :)
    - CSC docs covers different possible scenarios including the case of  snakemake+slurm. please check it. If you have too many jobs (rules) from bigger sample set, we recommend using HyperQueue. 
    - A: Great, thank you!


     

> **THANK YOU very much for your active participation! Questions are now closed. Feel free to ask more at servicedesk@csc.fi and/or join our [weekly research user meetings](https://ssl.eventilla.com/usersupportcoffee)**



---
**:arrow_up: Write your questions above this line :arrow_up:**

---

## Feedback day 1

One thing you liked:

- *Installing your own software*. I liked the material but I missed an explanation on how to install our own modules. That is, compiling our own software and then creating module files instead of modifying the environmental variables from bash.
    - A: Thanks a lot for this feedback! This is a nice idea, and something we surely should add to one of the tutorials :)
    - For general info on modules, including a few words of own modules as well, see https://csc-training.github.io/csc-env-eff/part-1/modules/
    - Thanks for the prompt reply! Just to be clear, this is a minor thing. You're doing a great job at making the use of supercomputers more accessible :-) 
    - **We added a simple tutorial for this as part of the CMake tutorial**, https://csc-training.github.io/csc-env-eff/hands-on/installing/installing_cmake.html

- The more relaxed pace of today was quite helpful in digesting and processing the information. Thanks! +3
- 

## Feedback - Day 2

One thing you liked:

- Really impressive and admirable that you created a tutorial for installing own modules so quickly after the feedback was given!
- 

One thing that could be improved:

- I feel that a break after going through the exercises together, i.e. before moving to the next topic, is nicer. E.g. keeping the practice and going through it together as one "cluster". Makes the course more structured.
- ..



## Useful links 
- [Elements of Supercomputing](https://edukamu.fi/elements-of-supercomputing) online course
- [Training links](https://docs.csc.fi/support/training-material/#training-materials-and-sources-from-csc-and-partners) by us and our friends
- [Weekly research user meetings](https://ssl.eventilla.com/usersupportcoffee) (come and ask anything!)
- [Data management self-learning course](https://e-learn.csc.fi/course/view.php?id=63)
- [Sensitive Data (SD) services webpage](https://research.csc.fi/sensitive-data)
- [Sensitive Data (SD) services user guide](https://docs.csc.fi/data/sensitive-data/)