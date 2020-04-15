#! /bin/bash
touch "./README.md"
cp progressbar.py ./ai42/
cp log.py .ai42/logging/
echo "import setuptools

with open(\"README.md\", \"r\") as fh:
    long_description = fh.read()

setuptools.setup(
    name=\"ai42\",
    version=\"1.0.0\",
    author=\"David Rodriguez\",
    author_email=\"darodrig@student.42madrid.com\",
    description=\"A small example package\",
    long_description=long_description,
    long_description_content_type=\"text/markdown\",
    url=\"https://github.com/d-r-e/bootcamp_python/tree/master/day02/ex04\",
    packages=setuptools.find_packages(),
    classifiers=[
        \"Programming Language :: Python :: 3\",
        \"License :: OSI Approved :: MIT License\",
        \"Operating System :: Linux\",
    ],
    python_requires='>=3.6',
)" > setup.py

echo "MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE." > LICENSE
python3 -m pip install --user --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel
