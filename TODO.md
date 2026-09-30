# TODO — Développement TDD

## Pokémon

- [ ] Un Pokémon commence avec tous ses points de vie
- [ ] Un Pokémon peut subir des dégâts
- [ ] Les points de vie d'un Pokémon ne peuvent pas descendre sous 0
- [ ] Un Pokémon peut être K.O.
- [ ] Un Pokémon peut récupérer des points de vie
- [ ] Les points de vie d'un Pokémon ne peuvent pas dépasser ses points de vie maximum

- [ ] Un Pokémon avec 0 PV est K.O.
- [ ] Un Pokémon avec des PV restants n'est pas K.O.

## Attaques

- [ ] Une attaque possède un nom et des dégâts
- [ ] Un Pokémon peut utiliser une attaque contre un autre Pokémon
- [ ] Une attaque réduit les PV du Pokémon ciblé


## Types

- [ ] Un Pokémon possède un type
- [ ] Une attaque possède un type
- [ ] Une attaque super efficace inflige deux fois plus de dégâts
- [ ] Une attaque sans avantage de type inflige ses dégâts normaux

## Stratégies de dégâts

- [x] Définir une interface abstraite `DamageStrategy`

- [x] Une stratégie de dégâts définit une méthode `calculate()`

- [x] `DamageStrategy` ne peut pas être instanciée directement

- [x] `SimpleDamageStrategy` utilise les dégâts de base de l'attaque

- [x] `TypeDamageStrategy` prend en compte le type de l'attaque et du défenseur

- [x] Les différentes stratégies de dégâts sont interchangeables

### Combat

- [x] Créer une classe `Battle`
- [x] Un combat possède une stratégie de calcul des dégâts
- [x] Un Pokémon peut attaquer un adversaire pendant un combat
- [x] Le combat utilise sa stratégie pour calculer les dégâts
- [x] Les dégâts calculés sont appliqués au Pokémon défenseur