Build a Web or Social Network Search Engine


You must work in teams of 5 students.

Each project report must have a section called "Collaboration Details" where you should clearly specify the contributions of each member of the team.

You have a choice of building a search engine for the Web or for reddit.

Part A: Build a Web Crawler for html pages, or a reddit post collector

Web:

Your application should read a file of seed  URLs.

The application should also input the number of pages to crawl and the number of levels (hops (i.e. hyperlinks) away from the seed URLs).

Optionally, you can filter the domains that your crawler should access, e.g. .edu or .gov only.

All crawled pages (html files) should be stored in a folder.

Python-based Scrapy will be the default crawler used in the discussion sessions. You can use other languages or libraries, like Java jsoup, but support for these will be limited.

You will be graded on the correctness and efficiency of your crawler (e.g., how does it handle duplicate pages? Does it prune pages outside the target domain? Or is the crawler multi-threaded?).

reddit:

Use the reddit API (https://www.reddit.com/dev/api/) to collect posts from one or more subreddits of your choice. You may also add some filters on keywords or users and so on.

It is easier to use the PRAW Python library (https://praw.readthedocs.io/).

Store posts in large files of about 10 MB, one post per row.

If a post contains a URL to an html page, get title of that page, and add title as an additional field of the post, that is, include it in the JSON of the post, so it becomes searchable in Part B.

In both cases, you should collect at least 500 MB of raw data.

Deliverables:

1: Report (4-5 pages) in pdf that includes:

1. Collaboration Details: Description of contribution of each team member.

2. Overview of system, including (but not limited to)

 	a. Architecture.

 	b. The crawling or data collection strategy.

 	c. Data structures employed.

3. Limitations (if any) of system.

4. Instruction on how to deploy the system. Ideally, you should include a crawler.bat (Windows) or crawler.sh (Unix/Linux) executable file that takes as input all necessary parameters.

Example: [user@server]./crawler.sh <seed-File:seed.txt> <num-pages: 10000> <hops-away: 6> <output-dir>
Similarly for reddit.

5. Screenshots showing the system in action.

2: Zip file with your code

Turn in your report and zip file to Canvas by 5/5.

 

Part B: Build index and Web-based search interface

B.1: Build index using PyLucene: Index your data using PyLucene (or PyElasticSearch but not Solr) or an equivalent from your language of preference (ask for approval from instructor).

Web:

Write a program that uses the PyLucene libraries to index all the html files in the folder you created in Part A. Handle different fields like title, body, creation date (if available).

reddit:

Write a program that parses the JSON objects of your big files form Part A and inserts them into PyLucene. Index available fields like username, timestamp, body, and so on.

 B2. Create a Web-based interface

The interface should contain a textbox, and a search button. When you click search, you should see a list of results (e.g., first 10) returned by PyLucene for this query and their scores. The list should be ordered in decreasing order of score. Handle fields as you deem appropriate. For reddit, order by a combination of time and relevance; describe your ranking function.

We recommend Flask or Django for the Web app, but you are free to use your own Web-based programming language (at your own risk).

Extra credit:

Web: Display a snippet for each result. You can use ideas discussed in class or your own ideas to come up with a good snippet generation algorithm. Don't use PyLucene-generated snippets.

Alternatively, you can use PageRank to rank pages, that is, you can allow the user to either rank by PyLucene ranking or by PageRank.

reddit: Allow ordering posts by votes, time, relevance or a combination of them (weight for each of the three factors).

Alternatively, you can use PageRank to rank posts, that is, you can allow the user to either rank by PyLucene score or by PageRank.

Deliverables:

1. Collaboration Details: Description of contribution of each team member.

2. Overview of system, including (but not limited to):

     	a. Architecture

     	b. Index Structures

     	c. Search Algorithm

3. Limitations of system.

4. Instructions on how to deploy the system. Ideally, you should include an indexer.bat (Windows) or indexer.sh (Unix/Linux) executable file that takes as input all necessary parameters
Example: [user@server] ./indexer.sh <output-dir>

5. A web-application (e.g. Web Archive) that can be deployed to a webserver like Tomcat.

6. Screenshots showing the system in action.

Turn in your report and zip file to Canvas by 6/6. Further, each team will record a short (up to 5 min) video demo of their project, and include a link to it in their final report.