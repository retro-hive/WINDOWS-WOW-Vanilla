Warrior
=======

Generating rage
---------------

As a warrior, you get two main sources of rage points.

Hitting
#######

| All your white hits will give you rage points.
| The formula for this is :math:`R = ((15 x d) / (4 x c)) + ((f x s) / 2) <= (15 x d) / c`
| ``d`` : ``D`` amage done
| ``c`` : ``C`` onversion score. This score equals to ``230.6`` at level 60.
| ``f`` : Hit ``F`` actor. It depends if you hit with main hand, off hand, and if you crit:
          * Main Hand
            * Normal hit = `3.5`
            * Critical hit = `7.0`
          * Off Hand
            * Normal hit = `1.75`
            * Critical hit = `3.5`
| ``s`` : Weapon ``S`` peed

Considering the above formula, it is obvious that you win more and more rage points
as you gear up and get DPS + Attack Power bonuses.

Receiving damage
################

| Each damage received will get you some rage points.
| The formula for this is :math:`R = (5/2) x (d/c)`
| ``d`` : ``D`` amage received.
| ``c`` : ``C`` onversion score. This score equals to ``230.6`` at level 60.

This means that the less damage you receive, the less rage you gain.
This is why going full protection might become a problem at some point :
  * You will gain less rage from hits received.
  * Your low offensive abilities will give you low rage points.


Generating threat
-----------------

From damage
###########

Threat is done through damage and buff effects.

A multiplier is applied depending on your stance:

  * Battle / Zerk : ``0.8``
  * Defense : ``1.30`` (you can get up to ``1.45`` with ``defiance`` talent)

Taking a ``1 000`` hit damage, we generate

  * Battle / Zerk : ``800`` threat
  * Defense : ``1 300`` threat (``1 450`` with ``defiance``)

From skills
###########

.. list-table::

  * - Skill
    - Rage cost
    - Threat
    - TPR
  * - `Revenge`_
    - 5
    - 355
    - 71
  * - `SunderArmor`_
    - 12-15
    - 260-299
    - 17-21
  * - `ShieldSlam`_
    - 20
    - 250 + Damage
    - 12.5-100
  * - `ShieldBash`_
    - 10
    - 180
    - 18
  * - `BattleShout`_
    - 10
    - 70 * Players in group
    - up to 35

.. _Revenge:     https://classic.wowhead.com/spell=25288/revenge
.. _SunderArmor: https://classic.wowhead.com/spell=11597/sunder-armor
.. _ShieldSlam:  https://classic.wowhead.com/spell=23925/shield-slam
.. _ShieldBash:  https://classic.wowhead.com/spell=1672/shield-bash
.. _BattleShout: https://classic.wowhead.com/spell=25289/battle-shout


.. toctree::
  :maxdepth: 2
  :titlesonly:
  :caption: Role
  :name: role

  warrior/tank
