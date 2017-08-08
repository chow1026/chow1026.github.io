<!--
.. title: D3 Building Blocks
.. slug: 02-d3_building_blocks
.. date: 2017-04-22 14:33:29 UTC+08:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->


### 1. D3 Version Notice

There's a new version of D3!
A new version of D3.js (version 4.0) was released on June 28th, 2016. This version changed the names of many of the functions in the library. From the release notes:

... one unavoidable consequence of adopting ES6 modules: every symbol in D3 4.0 now shares a flat namespace rather than the nested one of D3 3.x. For example, d3.scale.linear is now d3.scaleLinear, and d3.layout.treemap is now d3.treemap.
This means that the D3 code we have in this material will not work with version 4 of D3.js. We're working on updating the code, but for now, please keep this in mind as you are working through the course. Feel free to use either version 3 or version 4 for the final project.

### 2. Technical Interlude

Scott Murray provides an excellent overview of these fundamentals on his website, [alignedleft.com][3559901f]. (time estimate: 10 minutes)

  [3559901f]: http://alignedleft.com/tutorials/d3/fundamentals "Scott Murray's Aligned Left"

To learn the basics of HTML, CSS, and Javascript, we encourage you to work through Project 1 and Project 2 at https://dash.generalassemb.ly/. (time estimate: 10-20 hours)

Scott Murray also provides an excellent [tutorial of creating a visualization using D3.js][ee52dc79] if you'd like to get a preview of what's to come in later lessons. (time estimate: 10-15 hours)

  [ee52dc79]: http://alignedleft.com/tutorials/d3 "Scott Murray's D3 Tutorial"

If you have more time or want to get more comfortable with HTML and CSS prior to continuing in this course, consider taking our [Intro to HTML and CSS][1445459c]d course. (time estimate: 18+ hours)

  [1445459c]: https://www.udacity.com/course/ud304 "Udacity's Intro to HTML and CSS course"


### 3.





### 28. Server Requests And D3   

A simple [overview of requests and responses][2f6a9338] from Scott Murray's Interactive Data Visualization for the Web. Be sure to scroll to the top of the page to the section titled The Web.

  [2f6a9338]: http://chimera.labs.oreilly.com/books/1230000000345/ch03.html#_the_web "Overview of Requests and Responses"

More [detail on requests and javascript][f0688501].

  [f0688501]: http://eloquentjavascript.net/17_http.html "Javascript Requests"

@5:17 Jonathan mentions that the server can send an AJAX request.

With [AJAX][2130128c], web applications can send data to, and retrieve data from, a server asynchronously (in the background) without interfering with the display and behavior of the existing page. The data sent and returned is usually in the format of JSON (see [AJAJ][3851204d]).

  [2130128c]: http://en.wikipedia.org/wiki/Ajax_(programming) "AJAX"
  [3851204d]: http://en.wikipedia.org/wiki/AJAJ "AJAJ"


### 29.  Let's Make A Bar Chart
In the following videos, Jonathan will be working through part II of Mike Bostock's [Let's Make a Bar Chart Tutorial][f2b566db].

  [f2b566db]: http://bost.ocks.org/mike/bar/ "Bar Chart Tutorial"

We recommend going through Part I and Part II of the tutorial.

To examine the code files, we recommend using a text editor such as Sublime Text 3. You are welcome to use any text editor.


### 30. Code Structure And JavaScript
The code that Jonathan outlines is an adaptation from [Part II of Mike Bostock's Let's Make a Bar Chart][5edbe9dd].

  [5edbe9dd]: http://bost.ocks.org/mike/bar/2/ "Part II of Bar Chart Tutorial"

You can follow along with Jonathan by downloading the associated files and from the Downloadables section.


### 31. Layout And Scales
Mike Bostock's [Let's Make a Bar Chart Tutorial][f2b566db].  

@2:10 Jonathan discusses adding the domain to the linear scale, x. Keep in mind that you can set the domain and range of the linear scale separately or in a few lines of code using the method chaining syntax.

@3:14 Jonathan discusses passing a general function to the d3.max function. This "unnamed" function returns the information stored in the "value" property for each row of data in the data.tsv file. Keep in mind that each row of thedata.tsv file will be represented as a JavaScript object.

For example, take a look at the data.tsv file. Each row of the data.tsv file is a JavaScript object inside the data array. The first Javascript object then is {"name": "Locke", "value": 4}. In our case, the "unnamed" function(d) is defined to return d.value so the first data object returns the value 4. The function d3.max returns the largest value of all the values that are stored under the "value" property in the JavaScript objects.

The beauty of d3 is the ability to generalize though! We could define the "unnamed" function to be any function. Instead of pulling information from the "value" property, we could use the length of each name from the "name" property. Depending on what data you are trying to represent in your scale, you may write a different function(d) to go inside of the d3.max().

You don't have to pass a function into d3.max(). If you don't pass a function, then d3.max(array) returns the maximum element in the array based on "natural order". See the documentation for more information. [D3 Arrays](https://github.com/mbostock/d3/wiki/Arrays#d3_max)


### 32. Binding Data
Jonathan will cover the details of how exactly D3 binds data later in the course, but if you are interested in learning more now, Mike Bostock's [How Selections Work][7f16b28b] provides a great overview.

  [7f16b28b]: http://bost.ocks.org/mike/selection/ "How Selection Work"


### 33. Adding Bars And Text  
Much of this code might leave you confused. At this point in the course, you should not understand every line of code. Instead, you should focus on the structure of the code and any common functions or patterns that you see.

Throughout this code, you might notice the pattern function(d) { ... some code ...}.

These are anonymous accessor functions that access a data value using the parameter d to return a calculated value or string. You will learn about [anonymous accessor functions][92c4ce9d] and [how D3 binds data to SVG elements][cd49c7bc] in Lesson 3.

  [92c4ce9d]: https://www.udacity.com/course/viewer#!/c-ud507/l-3069149263/m-3071138998 "Anonymous Accessor Functions"
  [cd49c7bc]: https://www.udacity.com/course/viewer#!/c-ud507/l-3069149263/m-3071139018 "How D3 Binds Data to SVG Elements"


### 34. From Source Code To Graphic
If you would like to run these visualizations locally, you will need to start an HTTP sever. There will be instructions for doing this later in [Lesson 2b][c30d2d8c].

  [c30d2d8c]: https://www.udacity.com/course/viewer#!/c-ud507/l-3168988586/m-3063989000 "Lesson 2b"
