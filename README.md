# LinkedinEasyApplyJobsBot
A python bot to easy apply sinlge,double,triple and up to 5 pages long Linkedin Easy Apply jobs
To modify, use, get documentation or for you inquires you can email, ongun.demirag@gmail.com

Features:
- Ability to filter jobs, by easy apply, by location (Worldwide, Europe, Poland, etc.), by keyword (python, react, node), by experience and position
- Automatically apply single page jobs in which you need to send your up-to-date CV and contact
- Automatically apply two, three, four and five pages long offers with the requirements saved in LinkedIn like experience, legal rights, resume etc.
- Print the links for the jobs that the bot couldn’t apply because of extra requirements. (User can manually apply them to optimize the bot)
- Put time break in between functions to prevent threshold.
- Automatically apply for jobs
- Automatically run in the background
- Compatible with Firefox and Chrome
- Runs based on your criteria’s
- Much more!


How to setup: 
This tutorial briefly explains how to setup LinkedIn Easy Apply jobs bot. With few modifications you can make your own bot or try my other bots for other platforms.
1)	Install Firefox (90.0.2) or Chrome. I was using Firefox for this so I will continue the usage of it on Firefox browser. Process would be similar on Chrome too.
2)	Install Python. My version is 3.9 .6
3)	Download Geckodriver put it in Python’s installation folder.
4)	 Install pip, python get-pip.py
5)	Install selenium pip install selenium
6)	Download the linkedineassyapply.py code 
7)	Create a profile on Firefox, about:profiles
8)	Launch new profile, go Linkedin.com and log in your account
9)	Copy the root folder of your new profile, to do that type about:profiles on your Firefox search bar, copy the root folder C:\---\your-profile-name.
10)	Paste the root folder on webdriver.Firefox(“root-directory”) line
11)	Modify/adapt the code and run
12)	After each run check the jobs that the bot didn’t apply automatically, apply them manually by saving your preferences 
13)	Next time the bot will apply more jobs based on your saved preferences on Linkedin. 
14)	Feel free to contact with my for any update/request or question. 

![1](https://user-images.githubusercontent.com/34207598/128695723-2af373a6-3fbb-4dcc-9bba-24af57f17ee9.png)
![2](https://user-images.githubusercontent.com/34207598/128695725-5250cc6d-72e7-4a79-b060-8decfb9be54a.png)
![linkedineasyapplygif](https://user-images.githubusercontent.com/34207598/128695728-6efcb457-0f75-42e2-987a-f7a0c239a235.gif)
