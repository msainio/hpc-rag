---
title: Using CSC HPC environment efficiently 12.-14.4.2023
tags: [puhti, mahti, allas]

---

# Using CSC HPC environment efficiently 12.-14.4.2023 

###### tags: `puhti` `mahti` `allas`

> This is the collaborative "notebook" for the "Using CSC HPC environment efficiently" course organised in April 2023 by CSC -IT center for Science. 
> [Prerequisite course page in eLena platform](https://e-learn.csc.fi/course/view.php?id=75)
> [Course page in eLena platform](https://e-learn.csc.fi/course/view.php?id=76)
> [Collection of slides and material](https://csc-training.github.io/csc-env-eff/)
> [Zoom-link for sessions](https://cscfi.zoom.us/j/69471149828)
> [Zoom-link for SUPPORT SESSIONS / weekly user meetings](https://cscfi.zoom.us/j/65059161807)


:::danger
:calendar: The latest updates on the **course schedule** can be found in here.
:interrobang: This is also the place to ask questions about the workshop content! We use the Zoom chat only for posting links, reporting Zoom problems and such.
:::

:::info
:bulb: **Hint:** HedgeDoc is great for sharing information in this kind of courses, as the code formatting is nice & easy with [MarkDown](https://www.markdownguide.org/basic-syntax/)! Just add 3 ticks (``` ` ```) for the``` code blocks ```.  
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

### Prerequisite / support session 5.4.
14:00-15:00 Join the pre-course support session, which is also part of [CSC's weekly user meetings](https://cscfi.zoom.us/j/65059161807)

### Day 1: Wednesday 12.4.


 
 
| Time  | Content |
|-------|---------|
| 8:45  | Login, check connections work, test microphone |
| 9:00  | Welcome, course practical info, learning targets,  ice-breaker, feedback/expectations (10 min) |
| 9:10  | **Topic 1: Prerequisites & Connecting** (15 min) |
| 9:30  | **Topic 2: Introduction to HPC Environment** (20 min) |
| 9:45  | _Break_ (10 min)|
| 9:55 | **Topic 3: Disk Systems** (10 min) |
| 10:05 | **Intro to breakout rooms & hosts, joining the breakout rooms, accessing materials** (5 min) | 
| 10:10 | **Topic 3: Hands on 3.1** (20 min) |
| 10:30 | **Topic 4: Module System & preinstalled software** (10 min)|
| 10:40 | **Topic 4: Hands on 4.1** (10 min)|
| 10:50 | _Break_ (10 min) |
| 11:00 | **Topic 7: Allas and where to keep your data and current issues**  (20 min)|
| 11:25 | **Topic 7: Hands on 7.1** (30 min) |
| 11:50 | Recap + preparations for the next day (10min) |
| 12:00 | Finish |
| 14:00 | Bonus: Join the weekly user meeting https://cscfi.zoom.us/j/65059161807  |
    
 




### Day 2: Thursday 13.4.


    
    
| Time  | Content |
|-------|---------|
| 8:45  | Channel open, "morning coffee" |
| 9:00  | Re-cap, feedback/expectations + some Qs from HedgeDoc (10min) |
| 9:10  | **Topic 5: Batch queue system and interactive use** (15 min)|
| 9:30  | **Topic 5: Hands on 5.1** (35 min) | 
| 10:00  | _Break_ (10 min)|
| 10:10 | **Topic 6:  Understanding resource usage**  (15 min)|
| 10:30 | **Topic 6:** Hands on 6.1 (35 min) |
| 11:00 | _Break_ (10 min) |
| 11:10 | **Topic 8: Installing applications** (15min) |
| 11:25 | **Topic 8: Hands on 8.4 and 8.1** (25min) |
| 11:50 | Recap + preparations for next day (10 min)|
| 12:00 | Finish |



 
### Day 3: Friday 14.4.


    
    
 | Time  | Content |
|-------|---------|
| 8:45  | Channel open, "morning coffee" |
| 9:00  | Re-cap, feedback/expectations + some Qs from HedgeDoc (10min) |
| 9:10  | **Topic 9: Containers & Apptainer** (15min)|
| 9:25  | **Topic 9: Hands on 9.1** (35 min) | 
| 10:00  | _Break_ (10 min)|
| 10:10 | **Topic 10: How to speed up jobs** (20min)|
| 10:30 | **Topic 10: Hands on** (40min)  **NOTE:** use the `--reservation=april-fourteen-course` in your batch script!|
| 11:10 | _Break_ (10 min)|
| 11:20 | Topic themed breakout rooms + ask anything on all previous topics (25min) |
| 11:45 | Recap + feedback + open questions + cleaning up files from course project (15 min) |
| 12:00 | Finish |   
    



---



## ☃️ ICE BREAKER (HedgeDoc -practice)

### Ice breakers
Let's learn how to use this HedgeDoc document by answering an ice breaker question! 


    
**Q1: What from this workshop are you going to use in the near future?**

**Answers:**

 -  How to use Allas and running batch jobs in Puhti with R 
 -  Running jobs with Puhti for analysing genomic data and hoping to use R as well. 
 -  Becoming more efficient with running batch jobs
 - Need to learn and understand and possibly help others
 - How to create pipeline for (input) data flow from another administrative domain (like Statistics Finland) to CSC super computing facility for any large scale training?
 - Is there any dependency with programming langauges, i.e. only specific set of lanaguges can be used in HPC for loading library? More specifically, how to load custom made library (in emerging langauge like RUST) in CSC environment?
 - How to run your own applications on CSC
 - I wish someone had told me earlier that this service exist
 - running batch jobs in Puhti
 - puhti
 

### Q2: What topics would you like to still discuss (in topic themed break out rooms)? 
- Continuing with exercises: Room 1 (Ari-Matti), Room 3 (Rasmus)
- R / How to use efficiently R and best pratice (Room 4, Heli)
- Sensitive data / Which csc computing services can be used for sensitive data and how much of this course applies for sensitive data handling? (Room 5, Francesca)
- ML / Best ways to deal with genome wide data (should the data be in Allas, all computing in compute node batch script I assume?) Especially some tips for R and machine learning and genome wide data (Room 2, Laxman, Mats?)
- MATLAB (Sampo, room 6)
- language (Sam, room 7)
- spatial data (Samantha, room 8)


## 📝 Q & A

Your questions are answered here. We will answer them, and this document will store the answers for you for later use! :rocket: 

:::info
Scroll :arrow_down: to the bottom of the page to submit a question 
:::



- [x] **I have difficulty pasting my questions into HedgeDoc (here). Do you have some instructions on how to write here?**

    - A: HedgeDoc can look a bit differend depending on the view you are in. Can you see the three icons on top left corner, next to HedgeDoc text? There’s pencil, this side-by-side symbol, and an eye (see below for a screenshot). In eye view, you can’t edit, you are just viewing. The other two reveal the markdown (MD) version of the page, which you can edit. I find it easiest to edit with the side-by-side view, but it can be a bit slow sometimes. First time opening the page, the small Edit (pencil) button might be on right next to the table of contents. Please note that it might make things faster if you **switch to view only mode when not editing**!

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

- [x]  **Q7: Is there a way to paste text into linux terminal using (Finnish) keyboard only. (i mean without using right click). I am using PUTTY. On windows, how about `control + shift + C` for copying and `control + shift + V` It still does not work. :(**
    - A: In Putty (and MobaXterm) paste works with shift + insert.

---

- [x] **Q8: What is the price for billing units in commersial projects?**
  - A:     More about pricing of commercial projects: https://research.csc.fi/purchasing The base package costs 1190 EUR (VAT 0 %). It includes: 20 000 BUs, 4 user accounts. Note that LUMI has a different (more affordable) pricing: https://www.csc.fi/solutions-for-business

- [x] **Q9: What is the "Jupyter for Courses" on Puhti for?**
  - A:     This is kind of a placeholder on Puhti web interface to customise your own notebooks.For example when you build a notebook with your own python environment, it is possible to render your notebook application module or environment through "Jupyter for Course". More information can be found here: https://docs.csc.fi/computing/webinterface/jupyter-for-courses/
  
- [x] **Q10: Would any kind of cluster be called a supercomputer or when is the point reached?**
  - A: Many definitions given by our specialists :) Traditionally maybe smaller clusters in universities are/were called clusters, and bigger clusters in supercomputing centers were called supercomputers. Another characteristic to a supercomputer could be the queueing system (we hear more about that tomorrow), or the way the nodes are inter.connected.


- [x] **Q11: For the Breakout rooms, what's the definition of beginners and not so beginner?**
  - A: Let's see after the talk :) Idea is to get roughly equal amount of participants in all rooms, and perhaps get those taking their very first steps with CSC services/clusters/supercomputers to one room, so maybe if you only got your credentials and logged in to Puhti and run your first unix commands for the very first time ever now for this course, you could go to the beginners room :)

- [x] **Q12: Which disk area shall I use if I'm reading and writing a lot of huge files (like several 5-10 GB fil)?Would $LOCAL_SCRATCH bring a performance boost?**
  - A:How large is huge?
  - scratch is the correct one.
  - You can try local_scratch. It may be faster, depending on what is the bottleneck of your work.
  
  

- [x] **Q13: How the path can be saved using alias?**
  - A: By saving the path, do you mean something like `export PATH=/some/path/here:$PATH`?
  - I would maybe not save it using an alias, but perhaps define a function that takes the path to be added as an input. E.g.
    ```
    add_path () {
        export PATH="$1:$PATH"
    }
    ```
    - Then path can be added with `add_path /my/test/path`
    - If by saving path you mean just a shortcut for `cd`, try `alias mypath="cd /path/to/my/important/directory"` and then run `mypath` to quickly move there.
    - 💡 Hint: You can use your folder under /scratch for the rest of the tutorials. You can save the path using an alias (with cd or echo) or somewhere in your notes. --> But this is in the tutorial
    - 
    
- [x] **Q14: What means "  Where:
   S:  Module is Sticky, requires --force to unload or purge" after csc-tools module?**
  - A: Modules marked as "Sticky" are not removed with command `module purge`. To remove them you have to use command `module --force purge` This is to protect essential modules from accidental removal.

- [x] **Q15: In Puhti and Mahti, is it faster to get/send data from/to allas than from other servers, e.g. an university server?**
  - A: This depends on many factors. Some of the factors that affect the rate of file transfer is nature of files (lot of small files or few big files), speed of your university network and client (winscp/a-tools/rsync) you are using. The transfer of data within csc environment (Puhti, Mahti and Allas) is usually very fast.

- [x] **Q16: I need to leave the session unfortunately, can you post the prep for next day instruction somewhere? Thank you it would be great if this is possible.**
  - A: Thank you for joining today! See you tomorrow at 9:00, same Zoom URL :) No specific preps needed!     

- [x] **Q17: Is there some convenient way (like md5sum) to ensure that the files are not corrupted while moving them, for example, between Puhti and Allas?**
  - A:Not in a convenient way. You can store the checksum value in a file using 'md5sum' command on Puhti or Mahti before storing data to allas. Once you retrieve the data later, you can then check the checksum value again to see if you have preserved integrity of files. 

- [x] **Q18: When I use a-put to upload the  files to Allas, if it fails due to storage limit or time limit, will it create fragments and how to detect and remove them?**
  - A: a-put will try to check the availability of required space on Allas for your object before uploading. In case uploading fails for some reason, a-put command also deletes the partially uploaded files. Alternatively, you can also double check the same with a-list command (a-list bucket_name/beginning_of_the_object). 

- [x] **What are the ameta files created in Allas?**: 
    - A: As discussed, it is a metadata file decscring the bucket. Files with  _ameta extension are automatically created when you upload files with 'a-put' command. These are analogous to the metadata files created by other swift/rclone tools

- [x] **Q20: In the Allas tutorial it's said that "a-flip is meant for files that need to be published only temporarily, for example for a one-time share". Are the files shared with this command automatically removed or became private after some time?** 
    - A: Yes, files uploaded with a-flip will be deleted once they are older than two days, see https://docs.csc.fi/data/Allas/using_allas/a_commands/#a-flip (the age will be checked when you run a-flip again).

- [x] **Q21: For the file name, should it must be without space?**
    - A: This is highly recommended practice (not necessary though). Spaces in filenames can create problems when running Linux commands if not escaped properly
    - A: If we have for example file "my file.txt" and try to look at the content with cat command `cat my file.txt` cat will actually think there are two files: "my" and "file.txt". So we have to use quotes `cat "my file.txt"` or escape `cat my\ file.txt`. There will be similar problems if file names contain characters that are used as part of commands (e.g. various brackets). While they can be handled with escape and quotes it can get a bit messy and spaces and reserved characters are best avoided in file names.

- [x] **Q22: If I need to use a fast local disk ($local_scratch) - what is the conventional way to point it to the program? Do the programs provide own parameters for this purpose (like --tmp)?**
  - A: The programs don't provide own parameters (like --tmp)to refer to local scratch by default but you can point to $LOCAL_SCRATCH as a temporary directory when needed. One conventional option is to actually go to the local scratch directory on compute node and perform all your data analysis in that folder as shown roughly below:

```
- cd $LOCAL_SCRATCH (and also copy your data to the scratch folder and perform all preprocessing on data if needed there)
- your program command (and refer the data in local scratch folder as input to your programme and direct all results to the local scratch area)
- mv results_folder /scratch/<project>/$USER/  # remember to copy your results to scratch area
```

all of the steps have to be described  either in batch script (https://csc-training.github.io/csc-env-eff/hands-on/disk-areas/disk-areas-exercise-fastdisks.html) or as part of interactive jobs (https://docs.csc.fi/support/faq/local_scratch_for_data_processing/)

- [x] **Q23: What is a Docker container image?**
    - A: You will learn more about containers later in this course. Docker is one of the popular container platforms. And the  docker image is a read-only template (or actually a layered file system in case of docker) that contains everything (=all runtime environment) for creating a container. In a way, you can think of container image as a standalone (executable) file to run your application.

- [x] **Q24: After installing the metabat program with tykky, should I always add the bin directory to the $PATH before starting to work with program again?**
    - A: Yes. You are right - one should to add 'bin' directory path to $PATH variable before calling metabat program
    - A: With Tykky installed software it is highly recommended to only add them to PATH when actually using them. The installation directories often contain common things like Python. Having those in your PATH can cause conflicts with other software.


- [x] **Q25: Should I see from the documentation if the program can use more than one core? Is there some examples?**
  - A: Usually, yes. You can check the different flags (cores/threads) for your programme in that programmes documentation. But sometimes, it may not be obvious from documentation. You need to become familiar with the code you are using so that you know how it is best used; serial or parallel. There will be more information on different parallelization schemes / possibilities in the last lecture.

- [x] **Q26: Could you recommend some nice tutorials to learn grep and awk?**
  - A: Here's CSC's own Linux guide which might be helpful to get started: https://docs.csc.fi/support/tutorials/env-guide/

- [x] **Q27: As the conda environments are containerized with tykky, is it enough to just delete the container when not needed anymore?**
  - A: Yes. You can just delete the whole installation folder.


- [x] **Q28: Is it possible to leave this open over weekend? At least, I would like to do all the exercises in tutorials and it would be nice to have an option to ask.**
    - A: Ok, we can do this, only for you nice & brave people <3 We will keep it open for editing until Monday. I would also like to remind that you can continue the exercises and join the weekly support sessions (every Wednesday at 14-15) to ask about the course things too! You are ALWAYS welcome to these sessions, and you'll meet our friendly faces there :) https://ssl.eventilla.com/usersupportcoffee

- [x] **Q29: Is it OK to share the course material to a collegue?**
    - A: Absolutely! This material will stay here: [Collection of slides and material](https://csc-training.github.io/csc-env-eff/) Also, the online self-learning course in Elena is free and available for everyone, it contains the same material + some quizzes to check your learning: [Course page in eLena platform](https://e-learn.csc.fi/course/view.php?id=76) And it is totally ok to join the [weekly user support sessions](https://ssl.eventilla.com/usersupportcoffee) to ask about the course exercises as well!
> 

- [x] **Q30: Is it possible to have sudo rights inside a container?** 
  - A: Only if you have sudo rights in the host. When run with user rights, you only have user rights in the container.

- [x] **Q31: Is it correct that single tasks can be split to at most 20 CPUs on Puhti only, or is there any option to spool up more CPUs for a single task? I would imagine that this is not possible since the 2x20 CPUs on a single node are not sharing the same chache, right?**
    - A: Each Puhti node has 40 physical cores (2 CPUs with 20 cores each), so you can launch at most 40 threads from a single task.

- [x] **Q32: What are the differences between /scratch and $LOCAL_SCRATCH**: 
   - A: Some differences:
Technical: /scratch is on Lustre parallal file system. $LOCAL_SCRATCH is on a physical NVMe solid state disk installed in the node
Speed: /scratch is slower and performance can suffer especially if accessing many small files. $LOCAL_SCRATCH is fast and can speed up jobs that rely heavi on disk I/O.
Visibility: /scratch is visible from all nodes. $LOCAL_CRATCH is specfic to a single node.
Permanence: Project /scratch directory will exist for the life time of the project. Files wil exist 180 days (if unused). $LOCAL_SCRATCH allocation is specific to a job. After the job finishes, the allocation and files will be deleted. Remember to copy all necessary files to /scratch as part of the job.

- [x] **Q33: After containerizing a Conda environment with Tykky, is the correct way to use it just to add the bin to the path and start to use different tools?**
    - Yes! These "binaries" for the different tools are actually wrapper scripts that do quite a bit of things automatically for you and finally call the actual binaries within the containers. Nothing else needs to be done.

- [ ] **Q34**: 

- [ ] **Q35**: 
---
**:arrow_up: Write your questions above this line :arrow_up:**

---


**Testing area:** Here you can test how to use HedgeDoc :)
test tes te


---





## Useful links 
- [Containers course in June]( https://ssl.eventilla.com/containers-in-supercomputing-environment) (registration now open!)
- [The CSC Summer School in High-Performance Computing 2023](https://ssl.eventilla.com/summerschool2023) (Registration open now)
- [Elements of Super computing](https://edukamu.fi/elements-of-supercomputing) online course
- [Training links](https://docs.csc.fi/support/training-material/#training-materials-and-sources-from-csc-and-partners) by us and our friends
- [Weekly research user meetings](https://ssl.eventilla.com/usersupportcoffee) (come and ask anything!)
- [Data management self-learning course](https://e-learn.csc.fi/course/view.php?id=63)
- [Practical Deep Learing course](https://ssl.eventilla.com/event/8aPek)
- [Sensitive Data (SD) services webpage](https://research.csc.fi/sensitive-data)
- [Sensitive Data (SD) services user guide](https://docs.csc.fi/data/sensitive-data/)