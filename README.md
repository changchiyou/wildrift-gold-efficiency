# Wild Rift Gold Efficiency

<p align="center">
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



