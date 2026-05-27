from crew import ComplianceCrew

def run_compliance_assistant(pergunta: str):
    # Initialize the ComplianceCrew
    crew_instance = ComplianceCrew()

    # Run the AI Compliance Assistant
    result = crew_instance.crew().kickoff(inputs={"pergunta": pergunta})

    return result