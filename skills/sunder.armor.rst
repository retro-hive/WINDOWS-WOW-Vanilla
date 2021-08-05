.. _skill-sunder-armor:

============
Sunder Armor
============

| Sunder Armor is an armor debuff.
| It is often considered as a threat generation skill.
  In reality, it create very low threat, but will allow other skills to
  do much higher damage -> threat.

General informations
--------------------

+ Sunder armor cost 15 rage points.
+ It is an instant cast.
+ Each stack reduces target's armor by 450.
+ You can stack it 5 times, giving 2250 armor reduction.
+ You can improve Sunder Armor to cost 12 rage points (from protection tree).
+ You can improve Amount of threat by 15% from T1's 8/8 set (it will still be a bad threat tool).
+ You can apply Sunder armor on a target that already has 5 stacks,
  but only the threat points will apply.


Tips
----

+ Sunder Armor creates 260 threat for 15 rage points. This is a 17 ``TPR``
  skill, which is really low.
+ Sunder Armor is an essential skill to use to improve Raid's damage.
+ Sunder Armor as a ``GCD`` of 1.5s. It means 1 tank needs at least 7.5 seconds to apply 5 stacks,
  no matter its rage available.
+ | You should ask all your warriors (max 7) to make 1 Sunder Armor as opening skill.
  | This will allow your tank to save up to 75 rage points on real threat mecanisms,
    and help him to keep aggro on the fight.
+ | Most bosses in WoW have 3731 armor.
  | 5 stacks will lower their armor to :math:`3731 - 2250 = 1481`.
  | Coupling with ``Curse of Recklessness`` (``CoR`` 640 armor reduction) and
    ``Faerie Fire`` (``FF`` 505 armor reduction) will lead to :math:`3731 - (2250 + 640 + 505) = 336` armor left.

Damage reduction
----------------

| Let's see the damage reduction from armor points, with a unit having 3731 armor.
| Armor reduction is calculated using this formula : :math:`%reduction = armor / (armor + 5882.5)`

.. list-table::

  * - Debuffs
    - Armor
    - % reduction
  * - None
    - 3731
    - 38.8%
  * - 5 SA
    - 1481
    - 20%
  * - 5 SA + CoR
    - 841
    - 12%
  * - 5 SA + CoR + FF
    - 336
    - 5%

| It is essential to lower target's armor as much as possible to get a real boost on the raid.
| These debuffs are the very firsts to put on any target, to achieve really easier fights.
