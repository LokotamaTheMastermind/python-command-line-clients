def global_(answers):
    return not answers['folder_packages']


questions = [
    {
        'name': 'package_manager',
        'type': 'list',
        'message': 'Please select appropriate package manager',
        'choices': [
            # Package managers available
            {
                'name': 'Chocolatey'
            },
            {
                'name': 'Composer'
            },
            {
                'name': 'PIP'
            },
            {
                'name': 'NPM'
            },
            {
                'name': 'Yarn'
            }
        ]
    },
    {
        'name': 'folder_packages',
        'type': 'confirm',
        'message': 'Are the package available locally? (containerized)',
        'default': False,
    },
    {
        'name': 'global_packages',
        'type': 'confirm',
        'message': 'Are the package available globally?',
        'default': True,
        'when': global_,
    }
]
