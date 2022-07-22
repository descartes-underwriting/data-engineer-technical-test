# Context

To price an insurance policy we need to assess the hazard at the client sites .

In this project, the risk of earthquakes will be evaluated. The list of historical earthquakes that occurred at or around the client sites can be used to estimate the average loss the client would have suffered (also called *EL*, for *expected loss*).

## Client sites

The coordinates of the client assets are given in the file [../input/locations.csv](../input/locations.csv):

| Location name       | Latitude | Longitude | Insured value  |
|---------------------|----------|-----------|----------------|
| Hotel California    | 34.03    | -118.15   | 12.000.000 USD |
| Californification   | 33.98    | -118.48   | 10.000.000 USD |
| California Dreamin' | 34.09    | -118.40   | 28.000.000 USD |

## Historical data

The data provider for historical earthquakes is the United States Geological Service (USGS). Data can be access with the following API:

<https://earthquake.usgs.gov/fdsnws/event/1/>

## Expected loss

The evaluation of the losses is described by a payout structure that is given in the file [../input/payout_structure.csv](../input/payout_structure.csv).

| Magnitude | Radius | Payout |
|-----------|--------|--------|
| 5.5       | 50 km  |  25 %  |
| 6.0       | 45 km  |  35 %  |
| 6.5       | 20 km  |  50 %  |
| 7.5       | 10 km  | 100 %  |

The first line of the payout structure reads the following way:

+ An earthquake of magnitude >= 5.5 occurring within 50 km of one of our client sites will trigger a payment of 25 % of that site insured value

In case a pair (earthquake, client site) matches on more than one line of the payout structure, the maximum payout is kept, e.g. an earthquake of magnitude 8.5 at 5 km from the "Hotel California" site would trigger all payouts (25%, 35%, 50% and 100%), and therefore will be attributed a payout of 100% (12.000.000 USD).

The metrics of interest to assess the expected losses are:

+ the loss per earthquake, which is the sum of the individual losses at each locations for a given earthquake
+ the loss per year, which is the sum of all losses for all locations occurring in a given year
+ the burning cost (or *BC*), which is the sum of the losses since a given year divided by the number of years,

  $$BC(1950) = \dfrac{1}{(2022 - 1950)+1} \sum_{year=1950}^{2022} losses(year)$$
+ the expected loss, which in our case is equal to the burning cost of 1900 e.g.: $EL = BC(1900)$
