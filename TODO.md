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
- [x] Une attaque possède un nom et des dégâts
- [x] Une attaque possède un type- [ ] Une attaque réduit les PV du Pokémon ciblé


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

## Refactoring — Responsabilité des attaques

- [x] Identifier la duplication entre `Pokemon.attack()` et `Battle.attack()`
- [x] Décider que `Battle` est responsable de l'orchestration des attaques
- [x] Supprimer le test devenu redondant de `Pokemon.attack()`
- [x] Supprimer `Pokemon.attack()`
- [x] Supprimer la dépendance de `Pokemon` envers `DamageStrategy`
- [x] Vérifier que tous les tests restent verts après le refactoring

## Météo

- [x] Définir les différentes météos
- [ ] Un combat peut avoir une météo
- [ ] Sous la pluie, les attaques WATER sont renforcées
- [ ] Sous la pluie, les attaques FIRE sont affaiblies
- [ ] Sous le soleil, les attaques FIRE sont renforcées
- [ ] Sous le soleil, les attaques WATER sont affaiblies
- [ ] Une météo neutre ne modifie pas les dégâts
- [ ] Combiner ultérieurement météo et efficacité des types