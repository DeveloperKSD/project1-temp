"""External tools using Gemini API"""
import google.generativeai as genai

# PUT YOUR API KEY HERE
genai.configure(api_key='ENTER_API_KEY')

class TicketAnalyzer:
    def __init__(self):
        self.model = genai.GenerativeModel('ENTER_AI_NAME')
    
    def analyze(self, ticket, context):
        """Analyze ticket to find root cause"""
        prompt = f"""You are analyzing a support ticket during a headless e-commerce migration.

TICKET:
Merchant: {ticket['merchant_id']}
Issue: {ticket['description']}
Severity: {ticket['severity']}

CONTEXT FROM PAST ISSUES:
{context}

Identify the ROOT CAUSE from these categories:
- merchant_config_error
- platform_bug
- migration_issue
- documentation_gap
- api_misconfiguration

Respond in JSON:
{{
  "root_cause": "category",
  "reasoning": "brief explanation",
  "confidence": 0.0-1.0
}}"""
        
        response = self.model.generate_content(prompt)
        import json
        return json.loads(response.text.strip().replace('```json', '').replace('```', ''))

class ActionExecutor:
    def execute(self, decision):
        """Execute approved actions (simulation)"""
        print(f"✅ Executing: {decision['action']}")

        return {"status": "completed", "action": decision['action']}
