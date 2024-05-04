from setuptools import setup, find_packages

setup(
    name='misbehavin',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Add any other dependencies here
    ],
    author='Misbehavin crew',
    author_email='people@exmaple.com',
    description='A package for ragtime fun with web interactions',
    long_description='A package for ragtime fun with web interactions using AI agents',
    long_description_content_type='text/markdown',
    url='https://github.com/bitfot/misbehavin',
    classifiers=[
    ],
    entry_points={
        'console_scripts': [
            'misbehavin_planner = misbehavin.chat_agent.planner:main',
            'misbehavin_chatter = misbehavin.chat_agent.chatter:main'
        ]
    }
)
