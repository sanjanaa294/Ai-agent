class AgentState:
    def __init__(self, user_request):
        self.user_request = user_request
        self.plan = ""
        self.research = ""
        self.code = ""
        self.review = ""
        self.report = ""