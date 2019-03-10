import unicodecsv
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime as dt
from collections import defaultdict

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

# Takes a date as a string, and returns a Python datetime object.
# If there is no date given, returns None
def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')


# Takes a string which is either an empty string or represents an integer,
# and returns an int or None.
def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

def get_unique_students(data):
    unique_students = set()
    for data_point in data:
        unique_students.add(data_point['account_key'])
    return unique_students

# Given some data with an account_key field, removes any records corresponding to Udacity test accounts
def remove_udacity_accounts(data):
    non_udacity_data = []
    for data_point in data:
        if data_point['account_key'] not in udacity_test_accounts:
            non_udacity_data.append(data_point)
    return non_udacity_data

# Takes a student's join date and the date of a specific engagement record,
# and returns True if that engagement record happened within one week
# of the student joining.
def within_one_week(join_date, engagement_date):
    time_delta = engagement_date - join_date
    return time_delta.days >= 0 and time_delta.days < 7

def remove_free_trial_cancels(data):
    new_data = []
    for data_point in data:
        if data_point['account_key'] in paid_students:
            new_data.append(data_point)
    return new_data

def group_data(data, key_name):
    grouped_data = defaultdict(list)
    for data_point in data:
        key = data_point[key_name]
        grouped_data[key].append(data_point)
    return grouped_data

def sum_grouped_items(grouped_data, field_name):
    summed_data = {}
    for key, data_points in grouped_data.items():
        total = 0
        for data_point in data_points:
            total += data_point[field_name]
        summed_data[key] = total
    return summed_data

def describe_data(data):
    print 'Mean:', np.around(np.mean(data), decimals=2)
    print 'Standard deviation:', np.around(np.std(data), decimals=2)
    print 'Minimum:', np.around(np.min(data), decimals=2)
    print 'Maximum:', np.around(np.max(data), decimals=2)

def describe_data_hist(data, title, xlabel, ylabel):
    print 'Mean:', np.mean(data)
    print 'Standard deviation:', np.std(data)
    print 'Minimum:', np.min(data)
    print 'Maximum:', np.max(data)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.hist(data, bins=10)
    plt.show()

print('')
print('########################')
print('Exercicio 1')
print('########################')
#####################################
## Read in the data from daily_engagement.csv and project_submissions.csv
## and store the results in the below variables.
## Then look at the first row of each table.
#####################################
enrollments = read_csv('enrollments.csv')
daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')

print(enrollments[0])
print(daily_engagement[0])
print(project_submissions[0])

print('\n########################\n')

# Clean up the data types in the enrollments table
for enrollment in enrollments:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
    enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
    enrollment['join_date'] = parse_date(enrollment['join_date'])

# Clean up the data types in the engagement table
for engagement_record in daily_engagement:
    engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
    engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
    engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
    engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
    engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])

# Clean up the data types in the submissions table
for submission in project_submissions:
    submission['completion_date'] = parse_date(submission['completion_date'])
    submission['creation_date'] = parse_date(submission['creation_date'])

print(enrollments[0])
print(daily_engagement[0])
print(project_submissions[0])

print('')
print('########################')
print('Exercicio 2')
print('########################')
## Find the total number of rows and the number of unique students (account keys)
## in each table.

lista_enrollment = set()
lista_daily_engagement = set()
lista_project_submissions = set()

for enrollment in enrollments:
    lista_enrollment.add(enrollment['account_key'])

for engagement in daily_engagement:
    lista_daily_engagement.add(engagement['acct'])

for submission in project_submissions:
    lista_project_submissions.add(submission['account_key'])

total_enrollments = len(enrollments)
enrollments_unique = len(set(lista_enrollment))

total_daily_engagement = len(daily_engagement)
engagements_unique = len(set(lista_daily_engagement))

total_project_submissions = len(project_submissions)
submissions_unique = len(set(lista_project_submissions))

print('total_enrollments: {}'.format(total_enrollments))
print('enrollments_unique: {}'.format(enrollments_unique))

