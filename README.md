# Barks in Bubbles - Dog Grooming Salon

## Goal & Target Audience

### Project Link

## User Experience (UX)

### Strategy
### User Experience
#### First Time User
#### Returning / Frequent User
#### Interested Parties
### User Stories

**Epic 1: Homepage Above Fold and Navigation**

***User Stories:***

- As a Site User, I can view information about the salon on the homepage so that I can understand the salon's mission and background.

- As a Site User, I can see a welcoming message and a catchy image when I first visit the homepage so that I feel engaged and have a positive first impression of the salon.

- As a Site User, I can easily navigate the website through a comprehensive menu located in the header and access site pages so that I can explore the site fully and access my account.

**Epic 2: Information About Services Offered: Services, Groomers & Gallery**

***User Stories:***

- As a Site User, I can view a list of services on the homepage so that I can quickly learn about the different grooming options available.

- As a Site User, I can view information about the groomers on the 'Our Groomers' page so that I can choose a groomer based on their expertise.

- As a Site User, I can view a gallery of photos on the 'Gallery' page featuring dogs in the process of being groomed or already groomed so that I can see the quality and range of grooming services offered.

**Epic 3: Contact Information and Inquiries**

***User Stories:***

- As a Site User, I can find contact details in the footer on any page of the site so that I can reach out to the salon for further inquiries, to book an appointment, or to know the salon's location and working hours.

- As a Site User, I can access and use the contact form on the 'Contact' page so that I can send inquiries directly to the salon.

- As a Site Owner, I can store contact form requests in the database so that I can review them, mark as read, or delete.

- As a Site Owner, I can mark contact form submission as "read" so that I can track how many I still need to process.

**Epic 4: Account Management**

***User Stories:***

- As a Site User, I can create an account through Log In bar so that I can access personalized services to book and store my appointments.

- As a Site User, I can log in using the Log In bar so that I can easily see and manage my existing bookings or log out.

**Epic 5: Appointment Booking and Management**

***User Stories:***

- As a Site User, I can see multiple entry points to make a booking so that I can easily book a service.

- As a Registered Customer, I can book an appointment so that I can groom my dog.

- As a Registered Customer, I can delete my existing booking so that I can remove an appointment I no longer need.

- As a Registered Customer, I can edit my booking appointment so that I can update or change the details of the appointment or the information I have provided.

- As a Site Owner, I can view and manage all existing bookings so that I can oversee the salon's schedule and make changes or cancel bookings when needed.



## Design

### Wireframes
### Site Structure
### Database Structute 
### Colour Scheme
### Typography

## Features

### Existing Features
### Future Features

## Technologies used

### Languages
### Frameworks
### Database

## Testing

### Manual Testing
#### Site features and behaviour
#### User Stories

### Validator Testing
### Responsinvess
### Lighthouse Testing
### Accessibility Testing

### Bugs

#### Solved Bugs
### Remaining Bugs

## Deployment

The Dog Grooming Salon 'Barks in Bubbles' website is hosted on Heroku, a container-based cloud platform designed for app development, deployment, and management. It was deployed following the steps below.

### Part 1: Create a New App

1. **Log into Heroku Account**

2. **Create a New App:**
   - Select 'New' in the top-right corner of the Heroku Dashboard.
   - Choose 'Create new app' from the dropdown menu.
   - Enter the app name 'barks-in-bubbles' and select Europe as the region.
   - Click 'Create App'.

3. **Access Settings and Configure Environment Variables:**
   - Go to the 'Settings' tab of the created app.
   - Click on 'Config Vars'.
   - Add the `DISABLE_COLLECTSTATIC` key with a value of `1`.
   - Click 'Add'.
   - Add the `CLOUDINARY_URL` key with a value in the following format: `cloudinary://<api_key>:<api_secret>@<cloud_name>`.
   - Click 'Add'.
   - Add the `DATABASE_URL` key with a value in the following format: `postgres://<username>:<password>@<host>:<port>/<dbname>`.
   - Click 'Add'.

