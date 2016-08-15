<!--
.. title: Setting Up Nikola, a Static Site Generator
.. slug: nikola-setup
.. date: 2016-08-15 11:32:11 UTC+08:00
.. tags: Nikola, github, github pages
.. category:
.. link:
.. description:
.. type: text
-->

A while back, I started to look into static site generators for building my professional and personal blog site.  I had used [Wordpress][6d41a4cd] long ago, but want to practice programming in Python.  Recently I tried out [Medium][5e0e86b2], but find it rather limiting when it comes to formatting content, and to organizing my posts.   

  [6d41a4cd]: https://wordpress.org/ "Wordpress"
  [5e0e86b2]: https://medium.com/ "Medium"

I want to use the opportunity to explore what's new out there and get my hands dirty in programming again.  While researching, I stumble upon this site for static site generator - [StaticGen][df0bc734].  After testing out briefly with Pelican and Nikola, At last I decided to go with [Nikola][c35f987f] .

  [df0bc734]: https://www.staticgen.com/ "StaticGen"
  [c35f987f]: https://getnikola.com/ "Nikola"

Nikola is rather lightweight, written with Python, supports contents written in markdown (my preferred way of writing content), and supports [MathJax][24e45e1a] with a little tweaking.

  [24e45e1a]: https://www.mathjax.org/ "MathJax"

### Installation ###
The initial installation is rather basic.  First I install Nikola using pip.  Note that I install the extras as well, so I don't have to worry about them later.
```
$ pip install --upgrade "Nikola[extras]"
```
Then, I created a virtual environment and a project for this using  [`virtualevn`][8b1ab3a0] and [`virtualevnwrapper`][d8a1b3f5]:
```
$ mkproject -p /usr/local/bin/python3 nikola
$ workon nikola
```
  [d8a1b3f5]: https://virtualenvwrapper.readthedocs.io/en/latest/ "Python VirtualEnvWrapper"
  [8b1ab3a0]: https://virtualenv.pypa.io/en/stable/ "Python VirtualEnv"

Then I was able to initialize a Nikola site.  
```
$ nikola init {site_name}
```
Voila! We have a site!  Nikola has neat built-in commands. Check them out with `nikola help`.  For example, to create a new post, use the following:
```
$ nikola new_post {post_name}.md
```
I like to keep the nikola server running as I go through the edit/preview cycles, I typed
```
$ nikola auto -b
```

### Configurations ###
I used most of the default settings in the `config.py`, except for the following:
```
# Category Settings #
CATEGORY_PATH = "categories"
CATEGORY_PREFIX = ""
CATEGORY_ALLOW_HIERARCHIES = True
CATEGORY_OUTPUT_FLAT_HIERARCHY = False
CATEGORY_PAGES_ARE_INDEXES = False

# Author Page #
ENABLE_AUTHOR_PAGES = False

# Archives Settings #
CREATE_MONTHLY_ARCHIVE = True
CREATE_DAILY_ARCHIVE = True
ARCHIVE_PATH = "archives"
ARCHIVE_FILENAME = "archives.html"

# FavIcons #
FAVICONS = (
    ("icon", "{path to favicon}", "64x64"),
    ("icon", "{path to favicon}", "512x512"),
)

# Hide Source Link #
SHOW_SOURCELINK = False
```

### Organizing Content ###
Instead the built-in Category and Tag features, I am not quite satisfied with the way it organizes my content.  I prefer to organize my content a certain way.  So, in the `config.py`, I made the following settings:
```
POSTS = (
    ("posts/*.md", "posts", "post.tmpl"),
    ("course-notes/*.md", "course-notes", "post.tmpl"),
    ("links/*.md", "links", "post.tmpl"),
    ("books/*.md", "books", "post.tmpl"),
    ("movies-shows/*.md", "movies-shows", "post.tmpl"),
    ("music/*.md", "music", "post.tmpl"),
)
PAGES = (
    ("pages/*.md", "pages", "story.tmpl"),
)
```
Although Nikola offers two content types - post and page, I figure I only use the post type (for now at least).  I am simply keeping `PAGES` as is.   

To add the corresponding content type to the navigation links,
```
NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ("/posts/index.html", "Articles"),
        ("/course-notes/index.html", "Course Notes"),
        ("/links/index.html", "Links"),
        ("/books/index.html", "Books"),
        ("/archives/archives.html", "Archives"),
        ("/tags.html", "Tags"),
    ),
}
```

