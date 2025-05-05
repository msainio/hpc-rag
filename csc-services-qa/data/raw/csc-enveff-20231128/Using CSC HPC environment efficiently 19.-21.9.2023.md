---
title: Using CSC HPC environment efficiently 19.-21.9.2023
tags: [puhti, mahti, allas]

---

# Using CSC HPC environment efficiently 28.-30.11.2023 

###### tags: `puhti` `mahti` `allas`

> This is the collaborative "notebook" for the "Using CSC HPC environment efficiently" course organised in November 2023 by CSC -IT center for Science. 
> [Prerequisite course page in eLena platform](https://e-learn.csc.fi/course/view.php?id=75)
> [Course page in eLena platform](https://e-learn.csc.fi/course/view.php?id=76)
> [Collection of slides and material](https://csc-training.github.io/csc-env-eff/)
> [Zoom-link for sessions](https://cscfi.zoom.us/j/67271522589?pwd=R2dDVnVyYXJGSXQ5cFcyME54REJ1Zz09)
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

### Prerequisite / support session 22.11.
14:00-15:00 Join the pre-course support session, which is also part of [CSC's weekly user meetings](https://cscfi.zoom.us/j/65059161807)

### Day 1: Tuesday 28.11.


 
 
| Time  | Content |
|-------|---------|
| 8:45  | Login, check connections work, test microphone |
| 9:00  | Welcome, course practical info, learning targets,  ice-breaker, feedback/expectations (10 min) |
| 9:15  | **Topic 1: Prerequisites & Connecting** (15 min) |
| 9:30  | **Topic 2: Introduction to HPC Environment** (20 min) |
| 9:50  | _Break_ (10 min)|
| 10:00 | **Topic 3: Disk Systems** (15 min) |
| 10:15 | **Intro to breakout rooms & hosts, joining the breakout rooms, accessing materials**  | 
| 10:20 | **Topic 3: Hands on 3.1** (<20 min) |
| 10:35 | **Topic 4: Module System & preinstalled software** (15 min)|
| 10:50 | **Topic 4: Hands on 4.1** (10 min)|
| 11:00 | _Break_ (10 min) |
| 11:10 | **Topic 5: Batch queue system and interactive use**  (20 min)|
| 11:20 | **Topic 5: Hands on 5.1** (30 min) |
| 11:45 | **Going through hands ons 5.1. together (Test)** (10 min) |
| 11:55 | Recap + preparations for the next day (5 min) |
| 12:00 | Finish |




### Day 2: Wednesday 29.11.
    
    
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



 
### Day 3: Thursday 30.11.


    
    
 | Time  | Content                                                                            |
 | ----- |:---------------------------------------------------------------------------------- |
 | 8:45  | Channel open, "morning coffee"                                                     |
 | 9:00  | Re-cap, feedback/expectations + some Qs from HedgeDoc (5 min)                      |
 | 9:05  | **Topic 9: Containers & Apptainer** (20 min)                                       |
 | 9:25  | **Topic 9: Hands on 9.2** (30 min)                                                 |
 | 9:55 | _Break_ (10 min)                                                                   |
 | 10:05 | **Topic 10: How to speed up jobs** (30min)                                         |
 | 10:35 | **Topic 10: Hands on** (35min)                                                     |
 | 11:10 | _Break_ (10 min)                                                                   |
 | 11:20 | Topic themed breakout rooms + ask anything on all previous topics (25 min)         |
 | 11:45 | Recap + feedback + open questions + cleaning up files from course project (15 min) |
 | 12:00 | Finish                                                                             |
    



---



## ☃️ ICE BREAKER (HackMD -practice)

### Ice breakers
Let's learn how to use this HedgeDoc document by answering an ice breaker question! 


    
**Q1: What from this workshop are you going to use in the near future?**

**Answers:**

* Probably Puhti or Mahti
* I will be using Puhti for my work on a daily basis, so I'm sure there will be a lot of things from the workshop that I will be testing in practice.
* I'd like to learn multinode for a LLM project
* you got it :)
* I'd like to use Puhti for my projects 
* I'm going to use Puhti for bioinfomatics projects, actually started a bit already
* Containers
* For future projects that will utilize these services.
* Puhti :)
* I need to run my own applications with Puhti, so I probably need to learn containers
* I would like to run simulation with Puhti
* I qould like to use it for neuroimage processing that takes long time on personal computer
* I want to use Puhti more efficiently
* I have used Puhti and Allas to store my data but I'd like to learn to use Puhti to run some of my actual analysis too.
* I will use Rahti for our project.
* I would like to use Puhti
* I would like to use Rahti to run some of my applications that our research group needs
* I want to run batch jobs in Puhti more effectively as I think I've now been wasting too much resources
* Looking to make my parallel jobs more efficient
* I want to learn more about containers.
* to be a more efficient user
* I would like to use Puhti for whole genome resequencing.
* I would use it in the data analysis of my research. I am hoping most of the things from this training are going to clear many confusions for me and pave the way for easier use of CSC services.
* investigating whether CSC puhti would be good environment to analyse our project data (and e.g. Allas to store it)
* Want to use batch jobs more efficiently
* Use Puhti for microbiome analyses and Allas for data storage
* I have been using VTT's HPC cluster, but I'm curious about using CSC as well
* I will use Puhti and hopefully learn some new tricks to use it more efficiently
* I would like to possibly use Puhti or LUMI
* Use Phuti/Mahti more efficiently
* I would like to learn how to use the CSC for training deep learning models.
* I will be using Puhti for my project so would like to learn more about it.
* Mostly Puhti and Allas for bioinformatic and genomic analyses 
* puhti/mahti for deep learning projects 
* To use puhti environment 

### Q2: Feedback & comments on the going through the exercises together after the hands-on session?
* Thank you
* --


### Q3: What topics would you like to still discuss (in topic themed break out rooms)? 

* Hands on with the MobaXterm:)

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

- [x] **Q7: Hi, I am in Chicago for a last minute conference. Thought I could stay on but can’t as it is 2 am and I have a presentation tomorrow. Hope there is a recording of this**  
    - A: There’s no separate recording, but the lecture videos, slides and hands-ons are available in the [github page](https://csc-training.github.io/csc-env-eff/), and all the material + the quizzes etc can be accessed in [eLena platform](https://e-learn.csc.fi/course/view.php?id=76), so this course works well as self-study also!  

- [x] **Q8:After I run a  job on Puhti and the job closes, my home directory is filled with temp files created during the job (not a part of the input/output). Can I delete these?**
    - A: If you do not need them (they do not contain important info), then yes it's a good idea to delete them. The Home quota is also quite small, so if there's a lot of temp files being written might make sense to tell the program to write them to the local disk (`$LOCAL_SCRATCH`) instead. Writing a lot (thousands) of small files to the shared file system (e.g. home or scratch) might also worsen performance significantly, so using the local disk is recommended if dealing with large amounts of temporary files.


- [ ] **Q9:Hi, I can connect to mahti in vscode, but cannot connect with puhti. Terminal connection with ssh works but I think it is related to some files...?![Näyttökuva 2023-11-28 103719](https://hackmd.io/_uploads/Bk5mDmXrT.png)**  
    - A: Would it be possible that VSCode tabs and windows from previous app sessions of mahti are not closed before connecting with Puhti?

- [x] **Q10: I tried to setup SSH keys (generated with puttygen), but get the following error on login: "Server refused our key". I've added the public key both to my MyCSC profile and to ~/.ssh/authorized_keys**   
    - A: Just checking one thing: does your public key in file ~/.ssh/authorized_keys starts something like this: ```ssh-rsa  ...... ```? [Yes]
what kind of file permissions you have ? ```ls -l .ssh/authorized_keys``` [-rw-rw----, this may be the problem?]
 could you try to set to have the following permissions: ``` -rw-------.``` [Did not help.]
 [I got it working now :) It was a stupid user error on my part, had selected the wrong private key file in Putty. Thanks for the help.]
 Great that you got it workng... we all do such mistakes..
 
 - [x] **Q11: Could you explain please, there is this limitation "do not read plenty of small files", but it supposed to be ok to read multiple from @LOCAL_SCRATCH. So if the script is running from let's say projappl, but the folder with the files is in local_scratch, is it ok to read them iteratively? Am I missing smth? Thanks!**
    - A:  Yes. Main idea is that when your application (which can be installed on /ProJappl but can be called from anywhere) requires reading (or writing) thousands of small files, LOCAL_SCRATCH (=local SSD drive which are designed for faster reading and writing of files) is very efficient (= you can get improved wall-clock time). On lustre parallel file system (e.g., on /scratch/..), it would take more time for the same job and also causes a bit of overhead on file system.  


 - [x] **Q12: In the Slurm bash script example, srun was placed before each command (e.g. srun hostname; srun sleep 60). Is it needed?** 
    - A: It is used to tell the command to actually use the resources that were requested. This is important if you request e.g. multiple compute cores to use. If forgotten, the job would just run using a single core and the other requested resources would idle and thus be wasted.

- [x] **Q13: What's the difference between srun and sbatch?**
   - A: Sbatch is used to submit a batch job script. Srun is used to submit job directly. Anything in the #SBATCH lines in a batch job script can be given as command line arguments for srun. Srun can be handy for submitting simple jobs, but for more complex jobs, writing a batch job script is probably clearer. Batch job scripts also give you a record of what you did, so they can make troubleshooting easier.
 
 - [x] **Q14: With the exercise on batch jobs, trying to submit the job (sbatch my_serial.bash) results in an error with "Invalid account or account/partition combination specified". The project name should be correct at least.**
    - My colleague advised me to change the partition to "fmi", and now it worked.
 
 - [x] **Q15: Can I run something like sacct from jupyter or in interactive mode when there is no batch job submitted? How to know how much billing units I consume or if the requested resourses are optimal?**
     - A: `sacct` and `seff` can be used for any job ids irrespective of whether they have already completed or are still running. Note that the results might however be accurate only after the job has finished. Shell commands like sacct and seff can in principle be used in jupyter by adding an exclamation point before the command, e.g. `!sacct -j 1234567`. Seff will print the consumed billing units and to know if the requested resources were used optimally, check the CPU (or GPU efficiency) as well as the memory efficiency. These should ideally be close to 100%, although such a high efficiency is typically not possible. Just make sure that the efficiency is not too low. On mahti 50% CPU efficiency is also very good, since the calculation takes into account multithreading.

 - [x] **Q16: Not a question, but a tip. Didn't see any information about here in the course material, but based on previous Slurm use, I find it very useful to get email notifications about jobs starting and finishing with the following additions to the job submission script:**

    ```
    #SBATCH --mail-type=ALL # Send you an email message when your job starts and ends. Can also be e.g. BEGIN or END for just one or the other 
    #SBATCH --mail-user=X@Y.Z # If you want to specify a custom email address (otherwise I believe it is the one associated with your CSC account)
    ```

     - Good tip, thanks for sharing!
 
 - [x] **Q17: Question regarding to data storage and sharing: Human data should be encrypted if it is put to internet. Do you have some encryption tools?**
      - A: You can find the instructions for encoding your sensitive data here:  https://docs.csc.fi/data/Allas/allas_encryption/. You can also find more information on handling sensitive data services here: https://docs.csc.fi/data/sensitive-data/ and pay attention to SD connect service: https://docs.csc.fi/data/sensitive-data/sd_connect/
     
 - [x] **Q18: Sorry I most likely just missed this point, but could you re-iterate the prices/quotas for Allas storage for academic use? Thanks**
     - A: https://research.csc.fi/pricing-and-resources
     - https://research.csc.fi/billing-units
     - https://research.csc.fi/quotas
     - Default quotas for free academic use: Storage	10 TiB, Buckets per project	1 000, Objects per bucket	500 000
     - If you are using CSC's services free-of-charge and need to store more than 200 TiB in Allas, please contact servicedesk@csc.fi in order to agree with CSC about storage terms and possible costs.

 - [x] **Q19: When I pushed a new text file from puhti to allas with a-put, it automatically added extension .tar. Is this the way it should work?**
     - A: No. The tar extension should be added only if you add a directory to Allas with a-put.

 - [x] **Q20: Is there any advantage of using rclone over a-commands, or the other way around?**
     - rclone is typically faster as it does not do the checks and pre-prosessing that a-put/a-get does.
     - a-put/a-get provide you easier syntax and some automatized checks and pre/prot-prosessing steps. Also in the case of batch jobs a-commands allow you to automtaically re-generate the Allas token ( if the original Allas connection in opended with allas-conf -k).

 - [x] **Q21: How to know if I am requesting correct amount of resources for an interactive desktop session? I did not see those sessions with sacct even though I have run them before the course.**
    - A: sacct shows by default only jobs that were run on that day. To query for older jobs, use the `-S` flag (for Start), e.g. `sacct -u $USER -S2023-11-01` to see all your jobs that started after 1st Nov 2023. Remember to not query too long time intervals since the command is a quite heavy database operation.

 - [x] **Q22: What is the command to make a data already available in allas (but not in puhti) public, can it be done?**
     - `a-publish` will make the file public. If you just want to share a file temporarily, you can also use `a-flip` (the file will become unavailable after a while). 
     - note that access rights are controlled on bucket level: you can either publish all the objets in a bucket or none of them.
     - you can use https://pouta.csc.fi interface or `a-publish -b bucket-name` to make a bucket public.

- [x] **Q23: Is it possible to request software to be added to the modules maintained by CSC? Or have some software installed by CSC personnel to own projappl directory? These installations are quite difficult without Linux or coding knowledge.**
  - A: You can always ask. We will assess the situation case by case and decide wheher to add the software to our selection or not. Even if we choose not to make a public installation, we can provide you with detailed instructions on how to install it yourself. We can't install it in your /projappl for you, since we specialists do not have read or write access to your directories. (This is also good to keep in mind when writing a help request to servicedesk: You need to include or somehow share the files you want us to take a look at. We can't simply check them from your /scratch etc.)

- [ ] **Q24: I use snakemake pipelines in a lot of my work, and see it is available preinstalled. What would be the best approach for using it efficiently on Puhti? Can one use Snakemake's `--slurm --default-resources slurm_account=<project name?> slurm_partition=<partition>` parameters to launch the pipeline and have it submit the individual jobs to Slurm? Do you happen to have some example launch script available?**
    - A :(I am not a specialist in Snakemake workflows so I will answer at general level) one can use natively implemented slurm executor for your Snakemake pipeline and you can check the toy example here: https://yetulaxman.github.io/containers-workflows/hands-on/day4/snakemake.html. However, if you have lot of small job steps (or sub tasks) in your workflow, we advice submitting your job as a normal batch job with proper resoiurces  and use *local*   execution instead.  This means, all of your the sub tasks will be run inside of the same resource allocation. If you have too many small jobs (say several hundreds or even thousands), our suggestion in your case is to use HyperQueue executor (instead of slurm) where workers submit all of your sub-jobs to the same resource allocation (= everything happens in one batch job). For this, you should use the `--cluster` option and e.g. HyperQueue, see https://docs.csc.fi/apps/hyperqueue/#using-snakemake-with-hyperqueue


- [ ] **Q25: I want to train and retrain models on Puhti, and track metrics with MLflow which is running in Rahti. For this I need to be able to change env variables. Is it possible to create conda environments or what would be the go-to solution?**
    - A: If you mean that you need to set environment variables for the runs in Puhti, you can do that with the command `export VARIABLE=value` where "VARIABLE" is the name of the variable to set and "value" the value you want to set it to. This command can be given in the Slurm batch job script or in the terminal before launching the job. In fact we have a tutorial for using MLflow which shows some examples: https://docs.csc.fi/support/tutorials/ml-workflows/#mlflow-tracking-server
    - A: Conda shouldn't be needed for this, unless you need to install some packages from the conda repositories. MLflow should be included in our PyTorch module, and can also easily be installed by yourself with `pip install`.
    

- [ ] **Q26: I'd like to learn more how to use containers. Could you advise a best/most compatible with CSC infrastructure (online) course for that? I can see that there is a MOOC at UH (TKT21036 - TKT21038) on Docker, do you think it's helpful? Any other options?  Also, Kubernetes is often mentioned together with Docker; what is this? Is it used for academy-oriented DS projects? Thanks!**
    - A: Ari-Matti and Laxman have been arranging containers courses at CSC. Next one is not currently scheduled, but here's the course material for the previous one: https://yetulaxman.github.io/ContainersHPC2023/
    - This is probably the MOOC you meant?https://devopswithdocker.com
  - A: One introductory level course (bit heavy on biofield though) could be the following: https://yetulaxman.github.io/ContainersHPC2023/.  HPC systems don't entertain the deployment of docker containers as the docker engine require root access for running the container. However, concepts of docker are quite useful for understanding otehr containers as well. Singularity/Apptainer containers are HPC-friendly and do not require root access for running container. You can convert a docker image to Apptainer/singularity. 
  - A: Kubernetes is container orchestration system that can be used e.g. to automate starting/stopping containers. It's typically used in a setting where you provide services as containers.CSC uses similar but bit different framework called, OpenShift (which is a paid platform service from Red Hat UNLIKE Kubernetes (aka, k8s) is an open-source application from Google) in Rahti container cloud (https://rahti.csc.fi/)
  
- [ ] **Q27: Is it possible to use Tykky tool to put different conda installations into the same container?**

    - A: In theory, yes. But in practice, if you have two complex conda environments, each with conflicting python packages, tykky installation would more likely either fail or one of the environments may not work as intended. 
 
- [ ] **Q28: I am using vs code to connect to puhti. How could I visualize /scratch/project using EXPLORER on the left hand side.** 
    - A:

- [ ] **Q29: I am in the processing my MATLAB code for parallel computing but I will like to start running my code with a single core until its paralized. Maybe I might need a bit of assistance.**
    - A: How to proceed here might depend a bit on what exactly you are trying to compute. Perhaps you should send an email to servicedesk@csc.fi and include your script there and then we could give you some guidance? You can also have a look at our Matlab documentation https://docs.csc.fi/apps/matlab/


 
---
**:arrow_up: Write your questions above this line :arrow_up:**

---

**Themed breakout rooms:**

Ask anything on all previous topics, or anything really :)	

Room 1: Rasmus & Nino , chemistry (7)
Room 2: Laxman & Ari-Matti, bio (12)
Room 6: Mats, Machine learning (8)
Room 7: Samantha, Geoinformatics, anything about spatial data, remote sensing, earth observation etc :) (4)
Room 8: Heli, R (1)

---


**Testing area:** 
I have to leave earlier. Thank you for the course!





Here you can test how to use HackMD :)
test
test *test* **test**
(?) 
'''test'''
:)
-  [] testing


testman is `testing`
**Testing area ends**

---





## Useful links 
- [Elements of Super computing](https://edukamu.fi/elements-of-supercomputing) online course
- [Training links](https://docs.csc.fi/support/training-material/#training-materials-and-sources-from-csc-and-partners) by us and our friends
- [Weekly research user meetings](https://ssl.eventilla.com/usersupportcoffee) (come and ask anything!)
- [Data management self-learning course](https://e-learn.csc.fi/course/view.php?id=63)
- [Practical Deep Learning course](https://ssl.eventilla.com/event/8aPek)
- [Sensitive Data (SD) services webpage](https://research.csc.fi/sensitive-data)
- [Sensitive Data (SD) services user guide](https://docs.csc.fi/data/sensitive-data/)