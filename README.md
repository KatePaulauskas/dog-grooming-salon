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

