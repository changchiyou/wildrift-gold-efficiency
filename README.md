# Wild Rift Gold Efficiency

<p align="center">
  <a href="https://github.com/changchiyou/wildrift-gold-efficiency/actions/workflows/jekyll.yml"><img src="https://github.com/changchiyou/wildrift-gold-efficiency/actions/workflows/jekyll.yml/badge.svg" alt="Github Action"></a>
</p>

WR(Wild Rift) Gold Efficiency, a website combining the gold efficiency calculation formula from <a href="https://leagueoflegends.fandom.com/wiki/Gold_efficiency_(Wild_Rift)" target="_blank"><img class="badge" src="https://custom-icon-badges.demolab.com/badge/League_of_Legend_Wiki-Gold_efficiency-1f222e.svg?logo=lolwiki"></a> with the design elements from <a href="https://wr-meta.com/items/" target="_blank"><img class="badge" src="https://img.shields.io/badge/WR_META-LoL Wild Rift All Items and Runes-yellow.svg?logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB2ZXJzaW9uPSIxLjEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgd2lkdGg9IjEyMCIgaGVpZ2h0PSIxMjAiPgo8cGF0aCBkPSJNMCAwIEMzOS42IDAgNzkuMiAwIDEyMCAwIEMxMjAgMzkuNiAxMjAgNzkuMiAxMjAgMTIwIEM4MC40IDEyMCA0MC44IDEyMCAwIDEyMCBDMCA4MC40IDAgNDAuOCAwIDAgWiAiIGZpbGw9IiMwNDA0MDAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAsMCkiLz4KPHBhdGggZD0iTTAgMCBDMS4xMTY5Njc2MiAwLjAwMjIyMDYxIDIuMjMzOTM1MjQgMC4wMDQ0NDEyMiAzLjM4NDc1MDM3IDAuMDA2NzI5MTMgQzQuNjQ1OTgyMjEgMC4wMDY4MDQ2NiA1LjkwNzIxNDA1IDAuMDA2ODgwMTkgNy4yMDY2NjUwNCAwLjAwNjk1ODAxIEM4LjU5MzQxOTc5IDAuMDEyMDY1NDIgOS45ODAxNzQxNCAwLjAxNzI4MTQyIDExLjM2NjkyODEgMC4wMjI1OTgyNyBDMTIuNzc3OTczOTQgMC4wMjQ0NjI1IDE0LjE4OTAyMDQyIDAuMDI1ODg2MzggMTUuNjAwMDY3MTQgMC4wMjY4ODU5OSBDMTkuMzIwNDI3MiAwLjAzMDcxMDcyIDIzLjA0MDc0ODQ1IDAuMDQwNTQwNjIgMjYuNzYxMDkzMTQgMC4wNTE1ODk5NyBDMzAuNTU0ODI5NjYgMC4wNjE4MDUwNCAzNC4zNDg1NzI0MyAwLjA2NjM4MzgxIDM4LjE0MjMxODczIDAuMDcxNDI2MzkgQzQ1LjU5MDkwNDE2IDAuMDgyMTYyOTQgNTMuMDM5NDU3NTggMC4wOTkyMzg4MiA2MC40ODgwMjE4NSAwLjEyMDI1NDUyIEM1Ni43OTUzNzA4IDcuNTExMTIyNSA1My4xMDE5NjExNyAxNC45MDE1ODM2MiA0OS4zOTMxMjc0NCAyMi4yODQzNDc1MyBDNDcuNjUyMzY1MjMgMjUuNzQ5NzAwOSA0NS45MTM2NjQxIDI5LjIxNjA4NjQzIDQ0LjE3NTUyMTg1IDMyLjY4Mjc1NDUyIEM0My44MTAwNjI1NiAzMy40MTEzOTcwOSA0My40NDQ2MDMyNyAzNC4xNDAwMzk2NyA0My4wNjgwNjk0NiAzNC44OTA3NjIzMyBDMzcuODE4NTY0MDMgNDUuMzY0OTEzNjUgMzIuNjYwOTkyNzggNTUuODczMzc1MzIgMjcuNzExNDEwNTIgNjYuNDkzNTQ1NTMgQzI3LjMwODk4MTMyIDY3LjM1MDA0NyAyNi45MDY1NTIxMiA2OC4yMDY1NDg0NiAyNi40OTE5MjgxIDY5LjA4OTAwNDUyIEMyNi4xNDk3NjI1NyA2OS44MjU3MDM3NCAyNS44MDc1OTcwNSA3MC41NjI0MDI5NSAyNS40NTUwNjI4NyA3MS4zMjE0MjYzOSBDMjQuNDg4MDIxODUgNzMuMTIwMjU0NTIgMjQuNDg4MDIxODUgNzMuMTIwMjU0NTIgMjIuNDg4MDIxODUgNzUuMTIwMjU0NTIgQzE4Ljc3MjcxMzE5IDYwLjk3MDQ2MTk2IDE1LjkyNjk3NzIxIDQ3Ljc2OTc1MzU3IDE2LjQ4ODAyMTg1IDMzLjEyMDI1NDUyIEMxNS44MjgwMjE4NSAzMy4xMjAyNTQ1MiAxNS4xNjgwMjE4NSAzMy4xMjAyNTQ1MiAxNC40ODgwMjE4NSAzMy4xMjAyNTQ1MiBDMTQuMTc4NjQ2ODUgMzMuOTA0MDA0NTIgMTMuODY5MjcxODUgMzQuNjg3NzU0NTIgMTMuNTUwNTIxODUgMzUuNDk1MjU0NTIgQzEyLjQ4ODAyMTg1IDM4LjEyMDI1NDUyIDEyLjQ4ODAyMTg1IDM4LjEyMDI1NDUyIDExLjQ4ODAyMTg1IDQwLjEyMDI1NDUyIEMxMC43MzI2MzEyMyA0MC40MDY0MjYzOSA5Ljk3NzI0MDYgNDAuNjkyNTk4MjcgOS4xOTg5NTkzNSA0MC45ODc0NDIwMiBDNi4wNzkyNzAzMyA0Mi4yOTEwNTg0NyA0LjQ1Mjk1Mzk5IDQzLjgyMDg0ODMgMi4xMTMwMjE4NSA0Ni4yNDUyNTQ1MiBDMS4zMjU0MDQ2NiA0Ny4wNTk5NDIwMiAwLjUzNzc4NzQ4IDQ3Ljg3NDYyOTUyIC0wLjI3MzY5NjkgNDguNzE0MDA0NTIgQy0yLjcwNDc1OTM2IDUxLjMyNzUwMjczIC01LjA1NDc3MDUxIDUzLjk5NDA5NTE1IC03LjM3OTE2NTY1IDU2LjcwMjI4NTc3IEMtMTAuMjk1MDUyNzcgNjAuMDA4MDI1OTMgLTEzLjMwOTkxOTE4IDYzLjIxNzA5MTQyIC0xNi4zMjQ0NzgxNSA2Ni40MzI3NTQ1MiBDLTIyLjExMzQ5ODk2IDcyLjYwOTIwMjEzIC0yNy44NDEwMzg3NiA3OC44MzUxODExNCAtMzMuNTExOTc4MTUgODUuMTIwMjU0NTIgQy0zNC41MTE5NzgxNSA4My4xMjAyNTQ1MiAtMzQuNTExOTc4MTUgODMuMTIwMjU0NTIgLTMzLjQ4MzE2OTU2IDgwLjAxMzU2NTA2IEMtMzIuOTUxNDM2MjYgNzguNjc0NzcxNTQgLTMyLjQxMDg1NDc1IDc3LjMzOTQ3MzA1IC0zMS44NjM1NDA2NSA3Ni4wMDY5NzMyNyBDLTMxLjU3NTM1NDYxIDc1LjI4OTA5MTM0IC0zMS4yODcxNjg1OCA3NC41NzEyMDk0MSAtMzAuOTkwMjQ5NjMgNzMuODMxNTczNDkgQy0zMC4wNDY1NjY4NiA3MS40ODcyMzM3OCAtMjkuMDkxNzMzMzQgNjkuMTQ3NjAzOTIgLTI4LjEzNjk3ODE1IDY2LjgwNzc1NDUyIEMtMjcuNDkxMDYxNzIgNjUuMjA2MDk2OCAtMjYuODQ1NzE3NTMgNjMuNjA0MjA4MiAtMjYuMjAwOTQyOTkgNjIuMDAyMDkwNDUgQy0yMy40MDkyMDA1MSA1NS4wODg3NjQ5OSAtMjAuNTc5NTc4OTIgNDguMTk4MDY3NDIgLTE3LjU3NDQ3ODE1IDQxLjM3NDE2MDc3IEMtMTYuOTQ2Nzg1MjggMzkuOTQ4NzM5NjIgLTE2Ljk0Njc4NTI4IDM5Ljk0ODczOTYyIC0xNi4zMDY0MTE3NCAzOC40OTQ1MjIwOSBDLTE1LjU1MTIyMDQ1IDM2Ljc5OTgzNSAtMTQuNzg0MTE4MTcgMzUuMTEwMzgyNzkgLTE0LjAwMjcwMDgxIDMzLjQyNzYyNzU2IEMtMTIuNDIyMTM2MDcgMjkuOTA0NjQ5OTcgLTExLjUwOTE5NzYxIDI3LjYwODUxNzcgLTExLjUzMTUwOTQgMjMuNjkwNTY3MDIgQy0xMS41MDM4NzA0NyAxOC42MzgxNzE0NyAtOS42MTQyOTQ1IDE0LjgwNjA3NDY2IC03LjU3NDQ3ODE1IDEwLjI0NTI1NDUyIEMtNy4yMDEyOTQ1NiA5LjM3OTAwNDUyIC02LjgyODExMDk2IDguNTEyNzU0NTIgLTYuNDQzNjE4NzcgNy42MjAyNTQ1MiBDLTMuMTk1NzA4MjQgMC4xNTI5ODYzNCAtMy4xOTU3MDgyNCAwLjE1Mjk4NjM0IDAgMCBaICIgZmlsbD0iI0ZDRjUwMCIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoNTYuNTExOTc4MTQ5NDE0MDYsLTAuMTIwMjU0NTE2NjAxNTYyNSkiLz4KPHBhdGggZD0iTTAgMCBDMC4zMyAwIDAuNjYgMCAxIDAgQzEgMjcuNzIgMSA1NS40NCAxIDg0IEMtMTMuODUgODQgLTI4LjcgODQgLTQ0IDg0IEMtNDIuNjIwMTA1NDMgODAuNTUwMjYzNTYgLTQxLjQ5OTgyNDM1IDc3Ljk3MzI0NTAxIC0zOS41NjI1IDc0LjkzNzUgQy0zOS4xNTEyODkwNiA3NC4yODY1MjM0NCAtMzguNzQwMDc4MTIgNzMuNjM1NTQ2ODggLTM4LjMxNjQwNjI1IDcyLjk2NDg0Mzc1IEMtMzcgNzEgLTM3IDcxIC0zNS41MzkwNjI1IDY5LjIxMDkzNzUgQy0zMy40NzA5Mzk4MiA2Ni4yMzk5Nzk1NCAtMzIuMjAxMTQ5MzMgNjMuMDA5OTMyNzMgLTMwLjgxMjUgNTkuNjg3NSBDLTIxLjk2NDMzNDg4IDM5LjE4NTEyNDI3IC0xMS4wNTg1OTM4IDE5LjM3OTEyMjMgMCAwIFogIiBmaWxsPSIjRkRGNTAwIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMTksMzYpIi8+CjxwYXRoIGQ9Ik0wIDAgQzIuNjc4MjcwOTEgMi42NzgyNzA5MSAyLjk5MjA5MDA4IDUuNDcyNTcxMiAzLjc1IDkuMDYyNSBDMy45MTMzODg2NyA5LjgxNTMxMjUgNC4wNzY3NzczNCAxMC41NjgxMjUgNC4yNDUxMTcxOSAxMS4zNDM3NSBDNi4wODE5MDc5NCAyMC4wMjkxOTQwNiA3LjY1ODg5NTAzIDI4Ljc2NjkxMjU2IDkuMjUgMzcuNSBDOS4zODY2MDAzNCAzOC4yNDkwMzU5NSA5LjUyMzIwMDY4IDM4Ljk5ODA3MTkgOS42NjM5NDA0MyAzOS43Njk4MDU5MSBDMTAuMDU0NTY5NDIgNDEuOTE5MDAwNSAxMC40NDIwOTMyNiA0NC4wNjg3MjUzNSAxMC44MjgxMjUgNDYuMjE4NzUgQzExLjE2Njk4NzMgNDguMTA0OTcwNyAxMS4xNjY5ODczIDQ4LjEwNDk3MDcgMTEuNTEyNjk1MzEgNTAuMDI5Mjk2ODggQzEyIDUzIDEyIDUzIDEyIDU1IEMtOC43OSA1NSAtMjkuNTggNTUgLTUxIDU1IEMtNDkuMzgzMDY4NTcgNTEuNzY2MTM3MTQgLTQ4LjM3MDUwODc5IDUwLjEwMzkwNzA0IC00NS45ODgyODEyNSA0Ny42MDkzNzUgQy00NS4zOTQ2Njc5NyA0Ni45ODE2MDE1NiAtNDQuODAxMDU0NjkgNDYuMzUzODI4MTMgLTQ0LjE4OTQ1MzEyIDQ1LjcwNzAzMTI1IEMtNDMuMjYwMzYxMzMgNDQuNzM4MzAwNzggLTQzLjI2MDM2MTMzIDQ0LjczODMwMDc4IC00Mi4zMTI1IDQzLjc1IEMtNDEuMDk4OTU5MjggNDIuNDc1MTk1NjggLTM5Ljg4NjcyMTIzIDQxLjE5OTE1MDAzIC0zOC42NzU3ODEyNSAzOS45MjE4NzUgQy0zOC4wNTcyNzI5NSAzOS4yNjk2MDkzOCAtMzcuNDM4NzY0NjUgMzguNjE3MzQzNzUgLTM2LjgwMTUxMzY3IDM3Ljk0NTMxMjUgQy0zNS4xMzExNzA2NCAzNi4xNDE2NDA4MyAtMzMuNTM1MzQwMDkgMzQuMjk2MjIyMTUgLTMxLjk0NTMxMjUgMzIuNDIxODc1IEMtMjYuMTgwODY2ODkgMjUuNzc4ODc1NzMgLTE5Ljc5ODYyMDA0IDE5LjY5NDY2NTg0IC0xMy41NjI1IDEzLjUgQy0xMi4yNDUyMDk0MSAxMi4xODc3MzQxNSAtMTAuOTI4MTUwMTQgMTAuODc1MjM2MDUgLTkuNjExMzI4MTIgOS41NjI1IEMtNi40MTAyMTM5IDYuMzcyMzE0OTQgLTMuMjA1OTgxMzUgMy4xODUyOTM0OSAwIDAgWiAiIGZpbGw9IiNGREY1MDAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDYwLDY1KSIvPgo8cGF0aCBkPSJNMCAwIEMxMy44NiAwIDI3LjcyIDAgNDIgMCBDMzcuMTI1IDExLjE4NzUgMzcuMTI1IDExLjE4NzUgMzUuNTk4MTQ0NTMgMTQuNjg4MjMyNDIgQzM1LjE5NzA4NDk2IDE1LjYwOTY3MDQxIDM0Ljc5NjAyNTM5IDE2LjUzMTEwODQgMzQuMzgyODEyNSAxNy40ODA0Njg3NSBDMzMuNzcwMTA0OTggMTguODg2NTUzOTYgMzMuNzcwMTA0OTggMTguODg2NTUzOTYgMzMuMTQ1MDE5NTMgMjAuMzIxMDQ0OTIgQzMyLjA1NzE0MTQxIDIyLjg2NjMwODYgMzEuMDE2Njk5MDUgMjUuNDI1NTg3MzUgMzAgMjggQzI4LjkxMzA3NjQ5IDI0LjczOTIyOTQ3IDI5LjA1NDYwNzM3IDI0LjAyOTA2NzcxIDI5Ljk5NjA5Mzc1IDIwLjg3NSBDMzAuMjI0OTAyMzQgMjAuMDg2MDkzNzUgMzAuNDUzNzEwOTQgMTkuMjk3MTg3NSAzMC42ODk0NTMxMiAxOC40ODQzNzUgQzMwLjkzNjMwODU5IDE3LjY2NDUzMTI1IDMxLjE4MzE2NDA2IDE2Ljg0NDY4NzUgMzEuNDM3NSAxNiBDMzEuOTE4ODIwOTkgMTQuMzc2MDIwNDIgMzIuMzk2ODI4IDEyLjc1MTA1Mzk5IDMyLjg3MTA5Mzc1IDExLjEyNSBDMzMuMDg2OTMxMTUgMTAuNDA1NzAzMTMgMzMuMzAyNzY4NTUgOS42ODY0MDYyNSAzMy41MjUxNDY0OCA4Ljk0NTMxMjUgQzM0LjExODU2OTMxIDYuODQ4MDAwNDUgMzQuMTE4NTY5MzEgNi44NDgwMDA0NSAzNCA0IEMzMC4xMzg1NzU3MyAxMS4xNTU3ODYyMyAyNy40NzkwMTYyNiAxOC42NTQ5NDQzNiAyNC44MTI1IDI2LjMxMjUgQzI0LjU2NTc2NTM4IDI3LjAxNTM0MTE5IDI0LjMxOTAzMDc2IDI3LjcxODE4MjM3IDI0LjA2NDgxOTM0IDI4LjQ0MjMyMTc4IEMxNi4wNzkzMDE2MSA1MS4xOTI0MDcxMyA4LjU3MDEwNTE2IDc0LjEwOTI0OTA5IDEgOTcgQzAuNjcgOTcgMC4zNCA5NyAwIDk3IEMwIDY0Ljk5IDAgMzIuOTggMCAwIFogIiBmaWxsPSIjRkRGNTAwIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLDApIi8+CjxwYXRoIGQ9Ik0wIDAgQy0xLjM5MjI0NTkgNC42MjY3NTY1NyAtMy4yOTUyMDk4NCA4LjY0Njg2MjMxIC01LjYyNSAxMi44NzUgQy02LjI1NjY0MDYzIDE0LjAyNzQyMTg4IC02Ljg4ODI4MTI1IDE1LjE3OTg0Mzc1IC03LjUzOTA2MjUgMTYuMzY3MTg3NSBDLTguMDIxMTcxODcgMTcuMjM2MDE1NjIgLTguNTAzMjgxMjUgMTguMTA0ODQzNzUgLTkgMTkgQy05Ljk5IDE4LjM0IC0xMC45OCAxNy42OCAtMTIgMTcgQy0xMC45MDMyMjc2NSAxNC43MjUzMjQxOSAtOS43OTgwMTU3OCAxMi40NTU0NTQ3NiAtOC42ODc1IDEwLjE4NzUgQy04LjM3ODc2OTUzIDkuNTQ0OTAyMzQgLTguMDcwMDM5MDYgOC45MDIzMDQ2OSAtNy43NTE5NTMxMiA4LjI0MDIzNDM4IEMtMy42OTU4NzkyMSAwIC0zLjY5NTg3OTIxIDAgMCAwIFogIiBmaWxsPSIjMUMxQjAwIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMDYsNjApIi8+CjxwYXRoIGQ9Ik0wIDAgQy0xLjE1NTg1Mjg1IDMuOTEyMTE3MzMgLTIuMzU1MzQ5NjIgNi44NzQ1MDQxIC01IDEwIEMtNS42NiA5LjY3IC02LjMyIDkuMzQgLTcgOSBDLTQuNCAwIC00LjQgMCAwIDAgWiAiIGZpbGw9IiMyNjI0MDAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEwNiw2MCkiLz4KPC9zdmc+Cg=="></a>, featuring manually updated item data from <a href="https://wildrift.leagueoflegends.com/en-us/news/tags/patch-notes/" target="_blank"><img class="badge" src="https://img.shields.io/badge/Wild_Rift-Patch_Notes-blue.svg?logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2ZXJzaW9uPSIxLjEiIGlkPSJMYXllcl8yIiB4PSIwcHgiIHk9IjBweCIgdmlld0JveD0iMCAwIDQwIDQwIiB4bWw6c3BhY2U9InByZXNlcnZlIiB3aWR0aD0iNDBweCIgaGVpZ2h0PSI0MHB4IiBzdHlsZT0iIj48c3R5bGUgdHlwZT0idGV4dC9jc3MiPi5zdDB7ZmlsbDojNEFDNUYyO308L3N0eWxlPiA8Zz48cG9seWdvbiBjbGFzcz0ic3QwIiBwb2ludHM9IjIzLjQsMjguOSAyNS45LDM1LjIgMzAsMzUuMiAzMS44LDI4LjkgICI+PC9wb2x5Z29uPiA8cGF0aCBjbGFzcz0ic3QwIiBkPSJNMTkuMiwyMy4xYy0xLjUtMy43LTMuMy04LjYtMi44LTljMC4yLTAuMiwxLjIsMC43LDIuNywzLjNjMC4yLDAuMywwLjEtMC4xLDAuMS0wLjNjMC0yLDAtMTQuMSwwLTE0LjEgICBzLTUuNCwwLTUuOSwwYy0wLjMsMC0wLjQsMC0wLjQsMC4xYy0wLjEsMC4xLDAsMC4yLDAsMC40YzEuOSw1LjcsMi43LDguOSwyLjMsOS4yQzE1LDEyLjksMTQsMTEuNCwxMi40LDhDMTAsMi44LDguNS0wLjEsOC4zLDAuMSAgIEM4LDAuMyw5LjcsNS42LDE0LDE3LjVjMS40LDMuOSwxLjksNS45LDEuNiw2LjFjLTAuMywwLjItMS4xLTEuMS0yLjMtMy41Yy0xLjQtMi44LTItMy45LTIuMi0zLjljLTAuMiwwLjEsMC4zLDEuOSwxLjIsNC41ICAgYzEuMyw0LjEsMy41LDExLjIsMy4xLDExLjVjLTAuMiwwLjEtMC45LTEtMi4zLTQuMWMtMC4zLTAuNy0wLjUtMS0wLjUtMWMwLDAtMC4xLDAuMS0wLjEsMC4zYzAsMC40LDAsNC42LDAsNC42bC0xLjYsMy4zaDcuNCAgIGMtMS45LTUuNS0yLjUtOC0yLjItOC4xYzAuNC0wLjIsMiwzLDQsOC4xYzEuOSwwLjksNC4zLDMuMiw1LjcsNC41YzAuMywwLjMsMC40LDAuMywwLjMsMEMyNC40LDM1LjgsMjIuMiwzMC41LDE5LjIsMjMuMXoiPjwvcGF0aD48L2c+PC9zdmc+"></a>.

