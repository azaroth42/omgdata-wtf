---
title: "OMG, Data... WTF? Egregious Errors in Cultural Heritage Data"
---


# Data Science and Data Engineering Group Therapy



## Latest Egregious Data Errors

* __Dates.__ We hate dates. No one can get them right. It's almost like you need a Ph.D. in History to understand how to format a date so that someone else can understand you. And then there's people being funny...
  ![Hopefully you DIAF](/images/2021-08-17-deathdate1.png)
  Strangely, even my reasonably clever series of date parsers fails to extract an actual death date for this lad.

* __Places.__ Places are great. We love places. They're hierarchical, they have lat/long coordinates for comparison, they're removed from dolphin. They're ... wait, they're what?
  ![Removed from Dataset](/images/2021-08-24-dolphin-place.png)
  Looking forwards to seeing what the [geocoder](https://github.com/pelias/placeholder) makes of "Removed from dolphin, California, USA"