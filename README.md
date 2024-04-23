# Wild Rift Gold Efficiency

<p align="center">
  <a href="https://wildrift.leagueoflegends.com/en-us/news/game-updates/wild-rift-patch-notes-5-1/"><img src="https://img.shields.io/badge/Wild_Rift_Patch_Notes-5.1-blue.svg?logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjEiIGlkPSJMYXllcl8yIiB4PSIwcHgiIHk9IjBweCIgdmlld0JveD0iMCAwIDQwIDQwIiB4bWw6c3BhY2U9InByZXNlcnZlIiB3aWR0aD0iNDBweCIgaGVpZ2h0PSI0MHB4IiBzdHlsZT0iIj48c3R5bGUgdHlwZT0idGV4dC9jc3MiPi5zdDB7ZmlsbDojNEFDNUYyO308L3N0eWxlPiA8Zz48cG9seWdvbiBjbGFzcz0ic3QwIiBwb2ludHM9IjIzLjQsMjguOSAyNS45LDM1LjIgMzAsMzUuMiAzMS44LDI4LjkgICI+PC9wb2x5Z29uPiA8cGF0aCBjbGFzcz0ic3QwIiBkPSJNMTkuMiwyMy4xYy0xLjUtMy43LTMuMy04LjYtMi44LTljMC4yLTAuMiwxLjIsMC43LDIuNywzLjNjMC4yLDAuMywwLjEtMC4xLDAuMS0wLjNjMC0yLDAtMTQuMSwwLTE0LjEgICBzLTUuNCwwLTUuOSwwYy0wLjMsMC0wLjQsMC0wLjQsMC4xYy0wLjEsMC4xLDAsMC4yLDAsMC40YzEuOSw1LjcsMi43LDguOSwyLjMsOS4yQzE1LDEyLjksMTQsMTEuNCwxMi40LDhDMTAsMi44LDguNS0wLjEsOC4zLDAuMSAgIEM4LDAuMyw5LjcsNS42LDE0LDE3LjVjMS40LDMuOSwxLjksNS45LDEuNiw2LjFjLTAuMywwLjItMS4xLTEuMS0yLjMtMy41Yy0xLjQtMi44LTItMy45LTIuMi0zLjljLTAuMiwwLjEsMC4zLDEuOSwxLjIsNC41ICAgYzEuMyw0LjEsMy41LDExLjIsMy4xLDExLjVjLTAuMiwwLjEtMC45LTEtMi4zLTQuMWMtMC4zLTAuNy0wLjUtMS0wLjUtMWMwLDAtMC4xLDAuMS0wLjEsMC4zYzAsMC40LDAsNC42LDAsNC42bC0xLjYsMy4zaDcuNCAgIGMtMS45LTUuNS0yLjUtOC0yLjItOC4xYzAuNC0wLjIsMiwzLDQsOC4xYzEuOSwwLjksNC4zLDMuMiw1LjcsNC41YzAuMywwLjMsMC40LDAuMywwLjMsMEMyNC40LDM1LjgsMjIuMiwzMC41LDE5LjIsMjMuMXoiPjwvcGF0aD48L2c+PC9zdmc+"></a>
  <a href="https://github.com/changchiyou/wildrift-gold-efficiency/actions/workflows/jekyll.yml"><img src="https://github.com/changchiyou/wildrift-gold-efficiency/actions/workflows/jekyll.yml/badge.svg" alt="Github Action"></a>
</p>

A website combining the gold efficiency calculation formula from [<img src="https://static.wikia.nocookie.net/leagueoflegends/images/e/e6/Site-logo.png" width="17" height="17">](https://leagueoflegends.fandom.com/wiki/Gold_efficiency_(Wild_Rift)) with the design elements from [<img src="https://wr-meta.com/favicon.png" width="15" height="15">](https://wr-meta.com/items/), featuring manually updated item data for [Wild Rift](https://wildrift.leagueoflegends.com/).

## Backstory

Being a data enthusiast, I found the concept of Gold Efficiency mentioned in [<img src="https://static.wikia.nocookie.net/leagueoflegends/images/e/e6/Site-logo.png" width="17" height="17"> Gold efficiency (Wild Rift) | League of Legends Wiki](https://leagueoflegends.fandom.com/wiki/Gold_efficiency_(Wild_Rift)) highly intriguing. However, upon initial inspection, I noticed that the website contained a multitude of outdated and erroneous item data. Moreover, its disorganized layout made reading difficult, rendering it unsuitable for direct use.

After some time, I came across another website, [<img src="https://wr-meta.com/favicon.png" width="15" height="15"> WR META - LoL Wild Rift All Items and Runes](https://wr-meta.com/items/), which drew me in with its sleek and elegant design, as well as its CSS style. Although it also suffered from the issue of outdated and inaccurate item data, I had an idea:

<p align="center"><img src="https://github.com/changchiyou/wildrift-gold-efficiency/assets/46549482/59cdaef3-638a-40cf-beb7-99d5a9360eda" style="width: 65%;"></p>

Merging the calculation **formula** from [<img src="https://static.wikia.nocookie.net/leagueoflegends/images/e/e6/Site-logo.png" width="17" height="17">](https://leagueoflegends.fandom.com/wiki/Gold_efficiency_(Wild_Rift)) with the **style** of [<img src="https://wr-meta.com/favicon.png" width="15" height="15">](https://wr-meta.com/items/), and **manually updating** the item data myself. Thus, this website was born out of this concept.

## Installation (for contributer)

1. [Installation | Jekyll • Simple, blog-aware, static sites](https://jekyllrb.com/docs/installation/)
2. Clone this project via `git`:
    ```
    git clone git@github.com:changchiyou/wildrift-gold-efficiency.git; cd wildrift-gold-efficiency
    ```
3. Update `bundle` & Install dependencies from [Gemfile](/Gemfile):
    ```
    bundle update; bundle install
    ```
4. [Serve the Site](https://jekyllrb.com/tutorials/using-jekyll-with-bundler/#serve-the-site):
    ```
    bundle exec jekyll serve
    ```

## Update gold efficiency

1. Manually update item data in [item.yml](/_data/items.yml) ( and images' reference in [images.yml](/_data/images.yml)).
2. Install python dependencies and execute [data.py](/data.py) to re-calculate gold efficiency:

    ```
    pip install -r requirements.txt
    ```

    ```
    python data.py -c
    ```