### Part 2 - Update Code for Deployment

1. **Prepare Dependencies:**
   - In the workspace terminal, run the command to create a `requirements.txt` file with the project's dependencies for each project dependency, while working on the project:
     ```
     pip3 freeze --local > requirements.txt
     ```

2. **Install Gunicorn:**
   - Install the web server Gunicorn:
     ```
     pip3 install gunicorn~=20.1
     ```
   - Add Gunicorn to the project requirements:
     ```
     pip3 freeze --local > requirements.txt
     ```

3. **Create a Procfile:**
   - Create a `Procfile` at the root directory of the project.
   - Declare the process as `web` and add a start command:
     ```
     web: gunicorn codestar.wsgi
     ```

4. **Update Project settings.py File:**
   - Change `DEBUG` to `False`:
     ```
     DEBUG = False
     ```
   - Add `'.herokuapp.com'` to the `ALLOWED_HOSTS` in the project settings:
     ```
     ALLOWED_HOSTS = [
         '8000-katepaulaus-doggrooming-98d5mf21glf.ws.codeinstitute-ide.net',
         '.herokuapp.com'
     ]
     ```

5. **Push Updated Code to GitHub**

### Part 3 - Deployment with Static Files

To ensure the deployed app looks as nicely styled as the local development version, the project was deployed with static files using the WhiteNoise Python package by following the steps below:

1. **Install and Set Up the Python Package:**
   - Install WhiteNoise:
     ```
     pip3 install whitenoise~=5.3.0
     ```
   - Add WhiteNoise to the project requirements:
     ```
     pip3 freeze --local > requirements.txt
     ```
   - Integrate WhiteNoise into Django's `MIDDLEWARE` in the `groomingsalon/settings.py` file, ensuring it is placed right after the Django `SecurityMiddleware`:
     ```
     MIDDLEWARE = [
         'django.middleware.security.SecurityMiddleware',
         'whitenoise.middleware.WhiteNoiseMiddleware',
         # Other middleware...
     ]
     ```

2. **Create a Static Files Directory and Collect Static Files:**
   - Set the `STATIC_ROOT` path in the `groomingsalon/settings.py` file:
     ```
     STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
     ```
   - Run the `collectstatic` command in the terminal to gather static files into the `staticfiles` directory:
     ```
     python3 manage.py collectstatic
     ```

