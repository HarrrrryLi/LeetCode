First encoding skills. Suppose we have n required skills, we encoding them into integer, each bit represent one. Store this relation into a dict.(Using skill index as which bit represent which skill)

Next, initialize a dictionary called dp with key 0, value []

Then go through person list. For each person, convert his/her skills into integer. Then go through every item in dp, suppose we add current guy into the team, if skills of whole team don't change then continue. If it changes, update this new team if new skills set not in dp or this team has less people. 

Time Complexity O(people * 2 ^ skill) Space Complexit O(2 ^ skill)