print('total_daily_engagement: {}'.format(total_daily_engagement))
print('engagements_unique: {}'.format(engagements_unique))

print('total_project_submissions: {}'.format(total_project_submissions))
print('submissions_unique: {}'.format(submissions_unique))

print('\n########################\n')

# total_enrollments: 1640
# enrollments_unique: 1302
# total_daily_engagement: 136240
# engagements_unique: 1237
# total_project_submissions: 3642
# submissions_unique: 743

print('')
print('########################')
print('Exercicio 3')
print('########################')
# Rename the "acct" column in the daily_engagement table to "account_key".
for engagement_record in daily_engagement:
    if 'acct' in engagement_record:
        engagement_record['account_key'] = engagement_record['acct']
        del[engagement_record['acct']]

print('daily_engagement[0][account_key]:', daily_engagement[0]['account_key'])

print('\n########################\n')

total_enrollments = len(enrollments)
enrollments_unique = len(get_unique_students(enrollments))

total_daily_engagement = len(daily_engagement)
unique_engagement_students = get_unique_students(daily_engagement)
engagements_unique = len(get_unique_students(daily_engagement))

total_project_submissions = len(project_submissions)
submissions_unique = len(get_unique_students(project_submissions))

print('total_enrollments: {}'.format(total_enrollments))
print('enrollments_unique: {}'.format(enrollments_unique))

print('total_daily_engagement: {}'.format(total_daily_engagement))
print('engagements_unique: {}'.format(engagements_unique))

print('total_project_submissions: {}'.format(total_project_submissions))
print('submissions_unique: {}'.format(submissions_unique))

print('')
print('########################')
print('Exercicio 4')
print('########################')
## Find any one student enrollments where the student is missing from the daily engagement table.
## Output that enrollment.
for enrollment in enrollments:
    student = enrollment['account_key']
    if student not in unique_engagement_students:
        print(enrollment)
        break


print('')
print('########################')
print('Exercicio 5')
print('########################')
## Find the number of surprising data points (enrollments missing from
## the engagement table) that remain, if any.
num_problem_students = 0
for enrollment in enrollments:
    student = enrollment['account_key']
    if (student not in unique_engagement_students):
        print(enrollment)
        num_problem_students += 1

print('num_problem_students: {}' . format(num_problem_students))

## Find the number of surprising data points (enrollments missing from
## the engagement table) that remain, if any.
num_problem_students = 0
for enrollment in enrollments:
    student = enrollment['account_key']
    if (student not in unique_engagement_students and enrollment['join_date'] != enrollment['cancel_date']):
        print(enrollment)
        num_problem_students += 1

print('num_problem_students: {}' . format(num_problem_students))

print('\n########################\n')

# Create a set of the account keys for all Udacity test accounts
udacity_test_accounts = set()
for enrollment in enrollments:
    if enrollment['is_udacity']:
        udacity_test_accounts.add(enrollment['account_key'])

print('udacity_test_accounts: {}' . format(len(udacity_test_accounts)))

print('\n########################\n')

# Remove Udacity test accounts from all three tables
non_udacity_enrollments = remove_udacity_accounts(enrollments)
non_udacity_engagement = remove_udacity_accounts(daily_engagement)
non_udacity_submissions = remove_udacity_accounts(project_submissions)

print('non_udacity_enrollments: {}' . format(len(non_udacity_enrollments)))
print('non_udacity_engagement: {}' . format(len(non_udacity_engagement)))
print('non_udacity_submissions: {}' . format(len(non_udacity_submissions)))

print('')
print('########################')
print('Exercicio 6')
print('########################')
## Create a dictionary named paid_students containing all students who either
## haven't canceled yet or who remained enrolled for more than 7 days. The keys
## should be account keys, and the values should be the date the student enrolled.
paid_students = {}
for enrollment in non_udacity_enrollments:
    if (not enrollment['is_canceled'] or enrollment['days_to_cancel'] > 7):
        account_key = enrollment['account_key']
        enrollment_date = enrollment['join_date']
        if (account_key not in paid_students or enrollment_date > paid_students[account_key]):
            paid_students[account_key] = enrollment_date

