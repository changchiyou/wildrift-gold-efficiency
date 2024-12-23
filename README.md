# Wild Rift Gold Efficiency

<p align="center">
  <a href="https://github.com/changchiyou/wildrift-gold-efficiency/actions/workflows/jekyll.yml"><img src="https://github.com/changchiyou/wildrift-gold-efficiency/actions/workflows/jekyll.yml/badge.svg" alt="Github Action"></a>
</p>

WR(Wild Rift) Gold Efficiency, a website combining the gold efficiency calculation formula from <a href="https://leagueoflegends.fandom.com/wiki/Gold_efficiency_(Wild_Rift)" target="_blank"><img class="badge" src="https://custom-icon-badges.demolab.com/badge/League_of_Legend_Wiki-Gold_efficiency_(Wild_Rift)-1f222e.svg?logo=lolwiki"></a> with the design elements from <a href="https://wr-meta.com/items/" target="_blank"><img class="badge" src="https://custom-icon-badges.demolab.com/badge/WR_META-LoL Wild Rift All Items and Runes-yellow.svg?logo=wrmeta"></a>, featuring manually updated item data from <a href="https://wildrift.leagueoflegends.com/en-us/news/tags/patch-notes/" target="_blank"><img class="badge" src="https://custom-icon-badges.demolab.com/badge/Wild_Rift-Patch_Notes-blue.svg?logo=wildrift"></a>.

|Entrance|Features|PWA|
|-|-|-|
|![entrance](https://github.com/changchiyou/wildrift-gold-efficiency/assets/46549482/bbd4ca8c-27c7-4965-bda0-5ad34058e819)|![feature](https://github.com/changchiyou/wildrift-gold-efficiency/assets/46549482/d1188bd0-4f9a-482d-9bd8-cdb82899f119)|![pwa](https://github.com/changchiyou/wildrift-gold-efficiency/assets/46549482/0fdd3a02-c6a6-48a2-9012-adea46bbbab8)|

## Backstory

Being a data enthusiast, I found the concept of Gold Efficiency mentioned in [<img src="https://static.wikia.nocookie.net/leagueoflegends/images/e/e6/Site-logo.png" width="17" height="17">](https://leagueoflegends.fandom.com/wiki/Gold_efficiency_(Wild_Rift)) highly intriguing. However, upon initial inspection, I noticed that the website contained a multitude of outdated and erroneous item data. Moreover, its disorganized layout made reading difficult, rendering it unsuitable for direct use.

After some time, I came across another website, [<img src="https://wr-meta.com/favicon.png" width="15" height="15">](https://wr-meta.com/items/), which drew me in with its sleek and elegant design, as well as its CSS style. Although it also suffered from the issue of outdated and inaccurate item data, I had an idea:

<p align="center"><img src="https://github.com/changchiyou/wildrift-gold-efficiency/assets/46549482/59cdaef3-638a-40cf-beb7-99d5a9360eda" style="width: 65%;"></p>

Merging the calculation **formula** from [<img src="https://static.wikia.nocookie.net/leagueoflegends/images/e/e6/Site-logo.png" width="17" height="17">](https://leagueoflegends.fandom.com/wiki/Gold_efficiency_(Wild_Rift)) with the **style** of [<img src="https://wr-meta.com/favicon.png" width="15" height="15">](https://wr-meta.com/items/), and **manually updating** the item data myself. Thus, this website was born out of this concept.

## Installation (for developer)

1. [Installation | Jekyll • Simple, blog-aware, static sites](https://jekyllrb.com/docs/installation/)
2. Clone this project via `git`:
    ```bash
    git clone git@github.com:changchiyou/wildrift-gold-efficiency.git; cd wildrift-gold-efficiency
    ```
3. Update `bundle` & Install dependencies from [Gemfile](/Gemfile):
    ```bash
    bundle update; bundle install
    ```
4. [Serve the Site](https://jekyllrb.com/tutorials/using-jekyll-with-bundler/#serve-the-site):
    ```bash
    bundle exec jekyll serve
    ```
