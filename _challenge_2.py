# Create a Job Portal using Python 
def get_input(prompt):
    
    return input(prompt + ': ')

def get_education():
   
    while True:
        education = get_input('Education (1. High School, 2. Bachelor\'s, 3. Master\'s, 4. PhD)')
        if education in ['1', '2', '3', '4']:
            return education
        else:
            print('Invalid input, please enter 1, 2, 3, or 4')

def get_gender():
    
    while True:
        gender = get_input('Gender (1. Male, 2. Female, 3. Other)')
        if gender in ['1', '2', '3']:
            return gender
        else:
            print('Invalid input, please enter 1, 2, or 3')

def get_marital_status():
    
    while True:
        marital_status = get_input('Marital Status (1. Single, 2. Married, 3. Divorced, 4. Widowed)')
        if marital_status in ['1', '2', '3', '4']:
            return marital_status
        else:
            print('Invalid input, please enter 1, 2, 3, or 4')

def get_personal_info():
    
    print('---Personal Information---')
    first_name = get_input('First Name')
    middle_name = get_input('Middle Name')
    last_name = get_input('Last Name')
    email = get_input('Email')
    phone_number = get_input('Phone Number')
    education = get_education()
    gender = get_gender()
    age = get_input('Age')
    date_of_birth = get_input('Date of Birth')
    current_address = get_input('Current Address')
    permanent_address = get_input('Permanent Address')
    marital_status = get_marital_status()
    return {
        'first_name': first_name,
        'middle_name': middle_name,
        'last_name': last_name,
        'email': email,
        'phone_number': phone_number,
        'education': education,
        'gender': gender,
        'age': age,
        'date_of_birth': date_of_birth,
        'current_address': current_address,
        'permanent_address': permanent_address,
        'marital_status': marital_status,
    }

def submit_application():
    
    print('---Job Application---')
    personal_info = get_personal_info()
    declaration = get_input('I declare that the information provided is true and accurate (y/n)')
    if declaration.lower() == 'y':
        print('Thank you for submitting your job application!')
    else:
        print('Application not submitted. Please check the information provided.')


submit_application()