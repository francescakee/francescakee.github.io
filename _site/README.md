# About
## The Slate theme

[![Build Status](https://travis-ci.org/pages-themes/slate.svg?branch=master)](https://travis-ci.org/pages-themes/slate) [![Gem Version](https://badge.fury.io/rb/jekyll-theme-slate.svg)](https://badge.fury.io/rb/jekyll-theme-slate)

*Slate is a Jekyll theme for GitHub Pages. You can [preview the theme to see what it looks like](http://pages-themes.github.io/slate)*

## Customizing

### Configuration variables

Slate will respect the following variables, if set in your site's `_config.yml`:

```yml
title: [The title of your site]
description: [A short description of your site's purpose]
```

Additionally, you may choose to set the following optional variables:

```yml
show_downloads: ["true" or "false" to indicate whether to provide a download URL]
google_analytics: [Your Google Analytics tracking ID]
```

### Stylesheet

If you'd like to add your own custom styles:

1. Create a file called `/assets/css/style.scss` in your site
2. Add the following content to the top of the file, exactly as shown:
    ```scss
    ---
    ---

    @import "{{ site.theme }}";
    ```
3. Add any custom CSS (or Sass, including imports) you'd like immediately after the `@import` line

### Layouts

If you'd like to change the theme's HTML layout:

1. [Copy the original template](https://github.com/pages-themes/slate/blob/master/_layouts/default.html) from the theme's repository<br />(*Pro-tip: click "raw" to make copying easier*)
2. Create a file called `/_layouts/default.html` in your site
3. Paste the default layout content copied in the first step
4. Customize the layout as you'd like


### How to add and remove images

Look for the frontmatter in the index.html file you can add or remove images in tiles from adding or removing the names of the image in thumb array  and same goes for carousel. The thumb files should be stored in /assets/images/thumbs/ and actual image in /assets/images/ folder.

CAUTION: Take care of the spacing, indentation, and format when adding or removing the names from the array.

### site generation

`_site` dir is generated when you run jekyll, it converts all the liquid-tags, frontmatter, markdown, scss of files into simple html, css which is recognized by the web browsers and puts them in the `_site` dir. As you can see there is a index.md in the root folder which contains three dashes at the top and bottom the content inside it is called frontmatter and inside it we have specified certain info about that page refer these pages to get familiar.

### github pages and Jekyll


To create a github-pages repo use the instructions given in this doc https://pages.github.com/ and for more information on jekyll refer this jekyll docs https://jekyllrb.com/docs/home/ .


### preview a branch(different approach)
If you want to download the branch run these commands (for linux terminal) <br />
git clone https://github.com/username/reponame.git <br />
cd reponame <br />
git checkout master  `(for changing branch)`<br />

To install required gem files you can either manually install all the required using `gem install` or use `bundle exec jekyll serve`<br />

jekyll serve `(for Running jekyll)`<br />
now open browser and go to [`localhost:4000`](http://localhost:4000) to see the website. <br />

To push the changes:-<br />
git add --all<br />
git commit -m "commit message"<br />
git push origin master
