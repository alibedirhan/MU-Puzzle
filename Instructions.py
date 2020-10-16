print(""" The MU game is based on the MU puzzle described in
 Godel, Escher, Bach: An Eternal Golden Braid by Douglas R. Hofstadter

 The main idea is reach the target string MU string.
 The starting string will be MI. After that, some rules for changing the series will be told.
 If one of those rules is applicable at some point, and you want to use it, you may,
 but there is nothing that will dictate which rule you should use, in case there are several applicable rules.
 It’s up to you!

Rule-1: If you possess a string whose last letter is I, you can add on a U at the end.
       For example, MI and IM are two different strings.
       A string of symbols is not just a “bag” of symbols, in which the order doesn't make any difference.

Rule-2:  Suppose you have Mx. Then you may add Mxx to your collection. What I mean by this is shown below, in a few examples.
         From MIU, you may get MIUIU. ⟶ MIU, x = IU therefore; Mxx = MIUIU
         From MUM, you may get MUMUM. ⟶ MUM, x = UM therefore; Mxx = MUMUM
         From MU, you may get MUU. ⟶ MU, x = U therefore; Mxx = MUU

Rule-3: If III occurs in one of the strings in your collection, you may make a new string with U in place of III.
       Examples:
       From UMIIIMU, you could make UMUMU.
       From MIIII, you could make MIU (also MUI. From IIMII, you can’t get anywhere using this rule. The three I’s have to be consecutive.)
       From MIII, make MU. Don’t, under any circumstances, think you can run this rule backwards, as in the following example:
       From MU, make MIII < — This is wrong. Rules are one-way!

Rule-4: If UU occurs inside one of your strings, you can drop it.
       From UUU, get U.
       From MUUUIII, get MUIII.

There you have it. Now you may begin trying to make MU! """)
