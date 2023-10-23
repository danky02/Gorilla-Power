from typing import Callable, Any
from gorilla import GorillaPlugin

gorilla_says = [
    "Bananas make my day!",
    "I love swinging in the trees!",
    "Family time is the best time.",
    "Hugs and grooming = pure happiness!",
    "The sun on my fur feels amazing.",
    "Playing with friends is a blast!",
    "Nature's beauty surrounds us.",
    "Food, family, and forest – life is great!",
    "I'm a strong, happy gorilla!",
    "Rainforest adventures are the best adventures!",
    "Look at those tasty leaves!",
    "Swinging through the jungle is thrilling!",
    "Friends, fun, and food – what more could I want?",
    "Nature's beauty is awe-inspiring!",
    "I've got the best gorilla family ever!",
    "Jumping from branch to branch is a hoot!",
    "Belly laughs with my gorilla pals!",
    "Rolling in the grass is pure joy!",
    "Morning sunbeams warm my heart!",
    "Exploring the rainforest is an adventure!",
    "Napping in the shade is so peaceful!",
    "Banana breakfast – my favorite!",
    "No worries in the world!",
    "Feeling the breeze in my fur is delightful!",
    "Fruit feasts make me smile!",
    "Meeting new gorilla friends is exciting!",
    "Waterfall showers are refreshing!",
    "Treehouse hideouts are cozy!",
    "My heart beats to the jungle rhythm!",
    "Life is a jungle gym!",
    "Raindrops are like nature's music!",
    "Sharing a meal is heartwarming!",
    "The forest is full of surprises!",
    "I've got the best grooming buddies!",
    "Climbing high is thrilling!",
    "Roaring like a king of the jungle!",
    "Every day is an adventure!",
    "Nature's artwork is mesmerizing!",
    "Monkeying around is a blast!",
    "Sunsets in the canopy are breathtaking!",
]

import random

class Plugin(GorillaPlugin):
    name = "Gorilla Says"

    # PARSER OPTIONS
    suppress:bool = True
    copy_enable:bool = False
    paste_enable:bool = True
    
    def parser(self, text:str) -> str:
        index = random.randint(1, len(gorilla_says))-1
        return gorilla_says[index]