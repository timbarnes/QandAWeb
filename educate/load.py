#!/usr/bin/python -tt

# Access a tab-delimited file of topic, question, answer tuples
# Save the objects into the dj/educate database

import sys

import django
from xlrd import open_workbook
from models import Subject, Category, Question


def read_topics(filename):
    """Capture the list of topics in the file
    """
    topics = set()
    with open_workbook(filename) as book:
        sheet = book.sheet_by_index(0)
        for row_index in range(sheet.nrows):
            row_data = sheet.row(row_index)
            topics.add(row_data[0].value)
        return sorted(topics)


def save_topics(subject, topic_set):
    """Create an entry for each element from the set of topics provided.
       Because topic_set is a set(), there will be no duplicates.
    """
    sub = Subject.objects.filter(name=subject)
    if sub:
        sub = sub[0]
        categories = Category.objects.all()
        category_names = [cat.name for cat in categories]
        for entry in topic_set:
            if entry not in category_names:
                cat = Category(name=entry, subject=sub)
                cat.save()
    else:
        print('Subject not found:', sub)
    return


def read_questions(filename):
    """Read the questions using the xlrd processor.
        Lines are organized into lists of topic, question and answer.
    """
    with open_workbook(filename) as book:
        sheet = book.sheet_by_index(0)
        qlist = []
        for row_index in range(sheet.nrows):
            row_data = sheet.row(row_index)
            list.append(qlist, [x.value for x in row_data])
        return qlist


def save_questions(questions):
    """Iteratively write questions to the database.
    """
    for q in questions:
        cat = Category.objects.filter(name=q[0])
        if cat:
            qu = Question(category=cat[0],
                          question=q[1],
                          answer=q[2])
            qu.save()
        else:
            print("Please load categories first.")


def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [-c subject] file ')
        sys.exit(1)

    questions = []
    if args[0] == '-c':
        topics = list_topics(args[2])
        if topics:
            save_topics(args[1], topics)
        else:
            print(args[2], ': No topics found.')
    else:
        questions = read_questions(args[0])

    if len(questions) > 0:
        save_questions(questions)
    else:
        print("No questions found.")


if __name__ == '__main__':
    main()
