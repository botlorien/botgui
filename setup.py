from setuptools import setup, find_packages


setup(
    name="botgui",
    version="0.1.0",
    description='Class to build custom UI for bot processes',
    author='Ben-Hur P. B. Santos',
    author_email='botlorien@gmail.com',
    long_description=open("README.md", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/botlorien/botgui",  # Link para o repositório
    packages=find_packages(),  # Especifica que os pacotes estão na pasta src
    #  package_dir={"": "src"},  # Configura o diretório-base como src
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',  # Versão mínima do Python
    install_requires=[
        'customtkinter',
        'pillow',
        'tkcalendar',
        'python-dotenv',
        'cryptography'
        ],
    )
# pip install setuptools
# python setup.py sdist
# pip install twine
# twine upload dist/*