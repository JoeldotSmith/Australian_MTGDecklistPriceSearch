# MTG Decklist Price Search

Search for Magic: The Gathering card prices across multiple Australian (and international) vendors from the command line, then calculate the optimal split order to minimise total cost including postage.

**Vendors supported:**
- [Good Games TCG](https://tcg.goodgames.com.au/) — AUD, $6.50 postage
- [MTGMate](https://www.mtgmate.com.au/) — AUD, $6.00 postage
- [Card Kingdom](https://www.cardkingdom.com/) — USD (auto-converted to AUD), ~$10.50 USD postage

## Requirements

No dependencies required other than Python 3 (tested on Python 3.13, should work on most modern versions).

## Setup

Paste your decklist into `decklist.txt`, one card per line in the format:
``` text
1 Octavia, Living Thesis
1 Chart a Course
1 Curate
1 Deep Analysis
1 Defy Gravity
1 Gigadrowse
1 Illvoi Galeblade
```

## Usage

```bash
python3 main.py
```
## Flags

### `--filter-price`
Only show cards cheaper than the given price in the main table. Cards at or above the threshold are moved to a "Filtered Out" table.

```bash
python3 main.py --filter-price 5
```

### `--filter-diff`
Only show cards where the difference between the cheapest available price and the cheapest NM price (regardless of stock) is less than the given value. Useful for spotting cards where the only available copy is an expensive variant or damaged copy.

```bash
python3 main.py --filter-diff 1.50
```

### `--ignore-vendor`
Exclude one or more vendors from the search entirely. Accepts `ck` (Card Kingdom), `gg` (Good Games), and `mm` (MTGMate). Ignored vendors are skipped at the network level and excluded from price comparison and optimal order calculation.
```bash
python3 main.py --ignore-vendor ck
python3 main.py --ignore-vendor ck gg
```

Filters can be combined:

```bash
python3 main.py --filter-price 10 --filter-diff 2
```

### `--open`
Open the product page for each card in the main (non-filtered) table in your browser. Uses the winning vendor's URL.

```bash
python3 main.py --open
```

> **Warning:** This opens one browser tab per card. For large decklists this can open 50+ tabs.

## Example Output

``` text

Total cards: 51

  [CardKingdom] Fetching 51 cards (bulk)...   [CardKingdom] USD→AUD rate: 1.4197 ✓  (51 found)

  [GoodGames] Searching: Octavia, Living Thesis... ✓
  [GoodGames] Searching: Chart a Course... ✓
  [GoodGames] Searching: Curate... ✓
  [GoodGames] Searching: Deep Analysis... ✓
  [GoodGames] Searching: Defy Gravity... ✓
  [GoodGames] Searching: Gigadrowse... not found
  [GoodGames] Searching: Illvoi Galeblade... ✓
  [GoodGames] Searching: Impulse... ✓
  [GoodGames] Searching: Moment of Truth... ✓
  [GoodGames] Searching: Obsessive Search... ✓
  [GoodGames] Searching: Sleight of Hand... ✓
  [GoodGames] Searching: Spectral Sailor... ✓
  [GoodGames] Searching: Spyglass Siren... ✓
  [GoodGames] Searching: Strategic Planning... ✓
  [GoodGames] Searching: Treasure Cruise... ✓
  [GoodGames] Searching: Fact or Fiction... ✓
  [GoodGames] Searching: Reservoir Kraken... ✓
  [GoodGames] Searching: Kiora, the Rising Tide... not found
  [GoodGames] Searching: Nadir Kraken... not found
  [GoodGames] Searching: Redirect... ✓
  [GoodGames] Searching: Mission Briefing... ✓
  [GoodGames] Searching: Otherworldly Gaze... ✓
  [GoodGames] Searching: Shoreline Looter... not found
  [GoodGames] Searching: Thieving Skydiver... ✓
  [GoodGames] Searching: Traverse Eternity... not found
  [GoodGames] Searching: Cloud of Faeries... ✓
  [GoodGames] Searching: Consider... ✓
  [GoodGames] Searching: Talrand, Sky Summoner... ✓
  [GoodGames] Searching: Enter the Enigma... not found
  [GoodGames] Searching: Peek... ✓
  [GoodGames] Searching: Thought Scour... not found
  [GoodGames] Searching: Whelming Wave... ✓
  [GoodGames] Searching: Artful Dodge... not found
  [GoodGames] Searching: Rapid Hybridization... not found
  [GoodGames] Searching: Serum Visions... ✓
  [GoodGames] Searching: Frantic Search... not found
  [GoodGames] Searching: High Tide... ✓
  [GoodGames] Searching: Leap... ✓
  [GoodGames] Searching: Preordain... ✓
  [GoodGames] Searching: Wavebreak Hippocamp... not found
  [GoodGames] Searching: Archmage Emeritus... ✓
  [GoodGames] Searching: Quiet Speculation... not found
  [GoodGames] Searching: Brainstorm... ✓
  [GoodGames] Searching: Careful Study... ✓
  [GoodGames] Searching: Ghostly Pilferer... ✓
  [GoodGames] Searching: Shadow Rift... not found
  [GoodGames] Searching: Pongify... ✓
  [GoodGames] Searching: Ponder... ✓
  [GoodGames] Searching: Flow State... not found
  [GoodGames] Searching: Malcolm, Alluring Scoundrel... not found
  [GoodGames] Searching: Archmage of Runes... ✓

  [MTGMate] Fetching 51 cards (bulk)... ✓  (42 found)

┌                                                             MTG Card Price Search — GoodGames + MTGMate (51/51 cards)                                                              ┐
├───────────────────────────────┬──────────────────────────────────────────────┬─────────────────────┬───────┬──────────────────────┬───────────────┬───────────┬────────────────────┤
│ Card Title                    │ Set                                          │ Condition           │ Qty   │ Cheapest Available   │ Cheapest NM   │ Diff      │             Source │
├───────────────────────────────┼──────────────────────────────────────────────┼─────────────────────┼───────┼──────────────────────┼───────────────┼───────────┼────────────────────┤
│ Gigadrowse                    │ Guildpact                                    │ Lightly Played      │ 11    │ $0.40                │ $0.50         │ -$0.10    │        cardkingdom │
│ Illvoi Galeblade              │ Edge of Eternities                           │ Lightly Played      │ 2     │ $0.40                │ $0.50         │ -$0.10    │   cardkingdom (+2) │
│ Obsessive Search              │ Torment                                      │ Lightly Played      │ 6     │ $0.40                │ $0.50         │ -$0.10    │   cardkingdom (+2) │
│ Chart a Course                │ Ixalan                                       │ Lightly Played      │ 1     │ $0.44                │ $0.80         │ -$0.36    │   cardkingdom (+2) │
│ Defy Gravity                  │ Judgment                                     │ Lightly Played      │ 7     │ $0.44                │ $0.50         │ -$0.06    │   cardkingdom (+1) │
│ Curate                        │ Strixhaven: School of Mages                  │ Near Mint           │ 9     │ $0.50                │ $0.50         │ +$0.00    │     goodgames (+2) │
│ Deep Analysis                 │ Dominaria Remastered                         │ Near Mint           │ 10    │ $0.50                │ $0.40         │ +$0.10    │     goodgames (+2) │
│ Impulse                       │ Dominaria Remastered                         │ Near Mint           │ 15    │ $0.50                │ $0.50         │ +$0.00    │     goodgames (+2) │
│ Moment of Truth               │ March of the Machine                         │ Near Mint           │ 4     │ $0.50                │ $0.50         │ +$0.00    │     goodgames (+2) │
│ Sleight of Hand               │ Ninth Edition                                │ Moderately Played   │ 1     │ $0.50                │ $0.50         │ +$0.00    │     goodgames (+2) │
│ Spectral Sailor               │ Core Set 2020                                │ Near Mint           │ 8     │ $0.50                │ $0.80         │ -$0.30    │   cardkingdom (+2) │
│ Spyglass Siren                │ The Lost Caverns of Ixalan                   │ Near Mint           │ 74    │ $0.50                │ $0.80         │ -$0.30    │   cardkingdom (+2) │
│ Strategic Planning            │ Commander Legends                            │ Near Mint           │ 7     │ $0.50                │ $0.50         │ +$0.00    │     goodgames (+2) │
│ Treasure Cruise               │ Khans of Tarkir                              │ Near Mint           │ 106   │ $0.50                │ $0.50         │ +$0.00    │   cardkingdom (+2) │
│ Cloud of Faeries              │ Dominaria Remastered                         │ Near Mint           │ 13    │ $0.50                │ $0.50         │ +$0.00    │     goodgames (+2) │
│ Daring Leap                   │ Planeshift                                   │ Near Mint           │ 16    │ $0.50                │ $0.50         │ +$0.00    │     goodgames (+1) │
│ Fact or Fiction               │ Commander 2015                               │ Lightly Played      │ 1     │ $0.55                │ $0.80         │ -$0.25    │   cardkingdom (+2) │
│ Redirect                      │ 2012 Core Set                                │ Lightly Played      │ 2     │ $0.55                │ $1.50         │ -$0.95    │   cardkingdom (+2) │
│ Reservoir Kraken              │ Promo Pack                                   │ Near Mint           │ 8     │ $0.70                │ $1.50         │ -$0.80    │   cardkingdom (+2) │
│ Nadir Kraken                  │ Promo Pack                                   │ Lightly Played      │ 2     │ $0.78                │ $1.50         │ -$0.72    │        cardkingdom │
│ Otherworldly Gaze             │ Innistrad: Midnight Hunt                     │ Lightly Played      │ 2     │ $0.78                │ $0.50         │ +$0.28    │   cardkingdom (+2) │
│ Careful Consideration         │ Time Spiral                                  │ Near Mint           │ 10    │ $0.80                │ $0.80         │ +$0.00    │     goodgames (+2) │
│ Kiora, the Rising Tide        │ Foundations                                  │ Near Mint           │ 44    │ $0.84                │ $1.50         │ -$0.66    │   cardkingdom (+1) │
│ Mission Briefing              │ Guilds of Ravnica                            │ Near Mint           │ 17    │ $0.98                │ $1.50         │ -$0.52    │   cardkingdom (+2) │
│ Shoreline Looter              │ Bloomburrow                                  │ Near Mint           │ 65    │ $0.98                │ $0.80         │ +$0.18    │   cardkingdom (+1) │
│ Thieving Skydiver             │ The Lost Caverns of Ixalan Commander Decks   │ Near Mint           │ 35    │ $0.98                │ $1.50         │ -$0.52    │   cardkingdom (+2) │
│ Traverse Eternity             │ Universes Beyond: Doctor Who                 │ Near Mint           │ 13    │ $0.98                │ $1.50         │ -$0.52    │   cardkingdom (+1) │
│ Talrand, Sky Summoner         │ Commander 2020                               │ Near Mint           │ 25    │ $1.12                │ $1.50         │ -$0.38    │   cardkingdom (+2) │
│ Whelming Wave                 │ Born of the Gods                             │ Lightly Played      │ 20    │ $1.12                │ $1.50         │ -$0.38    │   cardkingdom (+2) │
│ Enter the Enigma              │ Duskmourn: House of Horror                   │ Near Mint           │ 132   │ $1.41                │ $0.80         │ +$0.61    │   cardkingdom (+1) │
│ Peek                          │ 10th Edition                                 │ Near Mint           │ 5     │ $1.41                │ $0.70         │ +$0.71    │   cardkingdom (+2) │
│ Thought Scour                 │ Iconic Masters                               │ Near Mint           │ 1     │ $1.41                │ $0.80         │ +$0.61    │   cardkingdom (+1) │
│ Artful Dodge                  │ Dark Ascension                               │ Lightly Played      │ 40    │ $1.46                │ $1.10         │ +$0.36    │        cardkingdom │
│ Octavia, Living Thesis        │ Commander 2021                               │ Near Mint           │ 1     │ $1.50                │ $1.50         │ +$0.00    │     goodgames (+2) │
│ Serum Visions                 │ Fifth Dawn                                   │ Lightly Played      │ 16    │ $1.69                │ $2.00         │ -$0.31    │   cardkingdom (+2) │
│ High Tide                     │ Fallen Empires                               │ Lightly Played      │ 30    │ $1.69                │ $1.80         │ -$0.11    │   cardkingdom (+2) │
│ Preordain                     │ 2011 Core Set                                │ Lightly Played      │ 84    │ $1.69                │ $1.00         │ +$0.69    │   cardkingdom (+2) │
│ Rapid Hybridization           │ Bloomburrow Commander Decks                  │ Near Mint           │ 142   │ $1.83                │ $1.10         │ +$0.73    │        cardkingdom │
│ Frantic Search                │ Commander 2020                               │ Near Mint           │ 4     │ $2.12                │ $1.00         │ +$1.12    │   cardkingdom (+1) │
│ Wavebreak Hippocamp           │ Foundations Jumpstart                        │ Near Mint           │ 32    │ $2.12                │ $1.50         │ +$0.62    │   cardkingdom (+1) │
│ Quiet Speculation             │ Eternal Masters                              │ Lightly Played      │ 13    │ $2.26                │ $0.80         │ +$1.46    │        cardkingdom │
│ Archmage Emeritus             │ Final Fantasy Commander Decks                │ Near Mint           │ 193   │ $2.83                │ $1.50         │ +$1.33    │   cardkingdom (+2) │
│ Careful Study                 │ Odyssey                                      │ Moderately Played   │ 9     │ $2.97                │ $6.70         │ -$3.73    │   cardkingdom (+1) │
│ Shadow Rift                   │ Tempest                                      │ Moderately Played   │ 3     │ $2.97                │ N/A           │ +$0.00    │        cardkingdom │
│ Ghostly Pilferer              │ Streets of New Capenna Commander Decks       │ Lightly Played      │ 1     │ $3.17                │ $4.20         │ -$1.03    │   cardkingdom (+2) │
│ Brainstorm                    │ 5th Edition                                  │ Lightly Played      │ 21    │ $3.39                │ $3.70         │ -$0.31    │   cardkingdom (+2) │
│ Pongify                       │ Mystery Booster/The List                     │ Near Mint           │ 11    │ $4.24                │ $3.70         │ +$0.54    │   cardkingdom (+2) │
│ Ponder                        │ 2010 Core Set                                │ Lightly Played      │ 31    │ $5.10                │ $21.30        │ -$16.20   │   cardkingdom (+2) │
│ Flow State                    │ Secrets of Strixhaven                        │ Near Mint           │ 772   │ $5.66                │ $5.40         │ +$0.26    │   cardkingdom (+1) │
│ Malcolm, Alluring Scoundrel   │ Promo Pack                                   │ Near Mint           │ 8     │ $5.66                │ $6.40         │ -$0.74    │   cardkingdom (+1) │
│ Archmage of Runes             │ Foundations                                  │ Near Mint           │ 1     │ $6.20                │ $6.20         │ +$0.00    │     goodgames (+2) │
├───────────────────────────────┼──────────────────────────────────────────────┼─────────────────────┼───────┼──────────────────────┼───────────────┼───────────┼────────────────────┤
│                               │                                              │                     │ Total │ $81.52               │ $98.40        │           │                    │
└───────────────────────────────┴──────────────────────────────────────────────┴─────────────────────┴───────┴──────────────────────┴───────────────┴───────────┴────────────────────┘

════════════════════════════════════════════════════════════
  OPTIMAL ORDER  —  total incl. postage: $100.56
════════════════════════════════════════════════════════════

┌                                           Order from Cardkingdom (51 cards)                                           ┐
├───────────────────────────────┬──────────────────────────────────────────────┬─────────────────────┬────────┬─────────┤
│ Card Title                    │ Set                                          │ Condition           │ Qty    │   Price │
├───────────────────────────────┼──────────────────────────────────────────────┼─────────────────────┼────────┼─────────┤
│ Obsessive Search              │ Torment                                      │ Lightly Played      │ 6      │   $0.40 │
│ Gigadrowse                    │ Guildpact                                    │ Lightly Played      │ 11     │   $0.40 │
│ Illvoi Galeblade              │ Edge of Eternities                           │ Lightly Played      │ 2      │   $0.40 │
│ Chart a Course                │ Ixalan                                       │ Lightly Played      │ 1      │   $0.44 │
│ Defy Gravity                  │ Judgment                                     │ Lightly Played      │ 7      │   $0.44 │
│ Spyglass Siren                │ The Lost Caverns of Ixalan                   │ Near Mint           │ 74     │   $0.50 │
│ Spectral Sailor               │ Core Set 2020                                │ Near Mint           │ 8      │   $0.50 │
│ Impulse                       │ Battlebond                                   │ Near Mint           │ 15     │   $0.50 │
│ Deep Analysis                 │ Commander 2019                               │ Near Mint           │ 15     │   $0.50 │
│ Strategic Planning            │ Commander 2013                               │ Near Mint           │ 8      │   $0.50 │
│ Sleight of Hand               │ Secrets of Strixhaven Mystical Archive       │ Near Mint           │ 2029   │   $0.50 │
│ Treasure Cruise               │ Khans of Tarkir                              │ Near Mint           │ 106    │   $0.50 │
│ Moment of Truth               │ March of the Machine                         │ Near Mint           │ 34     │   $0.50 │
│ Curate                        │ Strixhaven: School of Mages                  │ Near Mint           │ 42     │   $0.50 │
│ Fact or Fiction               │ Commander 2015                               │ Lightly Played      │ 1      │   $0.55 │
│ Redirect                      │ 2012 Core Set                                │ Lightly Played      │ 2      │   $0.55 │
│ Reservoir Kraken              │ Promo Pack                                   │ Near Mint           │ 8      │   $0.70 │
│ Otherworldly Gaze             │ Innistrad: Midnight Hunt                     │ Lightly Played      │ 2      │   $0.78 │
│ Nadir Kraken                  │ Promo Pack                                   │ Lightly Played      │ 2      │   $0.78 │
│ Kiora, the Rising Tide        │ Foundations                                  │ Near Mint           │ 44     │   $0.84 │
│ Mission Briefing              │ Guilds of Ravnica                            │ Near Mint           │ 17     │   $0.98 │
│ Shoreline Looter              │ Bloomburrow                                  │ Near Mint           │ 65     │   $0.98 │
│ Thieving Skydiver             │ The Lost Caverns of Ixalan Commander Decks   │ Near Mint           │ 35     │   $0.98 │
│ Traverse Eternity             │ Universes Beyond: Doctor Who                 │ Near Mint           │ 13     │   $0.98 │
│ Cloud of Faeries              │ Dominaria Remastered                         │ Near Mint           │ 51     │   $1.12 │
│ Whelming Wave                 │ Born of the Gods                             │ Lightly Played      │ 20     │   $1.12 │
│ Consider                      │ Innistrad: Midnight Hunt                     │ Lightly Played      │ 11     │   $1.12 │
│ Talrand, Sky Summoner         │ Commander 2020                               │ Near Mint           │ 25     │   $1.12 │
│ Thought Scour                 │ Iconic Masters                               │ Near Mint           │ 1      │   $1.41 │
│ Enter the Enigma              │ Duskmourn: House of Horror                   │ Near Mint           │ 132    │   $1.41 │
│ Peek                          │ 10th Edition                                 │ Near Mint           │ 5      │   $1.41 │
│ Artful Dodge                  │ Dark Ascension                               │ Lightly Played      │ 40     │   $1.46 │
│ Leap                          │ Stronghold                                   │ Moderately Played   │ 14     │   $1.48 │
│ Preordain                     │ 2011 Core Set                                │ Lightly Played      │ 84     │   $1.69 │
│ Serum Visions                 │ Fifth Dawn                                   │ Lightly Played      │ 16     │   $1.69 │
│ High Tide                     │ Fallen Empires                               │ Lightly Played      │ 30     │   $1.69 │
│ Rapid Hybridization           │ Bloomburrow Commander Decks                  │ Near Mint           │ 142    │   $1.83 │
│ Octavia, Living Thesis        │ Commander 2021                               │ Lightly Played      │ 1      │   $2.03 │
│ Frantic Search                │ Commander 2020                               │ Near Mint           │ 4      │   $2.12 │
│ Wavebreak Hippocamp           │ Foundations Jumpstart                        │ Near Mint           │ 32     │   $2.12 │
│ Quiet Speculation             │ Eternal Masters                              │ Lightly Played      │ 13     │   $2.26 │
│ Archmage Emeritus             │ Final Fantasy Commander Decks                │ Near Mint           │ 193    │   $2.83 │
│ Careful Study                 │ Odyssey                                      │ Moderately Played   │ 9      │   $2.97 │
│ Shadow Rift                   │ Tempest                                      │ Moderately Played   │ 3      │   $2.97 │
│ Ghostly Pilferer              │ Streets of New Capenna Commander Decks       │ Lightly Played      │ 1      │   $3.17 │
│ Brainstorm                    │ 5th Edition                                  │ Lightly Played      │ 21     │   $3.39 │
│ Pongify                       │ Mystery Booster/The List                     │ Near Mint           │ 11     │   $4.24 │
│ Ponder                        │ 2010 Core Set                                │ Lightly Played      │ 31     │   $5.10 │
│ Flow State                    │ Secrets of Strixhaven                        │ Near Mint           │ 772    │   $5.66 │
│ Malcolm, Alluring Scoundrel   │ Promo Pack                                   │ Near Mint           │ 8      │   $5.66 │
│ Archmage of Runes             │ Foundations                                  │ Near Mint           │ 152    │   $7.79 │
├───────────────────────────────┼──────────────────────────────────────────────┼─────────────────────┼────────┼─────────┤
│                               │                                              │                     │ Cards  │  $85.56 │
│                               │                                              │                     │ Post   │  $15.00 │
├───────────────────────────────┼──────────────────────────────────────────────┼─────────────────────┼────────┼─────────┤
│                               │                                              │                     │ Total  │ $100.56 │
└───────────────────────────────┴──────────────────────────────────────────────┴─────────────────────┴────────┴─────────┘
```


## Notes

- Card Kingdom prices are in USD and are converted to AUD at the live exchange rate fetched at runtime (falls back to 1.58 if the rate fetch fails).
- The optimal order calculation tries all combinations of vendors and picks the split that minimises total card cost plus postage. With three vendors this is 7 combinations; adding more vendors scales as `2^N - 1`.
- Cards filtered out by `--filter-price` or `--filter-diff`, and cards not found on any vendor, are excluded from the optimal order calculation.
- Good Games results are fetched one card at a time; MTGMate and Card Kingdom use a single bulk request each.