## Backstory

Being a data enthusiast, I found the concept of Gold Efficiency mentioned in [<img src="https://static.wikia.nocookie.net/leagueoflegends/images/e/e6/Site-logo.png" width="17" height="17">](https://leagueoflegends.fandom.com/wiki/Gold_efficiency_(Wild_Rift)) highly intriguing. However, upon initial inspection, I noticed that the website contained a multitude of outdated and erroneous item data. Moreover, its disorganized layout made reading difficult, rendering it unsuitable for direct use.

After some time, I came across another website, [<img src="https://wr-meta.com/favicon.png" width="15" height="15">](https://wr-meta.com/items/), which drew me in with its sleek and elegant design, as well as its CSS style. Although it also suffered from the issue of outdated and inaccurate item data, I had an idea:

<p align="center"><img src="https://github.com/changchiyou/wildrift-gold-efficiency/assets/46549482/59cdaef3-638a-40cf-beb7-99d5a9360eda" style="width: 65%;"></p>

Merging the calculation **formula** from [<img src="https://static.wikia.nocookie.net/leagueoflegends/images/e/e6/Site-logo.png" width="17" height="17">](https://leagueoflegends.fandom.com/wiki/Gold_efficiency_(Wild_Rift)) with the **style** of [<img src="https://wr-meta.com/favicon.png" width="15" height="15">](https://wr-meta.com/items/), and **manually updating** the item data myself. Thus, this website was born out of this concept.

## Installation (for developer)

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

## Establish Gold Efficiency Page for the New Version

Taking the update from [5.1a](https://changchiyou.github.io/wildrift-gold-efficiency/5.1a/) to [5.1b](https://changchiyou.github.io/wildrift-gold-efficiency/5.1b/) as an example:

1. Copy [items_5_1a.yml](/_data/items_5_1a.yml) & [stats_5_1a.yml](/_data/stats_5_1a.yml) and rename to [items_5_1b.yml](/_data/items_5_1b.yml) & [stats_5_1b.yml](/_data/stats_5_1b.yml):
2. Manually update item data in [items_5_1b.yml](/_data/items_5_1b.yml) based on [WILD RIFT PATCH NOTES 5.1B - ITEMS](https://wildrift.leagueoflegends.com/en-us/news/game-updates/wild-rift-patch-notes-5-1b/#items):

    The field info of `items_[version].yml`:

    | Field       | Requirement | Description                                                                                                                                                                                                                                 |
    |-------------|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    |`amount`|no need|Generated by [data.py](/data.py)|
    |`category`|required|Determines where the item belongs to. For instance, set `category` as `PHYSICAL DAMAGE ITEMS` to make the item belong to [📌 Physical Damage Items](https://changchiyou.github.io/wildrift-gold-efficiency/5.1b/#PHYSICAL-DAMAGE-ITEMS).|
    |`cost`|required|The cost of the item.|
    |`formula`|no need|Generated by [data.py](/data.py)|
    |`image`|required|The image reference of the item.|
    |`name`|required|The name of the item. The notes in `()` would be extracted and rendered with different style (only allowed 1 `()` set exists).|
    |`stats`|required|The stats info of the item. Check more detail info in following sheet.|

    The fields info of `stats` field:

    | Field       | Requirement | Description                                                                                                                                                                                                                                 |
    |-------------|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    |`formula`|no need|Generated by [data.py](/data.py)|
    |`passive`|optional|The unique passive which give the item the stat.|
    |`ratio`|optional|The stat ratio which is calculated with `ref` ( and `ref_type`) to generate `value`|
    |`ref`|optional|The target base stat for `value`'s calculation|
    |`ref_type`|optional|The target stat from the item for `value`'s calculation|
    |`type`|required|The type of the stat|
    |`value`|required|The value of the stat|
    |`value`*|no need|Generated by [data.py](/data.py) (only if `ratio`&`ref` are set)*|

    Some example:

    1. Basic:
        https://github.com/changchiyou/wildrift-gold-efficiency/blob/aff35e946e6855a12d898505d38e846fad24df14/_data/items_5_1b.yml#L15-L34

    2. `ratio` & `ref`:
        https://github.com/changchiyou/wildrift-gold-efficiency/blob/aff35e946e6855a12d898505d38e846fad24df14/_data/items_5_1b.yml#L819-L836

    3. `ref_type`:
        https://github.com/changchiyou/wildrift-gold-efficiency/blob/aff35e946e6855a12d898505d38e846fad24df14/_data/items_5_1b.yml#L367-L386

3. Manually update [stats_5_1b.yml](/_data/stats_5_1b.yml):

    The fields info of `stats_[version].yml`:

    | Field       | Requirement | Description                                                                                                                                                                                                                                 |
    |-------------|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | `image`     | required    | The reference of the image.                                                                                                                                                                                                                 |
    | `base_type` | optional    | Determines where the statistic price belongs in [💰 Base Statistic Prices](https://changchiyou.github.io/wildrift-gold-efficiency/5.1b/#Base-Statistic-Prices). Set `first` for *First-tier Base Item* and set `second` for *Second-tier Base Item*. |
    | `base_item` | optional    | The item used as the basis for calculating the statistic price.                                                                                                                                                                             |
    | `type`      | required    | Determines the classification of the stat in the [🔎 Stat Filters](https://changchiyou.github.io/wildrift-gold-efficiency/5.1b/#stat-filters). Set `""` to exclude from filters.                                                            |

    Some examples:

    1. Basic:
        https://github.com/changchiyou/wildrift-gold-efficiency/blob/aff35e946e6855a12d898505d38e846fad24df14/_data/stats_5_1b.yml#L41-L45

    2. Excluded from statistic price calculation:
        https://github.com/changchiyou/wildrift-gold-efficiency/blob/aff35e946e6855a12d898505d38e846fad24df14/_data/stats_5_1b.yml#L61-L63

    3. Exclude from statistic price calculation and filters:
        https://github.com/changchiyou/wildrift-gold-efficiency/blob/aff35e946e6855a12d898505d38e846fad24df14/_data/stats_5_1b.yml#L88-L90

4. Install python dependencies:

    ```
    pip install -r requirements.txt
    ```

5. Execute [data.py](/data.py) to re-generate `amount` and `formula` in [items_5_1b.yml](/_data/items_5_1b.yml) based on step `2.`( Manually update item data in [items_5_1b.yml](/_data/items_5_1b.yml) ):
    ```
    python data.py -c --items items_5_1b.yml --stats stats_5_1b.yml
    ```

    > For more info of params, execute:
    > ```
    > python data.py -h
    > ```