# -*- coding: utf-8 -*-

def python_jumpstart(folder_location, project_name, framework, is_sub_folder, is_git_repository):
    from PyInquirer import prompt, Separator

    extra_questions = [
        {
            'type': 'list',
            'name': 'project_type',
            'message': 'Choose the right project type for what you want',
            'choices': [
                Separator("\n= Web Development Stuff ="),
                {
                    'name': 'Django'
                },
                {
                    'name': 'Flask'
                },
                {
                    'name': 'Bottle'
                },
                Separator("\n= Game Development ="),
                {
                    'name': 'Pygame --> Coming soon',
                    'disabled': True
                },
                Separator("\n= Web Scraping ="),
                {
                    'name': 'Beautiful Soup'
                },
                Separator("\n= Machine Learning ="),
                {
                    'name': 'Numpy --> Coming Soon',
                },
                Separator("\n= Command Line Interfaces ="),
                {
                    'name': 'PyInquirer & Clint with args'
                },
                {
                    'name': 'PyInquirer & Click with args'
                },
                {
                    'name': 'PyInquirer & Figlet with args'
                },
                "More are coming soon!"
            ]
        }
    ]
    answers = prompt(extra_questions)
