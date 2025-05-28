from setuptools import setup, find_packages

setup(
    name="job-hunting-assistant",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "langchain-core",
        "langchain-community",
        "langchain-openai",
        "langchain-qdrant",
        "python-docx",
        "qdrant-client",
        "openai",
        "python-dotenv",
        "nltk",
        "unstructured",
        "unstructured[local-inference]",
        "pypdf",
        "pdf2image",
        "pytesseract",
    ],
) 