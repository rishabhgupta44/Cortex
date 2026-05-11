# ---------------------------------------------------------------------------
# Copyright (c) 2019 Rishabh Gupta
# This file is part of the Rule-Based Cognitive Architecture project.
# Distributed under the MIT License. See the LICENSE file for details.
# ---------------------------------------------------------------------------

import os,json,time
HumanCollection =  json.load(open("HumanAlive.json"))
KilledCollection =  json.load(open("HumanDead.json"))
class HuamanIndex():
      def __init__(self,alive,dead):
          self.Human = alive
          self.dead = dead
      def KillPerson(self,name):
          Con = input("Is the person is murdered [Y/y]: ")
          if Con.lower()=="y":
             Murderer = input("Name of the person killed him: ")
          if Con.lower()!="y":
              Murderer = 0
          DeathReason = input("Reason of death: ")
          DeathDate = input("Date of death: ")
          if Con.lower() =="y":
              time.sleep(5)
              print(f"{name} is now dead")
          PersonDeath = {
              "Name":name,
              "Murderer":Murderer,
              "Reason":DeathReason,
              "Date":DeathDate
          }
          self.Human.remove(str(name))
          self.dead.append(PersonDeath)
          try:
             NewAliveList = json.dumps(self.Human)
             NewDeadList =  json.dumps(self.dead)
          except:
              pass
          with open("HumanAlive.json","w+") as HumanAlive:
               HumanAlive.write(NewAliveList)
          with open("HumanDead.json","w+") as HumanDead:
               HumanDead.write(NewDeadList)
          print("Mission Successful.")
      def IniExecuter(self):
            try:
               InputNameCollector = input("Name the person you want to kill: ")
               if InputNameCollector.lower() in self.Human:
                for x in self.Human:
                    if x.lower() == InputNameCollector.lower():
                        Conformation = input("Are you sure [Y/y]: ")
                        if Conformation.lower()=="y":
                            z = HuamanIndex(self.Human,self.dead)
                            z.KillPerson(x)
                        if Conformation.lower()!="y":
                            print("Mission Aborted")
               else:
                   print()
                   print("The person is not alive [ Mission Failed! ]")
                   print()
            except:
                print()
                print("Error! Unable to complete the mission.")
                print()
      def DeadLister(self):
          for DeadList in self.dead:
              print("#######################################")
              print()
              print(f"Name of the person dead: {DeadList['Name']}")
              if DeadList["Murderer"] == 0:
                  print(f"Dead due to natural cause")
              if DeadList['Murderer'] !=0:
                  print(f"The person was killed by {DeadList['Murderer']}")
              print(f"Reason of Death: {DeadList['Reason']}")
              print(f"Date of Death: {DeadList['Date']}")
              print()
              print("#######################################")
m = HuamanIndex(HumanCollection,KilledCollection)
m.IniExecuter()
m.DeadLister()