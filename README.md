#### Structure
A hashmap mapping a card ID to the card's attributes.
`all.json` contains the entire card database.

This is the list of available fields:

```
name_         -> (str) Desert Pathfinder
id_           -> (int) 114031010
pp_           -> (int) 2
craft_        -> (str) Neutral
rarity_       -> (str) Gold
type_         -> (str) Follower
trait_        -> (str) Natura
expansion_    -> (str) Verdant Conflict
baseEffect_   -> (str) Last Words: If there are no allied Naterran Great Trees in play, summon a Naterran Great Tree.
baseFlair_    -> (str) Come, friend. You will cross the dunes safely on the wings of an angel.
What's that? My steed looks like no angel you've ever seen? But look there on his back! What else but wings would those two proud humps be?
rotation_     -> (bool) True
baseAtk_      -> (int) 2
baseDef_      -> (int) 2
evoAtk_       -> (int) 4
evoDef_       -> (int) 4
evoEffect_    -> (str) Evolve: Put a Naterran Great Tree into your hand.
Last Words: If there are no allied Naterran Great Trees in play, summon a Naterran Great Tree.
evoFlair_     -> (str) Fear not, friend, though you are beset by foes.
My steed is a demon who devours the desert itself. Behold his powerful jaws. Are these not the gnashing teeth of the maw of hell itself? Deterrent enough for any craven marauder.
tokens_       -> (list) [900012010]
alts_         -> (list) [712031010]
```

#### Notes
- Token and Promo cards have their `expansion_` field set to `Token`.
- The japanese database has an additional `cv_` field containing the name of the card's voice actor.
