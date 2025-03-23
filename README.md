
# HackHerSpace

![Logo](static/assets/Images/HackHerSpace-logo.png) 

# Table of Contents
- [User Experience](#user-experience)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Design](#design)
- [Agile Methodology](#agile-methodology)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Code](#code)
- [Testing](#testing)
    - [Bugs](#bugs)
    - [Testing User Stories](#testing-user-stories)
    - [Manual Testing](#manual-testing)
- [Deployment](#deployment)
- [Maintenance](#maintenance--updates)
- [Credits](#credits)

## ![favicon](static/assets/favicon/favicon-16x16.png) User Experience

### Project Goals
HackHerSpace is a project by 5Stars Team with the primary goal of uplifting, supporting, and inspiring women in coding and STEM fields. 5Stars Team aims to create a welcoming and inclusive community where women of all ages, backgrounds, and experiences can pursue their dreams in the tech industry.

As a member of HackHerSpace, you can take on the role of a mentor, sharing your knowledge and guiding other women in coding and technology. Or, as a mentee, you can learn from experienced women in the field, gaining valuable skills and support in a safe and encouraging environment.

### User Stories
**1. As a 15-year-old girl with an interest in ICT, I am looking for a place where I can connect with other girls and peers who share my passion. I want to have conversations about technology and feel part of a supportive community.**

Acceptance Criteria:

* Users can sign up and create a profile.
* The UI is responsive and accessible.
* Users can post, reply, and engage in discussions.

Tasks:

* Set up Django for user authentication (registration & login).
* Use Tailwind to design a friendly and accessible UI.
* Create a discussion forum where mentees can ask general questions



**2. As a woman interested in computing, I would like to learn more about the contributions of women in both the past and present. I want to discover inspiring female role models who can serve as my ‘heroines’ and motivate me in my own journey.**

Acceptance Criteria:

* Users can browse profiles of influential women in tech.
* The design is engaging with images, quotes, and contributions.

Tasks:

* Create a “Women in Tech” section with profiles of historical and modern figures.
* Use Tailwind to design a hero section featuring inspiring women.



**3. I would like to meet other women in a safe and inclusive environment where I can develop my skills and confidence without being affected by stereotypes associated with the male-dominated tech industry.**

Acceptance Criteria:

* A reporting system is in place for inappropriate content.
* Users can join and participate in safe groups.

Tasks:

* Allow users to report inappropriate content to ensure safety.
* Set up moderation tools in Django Admin to manage reports.



**4. I am a woman who has started learning to code, but I sometimes feel discouraged because I don’t see many women around me in tech. I want to find a supportive community, mentorship, and success stories of women in technology so that I can stay motivated and confident in my journey.**

Acceptance Criteria:

* Users can find and request mentors.
* A newsletter system is in place for motivation.
* Users can read success stories and submit their own.

Tasks:

* Implement a mentorship matching system.
* Add a Success Stories page featuring women who overcame challenges in tech.
* Allow users to submit their own success stories through a Django form.
* Create a weekly newsletter/email system to share inspirational content.
* Use Tailwind to design a motivating and visually appealing layout.



**5. As a woman who has been in the software development industry for over 20 years, I would like to encourage and support young girls and other women so they can become part of the tech industry.**

Acceptance Criteria:

* Experienced women can sign up as mentors and be matched with mentees.

Tasks:

* Implement a mentorship programme where experienced women can sign up as mentors.
* Use Tailwind to design a professional but welcoming interface for mentors.



**6. As an experienced coder, I want to mentor in the programming language I feel most confident in, so I can provide guidance and support to mentees in my area of expertise.**

Acceptance Criteria:

* Mentors can select one or more programming languages they specialise in.
* Mentees can filter mentors based on their preferred language.
* A mentee can request mentorship, and the mentor receives a notification.

Tasks:

* Allow mentors to select their preferred programming languages when signing up.
* Create a Django model for mentor profiles, including expertise fields.
* Implement a matching system where mentees can request mentorship based on language expertise.



### Design:

#### Colours/Fonts
Our team didn’t initially agree on a specific design for our website. A Windows 95-inspired look was suggested, with a grey navbar and footer, similar to the status bar in Windows 95, featuring a shadow box effect. However, things took their own course, and we ended up with a charming mix—something reminiscent of the wild west of 90s web design, when there were no strict rules. Early 2000s newspaper and university websites were also suggested as inspiration, and the homepage was designed based on one of these sites.

Fonts weren’t agreed upon either, so I’m just as curious about the final result as anyone else! The same goes for wireframes—although some sketches with design suggestions did appear by day two. 😊

* Colour palette
![Colour palette](static/assets/Images/HackHerSpace-palette-colour.png)

#### Wireframes

* Hompage Wireframe ![Hpmepage Wireframes](static/assets/wireframes/Homepage.png)

* Women in Tech Wireframe ![Women in Tech Wireframe](static/assets/wireframes/Woman%20in%20Tech%20page.png)

* Mentor Page Wireframe ![Mentor Page Wireframe](static/assets/wireframes/Mentor%20page.png)

* Q&A Wireframe ![Q&A Page Wireframe](static/assets/wireframes/Q&A%20page.png)


## ![favicon](static/assets/favicon/favicon-16x16.png) Agile Methodology

#### Kanban Board

The project's Kanban Board can be viewed [here](https://github.com/users/Joha-will/projects/10)


## ![favicon](static/assets/favicon/favicon-16x16.png) Features

#### Navbar

Each page features the same navbar, designed in a 90s-inspired style—grey with black text. The buttons in the navbar are centred, and there are seven links leading to different pages.

#### Footer

Every page also shares a minimalist footer, which contains only a simple copyright notice for a clean and consistent look.

#### Home

The homepage, also designed in a 90s-inspired style, is divided into three sections.

At the centre is the most important part, featuring a leading text explaining what HackHer Space is and its core principles. Below this, there's a 90s-era image of a woman drinking coffee in front of a computer.

On both sides, there are sidebars with links that lead nowhere—purely for aesthetic nostalgia.

#### About



#### Mentors

The Mentors page follows the same 90s-inspired style, featuring two sidebars.

In the central section, there are portraits of the available mentors, each accompanied by a short bio detailing their expertise and background.

#### Questions

The Q&A page is divided into two sections.

On the left side, there are five topics to choose from: Python, CSS, JavaScript, HTML, and Django. Clicking on a topic reveals a set of related questions.

On the right side, there is a form where users can select a topic (Python, JavaScript, etc.) and enter their question in a text area. Below, a "Submit Question" button allows users to send their queries.

#### History

The Women in Tech page showcases nine pioneering women selected by our team, ranging from Ada Lovelace and Frances Allen to our youngest heroine, Katie Bouman.

The profiles are arranged in a 3x3 grid, with each card featuring a portrait on a solid, colourful background. The original backgrounds were removed and replaced with warm tones to contrast with the grey 90s aesthetic.

When hovered over, each card reveals a quote from the featured woman. Below, a short bio highlights her contributions to technology.

#### Contact


## ![favicon](static/assets/favicon/favicon-16x16.png) Technologies Used

* HTML, CSS, Tailwind CSS, Python, JavaScript were used as the languages/frameworks.

* [Birme](https://www.birme.net/?image_format=webp&quality_webp=60) to resize, crop, compress and change the image format to WEBP.

* [Pixabay](https://pixabay.com/vectors/girl-laptop-type-typing-woman-158465/) to downland the images for the logo and favicon.

* [Favicon](https://favicon.io/) to create favicon.

* [GitHub](https://github.com/) to store the project, project board and collaboration.

* [Remove bg](https://www.remove.bg/) to remove the background and add a solid colour background for portrait photos.

* [Canva](https://www.canva.com/) was used to create logo, wireframes.

* [Coolors](https://coolors.co/) to make a colour palette

## ![favicon](static/assets/favicon/favicon-16x16.png) Code

## ![favicon](static/assets/favicon/favicon-16x16.png) Testing

### Bugs

### Unresolved Bugs

### Testing User Stories

### Manual Testing

### Accessibility

## ![favicon](static/assets/favicon/favicon-16x16.png) Deployment

This project was deployed on Heroku.

Deploying the Project on Heroku:





## ![favicon](static/assets/favicon/favicon-16x16.png) Maintenance & Updates

## ![favicon](static/assets/favicon/favicon-16x16.png) Credits

### Media

#### Images

* Images for the Women in Tech / History page.
All Images were sourced from [Wikimedia Commons](https://commons.wikimedia.org/). With the exception of three, all required attribution under their respective copyright licenses.

    * [Dr Fei-Fei Li](https://commons.wikimedia.org/wiki/File:Fei-Fei_Li_at_AI_for_Good_2017.jpg);
 Attribution: ITU Pictures, CC BY 2.0 <https://creativecommons.org/licenses/by/2.0>, via Wikimedia Commons

    * [Parisa Tabriz](https://commons.wikimedia.org/wiki/File:Parisa_Tabriz_Blackhat%2717_profile.jpg); Attribution:
mrisher, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons

    * [Katie Bouman](https://commons.wikimedia.org/wiki/File:Katie_Bouman_answers_questions_about_the_Event_Horizon_Telescope_project.jpg); Attribution:
Credit: NSF, Public domain, via Wikimedia Commons

    * [Timnit Gebru](https://commons.wikimedia.org/wiki/File:Timnit_Gebru_crop.jpg); Attribution:
https://commons.wikimedia.org/wiki/File:Timnit_Gebru_crop.jpg

    * [Radia Perlman](https://commons.wikimedia.org/wiki/File:Radia_Perlman_2009.jpg); Attribution:
Scientist-100 at English Wikipedia, Public domain, via Wikimedia Commons

    * [Frances Allen](https://commons.wikimedia.org/wiki/File:Allen_mg_2545-b.jpg); Attribution:
Rama, CC BY-SA 2.0 FR <https://creativecommons.org/licenses/by-sa/2.0/fr/deed.en>, via Wikimedia Commons

    * [Barbara Liskov](https://commons.wikimedia.org/wiki/File:Turing_Centenary_Celebration_Liskov.jpg); Attribution:
Dennis Hamilton from Seattle, Washington, USA, CC BY 2.0 <https://creativecommons.org/licenses/by/2.0>, via Wikimedia Commons

    * [Rana el Kaliouby](https://commons.wikimedia.org/wiki/File:Rana_El_Kaliouby.jpg); Cairue, CC BY-SA 4.0 <https://creativecommons.org/licenses/by-sa/4.0>, via Wikimedia Commons

    * [Ada Lovelace](https://commons.wikimedia.org/wiki/File:Ada_Lovelace_Chalon_portrait.jpg); Attribution:
Alfred Edward Chalon, Public domain, via Wikimedia Commons


* The illustration for the logo and the favicon was found on [Pixabay](https://pixabay.com/vectors/girl-laptop-type-typing-woman-158465/)


### Content

* [ChatGPT](https://openai.com/chatgpt/overview/) was used to review for spelling, grammar and consistency, and enhanced the content. Additionally, ChatGPT helped by providing information on the Women in Tech page.