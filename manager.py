from components.call_api import call_gemini

class Manager:
    def  call_gemini(self,user_ideas , niche , memory):
        ideas = call_gemini(user_ideas , niche , memory)
        memory = open("Memory.json")[str(niche)] if str(niche) in open("Memory.json") else []
        memory.extend(ideas)
        return memory
    def generate_audio(self):
        pass

    def generate_video(self):
        pass

    def generate_script(self):
        pass

    async def startGeneration(self, user_ideas , niche):
        ########CONTENT GENERATION##########
        memory = open("Memory.json","r")[str(niche)] if str(niche) in open("Memory.json") else []
        new_memory = await self.call_gemini(user_ideas , niche , memory)
        with open("Memory.json","w") as file :
            file["niche"] = memory
        ####################################
    '''
      todo :
        add :
            call_openai() , call_ollama()
        getMore ideas to do
    '''