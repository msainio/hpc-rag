# Using CSC HPC environment efficiently "basics level" 7.-8.2.2024 

###### tags: `puhti` `mahti` `allas`

:::warning
Link to this document: https://hackmd.io/@CSCBioMaria/Bk00RUSdp
:::

> This is the collaborative "notebook" for the "Using CSC HPC environment efficiently" course organised in February 2024 by CSC -IT center for Science. 
> [Prerequisite course page in eLena platform](https://e-learn.csc.fi/course/view.php?id=75)
> [Course page in eLena platform](https://e-learn.csc.fi/course/view.php?id=76)
> [Collection of slides and material](https://csc-training.github.io/csc-env-eff/)
> [Zoom-link for sessions](https://cscfi.zoom.us/j/64669968672?pwd=NGtxVWhuWVFHR2lvSHU1Y3o2RVlQdz09)
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

### Prerequisite / support session 31.1.
14:00-15:00 Join the pre-course support session, which is also part of [CSC's weekly user meetings](https://cscfi.zoom.us/j/65059161807)

### Day 1: Wednesday 7.2.
 
 
| Time  | Content |
|-------|---------|
| 8:45  | Login, check connections work, test microphone |
| 9:00  | Welcome, course practical info, learning targets,  ice-breaker, feedback/expectations (20 min) |
| 9:20  | **Topic 1: Prerequisites & Connecting** (15 min) |
| 9:35  | **Topic 2: Introduction to HPC Environment** (20 min) |
| 9:55  | _Break_ (10 min)|
| 10:05 | **Topic 3: Disk Systems** (15 min) |
| 10:20 | **Intro to breakout rooms & hosts, joining the breakout rooms, accessing materials** (10 min) | 
| 10:30 | **Topic 3: Hands on 3.1** (20 min) |
| 10:50 | **Going through the hands-on(s) together** (10 min)|
| 11:00 | _Break_ (10 min) |
| 11:10 | **Topic 4: Module System & preinstalled software** (15 min)|
| 11:25 | **Topic 4: Hands on 4.1** (20 min)|
| 11:45 | **Going through the hands-on(s) together** (10 min)|
| 11:55 | Recap + preparations for the next day (5 min) |
| 12:00 | Finish |
| 14:00 | Bonus: Join the weekly user meeting https://cscfi.zoom.us/j/65059161807  |



### Day 2: Thursday 8.2.
    
    
| Time  | Content |
|-------|---------|
| 8:45  | Channel open, "morning coffee" |
| 9:00  | Re-cap, feedback/expectations + some Qs from HedgeDoc (5 min) |
| 9:05  | **Topic 5: Batch queue system and interactive use** (10 min)|
| 9:15  | **Topic 5: Hands on 5.1** (30 min) | 
| 9:45 | **Going through the hands-on(s) together** (10 min)|
| 9:55 | _Break_ (10 min)|
| 10:05 | **Topic 6:  Understanding resource usage**  (15 min)|
| 10:20 | **Topic 6:** Hands on 6.1 (25 min) |
| 10:45 | **Going through the hands-on(s) together** (10 min)|
| 10:55 | _Break_ (10 min) |
| 11:10 | **Topic 7: Allas and where to keep your data** (20min)|
| 11:25 | **Topic 7: Hands on 7.1** (20min) |
| 10:45 | **Going through the hands-on(s) together** (10 min)|
| 11:55 | Recap (5 min)|
| 12:00 | Finish |





---



## ☃️ ICE BREAKER (HackMD -practice)

### Ice breakers
Let's learn how to use this HackMD document by answering an ice breaker question! 


    
**Q1: What topic of this course are you most excited about?**

**Answers:**

* batch jobs
* Learning how to use the cluster more efficiently and less messy
* get a general understanding of CSC services and their use
* learning batch jobs
* Learning compute power of CSC servers.
* Having an overview of how Puhti and Mahti works. 
* batch jobs & resource allocation (estimating resource usage)Using now the basics ral in
* Using Array batch job
* How to manage python version in puhti/mahti?
* Learning about batch jobs and how to estimate the needed resources
* batch job and GPU usage
* Just to know the basics so I can start using CSC efficiently
* How to run batch jobs and undestand more the code behind computing
* Learning to do my computations more efficiently and faster
* Learn more about the computing environment
* Running batch jobs
* Batch Jobs
* Using tools that exist in different modules at the same time (for batch jobs)
* Where can one find all the self-learning courses that are available?
    * https://e-learn.csc.fi/
* Information from using seff



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

- [x] **Q8: How to add a remote repository for git? I would like to use git for the scripts I write on the CSC servers and push/pull them from a remote repo**
    - A: If you want to add your own content to the materials of the course, you could fork the course repository https://github.com/csc-training/csc-env-eff  and clone your own fork to your working environment (eg supercomputer Puhti)
    - General: You can use git the same way you would use it in your own computing environment (from the command line). So for adding a remote repository, you can either create a repository on your favorite platform, eg GitHub and then clone it via ssh to Puhti, or other computing environment. OR you can initialize the repository on Puhti and then push it to a new remote repository. 
    - For setting up ssh keys you can use the command `ssh-keygen` on Puhti login node shell and store them to your users home directory. 

- [x] **Q9: Do you have an example script for how to use snakemake on Puhti? I would like to use snakemake but haven't worked on a server before that uses batch jobs (after reading snakemake docs, I'm still pretty clueless on how to use the 'Job properties'; so an example script would be nice)**
    - A: We are currently working on an example for a snakemake tutorial (soon also in CSC docs): https://github.com/CSCfi/csc-user-guide/blob/d720852e6e12f57d843095585781f775fbde1280/docs/support/tutorials/snakemake-puhti.md
    - **Follow up question:** It is really nice to see that you guys are working on this! I looked at the snakemake tutorial - and I understand it is a job in process - but I have several questions to the setup. Would it be possible with a course or seminar on this- using snakemake in CSC? 
    --- I would also be really interested in such a course!!
        - A: **Very good that you ask!** We don't have anything for snakemake at the moment. We only have a Nextflow (another workflow tool) hackathon coming up in April: https://ssl.eventilla.com/event/9kgb0 and possibly something on workflows for geoinformatics in late spring, keep checking our [training calendar](https://www.csc.fi/training#training-calendar). General idea of running both nextflow and snakemake in CSC supercomputing environemtn is about the same. So you can register for hackathon (and the event is free-of-charge)

- [x] **Q10: Where can I find the slides from the video "Study Tips for Using CSC HPC environment effectively"? (https://video.csc.fi/media/t/0_d7trmsru/455250) - Ah ok but there are several hyperlinks in there that we cannot access now!**
    - A: They are here! https://a3s.fi/CSC_training/00_study_tips.html

- [x] **Q11: Is there a nice way to automatically record the software versions you used when loading a module in your pipeline? (similar to a conda environment lock file)**
    - A: Not really in that sense. But all our modules come with specific versions. It is a good idea to load each module along with specific version in your batch script. If you don't mention a version, it is the latest stable version. 
    - A: If you include all "module load" commands in uour batch job script the load messages get saved in the SLURM out file. You could also include "module list" command. AS mentioned above it is always good idea to load modules with version number as the default version will change over time.

- [x] **Q12: Is it essential to have Haka or Virtu credentials for the course? I've got only CSC credentials.**
    - A: No, the CSC account is the important one for this course 


- [x] **Q13: How to know which open source/online software I am allowed to download/install/compile/run on CSC super computers (Puhti mainly)? I need several software packages which are from the Github account of a known collaborator. Is is possible to ask permission for specific packages from someone at CSC personally (email)?** 
    - A: When CSC installs a software tool in supercomputing environment we look for licence file which gives information on whether we can install for free on CSC systems. If they are opensource/free you are free to install as needed. For some reason if you are not clear, you can check with CSC by sending an e-mail to our service desk. You can browse licenses in our software stack in CSC documentation (https://docs.csc.fi/apps/by_discipline/) 

- [x] **Q14: Does developing codes in the server consume billing units?**
    - A: Whenever you use the computing resources, billing units are consumed. However, if you do not have high resource needs, the amount of billing units used is very minimal. 

- [x] **Q15: Is the Visual Studio Code in the Puhti/Mahti web interface compatible with GitHub Copilot? How about Pouta?**
    - A: It is not available by default, but there are open source copilot-like plugins you can try. Pouta is a cloud service where you can manage your own virtual machine, i.e. you have to set up everything yourself. So in principle it is compatible yes.
    - A: If you want to try something like this, might be good to send an email to servicedesk@csc.fi as it might require some tricks.
    - A: The official one should be possible to use, just has to be manually installed using the "Install from vsix" option in the extensions tab (in the three dots menu there) after downloading the extension from the Visual Studio Marketplace.
 
- [x] **Q16: Can I use a singularity container in Puhti?**
    - A: Yes. Singularity is now called Apptainer. Check this documentation: https://docs.csc.fi/computing/containers/overview/

- [x] **Q17: Do I need a license to use the pre-installed applications on Puhti, for example matlab?**
    - A: Depends on the software. Check the Docs page for each application, e.g. https://docs.csc.fi/apps/matlab/ 
    - A: You can list all the software by license: https://docs.csc.fi/apps/by_license/

- [x] **Q18: How do we know what resourses an application needs? Or what resources will be needed to run a certain analysis?**
    - A: Bit difficult to suggest on a general level. Good starting point is to check application documentation where you may find whether the application is memory intensive, parallelisable or has specific resource needs.  Once you get some idea about the software you can start with small data and perform some pilot experiments with minimal resources. You can then scale up the resources and data as needed. Only experience will help us here. Obviously, you can always ask the developer of the tool to know more information instantly. 
   - A: We will discuss this a bit tomorrow. You can also check this FAQ entry: https://docs.csc.fi/support/faq/how-much-memory-my-job-needs/
   - FOLLOW UP QUESTION: And how about a specific analysis? Let's say if we need to calculate some genetic diversity estimates, how to know how much resources does it take per Kb/Gb of a sequence/SNP data?
        - A: Let's see if Thursdays session answers this question, if not please post it again in the bottom of this document
   
- [x] **Q19: I think we will get presentation slides latter ?** 
    - A: All presentations and tutorials are available: https://csc-training.github.io/csc-env-eff/

- [x] **Q20: Can you please explain again about GPU NVIDIA processor in Puhti or Lumi?**
    - A: Puhti and Mahti have GPU NVIDIA processors while LUMI has AMD GPU processors.

- [x] **Q21: I'm sorry if I missed it, but what is the main difference between projappl and scratch directories except for the automatic cleaning in scratch? Where is it better to store files that we want to share with other project members?**
    - A: Both projappl and scratch are shared with all project members, we suggest to keep all working files in **scratch** and use projappl only for files related to installations, configuration files etc. I.e. files that are necessary for a longer period of time. Inactive research data should be stored in Allas (will be covered later in this course).

- [x] **Q22: How can you check your disk workload? Like how do you know if you need to use/switch to these fast local disks?**
    - A: Good question. It might not be easy, but if you know that your application will be reading/writing thousands of files or in general just doing a lot of I/O then that's at least much more efficient on fast local disk. So you need to know the details of your workflow.
    - A: It's difficult to see directly, but you could check resource usage with "seff" command. Low CPU efficiency can be an indication that time is spent waiting for the disk, not computing. If you have low CPU efficency try same analysis with local disk and compare performance. We will talk about this tomorrow.

- [x] **Q23: Can only the project manager/owner apply for more disk resources into an existing workspace?**
    - A: Yes, only the project manager can apply for a disk quota change.
    

- [x] **Q24: From zoom chat: One question about the cleaning of storage in putti every six months, will all the files in /scratch and /projappl be erased? Since the /projappl is a sharing directory.  Thanks!**
    - A: Files that have not been used in six months will only be deleted from /scratch. Files in your $HOME directory or /projappl will not be removed. Each time the cleaning happens, we will notify by email in advance and give instructions how you can check which files will be removed so that you can move them to e.g. Allas.

- [ ] **Q25: About ssh key tutorial: I follow the steps and end up getting the following error message **(I have replaced my actual ID with "userID")**: /usr/bin/ssh-copy-id: ERROR: /users/userID/.ssh/config: line 2: Bad configuration option: usekeychain ERROR: /users/userID/.ssh/config: terminating, 1 bad configuration options**
    - A: You need to use your real CSC username, it will not otherwise work.
        - From zoom chat: Hi, I left question 25, but the person replying didn’t seem to catch that I have just changed my user id to “userID” in the question for privacy purposes. I get the error with my real ID
        - A: Aha ok! Did you do these steps on your local machine or on Puhti? The tutorial assumes you're using MobaXterm on your own machine and you might get problems if using PuTTy as the steps are a bit different, see https://docs.csc.fi/computing/connecting/#ssh-keys-with-putty
        - I'm using the terminal on my local machine (MacOS)
        - Ok, then we might need to take a closer look. Maybe you could ask this in the next breakoutroom session?
    
    - Did you have some kind of configuration file (/users/userID/.ssh/config) with the the following content:?
```
   Host Puhti
      Hostname = puhti.csc.fi
      User = your CSC username
      PreferredAuthentications publickey
      IdentityFile ~/.ssh/puhti_ssh_key.key
  ```
  
and then run the following command on Mac terminal:

 `ssh Puhti`


 - I did not, but I used the default name and location. I also tried adding this content to the config file and I still get the error. This is my current config file (again, my real ID is changed to userID) I also tried with ~/id_ed25519:
```
Host Puhti
	Hostname = puhti.csc.fi
        User = userID
        PreferredAuthentications publickey
        IdentityFile /users/userID/.ssh/id_ed25519.pub
Host *
      	UseKeychain no
        AddKeysToAgent yes
```
If your userID is CSC username and id_ed25519.pub is your private key, then it would work.

can you try the following command directly instead ?:
```
ssh -i /users/userID/.ssh/id_ed25519.pub  cscusername@puhti.csc.fi

```
UserID = CSC username, following the tutorial, I assume the key is id_ed25519. With the command above I still get this error.
```
/users/userID/.ssh/config: line 7: Bad configuration option: usekeychain
/users/userID/.ssh/config: terminating, 1 bad configuration options
```
Ok. Thanks for the clarification. can you add the following line in the config file and check if it works?:
```
UseKeychain yes

```
Still the same error with "UseKeychain yes"

What if you comment out or delete the "UseKeychain" line? 
You can try. It is bit tricky that I don't have any "UseKeychain" related configurations but still works.  I am not able to reproduce the problem.

is the line 7 in the config file is "UseKeychain no" ?

- [x] **Q26: Is the SSH required? I could not get that to work, but I understood that Puhti and Mahti can be used from the web interface and then the SSH is not required? I use windows computer and tried to create SSH with Putty**
    - A: Yes, if you use the web interface, then you do not need to set up SSH keys since you will be authenticating by logging in using CSC account (or Haka/Virtu). The tutorial is for setting up and using the SSH keys for terminal access from your local computer so the steps outlined there should be done on your local machine. The tutorial also assumes use of MobaXterm on Windows. For PuTTy, see https://docs.csc.fi/computing/connecting/#ssh-keys-with-putty

- [x] **Q27: Related to Q24. Can you clarify is 180d per file or any activity in folder? i.e. If only one file is accessed in the folder, does it "protect" other files from deletion?**
    - A: The cleaning is done by file, so such protection will not work ;-). For details, see https://docs.csc.fi/support/tutorials/clean-up-data/#automatic-removal-of-files

- [x] **Q28: Do you have theme based forums where one can raise or look up previous questions? It feels a bit silly to ask what I would believe are common questions - eg how to run python or R based scripts of the CSC cluster - in its own email to you guys. Thus, is there "we who use R/python/jupyter on the CSC"-forum where one has gathered theme-specific questions?  It is not always one can attend the Wednesday sessions and the website is huge, it is not easy to find specific tutorials. Forums might be helpful.**
    - A: Good point! We do have some Frequently asked questions (FAQ) in our documentation, but not our own forum as such. We collect all course questions too, as well as the weekly support questions, but they are not ordered by theme, and therefore not easy to find. We use both courses and support sessions for updating FAQ once in a while though: https://docs.csc.fi/support/faq/
    - However, there is no stupid question, and we are also happy to answer questions that probably have been asked a hundred times. If we have a good docs page about the topic, you will get the link to that too :)

- [x] **Q29: How to access to jupyter from web interface? I tried, but not quite sure how does it work. can you show us? Thanks!**
    - A: Sure. we can show you as a small demo sometime during this course (or in break out rooms). Please remind us if this has not happened in Thu session.
    
- [x] **Q30: When we use the export SCRATCH= and export PROJAPPL= commands, where do these paths get exported to?**
    - A: They get stored into these variables. I.e. `export SCRATCH=/scratch/project_2001234` would mean that you can use `$SCRATCH` whenever you want to refer to the path `/scratch/project_2001234`. E.g. `cd $SCRATCH` would make you move into this scratch directory. Note the `$` sign, which is used in Linux shell to denote a variable.
    - FOLLOW UP QUESTION: Does it only work with SCRATCH and PROJAPPL or can we use it for exporting any path? And if yes, can we give it any name, e.g export STRUCTURE=/scratch/project_2001243/structure
        - Yes this would also work. Just be careful to not overwrite any important variables, e.g. PATH or PYTHONPATH, you can check if a variable already exist with `echo $VARIABLENAME` which either prints the variable name or nothing if it does not exist

- [x] **Q31: When the tutorial has $USER, do we need to type it as it is, or should we type our actual username? When I tried creating a new directory (in the first tutorial today) using $USER it created an empty file with my user name instead of a new folder.**
    - A: `$USER` is actually an environment variable which stores your CSC username as its value on Puhti. So it is a convenient shorthand to use if you don't want to type your username. It is different for each user (as each user has their own username). So to answer the question, type it as is. content inside  brackets (e.g. `<project>`) should be replaced somehow (e.g. by your actual project id).

- [x] **In this tutorial (https://csc-training.github.io/csc-env-eff/hands-on/disk-areas/disk-areas-tutorial-lue.html), right after step 6, if I type "lue --display-level=<n> $HOME", I get an error "-bash: n: No such file of directory". Then if I replace n with the name of any of the folders, it just says "-bash: /user/..: Is a directory" but it does not give info as general lue $HOME command did. Could you please explain how this --display-level=<n> works?**
    - A: The display level parameter (–display-level) of *lue* tool refers to the depth of folders hierarchy that the tool should report.  You can try with –display-level=1 and then –display-level=2. You can then see the difference. You can start to see the information of disk usage on subfolders as increase the depth. 

- [x] **The command echo $LOCAL_SCRATCH does not give an output, instead there is a blank line. Why is that? (end of step 3 of this tutorial: https://csc-training.github.io/csc-env-eff/hands-on/disk-areas/disk-areas-tutorial-fastdisks.html)**
    - A: I believe that you were trying to type the **echo** command on login nodes where we have only $TMPDIR, not the $LOCAL_SCRATCH. The $LOCAL_SCRATCH should be visible in interactive nodes as well as on some of compute nodes on Puhti. Mahti CPU nodes don't have local  disks (and hence no variable, $LOCAL_SCRATCH, exists).

- [ ] **Q34: Will there be another course after this one? Maybe more project oriented?**
    - A: Yes. there will be bit more advanced and extended version of this course.
    - Follow our training calendar for updates: https://www.csc.fi/training#training-calendar

- [ ] **Q35: I see in MyCSC that the project file allocation is almost full, at 99%. What should I do?**
    - A: You should figure out where you have a lot of data. For this, the tutorial from yesterday is useful, https://csc-training.github.io/csc-env-eff/hands-on/disk-areas/disk-areas-tutorial-lue.html. Then, when you know this, delete the unnecessary files and move those that you still need somewhere else, e.g. Allas.
    - There are 6 or 7 people in this project, maybe I should ask the project admin?
    - Indeed, it's good to communicate within your group and ask your colleagues to also check their files. It is of course also possible to apply for more quota, but the best option is always to first consider if all those files are really needed. https://docs.csc.fi/accounts/how-to-increase-disk-quotas/

- [ ] **Q36: Why the login node shell is used for these tutorials? Shouldn't the computing node be used for these?**
    - A: here we use batch job submissions on login nodes just to submit the jobs to cluster where actual computation happens in compute nodes.
    - A: Todays tutorials are tasks that you would normally do in the login shell (preparing and submitting batch jobs). Some other tutorials may be tasks that you would normally do in an interactive shell. This, hower, is sometimes problematic in a course situation, as the interactive resources are limited. Therefore we have designed the tutorials light enough to be run on the login nodes.

- [ ] **Q37: Sending jobs to the cluster via snakemake - is not really advised without calling snakemake by a batch script, even if you allocate appropriate amount of cores etc. Can you try to explain why this is?**
    - A: Snakemake can generate a large number of very short batch jobs and this puts load on the batch job system. In worst case scenario every step (e.g. checking if a file exist) is run as a separate batch job. So you should reserve some resources and let Snakemake do its thing within that reservation, but don't let Snakemake talk to the batch job system directly.
 - **follow up question: Thanks for that clarification. I don't feel that message comes across - not letting things interact with the cluster without batch script- given that one can load the snakemake module, and other modules, that are otherwise built to be able to send jobs to a cluster etc. But in snakemake you can specific cores etc, and my question therefore; shall resource allocation not be done at all and *only* be specified in the batch script (or shall it *also* be specified in the snakemake commands for resources)? Is it wrong to specify it within snakemake (even when I call snakemake from a batch script)?**
   - A: The problem is the Snakemake Slurm executor. Generally speaking don't use the `--slurm` option. 
   - A: Just to elaborate a bit, you may use a slurm option if you are sure that each rule takes considerable wall-clock time and you have fewer such rules. And then expect to stay in queue for the execution of each rule as snakemake submits each of those rules  to cluster as a separate job (=slurm way of working).  On the HPC cluster, if you have thousands of small jobs,  each job creates some overhead on slurm database and the otehr performance issues. Submitting tiny job on a cluster cluster can be overkill. On the otherhand, even when you execute everything in one batch job,there will be local executor submitting the jobs to locally (=in the same job allocation) without needing to queue for each rule on that compute nodes. As and when you have very hight-thoughput case (like working with hundereds of samples), you can use Hyperqueue executor with multiple nodes to perform your jobs. So bottomline is that you are still using cluster capabilities but in a efficient manner.


- [ ] **Q38: What do you do with batch jobs when you don't know how long your job might take? For example with #SBATCH --time=00:02:00 ?**
    - A: You can test beforehand in an interactive job for example. Run a minimal example and try to extrapolate based on the runtime. 
    - A: Overestimating time is not as bad as overestimating other resources. The job will end when the last process of the job ends and all reservations are freed.

- [ ] **Q39: Why is the number of cores per node called "--ntasks" instead of "--cores", like "--nodes"? Or is "--ntasks" something different that simply the number of cores per node?**
    - A: A single task may use multiple cores. The number of cores one task uses is specified using `--cpus-per-task` option. So it's a bit different. You could for example use --ntasks=40 and --cpus-per-task=1 to use all cores in one Puhti node. Or you could also do --ntasks=2 and --cpus-per-task=20, or --ntasks=1 and --cpus-per-task=40. In all cases here you're using all cores, but the details of the parallelization will be different (tasks are related to MPI ranks while cpus-per-task are actually the number threads that each MPI rank launch, but this is already a bit more advanced topic).
        - **Follow up question**: If I have a parallel job that is not parallelized with OpenMP or MPI (say, Matlab's parfor/parpool), does it matter how I request the number of CPUs I want? 
        - A: I do not know the specifics of how Matlab is parallelized, but I would assume it uses either or both of MPI and OpenMP under the hood. These are the main parallel programming standards as far as I'm aware. Please see our matlab documentation: https://docs.csc.fi/apps/matlab/

- [ ] **Q40: When is Putty recommended to use? Is it the same as MobaXterm?**
    - A: It is a matter of preference mostly. MobaXterm has much more features and can thus be more useful. PuTTY is a quite simple client that more or less just allows you to do SSH (i.e. no file transfer functionality e.g.).

- [ ] **Q41: Is it better to overestimate time rather than the number of cores? The resources will be free anyways after the job is finished, altough time allocation is not?**
    - A: Neither is optimal, but in this case it would be better to overestimate time, because you are only billed for the time you actually use and after your job ends the resources are freed for others to use. Cores that are reserved but not used are away from others and wasted if you do not utilize them efficiently. The main downside of requesting too much time is that you might queue for the resources for longer.

- [ ] **Q42: What threshold is considered too inefficient for CPU useage (in terms of percentage) ?**
    - A: The rule of thumb is that your job should get *at least* 1.5 times faster when you double the amount of resources. So as a percentage, the parallel (CPU) efficiency should be at least 75%

- [ ] **Q43: Does seff display some mean memory usage for a job? Sometimes seff shows that a job has not used all of the reserved memory (e.g. seff shows memory usage of approximately 40%) but still the job fails while running with an out of memory error and increasing the allocated memory for the job seems to fix this, even though seff showed that not all of the allocated memory were used in the first place. Could this be due to memory demand spiking highly in the course of running the job, even though most of the time not using all of the allocated memory?**
    - A: Seff is not 100% accurate and can miss shortlived memory spikes, unfortunately. Seff tries to give you the maximum memory usage (i.e. the memory that your job actually needs/used), but it can fail. Mean memory estimate would not be that useful because the needs are defined by the maximum.

- [ ] **Q44: Is there a way to restore my home directory to its state at the time my account was created (somehow like a fresh install)?** 
    - A: Not really, but this tool might accomplish sort of what you might be looking for: https://docs.csc.fi/support/tutorials/using_csc_env/
    - A: It will not delete files for you or anything like that, but it can be used to reset your .bashrc file for example

- [ ] **Q45: Is there any documentation for running MATLAB (array or parpool) jobs from the Terminal as batch-jobs? I think the documentation I found only considers using MATLAB Parallel Server from local GUI/workstation. I managed to modify the array.sh-script to run a simple MATLAB code (= prints input) as an array job, if the input is given as numbers, but I haven't managed to give ${SLURM_ARRAY_TASK_ID} as input. I simply added "module load matlab" and "srun matlab -nojvm -nosplash -batch 'TEST();'", but I don't know if these are the wanted MATLAB settings and how to input the array task ID. The error I get is "Invalid text character. Check for unsupported symbol, invisible character, or pasting of non-ASCII characters."**
    - A: I am not a matlab expert, but did you check our documentation here: https://docs.csc.fi/apps/matlab/ ?
    - **Follow up question**: Yes, I read those pages and I think they only advice how to use MATLAB Parallel Server from local GUI/workstation (sorry if i missed something). But if I have 200 array jobs that run for 50 hours, I would rather have them running somewhere in the background (Terminal). 
    - I asked our Matlab specialist Sampo to get back to this! If he has not time to do that right now, I'd suggest you send a ticket about it to servicedesk@csc.fi. Sorry that we have no Matlab expert now on call on this course!
    - **Follow up question**: No problem at all, great to know that help is available! 
    - A (from Sampo): We have only five licenses available for MATLAB outside the parallel server, thus you can't run your array jobs effectively with them. Array jobs are also possible to launch via MATLAB Parallel tool. We can provide you an example, please send your question to servicedesk@csc.fi. 
    - **Follow up question**: Thank you very much, this answer was very helpful! So I if use MPS instead of Terminal, I could run, for example, 1000+ array jobs (15 mins, 50 GiB) effectively? I already made some tests with MPS, thus I will continue those and contact servicedesk with a better formulated question. Many thanks! 
        - Asking servicedesk sounds good! Please note that there is limits on how many jobs a user can submit per day and at the same time. 
- [ ] **Q46: How do you know with which protocol a data object was uploaded to Allas?**
    - A: There is no 100% sure way to check this. However, if you have over 5 GB files you can check if they are stored as several object called as segments. If that is the case, then Swift protocol has been used. If you se just one big object, then S3 protocol has been used.

- [ ] **Q47: Is there a way of soft linking my data from allas to my working directory at /scratch/project_200…/user/ working directory?  (e.g., link -s /allas/data /scratch/project_200…/user/)**
    - A: No.
    - Sidenote: Some geospatial tools that are based on `GDAL` however, let you read data directly from Allas: https://docs.csc.fi/support/tutorials/gis/gdal_cloud/ ; but it is not too many tools that support this. 

- [ ] **Q48: How do we get the certificate of the course? In the eLena platform it says that the certificate is "Not available unless: The activity Course feedback, live course is marked complete", but that is also unavailable.**
    - A: We will check that and send you instructions via email. Thank you for letting us know!
    - EDIT: There was an error in the course settings, now the "Course feedback, live course" should be available you, if you selected the Feb2024 group in the top of the page! Thank you very much for pointing this out!

- [ ] **Q49: I try using the commands cd/scratch_projectname and /cd_projappl_projectname. Why nothing happens but the text "No such file or directory"?**
    - A: After logging into CSC platform with your account, you can migrate to the `/scratch` partition of your project as follows:
`cd /scratch/project_projectnumber`
For ex. If you have a project `project_1000110`, it should be: 
`cd /scratch/project_1000110`
Similarly, for migrating to the `/projappl` partition of your project, it would be: 
`cd /projappl/project_1000110`

- [ ] **Q50: Type your question there!**
    - A: Answer will appear here

- [ ] **Q51: Type your question there!**
    - A: Answer will appear here

- [ ] **Q52: Type your question there!**
    - A: Answer will appear here

---
**:arrow_up: Write your questions above this line :arrow_up:**

---

## Feeback day 1

One thing you liked:

- ..combination of lectures and good and simple tutorials 
- ..good tutorials, thank you!
- ..tutorials were short enough, so for me, who is just at the very beginning of using CSC, it was ot overwhealming
- ..having regular breaks was good!
- ..


One thing that could be improved:

- ..maybe some things go very into details > e.g. maybe for some of more general stuff on modules /programs might be more useful. Today quite some time was reserved for loading one module. Maybe a step back might be useful? For example a person X wishes to run R scritps/Python scripts on CSC instead of laptop. What steps are needed? 
    - Thank you for this feedback! We will talk about this a bit on Thursday, please let us know if that helped and if there is still some other parts that could have been skipped.
- ..there were maaaany words/names/abbreviations of 'services' that CSC and IT are using (e.g., Rahi, Kaivos, OKD, PaaS, OpenStack, etc.), and when we (or I) do not know what those mean, we (I) cannot fully understand what you are even talking about.. Maybe such things can be gathered into one cheat-sheet, with a name and shortly what it is used for? 
    - thank you for this feedback! There are indeed a lot of names. We have a short service overview here: https://siili.rahtiapp.fi/weekly_CSC_service_overview# , but it is missing the general IT words. For the beginner version of this course, we could maybe try to leave them out?
- ..
- ..

## Feedback - Day 2

One thing you liked:

- I found useful to test a batch job that failed because of wrong resource request, and learning how to fix it.
- I really liked the regular 10 minute breaks. That is something I forget to do in my usual workdays.
- The recap sessions were fantastic. It filled in gaps where I hadn't managed to do something in the 20minute breakout session and didn't have time to discuss it there.
- I liked the break out rooms, and the possibility they gave for discussions and questions. Also, this HackMD platform was nice
- ..
- ..

One thing that could be improved:

- An optional info on what the scripts we are calling during the exercises do would be nice. Otherwise it feels slightly detached to understand the outcome
- Perhaps a quick tutorial on using nano for writing the scripts.
- The prerequisite course could better clarify some points such as the multiple ways to login (CSC account vs Haka vs Virtu etc.) The prereq course information felt a bit disjointed.
- I was worried for not having a e-lena account, but in the end it wasn't needed. Perhaps this can be clarified.
- A bit more time in the break out rooms: now all the time was used for the exercises, but it would have been nice to also have some time for discussions
- ..

Were recap sessions after the breakoutrooms helpful? Please add an `o` for your vote:

- yes: o o o o o o o
- no: o o o
- don't know: o
- other:
    - I think the exercises were very straight forward and easy to complete according to the instructions, so the recaps were a bit unnecessary. Maybe one short if-needed-recap at the end of the day could be better?
    - ...
    - ..

## Useful links 
- [Elements of Supercomputing](https://edukamu.fi/elements-of-supercomputing) online course
- [Training links](https://docs.csc.fi/support/training-material/#training-materials-and-sources-from-csc-and-partners) by us and our friends
- [Weekly research user meetings](https://ssl.eventilla.com/usersupportcoffee) (come and ask anything!)
- [Data management self-learning course](https://e-learn.csc.fi/course/view.php?id=63)
- [Sensitive Data (SD) services webpage](https://research.csc.fi/sensitive-data)
- [Sensitive Data (SD) services user guide](https://docs.csc.fi/data/sensitive-data/)