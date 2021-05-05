import copy
import random
# Consider using the modules imported above.

class Hat :

    def __init__(self, **arg) :
        self.contents = []
        for key, no in arg.items() :
            self.contents = self.contents + [key]*int(no)

    def draw(self, number_of_balls_to_draw) :
        if number_of_balls_to_draw>=self.contents.__len__() :
            return self.contents
    
        balls = []
        for _ in range(number_of_balls_to_draw) :
            balls.append(self.contents.pop(int(random.random() * len(self.contents))))
            if len(self.contents)==0 : break
        return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count_expected_balls = 0
    for _ in range(num_experiments) :
        expected_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        balls = hat_copy.draw(num_balls_drawn)
        for key in balls :
            if key in expected_copy :
                expected_copy[key]-=1
        
        if all(val<=0 for val in expected_copy.values()) :
            count_expected_balls+=1

    return (count_expected_balls/num_experiments)

# def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
#     count = 0
#     for _ in range(num_experiments):
#         expected_copy = copy.deepcopy(expected_balls)
#         hat_copy = copy.deepcopy(hat)
#         colors_gotten = hat_copy.draw(num_balls_drawn)
#         for color in colors_gotten:
#             if(color in expected_copy):
#                 expected_copy[color]-=1
        
#         if(all(x <= 0 for x in expected_copy.values())):
#             count += 1

#     # compare {green: 1, blue: 1} with ['green', 'blue'] 
#     return count / num_experiments