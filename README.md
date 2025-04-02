# [Wild Rift Gold Efficiency](changchiyou.github.io/wildrift-gold-efficiency/)

<p align="center">
  <a href="https://github.com/changchiyou/wildrift-gold-efficiency/actions/workflows/jekyll.yml"><img src="https://github.com/changchiyou/wildrift-gold-efficiency/actions/workflows/jekyll.yml/badge.svg" alt="Github Action"></a>
  <a href="https://crowdin.com/?utm_term=click-badge-add-on" rel="nofollow"><img style="width:77;height:22px" src="https://badges.crowdin.net/badge/dark/crowdin-on-light.png" srcset="https://badges.crowdin.net/badge/dark/crowdin-on-light.png 1x,https://badges.crowdin.net/badge/dark/crowdin-on-light@2x.png 2x"  alt="Crowdin | Agile localization for tech companies" /></a>
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

## Translation

> [!NOTE]
> 🌍 Help Us Expand Our Language Options!
We'd love to make our project accessible to more people around the world. If you speak another language, you can help by suggesting new language options and contributing translations. Every little bit helps!
> 
> - Suggest a Language: If you don't see your language, add a suggestion!
> - Translate: Contribute translations to make our project better for everyone.
>
> Thank you for making our project more inclusive!

|Progress|Language|
|-|-|
|[![zh-TW translation](https://img.shields.io/badge/dynamic/json?color=blue&label=zh-TW&style=flat&logo=crowdin&query=%24.progress.3.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-16995820-777056.json)](https://crowdin.com/project/wildrift-gold-efficiency)|Chinese Traditional|
|[![de translation](https://img.shields.io/badge/dynamic/json?color=blue&label=de&style=flat&logo=crowdin&query=%24.progress.0.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-16995820-777056.json)](https://crowdin.com/project/wildrift-gold-efficiency)|German|
|[![ja translation](https://img.shields.io/badge/dynamic/json?color=blue&label=ja&style=flat&logo=crowdin&query=%24.progress.1.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-16995820-777056.json)](https://crowdin.com/project/wildrift-gold-efficiency)|Japanese|
|[![pt-BR translation](https://img.shields.io/badge/dynamic/json?color=blue&label=pt-BR&style=flat&logo=crowdin&query=%24.progress.2.data.translationProgress&url=https%3A%2F%2Fbadges.awesome-crowdin.com%2Fstats-16995820-777056.json)](https://crowdin.com/project/wildrift-gold-efficiency)|Portuguese, Brazilian|

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
    bundle exec jekyll serve --port 4001
    ```

## UpdateEstablish Gold Efficiency Page for the New Version v2 (for maintainer)

Please refer to [update_v2.md](/docs/update_v2.md).
