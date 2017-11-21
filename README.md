# What is Happening Today?

Hackathon ([Python Hackathon Engeto + Kiwi.com](https://www.facebook.com/events/1838098403073558))
attempt to analyse Slovak news sites to get hottest current articles and keywords.

## Why?

Because we are programmers, we are lazy and we want our programs to work for us.

## How?

By using simple analysis of suitable RSS feeds. We parse titles, perexes and keywords,
remove uninteresting stuff (stopwords) and make a bit of mumbo-jumbo with counting
occurrences and source cross-posting.

What's worth to mention:

* It took super-long to run the script, so parser runs in threads
* We managed to keep nice object abstraction considering hackathon limited time setting
* Slack integration included

_disclaimer: none of us had any substantial Python or Data Science experience
at the point of writing this code_

## Example

See it in action:

![](http://res.cloudinary.com/m1n0/image/upload/v1511222339/wht_leqq0m.gif)


## Authors:

* David Lukac [https://github.com/davidlukac](https://github.com/davidlukac)
* Milan Lukac [https://github.com/m1n0](https://github.com/m1n0)
* Peter Nagy [https://github.com/petonagy](https://github.com/petonagy)
