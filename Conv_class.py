from symptom_checker import getPredict


class medConv:

    questions=[
        "Do you have fever?",
        "Do you have dry cough?",
        "Do you have sore throat?",
        "Do you have hyper tension?",
        "Have you travelled abroad recently?",
        "Did you have contact with a covid patient?",
        "Have you recently attended a large gathering?",
        "Have you recently visited public exposed places?",
        "Do your family memebers work in public exposed places?"
    ]

    def __init__(self):
        # self.breathing_prob = 0
        # self.fever = 0
        # self.cough = 0
        # self.throat = 0
        # self.hyp_tension = 0
        # self.travel = 0
        # self.contact = 0
        # self.gathering = 0
        # self.public_place = 0
        # self.family_working = 0

        self.symptom_list = [0,0,0,0,0,0,0,0,0,0]

        self.conv_step = 0

        def getSymptom(self, inp):  #bolean input
            self.symptom_list[self.conv_step] = int(inp)
            self.conv_step += 1
            return self.questions[self.conv_step]

    



