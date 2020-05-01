# PITCH

## Description
Pitch is a Flask application that allows users an opportunity to say something meaningful if the user was given only one minute in life to say something.The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.
## Author : Maureen Wairimu

### Brief Webpage Overview.
<ul>
<li>Below is the landing page once the web browser is loaded</li>
<img src="/Screenshot from 2020-04-28 09-36-51.jpg" alt="Pitch landing page" width="1000"/>
</ul>

### Live link :

## User Story
<ul>
<li>Users can  see the pitches other people have posted.</li>
<li>Users can vote on the pitch they liked and give it a downvote or upvote.</li>
<li>Users can view the pitches they've  created in their profile page</li>
<li>Users can comment on the different pitches and leave feedback.</li>
<li>Users can submit a pitch in any category.</li>
<li>Users can view the different categories.</li>
<li>Users can sign in for them to leave a comment</li>
</ul>

## Setup Instructions
<ol>
<li>Clone or download the repository <code> https://github.com/maureen28/Pitch.git</code> </li>
<li>Create a virtual environment
<pre>
<code>
pip install virtualenv
source virtual/bin/activate
</code></pre>
</li>
<li>Install all the requirements <code> pip install -r requirements.txt</code></li>
<li>Add variables  <code> export DATABASE_URL='postgresql+psycopg2://name:password@localhost/pitching'
</code></li>
<li>Run <code>./start.sh</code></li>
<li>Run test at <code>python3 manage.py test</code></li>
</ol>

## Technology & Dependency
<ol>
<li>python3.6</li>0
<li>Pip & pyperclip</li>
<li>CSS(Bootstrap)</li>
<li>Flask Framework</li>
<li>PostgreSQL</li>
</ol>

## Behavior Driven Deveopment
<table>
<tr>
<th>Behaviour</th>
<th>Input</th>
<th>Output</th>
</tr>
<tr>
<td><strong>User login</strong></td>
<td>User enters email address and password</td>
<td>User is logged into the system</td>
</tr>
<tr>
<td><strong>Register as a new user</strong></td>
<td>A form containing username, email, password and confirm password </td>
<td>User is registered</td>
</tr>
<tr>
<td><strong>Adds a new pitch</strong></td>
<td>A form containing input fields for heading, pitch text and comment</td>
<td>New pitch is added.</td>
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
