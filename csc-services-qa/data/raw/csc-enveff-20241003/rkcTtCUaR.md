# Using CSC HPC environment efficiently, Part 1: Basics 3.-4.10.2024 

###### tags: `puhti` `mahti` `allas`

:::warning
Link to this document: https://hackmd.io/@CSCBioMaria/rkcTtCUaR/edit
:::

> This is the collaborative "notebook" for the "Using CSC HPC environment efficiently" basics course organised in October 2024 by CSC -IT center for Science. 
> [Prerequisite course page in eLena platform](https://e-learn.csc.fi/course/view.php?id=75)
> [Course page in eLena platform](https://e-learn.csc.fi/course/view.php?id=76)
> [Collection of slides and material](https://csc-training.github.io/csc-env-eff/)
> [Zoom-link for COURSE sessions](https://cscfi.zoom.us/j/61107561518?pwd=BaAsGEGtU1TWcwlUVkd84oB4J04h2N.1)
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

### Prerequisite / support session 25.9.
14:00-15:00 Join the pre-course support session, which is also part of [CSC's weekly user meetings](https://cscfi.zoom.us/j/65059161807)

### Day 1: Thursday 3.10.
 
 
| Time  | Content |
|-------|---------|
| 8:45  | Login, check connections work, test microphone |
| 9:00  | Welcome, course practical info, learning targets,  ice-breaker, feedback/expectations (15 min) |
| 9:15  | **Topic 1: Prerequisites & Connecting** (15 min) |
| 9:30  | **Topic 2: Introduction to HPC Environment** (20 min) |
| 9:50  | _Break_ (10 min)|
| 10:00 | **Topic 3: Disk Systems** (15 min) |
| 10:15 | **Intro to breakout rooms & hosts, joining the breakout rooms, accessing materials** (10 min) | 
| 10:25 | **Topic 3: Hands on 3.1** (20 min) |
| 10:45 | **Going through the hands-on(s) together** (15 min)|
| 11:00 | _Break_ (10 min) |
| 11:10 | **Topic Topic 7:  Allas and where to keep your data (** (25 min)|
| 11:35 | **Topic 7: Hands on 7.1** (15 min)|
| 11:50 | **Going through the hands-on(s) together** (10 min)|
| 12:00 | Finish |




### Day 2: Friday 4.10.
    
    
| Time  | Content |
|-------|---------|
| 8:45  | Channel open, "morning coffee" |
| 9:00  | Re-cap, feedback/expectations + some Qs from HedgeDoc (5 min) |
| 9:05  | **Topic 4: Module system** (15 min)|
| 9:20  | **Topic 4: Hands on 4.1** (20 min) | 
| 9:45 | **Going through the hands-on(s) together** (10 min)|
| 9:55 | _Break_ (10 min)|
| 10:05 | **Topic 5:  Batch queue system and interactive use**  (15 min)|
| 10:20 | **Topic 5:** Hands on 5.1 (20 min) |
| 10:45 | **Going through the hands-on(s) together** (10 min)|
| 10:55 | _Break_ (10 min) |
| 11:05 | **Topic 6: Understanding resource usage** (20min)|
| 11:25 | **Topic 6: Hands on 6.1** (20min) |
| 11:45 | **Going through the hands-on(s) together** (10 min)|
| 11:55 | Recap (5 min)|
| 12:00 | Finish |





---



## ☃️ ICE BREAKER (HackMD -practice)

### Ice breakers
Let's learn how to use this HackMD document by answering an ice breaker question! 


    
**Q1: What topic of this course are you most excited about?**

**Answers:**

* Getting familiar with working in Allas and Puhti.
* Just starting with some order and maybe the folder organization 
* To know how supercomputing can help my career
* Puhti and Allas
* puhti and allas
* Submitting batch jobs and allocating resources
* HPC overview!
* Just overal more smooth usage of Puhti
* How to store and fetch data from Allas and also how to do high throughput calculations
* Getting started and overview of the system
* Allas!
* Basics of supercomputing for data science tasks.
* Puhti and Allas!
* Sbatch
* Learning how to use Puhti efficiently
* Learning how to use CSC resources efficiently
* How to optimize the use of nodes and memory for your jobs
* All
* 

## 📝 Q & A

Your questions are answered here. We will answer them, and this document will store the answers for you for later use! :rocket: 

:::info
Scroll :arrow_down: to the bottom of the page to submit a question 
:::



- [x] **I have difficulty pasting my questions into HackMD (here). Do you have some instructions on how to write here?**

    - A: HackMD can look a bit differend depending on the view you are in. Can you see the three icons on top left corner, next to HackMD text? There’s pencil, this side-by-side symbol, and an eye (see below for a screenshot). In eye view, you can’t edit, you are just viewing. The other two reveal the markdown (MD) version of the page, which you can edit. I find it easiest to edit with the side-by-side view, but it can be a bit slow sometimes. First time opening the page, the small Edit (pencil) button might be on right next to the table of contents. Please note that it might make things faster if you **switch to view only mode when not editing**!

:::info
The small pencil icon for entering edit mode for the first time. You might need to scroll all the way up to see it.

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
    - A: This time: Yes. However, we don't promise to deliver them afterwards, as they will require editing and captioning, which takes time. Slides and hands-ons are available in the [github page](https://csc-training.github.io/csc-env-eff/), and all the material + the quizzes etc can be accessed in [eLena platform](https://e-learn.csc.fi/course/view.php?id=76), so this course works well as self-study also!  


- [x] **Q8: There's no "Sep24" option in e-Learn...?**
    - A: Good catch! Now there is, except it's Oct24, as it is actually October now :D

- [x] **Q9: Do I get a notification that my csc account will be locked soon?**
    - A: CSC sends an e-mail once a year requesting you to reset your password. Failure to reset the password will automatically lead to the locking of your account. CSC service desk (servicedesk@csc.fi) can help you if your account is locked for any reason.


- [x] **Q9: What actually are remote graphics?**
    - A: Here, we mean any graphical application that is running on HPC environment. So it is like accessing a GUI tool (for example Jupyter notebook) on your personal computer browser (i.e., local environment) while the tool is running on a remote enviroment (e.g., HPC environment)


- [x] **Q10: Regarding the folder organization, I am lost on what is the folder ondemand? What is scratch?**
    - A: You will learn more about these folders later. Open ondemand folder refers to the folder on supercomputer web interface. Scratch folder refers to a type of diskspace that a CSC user gets on supercomputers. (FYI, Open ondemad is a technology that allows building web interfaces to supercomputers )

- [x] **Q11: Can we have some SSH files as examples to learn how to compile commands?**
    - A: do you perhaps mean these compile commands here: https://docs.csc.fi/computing/connecting/ssh-keys/ ? We have a good documentation on how to set up SSH keys.

- [x] **Q12: Can I see the difference between the login nodes or supercomputer nodes. On the folders of my project I can't see the tmpdir**
    - A: Once you login to supercomputer, you will be automatically in login nodes. HOME/Projappl/Scratch folders are available on login and compute nodes. so there is no difference for these folders on parallel file system. However Temporary folder is different.  You have to refer to $TMPDIR (try `echo $TMPDIR` to see the exact path) on login node and $LOCAL_SCRATCH on compute node.
    - A: Note that $LOCAL_SCRATCH is available only if resources for it have been specifically requested in the batch job script or when starting an interactive session. More on this tomorrow.

- [x] **Q13: Which data storage should be used to install additional python libraries, virtual environments ?**
    - A: You will learn more about it later. Short answer is /projappl area for your project.

- [x] **Q14: when do we use chmod and/chown to give access to files in subfolders to other group members?:)**
    - A: By default the files and directories you create in /projappl and /scratch are accessible to all group members. You can use chmod to reduce the prermissions to your data. E.g. you could make a directory to be "read.only" for other project members with command   chmod -R g-w your-directory

    - Having a scratch directory, where only you have an access is not a good idea because if you later on leave from the CSC project, no one will have access to the data.

- [x] **Q15: How can I get files from my computer to Puhti? Can I wget them or which command should I use? Some universities don't give permission to download SSH-client to employees' own user but rather to a admin user which then again don't have the files for the analysis.**
    - A: Next lecture is more about data transfer. We will learn more about that. There are many protocols/transfer clients that one can use to transfer data to Puhti. if the clients need admin permissions for installation, I would suggest asking admins to install them on your computer.
    - A: Check https://docs.csc.fi/data/moving/.

- [x] **Q16: can i delete the files we used in the hands on or do we use them later?**
    - A: They can be deleted. We won't need them later.

- [x] **Q17: Will the use of Allas in this tutorial take any extra BU consumption** 
    - A: Not really. The files are small and can be deleted after the exercise. The usage is calculated by TB.

- [x] **Q18: Should I always transfer local files to Allas first, then move them to Puhti/Mahti?**
    - A: No need to move the data to allas first. But making data available in allas makes it convenient to move around different services quite quickly ad easily.

- [x] **Q19: What would be the best method of moving large amount of individual files to an Allas bucket?**
    - A: `rclone` with (-P flag, for progress ) would be one option. 

- [x] **Q20: Can you describe it again how to get the certificate after training sessions**
    - A: In e-Lena e-learning portal, you need to complete all the quizzes in part1, and give the course feedback. After these steps, the certificate should show up, and you should be able to download it!

- [x] **Q21: How long can we store our data in Allas?**
    - A: For the duration of your computing project. When the project is about to end, you need to download and store the data somewhere else, or extend the project. See https://docs.csc.fi/accounts/how-to-manage-your-project/
    - Note: the **course project** is only valid during the course! It's also not meant for your own use, so don't upload any own files there!

- [x] **How can we search the modules that are installed in Puhti/Mahti**
    - A: The vast majority of all applications installed on CSC systems are implemented as modules, so the [applications list in CSC documentation](https://docs.csc.fi/apps/) serves as a pretty comprehensive description of available modules.
However, due to the large number of installed software, some modules may not have a documentation page. `module avail` shows all available modules (such that you can load directly without first loading some dependencies), `module spider <pattern>` allows searching for specific ones and also listing all modules, including those that cannot be loaded currently due to missing (not loaded) dependencies. See also answer below.
   - A: `module spider` with no arguments shows all installed modules, but since the list is quite long it may not be that practical.
   - A: In this tutorial, even though bio-related, we go though a bit how to search for applications: https://csc-training.github.io/csc-env-eff/hands-on/modules/module-exercise-with-aligners.html

- [x] **Q23: `module load StdEnv` # Load the default module environment -> what is dfault module environment**
    - A: On Puhti it is `gcc/11.3.0`, `openmpi/4.1.4`, `intel-oneapi-mkl/2022.1.0`, `csc-tools`. In other words, it contains a specific compiler suite (gcc/11.3.0), MPI library (openmpi/4.1.4), linear algebra library (intel-oneapi-mkl/2022.1.0) and some tools developed by CSC (csc-tools).
    - A: `module list` shows currently loaded modules, so you can always run that before and after a `module` command to see what changed.
    - A: You can also try `module show StdEnv` to see what loading the module does.

- [x] **Q24: So when I log into Puhti, which project's BUs am I using if I have several ongoing projects? Can I move between projects to allocate my BU usage?**
    - A: Project BUs are consumed when you run jobs (or have extended the project's maximum available storage space). For this reason, the only obligatory argument to provide when running jobs is the accounting project i.e. the CSC project whose BUs will be used for the job. So the project to be billed must always be specified.

- [x] **Q25: What are the best settings (number of CPU, memory, image quality, and compression) for using the desktop in Puhti/Mahti and running programs like ParaView with a graphical interface? It has several settings, but the default ones are not good for smooth performance.**
    - A: For ParaView, I would recommend trying the accelerated visualization, since it allows the software to run and render on GPUs. The performance will this way be significantly improved. To see all apps with accelerated visualization available, see https://docs.csc.fi/computing/webinterface/accelerated-visualization/
    - A: Memory is a bit tricky to predict beforehand, this may depend on a case-by-case basis. The GPU nodes have 384 GB memory in total, so when reserving 1 GPU (out of the 4 available in total on a node), you can safely reserve up to 1/4 of the total memory (~90 GB).
    - A: If responsiveness is the main goal, higher compression may help in some cases. Then again, if accurate visual representation (while using the desktop) is important, compression should be as low as possible. 

- [x] **Q26: Can we access this HackMD file after the training ends? It would be nice to have access to it. (i.e as PDF)**
    - A: Yes. This HackMD page stays here after the training ends. Feel free to export these HackMD pages for example to your google drive or download as HTML/markdown files

- [ ] **Q27: The last question in the Quiz: Module system (load Gromacs module) appears to be out of date - it refers to "gromacs-env/2023" which is now "gromacs/2024.3", and the loaded versions of "gcc", "intel-oneapi-mkl", and "openmpi" are also more recent than those listed in the answers.**
    - A: Good catch, we'll update this after the course (we cannot do it now since it will reset your progress). Thanks for reporting!

- [x] **Q28:If my batch run takes e.g. 12 hours, can I just shut off Puhti (with e.g. exit-command) and my computer and the job stays running? Or is there a special command that is needed to shut the system AND keeping it running?**
    - A: Yes. Once you submit your job with your batch script, you can log out of the supercomputer. Your submiited job stays in queue and when it gets the requested resoures your job will be executed on the cluster (on compute nodes). You don't need to do anything else than just submitting job which will be run irrespective of whether you are logged in or out of the supercomputer.

- [x] **Q29: If only there were some convenient way of monitoring job progress...**
    - A: `tail -f slurm-<job_id>.out` (watch the output file and print any new lines written to it). You may also replace `slurm-<job_id>.out` with any other log file that your job might be outputting.
    - A: You can also monitor your jobs in the queue with `squeue --me` (equivalent to `squeue -u $USER`), but don't run it too often since the command can be heavy on the batch job system (especially with hundreds of users using the system at the same time).

- [x] **Q30: how do i know which queue to use? in the hands-on the test-queue**
    - A: You can find the information about partitions/queues on CSC documentation : https://docs.csc.fi/computing/running/batch-job-partitions/. Each queue has its own specific cofigurations. Depending on the your use case, select the one that suits the best.  For example if you need GPUs for your job, there are partitions for GPUs: gpu and gputest. You can also type `sinfo -s` on the commandline terminal on Puhti to see similar information. Just for insights, these partitions are made out of different needs of diverse set of jobs that users would have in HPC environemnt.

- [x] **Q31: How often do you have the Part2: Next steps-course?**
    - A: We TRY to have Part1 and Part2 twice a year, so one round in Oct-Nov and another in April-May. My advice: register for the next round, and repeat in spring if need be :)
    

---
**:arrow_up: Write your questions above this line :arrow_up:**

---

## Feedback day 1

One thing you liked:

- I found the tutorial on how to use Allas very useful 
- I just realized the function of Allas. I wondered why on my project dashboard there was an Allas, even though I only used Puhti
-


## Feedback - Day 2

One thing you liked:

- Well organized, starts from the very basics (which is needed). Hands-on excercises were an important feature. 
- HackMD is a very good tool!

One thing that could be improved:

- 
- ..



:::info
When you have time, please give us feedback also through the Official Feedback Form: https://ssl.eventilla.com/feedback/101HPkObr2MgbK6

(This is required to get the course certificate, in that case, give the feedback thru e-Lena!)

:::



## Useful links 
- [CSC Computing Environment Part2 : Next steps](https://csc.fi/en/training-calendar/online-csc-computing-environment-part-2-next-steps-3/) Registration now open!!!
- [Elements of Supercomputing](https://edukamu.fi/elements-of-supercomputing) online course
- [Training links](https://docs.csc.fi/support/training-material/#training-materials-and-sources-from-csc-and-partners) by us and our friends
- [Weekly research user meetings](https://ssl.eventilla.com/usersupportcoffee) (come and ask anything! Also course related questions are welcome!)
- [Data management self-learning course](https://e-learn.csc.fi/course/view.php?id=63)
- [Sensitive Data (SD) services webpage](https://research.csc.fi/sensitive-data)
- [Sensitive Data (SD) services user guide](https://docs.csc.fi/data/sensitive-data/)