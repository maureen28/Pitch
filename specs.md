# The NEWS API Specification
<p>I have tried to make the specifications as easy to read and understand.</p>
<p>Last modified: <b>27/4/2020</b></p>
<p>Version : 3.6</p>

## TABLE OF CONTENTS
<ul>
<li>Introduction</li>
<li>System Overview</li>
<li>Usage</li>
<li>Future Directions and open Questions</li>
</ul>

<h2> 1. Introduction </h2><hr>
<ol type='A'>
<li><b> Scope</b></li>
<p>This is a News Web application that keeps track of the top headlines as well as lists and preview news articles from various sources.</p>
<p>It is entirely powered by the News Api.</p>
<p>This project covers fetching, filtering and displaying data </p>
<p>It's future scope is the ability to implement subscription and authentication. Users will be able to subscribe so they can get the latest news.</p>

<li><b> Goals</b></li>
<ul>
<li>Gives information on politics, business, health and entertainment</li>
<li>Easily accessible</li>
<li>Instant and latest news from all over the world</li>
<li>Pictures relvant to the articles</li>
<ul>

<li><b> Goals for implementation</b></li>
<pre>
<code>This app must be secure in all environments. We do this by using the SECRET_API_KEY to avoid explicity as well as forgery</code>
</pre>
</ol>

<h2> 2. System Overview </h2><hr>
<p>This app follows the following steps to ensure it outputs the latest news from different sources </p>
<ol>
<li><b> How the System Works</b></li>
<pre><code> 
<b>Fetching data:</b>
Periodically, the News app gets updates from The News Web API using the defined Base_URL and an API_KEY, with the use of a context manager, the data from the API gets read, then converted into json format and stored in an object.

<b>Processing data:</b>
The Json data then gets processed while applying a filter by the key value assigned to a variable
ie: Once we create an object we then instantiate it respective class.
<b>Displaying data:</b>
Processed data then get passed into the template(html), where it gets iterated through and displayed.
</code></pre>
</ul>
<h2> 3. Usage </h2><hr>
<ol type ='a'>
<li><b> Requirements</b></li>
<p>Fair or good Internet Connection.</p>
<p>You can choose to use the live link provided in the README. Click it and follow instructions given on readme.</p>
<p>The app should work fine but if it doesn't feel free to raise a compability issue </p>
</ol>
<pre>
<code>** Disclaimer **
The data contained is not filtered by contents, hence the news app won't be responsible for any rude or explicit wordings or images.
</code>
</pre>

<h2> 4. Future Directions and Open Questions </h2><hr>
<p>NOTE : this app has been designed and implemented using Flask. It also allows flexibility for different uses.</p>
<p>If you have any questions feel free to <a href ='nimz69509@gmail.com'>Email me</a>. Your suggestions are welcomed.</p>