### Themes ###
Nikola's theme repo doesn't offer too extensive a choice. So I decided to make my own by following this very nicely written guide in [creating your own theme][8003f5e7].  You may find [my theme here][a1b3b6ee].  

  [8003f5e7]: http://nikola.readthedocs.io/en/latest/creating-a-theme/ "Creating a Nikola Theme"
  [a1b3b6ee]: https://github.com/chowy1026/nikola-themes/tree/hyde/v7/hyde "Nikola Theme - Hyde"


### Enabling MathJax ###
The steps to enable MathJax in Nikola are easy. First, add the following line to `templates\base_helper.tmpl`.
```
<link rel="stylesheet" href="http://fonts.googleapis.com/css?family=PT+Sans:400,400italic,700|Abril+Fatface">
```
Then add
```
MATHJAX_CONFIG = """
    <script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
    <script type="text/x-mathjax-config">
        MathJax.Hub.Config({
            tex2jax: {
                inlineMath: [ ['$','$'], ["\\\(","\\\)"] ],
                displayMath: [ ['$$','$$'], ["\\\[","\\\]"] ],
                processEscapes: true
            },
            displayAlign: 'left', // Change this to 'center' to center equations.
            "HTML-CSS": {
                styles: {'.MathJax_Display': {"margin": 0}}
            }
        });
    </script>
    <script type="text/x-mathjax-config">
  MathJax.Hub.Queue(function() {
    // Fix <code> tags after MathJax finishes running. This is a
    // hack to overcome a shortcoming of Markdown. Discussion at
    // https://github.com/mojombo/jekyll/issues/199
    var all = MathJax.Hub.getAllJax(), i;
    for(i = 0; i < all.length; i += 1) {
        all[i].SourceElement().parentNode.className += ' has-jax';
    }
});
</script>
    """
```
and this
```
HIDDEN_TAGS = ['mathjax']
```
to `config.py`.  All set! In markdown, I can use
`\\( {math expression} \\)` for inline math, and
```
\\[ {math expression} \\]
```
for block display.  For other references to [MathJax][24e45e1a], see [this link][02dad9de].

  [02dad9de]: https://mechowy.github.io/link/mathjax/ "MathJax Reference Links"

### GitHub Deploy ###
Admittedly, Git confuses me sometimes.  And the built-in command that Nikola offers is absolutely godsent.  It nicely push content to the master branch of your userpage repo, which is {github.username}.github.io, and keep source in the source branch.  

Having had my empty `{github.username}.github.io` repo ready on github, I have these in my `config.py`:
```
# DEPLOY_COMMANDS = {
#    'default': [
#        'git add .',
#        "git commit -am 'Update'",
#        'git push origin master',
#        'git subtree split --prefix output -b gh-pages',
#        'git push -f origin gh-pages:gh-pages',
#        'git branch -D gh-pages'
#    ]
#}

GITHUB_SOURCE_BRANCH = 'source'
GITHUB_DEPLOY_BRANCH = 'master'

GITHUB_REMOTE_NAME = 'origin'

GITHUB_COMMIT_SOURCE = True
```

~~ I am honestly a little confused whether or not the `DEPLOY_COMMANDS` is actually needed.  I looked into the github_deploy.py under the hood of Nikola, it seems the deploy commands are already predefined.  I need to further experiment whether the `nikola github_deploy` would work without a `DEPLOY_COMMANDS` defined in `config.py`.  Will update when I am 200% certain. ~~

Update: `nikola github_deploy` IS indeed GOD-SENT.  Without having to define `DEPLOY_COMMANDS`, it nicely does everything for us - push `output` content to master, and source to source.

~~That said~~ Now, whenever I want to update content to my github page, I simply type:
```
$ nikola github_deploy
```

### Others ###
For additional features, there are [plugins][d8d62cc3] that could be installed.  There is also a [Google Discussion Group for Nikola][8d3e7f67].  

  [d8d62cc3]: https://github.com/getnikola/plugins "Nikola Plugins"
  [8d3e7f67]: https://groups.google.com/forum/#!forum/nikola-discuss "Nikola Google Dicussion Group"
