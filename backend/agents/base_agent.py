from backend.core.llm import get_llm

from backend.agents.ResumeQAAgent import ResumeQAAgent
from backend.agents.ResumeImprovementAgent import ResumeImprovementAgent
from backend.agents.ResumeComparisonAgent import ResumeComparisonAgent
from backend.agents.interviewer_agent import InterviewerAgent
from backend.agents.resume_scoring_agent import ResumeScoringAgent
import os

class BaseAgent:
    """
    Central router that decides which router will handle the request
    """
    def __init__(self):
        self.llm = get_llm()
        self.resume_qa_agent = ResumeQAAgent()
        self.resume_improvement_agent = ResumeImprovementAgent()
        self.resume_comparison_agent = ResumeComparisonAgent()
        self.interviewer_agent = InterviewerAgent()
        self.resume_scoring_agent = ResumeScoringAgent()

    def detect_intent(self,question: str)  ->str:
        """
        Classify the intent using llm

        """
        prompt = f""" 
        
        You are an intent classification system.
        
        Classify the following user request into ONE of these intents:
        - resume_qa
        - resume_improvement
        - resume_comparison
        - interviewer
        - resume_scoring
        - general_chat

        User Request:
        "{question}"

        Respond with ONLY the intent name.
        """
        response = self.llm.invoke(prompt)
        return response.strip().lower()

    def handle_request(self,question: str,resume_id: str | None,role: str | None,compare_resume_id: str | None) -> dict:



      intent = self.detect_intent(question)
  
      INTENTS_REQUIRING_RESUME = {
          "resume_qa",
          "resume_improvement",
          "resume_comparison",
          "interviewer",
          "resume_scoring"
      }
  
      if intent in INTENTS_REQUIRING_RESUME and not resume_id:
          return {
              "intent": intent,
               "answer": "⚠️ Please upload a resume to use this feature."
          }
  
      if intent == "resume_qa":
          response = self.resume_qa_agent.run(resume_id, question)
  
      elif intent == "resume_improvement":
          response = self.resume_improvement_agent.run(resume_id,question)
  
      elif intent == "resume_comparison":


          role_prompt = f"""
          Extract the job role from the following user request.
          If no role is mentioned, respond with "null".

          User request:
          "{question}"

          Respond with ONLY the role name or "null".
          """
          role = self.llm.invoke(role_prompt).strip()

          response = self.resume_comparison_agent.run(resume_id,compare_resume_id,role)

      elif intent == "interviewer":
          response = self.interviewer_agent.evaluate(resume_id, role)

      elif intent == "resume_scoring":
           response = self.resume_scoring_agent.score(resume_id, role)

      else:
          response = self.llm.invoke(question)

      print("RAW INTENT RESPONSE:", repr(response))


      return {
        "intent": intent,
        "answer": response
      }
