# Do not modify these lines
__winc_id__ = "71dd124b4a6e4d268f5973db521394ee"
__human_name__ = "strings"

# Add your code after this line
scorer_one = "Ruud Gullit"
scorer_two = "Marco van Basten"
goal_0 = 32
goal_1 = 54
scorers = scorer_one + " " + str(goal_0) + ", " + scorer_two + " " + str(goal_1)
report = f"{scorer_one} scored in the {goal_0}nd minute\n\
{scorer_two} scored in the {goal_1}th minute"
print(scorers)
print(report)

# part two
player = "Gerald Vanenburg"
first_name = player[: player.find("d") + 1]
last_name = player[player.find("V") : len(player)]
last_name_len = len(last_name)
name_short = f"{player[0]}. {last_name}"
chant = " ".join([first_name + "!"] * len(first_name))
good_chant = chant[-1] != " "
