#parent class:
class Character:
    name = "Mario"
    special_ability1 = "Throw Hat"
    special_ability2 = "High Jump"

    def beatBowser(self):
        hero_name = input("Enter your character name: ")
        specialAbility = input("Enter \"Throw Hat\" or \"High Jump\":")
        if(specialAbility == self.special_ability1):
            print("{} Throws his hat deafeating Bowser and saving Princess Peach!".format(hero_name))
        elif(specialAbility == self.special_ability2):
            print("{} High Jumps at Bowser, but Bowser is too fast and runs away with the Princess!".format(hero_name))
        else:
            print("This Hero has no idea what they are doing, hopefully a worthy Hero with the ability to save the Princess comes along soon....")

#child class 1:

class Companion(Character):
    name = "Yoshi"
    heroType = "Sidekick"
    attack = "Throw Egg"
    love = "Lick"

    def beatBowser(self):
        hero_name = input("Enter your character name: ")
        attackLove = input("Enter \"Throw Egg\" or \"Lick\":")
        if(attackLove == self.attack):
            print("{} throws an egg deafeating Bowser, {} saves the day and runs off into the sunset with Mario and the Princess on his back!".format(hero_name,hero_name))
        elif(attackLove == self.love):
            print("{} licks Bowser. This enrages Bowser and he snatches up the Princess and climbs to the highest tower in the castle. The Princess is even further away now... ".format(hero_name))
        else:
            print("This Hero has no idea what they are doing, hopefully a worthy Hero with the ability to save the Princess comes along soon....")
    


#child class 2:

class Villian(Character):
    name = "Wario"
    villaniousDeed = "Trip"
    karma = "Burn"

    def beatBowser(self):
        hero_name = input("Enter your character name: ")
        influence = input("Enter \"Trip\" or \"Burn\":")
        if(influence == self.villaniousDeed):
            print("{} trips the hero, giving Bowser the upper hand! Bowser has given {} his word that he can marry the Princess' sister if {} helps successfully kidnap the Princess...".format(hero_name,hero_name,hero_name))
        elif(influence == self.karma):
            print("{} accidentally catches some of Bowsers fire breath on his butt! {} wont be able to sit for a week.".format(hero_name,hero_name))
        else:
            print("This villian has no idea what is going on, a hero is bound to rescue the Princess under this watch...")


player= Character()
player.beatBowser()

hero = Companion()
hero.beatBowser()

hero = Villian()
hero.beatBowser()
