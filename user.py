
class User:
    def __init__(self,first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

def display_info(self):
        print(self.first_name,"\n",self.last_name,"\n",self.email,sep="") 
        print(self.age,"\n", self.is_rewards_member,"\n", self.gold_card_points, sep="")

jone = User("Jone","doe","jone@email.com",55)
display_info(jone)

def enroll(self):
    if self.is_rewards_member is False:
        self.is_rewards_member = True
        self.gold_card_points = 200
    else:
        print("your already registered")

enroll(jone)
enroll(jone)
def spend_points(self,points):
    if self.gold_card_points < points:
        print("you don't have enough points to spend")
    else:
        self.gold_card_points -= points

spend_points(jone,50)

billy = User("Billy","The-kid","kidbilly354@email.com",35)
enroll(billy)
spend_points(billy,80)

tim = User("Tim","Purtin","timp@gmail.com",20)
spend_points(tim,40)

