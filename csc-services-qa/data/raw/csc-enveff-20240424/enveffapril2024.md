# Using CSC HPC environment efficiently, Part 1: Basics 24.-25.4.2024 

###### tags: `puhti` `mahti` `allas`

:::warning
Link to this document: https://hackmd.io/@CSCBioMaria/Bk00RUSdp
:::

> This is the collaborative "notebook" for the "Using CSC HPC environment efficiently" basics course organised in April 2024 by CSC -IT center for Science. 
> [Prerequisite course page in eLena platform](https://e-learn.csc.fi/course/view.php?id=75)
> [Course page in eLena platform](https://e-learn.csc.fi/course/view.php?id=76)
> [Collection of slides and material](https://csc-training.github.io/csc-env-eff/)
> [Zoom-link for COURSE sessions](https://cscfi.zoom.us/j/65186982904?pwd=S3hsNi92N3VHYmM0Znp1N1VFeXM4dz09)
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

### Prerequisite / support session 17.4.
14:00-15:00 Join the pre-course support session, which is also part of [CSC's weekly user meetings](https://cscfi.zoom.us/j/65059161807)

### Day 1: Wednesday 24.4.
 
 
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



### Day 2: Thursday 25.4.
    
    
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

* How to use parallel jobs
* I am excited about learning various tricks to get the most out of Puhti, Mahti, and Allas!
* Understanding how HPC works
* I am most excited about learning about how to use CSC more efficiently. I was thrown into it a bit, with out much background knowledge on how it works. I do use it on a bacsic level currently. 
* Learning to better use batch jobs and Allas
* Batch job options and possibilities
* I'm excited to lean about the logic behind using the csc facilities so I can use it better. 
* Learning about using Puhti for easier computation.
* Learning about launching jobs in Puhti
* Everything 
* I used CSC's Puhti aleardy quite a lot but I hope to refresh my knowledge and learn how to use the CSC's services better
* How to do batch jobs
* Learning about HPC and how to use it in my research
* How to do batch jobs
* Efficient usage of Puhti
* Using Puhti and Allas efficiently when working with very big data
* More advanced knowledge surrounding the puhti environment (e.g. installation of software using tykky)
* Getting familiar with CSC environment
* Getting more comfortable with Puhti and Allas
* Learn how to best utilize parallel computing in Puhti and Lumi for specific software.
* Get familiar with batch jobs on Puhti, Mahti, use of Allas and other tools.
* Disk
* Get familiar with Puhti and Allas
* How to install a software and run it in Lumi (for exaple Abaqus software that is only available in Puhti now)
* Is the simulation time faster in Lumi compared to Puhti or is it limited by same things as in puhti?
* Efficiently using puhti or other resources available
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


- [x] **Q8: What kind of task can be done in login nodes directly, in addition to submitting batch  jobs?**
    - A: You can use login node to get access to interactive nodes(https://docs.csc.fi/computing/running/interactive-usage/). You can also do some light-weight pre-processing of data in temporary directory in login node ( you have to move your data to $TMPDIR and then do preprocessing) before actual analysis. There are other useful things like checking disk usage and finding the information of different projects (commands: csc-workspaces; csc-projects) while being in login node.           

- [x] **Q9: What does it mean 'to run jobs in parallel'? Would they be related jobs that need information from eachother for example or something else?**
    - A: Running in parallel means that the progam you're using has been programmed such that you can split the workload into smaller pieces, each being processed at the same time using multiple processes (cores). This is the fundamental principle of supercomputing, i.e. we split a heavy calculation into smaller pieces, compute them in parallel, and then combine the results at the end.
    - A: Regarding information exchange, there are different types of parallel jobs. Sometimes the smaller pieces we split the job into are completely independent, in which case no information needs to be exchanged between them. This is sometimes called "embarrasing parallelism" or "trivial parallelism". Usually, however, the processes are not fully independent and information must be passed between the individual processes. Communication between processes is a very important topic when talking about parallel computing and is one of the reasons why you typically cannot just use arbitrarily many cores for your calculation, but the performance will level out at some point after which the performance does not improve anymore. There will simply be too much communication between the processes.

- [x] **Q10: When I sign in to puhti via ssh on my linux computer, am I accessing puhti via a login or compute node?**
    - A: Login node (aka, head node or user access node (uan))

- [x] **Q11: If I have a process that requires to read huge amount of data, is Mahti a good choice? I parallelized my code, but due to insufficient RAM it throws errors (I first used 32 cores in parallel in my code, then 8, then 4, none worked). However in Puhti with less cores (8) it works.**
    - A: Mahti is a good choice if your application leverages lot of parallelism (18 cores) but if you need lot of memory, Puhti has better options for selecting nodes with different memory. Mahti node has fixed memory of 256 GB. As per reading huge files, Lustre (parallel file system on Mahti and Puhti) is fine. Please also note that Mahti resources are provisioned as per node basis (i.e., smallest allocation one can get is at least one node) 

- [x] **Q12: Why Puhti, MAHTI, LUMI are not considered to be cloud enviroment as well?**
    - A: Typically a cloud environment is exclusively available to you, whilst supercomputing environments are shared systems with even up to thousand simultaneous users. Supercomputers use batch job (queuing) systems for this reason, and they typically can also give access to much larger resource allocations because of this compared to cloud resources.

- [x] **Q13: While accessing puhti via ssh (login node) how do I switch to a compute node?**
    - A: By submitting batch jobs to queue or requesting an interactive session. This will be covered in more detail in [batch jobs](https://csc-training.github.io/csc-env-eff/part-1/batch-jobs/) part of the course and in ["running jobs" in docs.csc.fi](https://docs.csc.fi/computing/running/getting-started/).

- [x] **Q14: While using the puhti jupyter, if I have around 2 TB of files to process, how do I use CSC storage to manage it. I want the files on CSC aswell.**
    - You have to first tranfer 2 TB of your data to the scratch area of Puhti (if you are a project manager, you can increase the scratch disk space in mycscs portal if needed)

- [ ] **Q15: Hi, I've had a bit of a technical problem in ne part of the prereq course, but I wasn't sure who to email about it.**
    - A: Sorry to hear that! Servicedesk@csc.fi and weekly support sessions are always good places to ask questions. What kind of trouble you had?
    - Q: The links to the videos in the documentation area under each topic don't open for me. I try to login with my CSC credentials but get an error that my username has not been found. (It's the same username and password I use for the my.csc.fi website). Specifically these two videos: First Glimpse of the Shell 1-4; Nano, Emacs, Vim. Should I send an email about it or is this an access issue that can be resolved from the owners of the course?


- [x] **Q16: In the nodes you said there are several cores, are those "threads" or does each core has 2 threads like in local cpus?**
    - A: Yes, each node has multiple cores (40 on Puhti, 128 on Mahti) and each physical CPU core has two hardware threads.
    - A: It should be noted that hyperthreading is not that useful in most HPC use cases. In most cases you should use 1 cpu/core per software thread.

- [x] **Q17: I have been using the normal ssh  command ssh <username>@puhti.csc.fi    # replace <username> with your CSC username, e.g. myname@puhti.csc.fi to login to puhti but nowadays it works while adding ssh -m hmac-sha2-512? I'm using windows.**
    - A: The need to explicitly specify the message authentication code (MAC) is related to a bug in some windows ssh clients. See more details at https://docs.csc.fi/support/faq/i-cannot-login/#why-is-my-ssh-client-saying-corrupted-mac-on-input

- [x] **Q18: Can we set read-only permissions to entire folders?**
    - A: Sure, for example `chmod -R g-w my_folder` would make a folder `my_folder` and its contents read-only for your UNIX group members (i.e. others in your CSC project). `-R` activates the recursive mode.

- [x] **Q19: When I use the lue module in my home directory, it shows that there was permission denied for 444 files. Is this normal or could there be a problem? I would've thought that I would have apermission on everything on my $HOME (that's also what's shown in the tutorial). Correction: 444 is the number of files, none were denied. I kept misreading it for 15 minutes. Sorry and thank you!**
    - A: Ok! :) Yes, all files in your $HOME should be owned by you and thus there shouldn't be any permission denied errors. If such a thing would anyway happen, only way to fix it is to contact servicedesk@csc.fi 

- [x] **Q20: hi! Should I have access to the course project in csc? I couldn't see it in puhti. If that's the case could you please add me? 🙂**
    - A: If you have another project, you can also use that for the course! If you don't have any project, let me (Maria) know, or follow the instructions in the "prerequisite mini-course"!

- [x] **Q21: Is the private SSH key restricted to one computer only? I have two computers, one for work (issued by HY) and the other is personal. If I connect to Puhti using the SSH key, do I have to generate two private/public key pairs for respective computers?**
    - A: Technically it is possible to copy the private key to another computer (e.g. by moving it on a USB stick), but it's recommended to have separate keys for each computer. This has a couple of advantages:
        - The secret key never leaves your computer, so it's harder to steal it (think: losing the USB stick, someone getting it from the cloud service you uploaded it to for transfer...)
        - If you find that the key is compromised (e.g. you accidentally paste its password somewhere you didn't want to), it's easy to remove its public key part from the target machine while still retaining easy access from your other computer

- [x] **Q22: Are module handling recommendations (related to conda etc.) also relevant to cloud services like e-/cpouta?**
    - A: Not really: Pouta does not use modules like the supercomputers do, as when you have a Pouta virtual machine, you are in complete control of it: you can install any software you like. It also doesn't use Lustre, so you don't need to worry about the small files created by conda installations. If you use different software with conflicting dependencies (e.g. two Python programs that need different versions of the same package), you of course need to use conda or other such tool for separating those environments each other, but no need to worry about Tykky or `module load`s or such.

- [x] **Q23: I'm not sure if this is the right time to ask this but here is goes. I recently needed to use scikit-bio in jupyter-lab in puhti which wasn't available. Is there any method to load these specific packages for python in my own environment?**
    - A: In this case you could install scikit-bio and jupyter-lab yourself using e.g. the Tykky tool. See https://docs.csc.fi/computing/containers/tykky/ and also https://docs.csc.fi/computing/webinterface/jupyter/#tykky-installations.

- [x] **Q24: Shall we complete the e-learn course "csc computing environment" as well, i.e. is watch videos, do all tutorials and quizes etc.?**
    - A: The materials there are pretty much the same stuff that we cover during the course days, so watching the videos and re-reading the slides etc is not mandatory. Completing the "extra" tutorials is also up to you, we recommend those that seem relevant to you! If you want the certificate for completing the course, you must complete the quizzes though.

- [x] **Q25: There seems to be a bug in the first quiz of the e-learn course (Topic 2: Quiz: HPC environment). I cannot fill in the first blank.**
    - A: The "Quiz: HPC environment" one? I cannot reproduce the problem. Have you noticed that you don't need to type anything: the answer selection is available for drag'n'dropping on the right side of the text. If you are working on a mobile device, changing to a desktop/laptop might be worth trying. Otherwise if refreshing the page does not work, let us organizers know and we will figure it out!

- [x] **Q25 cont.: Quiz: HPC environment. Yes, I noticed it's drag 'n' drop, and I'm working on my laptop, also I refreshed the page. But the problem remains. I can drag 'n' drop the words into the other gaps, but not into the first one. It doesn't stay, but flies back immediately... Thanks!**
    - A: Thanks, we will investigate :) 
    - A: Nothing seemed to be wrong, however I was able to reproduce the problem. I saved the quiz again and after that it seemed to work for me, so maybe something resetted. 

- [x] **Q26: I am a bit lost about the parts where conda and python were mentioned. From what I understood is that we're working on linux terminal and we're using that, so what does python have to do with that and what is a conda? I'm not sure if my question is clear but I'm generally confused about what that is.**
    - A: Python and conda are different things but very closely related.  As you probably know Python is a programming language. Conda is an open-source package manager  also for python packages. In other words, conda environment can be used to install python packages on e.g., Linux environment. 
    - A: So if you are not using Python yourself, no need to worry about the Python/conda stuff! It's just fairly commonly used (and a common pitfall when it comes to the small files), and that's why it comes up in the examples.
    - Q: It was brought up during the installation of the software I'm using because an 'add-on' to the software needs a conda-based installation. I didn't understand what that is at the time, but if I get it correctly now, then it's just basically using the conda package manager to install that software? Is it either that OR containerization, where containerization is prefered because of the issue with 'many small files'? I'm sorry if I'm not so clear but it's a bit confusing to me. I ended up not installing it.
      - A: Yes, the original instructions referred to using Conda to install the needed extra parts. In CSC HPC servers the use of Conda as-is is not allowed. Instead we have tool called [Tykky](https://docs.csc.fi/computing/containers/tykky/) that can be used to install Conda environments as containers. If you need some add-on to software, the software itself + the add-ons need to be installed with Tykky so the software can see the add-ons.

- [x] **Q27: What does it mean when it says we can "write our own module files"? Does this mean we just install our own software and package it into a module? What difference is that from just running a software that we installed on the puhti projappl for example?**
    - A: when we say we can write our own module files, it means that we  install our own software and then we create lua file (Lua is a kind of scripting language) to load all dependent libraries and add executable paths for the installed software. This way, we can just load a module without needing to care for dependencies and adding paths before using it.  This is very important when there is a lot of software stack to manage. It may not be that important if we have few software programmes to manage. Alternatively, if you install a software and take care of adding binary paths and dependencies for it by yourself, that is just fine and no need to worrry about module system. In term of functionality there is no difference. 

- [x] **Q28: What is the difference between needing memory and needing cores? How can I determine what resources my job needs?**
    - A: CPU cores are what your program uses to run calculations and otherwise execute your program (from a computer's point of view, each step in your program is actually some kind of a mathematical operation or a series of them). Memory is what holds the numbers on which those calculations are currently carried out: this could be variables, arrays, images, text... Note that this is different from disk space though: even if you handle e.g. terabytes of images from disk, it might be that only one image at a time is loaded in memory if they are processed one at a time. It's not easy to give "one size fits all" answer that would cover all cases when it comes to determining how much resources your job needs, but here are some pointers that might help you:
        - have you run your code on your own machine and either run out of memory or the execution takes up all available CPU?
        - run a small test in the `test` queue on Puhti, see what `seff <your jobid>` says and adjust accordingly

- [x] **Q29: How do I know if my job is considered as "heavy" computing or not? What would be the parameters (e.g. memory use) that define a job as light, moderate or heavy computing?**
    - A: Bit difficult to suggest on a general level. Good starting point is to check application documentation where you may find whether the application is memory intensive, parallelisable or has specific resource needs. Besdes,the software itself, the amount of data you are processing can also decide what kind of resources you need. Once you get some idea about the software you can start with small data and perform some pilot experiments with minimal resources. You can then scale up the resources and data as needed. Only experience will help us better. Obviously, you can always ask the developer of the tool to know more information instantly and have a head start.

- [x] **Q30: What is considered a 'task'? In terms of the batch job script. How do I know how many tasks my job will have and how many CPUs I will need per task?**
    - A: Slurm tasks refers to the number of MPI processes you use to run your job. How many you can use depends on your software. If your job supports MPI, you may request multiple tasks, but the optimal number depends on other factors, e.g. how big your calculation is. Note that just adding more tasks may not make the calculation faster after a certain point (this needs to be tested). If your job does not support MPI, requesting multiple tasks would just result in running the same thing multiple times.
    - A: By default one thread (or "CPU" in Slurm terminology, `--cpus-per-task`) is launched for each task. If your software implements both MPI parallelism *and* OpenMP threading, you may launch multiple tasks and also multiple threads per task. The total number of threads (CPUs) can be at most equal to the number of physical cores on a single node, or virtual cores (2*physical) if using hyperthreading. If your software implements only OpenMP, then you should use just `--ntasks=1` (but multiple `--cpus-per-task=N` is ok)
    - A: So for the question "how to know?", 1) read the documentation (both the official documentation of your software and docs.csc.fi) and 2) test!

- [x] **Q31: The third question in the batch job quiz (where you have to move the command blocks into the right boxes) isn't working!**
    - A: Thanks for reporting, will check! 
    - A: Checked, and wasn't able to repeat this either :/ Although it DOES require a little bit patience, and hovering the text box above the correct area (color changes and then the text box can be dropped). ***Can you let us know which browser and OS you are using?*** 
    - I am using google chrome, but i got it to work now!

- [x] **Q32: I didn't understand the part about the line endings. Is this something we need to worry about if we're using powershell to access puhti or?**
    - A: It something that is good to be aware of. Sometimes when you create files with Windows there may be hidden characters added at the end of lines that will cause things to fail on Linux. Converting with `dos2unix` will solve these issues. So if you get strange errors and are not sure why, `dos2unix` is good to try!
    - Q: So this is something we need to worry about if we created a batch job file (or any other one) within windows that we then want to import and run on Linux, yes?
    - A: Exactly.

- [x] **Q33: Are we allowed to use input from one project and set the output to be in another project's scratch folder?**
    - A: If you're a member of both projects, this is possible.

- [x] **Q34: How do we know if increasing the resources will not offer so much to our tasks?**
    - A: It may be hard to say beforehand, this is why it is good to test. E.g. run with 1, 2, 4, 8, ... cores and see does the job always get twice as fast when you double the cores. Rule of thumb is that the job should be *at least* 1.5 faster when doubling the number of cores.
    - A: Regarding the memory, a good way is to do a test and then check with `seff` how much memory was used.

- [x] **Q35: What causes the slower performance of runnig batch jobs during high load times? I noticed that during Christmas break my models were running much faster than e.g. a month earlier even though the model should take similar running times.**
    - A: Are you sure that your job really ran faster, as opposed to just finishing earlier due to having spent less time in the queue?
    - A: If your job is disk i/o dependent it could be related to load on file system (i.e. /scratch can get slower under heavy load). Perhaps your jobs would benefit from using local nvme disk?

- [x] **Q36: how can we check for all these points mentioned? e.g. if cores are waiting, How do we know that, and then how do we address that? and the rest of the points as well, how do we test or check for them? If the seff doesn't see that all the memory is used, how would I know that I'm running out of memory and ralize that I need to request more?**
    - A: Usually seff works fine enough. If your program uses more memory than allocated and is thus killed, `seff` fill show the job as `FAILED`. You can also see lines like `slurmstepd: error: Exceeded job memory limit` and `slurmstepd: error: StepId=21338959.batch exceeded memory limit (2367488 > 1048576), being killed` in the `slurm-<jobid>.out` file. When it comes to your run just being slower than you'd like, and cores idling, it's hard to give a definite answer on how to debug that: it depends a lot on what you are doing. You can always ask servicedesk@csc.fi for help in your specific case though, if you cannot figure out why your jobs aren't as efficient as they should be! Some pointers are available in [performance checklist in docs.csc.fi](https://docs.csc.fi/computing/running/performance-checklist/).

- [x] **Q37: What is sacct? How is it different from srun?**
    - A: https://docs.csc.fi/computing/running/submitting-jobs/ sacct = information about your past jobs, srun = submitting jobs in the batch script

- [x] **Q38: "If CPU efficiency seems too low, look at the completion time" what does the completion time tell us?**
    - A: This is mainly in reference in finding out the best number of CPUs for you job. If e.g. decreasing number of cores makes the job slower or increasing the number makes it faster, you should look at the completition time more than the listed CPU efficiency. 

- [x] **Q39: Can we then reserve more memory but less CPU? Is a job killed if it's not using enough CPU/more memory than allocated?**
    - A: Jobs will indeed be killed if they use more memory than is allocated: it would not be good if your program could write outside its allocated space, possibly on top of someone else's allocation. Jobs will not be killed for under utilizing CPU though (but it's still adviced to not reserve more than you need, both to shorten the time your jobs spend in the queue and to use the shared resources efficiently)

- [x] **Q40: Where can one check the disk workload?**
    - A: The global workload of the disks in the system can be seen e.g. on puhti.csc.fi: the usage metrics box includes disk lag. When it comes to how disk-heavy your program is, you can often get an idea just by figuring out how much data it reads from/writes to disk, and whether it's a large or small number of files. You can also test whether your program gets faster if you try using the local NVMe disks at $TMPDIR.

- [x] **Q41: What is an array job? and what does the last line in the batch script mean? /appl/soft/bio/course/sacct_exercise/test-a ${SLURM_ARRAY_TASK_ID}**
    - A: Array jobs is something you do when you have multiple similar independent tasks to run, for example you run the same analysis steps to multiple files. https://docs.csc.fi/computing/running/array-jobs/
    - ${SLURM_ARRAY_TASK_ID} = looping through the array jobs
    - Q: How can we determine if we should use such a job instead of the other kinds?
    - A: As mentioned, when you have many independent similar jobs, you can use array jobs. You dont need to write any loops, array job will take care of submitting those independent jobs to cluster based on the parameters you have supplied to sbatch directive of array flag (see more information in the above link). Please note that these independent jobs should take reasonable computational time (if they are too short, it would be overkill to submit as a seperate job) and also come with limit on the number of jobs one can submit (on Puhti maximum limit is 200 jobs)

- [x] **Q42: What does root-level mean?**
    - A: Root-level = main level when talking about file locations. A person with root level access = "administrator," "root user" or "superuser.")
    - A: And when talking about something being located "at root" or "root level", it means that it's location in the file system or such is directly at the "root" of the file system: there are no intermediate directories or such. For example a text file in someone's home directory might be found at `/home/someone/coolfile.txt`, whereas a file at root would be simply `/coolfile.txt` (but it would be unusual to have such a file in such a location)

- [x] **Q43: Does that mean that a folder with other files in it inside a bucket is treated as one object alongside everything inside it?**
    - A: We have a nice example tutorial about these cases: https://csc-training.github.io/csc-env-eff/hands-on/allas/allas-tutorial.html

- [x] **Q44: How do we know if our job would need an NVMe? Why doesn't the job use scratch for space?**
    - A: One obvious symptom suggesting that NVMe would be good is if your job runs faster on your own laptop than on Puhti. The disk on laptops is NVMe.
    - A: Also, knowing what your job does is of course useful. If you know beforehand that it will read/write a lot of (small) files, then NVMe may be useful (both to increase performance and avoid stressing the file system for all users).
    - A: Bottom-line: scratch space sits on the shared file system and performs poorly if your job does a lot of I/O. For other use scratch is just fine.

- [x] **Q45: From what I understood, loading  module loads its dependencies. Why then do we need to check with spider if there's anything else we need to load for our module?**
    - A: module **spider** command does not load your application/sofwtare. It would only search if the searched module exists in the installations. 

- [ ] **Q46: Are containers and images the same thing? What about dockers and tykky? A place where all the small files are treated as one large one if I understand correcty. What was the container registry/container wrapper that was mentined in the lecture yesterday. There was a lot of new terminology for me and I didn't understand what was downloaded from the quay.io website.**
    - A: People use containers and images interchangeably but they are not same. Container is more like an instance of image (or you can also think of container as image in action). When container is spawned, image is converted to a filesystem and you can launch as many containers as possible. Docker (also a company name) is a type of container platform like Singularity/Apptainer. Tykky is an in-house developed container wrapper at CSC to take of python-based installations of a complex software. Container registry is more like a database of images, usually hosted by organisations or companies. Dockerhub and quay.io are couple of examples of image registries. In the example, you were downloading image from the quay.io registry.
    - **Q: Is a container wrapper then the software that puts other applications into containers? And in this context is an image some kind of application?**

- [x] **Q47: What are the allas-cli-... directories created when using Allas?**
    - A: allas-cli-utils is the CSC provided toolkit for using Allas. You can download it to your linux or mac if you wish to use Allas wit the same command that waht we have in Puhti and Mahti (https://github.com/CSCfi/allas-cli-utils)

- [x] **Q48: If file transfer takes longer than 8 hours and the Allas swift connection gets interrupted, what will happen? Will the files be corrupted?**
    - A: In generally, you should remove the partly uploaded data and try again. There are special tools that you cann use in case of large data transfers. e.g. https://github.com/CSCfi/allas-cli-utils/blob/master/help/allas-dir-to-bucket.md We will cover this issue more deeply in the advanced course.

- [x] **Q49: Would we have a chance until the end of today or.. ? to ask any remaining questions on HackMD?**
    - A: Yes, we will keep the HackMD open for today. After this we will close it from editing, but you will have the read-only access to the document. After that, you are most welcome to ask questions in our weekly research user sessions (every Wednesday 14:00-15:00 in Zoom: https://ssl.eventilla.com/usersupportcoffee).

- [x] **Q50: In the breakout room with Rasmus, something was mentioned about creating .tar files. What was the question at the time and why/how would we need to create them?**
    - A: .tar archives are useful if you want to package your directory as a single file. I guess the question was about transferring a whole folder to Allas and whether we can be sure that the folder hierarchy is preserved even though Allas only has two levels of hierarchy (buckets and objects). If you want to be sure, then creating a tar archive (and optionally compressing) it before transfer to Allas is one way. If you use a-commands (e.g. a-put) to upload to Allas, then this will actually do the archiving for you, so no need to worry about it separately! One can also add `-c` option to compress it. See https://docs.csc.fi/data/Allas/using_allas/a_commands/ and https://docs.csc.fi/support/tutorials/env-guide/packing-and-compression-tools/

- [x] **Q51: If I installed some software on the projappl folder, and its GUI is web application that I can access from my browser via localhost, is there a way to launch this web application though the interactive partition? Would the application then be able to submit batch job scripts for the processing tasks of the software itself? The current set-up is that the web application is launched through the login node (from my understanding, that is to enable the software to submit batch jobs).**
    - A: This sounds like a quite complicated use case. Perhaps you could send a more detailed email to servicedesk@csc.fi ? This page might also be helpful: https://docs.csc.fi/support/tutorials/rstudio-or-jupyter-notebooks/ (it is about running rstudio and jupyter, but the SSH tunneling principles should be the same for any application)



---
**:arrow_up: Write your questions above this line :arrow_up:**

---

## Feedback day 1

One thing you liked:

- Overall it was really good day and special thanks for going through the hands on exercises together! 
- The lecturers are very patient and helpful. Thank you all for your time!


## Feedback - Day 2

One thing you liked:

- The hands-on sessions 
- Live answering of questions

One thing that could be improved:

- The handson sessions could be a bit longer 
- Some more difficult points could be discussed at a slightly slower pace
- ..

When you have time, please give us feedback also through the Official Feedback Form: https://ssl.eventilla.com/feedback/101HXA3xno3Jbzl
(This is required to get the course certificate, in that case, give the feedback thru e-Lena!)


## Useful links 
- [Elements of Supercomputing](https://edukamu.fi/elements-of-supercomputing) online course
- [Training links](https://docs.csc.fi/support/training-material/#training-materials-and-sources-from-csc-and-partners) by us and our friends
- [Weekly research user meetings](https://ssl.eventilla.com/usersupportcoffee) (come and ask anything! Also course related questions are welcome!)
- [Data management self-learning course](https://e-learn.csc.fi/course/view.php?id=63)
- [Sensitive Data (SD) services webpage](https://research.csc.fi/sensitive-data)
- [Sensitive Data (SD) services user guide](https://docs.csc.fi/data/sensitive-data/)