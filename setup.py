from setuptools import find_packages, setup


with open("README.md", "r", encoding="utf-8") as handle:
    long_description = handle.read()


setup(
    name="mbe-eval",
    version="0.2.0",
    author="Aparajeet Shadangi",
    author_email="aparajeet.shadangi@proton.me",
    description="Marginal Baseline Evaluation for auditing generalization metrics.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AparajeetS/metric-audit-paper-code",
    project_urls={
        "Source": "https://github.com/AparajeetS/metric-audit-paper-code",
        "Issues": "https://github.com/AparajeetS/metric-audit-paper-code/issues",
    },
    packages=find_packages(exclude=["experiments*", "examples*", "docs*", "tests*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    license="MIT",
    python_requires=">=3.9",
    install_requires=[
        "numpy>=1.24",
        "pandas>=2.0",
        "scipy>=1.10",
    ],
    extras_require={
        "torch": ["torch>=2.0", "torchvision>=0.15"],
        "plot": ["matplotlib>=3.7", "seaborn>=0.12"],
        "examples": ["torch>=2.0", "torchvision>=0.15", "scikit-learn>=1.3"],
        "dev": ["pytest>=7", "build>=1.0", "twine>=4"],
    },
)
