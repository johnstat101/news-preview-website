# [News Preview Website](https://news-preview-website.herokuapp.com/)

## By John Kimani

## Description

News Preview Website is a web appliction that displays a list of news sources from various sources. A user is able to peruse over various news sources and view all articles under it.

User Story:

* See various news sources and select the ones they prefer.
* See all news sources from the source they selected.
* See Image description and time the news article was created.
* Click on an article and read it fully from the news source

### Prerequisites

You need the following to start working on the project on your local computer:

* A computer running on either Windows, MacOS or Ubuntu operating system installed with the following:

```
-Python version 3.9
-Flask
-Pip
-virtualenv
-A text  Editor
```

## Getting Started

* Clone this repository to your local computer.
* Ensure you have python3.6 installed in your computer.
* From the terminal navigate to the cloned project folder.
* Create a virtual environment and access the folder via your virtual amchine.
* Visit https://newsapi.org/ and register for an API key.
* Create start.sh file and in it write the following lines:
```
 export NEWS_API_KEY='<Your-Api-Key>'
 python3.9 manage.py server
```
* Run ```chmod +x start.sh``` follwoed by ``` ./start.sh ``` while in the project folder to start the project.
* Once started, the project can be accessed on your localhost using the address: ``` localhost:5000 ```.
* Alternatively the application can be accessed by visiting https://news-preview-website.herokuapp.com/

## Technologies Used

* Python v3.9
* Boostrap
* Flask

## License

MIT License

Copyright (c) 2022 John Kimani

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. Copyright (c) 2018 Peter Polle

