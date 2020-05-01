# PITCH

## Description
Pitch is a Flask application that allows users an opportunity to say something meaningful if the user was given only one minute in life to say something.The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.
## Author : Maureen Wairimu

### Brief Webpage Overview.
<ul>
<li>Below is the landing page once the web browser is loaded</li>
<img src="/Screenshot from 2020-04-28 09-36-51.jpg" alt="Pitch landing page" width="1000"/>

## Setup Instructions
<ol>
<li>Clone or download the repository <code>https://github.com/maureen28/Pitch.git</code> </li>
<li>Create a virtual environment
<pre>
<code>
pip install virtualenv
source virtual/bin/activate
</code></pre>
</li>
<li>Install all the requirements <code>pip install -r requirements.txt</code></li>
<li>Add variables  <code> export DATABASE_URL='postgresql+psycopg2://name:password@localhost/pitching'
</code></li>
<li>Run <code>./start.sh</code></li>
<li>Run test at <code>python3 manage,py test</code></li>
</ol>

### Live link :

## Technology & Dependency
<ol>
<li>python3.6</li>
<li>Pip & pyperclip</li>
<li>CSS(Bootstrap)</li>
<li>Flask Framework</li>
<li>PostgreSQL</li>
</ol>

## BDD
<table>
<tr>
<th>Behaviour</th>
<th>Input</th>
<th>Output</th>
</tr>
<tr>
<td>Display articles from a news source</td>
<td><strong>Click a news source</strong></td>
<td>Redirected to a page with a list of articles from the source</td>
</tr>
<tr>
<td>Display news sources</td>
<td><strong>On page load</strong></td>
<td>List of various news sources is displayed per category</td>
</tr>
<tr>
<td>Display the preview of an article</td>
<td><strong>On page load</strong></td>
<td>Each article displays an image, title, description and publication date</td>
</tr>
</table>

### Known Bugs
If you find a bug please feel free to alert me.
To fix the bug:
<ul list-style-type=circle;>
<li>Fork the repository</li>
<li>Create a new branch(git branch my-contribution)</li>
<li>Make the changes, then (git add) to add changes</li>
<li>Commit the changes you have made(git commit -m"Fix bug") </li>
<li>Push changes made and click pull request so that I can access the changes made.</li>
</ul>

## Contact Information

To get in touch E-MAIL me on nimz69509@gmail.com

## License

MIT License
<b>Copyright (c) 2020 maureen28<b>