print('paid_students: {}' . format(len(paid_students)))

print('')
print('########################')
print('Exercicio 7')
print('########################')
## Create a list of rows from the engagement table including only rows where
## the student is one of the paid students you just found, and the date is within
## one week of the student's join date.
paid_enrollments = remove_free_trial_cancels(non_udacity_enrollments)
paid_engagement = remove_free_trial_cancels(non_udacity_engagement)
paid_submissions = remove_free_trial_cancels(non_udacity_submissions)

print('paid_enrollments: {}' . format(len(paid_enrollments)))
print('paid_engagement: {}' . format(len(paid_engagement)))
print('paid_submissions: {}' . format(len(paid_submissions)))

for engagement_record in paid_engagement:
    if engagement_record['num_courses_visited'] > 0:
        engagement_record['has_visited'] = 1
    else:
        engagement_record['has_visited'] = 0

paid_engagement_in_first_week = []
for engagement_record in paid_engagement:
    account_key = engagement_record['account_key']
    join_date = paid_students[account_key]
    engagement_record_date = engagement_record['utc_date']

    if within_one_week(join_date, engagement_record_date):
        paid_engagement_in_first_week.append(engagement_record)

print('paid_engagement_in_first_week: {}' . format(len(paid_engagement_in_first_week)))

print('\n########################\n')

# Create a dictionary of engagement grouped by student.
# The keys are account keys, and the values are lists of engagement records.
engagement_by_account = defaultdict(list)
for engagement_record in paid_engagement_in_first_week:
    account_key = engagement_record['account_key']
    engagement_by_account[account_key].append(engagement_record)

# Create a dictionary with the total minutes each student spent in the classroom during the first week.
# The keys are account keys, and the values are numbers (total minutes)
total_minutes_by_account = {}
for account_key, engagement_for_student in engagement_by_account.items():
    total_minutes = 0
    for engagement_record in engagement_for_student:
        total_minutes += engagement_record['total_minutes_visited']
    total_minutes_by_account[account_key] = total_minutes

# Summarize the data about minutes spent in the classroom
total_minutes = total_minutes_by_account.values()
print('Mean: {}' . format(np.mean(total_minutes)))
print('Standard deviation: {}' . format(np.std(total_minutes)))
print('Minimum: {}' . format(np.min(total_minutes)))
print('Maximum: {}' . format(np.max(total_minutes)))

print('')
print('########################')
print('Exercicio 8')
print('########################')
## Go through a similar process as before to see if there is a problem.
## Locate at least one surprising piece of data, output it, and take a look at it.

student_with_max_minutes = None
max_minutes = 0

for student, total_minutes in total_minutes_by_account.items():
    if total_minutes > max_minutes:
        max_minutes = total_minutes
        student_with_max_minutes = student

print('max_minutes: {}' . format(max_minutes))

for engagement_record in paid_engagement_in_first_week:
    if engagement_record['account_key'] == student_with_max_minutes:
        print('engagement_record: {}' . format(engagement_record))


print('')
print('########################')
print('Exercicio 9')
print('########################')
## Adapt the code above to find the mean, standard deviation, minimum, and maximum for
## the number of lessons completed by each student during the first week. Try creating
## one or more functions to re-use the code above.

engagement_by_account = group_data(paid_engagement_in_first_week, 'account_key')
print('engagement_by_account: {}' . format(engagement_by_account))

total_minutes_by_account = sum_grouped_items(engagement_by_account, 'total_minutes_visited')
print('total_minutes_by_account: {}' . format(total_minutes_by_account))

describe_data(total_minutes_by_account.values())

lessons_completed_by_account = sum_grouped_items(engagement_by_account, 'lessons_completed')
describe_data(lessons_completed_by_account.values())

print('')
print('########################')
print('Exercicio 10')
print('########################')
## Find the mean, standard deviation, minimum, and maximum for the number of
## days each student visits the classroom during the first week.
engagement_by_account = group_data(paid_engagement_in_first_week, 'account_key')
print('engagement_by_account: {}' . format(engagement_by_account))

