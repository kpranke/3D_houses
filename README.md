# 3D House Project
## Table of Contents
1. [Description](#description)
1. [Objectives](#objectives)
	1. [Challenges](#challenges)
	2. [Limitations](#limiatations)
	3. [Further developments](#further-developments)
[About the Project](#about-the-project)
[Project Status](#project-status)
[Personal situation](#personal-situation)

## Description
This project is a part of the Becode.org AI Bootcamp programme. The goal is to produce a 3D plot of a house situated in Flanders, Belgium with only the address of the house provided.

![3d house model](https://media.istockphoto.com/photos/yellow-house-on-white-background-picture-id1288550827?k=20&m=1288550827&s=612x612&w=0&h=AuvniCc5aIn8OtwuaKdq4PQWe-1RT1v-m68JmtGwluQ=)

## Objectives

- to be able to search and implement new libraries
- to be able to read and use the [shapefile](https://en.wikipedia.org/wiki/Shapefile) format
- to be able to read and use geoTIFFs
- to be able to render a 3D plot
- to be able to present a final product

### Challenges

### Limitations

### Further Developments

## Repo Architecture

3D House Project

│
│   README.md      :explains the project
│   requirements.txt : lists libraries installed in the environment in which the project was created 
│   main.py        :Python script file with the add plotting a 3D Canopy Height Model of a house for the provided address in Flanders, Belgium.
│   retrieve_bounds.py : Python script file necessary to create a .csv file containing bounds of 43 GeoTIFF files storing geospatial information of the Flanders region of Belgium as well as links to the respective DSM and DTM files available in a zippped folders on the [Geopunt.be](https://www.geopunt.be/) website. 
│   DTM_bounds.csv  : a .csv file, which stores info containing bounds of 43 GeoTIFF files storing geospatial information of the Flanders region of Belgium as well as links to the respective DSM and DTM files available in a zippped folders on the [Geopunt.be](https://www.geopunt.be/) website.
│   
│   
│__   
│   utils         :directory contains all modules required to run the game
│   │
│   │ card.py      :Python script file with the Symbol and Card classes 
│   │
│   │ game.py      :Python script file with the Board class
│   │
│   │ player.py    :Python script file with the Player and Deck classes

## Installation

## Usage

`git clone` this repository into your local environment.
Run `terieve_bounds.py` file first.

## Visuals
![3d house model example](3DHouse_example.png)
## Timeline

## Personal situation

I am currently participating in the Becode.org AI Bootcamp to upskill into a career in data science.

**[Back to top](#table-of-contents)**