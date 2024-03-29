# Minecraft_AI

<p align="center">
    <img src="https://i.imgur.com/BZEw7mA.png" width="300px" alt="Logo for MinecraftAI">
</p>

MinecraftAI is an add-on to Minecraft Education edition allowing users to generate machine learning and AI models that can predict and manipulate the game. The purpose of this project was to education and introduce machine learning concepts to high schoolers. As a team we wanted to achieve our goal while still keeping the fun and creative aspects that the Minecraft world brings. Minecraft Education team B has made a tool that helps the users and developers connect, communicate, and analyze while navigating the Minecraft education world. 

## Team
The members of Minecraft Education B are as follows:
* **Nathan Nesbitt** - [Nathan-Nesbitt](https://github.com/Nathan-Nesbitt)
* **Kathryn Lecha** - [kzlecha](https://github.com/kzlecha)
* **Carlos Rueda Carrasco** - [Carlos-Rueda-Carrasco](https://github.com/Carlos-Rueda-Carrasco)
* **Adrian Morillo** - [sonorousAd](https://github.com/sonorousAd)

## How to get the API running
<p align="center">
    <img src="https://media2.giphy.com/media/dZMW8MJLBjoOVzDtK1/giphy.gif" width="550px" alt="Logo for MinecraftAI">
</p>

Step 1:
- Download the newest release

Step 2:
- Unzip the the MinecraftAI_v***.zip folder and double click `main.exe` or you can also open the application through step 3-5.

Step 3:
- Open Terminal/Command line

Step 4:
- `cd` to the directory of the contents from the zip folder

Step 5:
- Once there simply run `./main.exe` to start the api running

## Frontend Design Overview
The front end of the application runs on a combination of HTML,CSS and JavaScript that use Bootstrap as the underlying toolkit. The page is made to be displayed ‘in-game’ and maintains consistency with the Minecraft theme and overall feel.

### Its components are the following:

#### Home page (Main_page.html)
- This is the home page of our system where the user will land as they first open the application. It allows the user to choose between `Free Code` and `Lessons` options.

#### Lessons page (Lessons_page.html)
- This page contains the various lessons available to the user, they are presented in a carousel style where each lesson appears in the center of the page and the user can slide left or right to display the different lessons.
Custom lessons can be created and integrated into the game by downloading them or linking them from within the game.
- One core feature to this page is that it allows the user to import lessons other than the pre build ones. The lessons have to be written in a markdown file. This allows for anybody to write custom lessons on the platform.

#### Lesson overview (lesson_overview.html)
- This page contains an overview of the selected lesson that will explain to the user what will be done in the lesson and what its goal is.

##### Examples of lessons:
- Ore Finder: `we are looking for a depth. This can be any value on the number line. Since we are looking for a value on the number line and not a group, this is a REGRESSION problem. This model will make the bot mine at the predicted depth and biome.`

- Data Collection: `we are looking to pull in data from the game for the block broken event. Whenever this happens in the game, we want to save the information relating to that event, such as the type of block that was broken and where it was broken.`

#### Lesson Explanation (lesson_explained.html)
- This page will display a more in depth explanation of the lesson and the appropriate AI concept and the tools used to solve the underlying problem. It will usually contain a graph that illustrates the AI concept used and its application to the lesson.

#### Coding page (Code_page.html)
- This page contains the code editor embedded in the page where the user will implement the AI concept and solve the task at hand. Instructions are found in the top right corner under the question mark symbol and will change as the user advances through the lesson. The code will auto fill by clicking on the indicated button thus allowing the user to understand the purpose of the added code and follow the step by step guide of its implementation.

#### Free code(Free_Code_page.html)
- This page follows a similar design then `Code` page. Here, users can freely code and explore Minecraft by writing any javascript code in the editor and implementing it in the game, this page also provides instructions on how to utilize various commands and functions.
Below the coding environment a terminal is located, here the user can see the more technical details of their code and further work on their ideas.

## Backend Design Overview

The back end of the application communicates with the frontend and handles incoming requests. Such requests are to either store and handle data from the game or to manipulate the data and perform a statistical analysis. It is composed of three major components:

The first being the `Broker` that communicates with the backend and channels requests to the appropriate libraries. The second being the `Minecraft_Store` and `Data` that processes, stores and formats the data in a CSV format for the `Minecraft Learns` AI library to use. Lastly, there is the Model Minecraft_Learns library that is called and used to process, train, model, and then predict a response variable. 