days_visited_by_account = sum_grouped_items(engagement_by_account, 'has_visited')
describe_data(days_visited_by_account.values())

print('')
print('########################')
print('Exercicio 11')
print('########################')
## Create two lists of engagement data for paid students in the first week.
## The first list should contain data for students who eventually pass the
## subway project, and the second list should contain data for students
## who do not.

subway_project_lesson_keys = ['746169184', '3176718735']

pass_subway_project = set()

for submission in paid_submissions:
    project = submission['lesson_key']
    rating = submission['assigned_rating']

    if ((project in subway_project_lesson_keys) and \
            (rating == 'PASSED' or rating == 'DISTINCTION')):
        pass_subway_project.add(submission['account_key'])

print('len(pass_subway_project): {}' . format(len(pass_subway_project)))

passing_engagement = []
non_passing_engagement = []

for engagement_record in paid_engagement_in_first_week:
    if engagement_record['account_key'] in pass_subway_project:
        passing_engagement.append(engagement_record)
    else:
        non_passing_engagement.append(engagement_record)

print('len(passing_engagement): {}' . format(len(passing_engagement)))
print('len(non_passing_engagement): {}' . format(len(non_passing_engagement)))

print('')
print('########################')
print('Exercicio 12')
print('########################')
## Compute some metrics you're interested in and see how they differ for
## students who pass the subway project vs. students who don't. A good
## starting point would be the metrics we looked at earlier (minutes spent
## in the classroom, lessons completed, and days visited)

passing_engagement_by_account = group_data(passing_engagement, 'account_key')
non_passing_engagement_by_account = group_data(non_passing_engagement, 'account_key')

print 'minutes spent - non-passing students:'
non_passing_minutes = sum_grouped_items(non_passing_engagement_by_account, 'total_minutes_visited')
describe_data(non_passing_minutes.values())

print('')

print 'minutes spent - passing students:'
passing_minutes = sum_grouped_items(passing_engagement_by_account, 'total_minutes_visited')
describe_data(passing_minutes.values())

print('##')

print 'lessons completed - non-passing students:'
non_passing_lessons = sum_grouped_items(non_passing_engagement_by_account, 'lessons_completed')
describe_data(non_passing_lessons.values())

print('')

print 'lessons completed - passing students:'
passing_lessons = sum_grouped_items(passing_engagement_by_account, 'lessons_completed')
describe_data(passing_lessons.values())

print('##')

print 'days visited - non-passing students:'
non_passing_visits = sum_grouped_items( non_passing_engagement_by_account, 'has_visited')
describe_data(non_passing_visits.values())

print('')

print 'days visited - passing students:'
passing_visits = sum_grouped_items(passing_engagement_by_account, 'has_visited')
describe_data(passing_visits.values())

print('')
print('########################')
print('Exercicio 13')
print('########################')
## Make histograms of the three metrics we looked at earlier for both
## students who passed the subway project and students who didn't. You
## might also want to make histograms of any other metrics you examined.
print 'non-passing students - minutes spent:'
describe_data_hist(non_passing_minutes.values(), 'non-passing students - minutes spent', 'number of minutes', 'number of students')

print('')

print 'passing students - minutes spent:'
describe_data_hist(passing_minutes.values(), 'passing students - minutes spent', 'number of minutes', 'number of students')

print('##')

print 'non-passing students - lessons completed:'
describe_data_hist(non_passing_lessons.values(), 'non-passing students - lessons completed', 'number of lessons', 'number of students')

print('')

print 'passing students - lessons completed:'
describe_data_hist(passing_lessons.values(), 'passing students - lessons completed', 'number of lesons', 'number of students')

print('##')

print 'non-passing students - days visited:'
describe_data_hist(non_passing_visits.values(), 'non-passing students - days visited', 'number of days', 'number of students')

print('')

print 'passing students - days visited:'
describe_data_hist(passing_visits.values(), 'passing students - days visited', 'number of days', 'number of students')

print('\n########################\n')
