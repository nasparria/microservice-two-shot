# Wardrobify

Team:

* Person 1 - Which microservice? Victoria Ziegler is doing hats
* Person 2 - Which microservice? Nicolas Asparria is doing Shoes

## Design

## Shoes microservice

The Shoes resource will be a microservice track its manufacturer (CharField), its name(CharField), its color(CharField), a URL for a picture(URLField), and the Bin(Foreing Key to the model location) in the wardrobe where it exists.


## Hats microservice

The Hat resource will be a microservice track its fabric (CharField), its style_name(CharField), its color(CharField), a URL for a picture(URLField), and the location(Foreing Key to the model location) in the wardrobe where it exists.
