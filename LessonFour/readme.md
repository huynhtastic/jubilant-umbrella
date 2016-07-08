# Lesson Four!
What we learned today:

  * Lists
  * Tuples
  * Sets
  * Dictionaries
  * Indexing and Slicing
  * Error Handling
  * Performance and Expense
  * Big O Notation and time complexity

# Homework Assignments
This homework took me a while to create... and it might take you longer to solve. So here's just one problem this week:

### 1. ...And Make it Double
Now that the registers are working and the people are getting in and out of HIB possibly faster than ever, you decide to turn your attention to the root cause: What happened to the registers' OS?

To get to the bottom of this, you follow Makash to the back to meet HIB's IT department. Surprisingly enough, you find out that HIB actually has a person with some experience in internet security, Arnold Drumf. Arnold tells you the registers were specifically targeted by an organized cyber-attack. He first noticed something was off when he experienced delays and frequent pauses while streaming his favorite UnderWatch Twitch streamer, B_Seagull. He has never experienced delays before, and after a little digging, he saw that there was a ton more inbound/outbound traffic than usual. With a little more investigation, he realized that someone had connected to the HIB internal network and was routing all of credit card transactions made at the registers to an offshore account instead of HIB's accounts receivables.

Almost immediately after realizing this, Arnold forkbombed the system, crashing the HIB network and cutting off the foreign connection. When the system rebooted, Arnold checked the network logs, but to his surprise, they were all jumbled. They all looked something in the form of:

e17n96o2i.C_@c4_:4n.2f2o51t7_m4o21r2n51_.

Among these files of jibberish, Arnold found a certain readme.txt:

--readme.txt--
```
By the time you see this, I'm probably a few dollars richer. Let's face it: it'll be a while before you can find me.

Let's play a game.

You're trying to find me, and I'm trying to find another genius to join me in my escapades. You figure this out, you can have your money back, and I can have another partner to have fun with. A win-win? We'll see.

You guys call me Lurk, The Lurker, whatever. Call me whatever you want. I'm a face with many names. But the word on the street is someone's already cracked my first cipher. If you're reading this, I know that person is you. If you aren't, then good luck.

Riddle 1:
You can see that your logs might look a little... vague. That might be an understatement. The point is, you cracked my first cipher, but that was easy. Now, prepare for trouble. And make it **DOUBLE**.

**HINT** **HINT**

Once you understand my first riddle, you'll know that you're missing two key words:
Riddle 2: (THIS ONE FIRST!)
Multiplies; but never breeds, Uses air; but never breathes.
Consumes much; will never eat, Often measured by its heat.

Riddle 3:
My name is short, yet my history long.
Once I was the greatest one, but now, all but my core is gone.
Known for might and buildings and art,
At last I fell, now stories they tell.
Who am I?
```

You're not sure what all of this means, but from the readme, you're sure that this is some sort of cipher (**HINT**). You assure Arnold that you will be able to crack these puzzles and find out what happened. Encouraged by your promises, he asks you to create two functions, encrypt and decrypt, that use the ciphering method that Lurk used to encipher these logs. He's put the logs into a encrypted_logs.txt file to help you in your development:

--encrypted_logs.txt--
```
e17n96o2i.C_@c4_:4n.2f2o51t7_m4o21r2n51_.
4_84e6_22e5o@7O_.d1:2225r1.p_P49n1:2.t12_
4_84e6_22e5o@7O_.d1:2225r1.p_P49n1:1.t12_
4_84e6_22e5o@7O_.d1:2225r1.p_P49n1:5.t12_
4_84e6_22e5o@7O_.d1:2285r1.p_P49n1:0.t12_
4846_15@7_._2251.12491:.22
4tm84it6_:i1aa5lB@7ee_.g__E_n22td5ee1.d_12hA49Re1:sm.vc22_N
4_1:1.e_S5c94o.n12k22@7N6_22t49w5a_.r1:
P_C_:__d4'5s._9r4n2o.l1_1-4-6A.
e2o5_H4d._1-02o7y.r___9x5P:_X2N4-R_4.
e1N.o0d._0o2x7y.r1-t-:P__s___T_e
M4_A4-_.SO4TR4EK_S.RN7EE2GT.R:_T1_E2-R5IW1__
Srf-H__LRl_Orc____Ere-IuIOe_E_a-C-t_GotS:e__:hLAb-L-oBBnP
4Fod1:mp1.l_.1_nr5eds94_ut.d_o_R/s22o/@7its6_ea12hh49:ox5aow_./c22ett
4o_o1:hh1.mod_smp5cea94dtt._ds12_ut22/c@7mnr6_o/22ats49n_.5p/s_.:ox1cow
4t94n36C.19o1n51_8_.t21n32:_95_1.o1.c844:@2i.6e._o2
4D1:1.S_O5P94L.N1222@7_6_22H49E5E_.L1E
4c.1:_1.i2_C45o.24:4.n212t22o@7t76_422o.59n15n1_._41e5
LO21:4_Ao2O:4SV22Mt1CD1LL72D4@_A.ER._O15M_4HE56_.1N_
e37n7n21_.C_@c46o2i.2f9o1_:8n.5o61r1t5_m
2cor44ne9..n__11etf44ot.21:r656_o7._Cu8724e.28.:34_1_4.14r5152n.4@5t_o1.i1m27o2_
4c@7o1.m32m5mg5_s.*/1_22_1:/6_l_ro09a04n_.d12:
r-iend_-mr_qaudi:erso_rrrt-i-geh
4o@7m1.m12_5ts5c/._32a22/1:l6_o1c09n14d_.:_dg
4mdd@2bdd1._dd19rdd1rddd4kddd6bdd31sdd2:edd1_sdd6fsdd.odd04udd45rdd_.pdd_oedd
e1t6ptS@m_a_2ty1:1r2S1us3_
```

To help you, it will be easier to learn how the cipher works, how to encipher using the ciphering method, then working your way backwards (with more research!).