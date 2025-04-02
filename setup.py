from setuptools import setup, find_packages

setup(
    name="newsletter-generator",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "crewai",
        "langchain",
        "openai",
        "python-dotenv",
    ],
    author="Seu Nome",
    author_email="seu.email@exemplo.com",
    description="Um gerador de newsletter usando Crew AI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/seu-usuario/newsletter-generator",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)