3. **Deployment:**
   - Check the Python version by running:
     ```
     python3 -V
     ```
   - From the [supported runtimes](https://devcenter.heroku.com/articles/python-support#specifying-a-python-version), copy the runtime closest to the current Python version.
   - Add a `runtime.txt` file to the project's root directory with the copied Python version: `python-3.12.4`.
   - Set `DEBUG` to `False` and push the changes to GitHub.
   - Open the Heroku dashboard, go to the app 'Settings' tab, and under 'Reveal config vars', remove the `DISABLE_COLLECTSTATIC` key/value pair.

### Part 4 - Set Up Deployment from GitHub

1. **Set Up Deployment from GitHub:**
   - In the Heroku dashboard switch to the 'Deploy' tab.
   - Choose 'GitHub' as the deployment method and connect the GitHub account.
   - In the search bar, type the repository name `dog-grooming-salon` and click 'Search' to find it on GitHub.
   - Click 'Connect' to link the Heroku app to the GitHub repository.

2. **Deploy the App:**
   - Click 'Deploy Branch' to manually deploy the app.
   - Wait for the app to build. Once ready, the message “Your app was successfully deployed” appears.

3. **View Deployed App:**
   - Click on the 'View' button to see the deployed project.

The deployed project link can be found at the following URL: [Dog Grooming Salon: Barks in Bubbles](https://barks-in-bubbles-a17d3839532d.herokuapp.com/).


## Credits

### Code Development

- To center the logo position in the header, the transform on the logo in the header was used: [SheCodes](https://www.shecodes.io/athena/121718-how-to-use-transform-translate-50-50-to-center-an-element-in-css121718-how-to-use-transform-translate-50-50-to-center-an-element-in-css).
- Visited state for the buttons in the header was set using instructions from [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/CSS/:visited).
- Buttons' background after the visited state was set following instructions from [Stack Overflow](https://stackoverflow.com/questions/28471219/issue-with-background-color-of-a-button-after-visited-state).
- Redirect to the Appointment booking page after a user is logged in was set using instructions from [Real Python](https://realpython.com/django-redirects/).
- The `get_context_data` method was used to include multiple models' data in a Django class-based view for the home page following instructions from [Django Documentation](https://docs.djangoproject.com/en/5.0/topics/class-based-views/generic-display/#adding-extra-context).
- To avoid 's' being appended at the end of the model name in the Django admin panel, the `Meta` class was added to the models following instructions from [Django Documentation](https://docs.djangoproject.com/en/5.0/ref/models/options/#verbose-name-plural).
- To set the choices argument for the appointment status field in the admin panel, the instructions from [ZeroToByte](https://zerotobyte.com/django-choices-best-practices/) were used.
- To set the date field with a calendar widget on the booking form, the instructions were used from [Python Assets](https://pythonassets.com/posts/date-field-with-calendar-widget-in-django-forms/).
- To specify how the time field should be handled within the booking form, the instructions were followed from [Django Documentation](https://docs.djangoproject.com/en/5.0/ref/forms/fields/).
- To prevent past date booking, the `clean` method was used for the date validation logic following the example here: [Stack Overflow](https://stackoverflow.com/questions/4941974/django-how-to-set-datefield-to-only-accept-today-future-dates).
- To store messages in the booking flow, the request object was used: [Sayari3](https://sayari3.com/articles/16-how-to-pass-user-object-to-django-form/).
- To convert the date into the day of the week and dynamically fetch the corresponding start and end times of a groomer, the following sources were used: [Programiz](https://www.programiz.com/python-programming/datetime/strftime) and [Stack Overflow](https://stackoverflow.com/questions/51905712/how-to-get-the-value-of-a-django-model-field-object).
- To store the selected service, groomer, and date in the session to be used in step two of the booking process, the following resources were used: [Django Tutorial On How To Create A Booking System For A Health Clinic](https://blog.devgenius.io/django-tutorial-on-how-to-create-a-booking-system-for-a-health-clinic-9b1920fc2b78) and Django Documentation: [Working with Forms](https://docs.djangoproject.com/en/5.0/topics/forms/) & [Form and Field Validation](https://docs.djangoproject.com/en/5.0/ref/forms/validation/).
- To retrieve the selected service, groomer, and date stored in the session, the `get_object_or_404` method was used following instructions from [GeeksforGeeks](https://www.geeksforgeeks.org/get_object_or_404-method-in-django-models/).

### Content & Design

- The text for the home page, services descriptions, and groomers' profiles was generated using [Chat GPT](https://chat.openai.com/).
- [Balsamiq Studios software](https://balsamiq.com/wireframes/) was used to create mockup wireframes for the current project.
- To select the fonts for the site, a font pairing service was used: [Font Joy](https://fontjoy.com/).
- Paired font families were downloaded from [Google Fonts](https://fonts.google.com/).
- The color palette for the site was extracted from the logo using [Coolors](https://coolors.co/).
- Site colors' accessibility was checked using [Adobe Color Accessibility Tool](https://color.adobe.com/).

### Media

- The logo was created using [DALL-E](https://openai.com/index/dall-e/) based on the desired outcome description provided.
- Grooming services and gallery images were sourced from [Freepik](https://www.freepik.com/).
- Groomers' profile images were sourced from [Unsplash](https://unsplash.com/).
- The hero image was sourced from [Vecteezy](https://www.vecteezy.com/).
- Social media icons displayed in the footer were taken from [Iconify](https://iconify.design).

